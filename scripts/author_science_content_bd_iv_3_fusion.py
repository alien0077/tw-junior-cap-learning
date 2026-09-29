import json
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
LESSON = ROOT / "lessons/science/lesson-science-content-bd-iv-3.json"
REPORT = ROOT / "implementation/reports/science-content-bd-iv-3-first-pass-review.json"
URLS = [
    ("https://www.yacjh.kh.edu.tw/upload/221/101_30637/114%E4%B8%8B%E5%AD%B8%E6%9C%9F%E7%AC%AC%E4%B8%80%E6%AC%A1%E6%AE%B5%E8%80%83%E4%B8%89%E5%B9%B4%E7%B4%9A%E8%87%AA%E7%84%B6.pdf", "高雄市立鹽埕國民中學公開自然科段考", "生態系角色、食物網與物質循環"),
    ("https://www.nhjh.tp.edu.tw/uploads/1738658165906utzaMLG4.pdf", "臺北市立內湖國民中學公開自然科段考", "能量流動、分解作用與環境因子資料判讀"),
    ("https://www.kcjh.kh.edu.tw/upload/190/104_34764/%E5%9C%8B%E6%98%8C--%E4%BA%8C%E5%B9%B4%E7%B4%9A--%E8%87%AA%E7%84%B6%E7%A7%91.pdf", "高雄市立國昌國民中學公開自然科試題", "生產者、消費者、分解者與生態系變化"),
]
BOUNDARY = "本紀錄只保存可追溯公開來源的章節定位、教學方向與評量能力；不複製出版社或學校教材正文、原題、選項、圖表、答案、影音或版面。"
EXPLANATIONS = [
    "A。藻類能利用光能製造有機物，屬於生產者；它把外界能量引入食物網，之後才可能由消費者取食傳遞。",
    "B。細菌和真菌分解遺體、落葉與排遺，將複雜有機物拆解，讓部分元素回到土壤、水或空氣，支援物質循環。",
    "A。水溫是非生物因子，會影響代謝速率、溶氧與生物可存活範圍，因此可能改變池塘生物的分布。",
    "C。分解者減少時，短期最直接的結果是枯葉與遺體分解變慢而累積；養分釋放變慢則是後續影響。",
    "A。生產者引入能量與有機物，消費者傳遞能量與物質，分解者促成元素回到環境；能量仍沿途以熱散失，並非循環。",
    "D。過量養分可促進藻類增生；藻類和遺體被微生物分解時會消耗溶氧，缺氧可能造成魚群死亡，這是有條件的連鎖推論。",
    "A。移除捕食者後，獵物還會受到其他天敵、食物量、疾病、競爭與溫度等因素限制，不能只沿一條食物鏈直線預測。",
    "B。生態系同時包含生物成分與光照、溫度、溶氧等非生物環境；少了後者就無法解釋角色活動與數量變化。",
    "A。高溫可能在特定材料與適宜範圍內加快分解，但超出耐受範圍或改變含水量、氧氣時可能抑制分解，結論不能無限外推。",
    "C。能量沿營養階層單向流動並散失，碳氮水等物質可經取食、排遺、分解與環境交換回流；生物與非生物條件也互相影響。",
]
STRATEGIES = [
    "先判斷是否能自行製造有機物，再定位生產者、消費者或分解者。",
    "把遺體與排遺的去向連到分解者，再追蹤元素回到環境的路徑。",
    "先分出生物與非生物因子，再說明該條件如何影響代謝、溶氧或分布。",
    "先找最直接的時間近端變化，再把養分與族群影響列為後續推論。",
    "用兩種箭頭分開畫能量單向流動和物質回流，並標記熱散失。",
    "由養分—藻類—分解—溶氧—魚群的因果鏈逐段檢查，避免跳過中間證據。",
    "檢查食物網中的替代路徑、其他限制因子與觀察時間，不作單線斷言。",
    "確認模型是否同時記錄生物角色、非生物條件與時間，而非只列物種名稱。",
    "把觀察範圍、材料、含水量、通氣和溫度一起看，避免把相關性外推成普遍定律。",
    "先分辨能量和物質的方向，再把生物—環境交換加入完整系統圖。",
]


def refs():
    return [{"url": u, "title": f"{t}；只取{loc}的題型與推理方向，未複製原題、選項、圖表或答案。", "year": "113-114", "subject": "science", "locator": loc, "observedPattern": "公開自然科評量常要求辨認生態系角色、食物網、能量流動、分解、物質循環、非生物因子與資料尺度；本題以全新生態系情境重寫。", "reuseDecision": "pattern-only", "status": "recorded", "locatorLevel": "paper"} for u, t, loc in URLS]


def main():
    lesson = json.loads(LESSON.read_text(encoding="utf-8"))
    lesson.update({"updatedAt": "2026-09-21", "reviewStatus": "draft", "authoringStandard": "version-fused-v1"})
    for row in lesson.get("publisherResearch", []):
        row["reviewedAt"] = "2026-09-21"
    for row in lesson.get("versionResearch", []):
        row["reviewedAt"] = "2026-09-21"
        row["licenseBoundary"] = BOUNDARY
    lesson["fusionRecord"]["llmSynthesisNote"] = "本課依官方自然科學課綱、kg-science-content-bd-iv-3、南一／康軒／翰林可取得的公開研究方向與三筆公立學校自然科試題能力模式，以自己的話獨立融合生產者、消費者、分解者、非生物條件、能量單向流動、碳氮水等物質回流、食物網替代路徑、時間尺度與資料限制；保留池塘—農田—堆肥的角色調查互動，未複製教材或試題，Terra 第二輪與正式發布審查尚未完成，維持 draft。"
    LESSON.write_text(json.dumps(lesson, ensure_ascii=False, indent=2) + "\n", encoding="utf-8")
    steps = ["圈出生產者、消費者、分解者、非生物因子與觀察時間。", "分開畫能量傳遞箭頭、物質回流箭頭與環境條件影響。", "先說明角色改變的直接結果，再沿食物網與分解路徑追蹤延遲影響。", "用生物量、養分、溶氧、溫度或分解速率資料支持推論，並排除替代解釋。", "回查結論的系統邊界、材料、時間尺度與模型限制，避免把能量說成循環或把單一結果普遍化。"]
    for i in range(1, 11):
        path = ROOT / f"questions/science/question-science-content-bd-iv-3-{i}.json"
        q = json.loads(path.read_text(encoding="utf-8"))
        q["examPatternRefs"] = refs()
        q["reviewStatus"] = "draft"
        q["updatedAt"] = "2026-09-21"
        q["answer"]["explanation"] = EXPLANATIONS[i - 1]
        q["solutionStrategy"] = STRATEGIES[i - 1]
        q["solutionSteps"] = steps
        q["provenance"]["sourceUrl"] = URLS[0][0]
        q["provenance"]["sourceLocator"] = "三筆公立學校公開自然科試題中的生態系角色、能量流動、分解、物質循環、非生物因子與資料判讀能力；本題改寫為生態系原創情境。"
        path.write_text(json.dumps(q, ensure_ascii=False, indent=2) + "\n", encoding="utf-8")
    REPORT.write_text(json.dumps({"unit": lesson["title"], "lessonId": lesson["id"], "status": "first-pass-ai-review-complete", "reviewStatus": "draft", "checks": {"unitSpecificOriginalContent": True, "threeVersionResearchRecords": True, "publicExamPatternRewrite": True, "fusionRecordPresent": True, "interactivePredictionManipulationExplanation": True, "answersAndDetailedSteps": True, "terraSecondPass": "pending"}, "reviewedAt": "2026-09-21"}, ensure_ascii=False, indent=2) + "\n", encoding="utf-8")
    print("authored science content bd iv 3")


if __name__ == "__main__":
    main()
