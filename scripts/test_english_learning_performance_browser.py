#!/usr/bin/env python3
"""Browser regression for the English learning-performance umbrella lesson."""
from __future__ import annotations

import argparse
import asyncio
from pathlib import Path

from playwright.async_api import async_playwright


LESSON_ID = "lesson-english-learning-performance"
ROOT = Path(__file__).resolve().parents[1]


async def run(url: str) -> dict:
    page_errors: list[str] = []
    blocked_requests: list[str] = []
    axe_source = (ROOT / "node_modules/axe-core/axe.min.js").read_text(encoding="utf-8")
    async with async_playwright() as playwright:
        browser = await playwright.chromium.launch(headless=True)
        page = await browser.new_page(viewport={"width": 375, "height": 1100}, reduced_motion="reduce")
        page.on("pageerror", lambda error: page_errors.append(str(error)))

        async def local_only(route):
            if route.request.url.startswith("http://127.0.0.1:8765/"):
                await route.continue_()
            else:
                blocked_requests.append(route.request.url)
                await route.abort()

        await page.route("**/*", local_only)
        response = await page.goto(url, wait_until="networkidle", timeout=60_000)
        assert response and response.status == 200
        await page.get_by_role("status").filter(has_text="資料載入完成").wait_for(timeout=30_000)
        await page.locator("#search").fill(LESSON_ID)
        card = page.locator(f'.card:has([data-lesson="{LESSON_ID}"])')
        await card.wait_for(timeout=30_000)
        sections = card.locator(".lesson-sections article")
        assert await sections.count() == 6
        headings = await sections.locator("b").all_text_contents()
        assert len(set(headings)) == 6
        activity = card.locator(f'.activity[data-lesson="{LESSON_ID}"]')
        steps = activity.locator(".activity-step")
        assert await steps.count() == 5

        first = steps.nth(0)
        wrong = first.get_by_role("button", name="A. 學生背出library、meet和late三個字。")
        await wrong.focus()
        await page.keyboard.press("Enter")
        assert "目標動詞" in await first.locator(".feedback").inner_text()
        assert await wrong.get_attribute("aria-pressed") == "true"
        correct = first.get_by_role("button", name="B. 學生根據卡片回答Where should we meet?並指出outside the library。")
        await correct.focus()
        await page.keyboard.press("Enter")
        assert "直接對準閱讀理解" in await first.locator(".feedback").inner_text()
        assert await correct.get_attribute("aria-pressed") == "true"
        assert await wrong.get_attribute("aria-pressed") == "false"

        answer_names = [
            (1, "C. 他目前的回答支持其抓到時間，但地點與條件資訊仍需再查證。"),
            (2, "A. 要求對方重述或用地圖指出位置，聽完後再確認自己的理解。"),
            (3, "B. 學生寫一則包含時間、集合地點與遇到問題時的下一步提醒。"),
            (4, "A. 請學生依新公告告訴缺席同伴改到哪裡、幾點開始，並指出公告中的依據。"),
        ]
        for index, name in answer_names:
            step = steps.nth(index)
            button = step.get_by_role("button", name=name)
            await button.focus()
            await page.keyboard.press("Enter")
            assert "可進入下一步" in await step.locator(".feedback").inner_text()

        await page.add_script_tag(content=axe_source)
        axe_result = await page.evaluate("""async (scope) => {
          const result = await axe.run(scope, { resultTypes: ['violations', 'incomplete'] });
          return { violations: result.violations, incomplete: result.incomplete };
        }""", await card.element_handle())
        assert not axe_result["violations"], axe_result["violations"]
        assert await activity.locator('[aria-live="polite"]').count() == 5
        assert await page.evaluate("matchMedia('(prefers-reduced-motion: reduce)').matches")

        responsive = []
        for width in (320, 375, 768):
            await page.set_viewport_size({"width": width, "height": 1100})
            size = await page.evaluate("({viewport: innerWidth, scroll: document.documentElement.scrollWidth})")
            assert size["scroll"] <= size["viewport"], size
            dimensions = await activity.locator("button[data-answer]").evaluate_all("buttons => buttons.map(button => { const r = button.getBoundingClientRect(); return {width:r.width,height:r.height}; })")
            assert all(item["width"] >= 44 and item["height"] >= 44 for item in dimensions), dimensions
            responsive.append({"width": width, "scrollWidth": size["scroll"]})

        assert not page_errors, page_errors
        visible_section_count = await sections.count()
        guided_choice_count = await steps.count()
        await browser.close()
        return {
            "status": "passed",
            "visibleSections": visible_section_count,
            "guidedChoiceSteps": guided_choice_count,
            "keyboardWrongRetryCorrect": True,
            "liveRegions": 5,
            "axeViolations": 0,
            "axeIncomplete": len(axe_result["incomplete"]),
            "reducedMotion": True,
            "responsive": responsive,
            "blockedExternalRequests": len(blocked_requests),
            "pageErrors": page_errors,
        }


def main() -> None:
    parser = argparse.ArgumentParser()
    parser.add_argument("--url", default="http://127.0.0.1:8765/site/index.html")
    args = parser.parse_args()
    print(asyncio.run(run(args.url)))


if __name__ == "__main__":
    main()
