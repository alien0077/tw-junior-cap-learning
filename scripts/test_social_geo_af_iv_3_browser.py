#!/usr/bin/env python3
"""Real-browser QA for the Af-IV-3 learner-facing lesson and four choices."""
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
        page = browser.new_page(viewport={"width": 375, "height": 900})
        page.route("**/*", lambda route: route.continue_() if route.request.url.startswith(("http://127.0.0.1:8765/", "http://localhost:8765/")) else route.abort())
        page.on("pageerror", lambda error: errors.append(str(error)))
        page.goto(args.url, wait_until="networkidle")
        page.get_by_label("搜尋我們的教材或題目").fill("區域發展空間差異")
        card = page.locator("#contentGrid article.card").filter(has_text="地 Af-Ⅳ-3：區域發展空間差異").first
        card.wait_for()
        sections = card.locator(".lesson-sections > article")
        section_texts = sections.all_inner_texts()
        authored_headings = [
            "一張就醫地圖提出問題：發展差異在哪裡？",
            "先把『區域發展空間差異』拆成四個可比較的問題",
            "三種證據拼出一個區域，而不是用排名代替理解",
            "區域差異會被自己的回饋機制放大",
            "方案不是把每個地方複製成同一座城市",
            "把課堂方法帶回自己的生活圈",
            "用四句話完成一個有界線的區域判斷",
        ]
        assert len(section_texts) >= len(authored_headings), section_texts
        assert [item.split("\n", 1)[0] for item in section_texts[-7:]] == authored_headings, section_texts
        lesson_text = "\n".join(section_texts)
        for phrase in ("一張就醫地圖", "四個可比較的問題", "三種證據", "回饋機制", "公平", "自己的生活圈", "四句話"):
            assert phrase in lesson_text, phrase

        activity = card.locator('.activity[data-lesson="lesson-social-content-geo-af-iv-3"]')
        assert activity.locator(".activity-step").count() == 4
        first = activity.locator(".activity-step").nth(0)
        first.locator('[data-answer="B"]').focus()
        page.keyboard.press("Enter")
        assert "年份、人口分母" in first.locator(".feedback").inner_text()
        first.locator('[data-answer="A"]').focus()
        page.keyboard.press("Enter")
        assert "可進入下一步" in first.locator(".feedback").inner_text()
        feedback_live = first.locator(".feedback").get_attribute("aria-live")
        assert feedback_live == "polite", feedback_live

        widths = {}
        for width in (320, 375, 768):
            page.set_viewport_size({"width": width, "height": 900})
            widths[str(width)] = page.evaluate("({body: document.body.scrollWidth, doc: document.documentElement.scrollWidth, client: document.documentElement.clientWidth})")
            assert widths[str(width)]["body"] <= width and widths[str(width)]["doc"] <= width, widths
        assert not errors, errors
        browser.close()
    print(json.dumps({"status": "passed", "url": args.url, "learnerVisibleSections": len(section_texts), "authoredTeachingSections": len(authored_headings), "guidedChoiceSteps": 4, "keyboardWrongRetryCorrect": True, "externalRequestsBlocked": True, "feedbackLiveRegion": feedback_live, "responsiveWidths": widths, "pageErrors": errors}, ensure_ascii=False))
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
