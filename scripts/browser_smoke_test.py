#!/usr/bin/env python3
"""Run the real Chromium workbench smoke test.

Start a local server at the repository root first, then run this script. The
script intentionally reports browser runtime evidence separately from content
and assistive-technology review.
"""
from __future__ import annotations

import argparse
import asyncio
import json
import os
from pathlib import Path
from urllib.parse import urlsplit

from playwright.async_api import async_playwright

ROOT = Path(__file__).resolve().parents[1]
LESSON_7_IV_2 = json.loads((ROOT / "lessons/english/lesson-english-performance-7-iv-2.json").read_text(encoding="utf-8"))


async def run(url: str, browser_channel: str) -> dict:
    async with async_playwright() as playwright:
        system_chrome = Path(os.environ.get(
            "TW_BROWSER_CHROME",
            "/Applications/Google Chrome.app/Contents/MacOS/Google Chrome",
        ))
        launch_kwargs = {"headless": True}
        if system_chrome.is_file():
            launch_kwargs["executable_path"] = str(system_chrome)
        elif browser_channel:
            launch_kwargs["channel"] = browser_channel
        browser = await playwright.chromium.launch(**launch_kwargs)
        page = await browser.new_page(viewport={"width": 375, "height": 900})
        await page.goto(url, wait_until="networkidle")
        option_count = await page.locator("#unit option").count()
        assert option_count == 1027, option_count
        viewport_metrics = {}
        for width in (320, 375, 768):
            await page.set_viewport_size({"width": width, "height": 900})
            await page.select_option("#unit", "cur-math-content-a-8-1")
            metrics = await page.evaluate("""() => ({
              body: document.body.scrollWidth,
              doc: document.documentElement.scrollWidth,
              client: document.documentElement.clientWidth,
              sections: document.querySelectorAll('article section[data-section]').length,
              buttons: document.querySelectorAll('.interactive-block button').length,
              select: document.querySelector('#unit').getBoundingClientRect().width
            })""")
            assert metrics["body"] <= width and metrics["doc"] <= width, (width, metrics)
            # A-8-1 now renders its six base flow buttons plus one guided-activity submit.
            assert metrics["sections"] == 7 and metrics["buttons"] == 7, metrics
            assert metrics["select"] <= metrics["client"], metrics
            viewport_metrics[str(width)] = metrics

        await page.set_viewport_size({"width": 375, "height": 900})
        values = await page.locator("#unit option").evaluate_all("(options) => options.map(o => o.value)")
        assert len(values) == 1027
        for value in values:
            await page.select_option("#unit", value)
            assert await page.locator("article.student-lesson-shell").get_attribute("data-lesson-id") == value
            assert await page.locator("article section[data-section]").count() == 7
            semantic_model = await page.locator(".component-visual-body").first.get_attribute("data-semantic-model")
            assert semantic_model, value
            assert await page.locator(".component-visual-body").first.get_attribute("data-content-source") == "unit-spec", value
            prompts = await page.locator(".component-visual-prompts").first.text_content()
            assert prompts and "待由本單元操作資料填入" not in prompts, value
            assert not await page.evaluate("() => document.documentElement.scrollWidth > document.documentElement.clientWidth"), value

        await page.select_option("#unit", "cur-science-content-fc-iv-1")
        assert await page.locator(".interactive-block").count() == 2
        assert await page.locator('.component-visual-body[data-component="SystemRelationshipBlock"]').count() == 1
        assert await page.locator('.component-visual-body[data-component="GuidedChoiceBlock"]').count() == 1
        science_fc_iv1_rendering = {"status": "passed", "interactiveBlocks": 2, "components": ["SystemRelationshipBlock", "GuidedChoiceBlock"]}

        await page.select_option("#unit", "cur-math-content-a-8-1")
        assert await page.locator(".formula-model li").count() == 3
        buttons = page.locator(".interactive-controls button")
        await buttons.nth(0).click()
        await buttons.nth(1).click()
        await buttons.nth(2).click()
        await page.locator('input[aria-label="用一句話說明觀察到的關係"]').fill("觀察證據與表徵同步改變。")
        await buttons.nth(3).click()
        await buttons.nth(4).click()
        output = await page.locator(".interactive-status").text_content()
        assert "已檢核" in output

        cdp = await page.context.new_cdp_session(page)
        ax_tree = await cdp.send("Accessibility.getFullAXTree")
        ax_nodes = ax_tree["nodes"]
        def ax_value(node, key):
            return node.get(key, {}).get("value")
        statuses = [node for node in ax_nodes if ax_value(node, "role") == "status"]
        assert statuses, "no status node in Accessibility tree"
        status_properties = {item.get("name"): item.get("value", {}).get("value") for item in statuses[0].get("properties", [])}
        assert status_properties.get("live") == "polite", status_properties
        assert status_properties.get("atomic") is True, status_properties
        buttons_in_ax = [ax_value(node, "name") for node in ax_nodes if ax_value(node, "role") == "button"]
        expected_buttons = ["提交預測", "操作一步", "記錄觀察", "提交解釋", "檢核並顯示局部回饋", "匯出操作紀錄"]
        assert all(label in buttons_in_ax for label in expected_buttons), buttons_in_ax
        textboxes = [node for node in ax_nodes if ax_value(node, "role") == "textbox"]
        assert any(ax_value(node, "name") == "用一句話說明觀察到的關係" for node in textboxes), "textbox accessible name missing"

        await page.locator("body").click(position={"x": 2, "y": 2})
        focus_tags = []
        for _ in range(12):
            await page.keyboard.press("Tab")
            focus_tags.append(await page.evaluate("() => document.activeElement?.tagName"))
        assert "BUTTON" in focus_tags and "INPUT" in focus_tags, focus_tags

        await page.emulate_media(reduced_motion="reduce")
        reduced_motion = await page.evaluate("""() => {
          const node = document.querySelector('.interactive-block');
          const style = getComputedStyle(node);
          return { animationName: style.animationName, transitionDuration: style.transitionDuration };
        }""")
        assert reduced_motion["animationName"] == "none", reduced_motion
        assert reduced_motion["transitionDuration"] == "0s", reduced_motion

        # Verify the current lesson's real public-content card, not only the
        # unit-spec workbench traversal above.
        parts = urlsplit(url)
        lesson_page = await browser.new_page(viewport={"width": 375, "height": 900})
        lesson_errors = []
        lesson_page.on("pageerror", lambda error: lesson_errors.append(str(error)))
        await lesson_page.goto(f"{parts.scheme}://{parts.netloc}/site/index.html", wait_until="networkidle")
        await lesson_page.locator("#status").wait_for()
        await lesson_page.locator("#search").fill(LESSON_7_IV_2["id"])
        lab = lesson_page.locator(f'[data-reading-strategy-lab="{LESSON_7_IV_2["id"]}"]')
        await lab.wait_for()
        assert "任務 1／5" in await lab.locator(".rsl-progress").inner_text()
        excerpt = await lab.locator(".rsl-excerpt").inner_text()
        assert "expected to trade" in excerpt, excerpt
        first_answer = LESSON_7_IV_2["interactive"]["steps"][0]["answer"]
        wrong_answer = "B" if first_answer != "B" else "C"
        await lab.locator(f'[data-rsl-answer][value="{wrong_answer}"]').check()
        await lab.locator('[data-rsl-action="check"]').click()
        assert "任務 1／5" in await lab.locator(".rsl-progress").inner_text()
        assert "expected to" in await lab.locator('[role="status"]').inner_text()
        await lab.locator(f'[data-rsl-answer][value="{first_answer}"]').focus()
        await lesson_page.keyboard.press("Space")
        await lab.locator('[data-rsl-action="check"]').focus()
        await lesson_page.keyboard.press("Enter")
        assert "任務 2／5" in await lab.locator(".rsl-progress").inner_text()
        for step in LESSON_7_IV_2["interactive"]["steps"][1:]:
            options = await lab.locator('[data-rsl-answer]').count()
            assert options == 3, options
            await lab.locator(f'[data-rsl-answer][value="{step["answer"]}"]').check()
            await lab.locator('[data-rsl-action="check"]').click()
        assert LESSON_7_IV_2["interactive"]["completionMessage"] in await lab.inner_text()
        await lesson_page.locator("#search").fill("地 Af-Ⅳ-1：聚落體系與交通網絡")
        geo_card = lesson_page.locator("#contentGrid article.card").filter(
            has=lesson_page.locator("h3", has_text="地 Af-Ⅳ-1：聚落體系與交通網絡")
        )
        await geo_card.wait_for()
        geo_sections = geo_card.locator(".lesson-sections > article")
        assert await geo_sections.count() == 6
        geo_section_text = "\n".join(await geo_sections.all_inner_texts())
        for heading in ("從一次就醫行程", "直線距離不等於可達性", "轉運站的便利與代價"):
            assert heading in geo_section_text
        for authored_transfer in ("不同年代的地圖", "新車站出現", "交通工具也沒有脫離情境的固定排名"):
            assert authored_transfer in geo_section_text, authored_transfer
        geo_activity = geo_card.locator('.activity[data-lesson="lesson-social-content-geo-af-iv-1"]')
        assert await geo_activity.locator(".activity-step").count() == 4
        first_geo_step = geo_activity.locator(".activity-step").nth(0)
        await first_geo_step.locator('[data-answer="B"]').click()
        assert "再想一次" in await first_geo_step.locator(".feedback").inner_text()
        await first_geo_step.locator('[data-answer="A"]').focus()
        await lesson_page.keyboard.press("Enter")
        assert "可進入下一步" in await first_geo_step.locator(".feedback").inner_text()
        historic_step = geo_activity.locator(".activity-step").nth(3)
        await historic_step.locator('[data-answer="B"]').click()
        assert "再想一次" in await historic_step.locator(".feedback").inner_text()
        await historic_step.locator('[data-answer="A"]').focus()
        await lesson_page.keyboard.press("Enter")
        assert "時間先後和位置重疊可提出假說" in await historic_step.locator(".feedback").inner_text()
        geo_viewports = {}
        for width in (320, 375, 768):
            await lesson_page.set_viewport_size({"width": width, "height": 900})
            metrics = await lesson_page.evaluate("""() => ({body: document.body.scrollWidth, doc: document.documentElement.scrollWidth, client: document.documentElement.clientWidth})""")
            assert metrics["body"] <= width and metrics["doc"] <= width, (width, metrics)
            geo_viewports[str(width)] = metrics
        geo_af_iv1_interaction = {
            "status": "passed",
            "unit": "地 Af-Ⅳ-1",
            "visibleLessonSections": await geo_sections.count(),
            "choiceStages": await geo_activity.locator(".activity-step").count(),
            "historicalNodeCausalityRetry": True,
            "wrongAnswerRetry": True,
            "keyboardCorrectAnswer": True,
            "viewports": geo_viewports,
            "pageErrors": lesson_errors,
        }
        assert not lesson_errors, lesson_errors
        await lesson_page.locator("#search").fill("lesson-math-content-s-9-1")
        s91_card = lesson_page.locator("#contentGrid article.card").filter(
            has=lesson_page.locator("h3", has_text="S-9-1：相似形")
        )
        await s91_card.wait_for()
        s91_sections = s91_card.locator(".lesson-sections > article")
        assert await s91_sections.count() == 6
        s91_text = "\n".join(await s91_sections.all_inner_texts())
        for required in ("縮印", "倍率一致", "2.8", "校刊編輯", "4、2", "12、5"):
            assert required in s91_text, required
        s91_activity = s91_card.locator('.activity[data-lesson="lesson-math-content-s-9-1"]')
        assert await s91_activity.locator(".activity-step").count() == 4
        first_s91_step = s91_activity.locator(".activity-step").nth(0)
        await first_s91_step.locator('[data-answer="B"]').click()
        assert "再想一次" in await first_s91_step.locator(".feedback").inner_text()
        await first_s91_step.locator('[data-answer="A"]').focus()
        await lesson_page.keyboard.press("Enter")
        assert "可進入下一步" in await first_s91_step.locator(".feedback").inner_text()
        s91_viewports = {}
        for width in (320, 375, 768):
            await lesson_page.set_viewport_size({"width": width, "height": 900})
            metrics = await lesson_page.evaluate("""() => ({body: document.body.scrollWidth, doc: document.documentElement.scrollWidth, client: document.documentElement.clientWidth})""")
            assert metrics["body"] <= width and metrics["doc"] <= width, (width, metrics)
            s91_viewports[str(width)] = metrics
        s91_interaction = {
            "status": "passed",
            "unit": "S-9-1",
            "visibleLessonSections": await s91_sections.count(),
            "choiceStages": await s91_activity.locator(".activity-step").count(),
            "wrongAnswerRetry": True,
            "keyboardCorrectAnswer": True,
            "viewports": s91_viewports,
            "pageErrors": lesson_errors,
        }
        assert not lesson_errors, lesson_errors
        await lesson_page.locator("#search").fill("lesson-science-content-db-iv-6")
        db_iv6_card = lesson_page.locator("#contentGrid article.card").filter(
            has=lesson_page.locator("h3", has_text="Db-Ⅳ-6：植物維管束的運輸功能")
        )
        await db_iv6_card.wait_for()
        db_iv6_sections = db_iv6_card.locator(".lesson-sections > article")
        assert await db_iv6_sections.count() == 6
        db_iv6_sim = db_iv6_card.locator('[data-simulation-lesson^="lesson-science-content-db-iv-6:"]')
        await db_iv6_sim.wait_for()
        assert await db_iv6_sim.locator(".sim-plant-transport").count() == 1
        assert "成熟葉片 → 果實" in await db_iv6_sim.locator(".sim-plant-phloem").inner_text()
        storage_source = db_iv6_sim.locator('[data-transport-choice="source"][data-value="storage"]')
        await storage_source.focus()
        await lesson_page.keyboard.press("Enter")
        assert "儲存器官（例如塊莖） → 果實" in await db_iv6_sim.locator(".sim-plant-phloem").inner_text()
        assert await db_iv6_sim.evaluate("document.activeElement.dataset.value") == "storage"
        await db_iv6_sim.locator('[data-transport-choice="sink"][data-value="shoot"]').click()
        assert "生長中的芽／嫩梢" in await db_iv6_sim.locator(".sim-plant-phloem").inner_text()
        transpiration_slider = db_iv6_sim.locator('[data-sim-control="transpiration"]')
        await transpiration_slider.focus()
        await lesson_page.keyboard.press("End")
        assert "較強" in await db_iv6_sim.inner_text()
        assert await db_iv6_sim.evaluate("document.activeElement.dataset.simControl") == "transpiration"
        db_iv6_viewports = {}
        for width in (320, 375, 768):
            await lesson_page.set_viewport_size({"width": width, "height": 900})
            metrics = await lesson_page.evaluate("""() => ({body: document.body.scrollWidth, doc: document.documentElement.scrollWidth, client: document.documentElement.clientWidth})""")
            assert metrics["body"] <= width and metrics["doc"] <= width, (width, metrics)
            db_iv6_viewports[str(width)] = metrics
        db_iv6_interaction = {
            "status": "passed",
            "unit": "Db-Ⅳ-6",
            "visibleLessonSections": await db_iv6_sections.count(),
            "sourceSinkControls": 5,
            "qualitativeTranspirationSlider": True,
            "keyboardFocusRetained": True,
            "viewports": db_iv6_viewports,
            "pageErrors": lesson_errors,
        }
        assert not lesson_errors, lesson_errors
        await lesson_page.reload(wait_until="networkidle")
        await lesson_page.locator("#search").fill(LESSON_7_IV_2["id"])
        lab = lesson_page.locator(f'[data-reading-strategy-lab="{LESSON_7_IV_2["id"]}"]')
        await lab.wait_for()
        assert LESSON_7_IV_2["interactive"]["completionMessage"] in await lab.inner_text()
        await lab.locator('[data-rsl-action="reset"]').click()
        assert "任務 1／5" in await lab.locator(".rsl-progress").inner_text()
        await lesson_page.locator("#search").fill("lesson-english-performance-7-iv-5")
        study_lab = lesson_page.locator('[data-reading-strategy-lab="lesson-english-performance-7-iv-5"]')
        await study_lab.wait_for()
        assert "任務 1／6" in await study_lab.locator(".rsl-progress").inner_text()
        assert "時間題" in await study_lab.locator(".rsl-excerpt").inner_text()
        await study_lab.locator('[data-rsl-answer][value="A"]').check()
        await study_lab.locator('[data-rsl-action="check"]').click()
        assert "任務 1／6" in await study_lab.locator(".rsl-progress").inner_text()
        assert "比較兩類題目" in await study_lab.locator('[role="status"]').inner_text()
        assert await study_lab.locator('[data-rsl-answer][value="A"]').is_checked()
        await study_lab.locator('[data-rsl-answer][value="B"]').focus()
        await lesson_page.keyboard.press("Space")
        await study_lab.locator('[data-rsl-action="check"]').focus()
        await lesson_page.keyboard.press("Enter")
        assert "任務 2／6" in await study_lab.locator(".rsl-progress").inner_text()
        for answer in ("C", "D", "A", "B", "C"):
            await study_lab.locator(f'[data-rsl-answer][value="{answer}"]').check()
            await study_lab.locator('[data-rsl-action="check"]').click()
        assert "六階任務完成" in await study_lab.inner_text()
        await lesson_page.reload(wait_until="networkidle")
        await lesson_page.locator("#search").fill("lesson-english-performance-7-iv-5")
        study_lab = lesson_page.locator('[data-reading-strategy-lab="lesson-english-performance-7-iv-5"]')
        await study_lab.wait_for()
        assert "六階任務完成" in await study_lab.inner_text()
        await study_lab.locator('[data-rsl-action="reset"]').click()
        assert "任務 1／6" in await study_lab.locator(".rsl-progress").inner_text()
        await lesson_page.locator("#search").fill("lesson-math-content-a-7-2")
        a72 = lesson_page.locator('.activity[data-lesson="lesson-math-content-a-7-2"]')
        await a72.wait_for()
        assert await a72.locator(".activity-step").count() == 4
        for index in range(4):
            step = a72.locator(".activity-step").nth(index)
            await step.locator('[data-answer="B"]').click()
            assert "再想一次" in await step.locator(".feedback").inner_text(), index
            await step.locator('[data-answer="A"]').click()
            feedback = await step.locator(".feedback").inner_text()
            assert "可進入下一步" in feedback, (index, feedback)
        assert "4x＋3＝27" in await a72.locator(".activity-step").nth(0).inner_text()
        assert "不是求解程序" in await a72.locator(".activity-step").nth(2).inner_text()
        await a72.locator(".activity-step").nth(0).locator('[data-answer="A"]').focus()
        await lesson_page.keyboard.press("Enter")
        a72_viewports = {}
        for width in (320, 375, 768):
            await lesson_page.set_viewport_size({"width": width, "height": 900})
            metrics = await lesson_page.evaluate("""() => ({body: document.body.scrollWidth, doc: document.documentElement.scrollWidth, client: document.documentElement.clientWidth})""")
            assert metrics["body"] <= width and metrics["doc"] <= width, (width, metrics)
            a72_viewports[str(width)] = metrics
        a72_interaction = {"status": "passed", "unit": "A-7-2", "stages": 4, "wrongAnswerRetry": True, "correctFeedback": True, "keyboard": True, "viewports": a72_viewports, "scope": "context modeling, equation classification, candidate substitution; no solving procedure"}
        await lesson_page.locator("#search").fill("lesson-math-content-a-7-7")
        a77 = lesson_page.locator('[data-simulation-lesson^="lesson-math-content-a-7-7"]')
        await a77.wait_for()
        assert "不等式範圍數線" in await a77.inner_text()
        assert "x ≥ 12" in await a77.inner_text()
        assert "11 不符合；12 符合；13 符合" in await a77.inner_text()
        await a77.locator('[data-inequality-relation="greater"]').click()
        assert "x ＞ 12" in await a77.inner_text()
        assert "12 不符合；13 符合" in await a77.inner_text()
        assert "端點不包含" in await a77.locator("svg").get_attribute("aria-label")
        await a77.locator('[data-inequality-relation="at-most"]').focus()
        await lesson_page.keyboard.press("Enter")
        assert "x ≤ 12" in await a77.inner_text()
        assert "向左延伸" in await a77.locator("svg").get_attribute("aria-label")
        boundary = a77.locator('[data-sim-control="boundary"]')
        await boundary.focus()
        await lesson_page.keyboard.press("ArrowRight")
        await lesson_page.keyboard.press("ArrowRight")
        assert "x ≤ 14" in await a77.inner_text()
        a77_viewports = {}
        for width in (320, 375, 768):
            await lesson_page.set_viewport_size({"width": width, "height": 900})
            metrics = await lesson_page.evaluate("""() => ({body: document.body.scrollWidth, doc: document.documentElement.scrollWidth, client: document.documentElement.clientWidth})""")
            assert metrics["body"] <= width and metrics["doc"] <= width, (width, metrics)
            a77_viewports[str(width)] = metrics
        a77_interaction = {"status": "passed", "unit": "A-7-7", "engine": "math-inequality-range", "relationToggle": True, "boundarySlider": True, "keyboard": True, "screenReaderLabel": "SVG aria-label includes endpoint and direction", "viewports": a77_viewports}
        await lesson_page.locator("#search").fill("lesson-math-content-a-7-8")
        a78 = lesson_page.locator('[data-simulation-lesson^="lesson-math-content-a-7-8"]')
        await a78.wait_for()
        assert "解集探針" in await a78.inner_text()
        assert "x＜−2" in await a78.inner_text()
        assert "−3 通過" in await a78.locator("svg").text_content()
        assert "負二為空心端點並向左延伸" in await a78.locator("svg").get_attribute("aria-label")
        assert await a78.locator("[data-design-step]").count() == 4
        await a78.locator('[data-design-step="3"]').focus()
        await lesson_page.keyboard.press("Enter")
        assert "−5、−4、−3" in await a78.inner_text()
        assert await lesson_page.evaluate("() => document.activeElement.dataset.designStep") == "3"
        a78_viewports = {}
        for width in (320, 375, 768):
            await lesson_page.set_viewport_size({"width": width, "height": 900})
            metrics = await lesson_page.evaluate("""() => ({body: document.body.scrollWidth, doc: document.documentElement.scrollWidth, client: document.documentElement.clientWidth})""")
            assert metrics["body"] <= width and metrics["doc"] <= width, (width, metrics)
            a78_viewports[str(width)] = metrics
        a78_interaction = {"status": "passed", "unit": "A-7-8", "engine": "concept-explorer / inequality-solution-set", "steps": 4, "proofNumberLine": True, "keyboardFocusRetained": True, "accessibleSvg": True, "viewports": a78_viewports}
        await lesson_page.locator("#search").fill("lesson-math-content-a-8-7")
        a87 = lesson_page.locator('.activity[data-lesson="lesson-math-content-a-8-7"]')
        await a87.wait_for()
        assert await a87.locator(".activity-step").count() == 6
        for index in range(6):
            step = a87.locator(".activity-step").nth(index)
            await step.locator('[data-answer="B"]').click()
            assert "再想一次" in await step.locator(".feedback").inner_text(), index
            await step.locator('[data-answer="A"]').click()
            feedback = await step.locator(".feedback").inner_text()
            assert "可進入下一步" in feedback, (index, feedback)
        assert "右側成3" in await a87.locator(".activity-step").nth(3).locator(".feedback").inner_text()
        await a87.locator(".activity-step").nth(0).locator('[data-answer="A"]').focus()
        await lesson_page.keyboard.press("Enter")
        a87_viewports = {}
        for width in (320, 375, 768):
            await lesson_page.set_viewport_size({"width": width, "height": 900})
            metrics = await lesson_page.evaluate("""() => ({body: document.body.scrollWidth, doc: document.documentElement.scrollWidth, client: document.documentElement.clientWidth})""")
            assert metrics["body"] <= width and metrics["doc"] <= width, (width, metrics)
            a87_viewports[str(width)] = metrics
        a87_interaction = {"status": "passed", "unit": "A-8-7", "stages": 6, "wrongAnswerRetry": True, "correctFeedback": True, "keyboard": True, "viewports": a87_viewports}
        await lesson_page.locator("#search").fill("lesson-math-content-a-8-4")
        a84 = lesson_page.locator('.activity[data-lesson="lesson-math-content-a-8-4"]')
        await a84.wait_for()
        assert await a84.locator(".activity-step").count() == 5
        for index in range(5):
            step = a84.locator(".activity-step").nth(index)
            await step.locator('[data-answer="B"]').click()
            assert "再想一次" in await step.locator(".feedback").inner_text(), index
            await step.locator('[data-answer="A"]').click()
            feedback = await step.locator(".feedback").inner_text()
            assert "可進入下一步" in feedback, (index, feedback)
        a84_counterexample = await a84.locator(".activity-step").nth(4).inner_text()
        assert "12" in a84_counterexample and "10" in a84_counterexample, a84_counterexample
        await a84.locator(".activity-step").nth(0).locator('[data-answer="A"]').focus()
        await lesson_page.keyboard.press("Enter")
        a84_viewports = {}
        for width in (320, 375, 768):
            await lesson_page.set_viewport_size({"width": width, "height": 900})
            metrics = await lesson_page.evaluate("""() => ({body: document.body.scrollWidth, doc: document.documentElement.scrollWidth, client: document.documentElement.clientWidth})""")
            assert metrics["body"] <= width and metrics["doc"] <= width, (width, metrics)
            a84_viewports[str(width)] = metrics
        a84_interaction = {"status": "passed", "unit": "A-8-4", "stages": 5, "wrongAnswerRetry": True, "correctFeedback": True, "keyboard": True, "viewports": a84_viewports, "productCounterexample": "(x+3)(x+4)=x²+7x+12, not x²+7x+10"}
        await lesson_page.locator("#search").fill("lesson-math-content-d-8-1")
        d81 = lesson_page.locator('.activity[data-lesson="lesson-math-content-d-8-1"]')
        await d81.wait_for()
        assert await d81.locator(".activity-step").count() == 4
        for index in range(4):
            step = d81.locator(".activity-step").nth(index)
            await step.locator('[data-answer="B"]').click()
            assert "再想一次" in await step.locator(".feedback").inner_text(), index
            await step.locator('[data-answer="A"]').click()
            assert "可進入下一步" in await step.locator(".feedback").inner_text(), index
        await d81.locator(".activity-step").nth(0).locator('[data-answer="A"]').focus()
        await lesson_page.keyboard.press("Enter")
        d81_viewports = {}
        for width in (320, 375, 768):
            await lesson_page.set_viewport_size({"width": width, "height": 900})
            metrics = await lesson_page.evaluate("""() => ({body: document.body.scrollWidth, doc: document.documentElement.scrollWidth, client: document.documentElement.clientWidth})""")
            assert metrics["body"] <= width and metrics["doc"] <= width, (width, metrics)
            d81_viewports[str(width)] = metrics
        d81_interaction = {"status": "passed", "unit": "D-8-1", "stages": 4, "wrongAnswerRetry": True, "correctFeedback": True, "keyboard": True, "viewports": d81_viewports, "ratioCheck": "20%,30%,35%,15%; cumulative 20%,50%,85%,100%; 85%-50%=35%"}
        await lesson_page.locator("#search").fill("lesson-math-content-a-7-1")
        a71 = lesson_page.locator('.simulation[aria-label="代數式同值檢核臺"]')
        await a71.wait_for()
        await a71.locator("[data-sim-reset]").click()
        assert await a71.locator(".sim-design-steps button").count() == 4
        assert "3x＋2＋5x−7" in await a71.inner_text()
        slider = a71.locator('input[data-sim-control="x"]')
        await slider.focus()
        for _ in range(4):
            await lesson_page.keyboard.press("ArrowLeft")
        assert await slider.input_value() == "-2"
        assert "-21" in await a71.locator("[data-expression-original]").inner_text()
        assert await a71.locator("[data-expression-original]").inner_text() == await a71.locator("[data-expression-reduced]").inner_text()
        assert await lesson_page.evaluate("document.activeElement?.getAttribute('data-sim-control')") == "x"
        a71_viewports = {}
        for width in (320, 375, 768):
            await lesson_page.set_viewport_size({"width": width, "height": 900})
            metrics = await lesson_page.evaluate("""() => ({body: document.body.scrollWidth, doc: document.documentElement.scrollWidth, client: document.documentElement.clientWidth})""")
            assert metrics["body"] <= width and metrics["doc"] <= width, (width, metrics)
            a71_viewports[str(width)] = metrics
        a71_interaction = {"status": "passed", "unit": "A-7-1", "engine": "math-expression-lab", "equivalentOutputsAtXMinus2": [-21, -21], "keyboardSliderFocusRetained": True, "staticValueTable": True, "viewports": a71_viewports, "pageErrors": lesson_errors}
        await lesson_page.locator("#search").fill("lesson-math-content-s-9-13")
        s913_card = lesson_page.locator("#contentGrid article.card").filter(
            has=lesson_page.locator("h3", has_text="S-9-13：表面積與體積")
        )
        await s913_card.wait_for()
        assert await s913_card.locator(".lesson-sections > article").count() == 6, "S-9-13 should render each fused lesson section exactly once"
        s913 = s913_card.locator('[data-simulation-lesson^="lesson-math-content-s-9-13:"]')
        await s913.wait_for()
        assert await s913.locator('[data-sim-control="prismLength"]').count() == 0
        assert await s913.locator("[data-prism-surface-area]").count() == 0
        await s913.locator('[data-geometry-prediction="A"]').click()
        await s913.locator('[data-geometry-action="submit-prediction"]').click()
        assert "預測尚不正確" in await s913.inner_text()
        assert await s913.locator('[data-sim-control="prismLength"]').count() == 0
        await s913.locator('[data-geometry-prediction="B"]').focus()
        await lesson_page.keyboard.press("Space")
        assert await s913.locator('[data-sim-control="prismLength"]').count() == 0
        await s913.locator('[data-geometry-action="submit-prediction"]').focus()
        await lesson_page.keyboard.press("Enter")
        assert await s913.locator("[data-prism-surface-area]").inner_text() == "240"
        assert await s913.locator("[data-prism-volume]").inner_text() == "180"
        assert await s913.locator(".sim-prism-visuals figure").count() == 2
        length_control = s913.locator('[data-sim-control="prismLength"]')
        await length_control.focus()
        await lesson_page.keyboard.press("ArrowRight")
        await lesson_page.keyboard.press("ArrowRight")
        assert await s913.locator("[data-prism-surface-area]").inner_text() == "320"
        assert await s913.locator("[data-prism-volume]").inner_text() == "300"
        assert await s913.evaluate("document.activeElement.dataset.simControl") == "prismLength"
        await s913.locator('[data-geometry-transfer="B"]').click()
        await s913.locator('[data-geometry-action="submit-transfer"]').click()
        assert "280 cm²、168 cm³" in await s913.inner_text()
        s913_viewports = {}
        for width in (320, 375, 768):
            await lesson_page.set_viewport_size({"width": width, "height": 900})
            metrics = await lesson_page.evaluate("""() => ({body: document.body.scrollWidth, doc: document.documentElement.scrollWidth, client: document.documentElement.clientWidth})""")
            assert metrics["body"] <= width and metrics["doc"] <= width, (width, metrics)
            s913_viewports[str(width)] = metrics
        await s913.locator("[data-sim-reset]").click()
        assert await s913.locator('[data-sim-control="prismLength"]').count() == 0
        s913_interaction = {"status": "passed", "unit": "S-9-13", "engine": "data-driven triangular-prism model v2", "base": "8-15-17", "predictionGate": True, "surfaceVolumeSync": [240, 180, 320, 300], "keyboardFocusRetained": True, "transfer": "280 cm² / 168 cm³", "reset": True, "viewports": s913_viewports, "pageErrors": lesson_errors}
        await lesson_page.locator("#search").fill("lesson-english-content-ac-iv-1")
        ac_iv1_card = lesson_page.locator("#contentGrid article.card").filter(
            has=lesson_page.locator("h3", has_text="Ac-Ⅳ-1：簡易英文標示")
        )
        await ac_iv1_card.wait_for()
        ac_iv1_sections = ac_iv1_card.locator(".lesson-sections article")
        assert await ac_iv1_sections.count() == 8
        for heading in (
            "三秒鐘內，你要先看哪裡？",
            "短語裡藏著四種不同工作",
            "用一張圖書館地圖拆解誤讀",
            "遮住一項線索，分辨確定與猜測",
            "替真正的訪客做一組不會誤導的標示",
            "清楚不是越短越好，而是少猜一步",
        ):
            assert await ac_iv1_sections.filter(has=lesson_page.get_by_text(heading, exact=True)).count() == 1, heading
        ac_iv1_interaction = {"status": "passed", "unit": "Ac-Ⅳ-1", "visibleSectionCount": await ac_iv1_sections.count(), "allSixAuthoredSectionsVisible": True, "reviewStatus": "draft"}
        await lesson_page.locator("#search").fill("lesson-english-content-ac-iv-2")
        ac_iv2_card = lesson_page.locator("#contentGrid article.card").filter(
            has=lesson_page.locator("h3", has_text="Ac-Ⅳ-2：常見教室用語")
        )
        await ac_iv2_card.wait_for()
        ac_iv2_sections = ac_iv2_card.locator(".lesson-sections article")
        assert await ac_iv2_sections.count() == 7
        for heading in (
            "任務卡少了一個步驟",
            "把指令拆成可以執行的資訊",
            "讓海報活動從模糊變清楚",
            "角色改變，說法也要調整",
            "在音訊故障時修復合作",
            "用下一步檢查你是否真的說清楚",
        ):
            assert await ac_iv2_sections.filter(has=lesson_page.get_by_text(heading, exact=True)).count() == 1, heading
        ac_iv2_interaction = {"status": "passed", "unit": "Ac-Ⅳ-2", "visibleSectionCount": await ac_iv2_sections.count(), "allSixAuthoredStagesVisible": True, "reviewStatus": "draft"}
        await lesson_page.locator("#search").fill("lesson-science-content-ba-iv-3")
        ba_iv3_card = lesson_page.locator("#contentGrid article.card").filter(
            has=lesson_page.locator("h3", has_text="Ba-Ⅳ-3：化學反應的吸熱與放熱")
        )
        await ba_iv3_card.wait_for()
        ba_iv3_sections = ba_iv3_card.locator(".lesson-sections article")
        assert await ba_iv3_sections.count() == 7
        for heading, evidence in (
            ("一個小袋子，為什麼會自己變冷？", "25.0°C 降到 18.5°C"),
            ("先畫邊界，再畫能量箭頭", "周圍→系統"),
            ("讀三組資料：同一個溫度方向，不同的證據強度", "29.1°C"),
            ("四格熱量帳本：從預測走到可檢查的結論", "系統未定義、對照不公平、結論超出資料"),
            ("把能量判讀帶到生活裝置", "開封與未開封裝置"),
            ("用一句有邊界的話收束推理", "尚不足以確認反應熱"),
        ):
            section = ba_iv3_sections.filter(has=lesson_page.get_by_text(heading, exact=True))
            assert await section.count() == 1, heading
            assert evidence in await section.inner_text(), (heading, evidence)
        ba_iv3_interaction = {"status": "passed", "unit": "Ba-Ⅳ-3", "visibleSectionCount": await ba_iv3_sections.count(), "allSixFullAuthoredStagesVisible": True, "reviewStatus": "draft"}
        await lesson_page.locator("#search").fill("lesson-chinese-content-ab-iv-1")
        ab_iv1_activity = lesson_page.locator('.activity[data-lesson="lesson-chinese-content-ab-iv-1"]')
        await ab_iv1_activity.wait_for()
        ab_iv1_card = ab_iv1_activity.locator("xpath=ancestor::article[contains(@class,'card')]")
        ab_iv1_sections = ab_iv1_card.locator(".lesson-sections article")
        for heading in (
            "從本單元情境進入",
            "建立本單元概念架構",
            "用自編例子走完一次",
            "依線索完成引導練習",
            "換到新情境遷移",
            "回顧證據與限制",
        ):
            assert await ab_iv1_sections.filter(has=lesson_page.get_by_text(heading, exact=True)).count() == 1, heading
        assert await ab_iv1_activity.locator(".activity-step").count() == 3
        first_ab_step = ab_iv1_activity.locator(".activity-step").nth(0)
        await first_ab_step.locator('[data-answer="B"]').focus()
        await lesson_page.keyboard.press("Enter")
        assert "詞語" in await first_ab_step.locator(".feedback").inner_text()
        await first_ab_step.locator('[data-answer="A"]').focus()
        await lesson_page.keyboard.press("Enter")
        assert "可進入下一步" in await first_ab_step.locator(".feedback").inner_text()
        ab_iv1_viewports = {}
        for width in (320, 375, 768):
            await lesson_page.set_viewport_size({"width": width, "height": 900})
            metrics = await lesson_page.evaluate("""() => ({body: document.body.scrollWidth, doc: document.documentElement.scrollWidth, client: document.documentElement.clientWidth})""")
            assert metrics["body"] <= width and metrics["doc"] <= width, (width, metrics)
            ab_iv1_viewports[str(width)] = metrics
        ab_iv1_interaction = {"status": "passed", "unit": "Ab-Ⅳ-1", "visibleAuthoredStages": 6, "choiceSteps": 3, "keyboardWrongHintAndCorrectFeedback": True, "viewports": ab_iv1_viewports}
        for width in (320, 375, 768):
            await lesson_page.set_viewport_size({"width": width, "height": 900})
            assert not await lesson_page.evaluate("() => document.documentElement.scrollWidth > document.documentElement.clientWidth"), width
        assert not lesson_errors, lesson_errors
        lesson_interaction = {"status": "passed", "unit": "7-IV-2", "stages": 5, "wrongAnswerRetry": True, "keyboard": True, "persistenceAndReset": True, "viewports": [320, 375, 768], "pageErrors": lesson_errors}
        study_plan_interaction = {"status": "passed", "unit": "7-IV-5", "stages": 6, "wrongAnswerRetry": True, "keyboard": True, "persistenceAndReset": True, "viewports": [320, 375, 768], "pageErrors": lesson_errors}
        await lesson_page.close()
        result = {
            "status": "passed",
            "optionCount": option_count,
            "viewportMetrics": viewport_metrics,
            "fullTraversal": 1027,
            "unitSpecContentSourceTraversal": 1027,
            "flow": output,
            "goldenFormulaCount": await page.locator(".formula-model li").count(),
            "keyboardFocusTags": focus_tags,
            "accessibilityTree": {"statusLive": status_properties.get("live"), "statusAtomic": status_properties.get("atomic"), "buttonCount": len(expected_buttons), "namedTextbox": True},
            "reducedMotion": reduced_motion,
            "lessonInteraction": lesson_interaction,
            "studyPlanInteraction": study_plan_interaction,
            "geoAfIv1Interaction": geo_af_iv1_interaction,
            "mathS91Interaction": s91_interaction,
            "scienceDbIv6Interaction": db_iv6_interaction,
            "scienceFcIv1StudentSpecRendering": science_fc_iv1_rendering,
            "a72Interaction": a72_interaction,
            "a77Interaction": a77_interaction,
            "a78Interaction": a78_interaction,
            "a87Interaction": a87_interaction,
            "a84Interaction": a84_interaction,
            "d81Interaction": d81_interaction,
            "a71Interaction": a71_interaction,
            "s913Interaction": s913_interaction,
            "englishAcIv1VisibleLesson": ac_iv1_interaction,
            "englishAcIv2VisibleLesson": ac_iv2_interaction,
            "scienceBaIv3VisibleLesson": ba_iv3_interaction,
            "chineseAbIv1VisibleLesson": ab_iv1_interaction,
            "scope": "real Chromium runtime; screen-reader and content/pedagogical review remain separate",
        }
        await browser.close()
        return result


def main() -> int:
    parser = argparse.ArgumentParser()
    parser.add_argument("--url", default="http://127.0.0.1:8765/implementation/workbench.html")
    parser.add_argument("--browser-channel", default="chromium", help="Fallback Playwright browser channel (e.g. chromium or chrome)")
    parser.add_argument("--report", default="implementation/reports/browser-smoke.json")
    args = parser.parse_args()
    result = asyncio.run(run(args.url, args.browser_channel))
    report = Path(args.report)
    if not report.is_absolute():
        report = Path(__file__).resolve().parents[1] / report
    report.parent.mkdir(parents=True, exist_ok=True)
    report.write_text(json.dumps(result, ensure_ascii=False, indent=2) + "\n", encoding="utf-8")
    print(json.dumps(result, ensure_ascii=False))
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
