#!/usr/bin/env python3
"""Playwright student-page regression for English 6-IV-1."""
from __future__ import annotations

import argparse
import asyncio
from pathlib import Path

from playwright.async_api import async_playwright


LESSON_ID = "lesson-english-performance-6-iv-1"
ROOT = Path(__file__).resolve().parents[1]


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
            if route.request.url.endswith("/site/simulations.js"):
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
        assert blocked_simulations, "simulation fallback was not exercised"
        await page.locator("#search").fill(LESSON_ID)
        card = page.locator(f'.card:has([data-lesson="{LESSON_ID}"])')
        await card.wait_for(timeout=30000)
        sections = card.locator(".lesson-sections article")
        assert await sections.count() == 6
        assert len(set(await sections.locator("b").all_text_contents())) == 6
        activity = card.locator(f'.activity[data-lesson="{LESSON_ID}"]')
        steps = activity.locator(".activity-step")
        assert await steps.count() == 4

        first = steps.nth(0)
        wrong = first.get_by_role("button", name="A. 說『我不會』就把字卡收起來。")
        await wrong.focus()
        await page.keyboard.press("Enter")
        assert "找一個" in await first.locator(".feedback").inner_text()
        assert await wrong.get_attribute("aria-pressed") == "true"
        correct = first.get_by_role("button", name="B. 指出不確定的開頭音，聽一次示範後再試讀。")
        await correct.focus()
        await page.keyboard.press("Enter")
        assert "把錯誤定位到開頭音" in await first.locator(".feedback").inner_text()
        assert await correct.get_attribute("aria-pressed") == "true"
        assert await wrong.get_attribute("aria-pressed") == "false"

        answer_names = [
            (1, "B. 不能；她已留下與任務相關的判斷、線索和核對行動。"),
            (2, "A. 『再聽一次開頭的 sh，和 sip 比較後試讀。』"),
            (3, "B. 每人先排一張並指出一個線索；聽完同伴理由後，必要時修正。"),
        ]
        for index, name in answer_names:
            step = steps.nth(index)
            await step.get_by_role("button", name=name).focus()
            await page.keyboard.press("Enter")
            assert "可進入下一步" in await step.locator(".feedback").inner_text()

        await page.add_script_tag(content=axe)
        axe_result = await page.evaluate("""async (scope) => {
          const result = await axe.run(scope, { resultTypes: ['violations', 'incomplete'] });
          return { violations: result.violations, incomplete: result.incomplete };
        }""", await card.element_handle())
        assert not axe_result["violations"], axe_result["violations"]
        assert await activity.locator('[aria-live="polite"]').count() == 4
        assert await page.evaluate("matchMedia('(prefers-reduced-motion: reduce)').matches")

        responsive = []
        for width in (320, 375, 768):
            await page.set_viewport_size({"width": width, "height": 1100})
            size = await page.evaluate("({viewport: innerWidth, scroll: document.documentElement.scrollWidth})")
            assert size["scroll"] <= size["viewport"], size
            dimensions = await activity.locator("button[data-answer]").evaluate_all(
                "buttons => buttons.map(button => { const r = button.getBoundingClientRect(); return {width:r.width,height:r.height}; })"
            )
            assert all(item["width"] >= 44 and item["height"] >= 44 for item in dimensions), dimensions
            responsive.append({"width": width, "scrollWidth": size["scroll"]})

        assert not errors, errors
        counts = {"visibleSections": await sections.count(), "guidedChoiceSteps": await steps.count()}
        await browser.close()
        return {
            "status": "passed",
            **counts,
            "keyboardWrongRetryCorrect": True,
            "liveRegions": 4,
            "axeViolations": 0,
            "axeIncomplete": len(axe_result["incomplete"]),
            "reducedMotion": True,
            "responsive": responsive,
            "blockedExternalRequests": len(blocked),
            "blockedSimulationScript": blocked_simulations,
            "guidedChoiceFallbackUsable": True,
            "pageErrors": errors,
        }


def main() -> None:
    parser = argparse.ArgumentParser()
    parser.add_argument("--url", default="http://127.0.0.1:8765/site/index.html")
    args = parser.parse_args()
    print(asyncio.run(run(args.url)))


if __name__ == "__main__":
    main()
