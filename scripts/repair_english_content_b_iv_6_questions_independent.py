#!/usr/bin/env python3
"""Independently rewrite English B-IV-6 picture-description questions."""
import json
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
OUT = ROOT / "questions/english"
LESSON = "lesson-english-content-b-iv-6"
SOURCES = [
    ("https://www.yacjh.kh.edu.tw/upload/221/101_30637/114%E4%B8%8B%E5%AD%B8%E6%9C%9F%E7%AC%AC%E4%B8%80%E6%AC%A1%E6%AE%B5%E8%80%83%E4%B8%89%E5%B9%B4%E7%B4%9A%E8%8B%B1%E6%96%87.pdf", "高雄市立鹽埕國民中學公開英文段考", "圖片描述、位置與實用英語"),
    ("https://www.bhjh.ntpc.edu.tw/p/406-1000-10627%2Cr111.php?Lang=zh-tw", "新北市立北投國民中學公開定期評量試題頁", "視覺場景、介系詞、動作與情境推論"),
    ("https://www.hcjh.ntpc.edu.tw/p/406-1000-7527%2Cr146.php", "新北市立新埔國民中學公開段考試題頁", "圖像描述、細節與應用"),
]

def refs():
    return [{"url": u, "title": f"{t}；僅研究公開題型與能力方向，未複製原題。", "year": "113-114", "subject": "english", "locator": l, "observedPattern": "公立學校英語評量要求從圖像或場景辨認位置、數量、顏色、動作、比較、缺漏、順序與整體推論；本題改為全新文字場景，未複製圖片。", "reuseDecision": "pattern-only", "status": "recorded", "locatorLevel": "paper"} for u, t, l in SOURCES]

DATA = [
    ("A park map shows **a kite above the picnic table and a basket under the bench**. Where is the kite?", ["Above the picnic table", "Under the bench", "Inside the basket", "Behind the park gate"], "A", "The scene places the kite above the picnic table; under the bench describes the basket.", "先建立物件—位置配對，再只追蹤題目所問的 kite。", ["List the kite, table, basket, and bench.", "Match the kite with its stated position.", "Separate above from under.", "Choose above the picnic table.", "Check that the answer does not borrow the basket's position."]),
    ("The school garden has **five sunflowers, two benches, and one fountain**. How many benches are shown?", ["Two", "Five", "One", "Seven"], "A", "The count for benches is two; five belongs to sunflowers and one belongs to the fountain.", "數量題要先鎖定名詞，再避免把不同物件的數字相加或交換。", ["Identify the noun benches.", "Scan the description for the number attached to benches.", "Ignore the counts for sunflowers and fountain.", "Select two.", "Verify that no addition is required because the question asks for one object type."]),
    ("In the scene, **a purple umbrella stands beside a yellow chair**. What color is the chair?", ["Yellow", "Purple", "Green", "White"], "A", "Yellow modifies chair, while purple modifies umbrella.", "把顏色和它修飾的名詞綁在一起，不因相鄰物件而誤配。", ["Find the object asked about: chair.", "Read the adjective attached to chair.", "Separate yellow chair from purple umbrella.", "Choose yellow.", "Reject colors not supported by the description."]),
    ("A picture shows **a child is opening a lunch box while her friend pours water**. What is the child doing?", ["Opening a lunch box", "Pouring water", "Closing a window", "Drawing a map"], "A", "The child is opening a lunch box; pouring water is the friend's action.", "先分辨人物，再把現在進行式動作與正確人物配對。", ["Identify the two people in the scene.", "Match child with opening a lunch box.", "Assign pouring water to the friend.", "Choose the child's action.", "Reject actions that belong to another person or are not mentioned."]),
    ("The picture shows **the red bus is longer than the blue van, but the van is quieter**. Which statement is true?", ["The red bus is longer than the blue van.", "The blue van is longer than the red bus.", "The bus is quieter than the van.", "Both vehicles have the same length."], "A", "The description compares length and says the red bus is longer; quietness is a separate comparison.", "比較題要先確認比較的屬性，不能用 quieter 的資訊改寫 longer。", ["Locate the two vehicles.", "Separate the length comparison from the sound comparison.", "Read which vehicle is longer.", "Choose the red-bus statement.", "Reject options that reverse the length or replace it with quietness."]),
    ("A notice board shows **a clock above the door and a calendar next to the window**. What is above the door?", ["A clock", "A calendar", "A window", "A backpack"], "A", "The clock is explicitly above the door; the calendar is next to the window.", "位置題必須核對參照物，above the door 不能改成 next to the window。", ["Find the reference object door.", "Locate the item connected by above.", "Distinguish clock from calendar.", "Choose a clock.", "Confirm the answer describes the vertical relation, not the neighboring window."]),
    ("At a beach, **a volunteer sorts glass bottles into a recycling box while a child reads a safety sign**. What idea does the scene show?", ["Recycling and safety awareness", "Cooking a family dinner", "Buying a train ticket", "Practicing a piano song"], "A", "Sorting bottles into a recycling box and reading a safety sign support recycling and safety awareness.", "整體推論要合併多個可見線索，但不能加入場景沒有的活動。", ["List the visible actions.", "Connect bottles and recycling box to recycling.", "Connect the child and safety sign to safety awareness.", "Choose the combined idea.", "Reject activities with no visual evidence."]),
    ("A classroom picture has **three pencils and a ruler on the desk, but no eraser**. Which item is missing?", ["An eraser", "A pencil", "A ruler", "A desk"], "A", "The description explicitly says there is no eraser; the other listed items are present.", "遇到 no 要辨認缺漏物件，不能把已出現的物件當成答案。", ["Inventory the desk items.", "Mark pencils and ruler as present.", "Find the phrase no eraser.", "Choose an eraser.", "Check that the answer is the only item explicitly absent."]),
    ("In three panels, **a boy has an empty cup, fills it at a water tap, and then drinks**. What happens in the middle panel?", ["He fills the cup at a water tap.", "He drinks before filling it.", "He loses the cup on a bus.", "He paints the tap red."], "A", "The middle panel is the filling action, between the empty cup and drinking.", "順序題要把每格動作排成時間線，再回答指定的中間事件。", ["Name the first, middle, and last panels.", "Locate the action between empty and drinking.", "Match the middle panel to fills at a water tap.", "Choose that action.", "Reject actions that change the sequence or add new details."]),
    ("A sunny playground scene shows **two students sharing a bench, a sleeping cat under it, and a red kite caught in a tree**. Which statement is supported?", ["Two students share a bench while a cat sleeps below it.", "Three cats fly the kite in a storm.", "The students are cooking inside a bus.", "The kite is under the bench and the cat is in the tree."], "A", "The first option preserves the people, bench, cat's position and action; the other options reverse or invent scene details.", "整合題逐一核對人物數量、位置與動作，最後檢查是否反轉物件關係。", ["Count the students and identify the bench.", "Locate the cat under the bench and note sleeping.", "Keep the kite detail separate from the cat detail.", "Choose the sentence preserving the supported facts.", "Reject reversed positions, changed weather, and invented activities."]),
]

assert len(DATA) == 10
TARGETS = ["A", "B", "C", "D", "B", "C", "D", "A", "B", "C"]
for i, (prompt, options, answer, explanation, strategy, steps) in enumerate(DATA, 1):
    target = TARGETS[i - 1]
    if target != answer:
        oi, ti = ord(answer) - 65, ord(target) - 65
        correct = options[oi]
        rest = [v for j, v in enumerate(options) if j != oi]
        options = rest[:ti] + [correct] + rest[ti:]
        answer = target
    item = {"id": f"question-english-content-b-iv-6-{i}", "subject": "english", "type": "single-choice", "prompt": prompt, "options": [{"id": chr(65+j), "text": t} for j, t in enumerate(options)], "knowledgeIds": ["kg-english-content-b-iv-6"], "difficulty": "medium", "answer": {"value": answer, "explanation": explanation}, "provenance": {"origin": "original", "license": "All rights reserved", "sourceUrl": SOURCES[0][0], "sourceLocator": "公立學校國中英語段考；只研究圖像描述、位置、數量、顏色、動作、比較、缺漏、順序與整體推論題型。", "authoringNote": "依官方英語文領域課綱、單元 KG 與三個公立學校公開來源，獨立改寫圖片描述題；未複製原文、選項、圖片或答案；待第二輪 AI／Terra 內容複核。"}, "reviewStatus": "draft", "updatedAt": "2026-09-13", "lessonId": LESSON, "examPatternRefs": refs(), "solutionStrategy": strategy, "solutionSteps": steps}
    (OUT / f"question-english-content-b-iv-6-{i}.json").write_text(json.dumps(item, ensure_ascii=False, indent=2) + "\n", encoding="utf-8")
print(f"rewrote {len(DATA)} independent questions for {LESSON}")
