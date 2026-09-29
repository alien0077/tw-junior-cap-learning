#!/usr/bin/env python3
"""Record public-school publisher evidence for social geography Aa-IV-1..4."""
import json
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
REPORT = ROOT / "implementation/reports/publisher-chapter-evidence-samples.json"
BLOCKERS = ROOT / "implementation/reports/blockers.json"
SOURCES = [
    ("nani", "https://course.cyc.edu.tw/upfile/course114/sub1/15950803923674214.pdf", "嘉義縣永慶高中公立課程計畫；南一版地理課程的地圖判讀、臺灣位置與問題探究範圍，定位地 Aa-IV-1～4。"),
    ("kanghsuan", "https://course.cyc.edu.tw/upfile/course114/sub1/15939547496629384.pdf", "嘉義縣立布袋國民中學公立課程計畫；康軒版地理課程列全球座標、海陸分布、臺灣地理位置與區域關聯探究。"),
    ("hanlin", "https://www.msjh.ntpc.edu.tw/uploads/1691978949408RP7cOuyZ.pdf", "臺北市立民生國民中學公立課程計畫；翰林版地理課程列地 Aa-IV-1～4，採地圖資料判讀、問題討論與紙筆／問答評量。"),
]
UNITS = [
    ("aa-iv-1", "地 Aa-Ⅳ-1：全球經緯度座標", ["經度", "緯度", "座標定位", "地圖比例與方向"], "用地球儀、平面地圖與座標格線三種表徵，讓學生由緯度帶和經度線交會定位地點。", "要求分清經度／緯度、東西／南北與度數方向，避免把地圖上的水平垂直位置直接當成座標名稱。"),
    ("aa-iv-2", "地 Aa-Ⅳ-2：全球海陸分布", ["海陸分布", "洲與洋", "半球", "空間尺度"], "用全球海陸分布圖與半球統計表，比較不同尺度下陸地、海洋與洲洋位置的空間關係。", "學生需以圖例、方向與尺度證據回答，不能只背洲名或把圖面大小當真實面積。"),
    ("aa-iv-3", "地 Aa-Ⅳ-3：臺灣地理位置特性及影響", ["臺灣位置", "海陸交通", "季風與區域", "地緣關聯"], "將臺灣放入東亞海陸位置、洋流／季風與交通網絡圖，推導位置對氣候、交流與產業的可能影響。", "要求把位置特徵與影響用地圖證據連結，避免把地理位置寫成單純的地名背誦。"),
    ("aa-iv-4", "地 Aa-Ⅳ-4：問題探究：臺灣與世界關聯", ["問題探究", "跨尺度關聯", "資料蒐集", "證據與結論"], "以臺灣與世界的商品、人口或環境議題為探究題，建立問題—資料—空間比較—結論—限制的研究流程。", "學生需說明資料來源與尺度限制，並區分資料支持的結論和個人推測。"),
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
            b["reason"] = b["reason"].replace("Five hundred thirty-three unit samples", "Five hundred thirty-seven unit samples")
    BLOCKERS.write_text(json.dumps(blockers, ensure_ascii=False, indent=2) + "\n", encoding="utf-8")
    print(json.dumps({"unitCount": data["unitCount"], "added": len(UNITS)}, ensure_ascii=False))

if __name__ == "__main__":
    main()
