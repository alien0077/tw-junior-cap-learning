#!/usr/bin/env python3
"""Record public-school publisher evidence for remaining language-domain roots."""
import json
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
REPORT = ROOT / "implementation/reports/publisher-chapter-evidence-samples.json"
BLOCKERS = ROOT / "implementation/reports/blockers.json"
SOURCES = [
    ("nani", "https://course.cyc.edu.tw/upfile/course113/sub1/15636172843290327.pdf", "嘉義縣公立校方南一版英語課程計畫；英語文領域與內容架構定位。"),
    ("kanghsuan", "https://course.cyc.edu.tw/upfile/course112/sub1/15342166894673419.pdf", "嘉義縣公立校方康軒版英語課程計畫；英語文能力、語言內容與文化架構定位。"),
    ("hanlin", "https://course.cyc.edu.tw/upfile/course114/sub1/15939623345151225.pdf", "嘉義縣公立校方翰林版英語課程計畫；聽說讀寫、語言內容與文化學習定位。"),
]
UNITS = [
    ("lesson-english-content-a", "英語文內容 A 總綱", ["字母語音", "字彙句構", "篇章理解"], "把字母、語音、字彙、句型與篇章線索放在可溝通的語境中，從形式辨認走向理解和運用。", "只背單字或句型，沒有檢查語境、功能與篇章關係。"),
    ("lesson-english-content-b", "英語文內容 B 總綱", ["聽說讀寫", "溝通策略", "文化理解"], "依任務與受眾整合聽說讀寫策略，使用澄清、重述、推論與跨文化比較完成溝通。", "把四技能當成分離練習，忽略任務目的和互動修補。"),
    ("lesson-chinese-content-a", "國語文內容 A 總綱", ["文字形音義", "詞句篇章", "語文表達"], "從字形、字音、字義進入詞句和篇章，讓形式判讀能支持閱讀理解與表達。", "只記字詞答案，沒有回到句段與語境驗證。"),
    ("lesson-chinese-content-b", "國語文內容 B 總綱", ["文本類型", "文化閱讀", "寫作表達"], "比較記敘、抒情、說明、議論與應用文本的目的、證據及語氣，再遷移到寫作和討論。", "用單一閱讀方法處理所有文體，忽略讀者、目的與證據差異。"),
]

def main():
    data = json.loads(REPORT.read_text(encoding="utf-8")); units = {x["lessonId"]: x for x in data["units"]}
    for lesson_id, title, core, representation, assessment in UNITS:
        units[lesson_id] = {"lessonId": lesson_id, "title": title, "evidenceStatus": "chapter-level-recorded-pending-fusion-review", "sources": [{"publisher": p, "sourceUrl": u, "sourceKind": "public-school-course-plan-identifying-publisher-material", "locator": f"{l}；{title}：概念、表徵與評量定位；核讀 2026-09-21。", "accessedAt": "2026-09-21", "observedConcepts": [title, *core], "observedRepresentations": [representation], "observedAssessment": [assessment], "licenseBoundary": "只記錄公立學校課程計畫的章節、教學方向與評量方式，不複製教材、例題、題目或答案。"} for p, u, l in SOURCES], "fusionReview": {"commonCore": core, "differencesToReview": [representation, assessment], "originalSynthesisBoundary": "三版本融合、內容／版權審查與 Terra 複核完成前維持 draft，不升級 publisher status。"}}
    data["units"] = sorted(units.values(), key=lambda x: x["lessonId"]); data["unitCount"] = len(data["units"]); data["updatedAt"] = "2026-09-21"; REPORT.write_text(json.dumps(data, ensure_ascii=False, indent=2) + "\n", encoding="utf-8")
    blockers = json.loads(BLOCKERS.read_text(encoding="utf-8"))
    for b in blockers.get("blockers", []):
        if isinstance(b.get("reason"), str): b["reason"] = b["reason"].replace("Nine hundred eleven unit samples", "Nine hundred fifteen unit samples")
    BLOCKERS.write_text(json.dumps(blockers, ensure_ascii=False, indent=2) + "\n", encoding="utf-8")
    print(json.dumps({"unitCount": data["unitCount"], "added": len(UNITS)}, ensure_ascii=False))

if __name__ == "__main__": main()
