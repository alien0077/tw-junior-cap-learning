#!/usr/bin/env python3
"""Browser regression for the learner-visible English 7-IV-2 lesson."""
from __future__ import annotations

import argparse
import asyncio
import json
from pathlib import Path

from playwright.async_api import async_playwright

ROOT = Path(__file__).resolve().parents[1]
LESSON_ID = "lesson-english-performance-7-iv-2"
LESSON = json.loads((ROOT / "lessons/english/lesson-english-performance-7-iv-2.json").read_text(encoding="utf-8"))


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
        headings = await sections.locator("b").all_text_contents()
        assert headings == [section["heading"] for section in LESSON["teaching"]["body"]], headings
        activity = card
        lab = activity.locator(f'[data-reading-strategy-lab="{LESSON_ID}"]')
        await lab.wait_for()
        assert LESSON["interactive"]["steps"]
        initial_prompt = await lab.locator(".rsl-task h5").inner_text()
        assert initial_prompt == LESSON["interactive"]["steps"][0]["prompt"]
        await page.add_script_tag(content=axe)
        axe_result = await page.evaluate("""async (scope) => {
          const result = await axe.run(scope, { resultTypes: ['violations', 'incomplete'] });
          return { violations: result.violations, incomplete: result.incomplete };
        }""", await card.element_handle())
        assert not axe_result["violations"], axe_result["violations"]

        step = LESSON["interactive"]["steps"][0]
        wrong = chr((ord(step["answer"]) - 65 + 1) % 3 + 65)
        await lab.locator(f'[data-rsl-answer][value="{wrong}"]').focus()
        await page.keyboard.press("Space")
        await lab.get_by_role("button", name="檢查並前進").focus()
        await page.keyboard.press("Enter")
        assert step["retryHint"] in await lab.locator(".rsl-status").inner_text()

        for item in LESSON["interactive"]["steps"]:
            current_lab = activity.locator(f'[data-reading-strategy-lab="{LESSON_ID}"]')
            await current_lab.locator(f'[data-rsl-answer][value="{item["answer"]}"]').focus()
            await page.keyboard.press("Space")
            await current_lab.get_by_role("button", name="檢查並前進").focus()
            await page.keyboard.press("Enter")
        final_status = await activity.locator("[data-reading-strategy-lab] .rsl-status").inner_text()
        assert LESSON["interactive"]["completionMessage"] in final_status

        responsive = []
        for width in (320, 375, 768):
            await page.set_viewport_size({"width": width, "height": 1100})
            size = await page.evaluate("({viewport: innerWidth, scroll: document.documentElement.scrollWidth})")
            assert size["scroll"] <= size["viewport"], size
            responsive.append({"width": width, "scrollWidth": size["scroll"]})
        assert not errors, errors
        await browser.close()
        return {"status": "passed", "visibleSections": 6, "readingStrategySteps": 5,
                "keyboardWrongRetryAndCompletion": True, "axeViolations": 0,
                "axeIncomplete": len(axe_result["incomplete"]), "responsive": responsive,
                "blockedExternalRequests": len(blocked), "pageErrors": errors}


def main() -> None:
    parser = argparse.ArgumentParser()
    parser.add_argument("--url", default="http://127.0.0.1:8765/site/index.html")
    args = parser.parse_args()
    print(json.dumps(asyncio.run(run(args.url)), ensure_ascii=False))


if __name__ == "__main__":
    main()
