#!/usr/bin/env python3
"""Real-browser QA for the Af-IV-2 learner-facing lesson and four choices."""
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
        page.on("pageerror", lambda error: errors.append(str(error)))
        page.goto(args.url, wait_until="networkidle")
        page.get_by_label("搜尋我們的教材或題目").fill("都市發展與都市化")
        card = page.locator("#contentGrid article.card").filter(has_text="地 Af-Ⅳ-2：都市發展與都市化").first
        card.wait_for()
        sections = card.locator(".lesson-sections > article")
        assert sections.count() == 6
        lesson_text = "\n".join(sections.all_inner_texts())
        for phrase in ("河港地區的變遷", "核心夜間人口下降", "都會區的形成", "不能說所有人搬進市中心"):
            assert phrase in lesson_text, phrase

        activity = card.locator('.activity[data-lesson="lesson-social-content-geo-af-iv-2"]')
        assert activity.locator(".activity-step").count() == 4
        first = activity.locator(".activity-step").nth(0)
        first.locator('[data-answer="B"]').focus()
        page.keyboard.press("Enter")
        assert "再想一次" in first.locator(".feedback").inner_text()
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
    print(json.dumps({"status": "passed", "url": args.url, "learnerVisibleSections": 6, "guidedChoiceSteps": 4, "keyboardWrongRetryCorrect": True, "feedbackLiveRegion": feedback_live, "responsiveWidths": widths, "pageErrors": errors}, ensure_ascii=False))
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
