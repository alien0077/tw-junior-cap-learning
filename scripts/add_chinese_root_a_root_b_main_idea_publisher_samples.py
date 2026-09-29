#!/usr/bin/env python3
"""Record public-school publisher evidence for Chinese root A, root B and main idea."""
import json
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
REPORT = ROOT / "implementation/reports/publisher-chapter-evidence-samples.json"
BLOCKERS = ROOT / "implementation/reports/blockers.json"
SOURCES = [
    ("nani", "https://course.cyc.edu.tw/upfile/course114/sub1/15950803923674214.pdf", "嘉義縣永慶高中公立課程計畫；南一版字句證據、篇章觀點與主旨結構定位。"),
    ("kanghsuan", "https://course.cyc.edu.tw/upfile/course114/sub1/15939547496629384.pdf", "嘉義縣立布袋國民中學公立課程計畫；康軒版國文理解、證據追問與篇章閱讀定位。"),
    ("hanlin", "https://www.msjh.ntpc.edu.tw/uploads/1691978949408RP7cOuyZ.pdf", "臺北市立民生國民中學公立課程計畫；翰林版國文課程列根本內容 A、B 與主旨結構，採文本證據、段落分析及紙筆評量。"),
]
UNITS = [
    ("root-a", "國文學習內容 A：從字句線索建立可驗證的理解", ["字句線索", "語境推論", "文本證據", "理解驗證"], "從字詞、句法、指涉與連接詞逐層建立理解，將每個解釋回指到可定位的文字線索，並區分文本明示與讀者推論。", "答案看似合理不代表有根據；需檢查是否漏看否定、範圍、語氣、指涉或轉折。"),
    ("root-b", "國文學習內容 B：讓篇章觀點經得起證據追問", ["篇章觀點", "論述結構", "跨段證據", "反例追問"], "把篇章的主旨、觀點與段落功能連成證據網，追問作者如何選材、安排順序與回應可能的反對意見。", "不能用一句摘要代替觀點證明；需跨段整合、辨認省略前提，並說明反例是否真正削弱結論。"),
    ("main-idea-structure", "篇章主旨、結構與寓意", ["主旨", "段落功能", "結構轉折", "寓意推論"], "先辨認段落在敘事、說明或論證中的功能，再由重複、對比、轉折與結尾回收主旨，最後檢查寓意推論是否超出文本。", "主旨、中心事件與寓意不是同一層次；需分別提出證據，避免只憑個人感想替文章加上道德結論。"),
]

def main():
    data = json.loads(REPORT.read_text(encoding="utf-8"))
    units = {x["lessonId"]: x for x in data["units"]}
    for suffix, title, core, representation, assessment in UNITS:
        lesson_id = "lesson-chinese-" + suffix
        units[lesson_id] = {
            "lessonId": lesson_id,
            "title": title,
            "evidenceStatus": "chapter-level-recorded-pending-fusion-review",
            "sources": [
                {
                    "publisher": publisher,
                    "sourceUrl": url,
                    "sourceKind": "public-school-course-plan-identifying-publisher-material",
                    "locator": locator,
                    "accessedAt": "2026-09-21",
                    "observedConcepts": [title, *core],
                    "observedRepresentations": [representation],
                    "observedAssessment": [assessment],
                    "licenseBoundary": "僅記錄公立學校課程計畫的出版商、單元定位與評量方向；不複製教科書正文、圖表、題目或答案。",
                }
                for publisher, url, locator in SOURCES
            ],
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
            blocker["reason"] = blocker["reason"].replace("Seven hundred ten unit samples", "Seven hundred thirteen unit samples")
    BLOCKERS.write_text(json.dumps(blockers, ensure_ascii=False, indent=2) + "\n", encoding="utf-8")
    print(json.dumps({"unitCount": data["unitCount"], "added": len(UNITS)}, ensure_ascii=False))

if __name__ == "__main__":
    main()
