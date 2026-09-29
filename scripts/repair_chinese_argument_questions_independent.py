#!/usr/bin/env python3
"""Independently rewrite Chinese argument-and-evidence questions."""
import json
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
OUT = ROOT / "questions/chinese"
LESSON = "lesson-chinese-argument-evidence-basics"
SOURCES = [
    ("https://www.sdjh.ntpc.edu.tw/var/file/0/1000/attach/16/pta_2229_1166226_19803.pdf", "新北市立石碇國中公開國文試題", "議論文主張、論據與推論"),
    ("https://www.yacjh.kh.edu.tw/upload/221/101_30637/114%E4%B8%8B%E5%AD%B8%E6%9C%9F%E7%AC%AC%E4%B8%80%E6%AC%A1%E6%AE%B5%E8%80%83%E4%B8%89%E5%B9%B4%E7%B4%9A%E5%9C%8B%E6%96%87.pdf", "高雄市立鹽埕國中公開國文段考", "證據品質、反論與結論範圍"),
    ("https://www.jlsh.mlc.edu.tw/var/file/12/1012/img/113-2-7-4.pdf", "國立卓蘭高中附設國中部公開課程與試題資料", "觀點、資料與可檢驗主張"),
]


def refs():
    return [{
        "url": url, "title": f"{title}；僅研究公開題型與能力方向，未複製原題。",
        "year": "113-114", "subject": "chinese", "locator": locator,
        "observedPattern": "公立學校國文評量要求辨識主張、理由與證據，檢查樣本、關聯、反論、結論範圍及可檢驗性；本題採全新語料。",
        "reuseDecision": "pattern-only", "status": "recorded", "locatorLevel": "paper"
    } for url, title, locator in SOURCES]


DATA = [
    ("事實論據", "要支持「固定運動有助於維持健康」，哪項最適合作為事實性論據？", ["我覺得運動的人看起來比較有精神。", "一項記錄固定族群運動頻率與健康指標的長期研究。", "很多人都說運動很好。", "運動服的款式越來越多。"], "B", "有研究方法、對象與觀察指標的資料可被檢查，能直接支援健康效果的討論；感想、傳聞與服裝款式不足以證明。", "先找能被查驗的對象、方法和結果，再判斷資料是否真的回答主張。"),
    ("論據功能", "文章先主張「校園應增加飲水設備」，接著列出各區使用量與排隊時間；這些數據主要扮演什麼角色？", ["標題", "反問", "論據", "作者簽名"], "C", "使用量與排隊時間是用來支持增加設備的資料，因此在論證中屬於論據。", "先找作者希望讀者接受的判斷，再問後面的資料是在支持、反駁還是裝飾它。"),
    ("樣本與普遍結論", "文章寫「這家店一定是全市最好吃，因為我的三位朋友都喜歡」；最適切的批判是？", ["朋友偏好未必代表全市，少數經驗不足以支持普遍結論。", "只要朋友超過三人就能證明。", "飲食不能成為議論題材。", "句子沒有使用標點符號。"], "A", "三位朋友的偏好只能提供局部經驗，不能直接推出全市排名；需更多樣本與明確比較方法。", "圈出結論中的範圍詞，再檢查論據的樣本數與代表性是否足以承擔該範圍。"),
    ("主張辨識", "一段文字先列出圖書館延長開放後的使用人次，最後寫「因此學校應增加晚間閱讀空間」；主要主張是？", ["圖書館有使用人次", "有人在晚間閱讀", "資料列出使用變化", "學校應增加晚間閱讀空間"], "D", "主張是作者希望讀者接受的政策判斷；前面的使用人次屬於支持它的資料。", "辨認哪句帶有應然判斷或行動要求，再把敘述性資料和結論分開。"),
    ("補強論證", "要補強「固定運動可能改善睡眠」的論點，哪項資料最有用？", ["一張設計漂亮的海報", "作者的暱稱", "有明確睡眠指標、觀察期間與運動紀錄的研究", "沒有日期的轉貼"], "C", "同時記錄運動與睡眠指標、期間和方法的研究，能直接檢查兩者關係，比外觀或無來源轉貼更有力。", "確認補充資料是否測量主張中的兩個變項，並檢查時間、方法與來源。"),
    ("個案界線", "若論據只描述一個人的減糖經驗，最合理的判斷是？", ["一定能代表全體。", "完全不能提供任何線索。", "可作為具體例子，但不足以代表所有人。", "必然已是統計結論。"], "C", "個案可讓讀者理解可能經驗，但代表性有限；若要推及全體，需要更多樣本與研究設計。", "把『提供例子』和『代表族群』分開，檢查結論是否比資料範圍更大。"),
    ("關聯檢查", "檢查論據是否真的支持主張時，哪個問題最直接？", ["作者用了幾個標點？", "文章有幾行？", "標題是否押韻？", "這項資料能否透過合理步驟支持該結論？"], "D", "關聯檢查要問資料如何導向結論，並確認中間推理沒有缺口；版面與押韻不代表論證成立。", "把主張和論據寫成箭頭，補出中間推理，再找是否有未證明的跳躍。"),
    ("反論功能", "作者先承認「增加設備需要經費」，接著說明可分期改善並提出預算資料；這段最可能有何功能？", ["刪除原本主張", "處理反論並用新資料強化主張", "改變文章字體", "提供頁碼"], "B", "承認成本是反方疑慮，再提出分期與預算回應，能讓原主張更完整而非假裝沒有問題。", "找出作者承認的疑慮，再看後文是否回應它、限制它或提出替代方案。"),
    ("可檢驗改寫", "要把「有人喜歡早起」改成較可檢驗的主張，哪項最適合？", ["大家一定喜歡早起。", "早起很棒。", "我覺得早起很漂亮。", "在明確日期調查的受訪者中，有多少人偏好早起？"], "D", "明確交代調查對象與時間，並要求可計數結果，才能檢查主張是否成立。", "把模糊的『有人』改成對象、時間與可觀察指標，避免把價值感受當事實。"),
    ("感受與證據", "下列哪項最可能把個人感受誤當成足以支持普遍結論的證據？", ["研究記錄兩組結果並交代樣本數。", "觀察者說明測量方法。", "資料列出調查日期與回收方式。", "我覺得這方法有效，所以所有人都適用。"], "D", "個人感受可以是經驗線索，卻不能直接推出所有人適用；需要樣本、方法與比較資料。", "辨認句子是否從『我』跳到『所有人』，再檢查中間是否缺少可檢驗資料。"),
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
        f"讀題定位：圈出「{tag}」與主張、論據、樣本、方法、反論或結論範圍。",
        f"拆解論證：把作者要讀者接受的判斷和支持資料分開，再依「{explanation}」檢查推理關係。",
        f"核對正解：選項 {target} 能直接回應題目要求，且資料品質與結論範圍相互匹配。",
        "排除誘答：檢查是否把感想、傳聞、外觀或單一個案誤當證據，或讓小範圍資料支撐過大的結論。",
        "回讀驗證：重新連起論據到主張的推理鏈，確認沒有未說明的樣本、因果或代表性跳躍。",
    ]
    item = {
        "id": f"question-chinese-argument-{i}", "subject": "chinese", "type": "single-choice",
        "prompt": prompt, "options": [{"id": chr(65 + j), "text": text} for j, text in enumerate(options)],
        "knowledgeIds": ["kg-chinese-content-bd-iv-1"], "difficulty": "medium",
        "answer": {"value": target, "explanation": explanation},
        "provenance": {"origin": "original", "license": "All rights reserved", "sourceUrl": SOURCES[0][0],
                       "sourceLocator": "三所公立學校公開國文資料；只研究主張、論據、樣本、反論與可檢驗推論。",
                       "authoringNote": "依官方語文領域課綱、單元 KG 與三個公立學校公開來源，重新撰寫論證與證據基礎題；未複製原文、選項、篇章或答案；待第二輪 AI／Terra 內容複核。"},
        "reviewStatus": "draft", "updatedAt": "2026-09-13", "lessonId": LESSON,
        "examPatternRefs": refs(), "solutionStrategy": strategy, "solutionSteps": steps,
    }
    (OUT / f"question-chinese-argument-{i}.json").write_text(json.dumps(item, ensure_ascii=False, indent=2) + "\n", encoding="utf-8")

print(f"rewrote {len(DATA)} independent questions for {LESSON}")
