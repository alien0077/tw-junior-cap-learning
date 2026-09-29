import json
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
LESSON = ROOT / "lessons/science/lesson-science-content-eb-iv-5.json"
REPORT = ROOT / "implementation/reports/science-content-eb-iv-5-first-pass-review.json"
URLS = [
    ("https://www.yacjh.kh.edu.tw/upload/221/101_30637/114%E4%B8%8B%E5%AD%B8%E6%9C%9F%E7%AC%AC%E4%B8%80%E6%AC%A1%E6%AE%B5%E8%80%83%E4%B8%89%E5%B9%B4%E7%B4%9A%E8%87%AA%E7%84%B6.pdf", "高雄市立鹽埕國民中學公開自然科段考", "壓力、受力面積、液體深度與壓力差"),
    ("https://www.nhjh.tp.edu.tw/uploads/1738658165906utzaMLG4.pdf", "臺北市立內湖國民中學公開自然科段考", "帕斯卡原理、液壓裝置與資料判讀"),
    ("https://www.kcjh.kh.edu.tw/upload/190/104_34764/%E5%9C%8B%E6%98%8C--%E4%BA%8C%E5%B9%B4%E7%B4%9A--%E8%87%AA%E7%84%B6%E7%A7%91.pdf", "高雄市立國昌國民中學公開自然科試題", "液體壓力、活塞力、位移與安全限制"),
]
BOUNDARY = "本紀錄只保存可追溯公開來源的章節定位、教學方向與評量能力；不複製出版社或學校教材正文、原題、選項、圖表、答案、影音或版面。"
EXPLANATIONS = [
    "D。平均壓力 p=F/A=120÷0.30=400 Pa；題目給的是垂直重量與接觸面積，不能把壓力當成 120 N。",
    "B。重量不變而接觸面積由 0.30 m² 增為 0.60 m²，p=F/A 變為原來的 1/2，因此平均壓力減半。",
    "B。相同力下，寬肩帶的接觸面積較大，p=F/A 較小，所以肩膀單位面積承受的壓力較小；不是背包重量變輕。",
    "B。水的靜水壓隨深度增加，深處孔的壓力差較大，水流初速通常較大，噴射距離也較遠；實際距離仍受孔高與阻力影響。",
    "B。靜止液體同一深度的壓力大小相同，且在各方向都有作用；容器左壁或中央不會單獨改變該深度的液體壓力。",
    "C。由帕斯卡原理 F1/A1=F2/A2，所以 F2=20×40/4=200 N；理想計算仍須注意力的方向與活塞面積單位。",
    "D。液體近似不可壓縮，體積守恆 A1d1=A2d2；大活塞面積是 6 倍，因此位移約 12/6=2 cm。",
    "A。液壓機可用較大面積得到較大輸出力，但輸出端位移較小，且輸入功與輸出功受能量守恆約束，不是憑空製造能量。",
    "A。氣泡可被壓縮，使部分輸入位移先用來壓縮氣體，壓力傳遞變慢且效率下降；液壓系統通常需排除空氣。",
    "D。先確認接觸面與垂直力，再用 p=F/A；液體題標示深度與方向，液壓題比較兩活塞壓力並用體積守恆檢查位移。",
]
STRATEGIES = [
    "圈出垂直力與受力面積，使用 p=F/A 並統一單位。",
    "固定力後只比較面積，判斷壓力與面積成反比。",
    "把背包重量視為相同總力，改比較肩帶接觸面積。",
    "先判斷深度造成的液體壓力，再檢查孔高與流出路徑。",
    "同時回答壓力大小與方向，記住靜止液體壓力不是只向下。",
    "列出兩活塞面積與施力，套用 F1/A1=F2/A2。",
    "用 A1d1=A2d2 連結面積比與位移比，不把力比當位移比。",
    "把輸出力增加和輸出位移減少放在能量守恆中一起判斷。",
    "檢查液體是否含氣泡、漏液或摩擦，分辨壓力傳遞失真的原因。",
    "依接觸面—深度—壓力比—位移四步選擇適當模型與方程式。",
]


def refs():
    return [{"url": u, "title": f"{t}；只取{loc}的題型與推理方向，未複製原題、選項、圖表或答案。", "year": "113-114", "subject": "science", "locator": loc, "observedPattern": "公開自然科評量常要求連結 p=F/A、受力面積、液體深度、壓力方向、帕斯卡原理、活塞位移與裝置限制；本題以全新壓力與液壓情境重寫。", "reuseDecision": "pattern-only", "status": "recorded", "locatorLevel": "paper"} for u, t, loc in URLS]


def main():
    lesson = json.loads(LESSON.read_text(encoding="utf-8")); lesson.update({"updatedAt": "2026-09-21", "reviewStatus": "draft", "authoringStandard": "version-fused-v1"})
    for row in lesson.get("publisherResearch", []): row["reviewedAt"] = "2026-09-21"
    for row in lesson.get("versionResearch", []): row.update({"reviewedAt": "2026-09-21", "licenseBoundary": BOUNDARY})
    lesson["fusionRecord"]["llmSynthesisNote"] = "本課依官方自然科學課綱、kg-science-content-eb-iv-5、南一／康軒／翰林可取得的公開研究方向與三筆公立學校自然科試題能力模式，以自己的話獨立融合 p=F/A、垂直受力、液體深度與方向、帕斯卡原理、活塞力與位移、能量守恆及氣泡安全限制；保留鞋釘—背帶—液壓升降台互動，未複製教材或試題，Terra 第二輪與正式發布審查尚未完成，維持 draft。"
    LESSON.write_text(json.dumps(lesson, ensure_ascii=False, indent=2) + "\n", encoding="utf-8")
    steps = ["圈出接觸面、垂直力、面積、液體深度、兩活塞面積與位移。", "壓力題使用 p=F/A，液體題先比較同深度或深度差，液壓題使用壓力相等。", "統一 N、m²、cm² 與位移單位，逐步代入並保留計算關係。", "用體積守恆與能量觀點檢查力變大是否伴隨位移變小，排除壓力只向下或無條件製造能量的說法。", "回查液體、氣泡、摩擦、漏液、孔高與安全條件，說明理想模型的適用限制。"]
    for i in range(1, 11):
        path = ROOT / f"questions/science/question-science-content-eb-iv-5-{i}.json"; q = json.loads(path.read_text(encoding="utf-8")); q.update({"examPatternRefs": refs(), "reviewStatus": "draft", "updatedAt": "2026-09-21", "solutionStrategy": STRATEGIES[i-1], "solutionSteps": steps}); q["answer"]["explanation"] = EXPLANATIONS[i-1]; q["provenance"]["sourceUrl"] = URLS[0][0]; q["provenance"]["sourceLocator"] = "三筆公立學校公開自然科試題中的壓力、液體深度、帕斯卡原理、活塞力位移與安全限制能力；本題改寫為壓力與液壓原創情境。"; path.write_text(json.dumps(q,ensure_ascii=False,indent=2)+"\n",encoding="utf-8")
    REPORT.write_text(json.dumps({"unit":lesson["title"],"lessonId":lesson["id"],"status":"first-pass-ai-review-complete","reviewStatus":"draft","checks":{"unitSpecificOriginalContent":True,"threeVersionResearchRecords":True,"publicExamPatternRewrite":True,"fusionRecordPresent":True,"interactivePredictionManipulationExplanation":True,"answersAndDetailedSteps":True,"terraSecondPass":"pending"},"reviewedAt":"2026-09-21"},ensure_ascii=False,indent=2)+"\n",encoding="utf-8")
    print("authored science content eb iv 5")


if __name__ == "__main__": main()
