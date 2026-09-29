#!/usr/bin/env python3
"""Independently rewrite Chinese discussion and feedback questions for Ab-IV-2."""
import json
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
OUT = ROOT / "questions/chinese"
LESSON = "lesson-chinese-performance-2-iv-2"
KG = "kg-chinese-performance-2-iv-2"
SOURCES = [
    ("https://www.sdjh.ntpc.edu.tw/var/file/0/1000/attach/16/pta_2229_1166226_19803.pdf", "新北市立石碇國中公開國文試題", "討論提問、回饋與論證"),
    ("https://www.yacjh.kh.edu.tw/upload/221/101_30637/114%E4%B8%8B%E5%AD%B8%E6%9C%9F%E7%AC%AC一%E6%AC%A1%E6%AE%B5%E8%80%83%E4%B8%89%E5%B9%B4%E7%B4%9A%E5%9C%8B%E6%96%87.pdf", "高雄市立鹽埕國中公開國文段考", "公共議題、條件與多方回應"),
    ("https://www.jlsh.mlc.edu.tw/var/file/12/1012/img/113-2-7-4.pdf", "國立卓蘭高中附設國中部公開課程與試題資料", "協商、回饋與可修正行動"),
]


def refs():
    return [{
        "url": url, "title": f"{title}；僅研究公開題型與能力方向，未複製原題。",
        "year": "113-114", "subject": "chinese", "locator": locator,
        "observedPattern": "公立學校國文評量以開放追問、群體詞、隱含條件、證據回饋、反例、協商執行欄位、成效與代價及修正循環要求口語互動；本題採全新語料。",
        "reuseDecision": "pattern-only", "status": "recorded", "locatorLevel": "paper"
    } for url, title, locator in SOURCES]


DATA = [
    ("開放追問", "聽完「校園應增加遮蔭」的提案後，哪個問題最能打開討論？", ["你是不是根本沒做功課？", "這方案一定會成功，對吧？", "我已經知道答案，不必再問。", "你觀察到哪些時段最需要遮蔭，能說明資料來源嗎？"], "D", "開放問題要求提案者說明觀察、條件與來源，能補充資訊而非指責或預設答案。", "先把評價詞改成時間、對象、資料與方法問題，讓對方有具體回答入口。"),
    ("群體詞查核", "對方說「大家都覺得新規則更方便」；哪個追問最適合？", ["所以所有人一定同意嗎？", "既然方便就不用資料了吧？", "你說大家，我直接相信。", "這裡的大家包括哪些人？你透過問卷、訪談還是其他資料知道的？"], "D", "好的追問把模糊群體詞拆成對象、方法與來源，讓主張變得可檢查，不嘲諷也不盲信。", "先確認群體範圍，再問資料取得方式與時間，避免把少數經驗寫成全體共識。"),
    ("隱含條件", "同學說「延後集合一定會讓大家更輕鬆」；哪個回應能澄清隱含條件？", ["你錯了，延後只會更糟。", "大家更輕鬆，不必再查條件。", "我也覺得輕鬆，這就算證明。", "若延後集合，交通和工作人員時間是否能配合？你根據什麼判斷大家更輕鬆？"], "D", "一定背後有交通、工作、時間與受影響者等假設；回應要把未說出的條件拉出來。", "圈出絕對詞，再逐一追問對象、資源、例外與支持判斷的資料。"),
    ("具體回饋", "同學報告資料豐富，但結論和資料的連結不清楚；哪句回饋最有幫助？", ["內容太亂，全部重做。", "資料很多，所以結論一定正確。", "我不喜歡這個主題，不必修改。", "你整理的訪談很完整；若再說明哪兩筆資料支持結論，聽者會更容易跟上。"], "D", "具體回饋先指出可保留的優點，再指出可操作的改進位置與理由，不籠統否定或空泛讚美。", "使用『已完成的部分＋缺口＋可執行修改』三段式回饋，讓對方知道如何重做。"),
    ("尊重自主", "對方分享個人經驗時，哪種回饋最尊重自主？", ["我知道你該怎麼做，照做就好。", "你的經驗太普通，沒有討論價值。", "我把你的故事轉給別人評分。", "我聽見你最在意的是時間壓力；你希望我先聽完，還是一起想方法？"], "D", "回饋先反映重點，再確認對方需要陪伴、澄清或解法，讓對方保有選擇，不擅自公開或接管。", "先確認理解與需求，再提供選項，避免把自己的解法直接套給對方。"),
    ("反例追問", "有人主張「設置提醒就能讓所有人準時」；哪個追問最能測試限制？", ["你能保證所有人會準時嗎？", "提醒很有用，不需討論例外。", "我找一個成功案例就夠了。", "若有人沒有手機或收到提醒仍不理解要求，方案要如何處理？有這類資料嗎？"], "D", "反例把所有的邊界具體化，並要求替代方案或資料，能檢查方法而非只增加信心。", "保留主張前提，再設計可能失效的情境，追問如何支援與評估。"),
    ("執行確認", "小組討論後大家都說「好，那就照辦」；主持人還應確認什麼？", ["只要點頭，細節自然一致。", "誰聲音最大就由誰決定。", "立即結束，不必留下紀錄。", "具體事項、負責人、期限、例外情況與檢查結果的方法。"], "D", "口頭共識可能掩蓋不同理解，確認執行欄位和檢查方式，才能把同意轉成可追蹤行動。", "把共識改寫成誰在何時做什麼、遇到什麼例外、用什麼指標確認完成。"),
    ("成效與代價", "試辦結果顯示新制度減少排隊，卻增加清潔時間；哪種回饋最合邏輯？", ["有成本就宣布制度完全失敗。", "排隊減少就忽略清潔人員負擔。", "把清潔時間從報告刪掉。", "保留減少排隊的效果，補查清潔成本並調整流程，再用下一輪資料檢查。"], "D", "有證據的回饋同時承認成效與代價，提出可修正方案，不把單一指標當全部結論。", "把正面結果與負面成本並列，再提出修改假設與下一輪檢查指標。"),
    ("提問順序", "要理解一項尚不清楚的公共提案，哪種提問順序最合理？", ["先批評說話者，再要求接受你的答案。", "先問細枝末節，永遠不確認主旨。", "先投票，再決定要問什麼。", "先確認主張與目標，再問資料和條件，追問受影響者與例外，最後確認方案與評估方式。"], "D", "提問從主旨到證據、條件、影響與評估，能逐步縮小不確定性並支援決策。", "按照主張—證據—條件—利害關係人—評估的順序，避免在不知目標時鑽細節。"),
    ("回饋循環", "要在會議提出能促進理解與修正的回饋，哪套做法最完整？", ["只表達喜歡或不喜歡，不說原因。", "用權威身分宣布錯誤，不讓對方回應。", "只挑一個成功結果，要求所有人照做。", "先重述主張，指出可確認證據，再提出疑問與例外，說明影響，最後共同約定修正與檢查方式。"], "D", "完整回饋把理解、證據、提問、分寸、協商和後續驗證連成循環，讓溝通產生可修正行動。", "依序確認理解、指出證據、提出問題、說明後果、協商修改與安排回查。"),
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
        f"讀題定位：圈出「{tag}」與主張、群體詞、條件、回饋、例外或執行欄位。",
        f"拆解互動：先確認對方真正說了什麼，再依「{explanation}」設計可查證、可回應的問題。",
        f"核對正解：選項 {target} 能降低模糊、保留不同聲音，並把討論推向可執行與可檢查的下一步。",
        "排除誘答：檢查是否用權威、嘲諷、盲信、單一成功案例或投票取代理由與條件分析。",
        "回讀驗證：確認問題、回饋、行動責任與評估方式形成完整的協商循環。",
    ]
    item = {
        "id": f"question-chinese-performance-2-iv-2-{i}", "subject": "chinese", "type": "single-choice",
        "prompt": prompt, "options": [{"id": chr(65 + j), "text": text} for j, text in enumerate(options)],
        "knowledgeIds": [KG], "difficulty": "medium",
        "answer": {"value": target, "explanation": explanation},
        "provenance": {"origin": "original", "license": "All rights reserved", "sourceUrl": SOURCES[0][0],
                       "sourceLocator": "三所公立學校公開國文資料；只研究開放追問、證據回饋、例外、協商與可修正行動。",
                       "authoringNote": "依官方語文領域課綱、單元 KG 與三個公立學校公開來源，重新撰寫中文口語表達與討論回饋 Ab-Ⅳ-2 題；未複製原文、選項、篇章或答案；待第二輪 AI／Terra 內容複核。"},
        "reviewStatus": "draft", "updatedAt": "2026-09-13", "lessonId": LESSON,
        "examPatternRefs": refs(), "solutionStrategy": strategy, "solutionSteps": steps,
    }
    (OUT / f"question-chinese-performance-2-iv-2-{i}.json").write_text(json.dumps(item, ensure_ascii=False, indent=2) + "\n", encoding="utf-8")

print(f"rewrote {len(DATA)} independent questions for {LESSON}")
