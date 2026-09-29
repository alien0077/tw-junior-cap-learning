#!/usr/bin/env python3
"""Verify the Ab-IV-2 authored lesson and its actual three-step local quiz."""
from __future__ import annotations

import argparse
import asyncio
import json
import os
from pathlib import Path

from playwright.async_api import async_playwright
import yaml

ROOT = Path(__file__).resolve().parents[1]
LESSON_ID = "lesson-chinese-content-ab-iv-2"
LESSON = json.loads((ROOT / "lessons/chinese/lesson-chinese-content-ab-iv-2.json").read_text(encoding="utf-8"))
SPEC = yaml.safe_load((ROOT / "implementation/unit-specs/chinese/cur-chinese-content-ab-iv-2.yaml").read_text(encoding="utf-8"))["unitImplementationSpec"]
AXE = (ROOT / "node_modules/axe-core/axe.min.js").read_text(encoding="utf-8")

assert SPEC["knowledgeGraphIds"] == LESSON["knowledgeIds"]
assert SPEC["interactiveBlocks"][0]["component"] == "GuidedChoiceBlock"
assert all(publisher in {record["publisher"] for record in LESSON["publisherResearch"]}
           for publisher in ("nani", "kanghsuan", "hanlin"))
QUESTION_FILES = [path for path in (ROOT / "questions/chinese").glob("*.json")
                  if json.loads(path.read_text(encoding="utf-8")).get("lessonId") == LESSON_ID]
assert QUESTION_FILES
assert all(json.loads(path.read_text(encoding="utf-8")).get("knowledgeIds") == LESSON["knowledgeIds"]
           for path in QUESTION_FILES)


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
            clean_url = request_url.split("?", 1)[0]
            if clean_url.endswith("/site/simulations.js"):
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
        card = page.locator(f'.card:has([data-lesson="{LESSON_ID}"])')
        await card.wait_for(timeout=30000)
        sections = card.locator(".lesson-sections > article")
        headings = await sections.locator("b").all_inner_texts()
        authored = [section["heading"] for section in LESSON["teaching"]["body"]]
        assert headings[-len(authored):] == authored, headings
        activity = card.locator(f'.activity[data-lesson="{LESSON_ID}"]')
        steps = activity.locator(".activity-step")
        expected_steps = LESSON["interactive"]["steps"]
        assert await steps.count() == len(expected_steps) == 3
        for index, item in enumerate(expected_steps):
            step = steps.nth(index)
            assert item["prompt"] in await step.inner_text()
            wrong = chr(ord(item["answer"]) + 1) if item["answer"] != "C" else "A"
            wrong_button = step.locator(f'[data-answer="{wrong}"]')
            await wrong_button.focus()
            await page.keyboard.press("Enter")
            feedback = step.locator(".feedback")
            assert "再想一次" in await feedback.inner_text()
            assert await wrong_button.get_attribute("aria-pressed") == "true"
            right_button = step.locator(f'[data-answer="{item["answer"]}"]')
            await right_button.focus()
            await page.keyboard.press("Enter")
            assert item["feedback"] in await feedback.inner_text()
            assert await right_button.get_attribute("aria-pressed") == "true"
        await page.add_script_tag(content=AXE)
        axe_incomplete = 0
        minimum_option_height = float("inf")
        for width in (320, 375, 768):
            await page.set_viewport_size({"width": width, "height": 1000})
            sizes = await page.evaluate("({body: document.body.scrollWidth, doc: document.documentElement.scrollWidth})")
            assert sizes["body"] <= width and sizes["doc"] <= width, (width, sizes)
            smallest = await steps.nth(0).locator("[data-answer]").first.evaluate("el => el.getBoundingClientRect().height")
            assert smallest >= 44, (width, smallest)
            minimum_option_height = min(minimum_option_height, smallest)
            axe = await page.evaluate("""async scope => {
              const result = await axe.run(scope, { resultTypes: ['violations', 'incomplete'] });
              return { violations: result.violations, incomplete: result.incomplete };
            }""", await card.element_handle())
            assert not axe["violations"], (width, axe["violations"])
            axe_incomplete += len(axe["incomplete"])
        assert not errors, errors
        print(json.dumps({"status": "passed", "visibleSections": len(headings),
                          "authoredTeachingSections": len(authored), "guidedChoiceSteps": len(expected_steps),
                          "blockedSimulationScript": bool(simulation_faults), "blockedExternalRequests": len(blocked),
                          "unitQuestionsMapped": len(QUESTION_FILES), "kgAndPublisherMapping": True,
                          "offlineFallbackUsable": True, "keyboardWrongRetryCorrect": True,
                          "axeViolations": 0, "axeIncompleteAcrossViewports": axe_incomplete,
                          "minimumOptionHeightPx": minimum_option_height,
                          "responsiveWidths": [320, 375, 768], "pageErrors": errors}, ensure_ascii=False))
        await browser.close()


if __name__ == "__main__":
    parser = argparse.ArgumentParser()
    parser.add_argument("--url", default="http://127.0.0.1:8765/site/index.html")
    asyncio.run(main(parser.parse_args().url))
