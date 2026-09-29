#!/usr/bin/env python3
"""Real-browser acceptance for Fc-IV-1 scale-boundary model and local fallback."""
from __future__ import annotations

import argparse
import json
import os
from pathlib import Path

from playwright.sync_api import sync_playwright


ROOT = Path(__file__).resolve().parents[1]
LESSON = json.loads((ROOT / "lessons/science/lesson-science-content-fc-iv-1.json").read_text(encoding="utf-8"))
AXE_SOURCE = (ROOT / "node_modules/axe-core/axe.min.js").read_text(encoding="utf-8")


def main() -> int:
    parser = argparse.ArgumentParser()
    parser.add_argument("--url", default="http://127.0.0.1:8765/site/index.html")
    args = parser.parse_args()
    chrome = Path(os.environ.get("TW_BROWSER_CHROME", "/Applications/Google Chrome.app/Contents/MacOS/Google Chrome"))
    errors: list[str] = []
    blocked: list[str] = []
    with sync_playwright() as playwright:
        launch = {"headless": True}
        if chrome.is_file():
            launch["executable_path"] = str(chrome)
        browser = playwright.chromium.launch(**launch)
        page = browser.new_page(viewport={"width": 375, "height": 900})

        def local_only(route):
            if route.request.url.startswith(("http://127.0.0.1:8765/", "http://localhost:8765/")):
                route.continue_()
            else:
                blocked.append(route.request.url)
                route.abort()

        page.route("**/*", local_only)
        page.on("pageerror", lambda error: errors.append(str(error)))
        page.goto(args.url, wait_until="networkidle")
        page.get_by_label("搜尋我們的教材或題目").fill("Fc-Ⅳ-1")
        card = page.locator(".card").filter(has_text="生物圈的生態系與組成層次").first
        card.wait_for()
        sections = card.locator(".lesson-sections article")
        section_texts = sections.all_inner_texts()
        authored_headings = [item["heading"] for item in LESSON["teaching"]["body"]]
        assert len(section_texts) >= len(authored_headings), section_texts
        assert [item.split("\n", 1)[0] for item in section_texts[-len(authored_headings):]] == authored_headings

        model = card.locator(".sim-ecosystem-scale")
        assert model.count() == 1
        assert model.locator('[aria-live="polite"][aria-atomic="true"]').count() == 1
        population = model.locator('[data-eco-scale="population"]')
        population.focus()
        page.keyboard.press("Enter")
        assert population.get_attribute("aria-pressed") == "true"
        assert "12隻同種青蛙" in model.locator(".sim-eco-evidence").inner_text()
        assert page.evaluate("document.activeElement.dataset.ecoScale") == "population"
        ecosystem = model.locator('[data-eco-scale="ecosystem"]')
        ecosystem.click()
        assert "生物群集" in model.locator(".sim-eco-evidence").inner_text()
        shore = model.locator('[data-eco-site="shore"]')
        shore.click()
        assert "潮間帶" in model.locator(".sim-eco-evidence").inner_text()
        assert "潮汐、鹽度" in model.locator(".sim-eco-evidence").inner_text()
        biosphere = model.locator('[data-eco-scale="biosphere"]')
        biosphere.click()
        assert "單一潮間帶樣區不能代表全部" in model.locator(".sim-eco-evidence").inner_text()

        steps = card.locator(".activity-step")
        assert steps.count() == len(LESSON["interactive"]["steps"]) == 4
        for index, item in enumerate(LESSON["interactive"]["steps"]):
            step = steps.nth(index)
            answer = item["answer"]
            answer_ids = [chr(ord("A") + option_index) for option_index in range(len(item["options"]))]
            wrong = next(option_id for option_id in answer_ids if option_id != answer)
            wrong_button = step.locator(f'[data-answer="{wrong}"]')
            wrong_button.focus()
            page.keyboard.press("Enter")
            assert item["retryHint"] in step.locator(".feedback").inner_text()
            correct_button = step.locator(f'[data-answer="{answer}"]')
            correct_button.focus()
            page.keyboard.press("Enter")
            assert step.locator(".feedback").inner_text().strip()

        widths = {}
        for width in (320, 375, 768):
            page.set_viewport_size({"width": width, "height": 900})
            widths[str(width)] = page.evaluate("({body: document.body.scrollWidth, document: document.documentElement.scrollWidth, client: document.documentElement.clientWidth})")
            assert widths[str(width)]["body"] <= width and widths[str(width)]["document"] <= width, widths
        assert blocked, "expected external requests to be blocked as part of offline-fallback verification"
        page.add_script_tag(content=AXE_SOURCE)
        axe_runs = []
        for width in (320, 375, 768):
            page.set_viewport_size({"width": width, "height": 900})
            result = page.evaluate("""async () => {
              const result = await axe.run(document.querySelector('.card'), { resultTypes: ['violations', 'incomplete'] });
              return { violations: result.violations, incomplete: result.incomplete };
            }""")
            assert not result["violations"], result["violations"]
            axe_runs.append({"width": width, "violations": 0, "incomplete": len(result["incomplete"])})
        assert not errors, errors
        browser.close()
    print(json.dumps({"status": "passed", "url": args.url, "authoredSections": len(authored_headings), "scaleControls": 5, "sites": 2, "keyboardChoiceSteps": 4, "externalRequestsBlocked": len(blocked), "offlineModelStillInteractive": True, "axeRuns": axe_runs, "responsiveWidths": widths, "pageErrors": errors}, ensure_ascii=False))
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
