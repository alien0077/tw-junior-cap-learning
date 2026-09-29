#!/usr/bin/env python3
"""Independently rewrite Chinese logical-listening questions for Ab-IV-3."""
import json
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
OUT = ROOT / "questions/chinese"
LESSON = "lesson-chinese-performance-1-iv-3"
KG = "kg-chinese-performance-1-iv-3"
SOURCES = [
    ("https://www.sdjh.ntpc.edu.tw/var/file/0/1000/attach/16/pta_2229_1166226_19803.pdf", "新北市立石碇國中公開國文試題", "口語論證、理由與證據"),
    ("https://www.yacjh.kh.edu.tw/upload/221/101_30637/114%E4%B8%8B%E5%AD%B8%E6%9C%9F%E7%AC%AC一%E6%AC%A1%E6%AE%B5%E8%80%83%E4%B8%89%E5%B9%B4%E7%B4%9A%E5%9C%8B%E6%96%87.pdf", "高雄市立鹽埕國中公開國文段考", "邏輯聆聽、條件與反例"),
    ("https://www.jlsh.mlc.edu.tw/var/file/12/1012/img/113-2-7-4.pdf", "國立卓蘭高中附設國中部公開課程與試題資料", "方案比較、限制與修正"),
]


def refs():
    return [{
        "url": url, "title": f"{title}；僅研究公開題型與能力方向，未複製原題。",
        "year": "113-114", "subject": "chinese", "locator": locator,
        "observedPattern": "公立學校國文評量以口頭提案的主張／理由、因果界線、條件分支、反例、方案比較、反方成本與試辦修正要求邏輯聆聽；本題採全新語料。",
        "reuseDecision": "pattern-only", "status": "recorded", "locatorLevel": "paper"
    } for url, title, locator in SOURCES]


DATA = [
    ("主張與理由", "同學說「應把午休延長十分鐘，因為最近很多人吃不完午餐」；這段話的主張是什麼？", ["午休應延長十分鐘", "最近很多人吃不完午餐", "午餐發生在午休", "同學正在說話"], "A", "希望聽者接受的行動方案是主張；吃不完午餐是支持它的現象與理由。", "先找帶有應該、需要或行動要求的句子，再把因為後面的內容標成理由。"),
    ("證據限制", "提案者說延長午休能改善用餐，並提出連續五天剩食量紀錄；哪項判斷最恰當？", ["五天資料已證明任何學校都會改善", "只要有理由就不需資料", "資料可支持方向，但仍需檢查其他原因與不同情境", "剩食量和用餐時間完全無關"], "C", "紀錄能提供支持方向的資料，但不能自動完成普遍或因果結論，仍要檢查其他變項。", "先承認資料支持的部分，再列出樣本期間、替代原因與外推範圍。"),
    ("因果跳躍", "有人說「換電子作業後遲交變少，所以電子作業一定讓學習變好」；最重要的追問是？", ["把一定改成非常一定即可", "遲交量與學習成效是不同指標，還要比較其他因素與更多資料", "兩件事同時改變就必然是因果", "電子作業不可能有任何效果"], "B", "遲交是行為指標，學習成效是另一項結果；從前者跳到後者需要更多測量與替代原因檢查。", "把原句中的兩個結果分開，確認是否真的測量了學習，並尋找同期改變的因素。"),
    ("條件分支", "校園積水提案說「雨量未超過警戒值先清落葉；超過則封鎖低窪區」；最重要的邏輯是？", ["不論雨量都只需清落葉", "封鎖低窪區和雨量無關", "提案沒有可執行步驟", "不同雨量條件對應不同處置，方案不是對所有情況用同一方法"], "D", "若／則分支把條件和行動連結，聆聽者要記住不同情況下的不同處置。", "把條件畫成兩條分支，再逐一配對行動，避免只記住其中一個動作。"),
    ("反例界線", "主張「只要設置提醒，就能讓所有人準時交作業」；哪個例子最能指出限制？", ["有人收到提醒並準時完成", "提醒訊息使用藍色字體", "有人收到提醒，仍因沒有網路或不理解要求而遲交", "老師在早上發出提醒"], "C", "反例保留收到提醒這項前提，卻顯示其他條件仍可能造成遲交，因此能削弱所有人的絕對結論。", "檢查反例是否符合主張前提，再看它是否讓結果不成立，而不是找完全無關的例子。"),
    ("方案比較", "兩方案都能減少垃圾：甲成本低但需人工分類，乙成本高但自動分類；比較時應聽哪些面向？", ["只聽哪個名稱比較新", "只看口號是否有環保兩字", "由提出方案者直接宣布勝負", "減量效果、成本、人力、執行條件與可能受影響者"], "D", "方案比較要把效果、資源、條件與分配後果放在共同尺度，不能只用新舊或口號決定。", "先列共同目標，再逐項比較效果、成本、人力、可行性與受影響者。"),
    ("問題定義", "同學說「圖書館太吵，應該改善」；找可行方法前第一個澄清問題是什麼？", ["直接購買最昂貴的隔音設備", "先責怪所有學生", "把圖書館永久關閉", "噪音發生在何時、哪裡、由哪些活動造成，以及誰受到影響"], "D", "問題若不具體，方案容易對錯對象下手；先補時間、位置、來源與受影響者才能比較方法。", "把模糊形容詞改成可觀察的時段、地點、來源與影響，再尋找對應方案。"),
    ("回應反方成本", "增加社團時間的提案遇到清潔人員可能加班的疑慮；哪個回應最有邏輯？", ["反方不喜歡社團，不必理會", "只重複社團很重要，不處理加班", "把反方意見從紀錄刪掉", "把加班時數與清潔需求列入成本，提出試辦和調整時段方案"], "D", "反方指出的是執行成本；有邏輯的回應承認限制、補入資料並提出可檢驗的修正。", "先準確重述疑慮，再估算成本，最後提出小規模試辦與評估指標。"),
    ("資料範圍", "資料只顯示一場試辦後參與人數增加；哪種重述最負責任？", ["這場試辦期間參與人數增加，但長期效果與原因仍需更多觀察", "方案一定讓所有人更喜歡活動", "參與人數增加就證明沒有成本", "一次試辦已證明所有情境都會成功"], "A", "負責任的重述保留觀察期間與已知指標，也標記長期效果、原因與成本尚未確定。", "在重述中保留時間、樣本與指標，並明確寫出資料沒有回答的問題。"),
    ("可執行流程", "要把校園交通安全口頭提案整理成可執行方法，哪套步驟最完整？", ["直接採用最受歡迎的口號", "只聽管理者意見，省略學生和家長", "先決定答案再挑支持資料", "先定義事故時段與地點，整理觀察和不同需求，比較方案成本／效果，試辦後依指標修正"], "D", "完整邏輯聆聽把問題、證據、利害關係人、方案、試辦和回饋串成可檢查的決策流程。", "依序做問題定義、資料整理、需求比較、方案試辦、指標檢核與修正。"),
]
TARGETS = ["A", "B", "C", "D", "B", "C", "D", "A", "B", "C"]

for i, (tag, prompt, options, answer, explanation, strategy) in enumerate(DATA, 1):
    target = TARGETS[i - 1]
    correct_index = ord(answer) - 65
    target_index = ord(target) - 65
    correct = options[correct_index]
    rest = [value for index, value in enumerate(options) if index != correct_index]
    options = rest[:target_index] + [correct] + rest[target_index:]
    steps = [
        f"讀題定位：圈出「{tag}」與主張、理由、條件、反例、方案、成本或資料範圍。",
        f"拆解邏輯：把聽到的句子改成主張—證據—限制鏈，再依「{explanation}」檢查跳躍。",
        f"核對正解：選項 {target} 能保留原說話者的條件與未知，且提出可執行或可檢查的判斷。",
        "排除誘答：檢查是否把一次資料推成普遍因果、忽略反方成本，或只用口號與人氣作決策。",
        "回讀驗證：確認問題定義、證據範圍、受影響者與修正步驟彼此相連。",
    ]
    item = {
        "id": f"question-chinese-performance-1-iv-3-{i}", "subject": "chinese", "type": "single-choice",
        "prompt": prompt, "options": [{"id": chr(65 + j), "text": text} for j, text in enumerate(options)],
        "knowledgeIds": [KG], "difficulty": "medium",
        "answer": {"value": target, "explanation": explanation},
        "provenance": {"origin": "original", "license": "All rights reserved", "sourceUrl": SOURCES[0][0],
                       "sourceLocator": "三所公立學校公開國文資料；只研究主張／理由、因果界線、條件、反例、方案比較與試辦修正。",
                       "authoringNote": "依官方語文領域課綱、單元 KG 與三個公立學校公開來源，重新撰寫中文聆聽與溝通表現 Ab-Ⅳ-3 題；未複製原文、選項、篇章或答案；待第二輪 AI／Terra 內容複核。"},
        "reviewStatus": "draft", "updatedAt": "2026-09-13", "lessonId": LESSON,
        "examPatternRefs": refs(), "solutionStrategy": strategy, "solutionSteps": steps,
    }
    (OUT / f"question-chinese-performance-1-iv-3-{i}.json").write_text(json.dumps(item, ensure_ascii=False, indent=2) + "\n", encoding="utf-8")

print(f"rewrote {len(DATA)} independent questions for {LESSON}")
