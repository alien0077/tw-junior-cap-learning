#!/usr/bin/env python3
"""Chromium regression for the learner-visible English 8-IV-1 lesson."""
from __future__ import annotations

import argparse
import asyncio
import json
from pathlib import Path

from playwright.async_api import async_playwright

ROOT = Path(__file__).resolve().parents[1]
LESSON_ID = "lesson-english-performance-8-iv-1"
LESSON = json.loads((ROOT / "lessons/english/lesson-english-performance-8-iv-1.json").read_text(encoding="utf-8"))


async def run(url: str) -> dict:
    errors: list[str] = []
    blocked: list[str] = []
    blocked_simulations: list[str] = []
    axe = (ROOT / "node_modules/axe-core/axe.min.js").read_text(encoding="utf-8")
    async with async_playwright() as playwright:
        browser = await playwright.chromium.launch(headless=True)
        page = await browser.new_page(viewport={"width": 375, "height": 1100}, reduced_motion="reduce")
        page.on("pageerror", lambda error: errors.append(str(error)))

        async def local_only(route):
            if route.request.url.split("?", 1)[0].endswith("/site/simulations.js"):
                blocked_simulations.append(route.request.url)
                await route.abort()
                return
            if route.request.url.startswith("http://127.0.0.1:8765/"):
                await route.continue_()
            else:
                blocked.append(route.request.url)
                await route.abort()

        await page.route("**/*", local_only)
        response = await page.goto(url, wait_until="networkidle", timeout=60000)
        assert response and response.status == 200
        await page.get_by_role("status").filter(has_text="資料載入完成").wait_for(timeout=30000)
        await page.locator("#search").fill(LESSON_ID)
        card = page.locator(f'.card:has([data-lesson="{LESSON_ID}"])')
        await card.wait_for(timeout=30000)
        assert blocked_simulations, "simulation-script fault injection did not run"
        sections = card.locator(".lesson-sections article")
        assert await sections.count() == len(LESSON["content"]["sections"]) == 7
        assert await sections.locator("b").all_text_contents() == [section["heading"] for section in LESSON["content"]["sections"]]
        activity = card.locator(f'[data-lesson="{LESSON_ID}"]')
        steps = activity.locator(".activity-step")
        assert await steps.count() == 4
        await page.add_script_tag(content=axe)
        axe_result = await page.evaluate("""async (scope) => {
          const result = await axe.run(scope, { resultTypes: ['violations', 'incomplete'] });
          return { violations: result.violations, incomplete: result.incomplete };
        }""", await card.element_handle())
        assert not axe_result["violations"], axe_result["violations"]

        for index, item in enumerate(LESSON["interactive"]["steps"]):
            current = steps.nth(index)
            wrong = "A" if item["answer"] != "A" else "B"
            await current.locator(f'[data-answer="{wrong}"]').focus()
            await page.keyboard.press("Enter")
            assert item["retryHint"] in await current.locator(".feedback").inner_text()
            await current.locator(f'[data-answer="{item["answer"]}"]').focus()
            await page.keyboard.press("Enter")
            assert item["feedback"] in await current.locator(".feedback").inner_text()

        responsive = []
        for width in (320, 375, 768):
            await page.set_viewport_size({"width": width, "height": 1100})
            size = await page.evaluate("({viewport: innerWidth, scroll: document.documentElement.scrollWidth})")
            assert size["scroll"] <= size["viewport"], size
            responsive.append({"width": width, "scrollWidth": size["scroll"]})
        assert not errors, errors
        await browser.close()
        return {"status": "passed", "visibleSections": 7, "guidedChoiceSteps": 4,
                "keyboardWrongRetryAndCorrectFeedback": True, "axeViolations": 0,
                "axeIncomplete": len(axe_result["incomplete"]), "responsive": responsive,
                "blockedSimulationScript": blocked_simulations,
                "localGuidedChoiceFallbackUsable": True,
                "blockedExternalRequests": len(blocked), "pageErrors": errors}


def main() -> None:
    parser = argparse.ArgumentParser()
    parser.add_argument("--url", default="http://127.0.0.1:8765/site/index.html")
    args = parser.parse_args()
    print(json.dumps(asyncio.run(run(args.url)), ensure_ascii=False))


if __name__ == "__main__":
    main()
