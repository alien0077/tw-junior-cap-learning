#!/usr/bin/env python3
"""Chromium regression for English 5-IV-8 original story-note interaction."""
from __future__ import annotations

import argparse
import asyncio
import json

from playwright.async_api import async_playwright


LESSON_ID = "lesson-english-performance-5-iv-8"


async def run(url: str) -> dict:
    page_errors: list[str] = []
    async with async_playwright() as playwright:
        browser = await playwright.chromium.launch(headless=True)
        page = await browser.new_page(viewport={"width": 375, "height": 1050}, reduced_motion="reduce")
        page.on("pageerror", lambda error: page_errors.append(str(error)))

        async def local_only(route):
            if route.request.url.startswith("http://127.0.0.1:8765/"):
                await route.continue_()
            else:
                await route.abort()

        await page.route("**/*", local_only)
        response = await page.goto(url, wait_until="networkidle", timeout=60_000)
        assert response and response.status == 200
        await page.locator("#search").fill("5-Ⅳ-8：聽簡單故事筆記")
        activity = page.locator(f'.activity[data-lesson="{LESSON_ID}"]')
        await activity.wait_for(timeout=30_000)
        card = page.locator(f'.card:has([data-lesson="{LESSON_ID}"])')
        sections = await card.locator(".lesson-sections article").count()
        steps = activity.locator(".activity-step")
        assert sections == 6, f"expected six visible authored sections, got {sections}"
        assert await steps.count() == 4
        await page.evaluate("""() => {
          window.__spokenStories = [];
          Object.defineProperty(window.speechSynthesis, 'speak', {configurable: true, writable: true, value: utterance => {
            window.__spokenStories.push({text: utterance.text, lang: utterance.lang, rate: utterance.rate});
            setTimeout(() => utterance.onend?.(), 0);
          }});
        }""")

        keys = ["A", "B", "C", "B"]
        for index, answer in enumerate(keys):
            step = steps.nth(index)
            transcript = step.locator("details")
            assert await transcript.count() == 1 and not await transcript.evaluate("el => el.open")
            play = step.get_by_role("button", name=f"播放第 {index + 1} 段英文對話")
            await play.focus()
            await page.keyboard.press("Enter")
            await page.wait_for_function("() => window.__spokenStories.length > 0")
            speech = await page.evaluate("window.__spokenStories.at(-1)")
            assert speech["lang"] == "en-US" and abs(speech["rate"] - 0.88) < 1e-5
            feedback = step.locator(".feedback")
            assert await feedback.get_attribute("aria-live") == "polite"
            options = step.locator("button[data-answer]")
            assert await options.count() == 3
            wrong = next(i for i, letter in enumerate("ABC") if letter != answer)
            await options.nth(wrong).focus()
            await page.keyboard.press("Enter")
            assert (await feedback.inner_text()).strip(), f"missing retry hint at story {index + 1}"
            await options.nth(ord(answer) - ord("A")).focus()
            await page.keyboard.press("Enter")
            assert "可進入下一步" in await feedback.inner_text()
            await transcript.locator("summary").focus()
            await page.keyboard.press("Enter")
            assert await transcript.evaluate("el => el.open")
            transcript_text = (await transcript.locator("p").inner_text()).replace("\n", " ")
            assert all(part.strip() in transcript_text for part in speech["text"].splitlines())

        assert len({item["text"] for item in await page.evaluate("window.__spokenStories")}) == 4
        await page.evaluate("Object.defineProperty(window, 'speechSynthesis', {configurable: true, value: undefined})")
        await steps.nth(0).get_by_role("button", name="播放第 1 段英文對話").click()
        assert "未提供語音播放" in await steps.nth(0).locator(".audio-status").inner_text()
        responsive = []
        for width in (320, 375, 768):
            await page.set_viewport_size({"width": width, "height": 1050})
            size = await page.evaluate("({viewport: innerWidth, scroll: document.documentElement.scrollWidth})")
            assert size["scroll"] <= size["viewport"], size
            responsive.append(size)
        assert not page_errors, page_errors
        await browser.close()
        return {"status": "passed", "sections": sections, "storySteps": len(keys), "speechApiMock": True,
                "keyboardRetryAndAnswer": True, "transcriptDisclosure": True, "speechFallback": True,
                "networkBlocked": True, "responsive": responsive, "pageErrors": page_errors}


def main() -> int:
    parser = argparse.ArgumentParser()
    parser.add_argument("--url", default="http://127.0.0.1:8765/site/index.html")
    args = parser.parse_args()
    print(json.dumps(asyncio.run(run(args.url)), ensure_ascii=False))
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
