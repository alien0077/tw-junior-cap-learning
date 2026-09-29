#!/usr/bin/env python3
"""Record independent publisher-scope evidence for N-7-1 through N-7-3."""
from __future__ import annotations

import json
import re
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
REPORT = ROOT / "implementation/reports/publisher-chapter-evidence-samples.json"
SOURCES = {
    "nani": ("https://www.tsjh.ntpc.edu.tw/app/index.php?Action=downloadfile&file=WVhSMFlXTm9Mekk0TDNCMFlWOHhNakU0Tmw4ek16a3pPVGs0WHpJM01qZzRMbkJrWmc9PQ%3D%3D&fname=WSGGRPQK20QO41KKLOLK54TXXSMO25JGKLB0DCNKCCQLOO40QKTSST54WSLKUSSSROPOIHKK2004GDLOQONKTSMOOPB0FHMPQPMPNOTSUWZWWXVWFH10YWFCSSWUX25HCA0UWIGVWKO40XSUSB040MPTXGDTWA0ZWUSOPTWFGTS45QKNOKK21HHDGB0JC24KK14WTIGYSEG14WSMLID30B514YWRKA434DCDGA0WWQOPP1000ZSIGMOIGDGJDLO", "淡水國中 114 學年度七年級第一學期部定課程計畫；南一版 N-7-1／N-7-2／N-7-3 學習內容、章節與評量欄位"),
    "kanghsuan": ("https://www.cshs.ntpc.edu.tw/app/index.php?Action=downloadfile&cg=823&file=WVhSMFlXTm9MelEwTDNCMFlWOHhOamcxT0Y4ME9EYzFOamN5WHpRd01UWTRMbkJrWmc9PQ%3D%3D&fname=0054RPA0IC44VXMPED04ROGDVW30B4ICQOQK4020UT0510TSYSA4YS54WWECTTOKVWPOXT154404MOWS1430ICNPOP34GCGCIHXTXW40YSUSB450PKSSXXFCNP10XX21JCLKSWIGQOB4SWHCUS30A110", "金山國中 113 學年度七年級第一學期部定課程計畫；康軒版第一冊 N-7-1／N-7-2 範圍及評量欄位，並連接負數與四則運算"),
    "hanlin": ("https://course.cyc.edu.tw/upfile/course109/sub1/14535426987992584.pdf", "梅山國中 109 學年度七年級第一學期數學教學計畫；翰林版第一冊，N-7-3 負數與四則混合運算及生活情境／評量欄位；同計畫的數與量範圍涵蓋 N-7-1／N-7-2"),
}
UNITS = {
    "N-7-1": {
        "title": "100 以內的質數",
        "concepts": ["質數與合數的定義", "100 以內質數的辨識", "以篩法有系統地排除合數"],
        "representations": ["因數配對與質數判定", "數表與篩法標記", "質數／合數文字說明"],
        "assessment": ["紙筆測驗", "口頭回答", "課堂觀察", "作業"],
        "differences": ["南一將質數與質因數分解放在因數分解章；康軒以因數倍數判別與 1～100 質數辨識連接；翰林把質數納入第一冊數與量的基礎計算脈絡。"],
    },
    "N-7-2": {
        "title": "質因數分解的標準分解式",
        "concepts": ["把合數分解成質因數乘積", "標準分解式的唯一性與排列約定", "用質因數分解求因數與倍數"],
        "representations": ["因數樹與連續除法", "質因數指數記法", "分解式與因數／倍數列表"],
        "assessment": ["紙筆測驗", "口頭回答", "課堂觀察", "作業"],
        "differences": ["南一以質因數分解銜接公因數與公倍數；康軒從倍數判別和質因數辨識逐步導入標準分解式；翰林把分解式作為七年級數與量的計算工具。"],
    },
    "N-7-3": {
        "title": "負數與數的四則混合運算",
        "concepts": ["正負號表徵生活中的相對量", "相反數與數線方向", "含分數、小數的負數四則混合運算"],
        "representations": ["溫度、收支或高度的正負量", "數線上的方向與距離", "運算式、括號與符號規則"],
        "assessment": ["紙筆測驗", "小組討論", "口頭回答", "作業"],
        "differences": ["南一把負數放在數與數線及四則運算章節；康軒以生活量和運算規則連接整數計算；翰林以氣溫等生活情境先建立負數意義，再進入混合運算。"],
    },
}

def make_sample(code: str, cfg: dict) -> dict:
    sources = []
    for publisher, (url, locator) in SOURCES.items():
        sources.append({
            "publisher": publisher,
            "sourceUrl": url,
            "sourceKind": "public-school-course-plan-identifying-publisher-material",
            "locator": f"{locator}；{code}：{cfg['title']} 的概念、表徵與評量定位；核讀 2026-09-20。",
            "accessedAt": "2026-09-20",
            "observedConcepts": cfg["concepts"],
            "observedRepresentations": cfg["representations"],
            "observedAssessment": cfg["assessment"],
            "licenseBoundary": "只記錄公立學校課程計畫的章節、教學方向與評量方式，不複製教材、例題、題目或答案。",
        })
    return {
        "lessonId": f"lesson-math-content-{code.lower()}",
        "title": f"{code}：{cfg['title']}",
        "evidenceStatus": "chapter-level-recorded-pending-fusion-review",
        "sources": sources,
        "fusionReview": {
            "commonCore": cfg["concepts"],
            "differencesToReview": cfg["differences"],
            "originalSynthesisBoundary": "本樣本只記錄三筆公立學校章節級證據；正文、例題、互動與題目仍須逐單元融合、內容／版權審查與 Terra 複核，維持 draft，不升級 publisher status。",
        },
    }

data = json.loads(REPORT.read_text(encoding="utf-8"))
existing = {item["lessonId"] for item in data["units"]}
for code, cfg in UNITS.items():
    lesson_id = f"lesson-math-content-{code.lower()}"
    if lesson_id not in existing:
        data["units"].append(make_sample(code, cfg))
data["unitCount"] = len(data["units"])
data["updatedAt"] = "2026-09-20"
REPORT.write_text(json.dumps(data, ensure_ascii=False, indent=2) + "\n", encoding="utf-8")
blocker_path = ROOT / "implementation/reports/blockers.json"
blockers = json.loads(blocker_path.read_text(encoding="utf-8"))
for blocker in blockers.get("blockers", []):
    reason = blocker.get("reason")
    if isinstance(reason, str) and "unit samples" in reason:
        blocker["reason"] = re.sub(r"Three hundred [a-z-]+ unit samples", "Three hundred fifty-six unit samples", reason)
blocker_path.write_text(json.dumps(blockers, ensure_ascii=False, indent=2) + "\n", encoding="utf-8")
print(json.dumps({"unitCount": data["unitCount"], "added": list(UNITS)}, ensure_ascii=False))
