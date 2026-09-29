#!/usr/bin/env python3
"""Run axe-core against representative real-browser workbench renders."""
from __future__ import annotations

import argparse
import asyncio
import json
import os
from pathlib import Path
from urllib.parse import urlsplit

from playwright.async_api import async_playwright

ROOT = Path(__file__).resolve().parents[1]
REPRESENTATIVE_UNITS = [
    "cur-chinese-content-a",
    "cur-english-content-a",
    "cur-math-content-a-7-2",
    "cur-math-content-a-7-1",
    "cur-math-content-a-7-7",
    "cur-math-content-a-7-8",
    "cur-math-content-a-8-1",
    "cur-math-content-a-8-4",
    "cur-math-content-s-9-1",
    "cur-math-content-s-9-13",
    "cur-math-content-d-8-1",
    "cur-science-content-bc-iv-3",
    "cur-science-content-ba-iv-3",
    "cur-science-content-db-iv-6",
    "cur-social-content-geo-af-iv-1",
    "cur-social-content-hist-qc-iv-2",
]


async def run(url: str) -> dict:
    axe_source = (ROOT / "node_modules/axe-core/axe.min.js").read_text(encoding="utf-8")
    async with async_playwright() as playwright:
        # macOS 上 bundled Chromium 可能因本機 sandbox／版本組合在 launch 時 SIGABRT；
        # 允許明確指定可用的系統 Chrome，避免把啟動器故障誤記成 accessibility failure。
        executable_path = os.environ.get(
            "TW_A11Y_CHROME",
            "/Applications/Google Chrome.app/Contents/MacOS/Google Chrome",
        )
        launch_kwargs = {"headless": True}
        if Path(executable_path).is_file():
            launch_kwargs["executable_path"] = executable_path
        else:
            launch_kwargs["channel"] = "chromium"
        browser = await playwright.chromium.launch(**launch_kwargs)
        page = await browser.new_page(viewport={"width": 375, "height": 900})
        await page.goto(url, wait_until="networkidle")
        await page.add_script_tag(content=axe_source)
        runs = []
        for width in (320, 375, 768):
            await page.set_viewport_size({"width": width, "height": 900})
            for lesson_id in REPRESENTATIVE_UNITS:
                await page.select_option("#unit", lesson_id)
                result = await page.evaluate("""async () => {
                  const result = await axe.run(document, { resultTypes: ['violations', 'incomplete'] });
                  return { violations: result.violations, incomplete: result.incomplete };
                }""")
                runs.append({"width": width, "lessonId": lesson_id, **result})
        parts = urlsplit(url)
        student_page = await browser.new_page(viewport={"width": 375, "height": 900})
        await student_page.goto(f"{parts.scheme}://{parts.netloc}/site/index.html", wait_until="networkidle")
        await student_page.add_script_tag(content=axe_source)
        await student_page.locator("#search").fill("lesson-math-content-s-9-13")
        card = student_page.locator("#contentGrid article.card").filter(
            has=student_page.locator("h3", has_text="S-9-13：表面積與體積")
        )
        simulation = card.locator('[data-simulation-lesson^="lesson-math-content-s-9-13:"]')
        await simulation.wait_for()
        await simulation.locator('[data-geometry-prediction="B"]').click()
        await simulation.locator('[data-geometry-action="submit-prediction"]').click()
        runtime_runs = []
        for width in (320, 375, 768):
            await student_page.set_viewport_size({"width": width, "height": 900})
            result = await student_page.evaluate("""async () => {
              const scope = document.querySelector('[data-simulation-lesson^="lesson-math-content-s-9-13:"]');
              const result = await axe.run(scope, { resultTypes: ['violations', 'incomplete'] });
              return { violations: result.violations, incomplete: result.incomplete };
            }""")
            runtime_runs.append({"width": width, "lessonId": "lesson-math-content-s-9-13", **result})
        runs.extend(runtime_runs)
        await student_page.close()
        violations = [item for run in runs for item in run["violations"]]
        incomplete = [item for run in runs for item in run["incomplete"]]
        report = {
            "status": "passed" if not violations else "failed",
            "engine": "axe-core",
            "viewports": [320, 375, 768],
            "representativeUnits": REPRESENTATIVE_UNITS,
            "runs": len(runs),
            "violationCount": len(violations),
            "incompleteCount": len(incomplete),
            "violations": violations,
            "incomplete": incomplete,
            "scope": "automated DOM accessibility rules; screen-reader semantics and content/pedagogical review remain separate",
        }
        await browser.close()
        return report


def main() -> int:
    parser = argparse.ArgumentParser()
    parser.add_argument("--url", default="http://127.0.0.1:8765/implementation/workbench.html")
    parser.add_argument("--report", default="implementation/reports/browser-a11y.json")
    args = parser.parse_args()
    report = asyncio.run(run(args.url))
    output = Path(args.report)
    if not output.is_absolute():
        output = ROOT / output
    output.parent.mkdir(parents=True, exist_ok=True)
    output.write_text(json.dumps(report, ensure_ascii=False, indent=2) + "\n", encoding="utf-8")
    print(json.dumps({key: report[key] for key in ["status", "engine", "viewports", "representativeUnits", "runs", "violationCount", "incompleteCount"]}, ensure_ascii=False))
    return 0 if report["status"] == "passed" else 1


if __name__ == "__main__":
    raise SystemExit(main())
