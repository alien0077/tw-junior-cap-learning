#!/usr/bin/env python3
"""Record three public-school publisher-linked records for Chinese Ab-IV-1."""
from __future__ import annotations

import json
import re
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
REPORT = ROOT / "implementation/reports/publisher-chapter-evidence-samples.json"

SAMPLE = {
    "lessonId": "lesson-chinese-content-ab-iv-1",
    "title": "Ab-Ⅳ-1：4000常用字形音義",
    "evidenceStatus": "chapter-level-recorded-pending-fusion-review",
    "sources": [
        {
            "publisher": "nani",
            "sourceUrl": "https://course.cyc.edu.tw/upfile/course110/sub1/14793292177358929.pdf",
            "sourceKind": "public-school-course-plan-identifying-publisher-material",
            "locator": "嘉義縣大林國民中學九年級國文領域教學計畫；公開 PDF 明列教材版本為南一版國中國文，課程欄位列 Ab-Ⅳ-1 四千個常用字的字形、字音和字義，並以課文閱讀、口頭提問、習作練習與文本理解活動落實；核讀 2026-09-20。",
            "accessedAt": "2026-09-20",
            "observedConcepts": ["常用字的字形、字音與字義", "從課文語境辨識字詞", "由字詞理解連結篇章閱讀"],
            "observedRepresentations": ["字詞與課文語境對照", "字音字義的詞語辨識", "文本閱讀與口頭提問"],
            "observedAssessment": ["口頭提問", "習作練習", "課程討論", "文本閱讀理解"],
            "licenseBoundary": "只記錄公立學校課程計畫的教材版本、學習內容與評量方向，不複製南一教材正文、例題、題目或答案。",
        },
        {
            "publisher": "kanghsuan",
            "sourceUrl": "https://course.cyc.edu.tw/upfile/course110/sub1/14808877883833836.pdf",
            "sourceKind": "public-school-course-plan-identifying-publisher-material",
            "locator": "嘉義縣民和國民中學特殊教育國文領域教學計畫；公開 PDF 明列參考教材為康軒版國文第三、四冊，將 Ab-Ⅳ-1 調整為常用字形、字音、字義的辨識，並以紙筆、口頭問答、指認、觀察、分類與配對評量檢核；核讀 2026-09-20。",
            "observedConcepts": ["常用字形音義辨識", "一字多音與一字多義的判讀", "文字知識與篇章理解的連結"],
            "observedRepresentations": ["字形／字音／字義分類卡", "詞語配對與語境指認", "口語問答和紙筆作答"],
            "observedAssessment": ["紙筆測驗", "口頭問答", "指認", "觀察", "分類與配對"],
            "accessedAt": "2026-09-20",
            "licenseBoundary": "只記錄公立學校課程計畫的教材版本、調整後學習重點與評量方向，不複製康軒教材、習作、題目或答案。",
        },
        {
            "publisher": "hanlin",
            "sourceUrl": "https://course.cyc.edu.tw/upfile/course110/sub1/14826950037937810.pdf",
            "sourceKind": "public-school-course-plan-identifying-publisher-material",
            "locator": "嘉義縣公立國民中學八年級第一學期國文領域教學計畫；公開 PDF 明列教材版本為翰林版國中國文八上，於各課學習內容列 Ab-Ⅳ-1，並以課程討論、寫作／閱讀學習單、文本觀察與作品創作連結字詞辨識和篇章理解；核讀 2026-09-20。",
            "observedConcepts": ["常用字形音義在各類文本中的辨識", "字詞理解支援篇章主旨與表達", "由觀察、討論到作品輸出的語文運用"],
            "observedRepresentations": ["課文中的字詞與段落意義對照", "閱讀學習單與寫作手法記錄", "討論、觀察和創作成果"],
            "observedAssessment": ["課程討論", "寫作手法學習單", "大自然觀察與創作", "文本閱讀活動"],
            "accessedAt": "2026-09-20",
            "licenseBoundary": "只記錄公立學校課程計畫的教材版本、章節學習內容與評量方向，不複製翰林教材、學習單、題目或答案。",
        },
    ],
    "fusionReview": {
        "commonCore": [
            "三版本均把字形、字音、字義放在具體詞語或文本語境中辨識，而非只背單一讀音",
            "字詞知識要回到篇章理解、口語表達或書面輸出驗證",
            "評量需同時觀察辨識結果與學生說明線索的能力",
        ],
        "differencesToReview": [
            "南一公開課程計畫以課文閱讀、口頭提問與習作練習呈現字詞到篇章的連接",
            "康軒公開資源班課程把字形音義拆成可觀察的指認、分類、配對與口頭問答，並標示一字多音、多義的辨識需求",
            "翰林公開課程計畫將 Ab-Ⅳ-1 分散在各課文本，透過討論、學習單與創作把字詞理解轉成閱讀和表達成果",
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
            blocker["reason"] = re.sub(r"Four hundred nine unit samples", "Four hundred ten unit samples", reason)
    blocker_path.write_text(json.dumps(blockers, ensure_ascii=False, indent=2) + "\n", encoding="utf-8")
    print(json.dumps({"unitCount": data["unitCount"], "lessonId": SAMPLE["lessonId"]}, ensure_ascii=False))


if __name__ == "__main__":
    main()
