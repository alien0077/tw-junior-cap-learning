#!/usr/bin/env python3
"""Record public-school publisher evidence for English reading performance 3-Ⅳ-7..9."""
import json
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
REPORT = ROOT / "implementation/reports/publisher-chapter-evidence-samples.json"
BLOCKERS = ROOT / "implementation/reports/blockers.json"
SOURCES = [
    ("nani", "https://course.cyc.edu.tw/upfile/course113/sub1/15636172843290327.pdf", "南一版第1、2冊七年級公立課程計畫；簡易對話、公共資訊與故事短文閱讀定位。"),
    ("kanghsuan", "https://course.cyc.edu.tw/upfile/course112/sub1/15342166894673419.pdf", "康軒版第1、2冊七年級公立課程計畫；對話文本、場所標示與故事閱讀活動定位。"),
    ("hanlin", "https://course.cyc.edu.tw/upfile/course114/sub1/15939623345151225.pdf", "翰林版第1、2冊七年級公立課程計畫；日常對話、公共資訊與故事理解評量定位。"),
]
UNITS = [
    ("lesson-english-performance-3-iv-7", "3-Ⅳ-7：理解簡易對話的主要內容", ["對話閱讀", "主旨", "說話者", "輪次線索"], "依對話輪次、稱呼、疑問與回應整理人物關係和交談目的，再以關鍵句確認主要內容與下一步行動。", "只讀單一輪次容易誤判；需把前後回應、語氣與省略資訊放在一起理解。"),
    ("lesson-english-performance-3-iv-8", "3-Ⅳ-8：理解簡易公共場所資訊", ["公共資訊", "場所", "時間", "行動"], "從公告、告示、地圖或指示牌讀取場所、時間、限制與行動要求，整合文字和圖示後判斷讀者應如何行動。", "只找關鍵名詞可能漏掉例外或限制；需核對日期、方向、單位與適用對象。"),
    ("lesson-english-performance-3-iv-9", "3-Ⅳ-9：理解簡易故事短文的主要內容", ["故事短文", "事件順序", "角色", "主旨"], "利用標題、角色、事件順序、轉折和結果建立故事骨架，區分直接敘述與推論，最後用自己的話說明主旨與因果。", "記住角色名稱不等於掌握故事；需說明問題如何發生、事件如何推進及結尾如何回應。"),
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
            blocker["reason"] = blocker["reason"].replace("Eight hundred one unit samples", "Eight hundred four unit samples")
    BLOCKERS.write_text(json.dumps(blockers, ensure_ascii=False, indent=2) + "\n", encoding="utf-8")
    print(json.dumps({"unitCount": data["unitCount"], "added": len(UNITS)}, ensure_ascii=False))

if __name__ == "__main__": main()
