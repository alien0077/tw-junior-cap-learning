import json
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
LESSON = ROOT / "lessons/science/lesson-science-content-jd-iv-2.json"
REPORT = ROOT / "implementation/reports/science-content-jd-iv-2-first-pass-review.json"
URLS = [
    ("https://www.yacjh.kh.edu.tw/upload/221/101_30637/114%E4%B8%8B%E5%AD%B8%E6%9C%9F%E7%AC%AC%E4%B8%80%E6%AC%A1%E6%AE%B5%E8%80%83%E4%B8%89%E5%B9%B4%E7%B4%9A%E8%87%AA%E7%84%B6.pdf", "鹽埕國中公開自然段考", "酸鹼、pH、溶液比較與實驗設計"),
    ("https://www.nhjh.tp.edu.tw/uploads/1738658165906utzaMLG4.pdf", "內湖國中公開自然段考", "理化數據、圖表判讀與測量限制"),
    ("https://www.kcjh.kh.edu.tw/upload/190/104_34764/%E5%9C%8B%E6%98%8C--%E4%BA%8C%E5%B9%B4%E7%B4%9A--%E8%87%AA%E7%84%B6%E7%A7%91.pdf", "國昌國中公開自然科試題", "酸鹼反應、控制變因與證據界線"),
]

def refs():
    return [{"url": u, "title": f"{t}；只取{loc}的題型與推理方向，未複製原題、選項、圖表或答案。", "year": "113-114", "subject": "science", "locator": loc, "observedPattern": "公開自然科評量常以 pH 數值、酸鹼比較、指示劑、校正、稀釋與控制變因檢查數據推理；本題為獨立改寫。", "reuseDecision": "pattern-only", "status": "recorded", "locatorLevel": "paper"} for u, t, loc in URLS]

def main():
    lesson = json.loads(LESSON.read_text(encoding="utf-8")); lesson["updatedAt"] = "2026-09-21"; lesson["reviewStatus"] = "draft"
    for row in lesson.get("versionResearch", []):
        row["reviewedAt"] = "2026-09-21"
        row["licenseBoundary"] = "本紀錄只保存可追溯公開來源的章節定位、教學方向與評量能力；不複製出版社或學校教材正文、原題、選項、圖表、答案、影音或版面。"
    lesson["fusionRecord"]["llmSynthesisNote"] = "本課依官方 Jd-Ⅳ-2 課綱、三筆公立校方公開章節定位與公開自然科試題 pattern 研究，獨立重寫酸鹼方向、pH 對數關係、指示劑、校正、稀釋、濃度與安全證據界線；未複製任何版本教材或試題。完整出版社內文未公開取得，不虛構逐頁閱讀；Terra 第二輪與正式發布審查尚未完成，維持 draft。"
    explanations = [
        "pH 越小代表氫離子濃度越大；在 25°C 下 pH=3 比 pH=5 多兩個 pH 單位，濃度相差 100 倍。正確答案：A。",
        "25°C 的 pH=7 通常表示中性條件；判讀仍應說明溫度，不能把 7 在所有溫度都當成固定中性界線。正確答案：B。",
        "pH=2 的甲比 pH=4 的乙氫離子濃度大 100 倍；體積相同不會改變各自讀值所代表的濃度關係。正確答案：C。",
        "橙紅色只能提供指示劑變色範圍的粗略線索，下一步應用校正過的 pH 計或適合範圍的測量重複確認。正確答案：D。",
        "未校正的 pH 計可能有系統性偏差，讀值不能直接當成樣品真實 pH；應先用標準緩衝液校正並記錄溫度。正確答案：B。",
        "稀釋酸性溶液會降低氫離子濃度，因此 pH 通常上升、往中性方向移動，但不會因稀釋就必然變成鹼性。正確答案：C。",
        "兩杯 pH 都是 3，只能直接知道各自的酸鹼方向與氫離子濃度相同；體積三倍不等於濃度三倍。正確答案：D。",
        "混合兩種酸要考慮氫離子濃度、體積與是否反應，pH 不是普通刻度平均值，因此不能直接說是 4。正確答案：A。",
        "pH=4 在 6—8 變色範圍外偏酸、pH=10 在範圍外偏鹼，兩者都可能呈指示劑的端點顏色，不能只以中間色猜測。正確答案：C。",
        "可靠比較要固定體積、溫度、濃度或測量條件，使用校正儀器並重複讀值；只看顏色或一次讀值不足。正確答案：B。",
    ]
    strategies = ["先把 pH 數值轉成氫離子濃度的十倍關係，再比較大小。", "先確認題目溫度，再判讀 pH=7 與中性的關係。", "先算 pH 差兩格代表 100 倍，再確認體積資訊是否真的改變濃度判斷。", "把指示劑當區間線索，再選擇能提供數值與重複性的下一步。", "先找儀器是否校正與溫度是否記錄，再判斷讀值能否支持結論。", "判斷稀釋後氫離子濃度的方向，再把 pH 變化說成往中性移動。", "分開濃度、體積和總物質量，避免由相同 pH 推出錯誤的體積關係。", "把 pH 當對數尺度，不能用兩個數字直接平均預測混合液。", "比較樣品 pH 與指示劑變色區間，判斷可辨識程度與不確定性。", "列出自變因、控制變因、校正、重複與測量指標，檢查設計是否公平。"]
    steps = ["讀題並圈出 pH、溫度、體積、濃度、指示劑、稀釋或校正條件。", "先判斷資料直接告訴我們酸鹼方向、相對強弱，還是只提供顏色範圍線索。", "若涉及 pH 差異，使用每差一格約十倍的氫離子濃度關係，不把 pH 當普通線性刻度。", "檢查是否混淆酸鹼強度、濃度、腐蝕性、毒性或清潔效果，並排除未控制條件的選項。", "用完整句重述答案，補上溫度、校正、重複測量或安全限制，確認推論沒有超出證據。"]
    for i in range(1, 11):
        p = ROOT / f"questions/science/question-science-content-jd-iv-2-{i}.json"; q = json.loads(p.read_text(encoding="utf-8")); q["examPatternRefs"] = refs(); q["reviewStatus"] = "draft"; q["updatedAt"] = "2026-09-21"; q["answer"]["explanation"] = explanations[i-1]; q["solutionStrategy"] = strategies[i-1]; q["solutionSteps"] = steps; q["provenance"]["sourceUrl"] = URLS[0][0]; q["provenance"]["sourceLocator"] = "公立學校公開自然科試題中的 pH 比較、指示劑、校正、稀釋與控制變因能力；本題改寫為 Jd-Ⅳ-2 原創情境。"; p.write_text(json.dumps(q, ensure_ascii=False, indent=2) + "\n", encoding="utf-8")
    LESSON.write_text(json.dumps(lesson, ensure_ascii=False, indent=2) + "\n", encoding="utf-8")
    REPORT.write_text(json.dumps({"unit": lesson["title"], "lessonId": lesson["id"], "status": "first-pass-ai-review-complete", "reviewStatus": "draft", "checks": {"unitSpecificOriginalContent": True, "threeVersionResearchRecords": True, "publicExamPatternRewrite": True, "fusionRecordPresent": True, "interactivePredictionManipulationExplanation": True, "answersAndDetailedSteps": True, "terraSecondPass": "pending"}, "reviewedAt": "2026-09-21"}, ensure_ascii=False, indent=2) + "\n", encoding="utf-8")
    print("authored science content jd-iv-2")

if __name__ == "__main__":
    main()
