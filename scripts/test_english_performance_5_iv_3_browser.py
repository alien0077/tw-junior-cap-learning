#!/usr/bin/env python3
"""Browser regression for original English 5-IV-3 conversation-response lesson."""
from __future__ import annotations

import argparse
import asyncio
import json

from playwright.async_api import async_playwright


LESSON_ID = "lesson-english-performance-5-iv-3"


async def run(url: str) -> dict:
    page_errors: list[str] = []
    blocked_simulation_requests: list[str] = []
    async with async_playwright() as playwright:
        browser = await playwright.chromium.launch(headless=True)
        page = await browser.new_page(viewport={"width": 375, "height": 900}, reduced_motion="reduce")
        page.on("pageerror", lambda error: page_errors.append(str(error)))

        async def local_only(route):
            if route.request.url.endswith("/site/simulations.js"):
                blocked_simulation_requests.append(route.request.url)
                await route.abort()
                return
            if route.request.url.startswith("http://127.0.0.1:8765/"):
                await route.continue_()
            else:
                await route.abort()

        await page.route("**/*", local_only)
        response = await page.goto(url, wait_until="networkidle", timeout=60_000)
        assert response and response.status == 200, "student page did not return HTTP 200"
        await page.locator("#search").fill("5-Ⅳ-3：常見問答回應")
        activity = page.locator(f'.activity[data-lesson="{LESSON_ID}"]')
        await activity.wait_for(timeout=30_000)
        assert blocked_simulation_requests, "simulation fallback was not exercised"
        card = page.locator(f'.card:has([data-lesson="{LESSON_ID}"])')
        sections = await card.locator(".lesson-sections article").count()
        steps = activity.locator(".activity-step")
        assert sections == 6, f"expected six visible sections; got {sections}"
        assert await steps.count() == 4
        for index in range(4):
            step = steps.nth(index)
            buttons = step.locator("button[data-answer]")
            feedback = step.locator(".feedback")
            assert await feedback.get_attribute("aria-live") == "polite"
            for j in range(await buttons.count()):
                label = (await buttons.nth(j).inner_text()).strip()
                assert await step.get_by_role("button", name=label, exact=True).count() == 1
            await buttons.nth(1).focus()
            await page.keyboard.press("Enter")
            assert (await feedback.inner_text()).strip(), f"step {index + 1} did not give retry feedback"
            await buttons.nth(0).focus()
            await page.keyboard.press("Enter")
            assert "可進入下一步" in await feedback.inner_text(), f"step {index + 1} did not show its answer explanation"
        responsive = []
        for width in (320, 375, 768):
            await page.set_viewport_size({"width": width, "height": 900})
            dimensions = await page.evaluate("({viewport: innerWidth, scroll: document.documentElement.scrollWidth})")
            assert dimensions["scroll"] <= dimensions["viewport"], dimensions
            responsive.append(dimensions)
        assert not page_errors, page_errors
        await browser.close()
        return {"status": "passed", "url": url, "sections": sections, "steps": 4,
                "keyboardRetryAndAnswer": True, "ariaLive": True, "accessibleOptions": True,
                "reducedMotion": "emulated", "externalNetworkBlocked": True,
                "simulationScriptBlocked": blocked_simulation_requests,
                "guidedChoiceFallbackUsable": True,
                "responsive": responsive, "pageErrors": page_errors}


def main() -> int:
    parser = argparse.ArgumentParser()
    parser.add_argument("--url", default="http://127.0.0.1:8765/site/index.html")
    args = parser.parse_args()
    print(json.dumps(asyncio.run(run(args.url)), ensure_ascii=False))
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
