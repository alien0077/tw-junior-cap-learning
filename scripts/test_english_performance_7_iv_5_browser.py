#!/usr/bin/env python3
"""Chromium regression for learner-visible English 7-IV-5 study planning."""
from __future__ import annotations

import argparse
import asyncio
import json
from pathlib import Path

from playwright.async_api import async_playwright

ROOT = Path(__file__).resolve().parents[1]
LESSON_ID = "lesson-english-performance-7-iv-5"
LESSON = json.loads((ROOT / "lessons/english/lesson-english-performance-7-iv-5.json").read_text(encoding="utf-8"))


async def run(url: str) -> dict:
    errors: list[str] = []
    blocked: list[str] = []
    axe = (ROOT / "node_modules/axe-core/axe.min.js").read_text(encoding="utf-8")
    async with async_playwright() as playwright:
        browser = await playwright.chromium.launch(headless=True)
        page = await browser.new_page(viewport={"width": 375, "height": 1100}, reduced_motion="reduce")
        page.on("pageerror", lambda error: errors.append(str(error)))

        async def local_only(route):
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
        card = page.locator(f'.card:has([data-reading-strategy-lab="{LESSON_ID}"])')
        await card.wait_for(timeout=30000)
        sections = card.locator(".lesson-sections article")
        assert await sections.count() == 6
        assert await sections.locator("b").all_text_contents() == [s["heading"] for s in LESSON["teaching"]["body"]]
        activity = card.locator(f'[data-reading-strategy-lab="{LESSON_ID}"]')
        await activity.wait_for()
        assert await activity.get_by_role("progressbar").count() == 1
        await page.add_script_tag(content=axe)
        axe_result = await page.evaluate("""async scope => {
          const result = await axe.run(scope, { resultTypes: ['violations', 'incomplete'] });
          return { violations: result.violations, incomplete: result.incomplete };
        }""", await card.element_handle())
        assert not axe_result["violations"], axe_result["violations"]

        for index, item in enumerate(LESSON["interactive"]["steps"]):
            current = page.locator(f'[data-reading-strategy-lab="{LESSON_ID}"]')
            wrong = "A" if item["answer"] != "A" else "B"
            wrong_radio = current.locator(f'[data-rsl-answer][value="{wrong}"]')
            await wrong_radio.focus()
            await page.keyboard.press("Space")
            check_button = current.get_by_role("button", name="檢查並前進")
            await check_button.focus()
            await page.keyboard.press("Enter")
            assert item["retryHint"] in await page.locator(f'[data-reading-strategy-lab="{LESSON_ID}"] [role="status"]').inner_text()
            current = page.locator(f'[data-reading-strategy-lab="{LESSON_ID}"]')
            right_radio = current.locator(f'[data-rsl-answer][value="{item["answer"]}"]')
            await right_radio.focus()
            await page.keyboard.press("Space")
            check_button = current.get_by_role("button", name="檢查並前進")
            await check_button.focus()
            await page.keyboard.press("Enter")
            if index < len(LESSON["interactive"]["steps"]) - 1:
                assert item["feedback"] in await page.locator(f'[data-reading-strategy-lab="{LESSON_ID}"] [role="status"]').inner_text()
            if index == 0:
                await page.reload(wait_until="networkidle")
                await page.get_by_role("status").filter(has_text="資料載入完成").wait_for(timeout=30000)
                await page.locator("#search").fill(LESSON_ID)
                await page.locator(f'[data-reading-strategy-lab="{LESSON_ID}"]').wait_for()
                assert "任務 2／6" in await page.locator(f'[data-reading-strategy-lab="{LESSON_ID}"]').inner_text()

        complete = page.locator(f'[data-reading-strategy-lab="{LESSON_ID}"]')
        assert LESSON["interactive"]["completionMessage"] in await complete.inner_text()
        await complete.get_by_role("button", name="重新開始").focus()
        await page.keyboard.press("Enter")
        assert "任務 1／6" in await page.locator(f'[data-reading-strategy-lab="{LESSON_ID}"]').inner_text()
        responsive = []
        for width in (320, 375, 768):
            await page.set_viewport_size({"width": width, "height": 1100})
            size = await page.evaluate("({viewport: innerWidth, scroll: document.documentElement.scrollWidth})")
            assert size["scroll"] <= size["viewport"], size
            responsive.append({"width": width, "scrollWidth": size["scroll"]})
        assert not errors, errors
        await browser.close()
        return {"status": "passed", "visibleSections": 6, "guidedChoiceSteps": 6,
                "keyboardWrongRetryAndCorrectFeedback": True, "persistenceAfterReload": True,
                "completionAndReset": True,
                "axeViolations": 0, "axeIncomplete": len(axe_result["incomplete"]),
                "responsive": responsive, "blockedExternalRequests": len(blocked), "pageErrors": errors}


def main() -> None:
    parser = argparse.ArgumentParser()
    parser.add_argument("--url", default="http://127.0.0.1:8765/site/index.html")
    args = parser.parse_args()
    print(json.dumps(asyncio.run(run(args.url)), ensure_ascii=False))


if __name__ == "__main__":
    main()
