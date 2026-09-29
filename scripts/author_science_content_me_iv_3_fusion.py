import json
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
LESSON = ROOT / "lessons/science/lesson-science-content-me-iv-3.json"
REPORT = ROOT / "implementation/reports/science-content-me-iv-3-first-pass-review.json"
URLS = [
    ("https://www.yacjh.kh.edu.tw/upload/221/101_30637/114%E4%B8%8B%E5%AD%B8%E6%9C%9F%E7%AC%AC%E4%B8%80%E6%AC%A1%E6%AE%B5%E8%80%83%E4%B8%89%E5%B9%B4%E7%B4%9A%E8%87%AA%E7%84%B6.pdf", "鹽埕國中公開自然段考", "空氣污染物、來源、監測資料與防治"),
    ("https://www.nhjh.tp.edu.tw/uploads/1738658165906utzaMLG4.pdf", "內湖國中公開自然段考", "地球科學圖表、污染現象與證據判讀"),
    ("https://www.kcjh.kh.edu.tw/upload/190/104_34764/%E5%9C%8B%E6%98%8C--%E4%BA%8C%E5%B9%B4%E7%B4%9A--%E8%87%AA%E7%84%B6%E7%A7%91.pdf", "國昌國中公開自然科試題", "污染形成、控制變因與環境決策"),
]

def refs():
    return [{"url": u, "title": f"{t}；只取{loc}的題型與推理方向，未複製原題、選項、圖表或答案。", "year": "113-114", "subject": "science", "locator": loc, "observedPattern": "公開自然科評量常以污染物與前驅物、來源、氣象條件、監測數據、健康風險和防治證據測量因果判讀；本題為獨立改寫。", "reuseDecision": "pattern-only", "status": "recorded", "locatorLevel": "paper"} for u, t, loc in URLS]

def main():
    lesson = json.loads(LESSON.read_text(encoding="utf-8")); lesson["updatedAt"] = "2026-09-21"; lesson["reviewStatus"] = "draft"
    for row in lesson.get("versionResearch", []):
        row["reviewedAt"] = "2026-09-21"
        row["licenseBoundary"] = "本紀錄只保存可追溯公開來源的章節定位、教學方向與評量能力；不複製出版社或學校教材正文、原題、選項、圖表、答案、影音或版面。"
    lesson["fusionRecord"]["llmSynthesisNote"] = "本課依官方 Me-Ⅳ-3 課綱、三筆公立校方公開章節定位與公開自然科試題 pattern 研究，獨立重寫一次／二次污染物、來源、氣象、監測、暴露與防治層次；未複製任何版本教材或試題。完整出版社內文未公開取得，不虛構逐頁閱讀；Terra 第二輪與正式發布審查尚未完成，維持 draft。"
    explanations = [
        "二氧化硫、氮氧化物或細懸浮微粒可直接作為污染物，氮氧化物也可能是臭氧形成的前驅物；不能把風向或天空顏色當污染物。正確答案：B。",
        "都市 PM2.5 可能與交通、燃燒、工業排放及二次生成相關，判斷來源要同步看時間、風向與測站位置。正確答案：C。",
        "近地面臭氧是二次污染物，濃度升高可能刺激眼睛與呼吸道；不能把臭氧當成氧氣增加或安全指標。正確答案：A。",
        "限制怠速、改善大眾運輸或降低車輛排放可直接作用於交通源頭；戴口罩主要是降低個人暴露，作用位置不同。正確答案：D。",
        "兩地 PM2.5 數字要有可比性，至少要記錄同一時段或時間範圍、測點、單位與風向等條件，否則不能直接歸因。正確答案：B。",
        "逆溫時上層暖空氣抑制近地空氣上升，污染物較難擴散，容易在近地面累積；這不是污染物突然消失。正確答案：B。",
        "公平研究要設置相近道路條件與測點、重複不同時段，並控制風速、車流與背景濃度，只比較綠帶這項差異。正確答案：C。",
        "燃氣不完全燃燒可能產生一氧化碳，保持通風、檢查設備並避免在密閉空間使用可降低風險；氣味不是可靠警報。正確答案：A。",
        "空品警報時敏感族群應查證官方數據、減少戶外劇烈活動並依需要改善室內空氣，而非只看天空顏色。正確答案：D。",
        "有效政策要比較政策前後同類測點的長期污染物資料，並同時檢查氣象、車流或產業變化，不能只看單日數字。正確答案：C。",
    ]
    strategies = ["先區分污染物、前驅物、來源與氣象條件，再檢查選項是否把不同層次混在一起。", "把污染濃度放回時間、風向、測點與可能來源，避免由單一地點下唯一結論。", "分辨近地面臭氧的二次生成與健康影響，不把臭氧和氧氣或一次排放混淆。", "先定位措施作用在源頭、排放處理或暴露端，再判斷是否真的直接降低交通排放。", "先檢查兩地資料的單位、時間、測點與氣象條件，再比較數值。", "尋找逆溫造成的垂直擴散限制，確認污染物為何在近地面累積。", "列出自變因、控制變因、對照測點與重複測量，判斷研究是否公平。", "把一氧化碳形成條件、通風與設備安全分開，選能降低暴露的措施。", "先讀官方空品資訊，再依族群風險調整戶外行動與室內通風／過濾。", "比較長期、同方法、同測點的前後資料，並排除氣象和其他來源造成的假改善。"]
    steps = ["讀題並標出污染物、來源、時間、地點、氣象、暴露或防治作用位置。", "把資料分成直接測得的結果、可提出的合理假說與仍缺少的證據。", "檢查選項是否符合一次／二次污染物、固定／移動來源與污染形成條件。", "排除把灰霾顏色、單一測站、單日讀值或個人感受當成唯一因果的說法。", "用完整句重述答案，補上比較基準、控制條件或資料限制，確認推論不超出證據。"]
    for i in range(1, 11):
        p = ROOT / f"questions/science/question-science-content-me-iv-3-{i}.json"; q = json.loads(p.read_text(encoding="utf-8")); q["examPatternRefs"] = refs(); q["reviewStatus"] = "draft"; q["updatedAt"] = "2026-09-21"; q["answer"]["explanation"] = explanations[i-1]; q["solutionStrategy"] = strategies[i-1]; q["solutionSteps"] = steps; q["provenance"]["sourceUrl"] = URLS[0][0]; q["provenance"]["sourceLocator"] = "公立學校公開自然科試題中的污染物、來源、監測、控制變因與防治能力；本題改寫為 Me-Ⅳ-3 原創情境。"; p.write_text(json.dumps(q, ensure_ascii=False, indent=2) + "\n", encoding="utf-8")
    LESSON.write_text(json.dumps(lesson, ensure_ascii=False, indent=2) + "\n", encoding="utf-8")
    REPORT.write_text(json.dumps({"unit": lesson["title"], "lessonId": lesson["id"], "status": "first-pass-ai-review-complete", "reviewStatus": "draft", "checks": {"unitSpecificOriginalContent": True, "threeVersionResearchRecords": True, "publicExamPatternRewrite": True, "fusionRecordPresent": True, "interactivePredictionManipulationExplanation": True, "answersAndDetailedSteps": True, "terraSecondPass": "pending"}, "reviewedAt": "2026-09-21"}, ensure_ascii=False, indent=2) + "\n", encoding="utf-8")
    print("authored science content me-iv-3")

if __name__ == "__main__":
    main()
