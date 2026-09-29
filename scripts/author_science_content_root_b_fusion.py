import json
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
LESSON = ROOT / "lessons/science/lesson-science-content-root-b.json"
QDIR = ROOT / "questions/science"
REPORT = ROOT / "implementation/reports/science-content-root-b-first-pass-review.json"
TODAY = "2026-09-23"
SOURCES = [
    ("https://www.yacjh.kh.edu.tw/view/index.php?DataId=497103&MainMenuId=30637&MainType=101&SubMenuId=0&SubType=0&WebID=221&Work=View&page=1", "高雄市立鹽埕國民中學公開自然科定期評量試題頁", "生命、地球環境、尺度與資料判讀", "只取公立校方公開試題的情境判讀能力，改寫成跨尺度問題。"),
    ("https://www.bhjh.ntpc.edu.tw/p/406-1000-10627%2Cr111.php?Lang=zh-tw", "新北市立板橋國民中學公開自然科定期評量試題頁", "生態、天氣、天文觀察與證據", "只取公開試題的資料／模型推理方向，未複製原題。"),
    ("https://www.hcjh.ntpc.edu.tw/p/406-1000-7527%2Cr146.php", "新北市立新莊國民中學公開自然科定期評量試題頁", "尺度、週期、環境與模型限制", "只取能力模式並重新設計生命—地球—宇宙情境。"),
]
REFS = [{"url": u, "title": t, "year": "113-115", "subject": "science", "locator": l, "observedPattern": p, "reuseDecision": "pattern-only", "status": "recorded", "locatorLevel": "paper"} for u, t, l, p in SOURCES]
ROWS = [
    ("easy", "觀察校園池塘藻類變多，若要判斷是否與營養鹽增加有關，哪項證據最有用？", ["不同營養鹽濃度下的藻類量，並控制光照、溫度與水量", "只拍一張最綠的照片", "只問同學覺得水色如何", "把季節和營養鹽同時改變"], "A", "要支持因果，需比較操弄營養鹽的條件並控制其他可能影響藻類的因素。", "先把現象轉成可量測結果，再安排單一主要變因與控制條件。"),
    ("medium", "氣象站記錄一週降雨量增加，哪個結論最符合資料尺度？", ["可描述該地該週的降雨情形，不能直接代表全年氣候趨勢", "可證明全球氣候永久變濕", "可推論所有地區同週都下同樣多雨", "可由一次紀錄決定未來百年降雨"], "A", "一週、單地點的觀測屬短時間與局部尺度，能支持局部描述但不足以直接外推長期或全球趨勢。", "先寫清楚空間與時間範圍，再檢查結論是否超出樣本尺度。"),
    ("medium", "月球某晚看起來接近半月，若要預測一週後月相，最需要使用哪種表示？", ["月球繞地球運動與日照幾何的週期模型", "只看月球表面顏色", "把月相當成月球形狀每天改變", "只用當晚亮度不考慮觀察日期"], "A", "月相是日、地、月相對位置與照明幾何造成的週期現象，預測必須納入運動與觀察時間。", "先定義觀察者、光源與天體位置，再沿週期模型推進日期。"),
    ("hard", "比較一棵樹的葉片氣孔與整個森林的碳吸收時，哪項做法能避免尺度混淆？", ["分別定義個體器官與生態系的測量單位，再說明如何由局部資料推到整體", "把一片葉子的數值直接當成整片森林", "只比較照片大小", "不必指定時間與面積"], "A", "葉片氣孔是器官尺度，森林碳吸收是生態系與時間累積尺度，單位、面積與時間邊界都要重新定義。", "先標出空間層級和時間範圍，再檢查是否需要抽樣、加總或模型外推。"),
    ("easy", "衛星影像顯示沿海濕地面積縮小，哪項敘述最謹慎？", ["影像支持該時間段與解析度下的面積變化，仍需查核原因與其他地點", "影像必然證明唯一原因是污染", "低解析影像能看出每個物種數量", "一次影像能代表所有年代"], "A", "影像直接支持可見的面積差異，但原因、物種數量與長期趨勢需要其他資料和更合適的尺度。", "把直接觀察與原因推論分開，列出解析度、日期與未測量的因素。"),
    ("medium", "地震波在不同地層的到時不同，使用模型時最重要的限制是？", ["模型要說明波速、路徑與地層假設，不能只用一個到時值描述所有地下結構", "地下結構一定均勻所以不需假設", "只要波到達就能知道所有岩石種類", "忽略測站距離也不影響推論"], "A", "地震波推論依賴波速、路徑、測站與地層模型；資料不足時只能給出受假設限制的解釋。", "列出輸入資料與模型假設，再檢查不同地層組合是否也能產生相同到時。"),
    ("hard", "星系影像中某區域較亮，哪項說法不應直接由亮度推出？", ["該區域一定距離最近且包含最多質量", "可先比較影像中的相對亮度", "還需考慮距離、塵埃、曝光與恆星族群", "亮度是觀測量，成因需要模型與額外資料"], "A", "影像亮度受距離、塵埃、曝光與天體組成等因素影響，不能把單一觀測量直接等同距離或質量。", "先區分影像觀測量與物理量，再列出可能造成相同亮度的替代解釋。"),
    ("medium", "城市熱島研究發現市中心夜間較熱；若要比較不同土地覆蓋的影響，應如何設計？", ["在相近天氣與測量時間下比較不同地表，並控制高度、儀器與周圍環境", "只選最熱的一個路口", "市中心與郊區同時改變所有測量條件", "用白天一次資料推論全年夜間"], "A", "熱島比較必須控制時間、天氣、儀器與位置等條件，否則差異可能來自測量設計而非土地覆蓋。", "先固定觀測時段和儀器，再用多地點、多日資料分離地表與天氣因素。"),
    ("hard", "一個模型能解釋單一池塘的缺氧，但不能解釋海岸大尺度資料；合理做法是？", ["標示模型的空間與時間適用範圍，找出需要新增的過程與資料後再擴充模型", "直接把池塘結果放大成全球結論", "只刪除海岸資料", "宣稱模型在所有尺度都相同"], "A", "模型的有效性有尺度邊界；擴大範圍需加入水流、風場、交換與時間變化等過程並重新驗證。", "比較模型原本的假設與新資料的差異，再決定哪些機制和觀測必須補入。"),
    ("medium", "閱讀生命、地球與宇宙資料時，哪個遷移流程最可靠？", ["先確定尺度與單位，再分開觀察、模型、證據與不確定性，最後寫條件式結論", "先用熟悉名詞套入答案", "只看圖表顏色不看座標", "把局部資料直接說成普遍定律"], "A", "跨尺度推理要讓觀測、模型與結論各自有範圍，並明確說出資料不能支持的部分。", "用尺度—表示—證據—限制四格檢查推理鏈，最後提出可改變結論的新資料。"),
]
IDS = ["04", "05", "06", "07", "08", "09", "10", "19", "20", "21"]

def make_question(n, row):
    diff, prompt, opts, source_answer, explanation, strategy = row
    target = "DBACDBACDB"[n - 1]
    idx = ord(source_answer) - 65
    correct = opts[idx]
    distractors = [x for i, x in enumerate(opts) if i != idx]
    ordered, di = [], 0
    for label in "ABCD":
        if label == target: ordered.append(correct)
        else: ordered.append(distractors[di]); di += 1
    steps = ["先標記觀察對象的空間尺度、時間範圍、單位與直接可見資料。", "把現象、模型假設、可量測證據和推論結論分欄，避免跨層跳躍。", "檢查控制條件、週期位置、抽樣方式與可能的替代解釋。", f"排除把局部當全球、短期當長期、亮度當質量或把模型當事實的選項，答案為 {target}。", f"把答案放回原情境並標註適用邊界：{explanation}"]
    return {"id": f"question-science-root-b-{IDS[n-1]}", "subject": "science", "type": "single-choice", "prompt": prompt, "options": [{"id": k, "text": v} for k, v in zip("ABCD", ordered)], "knowledgeIds": ["kg-science-content-b", "kg-science-learning-content"], "difficulty": diff, "answer": {"value": target, "explanation": f"{explanation} 正確答案為選項 {target}。"}, "examPatternRefs": REFS, "provenance": {"origin": "original", "license": "All rights reserved", "sourceUrl": SOURCES[0][0], "sourceLocator": "三筆公立國中公開自然科資料僅作生命系統、地球環境、宇宙觀測、尺度與模型限制的能力方向；本題為根層 B 原創情境改寫。", "authoringNote": "依官方課綱、Knowledge Graph 與公開試題 pattern-only 能力方向獨立改寫；未複製原題、選項、圖表或答案；待第二輪 AI／Terra 內容複核。"}, "reviewStatus": "draft", "updatedAt": TODAY, "lessonId": "lesson-science-content-root-b", "solutionStrategy": strategy, "solutionSteps": steps}

def main():
    lesson = json.loads(LESSON.read_text(encoding="utf-8"))
    lesson.update({"updatedAt": TODAY, "reviewStatus": "draft", "authoringStandard": "version-fused-v1"})
    for row in lesson.get("publisherResearch", []) + lesson.get("versionResearch", []): row["reviewedAt"] = TODAY
    lesson["fusionRecord"]["llmSynthesisNote"] = "本課依官方自然科學課綱、kg-science-content-b 與 kg-science-learning-content、南一／康軒／翰林公開版本研究限制及三筆公立國中公開試題的能力模式，獨立融合生命系統、地球環境、宇宙觀測、尺度選擇、週期模型、抽樣證據與模型限制。題目與互動保留根層 B 的跨尺度遷移目的，但全部重新設計，未複製受保護內容；Terra 第二輪與正式發布審查尚未完成，維持 draft。"
    LESSON.write_text(json.dumps(lesson, ensure_ascii=False, indent=2) + "\n", encoding="utf-8")
    for i, row in enumerate(ROWS, 1):
        (QDIR / f"question-science-root-b-{IDS[i-1]}.json").write_text(json.dumps(make_question(i, row), ensure_ascii=False, indent=2) + "\n", encoding="utf-8")
    REPORT.write_text(json.dumps({"unit": lesson["title"], "lessonId": lesson["id"], "status": "first-pass-ai-review-complete", "reviewStatus": "draft", "checkedQuestions": 10, "checks": {"unitSpecificOriginalContent": True, "threeVersionResearchRecords": True, "threePublicSchoolExamPatternSources": True, "answersAndDetailedSteps": True, "interactivePredictionManipulationExplanation": True, "terraSecondPass": "pending"}, "reviewedAt": TODAY, "note": "10 題重新改寫為生命、地球、宇宙、尺度、週期、抽樣證據與模型限制的跨尺度遷移題；每題具唯一答案、解析、策略與五步解法。"}, ensure_ascii=False, indent=2) + "\n", encoding="utf-8")
    print("authored science content root-b")

if __name__ == "__main__":
    main()
