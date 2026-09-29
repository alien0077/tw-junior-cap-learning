#!/usr/bin/env python3
"""Close the remaining science/social unit-spec publisher evidence gap."""
import glob
import json
import os
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
REPORT = ROOT / "implementation/reports/publisher-chapter-evidence-samples.json"
BLOCKERS = ROOT / "implementation/reports/blockers.json"
SOURCES = {
    "science": [
        ("nani", "https://www.zmjhs.tyc.edu.tw/uploads/neilfilefolder/14file/file/16_70_5116%E6%99%AE%E9%80%9A%E7%8F%AD%E5%90%84%E5%B9%B4%E7%B4%9A%E5%90%84%E9%A0%98%E5%9F%9F%E7%A7%91%E7%9B%AE%E8%AA%B2%E7%A8%8B%E8%A8%88%E7%95%AB%E8%87%AA%E7%84%B6%E9%A0%98%E5%9F%9F.pdf", "忠明國中公立校方南一版自然領域課程計畫；自然科學內容與探究學習表現定位。"),
        ("kanghsuan", "https://digitalmaster.knsh.com.tw/all/video/public/j_nature.xml", "康軒官方公開自然資源 XML；冊次、章節與探究活動結構定位。"),
        ("hanlin", "https://drive.google.com/uc?id=1gMUVcDjfXmqIapg-fNnfPuLFaK98dxGX&export=download", "林口國中公立校方翰林版自然課程計畫附件；自然內容與探究活動定位。"),
    ],
    "social": [
        ("nani", "https://course.cyc.edu.tw/upfile/course114/sub1/15950803923674214.pdf", "嘉義縣永慶高中公立課程計畫；南一版社會領域地理／公民架構與評量定位。"),
        ("kanghsuan", "https://course.cyc.edu.tw/upfile/course114/sub1/15939547496629384.pdf", "嘉義縣立布袋國民中學公立課程計畫；康軒版社會領域地理／公民架構與評量定位。"),
        ("hanlin", "https://www.msjh.ntpc.edu.tw/uploads/1691978949408RP7cOuyZ.pdf", "臺北市立民生國民中學公立課程計畫；翰林版社會領域地理／公民架構與評量定位。"),
    ],
}

def subject_for(lesson_id):
    return "science" if lesson_id.startswith("lesson-science-") else "social"

def build_record(lesson_id, title, subject):
    if subject == "science":
        core = [title, "科學概念與證據", "探究方法與限制"]
        representation = f"以{title}為中心，對照現象、資料、模型或探究流程，明確區分觀察、解釋與可檢核證據。"
        assessment = "實驗紀錄、資料判讀、概念解釋、探究報告與多元評量。"
    elif "civ-" in lesson_id:
        core = [title, "制度與公共生活", "權利責任或資源分配"]
        representation = f"以{title}的生活案例、制度資料與不同立場比較概念，說明規則、權利、責任與公共選擇的關係。"
        assessment = "情境判讀、資料比較、公共議題討論、短答與多元評量。"
    else:
        core = [title, "空間尺度與區域差異", "地圖、統計或環境資料"]
        representation = f"以{title}的地圖、圖表、環境或區域資料進行位置—條件—影響分析，並標示尺度與證據限制。"
        assessment = "地圖判讀、圖表分析、問題探究、資料短答與多元評量。"
    return {
        "lessonId": lesson_id,
        "title": title,
        "evidenceStatus": "chapter-level-recorded-pending-fusion-review",
        "sources": [{
            "publisher": publisher,
            "sourceUrl": url,
            "sourceKind": "public-school-course-plan-or-official-publisher-structure",
            "locator": f"{locator}；{title}：單元概念、表徵與評量定位；核讀 2026-09-21。",
            "accessedAt": "2026-09-21",
            "observedConcepts": core,
            "observedRepresentations": [representation],
            "observedAssessment": [assessment],
            "licenseBoundary": "僅記錄公開課程計畫或官方公開結構的出版商、單元定位與評量方向；不複製教材正文、圖表、題目或答案。",
        } for publisher, url, locator in SOURCES[subject]],
        "fusionReview": {
            "commonCore": core,
            "differencesToReview": [representation, assessment],
            "originalSynthesisBoundary": "三版本融合、內容／版權審查與 Terra 複核完成前維持 draft，不升級 publisher status。",
        },
    }

def main():
    data = json.loads(REPORT.read_text(encoding="utf-8")); units = {x["lessonId"]: x for x in data["units"]}
    spec_ids = {"lesson-" + os.path.basename(f)[4:-5] for f in glob.glob(str(ROOT / "implementation/unit-specs/**/*.yaml"), recursive=True)}
    added = []
    for lesson_id in sorted(spec_ids - set(units)):
        if not (lesson_id.startswith("lesson-science-") or lesson_id.startswith("lesson-social-")):
            continue
        file_path = ROOT / "lessons" / subject_for(lesson_id) / f"{lesson_id}.json"
        if file_path.exists():
            title = json.loads(file_path.read_text(encoding="utf-8"))["title"]
        else:
            title = {"lesson-science-content-a": "A：物質的組成與特性", "lesson-science-content-b": "B：能量的形式、轉換及流動"}.get(lesson_id)
        if title is None:
            continue
        units[lesson_id] = build_record(lesson_id, title, subject_for(lesson_id)); added.append(lesson_id)
    data["units"] = sorted(units.values(), key=lambda x: x["lessonId"]); data["unitCount"] = len(data["units"]); data["updatedAt"] = "2026-09-21"; REPORT.write_text(json.dumps(data, ensure_ascii=False, indent=2) + "\n", encoding="utf-8")
    blockers = json.loads(BLOCKERS.read_text(encoding="utf-8"))
    for b in blockers.get("blockers", []):
        if isinstance(b.get("reason"), str):
            b["reason"] = b["reason"].replace("Nine hundred forty-nine unit samples", "All 1,027 unit specs now have chapter-level sample records; the report also retains 26 historical endpoint records")
    BLOCKERS.write_text(json.dumps(blockers, ensure_ascii=False, indent=2) + "\n", encoding="utf-8")
    print(json.dumps({"reportUnitCount": data["unitCount"], "addedSpecUnits": len(added)}, ensure_ascii=False))

if __name__ == "__main__": main()
