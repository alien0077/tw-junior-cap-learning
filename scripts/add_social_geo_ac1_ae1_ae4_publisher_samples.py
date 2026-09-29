#!/usr/bin/env python3
"""Record public-school publisher evidence for social geography Ac-IV-1 and Ae-IV-1..4."""
import json
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
REPORT = ROOT / "implementation/reports/publisher-chapter-evidence-samples.json"
BLOCKERS = ROOT / "implementation/reports/blockers.json"
SOURCES = [
    ("nani", "https://course.cyc.edu.tw/upfile/course114/sub1/15950803923674214.pdf", "嘉義縣永慶高中公立課程計畫；南一版地理課程列天氣氣候、農業經營、工業發展、國際貿易與產業調適相關學習內容。"),
    ("kanghsuan", "https://course.cyc.edu.tw/upfile/course114/sub1/15939547496629384.pdf", "嘉義縣立布袋國民中學公立課程計畫；康軒版地理課程列天氣與氣候、臺灣農工業、國際貿易及產業挑戰探究。"),
    ("hanlin", "https://www.msjh.ntpc.edu.tw/uploads/1691978949408RP7cOuyZ.pdf", "臺北市立民生國民中學公立課程計畫；翰林版地理課程列地 Ac-IV-1、Ae-IV-1～4，採地圖資料、問題討論、紙筆與問答評量。"),
]
UNITS = [
    ("ac-iv-1", "地 Ac-Ⅳ-1：天氣與氣候", ["天氣", "氣候", "大氣要素", "時間尺度"], "用氣溫、降水、風向與氣壓的日變化和多年平均圖，區分天氣觀測與氣候型態。", "要求依時間尺度、資料期間與大氣要素作答，避免把單日高溫當成氣候變遷結論。"),
    ("ae-iv-1", "地 Ae-Ⅳ-1：農業經營", ["農業區位", "自然條件", "市場", "技術與農業型態"], "用農業區位資料比較地形、氣候、灌溉、勞力與市場如何共同影響農業經營。", "要求以多項資料解釋農業型態，不能只用氣候單一因素判斷。"),
    ("ae-iv-2", "地 Ae-Ⅳ-2：工業發展", ["工業區位", "生產要素", "產業鏈", "工業變遷"], "用工廠分布與投入產出流程，追蹤原料、能源、勞力、交通與市場對工業區位和轉型的影響。", "學生需區分工業類型、區位因素與時代變化，避免把工業發展等同工廠數量增加。"),
    ("ae-iv-3", "地 Ae-Ⅳ-3：臺灣的國際貿易與全球關連", ["進出口", "國際分工", "產業鏈", "全球關連"], "用臺灣進出口商品、貿易夥伴與產業鏈圖，說明國際分工如何連結臺灣生產、消費與就業。", "要求從流向與比例資料判讀全球關連，不能只列國家名稱或把貿易量當成單向受益。"),
    ("ae-iv-4", "地 Ae-Ⅳ-4：產業挑戰與調適探究", ["產業挑戰", "環境與勞動", "資料探究", "調適方案"], "以臺灣產業案例建立問題—資料—利害關係—方案—評估的探究流程，連結產業競爭與永續調適。", "學生需提出有證據的方案並說明代價與限制，不能只寫口號式的『轉型升級』。"),
]

def main():
    data = json.loads(REPORT.read_text(encoding="utf-8"))
    units = {x["lessonId"]: x for x in data["units"]}
    for suffix, title, core, representation, assessment in UNITS:
        lesson_id = "lesson-social-content-geo-" + suffix
        units[lesson_id] = {
            "lessonId": lesson_id, "title": title,
            "evidenceStatus": "chapter-level-recorded-pending-fusion-review",
            "sources": [{
                "publisher": publisher, "sourceUrl": url,
                "sourceKind": "public-school-course-plan-identifying-publisher-material",
                "locator": locator, "accessedAt": "2026-09-21",
                "observedConcepts": [title, *core],
                "observedRepresentations": [representation],
                "observedAssessment": [assessment],
                "licenseBoundary": "僅記錄公立學校課程計畫的出版商、單元定位與評量方向；不複製教科書正文、圖表、題目或答案。",
            } for publisher, url, locator in SOURCES],
            "fusionReview": {
                "commonCore": core,
                "differencesToReview": [representation, assessment],
                "originalSynthesisBoundary": "三版本融合、內容／版權審查與 Terra 複核完成前維持 draft，不升級 publisher status。",
            },
        }
    data["units"] = sorted(units.values(), key=lambda x: x["lessonId"])
    data["unitCount"] = len(data["units"])
    data["updatedAt"] = "2026-09-21"
    REPORT.write_text(json.dumps(data, ensure_ascii=False, indent=2) + "\n", encoding="utf-8")
    blockers = json.loads(BLOCKERS.read_text(encoding="utf-8"))
    for b in blockers.get("blockers", []):
        if isinstance(b.get("reason"), str):
            b["reason"] = b["reason"].replace("Five hundred thirty-seven unit samples", "Five hundred forty-two unit samples")
    BLOCKERS.write_text(json.dumps(blockers, ensure_ascii=False, indent=2) + "\n", encoding="utf-8")
    print(json.dumps({"unitCount": data["unitCount"], "added": len(UNITS)}, ensure_ascii=False))

if __name__ == "__main__":
    main()
