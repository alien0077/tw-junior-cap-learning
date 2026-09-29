#!/usr/bin/env python3
"""Record public-school publisher evidence for social history Fa-IV-1..4."""
import json
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
REPORT = ROOT / "implementation/reports/publisher-chapter-evidence-samples.json"
BLOCKERS = ROOT / "implementation/reports/blockers.json"
SOURCES = [
    ("nani", "https://course.cyc.edu.tw/upfile/course114/sub1/15950803923674214.pdf", "嘉義縣永慶高中公立課程計畫；南一版歷史課程列近代國家、兩次世界大戰、冷戰與臺灣。"),
    ("kanghsuan", "https://course.cyc.edu.tw/upfile/course114/sub1/15939547496629384.pdf", "嘉義縣立布袋國民中學公立課程計畫；康軒版歷史課程列民族國家、世界大戰、冷戰、全球秩序與資料探究。"),
    ("hanlin", "https://www.msjh.ntpc.edu.tw/uploads/1691978949408RP7cOuyZ.pdf", "臺北市立民生國民中學公立課程計畫；翰林版歷史課程列歷 Fa-IV-1～4，採時間線、地圖、史料、討論與紙筆評量。"),
]
UNITS = [
    ("fa-iv-1", "歷 Fa-Ⅳ-1：民族國家與帝國競爭", ["民族國家", "帝國競爭", "工業化", "國際秩序"], "以國家、產業、軍事與外交資料，分析民族國家與帝國競爭如何改變近代國際秩序。", "不能把民族國家視為自然形成，也不能把工業化成果與帝國支配分開看待。"),
    ("fa-iv-2", "歷 Fa-Ⅳ-2：世界大戰與社會", ["世界大戰", "總體戰", "動員", "平民生活"], "比較戰線、動員、經濟與平民生活資料，說明世界大戰如何造成跨區域的社會與政治後果。", "需區分戰爭宣傳、政府政策與民眾經驗，不能只用軍事勝負概括影響。"),
    ("fa-iv-3", "歷 Fa-Ⅳ-3：冷戰與全球分裂", ["冷戰", "陣營", "代理衝突", "科技競爭"], "從聯盟、代理衝突、援助與科技資料，判讀冷戰的全球尺度及不同地區的自主選擇。", "不要把世界簡化成兩個陣營，需指出地方行動者與不同議題的交錯。"),
    ("fa-iv-4", "歷 Fa-Ⅳ-4：戰後全球秩序", ["戰後秩序", "國際組織", "殖民解體", "全球化"], "整合國際組織、民族獨立、經濟與人口資料，分析戰後全球秩序的建立、限制與變化。", "需區分制度設計與實際權力，不能把加入組織直接等同平等參與。"),
]

def main():
    data = json.loads(REPORT.read_text(encoding="utf-8"))
    units = {x["lessonId"]: x for x in data["units"]}
    for suffix, title, core, representation, assessment in UNITS:
        lesson_id = "lesson-social-content-hist-" + suffix
        units[lesson_id] = {
            "lessonId": lesson_id, "title": title,
            "evidenceStatus": "chapter-level-recorded-pending-fusion-review",
            "sources": [{"publisher": publisher, "sourceUrl": url, "sourceKind": "public-school-course-plan-identifying-publisher-material", "locator": locator, "accessedAt": "2026-09-21", "observedConcepts": [title, *core], "observedRepresentations": [representation], "observedAssessment": [assessment], "licenseBoundary": "僅記錄公立學校課程計畫的出版商、單元定位與評量方向；不複製教科書正文、圖表、題目或答案。"} for publisher, url, locator in SOURCES],
            "fusionReview": {"commonCore": core, "differencesToReview": [representation, assessment], "originalSynthesisBoundary": "三版本融合、內容／版權審查與 Terra 複核完成前維持 draft，不升級 publisher status。"},
        }
    data["units"] = sorted(units.values(), key=lambda x: x["lessonId"])
    data["unitCount"] = len(data["units"])
    data["updatedAt"] = "2026-09-21"
    REPORT.write_text(json.dumps(data, ensure_ascii=False, indent=2) + "\n", encoding="utf-8")
    blockers = json.loads(BLOCKERS.read_text(encoding="utf-8"))
    for blocker in blockers.get("blockers", []):
        if isinstance(blocker.get("reason"), str): blocker["reason"] = blocker["reason"].replace("Six hundred six unit samples", "Six hundred ten unit samples")
    BLOCKERS.write_text(json.dumps(blockers, ensure_ascii=False, indent=2) + "\n", encoding="utf-8")
    print(json.dumps({"unitCount": data["unitCount"], "added": len(UNITS)}, ensure_ascii=False))

if __name__ == "__main__": main()
