#!/usr/bin/env python3
"""Record public-school publisher evidence for English learning performance 6-9."""
import json
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
REPORT = ROOT / "implementation/reports/publisher-chapter-evidence-samples.json"
BLOCKERS = ROOT / "implementation/reports/blockers.json"
SOURCES = [
    ("nani", "https://course.cyc.edu.tw/upfile/course113/sub1/15636172843290327.pdf", "南一版七至九年級公立課程計畫；學習態度、策略、文化理解與思考判斷能力的教材及評量定位。"),
    ("kanghsuan", "https://course.cyc.edu.tw/upfile/course112/sub1/15342166894673419.pdf", "康軒版七至九年級公立課程計畫；學習方法、文化溝通、資訊組織與文本推論的教材及評量定位。"),
    ("hanlin", "https://course.cyc.edu.tw/upfile/course114/sub1/15939623345151225.pdf", "翰林版七至九年級公立課程計畫；自主學習、跨文化表達、資料判讀與事實意見辨識的教材及評量定位。"),
]

UNITS = [
    ("lesson-english-performance-6", "學習興趣與態度", ["學習動機", "課堂參與", "自主調整"], "把學習態度從抽象口號轉成可觀察的預習、提問、練習與修正行動，並依學習紀錄判斷下一步。", "把有沒有完成作業當成全部證據，忽略方法、投入與修正歷程。"),
    ("lesson-english-performance-6-iv-1", "6-Ⅳ-1：積極參與課堂練習", ["課堂練習", "參與", "回饋"], "先辨認練習目標，再用完整回應、同儕協作與回饋修正留下參與證據，而不是只追求搶答。", "坐在課堂中不等於參與；需指出具體回應或修正如何對應目標。"),
    ("lesson-english-performance-6-iv-2", "6-Ⅳ-2：預習複習整理", ["預習", "複習", "整理"], "預習先建立問題，複習再用錯誤與遺漏回查，最後以自己的表格、例句或索引整理可再使用的知識。", "把重新抄寫全部內容當成複習，卻沒有檢查理解或錯誤。"),
    ("lesson-english-performance-6-iv-3", "6-Ⅳ-3：參與提升英語活動", ["英語活動", "延伸練習", "目標"], "從活動規則與語言目標選擇合適任務，透過表演、遊戲、任務或交流把課內語言用到新的互動情境。", "只看活動是否有趣，未能說明活動如何增加語言使用。"),
    ("lesson-english-performance-6-iv-4", "6-Ⅳ-4：接觸課外多元素材", ["課外素材", "多模態", "選材"], "依程度與目的接觸歌曲、短文、影片、圖像或網站，先抓主要訊息，再記錄素材形式如何影響理解。", "素材越難越好；忽略長度、語速、主題與自身目的。"),
    ("lesson-english-performance-6-iv-5", "6-Ⅳ-5：主動查詢工具書或網路", ["查詢", "工具書", "網路查證"], "先寫出不知道的部分與查詢條件，再比較字典、參考書或可靠網站的結果，記下可追溯的證據與限制。", "看到搜尋結果第一筆就照抄，沒有核對語境、作者或日期。"),
    ("lesson-english-performance-6-iv-6", "6-Ⅳ-6：運用網路或課外資源分享", ["資源分享", "著作權", "摘要"], "分享前確認來源、授權與讀者需求，以自己的話摘要重點並附查閱資訊，讓他人能理解且重新查找。", "把連結貼出來就算分享，忽略來源可信度與改寫界線。"),
    ("lesson-english-performance-7", "學習方法與策略", ["學習策略", "選擇方法", "自我監控"], "比較不同策略在字義、閱讀、口語與寫作任務中的適用條件，用學習紀錄判斷何時保留、調整或更換策略。", "把某一種讀書法當成所有任務都適用，未看任務目標與證據。"),
    ("lesson-english-performance-7-iv-1", "7-Ⅳ-1：字典依上下文查意義", ["上下文", "詞義", "字典"], "先用句內線索預測詞義，再以詞性、搭配與例句查證，最後把選定義項放回原句檢查是否通順。", "只選字典第一個義項，忽略詞性、搭配與上下文限制。"),
    ("lesson-english-performance-7-iv-2", "7-Ⅳ-2：利用背景知識", ["背景知識", "預測", "文本查證"], "先把相關經驗轉成可檢驗的預測，再回到文本尋找支持或修正預測的字句，不讓先備印象取代證據。", "背景知識與文本矛盾時仍堅持原本想法。"),
    ("lesson-english-performance-7-iv-3", "7-Ⅳ-3：非語言與語言溝通策略", ["溝通策略", "非語言線索", "修補"], "遇到詞彙不足時結合手勢、圖示、重述、請對方放慢或換句話說，依對方反應判斷溝通是否真的完成。", "把單一手勢或翻譯工具當成萬用解法，沒有確認對方理解。"),
    ("lesson-english-performance-7-iv-4", "7-Ⅳ-4：把討論技巧轉移學習", ["討論技巧", "轉移", "提問回應"], "把輪流發言、追問理由、整理共識與禮貌異議轉用到新的學習任務，並說明情境改變後要調整的做法。", "只複製原活動句型，沒有根據新任務的受眾與目的調整。"),
    ("lesson-english-performance-7-iv-5", "7-Ⅳ-5：學習計畫與自我監控", ["學習計畫", "檢核點", "調整"], "把長目標拆成有期限、可觀察的練習，設計中途檢核點，依成果與困難調整時間、材料或策略。", "只列願望或時程，沒有成功條件與修正依據。"),
    ("lesson-english-performance-8", "文化理解", ["文化脈絡", "比較", "尊重"], "從節慶、日常禮儀與生活制度的具體材料比較文化現象，區分可觀察差異與不宜武斷的價值判斷。", "把單一案例當成整個文化的固定特徵。"),
    ("lesson-english-performance-8-iv-1", "8-Ⅳ-1：介紹國內節慶", ["國內節慶", "脈絡", "英文介紹"], "以時間、地點、參與者、活動與意義組織國內節慶介紹，選擇能支持主旨的資料，避免只列活動名稱。", "只翻譯節慶名稱，沒有交代活動如何與地方生活相連。"),
    ("lesson-english-performance-8-iv-2", "8-Ⅳ-2：介紹國外節慶", ["國外節慶", "資料組織", "文化說明"], "以讀者需要的背景資訊說明國外節慶，標明資料來源與不確定處，避免把媒體印象當作普遍事實。", "把網路上的單一觀光描述寫成所有人都如此生活。"),
    ("lesson-english-performance-8-iv-3", "8-Ⅳ-3：比較國內外節慶習俗", ["跨文化比較", "相同與差異", "比較基準"], "先固定比較面向，再找兩邊可核對的資料，分別寫相同、差異與可能原因，不用高低優劣取代分析。", "只列兩國不同，沒有共同基準或證據。"),
    ("lesson-english-performance-8-iv-4", "8-Ⅳ-4：尊重欣賞不同文化", ["文化尊重", "觀點", "避免刻板印象"], "辨認描述中的觀點與權力位置，使用具體而不貶抑的語言表達欣賞，遇到陌生做法先提問脈絡再下結論。", "用表面稱讚或刻板標籤代替理解與尊重。"),
    ("lesson-english-performance-8-iv-5", "8-Ⅳ-5：基本世界觀", ["全球連結", "多元觀點", "世界議題"], "從生活物件、資訊流動或環境議題追蹤地方與世界的連結，並比較不同地區受到的影響與回應。", "把世界觀縮成國家清單，沒有事件、證據與觀點關係。"),
    ("lesson-english-performance-8-iv-6", "8-Ⅳ-6：國際生活基本禮儀", ["國際禮儀", "情境", "語氣"], "依身分、場合、媒介與文化期待選擇問候、請求、拒絕或致謝方式，並觀察對方反應後修正語氣。", "背一套固定禮貌句，忽略關係、場合與對方感受。"),
    ("lesson-english-performance-9", "邏輯思考、判斷與創造力", ["資訊推理", "分類比較", "創意解決"], "把文本或資料拆成主張、證據與關係，經由比較分類、因果判斷與替代方案形成可說明的結論。", "只看答案是否合理，沒有指出資訊之間的邏輯連結。"),
    ("lesson-english-performance-9-iv-1", "9-Ⅳ-1：依資訊推論", ["推論", "證據", "結論範圍"], "先區分文本明示與讀者推得的內容，再用多筆線索建立推論，並標示哪些部分仍不能確定。", "把自己的常識或猜測寫成文本已證實的事實。"),
    ("lesson-english-performance-9-iv-2", "9-Ⅳ-2：比較分類排序資訊", ["比較", "分類", "排序"], "先定義比較欄位與排序規則，再整理資料的共同點、差異與例外，讓結論能回扣原始資訊。", "改用不同標準排序卻沒有說明，導致看似矛盾的結論。"),
    ("lesson-english-performance-9-iv-3", "9-Ⅳ-3：上下文釐清因果", ["上下文", "因果", "連接詞"], "追蹤事件先後、因果連接詞與條件限制，分辨真正原因、伴隨現象與結果，避免只依時間順序下結論。", "事件先發生就當成原因，忽略文本中的條件與證據。"),
    ("lesson-english-performance-9-iv-4", "9-Ⅳ-4：從文本線索分辨事實意見", ["事實", "意見", "文本線索"], "檢查句子是否可由資料驗證、是否含價值詞或推測語氣，再以證據區分事實敘述、個人判斷與混合句。", "把語氣肯定當成事實，或把所有帶形容詞的句子一律判成意見。"),
]


def main():
    data = json.loads(REPORT.read_text(encoding="utf-8"))
    units = {item["lessonId"]: item for item in data["units"]}
    for lesson_id, title, core, representation, assessment in UNITS:
        units[lesson_id] = {
            "lessonId": lesson_id,
            "title": title,
            "evidenceStatus": "chapter-level-recorded-pending-fusion-review",
            "sources": [
                {
                    "publisher": publisher,
                    "sourceUrl": url,
                    "sourceKind": "public-school-course-plan-identifying-publisher-material",
                    "locator": locator,
                    "accessedAt": "2026-09-21",
                    "observedConcepts": [title, *core],
                    "observedRepresentations": [representation],
                    "observedAssessment": [assessment],
                    "licenseBoundary": "僅記錄公立學校課程計畫的出版商、單元定位與評量方向；不複製教材正文、歌詞、題目、答案或版面。",
                }
                for publisher, url, locator in SOURCES
            ],
            "fusionReview": {
                "commonCore": core,
                "differencesToReview": [representation, assessment],
                "originalSynthesisBoundary": "三版本融合、內容／版權審查與 Terra 複核完成前維持 draft，不升級 publisher status。",
            },
        }
    data["units"] = sorted(units.values(), key=lambda item: item["lessonId"])
    data["unitCount"] = len(data["units"])
    data["updatedAt"] = "2026-09-21"
    REPORT.write_text(json.dumps(data, ensure_ascii=False, indent=2) + "\n", encoding="utf-8")
    blockers = json.loads(BLOCKERS.read_text(encoding="utf-8"))
    for blocker in blockers.get("blockers", []):
        if isinstance(blocker.get("reason"), str):
            blocker["reason"] = blocker["reason"].replace("Eight hundred thirty-five unit samples", "Eight hundred seventy unit samples")
    BLOCKERS.write_text(json.dumps(blockers, ensure_ascii=False, indent=2) + "\n", encoding="utf-8")
    print(json.dumps({"unitCount": data["unitCount"], "added": len(UNITS)}, ensure_ascii=False))


if __name__ == "__main__":
    main()
