#!/usr/bin/env python3
"""Record public-school publisher evidence for English reading performance 3-Ⅳ-4..6."""
import json
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
REPORT = ROOT / "implementation/reports/publisher-chapter-evidence-samples.json"
BLOCKERS = ROOT / "implementation/reports/blockers.json"
SOURCES = [
    ("nani", "https://course.cyc.edu.tw/upfile/course113/sub1/15636172843290327.pdf", "南一版第1、2冊七年級公立課程計畫；簡易圖表、生活用語與句型閱讀定位。"),
    ("kanghsuan", "https://course.cyc.edu.tw/upfile/course112/sub1/15342166894673419.pdf", "康軒版第1、2冊七年級公立課程計畫；表格圖像、生活語句與核心句型閱讀定位。"),
    ("hanlin", "https://course.cyc.edu.tw/upfile/course114/sub1/15939623345151225.pdf", "翰林版第1、2冊七年級公立課程計畫；圖表資訊、生活溝通文本與句型理解定位。"),
]
UNITS = [
    ("lesson-english-performance-3-iv-4", "3-Ⅳ-4：理解簡易圖表", ["圖表", "標題", "欄列", "資料比較"], "先讀圖表標題、單位、欄列與圖例，再把數字或分類資訊轉成英文句子；回答時區分圖表直接呈現和根據資料推論的內容。", "只抓最高或最低值可能忽略問題焦點；需確認比較對象、時間範圍、單位與資料限制。"),
    ("lesson-english-performance-3-iv-5", "3-Ⅳ-5：理解簡易生活用語", ["生活用語", "語境", "功能", "語用"], "依場所、人物關係和前後句判斷生活用語是在問候、請求、邀約、拒絕或提供資訊，不能只用字面翻譯決定意思。", "同一句話在不同場景可能有不同功能；需利用稱呼、語氣、回應與情境線索驗證解讀。"),
    ("lesson-english-performance-3-iv-6", "3-Ⅳ-6：理解基本重要句型", ["基本句型", "語序", "時間", "句意"], "以主語、動詞、疑問詞、否定詞和時間線索拆解基本句型，先判斷句子功能，再把句型放回段落確認指涉與事件關係。", "只看單字而忽略否定、時態或疑問範圍會改變句意；需保留句法線索並說明推理步驟。"),
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
            blocker["reason"] = blocker["reason"].replace("Seven hundred ninety-eight unit samples", "Eight hundred one unit samples")
    BLOCKERS.write_text(json.dumps(blockers, ensure_ascii=False, indent=2) + "\n", encoding="utf-8")
    print(json.dumps({"unitCount": data["unitCount"], "added": len(UNITS)}, ensure_ascii=False))

if __name__ == "__main__": main()
