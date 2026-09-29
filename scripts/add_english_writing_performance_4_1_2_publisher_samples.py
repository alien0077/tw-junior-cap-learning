#!/usr/bin/env python3
"""Record public-school publisher evidence for English writing overview and 4-Ⅳ-1..2."""
import json
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
REPORT = ROOT / "implementation/reports/publisher-chapter-evidence-samples.json"
BLOCKERS = ROOT / "implementation/reports/blockers.json"
SOURCES = [
    ("nani", "https://course.cyc.edu.tw/upfile/course113/sub1/15636172843290327.pdf", "南一版第1、2冊七年級公立課程計畫；英文寫作、字彙拼寫與圖文句子產出定位。"),
    ("kanghsuan", "https://course.cyc.edu.tw/upfile/course112/sub1/15342166894673419.pdf", "康軒版第1、2冊七年級公立課程計畫；拼字、圖片描述與句子書寫活動定位。"),
    ("hanlin", "https://course.cyc.edu.tw/upfile/course114/sub1/15939623345151225.pdf", "翰林版第1、2冊七年級公立課程計畫；字彙書寫、圖表資訊與句型書面評量定位。"),
]
UNITS = [
    ("lesson-english-performance-4", "語言能力（寫）", ["書面表達", "拼寫", "句子", "段落"], "以字詞拼寫、句子組織、功能文本和短段落逐步建立書面表達，讓內容目的、語言形式和讀者需求互相對齊，並透過修訂提高可讀性。", "寫得長不等於寫作完成；需同時檢查拼寫、句法、資訊組織、格式和任務目的。"),
    ("lesson-english-performance-4-iv-1", "4-Ⅳ-1：拼寫國中基本單字", ["拼寫", "字母順序", "音形對應", "校對"], "由讀音、字母順序、字尾和常見字形模式建立拼寫，再把單字放入句子中校對；遇到不確定拼法要使用字典或字詞表查證。", "只會辨認單字不等於能拼寫；需檢查音形、字母位置、大小寫與在句中的意義。"),
    ("lesson-english-performance-4-iv-2", "4-Ⅳ-2：依圖示圖表寫句子", ["圖示", "圖表", "資料轉寫", "句子"], "先讀圖表標題、單位和關係，再把人物、數量、位置或趨勢轉成符合資料的英文句子；寫完回看是否加入圖表沒有提供的猜測。", "把圖表名詞逐一列出不算描述；需使用比較、位置、數量或時間語句表達資料關係。"),
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
            blocker["reason"] = blocker["reason"].replace("Eight hundred thirteen unit samples", "Eight hundred sixteen unit samples")
    BLOCKERS.write_text(json.dumps(blockers, ensure_ascii=False, indent=2) + "\n", encoding="utf-8")
    print(json.dumps({"unitCount": data["unitCount"], "added": len(UNITS)}, ensure_ascii=False))

if __name__ == "__main__": main()
