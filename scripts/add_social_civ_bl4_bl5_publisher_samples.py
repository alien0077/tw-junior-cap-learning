#!/usr/bin/env python3
"""Record public-school publisher evidence for social civics Bl-IV-4..5."""
import json
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
REPORT = ROOT / "implementation/reports/publisher-chapter-evidence-samples.json"
BLOCKERS = ROOT / "implementation/reports/blockers.json"
SOURCES = [
    ("nani", "https://www.cksh.hc.edu.tw/uploads/1703731557126uLS1C2G5.pdf", "新竹市立建功高中國中部公立課程計畫；文件標示南一版，課程欄列公 Bl-IV-4、Bl-IV-5，並以資源分配與價格機制為單元定位。"),
    ("kanghsuan", "https://course.cyc.edu.tw/upfile/course114/sub1/15939547496629384.pdf", "嘉義縣立布袋國民中學公立課程計畫；文件標示康軒版第五、六冊，課程欄列公 Bl-IV-4、Bl-IV-5，並安排資料判讀與討論。"),
    ("hanlin", "https://course.cyc.edu.tw/upfile/course114/file_school/15952869896665246.pdf", "嘉義縣阿里山國民中小學公立課程計畫；文件標示翰林版第五冊，課程欄列公 Bl-IV-4、Bl-IV-5，並連結價格、資源分配與評量活動。"),
]
UNITS = [
    {
        "lessonId": "lesson-social-content-civ-bl-iv-4",
        "title": "公 Bl-Ⅳ-4：價格影響資源分配",
        "core": ["價格訊號", "供需與資源配置", "誘因", "價格不是唯一分配條件"],
        "representation": "用同一項稀少資源在價格變動前後的需求、供給與分配結果表，追蹤價格如何傳遞稀少性與誘因訊息。",
        "assessment": "要求由資料指出價格變化、行為反應與分配結果的連結，並說明政策或市場限制，避免把價格直接等同公平。",
    },
    {
        "lessonId": "lesson-social-content-civ-bl-iv-5",
        "title": "公 Bl-Ⅳ-5：不同資源分配方法的優缺點",
        "core": ["市場價格分配", "排隊與抽籤", "配給與資格分配", "效率與公平的權衡"],
        "representation": "以比較矩陣呈現市場、排隊、抽籤、配給等方法在效率、資訊需求、弱勢保障與執行成本上的差異。",
        "assessment": "先辨認分配規則，再依情境目標與限制提出方案及代價，不能只用『公平』或『有效率』單一詞語下結論。",
    },
]

def main():
    data = json.loads(REPORT.read_text(encoding="utf-8"))
    units = {x["lessonId"]: x for x in data["units"]}
    for u in UNITS:
        sources = []
        for publisher, url, locator in SOURCES:
            sources.append({
                "publisher": publisher,
                "sourceUrl": url,
                "sourceKind": "public-school-course-plan-identifying-publisher-material",
                "locator": locator,
                "accessedAt": "2026-09-21",
                "observedConcepts": [u["title"], *u["core"]],
                "observedRepresentations": [u["representation"]],
                "observedAssessment": [u["assessment"]],
                "licenseBoundary": "僅記錄公立學校課程計畫的出版商、單元定位與評量方向；不複製教科書正文、圖表、題目或答案。",
            })
        units[u["lessonId"]] = {
            "lessonId": u["lessonId"], "title": u["title"],
            "evidenceStatus": "chapter-level-recorded-pending-fusion-review",
            "sources": sources,
            "fusionReview": {
                "commonCore": u["core"],
                "differencesToReview": [u["representation"], u["assessment"]],
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
            b["reason"] = b["reason"].replace("Five hundred one unit samples", "Five hundred three unit samples")
    BLOCKERS.write_text(json.dumps(blockers, ensure_ascii=False, indent=2) + "\n", encoding="utf-8")
    print(json.dumps({"unitCount": data["unitCount"], "added": 2}, ensure_ascii=False))

if __name__ == "__main__":
    main()
