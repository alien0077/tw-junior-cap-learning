#!/usr/bin/env python3
"""Verify Ac-IV-3 authored lesson, three-step feedback, keyboard, and mobile layout."""
from __future__ import annotations

import argparse
import asyncio
import json
import os
from pathlib import Path

from playwright.async_api import async_playwright


async def main(url: str) -> None:
    async with async_playwright() as playwright:
        launch_options = {"headless": True}
        chrome = Path(os.environ.get("TW_BROWSER_CHROME", "/Applications/Google Chrome.app/Contents/MacOS/Google Chrome"))
        if chrome.is_file():
            launch_options["executable_path"] = str(chrome)
        browser = await playwright.chromium.launch(**launch_options)
        page = await browser.new_page(viewport={"width": 375, "height": 900})
        errors: list[str] = []
        page.on("pageerror", lambda error: errors.append(str(error)))
        await page.goto(url, wait_until="networkidle")
        await page.locator("#search").fill("lesson-chinese-content-ac-iv-3")
        card = page.locator('#contentGrid article.card').filter(
            has=page.locator("h3", has_text="Ac-Ⅳ-3：搭建可檢查的文句推論")
        )
        await card.wait_for()
        sections = card.locator(".lesson-sections > article")
        headings = await sections.locator("b").all_inner_texts()
        expected = [
            "剩下的飯菜，不能直接說成全校的心聲",
            "搭一座推論橋，每一格都要有名字",
            "把過度結論縮回證據半徑",
            "資料桌上的偵錯站",
            "替餐廳寫一頁不誇張的建議書",
            "讓你的結論能接受追問",
        ]
        assert headings == expected, headings
        activity = card.locator('.activity[data-lesson="lesson-chinese-content-ac-iv-3"]')
        steps = activity.locator(".activity-step")
        assert await steps.count() == 3
        for i in range(3):
            assert await steps.nth(i).locator("button[data-answer]").count() == 3
        first = steps.nth(0)
        await first.locator('[data-answer="A"]').click()
        assert "數字猜心理原因" in await first.locator(".feedback").inner_text()
        await first.locator('[data-answer="B"]').focus()
        await page.keyboard.press("Enter")
        assert "可進入下一步" in await first.locator(".feedback").inner_text()
        second = steps.nth(1)
        await second.locator('[data-answer="B"]').click()
        assert "全校" in await second.locator(".feedback").inner_text()
        await second.locator('[data-answer="A"]').click()
        assert "不等於證明因果" in await second.locator(".feedback").inner_text()
        third = steps.nth(2)
        await third.locator('[data-answer="C"]').click()
        assert "全校代表性及原因" in await third.locator(".feedback").inner_text()
        viewports = {}
        for width in (320, 375, 768):
            await page.set_viewport_size({"width": width, "height": 900})
            metrics = await page.evaluate("""() => ({body: document.body.scrollWidth, doc: document.documentElement.scrollWidth, client: document.documentElement.clientWidth})""")
            assert metrics["body"] <= width and metrics["doc"] <= width, (width, metrics)
            viewports[str(width)] = metrics
        assert not errors, errors
        print(json.dumps({"status": "passed", "lessonId": "lesson-chinese-content-ac-iv-3", "visibleAuthoredSections": headings, "guidedChoiceSteps": 3, "wrongAnswerRetry": True, "keyboardRetry": True, "scopeAndCausalityFeedback": True, "viewports": viewports, "pageErrors": errors}, ensure_ascii=False))
        await browser.close()


if __name__ == "__main__":
    parser = argparse.ArgumentParser()
    parser.add_argument("--url", default="http://127.0.0.1:8765/site/index.html")
    asyncio.run(main(parser.parse_args().url))
