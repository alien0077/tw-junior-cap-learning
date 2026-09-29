#!/usr/bin/env python3
"""Record public-school publisher evidence for English thinking and content roots."""
import json
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
REPORT = ROOT / "implementation/reports/publisher-chapter-evidence-samples.json"
BLOCKERS = ROOT / "implementation/reports/blockers.json"
SOURCES = [
    ("nani", "https://course.cyc.edu.tw/upfile/course113/sub1/15636172843290327.pdf", "南一版第1、2冊七年級公立課程計畫；閱讀策略、句型溝通與思考能力定位。"),
    ("kanghsuan", "https://course.cyc.edu.tw/upfile/course112/sub1/15342166894673419.pdf", "康軒版第1、2冊七年級公立課程計畫；問題解決、句型線索與語用理解定位。"),
    ("hanlin", "https://course.cyc.edu.tw/upfile/course114/sub1/15939623345151225.pdf", "翰林版第1、2冊七年級公立課程計畫；英語思考策略、跨文本理解與自主學習定位。"),
]
UNITS = [
    ("lesson-english-content-d", "D：思考能力", ["思考策略", "問題解決", "推論", "反思"], "以預測、分類、比較、推論、查證和反思處理英文訊息；學生要說明自己如何從語言線索與情境證據得到結論，而不是只交出答案。", "把猜中答案當成思考完成會忽略過程；需保留線索、排除理由和不確定性，才能檢查推論是否可遷移。"),
    ("lesson-english-content-root-a", "英語學習內容 A：用句型線索完成準確溝通", ["句型線索", "句法", "語意", "溝通任務"], "把句型形式、語序、時間與人稱線索連到溝通目的，在問答、描述、請求與敘事中選擇能讓聽者理解的表達；完成後以替換情境檢查是否仍準確。", "只填對文法選項不等於完成溝通；需說明形式如何改變意義與禮貌，並處理對象、情境和回應。"),
    ("lesson-english-content-root-b", "英語學習內容 B：從閱讀線索推回訊息與語用", ["閱讀線索", "主旨", "語用", "跨句整合"], "從標題、關鍵字、代名詞、連接詞、語氣與段落功能整合訊息，推回作者目的、人物關係與未明說的意思，再用文本片段支持解釋。", "只翻譯單字會失去語用；需區分字面資訊、跨句推論與文化背景推測，並標出證據的強弱。"),
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
            blocker["reason"] = blocker["reason"].replace("Seven hundred sixty-two unit samples", "Seven hundred sixty-five unit samples")
    BLOCKERS.write_text(json.dumps(blockers, ensure_ascii=False, indent=2) + "\n", encoding="utf-8")
    print(json.dumps({"unitCount": data["unitCount"], "added": len(UNITS)}, ensure_ascii=False))

if __name__ == "__main__": main()
