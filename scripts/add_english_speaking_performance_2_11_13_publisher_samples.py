#!/usr/bin/env python3
"""Record public-school publisher evidence for English speaking performance 2-Ⅳ-11..13."""
import json
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
REPORT = ROOT / "implementation/reports/publisher-chapter-evidence-samples.json"
BLOCKERS = ROOT / "implementation/reports/blockers.json"
SOURCES = [
    ("nani", "https://course.cyc.edu.tw/upfile/course113/sub1/15636172843290327.pdf", "南一版第1、2冊七年級公立課程計畫；短劇、討論與主題情境溝通定位。"),
    ("kanghsuan", "https://course.cyc.edu.tw/upfile/course112/sub1/15342166894673419.pdf", "康軒版第1、2冊七年級公立課程計畫；角色短劇、分組討論與生活主題活動定位。"),
    ("hanlin", "https://course.cyc.edu.tw/upfile/course114/sub1/15939623345151225.pdf", "翰林版第1、2冊七年級公立課程計畫；短劇展演、引導討論與主題溝通評量定位。"),
]
UNITS = [
    ("lesson-english-performance-2-iv-11", "2-Ⅳ-11：簡易短劇", ["短劇", "角色", "情節", "合作表演"], "依角色目標、場景和事件順序改編或演出簡易短劇，讓台詞、動作、語調和輪次共同傳達情節；演出後以觀眾理解和同伴回饋修訂。", "背台詞不等於演出有效；需看角色關係、情緒轉折與非語言表現是否支持情節和聽者理解。"),
    ("lesson-english-performance-2-iv-12", "2-Ⅳ-12：引導式討論", ["討論", "輪流發言", "同意異議", "理由"], "在明確主題與提示卡下提出意見、追問、同意或保留，引用對話中的資訊回應同伴；主持者要維持輪次、澄清問題並整理暫時共識。", "輪流說話不等於討論；需檢查發言是否回應前一位、是否提供理由，以及不同意時是否仍維持合作關係。"),
    ("lesson-english-performance-2-iv-13", "2-Ⅳ-13：依主題情境日常溝通", ["主題溝通", "情境轉換", "日常互動", "策略修補"], "依主題和人物關係完成購物、邀約、求助、規劃或分享等日常任務，遇到聽不懂或資訊不足時使用重述、確認、手勢或替代表達維持溝通。", "固定句型只適用單一場景；需能因目的、對象和限制調整語句，並在誤解發生時修補對話。"),
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
            blocker["reason"] = blocker["reason"].replace("Seven hundred eighty-nine unit samples", "Seven hundred ninety-two unit samples")
    BLOCKERS.write_text(json.dumps(blockers, ensure_ascii=False, indent=2) + "\n", encoding="utf-8")
    print(json.dumps({"unitCount": data["unitCount"], "added": len(UNITS)}, ensure_ascii=False))

if __name__ == "__main__": main()
