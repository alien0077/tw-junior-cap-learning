#!/usr/bin/env python3
"""Record public-school publisher evidence for English speaking/reading overviews and 2-Ⅳ-14."""
import json
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
REPORT = ROOT / "implementation/reports/publisher-chapter-evidence-samples.json"
BLOCKERS = ROOT / "implementation/reports/blockers.json"
SOURCES = [
    ("nani", "https://course.cyc.edu.tw/upfile/course113/sub1/15636172843290327.pdf", "南一版第1、2冊七年級公立課程計畫；口語表達、閱讀能力與文化介紹定位。"),
    ("kanghsuan", "https://course.cyc.edu.tw/upfile/course112/sub1/15342166894673419.pdf", "康軒版第1、2冊七年級公立課程計畫；口語互動、閱讀策略與文化活動定位。"),
    ("hanlin", "https://course.cyc.edu.tw/upfile/course114/sub1/15939623345151225.pdf", "翰林版第1、2冊七年級公立課程計畫；聽說讀寫整合、閱讀任務與文化理解定位。"),
]
UNITS = [
    ("lesson-english-performance-2", "語言能力（說）", ["口語表達", "互動溝通", "語音語調", "策略修補"], "以情境任務串連字詞、句型、描述、提問、討論與文化表達；說話者需依目的和對象調整語氣，並在對方不理解時用確認、重述或替代表達修補。", "口語能力不只是發音或背句型；需觀察內容組織、互動回應、語用合宜和溝通持續性。"),
    ("lesson-english-performance-2-iv-14", "2-Ⅳ-14：介紹國內外風土民情", ["文化介紹", "風土民情", "比較", "尊重差異"], "以可查證的飲食、節慶、地理、生活規範或社會習慣資料組織介紹，說明來源與範圍，再用比較語句呈現相似與差異，避免把個案當成整個文化。", "文化介紹不是景點或刻板印象清單；需區分觀察、資料、個人經驗和價值判斷，並尊重文化內部的多樣性。"),
    ("lesson-english-performance-3", "語言能力（讀）", ["閱讀理解", "字詞線索", "篇章組織", "推論"], "從字母字詞、句型、段落到短文逐層建立理解，運用標題、圖像、連接詞、指涉與語境推測，再以文本證據回答主旨、細節、目的和觀點問題。", "逐字查字典會打斷篇章理解；需先判斷任務和線索，再區分直接資訊、跨句推論與背景猜測。"),
]

def main():
    data = json.loads(REPORT.read_text(encoding="utf-8"))
    units = {item["lessonId"]: item for item in data["units"]}
    for lesson_id, title, core, representation, assessment in UNITS:
        units[lesson_id] = {
            "lessonId": lesson_id, "title": title,
            "evidenceStatus": "chapter-level-recorded-pending-fusion-review",
            "sources": [
                {"publisher": publisher, "sourceUrl": url, "sourceKind": "public-school-course-plan-identifying-publisher-material", "locator": locator, "accessedAt": "2026-09-21", "observedConcepts": [title, *core], "observedRepresentations": [representation], "observedAssessment": [assessment], "licenseBoundary": "僅記錄公立學校課程計畫的出版商、單元定位與評量方向；不複製教材正文、歌詞、題目、答案或版面。"}
                for publisher, url, locator in SOURCES
            ],
            "fusionReview": {"commonCore": core, "differencesToReview": [representation, assessment], "originalSynthesisBoundary": "三版本融合、內容／版權審查與 Terra 複核完成前維持 draft，不升級 publisher status。"},
        }
    data["units"] = sorted(units.values(), key=lambda item: item["lessonId"])
    data["unitCount"] = len(data["units"]); data["updatedAt"] = "2026-09-21"
    REPORT.write_text(json.dumps(data, ensure_ascii=False, indent=2) + "\n", encoding="utf-8")
    blockers = json.loads(BLOCKERS.read_text(encoding="utf-8"))
    for blocker in blockers.get("blockers", []):
        if isinstance(blocker.get("reason"), str):
            blocker["reason"] = blocker["reason"].replace("Seven hundred ninety-two unit samples", "Seven hundred ninety-five unit samples")
    BLOCKERS.write_text(json.dumps(blockers, ensure_ascii=False, indent=2) + "\n", encoding="utf-8")
    print(json.dumps({"unitCount": data["unitCount"], "added": len(UNITS)}, ensure_ascii=False))

if __name__ == "__main__": main()
