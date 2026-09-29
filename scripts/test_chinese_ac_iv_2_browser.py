#!/usr/bin/env python3
"""Verify the published Ac-IV-2 lesson text and guided-choice behavior in Chromium."""
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
        await page.locator("#search").fill("lesson-chinese-content-ac-iv-2")
        card = page.locator('#contentGrid article.card').filter(
            has=page.locator("h3", has_text="Ac-Ⅳ-2：敘事有無判斷表態等句型")
        )
        await card.wait_for()
        sections = card.locator(".lesson-sections > article")
        section_count = await sections.count()
        assert section_count == 7, f"visible section count={section_count}; card={await card.inner_text()}"
        headings = await sections.locator("b").all_inner_texts()
        assert headings == [
            "公告還沒貼好，先看句子把焦點放哪裡",
            "先找述語，再判它扮演的工作",
            "把同一張公告拆成四個可核對的鏡頭",
            "碰到『有』或『是』，先拆成分別急著分類",
            "引導練習：替招募公告做句型標籤",
            "遷移：同一消息，改變句型也改變讀者先看到的資訊",
            "離開前做一次反例檢查",
        ], headings
        activity = card.locator('.activity[data-lesson="lesson-chinese-content-ac-iv-2"]')
        steps = activity.locator(".activity-step")
        assert await steps.count() == 5
        for i in range(5):
            assert await steps.nth(i).locator("button[data-answer]").count() == 3
        first = steps.nth(0)
        await first.locator('[data-answer="B"]').click()
        assert "再看" in await first.locator(".feedback").inner_text()
        await first.locator('[data-answer="A"]').focus()
        await page.keyboard.press("Enter")
        assert "可進入下一步" in await first.locator(".feedback").inner_text()
        last = steps.nth(4)
        await last.locator('[data-answer="B"]').click()
        assert "歧義" in await last.locator(".feedback").inner_text() or "兩種" in await last.locator(".feedback").inner_text() or "敘事或表態讀法" in await last.locator(".feedback").inner_text()
        viewports = {}
        for width in (320, 375, 768):
            await page.set_viewport_size({"width": width, "height": 900})
            metrics = await page.evaluate("""() => ({body: document.body.scrollWidth, doc: document.documentElement.scrollWidth, client: document.documentElement.clientWidth})""")
            assert metrics["body"] <= width and metrics["doc"] <= width, (width, metrics)
            viewports[str(width)] = metrics
        assert not errors, errors
        print(json.dumps({"status": "passed", "lessonId": "lesson-chinese-content-ac-iv-2", "visibleSections": headings, "guidedChoiceSteps": 5, "wrongAnswerHint": True, "keyboardRetry": True, "ambiguityFeedback": True, "viewports": viewports, "pageErrors": errors}, ensure_ascii=False))
        await browser.close()


if __name__ == "__main__":
    parser = argparse.ArgumentParser()
    parser.add_argument("--url", default="http://127.0.0.1:8765/site/index.html")
    asyncio.run(main(parser.parse_args().url))
