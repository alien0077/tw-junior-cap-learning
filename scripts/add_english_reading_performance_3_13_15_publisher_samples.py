#!/usr/bin/env python3
"""Record public-school publisher evidence for English reading performance 3-Ⅳ-13..15."""
import json
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
REPORT = ROOT / "implementation/reports/publisher-chapter-evidence-samples.json"
BLOCKERS = ROOT / "implementation/reports/blockers.json"
SOURCES = [
    ("nani", "https://course.cyc.edu.tw/upfile/course113/sub1/15636172843290327.pdf", "南一版第1、2冊七年級公立課程計畫；短劇閱讀、快速閱讀與敘事觀點定位。"),
    ("kanghsuan", "https://course.cyc.edu.tw/upfile/course112/sub1/15342166894673419.pdf", "康軒版第1、2冊七年級公立課程計畫；短劇大意、重點掃讀與文本觀點活動定位。"),
    ("hanlin", "https://course.cyc.edu.tw/upfile/course114/sub1/15939623345151225.pdf", "翰林版第1、2冊七年級公立課程計畫；短文理解、快速閱讀與作者態度目的評量定位。"),
]
UNITS = [
    ("lesson-english-performance-3-iv-13", "3-Ⅳ-13：了解簡易短劇大意", ["短劇大意", "角色", "事件", "情節主旨"], "先用角色、場景和輪次重建短劇事件，再辨認衝突與結果，最後用不依賴台詞逐句翻譯的方式重述大意。", "只摘錄台詞或角色名稱不等於理解；需說明事件順序和角色目標如何形成主旨。"),
    ("lesson-english-performance-3-iv-14", "3-Ⅳ-14：快速閱讀抓重點", ["快速閱讀", "略讀", "掃讀", "重點"], "依題目和閱讀目的先略讀標題、首尾與段落首句，再掃讀數字、專名或關鍵詞定位證據；找到重點後回讀確認上下文和限制。", "快讀不是任意跳讀；需交代選擇策略的理由，並檢查是否因速度漏掉否定、轉折或例外。"),
    ("lesson-english-performance-3-iv-15", "3-Ⅳ-15：分析敘事者觀點態度目的", ["敘事者", "觀點", "態度", "目的"], "比較敘事者選擇呈現的事件、形容詞、引述和省略，推論其觀點、態度與寫作目的；同時區分文本明示和讀者推論。", "把作者或敘事者和角色聲音混為一談會誤讀；需標出語言證據、敘事距離與可能的其他解讀。"),
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
            blocker["reason"] = blocker["reason"].replace("Eight hundred seven unit samples", "Eight hundred ten unit samples")
    BLOCKERS.write_text(json.dumps(blockers, ensure_ascii=False, indent=2) + "\n", encoding="utf-8")
    print(json.dumps({"unitCount": data["unitCount"], "added": len(UNITS)}, ensure_ascii=False))

if __name__ == "__main__": main()
