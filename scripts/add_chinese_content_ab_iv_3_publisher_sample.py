#!/usr/bin/env python3
"""Record three public-school publisher-linked records for Chinese Ab-IV-3."""
from __future__ import annotations

import json
import re
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
REPORT = ROOT / "implementation/reports/publisher-chapter-evidence-samples.json"

SAMPLE = {
    "lessonId": "lesson-chinese-content-ab-iv-3",
    "title": "Ab-Ⅳ-3：象形指事會意形聲",
    "evidenceStatus": "chapter-level-recorded-pending-fusion-review",
    "sources": [
        {
            "publisher": "nani",
            "sourceUrl": "https://fsjh.chc.edu.tw/storage/074521/open_files/01%E6%95%99%E5%8B%99%E8%99%95/002%E5%B9%B4%E5%BA%A6%E8%AA%B2%E7%A8%8B%E8%A8%88%E7%95%AB/110%E5%AD%B8%E5%B9%B4%E5%BA%A6%E8%AA%B2%E7%A8%8B%E8%A8%88%E7%95%AB/%E5%9C%8B%E6%96%87/%E5%9C%8B%E6%96%87%E4%B8%83%E5%B9%B4%E7%B4%9A.pdf",
            "sourceKind": "public-school-course-plan-identifying-publisher-material",
            "locator": "彰化縣福興國中 110 學年度七年級南一版國文課程計畫；第 6 週語文常識『認識漢字的造字法則』明列 Ab-Ⅳ-3，從文字演變字卡、造字依據、圖卡與討論引導象形、指事、會意、形聲，採參與、合作、口頭與作業評量；核讀 2026-09-20。",
            "accessedAt": "2026-09-20",
            "observedConcepts": ["四種基本造字原則", "文字形體演變與造字依據", "由構件和圖像推測字形、字義"],
            "observedRepresentations": ["古今字形卡片", "實物／圖像與象形字對照", "構件圖示和小組討論"],
            "observedAssessment": ["參與態度", "合作能力", "口頭評量", "作業評量"],
            "licenseBoundary": "只記錄公立學校課程計畫的教材版本、章節教學方向與評量方式，不複製南一教材、圖卡、題目或答案。",
        },
        {
            "publisher": "kanghsuan",
            "sourceUrl": "https://market.cloud.edu.tw/resources/web/1807317",
            "sourceKind": "public-school-course-plan-identifying-publisher-material",
            "locator": "教育部教育雲公開臺北市士林國中混成教學資源；頁面明列教材版本為康軒版、授課年級為國中，對應 Ab-Ⅳ-3 四種造字原則，並以字體演變、書法欣賞、數位共編與學生創作進行學習；核讀 2026-09-20。",
            "accessedAt": "2026-09-20",
            "observedConcepts": ["象形、指事、會意、形聲的分類", "字體演變與構件觀察", "由造字原理連結識字與創作"],
            "observedRepresentations": ["字體演變視覺材料", "數位簡報與共編卡片", "造字原則與書法作品對照"],
            "observedAssessment": ["數位共編活動", "口頭說明", "造字創作", "作品分享"],
            "licenseBoundary": "只記錄公立學校公開教學資源中的教材版本、學習內容與活動方向，不複製康軒教材、投影片、圖片、題目或答案。",
        },
        {
            "publisher": "hanlin",
            "sourceUrl": "https://www.curriculum.chc.edu.tw/storage/164/110/5-7-%E5%9C%8B%E8%AA%9E%E6%96%87.pdf/Go8bL8272DkbZSBkIKB7cjbselE8qpVsFtUIUjGh.pdf",
            "sourceKind": "public-school-course-plan-identifying-publisher-material",
            "locator": "彰化縣公立國中 110 學年度七年級翰林版國文教學進度總表；公開 PDF p.38 附近的 Ab-Ⅳ-3 單元明列象形、指事、會意、形聲，要求觀察實物與象形字、理解指事抽象概念、辨認形符聲符並完成形聲字報告，搭配學習單、資料蒐集與口頭報告；核讀 2026-09-20。",
            "accessedAt": "2026-09-20",
            "observedConcepts": ["四種造字原則的定義與差異", "形符／聲符功能", "由字形演變與部件證據判定造字方法"],
            "observedRepresentations": ["實物圖像與古文字比較", "指事字的抽象標記", "形聲字部件分析與小組報告"],
            "observedAssessment": ["學習單", "資料蒐集", "口頭報告", "互動觀察"],
            "licenseBoundary": "只記錄公立學校課程計畫的教材版本、章節學習重點與評量方向，不複製翰林教材、動畫、報告內容、題目或答案。",
        },
    ],
    "fusionReview": {
        "commonCore": [
            "三版本均把象形、指事、會意、形聲視為可用構件證據判斷的造字原則，而非死背名稱",
            "教學均從字形演變、部件功能或圖像／語境觀察走向分類與說明",
            "評量要求學生說出判定理由，並可透過卡片、報告、創作或討論表達",
        ],
        "differencesToReview": [
            "南一較突出文字演變字卡、古人造字依據與合作討論",
            "康軒公開混成資源把造字原理接到字體演變、書法欣賞和數位創作",
            "翰林將實物／圖像、指事抽象概念與形符聲符分層，並要求形聲字小組報告",
        ],
        "originalSynthesisBoundary": "本樣本只記錄三筆可追溯的公立學校／公立教育資源章節級證據；lesson 正文、互動與題目仍須逐單元融合、內容／版權審查與 Terra 複核，維持 draft，不升級 publisher status。",
    },
}


def main() -> None:
    data = json.loads(REPORT.read_text(encoding="utf-8"))
    if not any(item.get("lessonId") == SAMPLE["lessonId"] for item in data["units"]):
        data["units"].append(SAMPLE)
    data["unitCount"] = len(data["units"])
    data["updatedAt"] = "2026-09-20"
    REPORT.write_text(json.dumps(data, ensure_ascii=False, indent=2) + "\n", encoding="utf-8")

    blocker_path = ROOT / "implementation/reports/blockers.json"
    blockers = json.loads(blocker_path.read_text(encoding="utf-8"))
    for blocker in blockers.get("blockers", []):
        reason = blocker.get("reason")
        if isinstance(reason, str) and "unit samples" in reason:
            blocker["reason"] = re.sub(r"Four hundred eleven unit samples", "Four hundred twelve unit samples", reason)
    blocker_path.write_text(json.dumps(blockers, ensure_ascii=False, indent=2) + "\n", encoding="utf-8")
    print(json.dumps({"unitCount": data["unitCount"], "lessonId": SAMPLE["lessonId"]}, ensure_ascii=False))


if __name__ == "__main__":
    main()
