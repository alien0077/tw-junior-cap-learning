#!/usr/bin/env python3
"""Record public-school publisher evidence for English syntax, discourse and culture."""
import json
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
REPORT = ROOT / "implementation/reports/publisher-chapter-evidence-samples.json"
BLOCKERS = ROOT / "implementation/reports/blockers.json"
SOURCES = [
    ("nani", "https://course.cyc.edu.tw/upfile/course113/sub1/15636172843290327.pdf", "南一版第1、2冊七年級公立課程計畫；句型、篇章與生活文化素材定位。"),
    ("kanghsuan", "https://course.cyc.edu.tw/upfile/course112/sub1/15342166894673419.pdf", "康軒版第1、2冊七年級公立課程計畫；句構練習、短文理解與文化活動定位。"),
    ("hanlin", "https://course.cyc.edu.tw/upfile/course114/sub1/15939623345151225.pdf", "翰林版第1、2冊七年級公立課程計畫；句型語用、篇章理解與文化理解定位。"),
]
UNITS = [
    ("lesson-english-content-ad", "Ad：句構", ["句型", "語序", "時態", "語用"], "以句子的角色、語序、時態、助動詞和連接詞解釋意思，再把句型放回請求、描述、敘事或提問情境，觀察形式如何改變溝通功能。", "只背文法名稱不能證明會用；需指出句中線索、說明為何選擇形式，並在新情境中完成表達。"),
    ("lesson-english-content-ae", "Ae：篇章", ["篇章", "段落", "主旨", "連貫"], "從標題、關鍵詞、代名詞、連接詞與段落功能建立篇章地圖，區分主旨、細節、推論與作者目的，再用證據重述內容。", "逐句翻譯可能失去篇章關係；需檢查指涉、因果、轉折與段落組織如何共同支持理解。"),
    ("lesson-english-content-c", "C：文化與習俗", ["文化", "習俗", "比較", "尊重差異"], "以語言使用和生活情境比較不同社群的稱呼、節慶、時間安排與互動規範，先描述可觀察資料，再區分文化差異、個人選擇與刻板印象。", "把單一文本當成整個文化的代表會過度概括；需標示資料範圍、比較維度與不確定處，避免價值評斷取代理解。"),
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
            blocker["reason"] = blocker["reason"].replace("Seven hundred fifty-nine unit samples", "Seven hundred sixty-two unit samples")
    BLOCKERS.write_text(json.dumps(blockers, ensure_ascii=False, indent=2) + "\n", encoding="utf-8")
    print(json.dumps({"unitCount": data["unitCount"], "added": len(UNITS)}, ensure_ascii=False))

if __name__ == "__main__": main()
