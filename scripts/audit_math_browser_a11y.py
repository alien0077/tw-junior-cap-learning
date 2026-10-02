#!/usr/bin/env python3
"""axe-core accessibility audit scoped to math workbench and math production simulations."""
from __future__ import annotations

import argparse
import asyncio
import json
import os
from pathlib import Path
from urllib.parse import urlsplit

from playwright.async_api import async_playwright

ROOT = Path(__file__).resolve().parents[1]
MATH_UNITS = [
    "cur-math-content-a-7-1",
    "cur-math-content-a-7-2",
    "cur-math-content-a-7-7",
    "cur-math-content-a-7-8",
    "cur-math-content-a-8-1",
    "cur-math-content-a-8-4",
    "cur-math-content-f-8-2",
    "cur-math-content-d-8-1",
    "cur-math-content-s-9-1",
    "cur-math-content-s-9-13",
]


async def axe_scope(page, selector: str | None = None) -> dict:
    expression = """async (selector) => {
      const scope = selector ? document.querySelector(selector) : document;
      if (!scope) throw new Error('axe scope missing: ' + selector);
      const result = await axe.run(scope, { resultTypes: ['violations', 'incomplete'] });
      return { violations: result.violations, incomplete: result.incomplete };
    }"""
    return await page.evaluate(expression, selector)


async def run(url: str) -> dict:
    axe_source = (ROOT / "node_modules/axe-core/axe.min.js").read_text(encoding="utf-8")
    async with async_playwright() as playwright:
        executable_path = os.environ.get(
            "TW_A11Y_CHROME",
            "/Applications/Google Chrome.app/Contents/MacOS/Google Chrome",
        )
        launch_kwargs = {"headless": True}
        if Path(executable_path).is_file():
            launch_kwargs["executable_path"] = executable_path
        browser = await playwright.chromium.launch(**launch_kwargs)

        page = await browser.new_page(viewport={"width": 375, "height": 900})
        await page.goto(url, wait_until="networkidle")
        await page.add_script_tag(content=axe_source)
        runs: list[dict] = []
        for width in (320, 375, 768):
            await page.set_viewport_size({"width": width, "height": 900})
            for lesson_id in MATH_UNITS:
                await page.select_option("#unit", lesson_id)
                result = await axe_scope(page, "article.student-lesson-shell")
                runs.append({"surface": "workbench", "width": width, "lessonId": lesson_id, **result})

        parts = urlsplit(url)
        site = await browser.new_page(viewport={"width": 375, "height": 900})
        await site.goto(f"{parts.scheme}://{parts.netloc}/site/index.html", wait_until="networkidle")
        await site.add_script_tag(content=axe_source)

        for lesson_id, title in [
            ("lesson-math-content-a-7-8", "A-7-8：一元一次不等式的解與應用"),
            ("lesson-math-content-s-9-13", "S-9-13：表面積與體積"),
        ]:
            await site.locator("#search").fill(lesson_id)
            card = site.locator("#contentGrid article.card").filter(has=site.locator("h3", has_text=title))
            await card.wait_for()
            simulation_selector = f'[data-simulation-lesson^="{lesson_id}:"]'
            await card.locator(simulation_selector).wait_for()
            for width in (320, 375, 768):
                await site.set_viewport_size({"width": width, "height": 900})
                result = await axe_scope(site, simulation_selector)
                runs.append({"surface": "production", "width": width, "lessonId": lesson_id, **result})

        violations = [item for run in runs for item in run["violations"]]
        incomplete = [item for run in runs for item in run["incomplete"]]
        report = {
            "status": "passed" if not violations else "failed",
            "engine": "axe-core",
            "viewports": [320, 375, 768],
            "representativeMathUnits": MATH_UNITS,
            "productionMathUnits": ["lesson-math-content-a-7-8", "lesson-math-content-s-9-13"],
            "runs": len(runs),
            "violationCount": len(violations),
            "incompleteCount": len(incomplete),
            "violations": violations,
            "incomplete": incomplete,
            "scope": "automated math DOM accessibility rules; manual assistive-technology review remains separate",
        }
        await site.close()
        await page.close()
        await browser.close()
        return report


def main() -> int:
    parser = argparse.ArgumentParser()
    parser.add_argument("--url", default="http://127.0.0.1:8765/implementation/workbench.html")
    parser.add_argument("--report", default="implementation/reports/math-runtime-a11y-current.json")
    args = parser.parse_args()
    report = asyncio.run(run(args.url))
    output = Path(args.report)
    if not output.is_absolute():
        output = ROOT / output
    output.parent.mkdir(parents=True, exist_ok=True)
    output.write_text(json.dumps(report, ensure_ascii=False, indent=2) + "\n", encoding="utf-8")
    print(json.dumps({
        key: report[key]
        for key in ["status", "engine", "viewports", "runs", "violationCount", "incompleteCount"]
    }, ensure_ascii=False))
    return 0 if report["status"] == "passed" else 1


if __name__ == "__main__":
    raise SystemExit(main())
