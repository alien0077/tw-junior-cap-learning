#!/usr/bin/env python3
"""Exercise the rendered A-8-2 guided activity in real Chromium at narrow and desktop widths."""
from __future__ import annotations

import argparse
import asyncio
import json
from pathlib import Path

from playwright.async_api import async_playwright


async def run(url: str, screenshot: Path) -> dict:
    async with async_playwright() as playwright:
        browser = await playwright.chromium.launch(channel="chrome", headless=True)
        page = await browser.new_page(viewport={"width": 1280, "height": 1000})
        await page.goto(url, wait_until="networkidle")
        await page.select_option("#unit", "cur-math-content-a-8-2")
        activity = page.locator(".guided-activity")
        assert await activity.locator("h4").inner_text() == "多項式標記台：讀出項數、係數、常數與項次"
        progress = activity.locator(".guided-activity-progress")
        prompt = activity.locator("label")
        answer = activity.locator("input")
        submit = activity.locator("button")
        hint = activity.locator(".guided-activity-hint")
        completed = []
        for step, accepted in enumerate(("4", "−1、4、−9", "7x⁴，4", "1−3x+2x⁴"), start=1):
            assert await progress.inner_text() == f"第 {step}/4 步"
            prompt_text = await prompt.inner_text()
            assert prompt_text.strip(), (step, prompt_text)
            assert await answer.is_visible()
            await answer.fill("明顯錯誤")
            await submit.click()
            assert "還不符合條件" in await activity.locator(".guided-activity-feedback").inner_text()
            assert await hint.is_visible()
            assert await progress.inner_text() == f"第 {step}/4 步"
            await answer.fill(accepted)
            await submit.click()
            assert not await hint.is_visible()
            completed.append(step)
        assert await progress.inner_text() == "已完成 4/4 步"
        assert "你已能分辨項數" in await activity.inner_text()
        await page.set_viewport_size({"width": 320, "height": 900})
        dimensions = await page.evaluate("""() => ({
          body: document.body.scrollWidth,
          document: document.documentElement.scrollWidth,
          client: document.documentElement.clientWidth,
          activity: document.querySelector('.guided-activity').getBoundingClientRect().width
        })""")
        assert dimensions["body"] <= 320 and dimensions["document"] <= 320, dimensions
        screenshot.parent.mkdir(parents=True, exist_ok=True)
        await activity.screenshot(path=str(screenshot))
        await browser.close()
        return {"status": "passed", "unit": "cur-math-content-a-8-2", "stepsCompleted": completed,
                "wrongAnswerRetry": "passed", "responsive320": dimensions, "screenshot": str(screenshot)}


def main() -> int:
    parser = argparse.ArgumentParser()
    parser.add_argument("--url", default="http://127.0.0.1:8765/implementation/workbench.html")
    parser.add_argument("--screenshot", type=Path, default=Path("/private/tmp/a82-workbench.png"))
    args = parser.parse_args()
    result = asyncio.run(run(args.url, args.screenshot))
    print(json.dumps(result, ensure_ascii=False))
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
