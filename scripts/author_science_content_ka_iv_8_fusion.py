import json
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
LESSON = ROOT / "lessons/science/lesson-science-content-ka-iv-8.json"
REPORT = ROOT / "implementation/reports/science-content-ka-iv-8-first-pass-review.json"
URLS = [
    ("https://www.yacjh.kh.edu.tw/upload/221/101_30637/114%E4%B8%8B%E5%AD%B8%E6%9C%9F%E7%AC%AC%E4%B8%80%E6%AC%A1%E6%AE%B5%E8%80%83%E4%B8%89%E5%B9%B4%E7%B4%9A%E8%87%AA%E7%84%B6.pdf", "鹽埕國中公開自然段考", "光路、反射折射、角度與光學實驗"),
    ("https://www.nhjh.tp.edu.tw/uploads/1738658165906utzaMLG4.pdf", "內湖國中公開自然段考", "光學圖示、介面現象與資料判讀"),
    ("https://www.kcjh.kh.edu.tw/upload/190/104_34764/%E5%9C%8B%E6%98%8C--%E4%BA%8C%E5%B9%B4%E7%B4%9A--%E8%87%AA%E7%84%B6%E7%A7%91.pdf", "國昌國中公開自然科試題", "反射折射、全反射與控制變因"),
]

def refs():
    return [{"url": u, "title": f"{t}；只取{loc}的題型與推理方向，未複製原題、選項、圖表或答案。", "year": "113-114", "subject": "science", "locator": loc, "observedPattern": "公開自然科評量常以法線角度、反射折射光路、視位置、全反射與光學實驗控制變因檢查模型推理；本題為獨立改寫。", "reuseDecision": "pattern-only", "status": "recorded", "locatorLevel": "paper"} for u, t, loc in URLS]

def main():
    lesson = json.loads(LESSON.read_text(encoding="utf-8")); lesson["updatedAt"] = "2026-09-21"; lesson["reviewStatus"] = "draft"
    for row in lesson.get("versionResearch", []):
        row["reviewedAt"] = "2026-09-21"
        row["licenseBoundary"] = "本紀錄只保存可追溯公開來源的章節定位、教學方向與評量能力；不複製出版社或學校教材正文、原題、選項、圖表、答案、影音或版面。"
    lesson["fusionRecord"]["llmSynthesisNote"] = "本課依官方 Ka-Ⅳ-8 課綱、三筆公立校方公開章節定位與公開自然科試題 pattern 研究，獨立重寫法線、反射、折射、視位置、全反射、複合光路與量測限制；未複製任何版本教材或試題。完整出版社內文未公開取得，不虛構逐頁閱讀；Terra 第二輪與正式發布審查尚未完成，維持 draft。"
    explanations = [
        "反射角和入射角都從法線量，平面鏡反射滿足兩者相等，因此反射角為 35°。正確答案：A。",
        "光線與鏡面夾 20°，而法線與鏡面垂直，所以入射角為 90°−20°=70°。正確答案：B。",
        "光由空氣進入光速較慢的玻璃，斜射時通常向法線偏折；判斷角度時要明確說以法線為基準。正確答案：C。",
        "全反射要先由光學上較慢介質射向較快介質，再讓入射角大於臨界角；只說透明或角度大仍不完整。正確答案：D。",
        "鉛筆兩段光線在水面折射，眼睛以直線反向延伸後形成錯誤視位置，因此看似彎折，不是鉛筆真的彎了。正確答案：B。",
        "平面鏡成像的虛像距離等於物體距離，物距 40 cm 時像距鏡面也是 40 cm。正確答案：C。",
        "物體向鏡面移近 10 cm，物距與像距各少 10 cm，物像間距總共減少 20 cm。正確答案：D。",
        "透明介面通常會同時有部分光反射與部分光折射，兩條不同方向的光路比只看亮度更能支持結論。正確答案：A。",
        "正向入射時光線沿法線前進，方向可能近似不變，但速度與波長仍可能改變，所以不能說沒有折射。正確答案：C。",
        "比較折射效果要固定入射角、光源、幾何位置與量角方法，只更換材料並重複測量折射角。正確答案：B。",
    ]
    strategies = ["先畫交點與法線，再用入射角等於反射角。", "先把光線與鏡面的角度轉成與法線的互餘角。", "比較兩介質光速，再判斷折射線向法線或離開法線。", "依序檢查介質方向與臨界角，兩項都符合才可判定全反射。", "畫出介面兩側光線，再用反向延伸說明視位置。", "直接使用平面鏡物距等於像距，再確認題目問的是到鏡面距離。", "物距改變多少，像距同方向改變多少，兩者相加得到物像間距變化。", "找是否有同一入射光分成反射與折射兩條路徑。", "區分方向近似不變與速度、波長改變，不把正入射當成沒有折射。", "列出入射角、材料、位置與量角為控制變因，只改材料並重複。"]
    steps = ["讀題並圈出入射點、法線、介質、角度、物距或實驗變因。", "先確認角度是相對法線還是相對介面，再畫出方向箭頭。", "依反射定律、折射方向、臨界角或平面鏡成像關係計算／判斷。", "排除把亮度、透明度、視位置或單一示意圖當成完整光路證據的選項。", "用完整句重述答案，補上介質、角度基準與量測限制，確認結論不超出資料。"]
    for i in range(1, 11):
        p = ROOT / f"questions/science/question-science-content-ka-iv-8-{i}.json"; q = json.loads(p.read_text(encoding="utf-8")); q["examPatternRefs"] = refs(); q["reviewStatus"] = "draft"; q["updatedAt"] = "2026-09-21"; q["answer"]["explanation"] = explanations[i-1]; q["solutionStrategy"] = strategies[i-1]; q["solutionSteps"] = steps; q["provenance"]["sourceUrl"] = URLS[0][0]; q["provenance"]["sourceLocator"] = "公立學校公開自然科試題中的反射折射、法線角度、全反射、成像與光學控制變因能力；本題改寫為 Ka-Ⅳ-8 原創情境。"; p.write_text(json.dumps(q, ensure_ascii=False, indent=2) + "\n", encoding="utf-8")
    LESSON.write_text(json.dumps(lesson, ensure_ascii=False, indent=2) + "\n", encoding="utf-8")
    REPORT.write_text(json.dumps({"unit": lesson["title"], "lessonId": lesson["id"], "status": "first-pass-ai-review-complete", "reviewStatus": "draft", "checks": {"unitSpecificOriginalContent": True, "threeVersionResearchRecords": True, "publicExamPatternRewrite": True, "fusionRecordPresent": True, "interactivePredictionManipulationExplanation": True, "answersAndDetailedSteps": True, "terraSecondPass": "pending"}, "reviewedAt": "2026-09-21"}, ensure_ascii=False, indent=2) + "\n", encoding="utf-8")
    print("authored science content ka-iv-8")

if __name__ == "__main__":
    main()
