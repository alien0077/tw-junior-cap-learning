#!/usr/bin/env python3
"""Verify Ab-IV-3 curriculum/KG links and the authored three-step character quiz."""
from __future__ import annotations

import argparse
import asyncio
import json
import os
from pathlib import Path

import yaml
from playwright.async_api import async_playwright

ROOT = Path(__file__).resolve().parents[1]
LESSON_ID = "lesson-chinese-content-ab-iv-3"
LESSON = json.loads((ROOT / "lessons/chinese/lesson-chinese-content-ab-iv-3.json").read_text(encoding="utf-8"))
SPEC = yaml.safe_load((ROOT / "implementation/unit-specs/chinese/cur-chinese-content-ab-iv-3.yaml").read_text(encoding="utf-8"))["unitImplementationSpec"]
AXE = (ROOT / "node_modules/axe-core/axe.min.js").read_text(encoding="utf-8")
QUESTION_FILES = [p for p in (ROOT / "questions/chinese").glob("*.json")
                  if json.loads(p.read_text(encoding="utf-8")).get("lessonId") == LESSON_ID]

assert SPEC["knowledgeGraphIds"] == LESSON["knowledgeIds"]
assert SPEC["interactiveBlocks"][0]["component"] == "GuidedChoiceBlock"
assert all(p in {r["publisher"] for r in LESSON["publisherResearch"]}
           for p in ("nani", "kanghsuan", "hanlin"))
assert QUESTION_FILES
assert all(json.loads(p.read_text(encoding="utf-8")).get("knowledgeIds") == LESSON["knowledgeIds"]
           for p in QUESTION_FILES)


async def main(url: str) -> None:
    async with async_playwright() as playwright:
        options = {"headless": True}
        chrome = Path(os.environ.get("TW_BROWSER_CHROME", "/Applications/Google Chrome.app/Contents/MacOS/Google Chrome"))
        if chrome.is_file():
            options["executable_path"] = str(chrome)
        browser = await playwright.chromium.launch(**options)
        page = await browser.new_page(viewport={"width": 375, "height": 1000}, reduced_motion="reduce")
        errors: list[str] = []
        blocked: list[str] = []
        simulation_faults: list[str] = []
        page.on("pageerror", lambda error: errors.append(str(error)))

        async def local_only(route):
            request_url = route.request.url
            if request_url.split("?", 1)[0].endswith("/site/simulations.js"):
                simulation_faults.append(request_url)
                await route.abort()
            elif request_url.startswith("http://127.0.0.1:8765/"):
                await route.continue_()
            else:
                blocked.append(request_url)
                await route.abort()

        await page.route("**/*", local_only)
        response = await page.goto(url, wait_until="networkidle", timeout=60000)
        assert response and response.status == 200
        assert simulation_faults, "simulation.js failure injection did not run"
        await page.get_by_role("status").filter(has_text="資料載入完成").wait_for(timeout=30000)
        await page.locator("#search").fill(LESSON_ID)
        card = page.locator(f'.card:has([data-lesson="{LESSON_ID}"])').first
        await card.wait_for(timeout=30000)
        headings = await card.locator(".lesson-sections > article b").all_inner_texts()
        authored = [section["heading"] for section in LESSON["teaching"]["body"]]
        assert headings[-len(authored):] == authored, headings
        steps = card.locator(f'.activity[data-lesson="{LESSON_ID}"] .activity-step')
        expected = LESSON["interactive"]["steps"]
        assert await steps.count() == len(expected) == 3
        for index, item in enumerate(expected):
            step = steps.nth(index)
            assert item["prompt"] in await step.inner_text()
            wrong = "B" if item["answer"] == "A" else "A"
            wrong_button = step.locator(f'[data-answer="{wrong}"]')
            await wrong_button.focus()
            await page.keyboard.press("Enter")
            feedback = step.locator(".feedback")
            assert "再想一次" in await feedback.inner_text()
            assert await wrong_button.get_attribute("aria-pressed") == "true"
            right = step.locator(f'[data-answer="{item["answer"]}"]')
            await right.focus()
            await page.keyboard.press("Enter")
            assert item["feedback"] in await feedback.inner_text()
            assert await right.get_attribute("aria-pressed") == "true"
        await page.add_script_tag(content=AXE)
        incomplete_count = 0
        min_touch_height = float("inf")
        for width in (320, 375, 768):
            await page.set_viewport_size({"width": width, "height": 1000})
            dimensions = await page.evaluate("({body: document.body.scrollWidth, doc: document.documentElement.scrollWidth})")
            assert dimensions["body"] <= width and dimensions["doc"] <= width, (width, dimensions)
            height = await steps.nth(0).locator("[data-answer]").first.evaluate("e => e.getBoundingClientRect().height")
            min_touch_height = min(min_touch_height, height)
            assert height >= 44, (width, height)
            result = await page.evaluate("""async scope => {
              const r = await axe.run(scope, { resultTypes: ['violations', 'incomplete'] });
              return { violations: r.violations, incomplete: r.incomplete };
            }""", await card.element_handle())
            assert not result["violations"], (width, result["violations"])
            incomplete_count += len(result["incomplete"])
        assert not errors, errors
        print(json.dumps({"status": "passed", "visibleSections": len(headings),
                          "authoredTeachingSections": len(authored), "guidedChoiceSteps": len(expected),
                          "unitQuestionsMapped": len(QUESTION_FILES), "kgAndThreePublisherRecords": True,
                          "simulationFailureFallback": bool(simulation_faults), "blockedExternalRequests": len(blocked),
                          "offlineFallbackUsable": True, "keyboardWrongRetryCorrect": True,
                          "axeViolations": 0, "axeIncompleteAcrossViewports": incomplete_count,
                          "minimumOptionHeightPx": min_touch_height,
                          "responsiveWidths": [320, 375, 768], "pageErrors": errors}, ensure_ascii=False))
        await browser.close()


if __name__ == "__main__":
    parser = argparse.ArgumentParser()
    parser.add_argument("--url", default="http://127.0.0.1:8765/site/index.html")
    asyncio.run(main(parser.parse_args().url))
