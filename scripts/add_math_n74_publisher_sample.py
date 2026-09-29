#!/usr/bin/env python3
"""Append the independently核讀 N-7-4 three-publisher evidence sample."""
from __future__ import annotations

import json
import re
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
REPORT = ROOT / "implementation/reports/publisher-chapter-evidence-samples.json"

SAMPLE = {
    "lessonId": "lesson-math-content-n-7-4",
    "title": "N-7-4：數的運算規律",
    "evidenceStatus": "chapter-level-recorded-pending-fusion-review",
    "sources": [
        {
            "publisher": "nani",
            "sourceUrl": "https://hakka.mtjh.kh.edu.tw/114plan/05/1/5-1-G-7.pdf",
            "sourceKind": "public-school-course-plan-identifying-publisher-material",
            "locator": "PDF p.1-2 / extracted lines 108-113 and 169-174; N-7-4 lists exchange, associative and distributive laws and signed-expression transformations; the same rows identify 南一 Nanibook／南一數學影音網／南一 Nanipaper.",
            "accessedAt": "2026-09-20",
            "observedConcepts": ["交換律與結合律", "分配律", "負號與括號內加減式的等價轉換"],
            "observedRepresentations": ["整數運算式", "括號與負號的符號轉換", "生活情境中的四則運算"],
            "observedAssessment": ["紙筆測驗", "互相討論", "口頭回答", "作業"],
            "licenseBoundary": "只記錄公立學校課程計畫的章節、教學方向與評量方式，不複製教材、例題、題目或答案。",
        },
        {
            "publisher": "kanghsuan",
            "sourceUrl": "https://www.dfsh.ntpc.edu.tw/app/index.php?Action=downloadfile&file=WVhSMFlXTm9MemMwTDNCMFlWOHlNak00WHpZNE56STJOMTg0TkRNNU9TNXdaR1k9&fname=WSGGIGB0MK10OOMP50POSWHGFC30WTIG14JCB114A1A1GCFCYSA4FCB4FGOOJG50VWPOXT154404MOWS1430ICNPOP34GCGCIHXTXW40YSUSB450PKSSXXFCNO10XX21JCLKSWIGQOB4SWHCUS30A110",
            "sourceKind": "public-school-course-plan-identifying-publisher-material",
            "locator": "PDF text extraction search hit N-7-4 in the 114學年度康軒版七年級數學課程計畫; the first-semester unit scope records exchange, associative and distributive laws, signed-expression transformations and contextual application; accessed 2026-09-20.",
            "accessedAt": "2026-09-20",
            "observedConcepts": ["交換律、結合律與分配律", "負數加減的括號與符號關係", "將運算規律用於生活情境"],
            "observedRepresentations": ["符號式與運算步驟", "正負數情境", "課本／習作／電子書的練習與反思"],
            "observedAssessment": ["紙筆測驗", "互相討論", "口頭回答", "作業"],
            "licenseBoundary": "只記錄公立學校課程計畫的章節、學習重點與評量方式，不複製康軒教材、題目或答案。",
        },
        {
            "publisher": "hanlin",
            "sourceUrl": "https://www.wsjh.ntpc.edu.tw/wp-content/uploads/doc/wsjh613/07_113-1%E7%BF%B0%E6%9E%97%E7%89%88_%E4%B8%83%E5%B9%B4%E7%B4%9A%E6%95%B8%E5%AD%B8.pdf",
            "sourceKind": "public-school-course-plan-identifying-publisher-material",
            "locator": "PDF text extraction search hit N-7-4 in the 113學年度翰林版七年級第一學期數學課程計畫; the weekly scope records exchange／associative／distributive laws, signed-expression transformations and paper-pencil／discussion assessment; accessed 2026-09-20.",
            "accessedAt": "2026-09-20",
            "observedConcepts": ["交換律與結合律的熟練運用", "分配律與整數運算簡化", "負號與括號轉換的條件判讀"],
            "observedRepresentations": ["數式改寫", "整數與生活量的正負表徵", "運算規律的口頭與紙筆說明"],
            "observedAssessment": ["紙筆測驗", "小組討論", "口頭回答", "作業"],
            "licenseBoundary": "只記錄公立學校課程計畫的章節與評量方向，不複製翰林教材、學習單、題目或答案。",
        },
    ],
    "fusionReview": {
        "commonCore": [
            "三版本均把交換律、結合律與分配律放在七年級整數運算脈絡中",
            "三版本均要求處理負號、括號與加減式的等價轉換",
            "三版本均以紙筆運算、討論或生活情境檢查運算規律能否遷移",
        ],
        "differencesToReview": [
            "南一在週次表中將符號轉換與正負數單元並列，並明列 Nanibook 與線上練習資源",
            "康軒把運算規律放入整數運算的反思與總結流程",
            "翰林強調乘除運算、計算機與課本／習作練習的連接",
        ],
        "originalSynthesisBoundary": "本樣本只記錄三筆公立學校課程計畫的章節級證據；lesson 正文、例題、互動與題目仍須完成逐單元版本融合、內容審查與 Terra 複核，維持 draft，不升級 publisher status。",
    },
}

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
        blocker["reason"] = re.sub(r"Three hundred [a-z-]+ unit samples", "Three hundred thirty-five unit samples", reason)
blocker_path.write_text(json.dumps(blockers, ensure_ascii=False, indent=2) + "\n", encoding="utf-8")
print(json.dumps({"unitCount": data["unitCount"], "lessonId": SAMPLE["lessonId"]}, ensure_ascii=False))
