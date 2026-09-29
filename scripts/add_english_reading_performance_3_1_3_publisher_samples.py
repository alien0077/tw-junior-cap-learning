#!/usr/bin/env python3
"""Record public-school publisher evidence for English reading performance 3-Ⅳ-1..3."""
import json
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
REPORT = ROOT / "implementation/reports/publisher-chapter-evidence-samples.json"
BLOCKERS = ROOT / "implementation/reports/blockers.json"
SOURCES = [
    ("nani", "https://course.cyc.edu.tw/upfile/course113/sub1/15636172843290327.pdf", "南一版第1、2冊七年級公立課程計畫；書寫體字母、課堂字詞與生活標示閱讀定位。"),
    ("kanghsuan", "https://course.cyc.edu.tw/upfile/course112/sub1/15342166894673419.pdf", "康軒版第1、2冊七年級公立課程計畫；字母字詞辨識、圖示與公共標示活動定位。"),
    ("hanlin", "https://course.cyc.edu.tw/upfile/course114/sub1/15939623345151225.pdf", "翰林版第1、2冊七年級公立課程計畫；字體辨識、字詞閱讀與生活資訊理解定位。"),
]
UNITS = [
    ("lesson-english-performance-3-iv-1", "3-Ⅳ-1：辨識書寫體字母", ["書寫體", "印刷體", "大小寫", "字母辨識"], "比較書寫體與印刷體的大小寫對應，利用字形連續筆畫與上下文確認字母，再把辨識遷移到姓名、標題和短字詞。", "只看單一筆畫容易混淆字母；需利用整體字形、位置和字詞語境交叉確認。"),
    ("lesson-english-performance-3-iv-2", "3-Ⅳ-2：辨識課堂字詞", ["課堂字詞", "字形", "詞義", "語境"], "在課堂指令、物品和活動文本中辨認常見字詞，先利用字形與周邊句子推定功能，再用圖片、字典或再次閱讀確認。", "把字詞孤立翻譯會忽略其在指令或句子中的功能；需說明上下文如何縮小詞義範圍。"),
    ("lesson-english-performance-3-iv-3", "3-Ⅳ-3：理解簡易英文標示", ["英文標示", "圖示", "功能", "公共資訊"], "結合文字、圖示、顏色、位置與場所情境判斷標示是在指引、警告、禁止或提供服務，並說明讀者應採取的行動。", "逐字翻譯可能誤判功能；需把標示放回真實場所，確認方向、限制和對象。"),
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
            blocker["reason"] = blocker["reason"].replace("Seven hundred ninety-five unit samples", "Seven hundred ninety-eight unit samples")
    BLOCKERS.write_text(json.dumps(blockers, ensure_ascii=False, indent=2) + "\n", encoding="utf-8")
    print(json.dumps({"unitCount": data["unitCount"], "added": len(UNITS)}, ensure_ascii=False))

if __name__ == "__main__": main()
