#!/usr/bin/env python3
"""Real-browser regression for the Ca-IV-1 learner lesson and separation lab."""
from __future__ import annotations

import argparse
import json
import os
from pathlib import Path

from playwright.sync_api import sync_playwright


def main() -> int:
    parser = argparse.ArgumentParser()
    parser.add_argument("--url", default="http://127.0.0.1:8765/site/index.html")
    args = parser.parse_args()
    chrome = Path(os.environ.get("TW_BROWSER_CHROME", "/Applications/Google Chrome.app/Contents/MacOS/Google Chrome"))
    errors: list[str] = []
    with sync_playwright() as playwright:
        launch = {"headless": True}
        if chrome.is_file():
            launch["executable_path"] = str(chrome)
        browser = playwright.chromium.launch(**launch)
        page = browser.new_page(viewport={"width": 375, "height": 1000})
        page.on("pageerror", lambda error: errors.append(str(error)))
        page.goto(args.url, wait_until="networkidle")
        page.get_by_label("搜尋我們的教材或題目").fill("Ca-Ⅳ-1")
        card = page.locator(".card").filter(has_text="Ca-Ⅳ-1：實驗分離混合物").first
        card.wait_for()
        assert card.locator(".lesson-sections article").count() == 7
        for heading in (
            "先別拿濾紙：這罐混合物到底要救回什麼？",
            "三種成分，逐站交接",
            "換一個問題：色水要留下顏料，還是留下水？",
        ):
            assert card.locator(".lesson-sections").inner_text().count(heading) == 1

        activity = card.locator(".activity-step").first
        activity.locator('[data-answer="B"]').click()
        assert "三種材料各自有哪些不同物性" in activity.locator(".feedback").inner_text()
        activity.locator('[data-answer="A"]').click()
        assert "磁選利用鐵屑會受磁力吸引" in activity.locator(".feedback").inner_text()

        actions = [
            "隔著紙套用磁鐵取出鐵屑",
            "對鹽砂殘料加水攪拌後過濾",
            "按回收目標選蒸發結晶取鹽",
            "盤點鐵屑、砂、鹽晶、濾渣",
        ]
        steps = card.locator("[data-design-step]")
        assert steps.count() == 4
        for index, action in enumerate(actions):
            current = card.locator(f'[data-design-step="{index}"]')
            current.focus()
            page.keyboard.press("Enter")
            card.locator(f'[data-design-step="{index}"][aria-current="step"]').wait_for()
            assert action in card.locator(".sim-design").inner_text()

        widths = {}
        for width in (320, 375, 768):
            page.set_viewport_size({"width": width, "height": 1000})
            widths[str(width)] = page.evaluate("({body: document.body.scrollWidth, document: document.documentElement.scrollWidth, client: document.documentElement.clientWidth})")
            assert widths[str(width)]["body"] <= width and widths[str(width)]["document"] <= width, widths
        assert not errors, errors
        browser.close()
    print(json.dumps({"status": "passed", "unit": "Ca-Ⅳ-1", "visibleLessonSections": 7, "interactionStages": len(actions), "wrongAnswerRetry": True, "keyboard": True, "responsiveWidths": widths, "pageErrors": errors}, ensure_ascii=False))
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
