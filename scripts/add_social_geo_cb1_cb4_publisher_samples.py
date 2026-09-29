#!/usr/bin/env python3
"""Record public-school publisher evidence for social geography Cb-IV-1..4."""
import json
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
REPORT = ROOT / "implementation/reports/publisher-chapter-evidence-samples.json"
BLOCKERS = ROOT / "implementation/reports/blockers.json"
SOURCES = [
    ("nani", "https://course.cyc.edu.tw/upfile/course114/sub1/15950803923674214.pdf", "嘉義縣永慶高中公立課程計畫；南一版地理課程列全球區域發展、產業、文化交流與臺灣議題。"),
    ("kanghsuan", "https://course.cyc.edu.tw/upfile/course114/sub1/15939547496629384.pdf", "嘉義縣立布袋國民中學公立課程計畫；康軒版地理課程列全球區域比較、產業互動與問題探究。"),
    ("hanlin", "https://www.msjh.ntpc.edu.tw/uploads/1691978949408RP7cOuyZ.pdf", "臺北市立民生國民中學公立課程計畫；翰林版地理課程列地 Cb-IV-1～4，採地圖、圖表、討論、紙筆與問答評量。"),
]
UNITS = [
    ("cb-iv-1", "地 Cb-Ⅳ-1：區域發展差異", ["區域發展", "空間差異", "發展指標", "尺度比較"], "比較不同區域的自然、人口、產業與生活指標，建立多指標且有尺度意識的區域判讀。", "不能用單一指標或國家平均值代表整個區域，需說明資料時間與範圍。"),
    ("cb-iv-2", "地 Cb-Ⅳ-2：全球產業鏈", ["產業鏈", "跨國企業", "物流網絡", "勞動與環境"], "由原料、製造、運輸到消費追蹤全球產業鏈，分析價值、風險與環境成本如何分布。", "需區分生產地、品牌地、消費地與收益流向，避免把商品來源簡化成單一國家。"),
    ("cb-iv-3", "地 Cb-Ⅳ-3：文化交流與認同", ["文化交流", "人口流動", "地方認同", "文化變遷"], "以語言、飲食、宗教與媒體流動資料，分析交流如何產生混融、衝突與新的地方認同。", "不可把文化當作固定或同質，應標示誰的觀點被記錄以及資料缺口。"),
    ("cb-iv-4", "地 Cb-Ⅳ-4：全球議題回應", ["全球治理", "氣候與資源", "多方協作", "政策評估"], "整合跨國資料評估全球議題的政策回應，提出能連結尺度、利害關係與證據限制的方案。", "要分開政策目標、執行結果與分配影響，不能用宣示或單一案例證明整體成效。"),
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
    for blocker in blockers.get("blockers", []):
        if isinstance(blocker.get("reason"), str):
            blocker["reason"] = blocker["reason"].replace("Five hundred eighty-five unit samples", "Five hundred eighty-nine unit samples")
    BLOCKERS.write_text(json.dumps(blockers, ensure_ascii=False, indent=2) + "\n", encoding="utf-8")
    print(json.dumps({"unitCount": data["unitCount"], "added": len(UNITS)}, ensure_ascii=False))

if __name__ == "__main__":
    main()
