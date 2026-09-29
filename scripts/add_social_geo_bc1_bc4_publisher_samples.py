#!/usr/bin/env python3
"""Record public-school publisher evidence for social geography Bc-IV-1..4."""
import json
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
REPORT = ROOT / "implementation/reports/publisher-chapter-evidence-samples.json"
BLOCKERS = ROOT / "implementation/reports/blockers.json"
SOURCES = [
    ("nani", "https://course.cyc.edu.tw/upfile/course114/sub1/15950803923674214.pdf", "嘉義縣永慶高中公立課程計畫；南一版地理課程列自然資源、氣候變遷、區域發展戰略競合與大洋洲文化連結。"),
    ("kanghsuan", "https://course.cyc.edu.tw/upfile/course114/sub1/15939547496629384.pdf", "嘉義縣立布袋國民中學公立課程計畫；康軒版地理課程列自然資源、氣候變遷衝擊、區域競合與原住民族文化。"),
    ("hanlin", "https://www.msjh.ntpc.edu.tw/uploads/1691978949408RP7cOuyZ.pdf", "臺北市立民生國民中學公立課程計畫；翰林版地理課程列地 Bc-IV-1～4，採圖表判讀、討論、紙筆與問答評量。"),
]
UNITS = [
    ("bc-iv-1", "地 Bc-Ⅳ-1：自然資源", ["自然資源", "分布與利用", "資源有限", "人地關係"], "以資源分布、開採量與消費量圖表，分析自然資源的空間差異、利用方式與永續限制。", "要求區分資源分布與可取得量，並說明資料尺度，避免把有資源直接等同可無限利用。"),
    ("bc-iv-2", "地 Bc-Ⅳ-2：氣候變遷衝擊", ["氣候變遷", "衝擊差異", "脆弱度", "調適"], "用溫度、降水、海平面與災害暴露資料，比較不同地區和群體的衝擊與調適能力。", "學生需分辨氣候趨勢、單次天氣事件與脆弱度，不以單一事件推論全部氣候變遷。"),
    ("bc-iv-3", "地 Bc-Ⅳ-3：區域發展戰略競合", ["區域戰略", "合作與競爭", "交通資源", "地緣經濟"], "以區域產業、交通、資源與政策資料，分析不同地區在合作共享與競爭配置之間的策略選擇。", "要求指出利害關係人與空間尺度，不能把區域競合簡化成單一國家對抗。"),
    ("bc-iv-4", "地 Bc-Ⅳ-4：大洋洲與臺灣原住民族文化連結", ["大洋洲", "原住民族", "文化連結", "環境與遷移"], "以海洋航路、語言／文化證據與生活環境資料，探究大洋洲與臺灣原住民族的歷史及文化連結。", "要求區分證據、推論與族群多樣性，避免以單一文化故事代表所有原住民族。"),
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
            b["reason"] = b["reason"].replace("Five hundred fifty-three unit samples", "Five hundred fifty-seven unit samples")
    BLOCKERS.write_text(json.dumps(blockers, ensure_ascii=False, indent=2) + "\n", encoding="utf-8")
    print(json.dumps({"unitCount": data["unitCount"], "added": len(UNITS)}, ensure_ascii=False))

if __name__ == "__main__":
    main()
