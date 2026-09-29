#!/usr/bin/env python3
"""Record three public-school publisher-linked records for Chinese Ab-IV-2."""
from __future__ import annotations

import json
import re
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
REPORT = ROOT / "implementation/reports/publisher-chapter-evidence-samples.json"

SAMPLE = {
    "lessonId": "lesson-chinese-content-ab-iv-2",
    "title": "Ab-Ⅳ-2：3500常用字使用",
    "evidenceStatus": "chapter-level-recorded-pending-fusion-review",
    "sources": [
        {
            "publisher": "nani",
            "sourceUrl": "https://course.cyc.edu.tw/upfile/course110/sub1/14793292177358929.pdf",
            "sourceKind": "public-school-course-plan-identifying-publisher-material",
            "locator": "嘉義縣大林國民中學九年級國文領域教學計畫；公開 PDF 明列教材版本為南一版國中國文，將常用字從字形、字音、字義延伸到課文詞語與閱讀理解，並以口頭提問、習作練習和文本活動檢核使用；核讀 2026-09-20。",
            "accessedAt": "2026-09-20",
            "observedConcepts": ["常用字在詞語和句子中的正確使用", "字音字義與語境的配合", "詞語使用支援文本理解與表達"],
            "observedRepresentations": ["詞語放回課文句子", "字詞意義與前後文線索", "閱讀理解和口語回答"],
            "observedAssessment": ["口頭提問", "習作練習", "課程討論", "課文閱讀理解"],
            "licenseBoundary": "只記錄公立學校課程計畫的教材版本、學習重點與評量方向，不複製南一教材正文、例題、題目或答案。",
        },
        {
            "publisher": "kanghsuan",
            "sourceUrl": "https://www.se.curriculum.chc.edu.tw/years/110/plans/239/views/4-1-1.pdf",
            "sourceKind": "public-school-course-plan-identifying-publisher-material",
            "locator": "彰化縣福興國中 110 學年度課程計畫；公開 PDF 明列康軒版國文第三、四冊課本及習作，將 Ab-Ⅳ-2 調整為常用字使用與語詞應用，並安排生活化學習單、問答、觀察與紙筆／口語替代評量；核讀 2026-09-20。",
            "accessedAt": "2026-09-20",
            "observedConcepts": ["常用字在詞語中的使用", "相近字詞的意義分辨", "由生活語境選擇恰當字詞"],
            "observedRepresentations": ["詞語與生活情境配對", "音近／形近字比較", "口語解釋與學習單記錄"],
            "observedAssessment": ["紙筆評量", "問答", "觀察", "學習單", "生活化口語評量"],
            "licenseBoundary": "只記錄公立學校課程計畫的教材版本、調整後學習重點與評量方向，不複製康軒教材、習作、題目或答案。",
        },
        {
            "publisher": "hanlin",
            "sourceUrl": "https://course.cyc.edu.tw/upfile/course110/sub1/14826950037937810.pdf",
            "sourceKind": "public-school-course-plan-identifying-publisher-material",
            "locator": "嘉義縣公立國民中學八年級第一學期國文領域教學計畫；公開 PDF 明列教材版本為翰林版國中國文八上，於各課同時列 Ab-Ⅳ-1 與 Ab-Ⅳ-2，透過課文討論、寫作／閱讀學習單、觀察與創作要求學生把字詞用在完整文本與表達中；核讀 2026-09-20。",
            "accessedAt": "2026-09-20",
            "observedConcepts": ["常用字在各類文本中的使用", "字詞選擇與句意、篇章主旨的關聯", "從閱讀理解轉為口語與書面表達"],
            "observedRepresentations": ["課文詞語與段落意義", "閱讀學習單和寫作手法記錄", "討論、觀察與創作成果"],
            "observedAssessment": ["課程討論", "寫作手法學習單", "觀察與創作", "口頭及書面表達"],
            "licenseBoundary": "只記錄公立學校課程計畫的教材版本、章節學習內容與評量方向，不複製翰林教材、學習單、題目或答案。",
        },
    ],
    "fusionReview": {
        "commonCore": [
            "三版本均要求把常用字放回詞語、句子或篇章中使用，不能只靠孤立字形或注音作答",
            "字詞選擇要由前後文、動作、對象與語氣等證據支持",
            "評量同時重視辨識結果、語境說明與實際表達",
        ],
        "differencesToReview": [
            "南一把常用字使用連到課文閱讀、口頭提問與習作練習",
            "康軒公開資源班課程更明確拆出生活化詞語應用、相近字詞分辨與替代評量方式",
            "翰林將常用字使用分散在各篇文本，以閱讀學習單、討論與創作檢查能否遷移到表達",
        ],
        "originalSynthesisBoundary": "本樣本只記錄三筆可追溯的公立學校章節級證據；lesson 正文、互動與題目仍須逐單元融合、內容／版權審查與 Terra 複核，維持 draft，不升級 publisher status。",
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
            blocker["reason"] = re.sub(r"Four hundred ten unit samples", "Four hundred eleven unit samples", reason)
    blocker_path.write_text(json.dumps(blockers, ensure_ascii=False, indent=2) + "\n", encoding="utf-8")
    print(json.dumps({"unitCount": data["unitCount"], "lessonId": SAMPLE["lessonId"]}, ensure_ascii=False))


if __name__ == "__main__":
    main()
