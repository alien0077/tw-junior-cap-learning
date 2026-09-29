#!/usr/bin/env python3
"""Browser regression for English 5-IV-7 listening notes and local speech playback."""
from __future__ import annotations

import argparse
import asyncio
import json

from playwright.async_api import async_playwright


LESSON_ID = "lesson-english-performance-5-iv-7"


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
        assert response and response.status == 200, "student page did not return HTTP 200"
        await page.locator("#search").fill("5-Ⅳ-7：聽日常對話筆記")
        activity = page.locator(f'.activity[data-lesson="{LESSON_ID}"]')
        await activity.wait_for(timeout=30_000)
        card = page.locator(f'.card:has([data-lesson="{LESSON_ID}"])')
        sections = await card.locator(".lesson-sections article").count()
        steps = activity.locator(".activity-step")
        assert sections == 6, f"expected six authored visible sections, got {sections}"
        assert await steps.count() == 4, f"expected four listening tasks, got {await steps.count()}"

        # Keep the real UI event/data path deterministic without claiming to measure human hearing.
        await page.evaluate("""() => {
          window.__spokenScripts = [];
          Object.defineProperty(window.speechSynthesis, 'speak', {configurable: true, writable: true, value: utterance => {
            window.__spokenScripts.push({text: utterance.text, lang: utterance.lang, rate: utterance.rate});
            setTimeout(() => utterance.onend?.(), 0);
          }});
        }""")

        answer_keys = ["A", "B", "A", "B"]
        scripts = []
        for index, key in enumerate(answer_keys):
            step = steps.nth(index)
            transcript = step.locator("details")
            assert await transcript.count() == 1
            assert not await transcript.evaluate("node => node.open"), "transcript must start collapsed"
            play = step.get_by_role("button", name=f"播放第 {index + 1} 段英文對話")
            await play.focus()
            await page.keyboard.press("Enter")
            status = step.locator(".audio-status")
            await page.wait_for_function("() => window.__spokenScripts.length > 0")
            spoken = await page.evaluate("window.__spokenScripts.at(-1)")
            assert spoken["lang"] == "en-US" and abs(spoken["rate"] - 0.88) < 1e-5
            scripts.append(spoken["text"])
            await status.evaluate("el => new Promise(resolve => { const poll = () => el.textContent.includes('播放結束') ? resolve(true) : setTimeout(poll, 10); poll(); })")
            assert not await transcript.evaluate("node => node.open")
            buttons = step.locator("button[data-answer]")
            assert await buttons.count() == 3
            feedback = step.locator(".feedback")
            assert await feedback.get_attribute("aria-live") == "polite"
            wrong = next(i for i, letter in enumerate("ABC") if letter != key)
            await buttons.nth(wrong).focus()
            await page.keyboard.press("Enter")
            assert (await feedback.inner_text()).strip(), f"step {index + 1} missing retry hint"
            await buttons.nth(ord(key) - ord("A")).focus()
            await page.keyboard.press("Enter")
            assert "可進入下一步" in await feedback.inner_text(), f"step {index + 1} missing explanation"
            await transcript.locator("summary").focus()
            await page.keyboard.press("Enter")
            assert await transcript.evaluate("node => node.open"), "transcript should open by keyboard"
            transcript_text = (await transcript.locator("p").inner_text()).replace("\n", " ")
            assert all(part.strip() in transcript_text for part in spoken["text"].splitlines())
        assert len(set(scripts)) == 4, "each listening task must use its own original dialogue"
        await page.evaluate("Object.defineProperty(window, 'speechSynthesis', {configurable: true, value: undefined})")
        await steps.nth(0).get_by_role("button", name="播放第 1 段英文對話").click()
        assert "未提供語音播放" in await steps.nth(0).locator(".audio-status").inner_text()
        assert await steps.nth(0).locator("details").evaluate("node => node.open"), "transcript fallback remains available"

        responsive = []
        for width in (320, 375, 768):
            await page.set_viewport_size({"width": width, "height": 1050})
            size = await page.evaluate("({viewport: innerWidth, scroll: document.documentElement.scrollWidth})")
            assert size["scroll"] <= size["viewport"], size
            responsive.append(size)
        assert not page_errors, page_errors
        await browser.close()
        return {"status": "passed", "url": url, "sections": sections, "steps": 4,
                "speechSynthesisDataPath": "mocked API, real page controls and data binding exercised",
                "keyboardPlaybackAndAnswers": True, "collapsedTranscriptAndKeyboardDisclosure": True,
                "speechUnavailableFallback": True, "ariaLive": True, "externalNetworkBlocked": True, "responsive": responsive,
                "pageErrors": page_errors}


def main() -> int:
    parser = argparse.ArgumentParser()
    parser.add_argument("--url", default="http://127.0.0.1:8765/site/index.html")
    args = parser.parse_args()
    print(json.dumps(asyncio.run(run(args.url)), ensure_ascii=False))
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
