#!/usr/bin/env python3
"""Verify Chinese Ab-IV-1 lesson rendering and offline guided-choice behavior."""
from __future__ import annotations

import argparse
import asyncio
import json
import os
from pathlib import Path

from playwright.async_api import async_playwright

ROOT = Path(__file__).resolve().parents[1]
LESSON_ID = "lesson-chinese-content-ab-iv-1"
LESSON = json.loads((ROOT / "lessons/chinese/lesson-chinese-content-ab-iv-1.json").read_text(encoding="utf-8"))
AXE = (ROOT / "node_modules/axe-core/axe.min.js").read_text(encoding="utf-8")


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
            clean_url = route.request.url.split("?", 1)[0]
            if clean_url.endswith("/site/simulations.js"):
                simulation_faults.append(route.request.url)
                await route.abort()
            elif route.request.url.startswith("http://127.0.0.1:8765/"):
                await route.continue_()
            else:
                blocked.append(route.request.url)
                await route.abort()

        await page.route("**/*", local_only)
        response = await page.goto(url, wait_until="networkidle", timeout=60000)
        assert response and response.status == 200
        assert simulation_faults, "simulation.js fault injection did not run"
        await page.get_by_role("status").filter(has_text="資料載入完成").wait_for(timeout=30000)
        await page.locator("#search").fill(LESSON_ID)
        card = page.locator(f'.card:has([data-lesson="{LESSON_ID}"])')
        await card.wait_for(timeout=30000)
        sections = card.locator(".lesson-sections > article")
        visible_headings = await sections.locator("b").all_inner_texts()
        authored_headings = [s["heading"] for s in LESSON["teaching"]["body"]]
        assert len(visible_headings) == len(LESSON["content"]["sections"]) + len(authored_headings)
        assert visible_headings[-len(authored_headings):] == authored_headings
        activity = card.locator(f'.activity[data-lesson="{LESSON_ID}"]')
        steps = activity.locator(".activity-step")
        assert await steps.count() == 3
        first = steps.nth(0)
        item = LESSON["interactive"]["steps"][0]
        wrong = chr(ord(item["answer"]) + 1) if item["answer"] != "C" else "A"
        await first.locator(f'[data-answer="{wrong}"]').focus()
        await page.keyboard.press("Enter")
        assert item["retryHint"] in await first.locator(".feedback").inner_text()
        await first.locator(f'[data-answer="{item["answer"]}"]').focus()
        await page.keyboard.press("Enter")
        assert item["feedback"] in await first.locator(".feedback").inner_text()
        await page.add_script_tag(content=AXE)
        axe = await page.evaluate("""async scope => {
          const result = await axe.run(scope, { resultTypes: ['violations', 'incomplete'] });
          return { violations: result.violations, incomplete: result.incomplete };
        }""", await card.element_handle())
        assert not axe["violations"], axe["violations"]
        for width in (320, 375, 768):
            await page.set_viewport_size({"width": width, "height": 1000})
            metrics = await page.evaluate("({body: document.body.scrollWidth, doc: document.documentElement.scrollWidth})")
            assert metrics["body"] <= width and metrics["doc"] <= width, (width, metrics)
        assert not errors, errors
        print(json.dumps({"status": "passed", "visibleSections": len(visible_headings),
                          "authoredTeachingSections": len(authored_headings), "guidedChoiceSteps": 3,
                          "blockedSimulationScript": simulation_faults, "blockedExternalRequests": len(blocked),
                          "offlineFallbackUsable": True, "keyboardWrongRetryCorrect": True,
                          "axeViolations": 0, "axeIncomplete": len(axe["incomplete"]),
                          "responsiveWidths": [320, 375, 768], "pageErrors": errors}, ensure_ascii=False))
        await browser.close()


if __name__ == "__main__":
    parser = argparse.ArgumentParser()
    parser.add_argument("--url", default="http://127.0.0.1:8765/site/index.html")
    asyncio.run(main(parser.parse_args().url))
