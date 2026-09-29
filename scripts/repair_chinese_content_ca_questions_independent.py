#!/usr/bin/env python3
"""Independently rewrite Chinese CA material-culture questions."""
import json
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
OUT = ROOT / "questions/chinese"
LESSON = "lesson-chinese-content-ca"
SOURCES = [
    ("https://www.sdjh.ntpc.edu.tw/var/file/0/1000/attach/16/pta_2229_1166226_19803.pdf", "新北市立石碇國中公開國文試題", "說明文證據與生活議題"),
    ("https://www.yacjh.kh.edu.tw/upload/221/101_30637/114%E4%B8%8B%E5%AD%B8%E6%9C%9F%E7%AC%AC%E4%B8%80%E6%AC%A1%E6%AE%B5%E8%80%83%E4%B8%89%E5%B9%B4%E7%B4%9A%E5%9C%8B%E6%96%87.pdf", "高雄市立鹽埕國中公開國文段考", "文本主旨、材料與推論"),
    ("https://www.jlsh.mlc.edu.tw/var/file/12/1012/img/113-2-7-4.pdf", "國立卓蘭高中附設國中部公開課程與試題資料", "跨段整合與限制性結論"),
]


def refs():
    return [{
        "url": url, "title": f"{title}；僅研究公開題型與能力方向，未複製原題。",
        "year": "113-114", "subject": "chinese", "locator": locator,
        "observedPattern": "公立學校國文評量以生活物件、說明材料與社會議題要求區分直接證據、合理推論、主旨範圍及多段資訊整合；本題採全新情境與語料。",
        "reuseDecision": "pattern-only", "status": "recorded", "locatorLevel": "paper"
    } for url, title, locator in SOURCES]


DATA = [
    ("物件直接證據", "研究一只修補多次的陶杯，哪項最能由物件本身直接觀察？", ["杯身有不同顏色的補釘與磨損痕跡", "它一定象徵家族團結", "每次修補都發生在節慶前", "使用者一定很珍惜它"], "A", "補釘與磨損是可直接觀察的物質特徵；象徵意義、時間與使用者情感都需要其他資料支持。", "先分開看得見的形制與需要訪談或文本才能知道的意義，再選直接證據。"),
    ("生活系統主旨", "文章從稻田、水圳、運輸寫到餐桌，最主要是要讀者理解什麼？", ["食物只要好吃就與生產無關", "一餐背後連結勞動、技術、資源與分配", "作者只是在介紹餐具外形", "運輸距離一定決定食物價值"], "B", "文章把一碗飯拆成生產與流通的路徑，主旨是看見飲食和勞動、基礎設施及資源的連結。", "整理段落共同回答的問題，再排除只擷取單一物件或過度絕對的選項。"),
    ("服飾多重功能", "比較制服、快時尚與修補時，哪個說法最能保留文本的複雜性？", ["制服一定壓抑，快時尚一定自由", "衣服只有遮蔽功能，不能談社會關係", "服飾兼具保護、身分、消費與環境勞動代價", "修補只是省錢，和價值選擇無關"], "C", "服飾同時涉及實用、身分與消費，也可能把成本轉移到環境與勞動者；不能用單一價值概括。", "把文本談到的功能與代價並列，檢查答案是否同時涵蓋便利和限制。"),
    ("空間記憶", "舊橋改建為寬路後，居民仍用舊橋墩位置約人；這項材料最支持哪個推論？", ["改建後所有舊記憶必然消失", "只要沿用舊稱呼，橋的功能就完全沒變", "建築形式的變化可能和地方記憶、定位方式並存", "交通設施和人的記憶不會互相影響"], "D", "舊橋墩仍是定位線索，顯示物質形式改變不必然消除人與空間的記憶關係。", "先指出材料中的改變與延續，再用兩者共同解釋，而不要把其中一面擴大成全部結論。"),
    ("可及性分析", "新車站縮短市中心到河岸的時間，但票價和轉乘距離使部分居民仍少去；評估交通改善時還要看什麼？", ["只看車站外觀是否新穎", "速度、費用、轉乘、身體條件與誰真正受益", "只問居民是否喜歡新車輛", "只要平均時間下降就代表公平"], "B", "交通可及性不只由速度決定，費用、距離、身體條件與使用者差異會改變實際受益。", "把『設施變好』拆成時間、成本、可使用性與分配效果四層再判斷。"),
    ("技術生命週期", "感應燈減少無人時段耗電，卻需要更換感應器；完整分析應加入哪個面向？", ["只看設備上市年份", "刪去維修問題才能證明進步", "把節電效益與材料、維修勞動及廢棄物一起比較", "只問外觀是否符合潮流"], "C", "科技功能應放回生命週期看，節電效益和維修材料、勞動及淘汰成本需要一起衡量。", "先承認技術帶來的效益，再追問製造、維修、替換與廢棄階段的代價。"),
    ("證據與推論", "文章明寫『碗邊有一道裂痕，並以布包好保存』；下列哪項屬合理推論而非直接描述？", ["碗邊有一道裂痕", "碗曾以布包裹保存", "這些痕跡可能反映長期使用與被珍惜的記憶", "文章提到碗的保存方式"], "C", "長期使用與珍惜是由裂痕、包裹和情境連結出的解釋，不是句面直接陳述。", "把選項逐一對照原文，只有需要把多個線索連結成解釋的才是推論。"),
    ("避免世代概括", "比較兩代衣櫃時，如何避免把個案習慣直接寫成整代人的性格？", ["指出材料、價格、工作時間與流行環境差異，並承認仍需更多家庭資料", "老一代一定節儉，學生一定浪費", "年代不同就表示所有人選擇相同", "選一代寫成唯一正確的生活方式"], "A", "世代比較必須交代條件、樣本與限制，不能把少數經驗化成整代人的道德評價。", "先找比較的實際條件，再檢查結論範圍是否超過資料能支持的程度。"),
    ("便利與代價", "介紹一次性餐盒只寫方便、便宜，沒有提清洗、製造與廢棄；最需要補哪類資訊？", ["增加更多讚美便利的形容詞", "補出資源、勞動、環境成本與不同使用者需求", "刪除價格避免讀者思考", "只放照片不說明材料"], "B", "物質文化分析要追問便利由誰生產、誰清理、耗用哪些資源及代價由誰承擔。", "從消費者眼前的好處延伸到生產、使用與廢棄全流程，補足被隱藏的成本。"),
    ("跨文整合流程", "要整合三篇物質文化短文，哪套方法最完整？", ["只列物品名稱，數量多就算理解", "只找象徵意義，不看使用情境", "用個人消費經驗直接評判作者", "先記材料、形制、使用者，再放回時代空間，最後區分證據、意義與評價"], "D", "完整閱讀要從物件走到生活系統，連結技術、制度、記憶與環境代價，並分層處理證據和評價。", "依序做物件觀察、情境定位、跨文連結、證據檢核與價值判斷，避免只停在名稱或感想。"),
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
        f"讀題定位：圈出「{tag}」與材料、使用者、時間、空間或成本的關鍵線索。",
        f"分層整理：先分直接描述、合理推論與價值評價，再依「{explanation}」確認答案範圍。",
        f"核對正解：選項 {target} 能由一項或多項文本證據支持，且沒有把局部經驗擴大成絕對結論。",
        "排除誘答：檢查是否只看物件外觀、忽略生產與使用脈絡，或加入文本沒有提供的心理與道德判斷。",
        "回讀驗證：把答案放回全文，確認它同時解釋材料、生活系統與限制條件。",
    ]
    item = {
        "id": f"question-chinese-content-ca-{i}", "subject": "chinese", "type": "single-choice",
        "prompt": prompt, "options": [{"id": chr(65 + j), "text": text} for j, text in enumerate(options)],
        "knowledgeIds": ["kg-chinese-content-ca"], "difficulty": "medium",
        "answer": {"value": target, "explanation": explanation},
        "provenance": {"origin": "original", "license": "All rights reserved", "sourceUrl": SOURCES[0][0],
                       "sourceLocator": "三所公立學校公開國文資料；只研究生活議題說明、物件證據、跨段整合與限制性推論。",
                       "authoringNote": "依官方語文領域課綱、單元 KG 與三個公立學校公開來源，重新撰寫 CA 物質文化與生活系統題；未複製原文、選項、篇章或答案；待第二輪 AI／Terra 內容複核。"},
        "reviewStatus": "draft", "updatedAt": "2026-09-13", "lessonId": LESSON,
        "examPatternRefs": refs(), "solutionStrategy": strategy, "solutionSteps": steps,
    }
    (OUT / f"question-chinese-content-ca-{i}.json").write_text(json.dumps(item, ensure_ascii=False, indent=2) + "\n", encoding="utf-8")

print(f"rewrote {len(DATA)} independent questions for {LESSON}")
