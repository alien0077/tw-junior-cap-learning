#!/usr/bin/env python3
"""Record independently checked public-school publisher-scope evidence for A-7-1."""
from __future__ import annotations

import json
import re
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
REPORT = ROOT / "implementation/reports/publisher-chapter-evidence-samples.json"

SAMPLE = {
    "lessonId": "lesson-math-content-a-7-1",
    "title": "A-7-1：代數符號",
    "evidenceStatus": "chapter-level-recorded-pending-fusion-review",
    "sources": [
        {
            "publisher": "nani",
            "sourceUrl": "https://www.tsjh.ntpc.edu.tw/app/index.php?Action=downloadfile&file=WVhSMFlXTm9Mekk0TDNCMFlWOHhNakU0Tmw4ek16a3pPVGs0WHpJM01qZzRMbkJrWmc9PQ%3D%3D&fname=WSGGRPQK20QO41KKLOLK54TXXSMO25JGKLB0DCNKCCQLOO40QKTSST54WSLKUSSSROPOIHKK2004GDLOQONKTSMOOPB0FHMPQPMPNOTSUWZWWXVWFH10YWFCSSWUX25HCA0UWIGVWKO40XSUSB040MPTXGDTWA0ZWUSOPTWFGTS45QKNOKK21HHDGB0JC24KK14WTIGYSEG14WSMLID30B514YWRKA434DCDGA0WWQOPP1000ZSIGMOIGDGJDLO",
            "sourceKind": "public-school-course-plan-identifying-publisher-material",
            "locator": "新北市立淡水國中 114 學年度七年級第一學期部定課程計畫；公開 PDF 的 A-7-1 欄位明列南一版教科書，並以符號表徵交換律、分配律、結合律、化簡同類項與生活情境列式；核讀 2026-09-20。",
            "accessedAt": "2026-09-20",
            "observedConcepts": ["文字符號代表數量", "一次式的化簡與同類項", "從生活敘述建立代數式"],
            "observedRepresentations": ["文字敘述與代數式互換", "運算律的符號表徵", "代入特定數值檢查式子的意義"],
            "observedAssessment": ["紙筆測驗", "口頭回答", "討論", "作業"],
            "licenseBoundary": "只記錄公立學校課程計畫的章節、教學方向與評量方式，不複製教材、例題、題目或答案。",
        },
        {
            "publisher": "kanghsuan",
            "sourceUrl": "https://www.cshs.ntpc.edu.tw/app/index.php?Action=downloadfile&cg=823&file=WVhSMFlXTm9MelEwTDNCMFlWOHhOamcxT0Y4ME9EYzFOamN5WHpRd01UWTRMbkJrWmc9PQ%3D%3D&fname=0054RPA0IC44VXMPED04ROGDVW30B4ICQOQK4020UT0510TSYSA4YS54WWECTTOKVWPOXT154404A0WSST14MOICB0RKMP1444VXXWA0SWMKGHFGUSCCYWFC0040DDKKB0LKUWLOVWTWWSB0403541GDQPMLA0B4ZSFGOOLK30DGRKPO2125HC04MOIGTW14JDRLOPEGFHMOUTXT30FCUW30JGLLUSDC0150RKKKXX0150HGWTHGDCTW25LKFGB0UW10GGFDA0VSKPNO1145",
            "sourceKind": "public-school-course-plan-identifying-publisher-material",
            "locator": "新北市立金山國中 113 學年度七年級第一學期部定課程計畫；公開 PDF 第 16 頁附近的 A-7-1／3-1 代數式的化簡欄位明列康軒版第一冊課本與紙筆、作業評量；核讀 2026-09-20。",
            "accessedAt": "2026-09-20",
            "observedConcepts": ["利用運算規則化簡代數式", "交換律、結合律與分配律的符號運用", "設定文字符號數值後計算式值"],
            "observedRepresentations": ["代數式與運算步驟", "係數、常數項與同類項", "文字情境轉為符號式"],
            "observedAssessment": ["紙筆測驗", "作業"],
            "licenseBoundary": "只記錄公立學校課程計畫的章節、教學方向與評量方式，不複製康軒教材、題目或答案。",
        },
        {
            "publisher": "hanlin",
            "sourceUrl": "https://www.msjh.tp.edu.tw/uploads/1755572578742THrRJJpw.pdf",
            "sourceKind": "public-school-course-plan-identifying-publisher-material",
            "locator": "臺北市立民生國中 114 學年度七年級資源班數學課程計畫；公開 PDF p.1 明列翰林版七年級數學，A-7-1-1～A-7-1-3 分列運算律、一次式化簡／同類項與生活情境；核讀 2026-09-20。",
            "accessedAt": "2026-09-20",
            "observedConcepts": ["運算律的代數符號表徵", "一次式化簡與同類項", "生活情境的代數建模"],
            "observedRepresentations": ["交換律、分配律、結合律的文字與符號對照", "一次式的項與係數", "生活量與代數符號的對應"],
            "observedAssessment": ["口語評量", "觀察評量", "實作評量", "紙筆測驗"],
            "licenseBoundary": "只記錄公立學校課程計畫的章節與評量方向，不複製翰林教材、學習單、題目或答案。",
        },
    ],
    "fusionReview": {
        "commonCore": [
            "三版本均要求用符號代表數量並理解文字式的意義",
            "三版本均涵蓋運算律、一次式化簡與同類項",
            "三版本均把代數式帶回情境或以評量檢查表徵與運算是否一致",
        ],
        "differencesToReview": [
            "南一的公開課程計畫較突出文字敘述、代入與生活列式的連接",
            "康軒以 3-1 代數式化簡安排運算規則與紙筆／作業檢核",
            "翰林將 A-7-1 拆成運算律、化簡同類項與生活情境三個細目，並納入口語、觀察與實作評量",
        ],
        "originalSynthesisBoundary": "本樣本只記錄三筆公立學校章節級證據；lesson 正文、例題、互動與題目仍須完成逐單元版本融合、內容審查與 Terra 複核，維持 draft，不升級 publisher status。",
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
        blocker["reason"] = re.sub(r"Three hundred [a-z-]+ unit samples", "Three hundred forty unit samples", reason)
blocker_path.write_text(json.dumps(blockers, ensure_ascii=False, indent=2) + "\n", encoding="utf-8")
print(json.dumps({"unitCount": data["unitCount"], "lessonId": SAMPLE["lessonId"]}, ensure_ascii=False))
