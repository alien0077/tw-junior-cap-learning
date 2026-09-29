#!/usr/bin/env python3
"""Student-page browser regression for the Chinese curriculum learning-performance lesson."""
from __future__ import annotations

import argparse
import asyncio
import json
from pathlib import Path

from playwright.async_api import async_playwright


LESSON_ID = "lesson-chinese-learning-performance"
ROOT = Path(__file__).resolve().parents[1]


async def run(url: str) -> dict:
    page_errors: list[str] = []
    blocked_requests: list[str] = []
    blocked_simulations: list[str] = []
    axe_source = (ROOT / "node_modules/axe-core/axe.min.js").read_text(encoding="utf-8")
    async with async_playwright() as playwright:
        browser = await playwright.chromium.launch(headless=True)
        page = await browser.new_page(viewport={"width": 375, "height": 1100}, reduced_motion="reduce")
        page.on("pageerror", lambda error: page_errors.append(str(error)))

        async def local_only(route):
            if route.request.url.split("?", 1)[0].endswith("/site/simulations.js"):
                blocked_simulations.append(route.request.url)
                await route.abort()
                return
            if route.request.url.startswith("http://127.0.0.1:8765/"):
                await route.continue_()
            else:
                blocked_requests.append(route.request.url)
                await route.abort()

        await page.route("**/*", local_only)
        response = await page.goto(url, wait_until="networkidle", timeout=60_000)
        assert response and response.status == 200
        assert blocked_simulations, "simulation-script fault injection did not run"
        await page.get_by_role("status").filter(has_text="資料載入完成").wait_for(timeout=30_000)
        await page.locator("#search").fill(LESSON_ID)
        card = page.locator(f'.card:has([data-lesson="{LESSON_ID}"])')
        await card.wait_for(timeout=30_000)
        sections = card.locator(".lesson-sections article")
        assert await sections.count() == 6, f"expected 6 visible authored sections, got {await sections.count()}"
        headings = await sections.locator("b").all_text_contents()
        assert len(set(headings)) == 6, headings
        activity = card.locator(f'.activity[data-lesson="{LESSON_ID}"]')
        steps = activity.locator(".activity-step")
        assert await steps.count() == 5
        await page.add_script_tag(content=axe_source)
        axe_result = await page.evaluate("""async (scope) => {
          const result = await axe.run(scope, { resultTypes: ['violations', 'incomplete'] });
          return { violations: result.violations, incomplete: result.incomplete };
        }""", await card.element_handle())
        assert not axe_result["violations"], axe_result["violations"]

        first = steps.nth(0)
        first_answer = first.get_by_role("button", name="A. 閱讀")
        await first_answer.focus()
        await page.keyboard.press("Enter")
        assert "5 是閱讀類" in await first.locator(".feedback").inner_text()
        assert await first_answer.get_attribute("aria-pressed") == "true"
        assert await first.get_by_role("button", name="B. 寫作").get_attribute("aria-pressed") == "false"

        second = steps.nth(1)
        await second.get_by_role("button", name="A. 只交一句『大家都想要更多書』").focus()
        await page.keyboard.press("Enter")
        assert "多份資料" in await second.locator(".feedback").inner_text()
        assert await second.get_by_role("button", name="A. 只交一句『大家都想要更多書』").get_attribute("aria-pressed") == "true"
        await second.get_by_role("button", name="C. 附回饋來源欄的分類表，並標出哪些意見支持共同點").focus()
        await page.keyboard.press("Enter")
        assert "分類表" in await second.locator(".feedback").inner_text()
        assert await second.get_by_role("button", name="C. 附回饋來源欄的分類表，並標出哪些意見支持共同點").get_attribute("aria-pressed") == "true"
        assert await second.get_by_role("button", name="A. 只交一句『大家都想要更多書』").get_attribute("aria-pressed") == "false"

        third = steps.nth(2)
        await third.get_by_role("button", name="B. 標出兩則公告的目的線索，列出異同並說明引用哪句支持判斷").focus()
        await page.keyboard.press("Enter")
        assert "執行比較" in await third.locator(".feedback").inner_text()

        fourth = steps.nth(3)
        await fourth.get_by_role("button", name="A. 只記下簡化後句子的長度").focus()
        await page.keyboard.press("Enter")
        assert "原本要展現" in await fourth.locator(".feedback").inner_text()
        await fourth.get_by_role("button", name="C. 原目標、提供的支持／改變的條件，以及用來判斷表現的作品證據").focus()
        await page.keyboard.press("Enter")
        assert "目標、條件與證據" in await fourth.locator(".feedback").inner_text()

        fifth = steps.nth(4)
        await fifth.get_by_role("button", name="B. 比較兩張海報的目的與受眾；各摘一項文字線索，完成異同表並用線索說明判斷。").focus()
        await page.keyboard.press("Enter")
        assert "出口任務" in await fifth.locator(".feedback").inner_text()
        aria_live_regions = await activity.locator('[aria-live="polite"]').count()
        assert aria_live_regions == 5, f"each activity step should announce feedback, got {aria_live_regions} regions"
        reduced_motion = await page.evaluate("matchMedia('(prefers-reduced-motion: reduce)').matches")
        assert reduced_motion

        responsive = []
        for width in (320, 375, 768):
            await page.set_viewport_size({"width": width, "height": 1100})
            size = await page.evaluate("({viewport: innerWidth, scroll: document.documentElement.scrollWidth})")
            assert size["scroll"] <= size["viewport"], size
            targets = await page.locator(f'.activity[data-lesson="{LESSON_ID}"] button[data-answer]').evaluate_all("buttons => buttons.map(button => { const r = button.getBoundingClientRect(); return {width: r.width, height: r.height}; })")
            assert all(target["width"] >= 44 and target["height"] >= 44 for target in targets), targets
            responsive.append(size)
        assert not page_errors, page_errors
        visible_section_count = await sections.count()
        guided_choice_step_count = await steps.count()
        await browser.close()
        return {
            "status": "passed",
            "lessonId": LESSON_ID,
            "visibleSections": visible_section_count,
            "uniqueHeadings": len(set(headings)),
            "guidedChoiceSteps": guided_choice_step_count,
            "keyboardCorrectFeedback": True,
            "keyboardRetryThenCorrectFeedback": True,
            "ariaLiveFeedbackRegions": aria_live_regions,
            "reducedMotion": reduced_motion,
            "axeViolationCount": len(axe_result["violations"]),
            "axeIncompleteCount": len(axe_result["incomplete"]),
            "networkBlocked": True,
            "blockedSimulationScript": blocked_simulations,
            "localGuidedChoiceFallbackUsable": True,
            "blockedRequestCount": len(blocked_requests),
            "responsive": responsive,
            "pageErrors": page_errors,
        }


def main() -> int:
    parser = argparse.ArgumentParser()
    parser.add_argument("--url", default="http://127.0.0.1:8765/site/index.html")
    args = parser.parse_args()
    print(json.dumps(asyncio.run(run(args.url)), ensure_ascii=False))
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
