#!/usr/bin/env python3
"""Real Chromium regression for the Ca-IV-2 learner lesson and evidence lab."""
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
        page.get_by_label("搜尋我們的教材或題目").fill("Ca-Ⅳ-2")
        card = page.locator(".card").filter(has_text="Ca-Ⅳ-2：以化學性質鑑定化合物").first
        card.wait_for()
        assert card.locator(".lesson-sections article").count() == 7
        for heading in (
            "未知白色粉末的身分謎題",
            "自編案例：辨認三瓶透明溶液",
            "建立反應指紋表",
            "遷移：辨識水垢與清潔劑的風險",
            "鑑定報告的最後一行不能過度自信",
        ):
            assert card.locator(".lesson-sections").inner_text().count(heading) == 1

        steps = [
            ("A", "先排除任何直接嗅聞"),
            ("A", "把『可直接由指示劑得知的性質』"),
            ("B", "尋找兩個原理不同"),
            ("B", "相同試劑再做一次不算獨立檢驗"),
        ]
        for index, (wrong_answer, retry_hint) in enumerate(steps):
            activity = card.locator(".activity-step").nth(index)
            activity.locator(f'[data-answer="{wrong_answer}"]').click()
            assert retry_hint in activity.locator(".feedback").inner_text()
        for index, correct_answer in enumerate(("B", "B", "A", "C")):
            activity = card.locator(".activity-step").nth(index)
            activity.locator(f'[data-answer="{correct_answer}"]').click()
            assert "可進入下一步" in activity.locator(".feedback").inner_text()

        lab = card.locator(".sim-chemical-id")
        assert lab.count() == 1
        assert "不是實驗步驟或真實化學品操作指引" in lab.inner_text()
        lab.get_by_label("檢驗方法").select_option("carbonateCheck")
        run = lab.get_by_role("button", name="執行虛擬檢驗")
        run.focus()
        page.keyboard.press("Enter")
        assert "氣體通入石灰水後變混濁" in lab.inner_text()
        assert "支持生成二氧化碳" in lab.inner_text()
        assert run.evaluate("el => document.activeElement === el"), "focus should remain on the activated control"

        lab.get_by_label("樣品對照").select_option("blank")
        run = lab.get_by_role("button", name="執行虛擬檢驗")
        run.click()
        assert "空白對照沒有顯色或產氣變化" in lab.inner_text()
        assert "不能用來判定未知樣品身分" in lab.inner_text()

        widths = {}
        for width in (320, 375, 768):
            page.set_viewport_size({"width": width, "height": 1000})
            widths[str(width)] = page.evaluate("({body: document.body.scrollWidth, document: document.documentElement.scrollWidth, client: document.documentElement.clientWidth})")
            overflow = page.evaluate("""() => { const card=[...document.querySelectorAll('.card')].find(el=>el.innerText.includes('Ca-Ⅳ-2：以化學性質鑑定化合物')); return [...card.querySelectorAll('*')].map(el=>({tag:el.tagName,cls:el.className?.toString(),text:el.innerText?.slice(0,65),left:Math.round(el.getBoundingClientRect().left),right:Math.round(el.getBoundingClientRect().right),width:Math.round(el.getBoundingClientRect().width),scrollWidth:el.scrollWidth,clientWidth:el.clientWidth,minWidth:getComputedStyle(el).minWidth,display:getComputedStyle(el).display})).filter(x=>x.right>innerWidth||x.scrollWidth>x.clientWidth).sort((a,b)=>b.right-a.right).slice(0,20) }""")
            layout = page.evaluate("""() => {const card=[...document.querySelectorAll('.card')].find(el=>el.innerText.includes('Ca-Ⅳ-2：以化學性質鑑定化合物'));const out=[];for(let el=card;el;el=el.parentElement){const r=el.getBoundingClientRect(),s=getComputedStyle(el);out.push({tag:el.tagName,id:el.id,cls:el.className?.toString(),left:Math.round(r.left),right:Math.round(r.right),width:Math.round(r.width),grid:s.gridTemplateColumns,padding:s.padding});}return out}""")
            assert widths[str(width)]["body"] <= width and widths[str(width)]["document"] <= width, {"metrics": widths, "layout": layout, "overflowingElements": overflow}
        assert not errors, errors
        browser.close()
    print(json.dumps({"status": "passed", "unit": "Ca-IV-2", "visibleLessonSections": 7, "quizSteps": 4, "retryHints": 4, "virtualEvidenceTests": 2, "keyboard": True, "responsiveWidths": widths, "pageErrors": errors}, ensure_ascii=False))
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
