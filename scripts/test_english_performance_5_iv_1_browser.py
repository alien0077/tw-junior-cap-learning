#!/usr/bin/env python3
"""Browser regression for the authored 5-IV-1 vocabulary lesson interaction."""
from __future__ import annotations

import argparse
import asyncio
import json

from playwright.async_api import async_playwright


async def run(url: str) -> dict:
    page_errors: list[str] = []
    blocked_simulation_requests: list[str] = []
    async with async_playwright() as playwright:
        browser = await playwright.chromium.launch(headless=True)
        page = await browser.new_page(
            viewport={"width": 375, "height": 900}, reduced_motion="reduce"
        )
        page.on("pageerror", lambda error: page_errors.append(str(error)))
        local_origin = "http://127.0.0.1:8765"

        async def local_only(route):
            if route.request.url.endswith("/site/simulations.js"):
                blocked_simulation_requests.append(route.request.url)
                await route.abort()
                return
            if route.request.url.startswith(local_origin + "/"):
                await route.continue_()
            else:
                await route.abort()

        await page.route("**/*", local_only)
        response = await page.goto(url, wait_until="networkidle", timeout=60_000)
        assert response and response.status == 200, "student page did not return HTTP 200"

        await page.locator("#search").fill("5-Ⅳ-1：基本字彙理解使用")
        activity = page.locator(
            '.activity[data-lesson="lesson-english-performance-5-iv-1"]'
        )
        await activity.wait_for(timeout=30_000)
        assert blocked_simulation_requests, "simulation fallback was not exercised"
        lesson_card = page.locator('.card:has([data-lesson="lesson-english-performance-5-iv-1"])')
        section_count = await lesson_card.locator(".lesson-sections article").count()
        step_count = await activity.locator(".activity-step").count()
        assert section_count >= 6, f"expected six authored sections, saw {section_count}"
        assert step_count == 4, f"expected four interaction steps, saw {step_count}"

        for index in range(step_count):
            step = activity.locator(".activity-step").nth(index)
            buttons = step.locator("button[data-answer]")
            feedback = step.locator(".feedback")
            assert await feedback.get_attribute("aria-live") == "polite"
            for option_index in range(await buttons.count()):
                option_text = (await buttons.nth(option_index).inner_text()).strip()
                assert await step.get_by_role("button", name=option_text, exact=True).count() == 1
            await buttons.nth(1).focus()
            await page.keyboard.press("Enter")
            retry = (await feedback.inner_text()).strip()
            assert retry, f"step {index + 1} did not show retry feedback"
            await buttons.nth(0).focus()
            await page.keyboard.press("Enter")
            explanation = await feedback.inner_text()
            assert "可進入下一步" in explanation, (
                f"step {index + 1} did not show correct-answer explanation"
            )

        responsive: list[dict[str, int]] = []
        for width in (320, 375, 768):
            await page.set_viewport_size({"width": width, "height": 900})
            await page.wait_for_timeout(120)
            dimensions = await page.evaluate(
                "({viewport: innerWidth, scroll: document.documentElement.scrollWidth})"
            )
            assert dimensions["scroll"] <= dimensions["viewport"], dimensions
            responsive.append(dimensions)

        assert not page_errors, page_errors
        result = {
            "status": "passed",
            "url": page.url,
            "httpStatus": response.status,
            "authoredSections": section_count,
            "guidedChoiceSteps": step_count,
            "keyboardWrongRetryCorrect": True,
            "feedbackLiveRegion": True,
            "optionAccessibleNames": True,
            "reducedMotion": "emulated",
            "externalNetworkBlocked": True,
            "simulationScriptBlocked": blocked_simulation_requests,
            "guidedChoiceFallbackUsable": True,
            "responsive": responsive,
            "pageErrors": page_errors,
        }
        await browser.close()
        return result


def main() -> int:
    parser = argparse.ArgumentParser()
    parser.add_argument(
        "--url", default="http://127.0.0.1:8765/site/index.html"
    )
    args = parser.parse_args()
    print(json.dumps(asyncio.run(run(args.url)), ensure_ascii=False))
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
