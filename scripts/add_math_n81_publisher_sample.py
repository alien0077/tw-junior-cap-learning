#!/usr/bin/env python3
from __future__ import annotations

import json
import re
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
REPORT = ROOT / "implementation/reports/publisher-chapter-evidence-samples.json"
SOURCES = [
    {
        "publisher": "nani",
        "sourceUrl": "https://www.jlsh.mlc.edu.tw/var/file/12/1012/img/113-2-8-3.pdf",
        "locator": "PDF 113學年度八年級數學課程計畫；N-8-1列於第九週 2-2 根式的運算，教材欄明列南一版教科書、教師手冊與學習單。",
        "concepts": ["二次方根的意義", "根式化簡", "根式四則運算"],
        "representations": ["根號與平方的反運算", "最簡根式", "根式運算式"],
        "assessment": ["口頭回答", "討論", "作業", "操作", "紙筆測驗"],
    },
    {
        "publisher": "kanghsuan",
        "sourceUrl": "https://hakka.mtjh.kh.edu.tw/114plan/05/1/5-1-G-8.pdf",
        "locator": "PDF p.1-2／114學年度八年級數學課程計畫；第二章平方根與畢氏定理的 2-1 平方根與近似值列出 N-8-1，線上平台明列康軒數學影音頻道。",
        "concepts": ["平方根與面積模型的連結", "根式的化簡與運算", "以近似值與計算機驗證根式結果"],
        "representations": ["正方形面積—邊長模型", "根號符號", "計算機近似與代數結果對照"],
        "assessment": ["口頭回答", "討論", "作業", "操作", "紙筆測驗"],
    },
    {
        "publisher": "hanlin",
        "sourceUrl": "https://www.wsjh.ntpc.edu.tw/app/index.php?Action=downloadfile&cg=836&file=WVhSMFlXTm9Memt2Y0hSaFh6RTNNRE5mTlRjeE1UVTROVjgxTXpBNU55NXdaR1k9&fname=WW54RPOKLOSSYX15A404JGWTRK30B4ICRKNOUWMPUTGDYXEGROB4EGLLQOHGJGWXWW00UTZXB0B0A020MOXSMO35WSROMKGC01RL00QPNKTS50SW50SS01XXRKLKCDMLDGA0NOXTRKHCDC20USB004NPVXGDB0SSSSNKECFGFG54GHQKWWWSUT0544EGLKGDMOOKWTMOYSEG14WSMLID30B514YWJGA4PKDCXW50WW10NPYXIGXS30ZWVWB4NPLKYSUWXSYS00IDCCQPUW20EG54LOKB14135ML4414NO1111",
        "locator": "PDF 114學年度八年級第一學期課程計畫；第六至第九週 N-8-1列出根式意義、最簡根式、質因數分解化簡、根式乘除加減與有理化分母，教材／評量欄含翰林教具、紙筆測驗與口頭回答。",
        "concepts": ["由正方形面積引入根號", "最簡根式與質因數分解", "根式加減、乘除與有理化分母"],
        "representations": ["面積幾何模型", "標準分解式與根式", "平方差公式的有理化步驟"],
        "assessment": ["紙筆測驗", "觀察", "口頭回答", "資料蒐集", "作業繳交"],
    },
]

sample = {
    "lessonId": "lesson-math-content-n-8-1",
    "title": "N-8-1：二次方根",
    "evidenceStatus": "chapter-level-recorded-pending-fusion-review",
    "sources": [
        {
            "publisher": s["publisher"],
            "sourceUrl": s["sourceUrl"],
            "sourceKind": "public-school-course-plan-identifying-publisher-material",
            "locator": s["locator"] + " 核讀 2026-09-20。",
            "accessedAt": "2026-09-20",
            "observedConcepts": s["concepts"],
            "observedRepresentations": s["representations"],
            "observedAssessment": s["assessment"],
            "licenseBoundary": "只記錄公立學校課程計畫的章節、教學方向與評量方式，不複製教材、例題、題目或答案。",
        }
        for s in SOURCES
    ],
    "fusionReview": {
        "commonCore": ["二次方根由平方的反運算定義", "根式可透過完全平方因數化簡", "根式四則運算需保留定義域與等價性檢查"],
        "differencesToReview": ["南一以課程週次與根式運算教材範圍定位", "康軒以正方形面積、近似值與計算機操作連接根式概念", "翰林明列最簡根式、質因數分解、加減乘除與有理化分母的活動序列"],
        "originalSynthesisBoundary": "本樣本只證明三筆公立學校章節級證據已記錄；正文、例題、互動與題目仍須逐單元融合、內容／版權審查與 Terra 複核，維持 draft，不升級 publisher status。",
    },
}

data = json.loads(REPORT.read_text(encoding="utf-8"))
if not any(x.get("lessonId") == sample["lessonId"] for x in data["units"]):
    data["units"].append(sample)
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
print(json.dumps({"unitCount": data["unitCount"], "lessonId": sample["lessonId"]}, ensure_ascii=False))
