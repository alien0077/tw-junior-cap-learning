#!/usr/bin/env python3
"""Independently rewrite Chinese technology-mediated communication questions."""
import json
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
OUT = ROOT / "questions/chinese"
LESSON = "lesson-chinese-performance-1-iv-4"
KG = "kg-chinese-performance-1-iv-4"
SOURCES = [
    ("https://www.sdjh.ntpc.edu.tw/var/file/0/1000/attach/16/pta_2229_1166226_19803.pdf", "新北市立石碇國中公開國文試題", "數位溝通、資訊與文本"),
    ("https://www.yacjh.kh.edu.tw/upload/221/101_30637/114%E4%B8%8B%E5%AD%B8%E6%9C%9F%E7%AC%AC一%E6%AC%A1%E6%AE%B5%E8%80%83%E4%B8%89%E5%B9%B4%E7%B4%9A%E5%9C%8B%E6%96%87.pdf", "高雄市立鹽埕國中公開國文段考", "媒體識讀、隱私與互動"),
    ("https://www.jlsh.mlc.edu.tw/var/file/12/1012/img/113-2-7-4.pdf", "國立卓蘭高中附設國中部公開課程與試題資料", "線上協作、來源與參與公平"),
]


def refs():
    return [{
        "url": url, "title": f"{title}；僅研究公開題型與能力方向，未複製原題。",
        "year": "113-114", "subject": "chinese", "locator": locator,
        "observedPattern": "公立學校國文評量以數位記錄、來源查核、線上回應、語氣與證據保留、參與公平、隱私同意及協作整理要求負責任的科技溝通；本題採全新語料。",
        "reuseDecision": "pattern-only", "status": "recorded", "locatorLevel": "paper"
    } for url, title, locator in SOURCES]


DATA = [
    ("紀錄目的", "小組用共享文件記錄訪談，最重要的第一步是什麼？", ["直接把所有語音轉成文字，不需人工核對", "只讓最熟悉工具的人決定全部內容", "把分享連結公開給所有人", "先說明記錄目的、欄位和誰負責確認內容"], "D", "先定義目的、欄位與責任，才能讓工具服務聆聽任務，避免資料堆積或錯誤轉錄。", "先問這份紀錄要支持什麼決策，再決定欄位、核對者與使用權限。"),
    ("官方查核", "群組收到「明天停課」截圖，運用科技查證時最合適的做法是？", ["看到轉傳很多就相信", "只看截圖標誌，不查原始來源", "立刻轉發給所有群組", "比對校方官方網站或正式通知，確認發布時間與適用對象"], "D", "數位訊息可能脫離脈絡，查證要回到可追溯來源、日期、對象與適用範圍。", "先開啟正式來源，再逐項核對發布者、時間、地區與公告全文。"),
    ("線上異議", "線上討論有人提出不同意見，哪種留言最能增進互動？", ["你又錯了，別浪費時間。", "按讚表示同意，不必說明理由。", "刪掉不同意見，讓討論更有效率。", "我理解你擔心執行時間；你提到的兩週根據哪項紀錄，我們一起補進表格嗎？"], "D", "好的數位回應先承接對方觀點，再提出可查證問題和共同工作方式，不靠攻擊或刪除異議。", "引用對方具體關注，再用問題邀請資料補充，讓異議成為協作入口。"),
    ("不確定語氣", "共享筆記把「受訪者說可能缺水」改成「社區一定會缺水」；最需要修正什麼？", ["把一定改成更大的字體", "刪掉受訪者身分，讓句子看似客觀", "只要寫進共享文件就代表已證實", "保留原話的不確定程度，區分受訪者說法、推論與待查資料"], "D", "共享記錄仍要維持來源、語氣與證據界線，不能把可能改成必然，也不能把轉錄當驗證。", "回看原始語句，標記說話者與限定語，再把待查資料另外列出。"),
    ("參與公平", "小組只用即時視訊討論，但有成員家中網路不穩；哪種安排較公平？", ["要求網路不穩者退出", "只放會議錄影，不提供其他方式", "因多數人方便就不調整", "提供錄音或文字摘要、非同步回應期限與替代提交方式"], "D", "科技增進互動也可能造成門檻；替代管道讓不同設備與時間條件的人仍能取得資訊和發言。", "先盤點參與障礙，再提供等價的資訊取得、回應與提交方式。"),
    ("錄音同意", "錄製訪談前，哪項做法最符合負責任的數位互動？", ["只要是學習活動就能默默錄音", "把原始錄音公開讓大家判斷", "錄音後才詢問是否介意", "先說明錄音目的、保存期限、觀看權限並取得受訪者同意"], "D", "科技保存聲音也增加隱私風險，事前告知、同意與權限是互動倫理的一部分。", "在錄製前說明用途、保存與分享範圍，讓對方能同意、拒絕或提出限制。"),
    ("訊息完整性", "用手機提醒組員會議異動，哪項資訊不可省略？", ["作者最喜歡的貼圖", "所有未確認的交通推測", "只有請注意三個字", "異動原因、日期時間、平台／地點、需回應的動作與查詢方式"], "D", "短訊息仍需保留完成行動的必要欄位，媒介變短不能刪掉時間、地點、動作與來源。", "用誰、何時、何地、改了什麼、要做什麼與去哪裡查六項檢查訊息。"),
    ("多源整理", "小組從錄音、文字留言與問卷得到不同意見，要如何整理？", ["把票數最多的說法當全部事實", "只選最容易輸入的資料", "刪除不同意見後再下結論", "標記每筆資料來源與時間，再分出共同點、差異、未確認處與待追問問題"], "D", "數位工具加快整理但不能代替來源判讀；共同點、差異與未知都要保留，才不製造假共識。", "先為每筆資料建立來源與時間，再分群比較，不把票數或輸入方便當可靠性標準。"),
    ("指涉清楚", "群組訊息只寫「這次先不用了」，不同成員不知道取消哪項活動；如何改善？", ["把語氣改強硬", "增加表情符號取代名詞", "只轉傳一次避免追問", "補上對象、活動名稱、時間、取消／延期狀態與後續聯絡方式"], "D", "數位文字缺少現場語氣與共同背景，更需要明確指涉和行動資訊降低誤讀。", "把省略的對象、事件、時間與狀態補齊，再說明收件者下一步。"),
    ("完整線上討論", "要用科技完成一次有品質的線上討論，哪套流程最完整？", ["先開直播，想到什麼就說", "只讓主持人發言", "用投票結果取代理由與資料查證", "先定目的與規則，提供可查證資料與來源，安排同步／非同步發言，整理共同點與歧異，最後確認決議與權限"], "D", "完整數位互動結合工具、來源、參與公平、記錄、隱私與後續責任，科技不會自動產生共識。", "依序規劃目的、規則、資料、參與管道、整理方式、決議與權限。"),
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
        f"讀題定位：圈出「{tag}」與工具、來源、時間、權限、語氣或參與條件。",
        f"拆解資訊：先分內容、來源、使用權限與互動效果，再依「{explanation}」判斷。",
        f"核對正解：選項 {target} 能降低誤讀或排除風險，並保留可查證、可參與與可修正的空間。",
        "排除誘答：檢查是否把轉發量代替來源、把共享代替驗證、把多數方便代替公平，或忽略隱私同意。",
        "回讀驗證：確認工具選擇、文字內容、資料來源、權限與後續責任彼此一致。",
    ]
    item = {
        "id": f"question-chinese-performance-1-iv-4-{i}", "subject": "chinese", "type": "single-choice",
        "prompt": prompt, "options": [{"id": chr(65 + j), "text": text} for j, text in enumerate(options)],
        "knowledgeIds": [KG], "difficulty": "medium",
        "answer": {"value": target, "explanation": explanation},
        "provenance": {"origin": "original", "license": "All rights reserved", "sourceUrl": SOURCES[0][0],
                       "sourceLocator": "三所公立學校公開國文資料；只研究數位溝通、來源查核、隱私同意、參與公平與線上協作。",
                       "authoringNote": "依官方語文領域課綱、單元 KG 與三個公立學校公開來源，重新撰寫中文聆聽與溝通表現 Ab-Ⅳ-4 題；未複製原文、選項、篇章或答案；待第二輪 AI／Terra 內容複核。"},
        "reviewStatus": "draft", "updatedAt": "2026-09-13", "lessonId": LESSON,
        "examPatternRefs": refs(), "solutionStrategy": strategy, "solutionSteps": steps,
    }
    (OUT / f"question-chinese-performance-1-iv-4-{i}.json").write_text(json.dumps(item, ensure_ascii=False, indent=2) + "\n", encoding="utf-8")

print(f"rewrote {len(DATA)} independent questions for {LESSON}")
