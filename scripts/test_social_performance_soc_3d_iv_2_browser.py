#!/usr/bin/env python3
"""Real-browser regression for the Soc3d-IV-2 authored lesson interaction."""
from __future__ import annotations

import argparse
import asyncio
import json
from pathlib import Path
from urllib.parse import urlsplit

from playwright.async_api import async_playwright


ROOT = Path(__file__).resolve().parents[1]
LESSON_ID = "lesson-social-performance-soc-3d-iv-2"
LESSON = json.loads((ROOT / "lessons/social/lesson-social-performance-soc-3d-iv-2.json").read_text(encoding="utf-8"))


async def run(url: str) -> dict:
    errors: list[str] = []
    blocked: list[str] = []
    origin = f"{urlsplit(url).scheme}://{urlsplit(url).netloc}/"
    axe = (ROOT / "node_modules/axe-core/axe.min.js").read_text(encoding="utf-8")
    async with async_playwright() as playwright:
        browser = await playwright.chromium.launch(headless=True)
        page = await browser.new_page(viewport={"width": 375, "height": 1100}, reduced_motion="reduce")
        page.on("pageerror", lambda error: errors.append(str(error)))

        async def local_only(route):
            if route.request.url.startswith(origin):
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
        sections = card.locator(".lesson-sections article")
        assert await sections.count() == 6
        assert await sections.locator("b").all_text_contents() == [item["heading"] for item in LESSON["content"]["sections"]]
        for heading in ("讓受影響的人參與定義問題", "把價值轉成可比較的方案條件", "選一個能先試、可撤回的改變"):
            assert heading in "\n".join(await sections.locator("b").all_text_contents())

        activity = card.locator(f'.activity[data-lesson="{LESSON_ID}"]')
        steps = activity.locator(".activity-step")
        assert await steps.count() == 6
        for index, item in enumerate(LESSON["interactive"]["steps"]):
            current = steps.nth(index)
            assert await current.locator("[data-answer]").count() == len(item["options"])
            wrong = next(letter for letter in "ABC"[: len(item["options"])] if letter != item["answer"])
            await current.locator(f'[data-answer="{wrong}"]').focus()
            await page.keyboard.press("Enter")
            assert item["retryHint"] in await current.locator(".feedback").inner_text()
            assert await current.locator(f'[data-answer="{item["answer"]}"]').get_attribute("aria-pressed") == "false"
            await current.locator(f'[data-answer="{item["answer"]}"]').focus()
            await page.keyboard.press("Enter")
            assert item["feedback"] in await current.locator(".feedback").inner_text()
            assert await current.locator(f'[data-answer="{item["answer"]}"]').get_attribute("aria-pressed") == "true"

        await page.add_script_tag(content=axe)
        axe_result = await page.evaluate("""async (scope) => {
          const result = await axe.run(scope, { resultTypes: ['violations', 'incomplete'] });
          return { violations: result.violations, incomplete: result.incomplete };
        }""", await card.element_handle())
        assert not axe_result["violations"], axe_result["violations"]

        responsive = []
        for width in (320, 375, 768):
            await page.set_viewport_size({"width": width, "height": 1100})
            size = await page.evaluate("({viewport: innerWidth, scroll: document.documentElement.scrollWidth})")
            assert size["scroll"] <= size["viewport"], size
            responsive.append({"width": width, "scrollWidth": size["scroll"]})
        assert not errors, errors
        assert blocked, "External requests should be blocked to prove local fallback."
        visible_section_count = await sections.count()
        guided_choice_steps = await steps.count()
        await browser.close()
        return {
            "status": "passed",
            "unit": "社3d-Ⅳ-2",
            "visibleSections": visible_section_count,
            "guidedChoiceSteps": guided_choice_steps,
            "answerSequence": [item["answer"] for item in LESSON["interactive"]["steps"]],
            "keyboardWrongRetryAndCorrectFeedback": True,
            "axeViolations": len(axe_result["violations"]),
            "axeIncomplete": len(axe_result["incomplete"]),
            "responsive": responsive,
            "blockedExternalRequests": len(blocked),
            "pageErrors": errors,
        }


def main() -> None:
    parser = argparse.ArgumentParser()
    parser.add_argument("--url", default="http://127.0.0.1:8765/site/index.html")
    args = parser.parse_args()
    print(json.dumps(asyncio.run(run(args.url)), ensure_ascii=False))


if __name__ == "__main__":
    main()
