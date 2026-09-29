#!/usr/bin/env python3
"""Record public-school evidence for Civ Ba-IV-2, Ba-IV-3 and Ba-IV-4."""
import json
import re
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
REPORT = ROOT / "implementation/reports/publisher-chapter-evidence-samples.json"
URLS = {
    "nani": "https://course.cyc.edu.tw/upfile/course109/sub1/14535426760482702.pdf",
    "kanghsuan": "https://www.csjh.kh.edu.tw/fxmteach/113/113%E7%89%B9%E6%AE%8A%E6%95%99%E8%82%B2%E8%AA%B2%E7%A8%8B%E8%A8%88%E7%95%AB/113%E7%89%B9%E6%95%99%E7%8F%AD/113-2%E7%89%B9%E6%95%99%E6%B7%B7%E9%BD%A1%E4%B8%80%E7%8F%AD%E8%AA%B2%E7%A8%8B%E9%80%B2%E5%BA%A6%E8%A8%88%E7%95%AB%E8%A1%A8.pdf",
    "hanlin": "https://data.yjm.kh.edu.tw/curriculum113/01.%E4%B8%80%E7%94%B2%E5%9C%8B%E4%B8%AD%E6%99%AE%E9%80%9A%E7%8F%AD113%E8%AA%B2%E7%A8%8B%E8%A8%88%E7%95%AB/5.%E9%A0%98%E5%9F%9F%E5%AD%B8%E7%BF%92%E8%AA%B2%E7%A8%8B%E8%A8%88%E7%95%AB/5-1.%E5%90%84%E9%A0%98%E5%9F%9F%E8%AA%B2%E7%A8%8B%E8%A8%88%E7%95%AB/05%E7%A4%BE%E6%9C%83/%E4%B8%83%E5%B9%B4%E7%B4%9A%E8%AA%B2%E7%A8%8B%E8%A8%88%E7%95%AB/113%E4%B8%80%E4%B8%8A%E7%A4%BE%E6%9C%83%E5%88%86%E7%A7%91%E4%B8%89%E6%AC%A1%E6%AE%B5%E8%80%83%28%E5%85%AC%E6%B0%91%29.pdf",
}
LICENSE = "只記錄公立學校課程計畫的版本、章節重點與評量方向，不複製教材、圖表、題目或答案。"
SAMPLES = [
    {
        "lessonId": "lesson-social-content-civ-ba-iv-2",
        "title": "公 Ba-Ⅳ-2：原住民族部落的意義與重要性",
        "core": ["部落不只是居住地，也可能承載信仰、文化傳承、政治協作、生產分配與集體認同", "分析部落重要性要同時看歷史、土地、制度與族群自主性，避免把不同族群經驗簡化成單一模式", "以地圖、口述／文本資料、制度脈絡與當代議題理解部落的處境與訴求"],
        "diff": ["南一把部落放在社區與部落單元，連結信仰、文化、政治、生產與政府回應", "康軒以史前文化、族群遷徙、社區參與和部落永續發展建立文化脈絡", "翰林以原住民族文化、社會互動與多元觀點支持理解與討論"],
        "obs": [["nani", "南一版課程計畫；公 Ba-Ⅳ-2 與社區、部落、文化傳承、政治及生產分配並列", "部落功能矩陣；歷史／當代時間線；政府回應資料", "口頭問答、課堂觀察、參與討論、紙筆測驗"], ["kanghsuan", "康軒版課程計畫；公 Ba-Ⅳ-2、原住民族遷徙、社區與部落永續發展", "遷徙地圖；部落重要性案例卡；永續行動表", "紙筆、口語、指認、課堂參與"], ["hanlin", "翰林版課程計畫；家庭／社群與多元文化脈絡中的原住民族議題", "文化證據表；群體觀點比較；資料解釋短講", "課堂發言、圖表／文字解釋、討論與學習紀錄"]],
    },
    {
        "lessonId": "lesson-social-content-civ-ba-iv-3",
        "title": "公 Ba-Ⅳ-3：親屬關係與親子權利義務",
        "core": ["親屬關係可能由血親、婚姻或法律程序形成，親子關係同時包含身分、照顧、扶養與保護責任", "判讀權利義務要區分家庭倫理期待與法律規範，並留意未成年人與不同家庭處境", "以案例、法規摘要與角色觀點說明權利義務如何形成、衝突與尋求協助"],
        "diff": ["南一將親屬關係與家庭型態、家庭職能及社會變遷連續安排", "康軒以親屬法律形成與親子權利義務搭配生活案例和口語理解", "翰林以家庭生活單元、生活經驗與制度脈絡引導學生解釋"],
        "obs": [["nani", "南一版課程計畫；公 Ba-Ⅳ-3 與家庭型態、家庭職能及社會變遷並列", "親屬關係圖；權利／義務對照表；家庭案例時間線", "口頭問答、課堂觀察、參與討論、紙筆測驗"], ["kanghsuan", "康軒版課程計畫；公 Ba-Ⅳ-3 明列親屬法律形成與親子權利義務", "法律關係流程；案例角色卡；權利義務配對", "紙筆、口語、課堂參與與指認評量"], ["hanlin", "翰林版課程計畫；家庭生活、生活經驗、社會變遷與公民概念學習", "家庭關係與制度表；衝突情境對話；協助資源地圖", "課堂發言、案例解釋、討論與紙筆評量"]],
    },
    {
        "lessonId": "lesson-social-content-civ-ba-iv-4",
        "title": "公 Ba-Ⅳ-4：家庭型態與職能變遷",
        "core": ["家庭型態會因人口、婚姻、遷移、經濟與社會價值改變而多樣化，不能以單一樣貌定義正常家庭", "家庭職能包括照顧、情感、經濟與社會化，可能由家庭、社區、學校或公共制度共同承擔", "以統計圖表、生活案例與政策資料分析變遷，並區分描述、原因與價值判斷"],
        "diff": ["南一將家庭型態與家庭職能放在社會轉變脈絡中，強調認識功能改變", "康軒以家庭型態、親屬與社會規範並置，透過生活情境理解差異", "翰林以家庭生活、社會變遷及圖表／發言活動引導多元觀察"],
        "obs": [["nani", "南一版課程計畫；公 Ba-Ⅳ-4 與家庭型態、社會轉變及家庭功能改變並列", "家庭型態統計圖；職能變化時間線；制度支持比較", "口頭問答、課堂觀察、參與討論、紙筆測驗"], ["kanghsuan", "康軒版課程計畫；公 Ba-Ⅳ-4 與社會規範、家庭與原住民族議題並列", "家庭案例卡；功能分工圖；不同型態比較表", "紙筆、口語、指認與課堂參與"], ["hanlin", "翰林版課程計畫；家庭生活單元、社會變遷、文字／圖表表達與課堂發言", "人口／家庭圖表；家庭功能分擔表；多方觀點短講", "課堂發言、圖表解釋、參與討論與學習紀錄"]],
    },
]


def main():
    data = json.loads(REPORT.read_text(encoding="utf-8"))
    existing = {item["lessonId"] for item in data["units"]}
    added = []
    for sample in SAMPLES:
        sources = [{"publisher": p, "sourceUrl": URLS[p], "sourceKind": "public-school-course-plan-identifying-publisher-material", "locator": f"{concept}；核讀 2026-09-21。", "accessedAt": "2026-09-21", "observedConcepts": concept.split("；"), "observedRepresentations": representation.split("；"), "observedAssessment": assessment.split("、"), "licenseBoundary": LICENSE} for p, concept, representation, assessment in sample["obs"]]
        record = {"lessonId": sample["lessonId"], "title": sample["title"], "evidenceStatus": "chapter-level-recorded-pending-fusion-review", "sources": sources, "fusionReview": {"commonCore": sample["core"], "differencesToReview": sample["diff"], "originalSynthesisBoundary": "逐單元融合、內容／版權審查與 Terra 複核前維持 draft，不升級 publisher status。"}}
        if record["lessonId"] not in existing:
            data["units"].append(record)
            added.append(record["lessonId"])
    data["unitCount"] = len(data["units"])
    data["updatedAt"] = "2026-09-21"
    REPORT.write_text(json.dumps(data, ensure_ascii=False, indent=2) + "\n", encoding="utf-8")
    blockers_path = ROOT / "implementation/reports/blockers.json"
    blockers = json.loads(blockers_path.read_text(encoding="utf-8"))
    for blocker in blockers.get("blockers", []):
        reason = blocker.get("reason")
        if isinstance(reason, str) and "unit samples" in reason:
            blocker["reason"] = re.sub(r"Four hundred (?:forty-four|forty-seven|fifty|fifty-three|fifty-six|fifty-nine|sixty-two|sixty-five|sixty-eight|seventy-one|seventy-four|seventy-seven|seventy-nine|eighty) unit samples", "Four hundred eighty-three unit samples", reason)
    blockers_path.write_text(json.dumps(blockers, ensure_ascii=False, indent=2) + "\n", encoding="utf-8")
    print(json.dumps({"unitCount": data["unitCount"], "added": added}, ensure_ascii=False))


if __name__ == "__main__":
    main()
