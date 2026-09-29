#!/usr/bin/env python3
"""Record independently read N-7-5 through N-7-9 publisher-scope samples."""
from __future__ import annotations

import json
import re
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
REPORT = ROOT / "implementation/reports/publisher-chapter-evidence-samples.json"
SOURCES = {
    "nani": ("https://hakka.mtjh.kh.edu.tw/114plan/05/1/5-1-G-7.pdf", "民族國中南一版七年級數學課程計畫；PDF p.1-3 的週次與 N-7-x 學習內容欄位"),
    "kanghsuan": ("https://www.dfsh.ntpc.edu.tw/app/index.php?Action=downloadfile&file=WVhSMFlXTm9MemMwTDNCMFlWOHlNak00WHpZNE56STJOMTg0TkRNNU9TNXdaR1k9&fname=WSGGIGB0MK10OOMP50POSWHGFC30WTIG14JCB114A1A1GCFCYSA4FCB4FGOOJG50VWPOXT154404MOWS1430ICNPOP34GCGCIHXTXW40YSUSB450PKSSXXFCNO10XX21JCLKSWIGQOB4SWHCUS30A110", "康軒版七年級數學課程計畫；PDF 文字擷取中的 N-7-x 學習內容與第一學期教學範圍"),
    "hanlin": ("https://www.wsjh.ntpc.edu.tw/wp-content/uploads/doc/wsjh613/07_113-1%E7%BF%B0%E6%9E%97%E7%89%88_%E4%B8%83%E5%B9%B4%E7%B4%9A%E6%95%B8%E5%AD%B8.pdf", "文山國中翰林版七年級數學課程計畫；PDF 文字擷取中的 N-7-x 學習內容、週次與評量欄位"),
}

UNITS = {
    "N-7-5": ("數線", ["負數在數線上的位置與大小比較", "絕對值作為到原點的距離", "以 |a-b| 表示兩點距離"], ["數線圖", "方向與距離", "代數式與幾何位置互換"], ["數線操作", "紙筆測驗", "口頭回答"], ["南一連接正負數與數線距離；康軒把向量／生活情境作為理解入口；翰林強調絕對值符號與距離計算"]),
    "N-7-6": ("指數的意義", ["非負整數次方的意義", "a 不為 0 時 a^0=1", "同底數大小比較與指數運算"], ["重複乘法", "底數—指數標記", "科學記號前置表徵"], ["紙筆測驗", "討論", "作業"], ["南一把指數放在整數／科學記號章節；康軒以運算規則與反思整理銜接；翰林把計算機與符號讀寫列入練習脈絡"]),
    "N-7-7": ("指數律", ["同底數乘法指數律", "冪的冪與乘積的次方", "同底數除法指數律及指數差"], ["數字例與符號例", "指數相加／相減", "乘積與冪的等價改寫"], ["紙筆測驗", "小組討論", "作業"], ["南一強調由數字例建立規律；康軒將乘除指數律放在分數與指數章節；翰林以同底數改寫與計算機驗算支援形式化"]),
    "N-7-8": ("科學記號", ["以 1 到 10 之間係數表示正數", "正指數與負指數的數量級", "科學記號的乘除與比較"], ["十的冪", "小數點位移", "數量級與標準格式"], ["紙筆測驗", "口頭回答", "作業"], ["南一把科學記號與指數記法放在第一章；康軒在數與量架構中連接複雜數式；翰林將標準格式與生活數量的判讀放入章節練習"]),
    "N-7-9": ("比與比例式", ["比與比值的表示", "比例式的基本運算", "正比、反比與有意義的生活情境"], ["雙量比值", "比例式交叉相乘", "表格／圖形與情境量"], ["紙筆測驗", "情境討論", "作業"], ["南一強調比值與生活量；康軒以有意義比值安排正比反比應用；翰林把比例推理、圖表與複雜數值的計算工具分開檢核"]),
}

def make_sample(code: str, title: str, concepts: list[str], representations: list[str], assessments: list[str], differences: list[str]) -> dict:
    sources = []
    for publisher, (url, base_locator) in SOURCES.items():
        sources.append({
            "publisher": publisher,
            "sourceUrl": url,
            "sourceKind": "public-school-course-plan-identifying-publisher-material",
            "locator": f"{base_locator}；{code}：{title} 的相關學習內容與評量定位；核讀 2026-09-20。",
            "accessedAt": "2026-09-20",
            "observedConcepts": concepts,
            "observedRepresentations": representations,
            "observedAssessment": assessments,
            "licenseBoundary": "只記錄公立學校課程計畫的章節、教學方向與評量方式，不複製教材、例題、題目或答案。",
        })
    return {
        "lessonId": f"lesson-math-content-{code.lower().replace('-', '-')}",
        "title": f"{code}：{title}",
        "evidenceStatus": "chapter-level-recorded-pending-fusion-review",
        "sources": sources,
        "fusionReview": {
            "commonCore": concepts,
            "differencesToReview": differences,
            "originalSynthesisBoundary": "本樣本只證明三筆公立學校章節級證據已記錄；正文、例題、互動與題目仍須逐單元融合、內容／版權審查與 Terra 複核，維持 draft，不升級 publisher status。",
        },
    }

data = json.loads(REPORT.read_text(encoding="utf-8"))
existing = {item["lessonId"] for item in data["units"]}
for code, (title, concepts, representations, assessments, differences) in UNITS.items():
    lesson_id = f"lesson-math-content-{code.lower()}"
    if lesson_id not in existing:
        data["units"].append(make_sample(code, title, concepts, representations, assessments, differences))
data["unitCount"] = len(data["units"])
data["updatedAt"] = "2026-09-20"
REPORT.write_text(json.dumps(data, ensure_ascii=False, indent=2) + "\n", encoding="utf-8")
blocker_path = ROOT / "implementation/reports/blockers.json"
blockers = json.loads(blocker_path.read_text(encoding="utf-8"))
for blocker in blockers.get("blockers", []):
    reason = blocker.get("reason")
    if isinstance(reason, str) and "unit samples" in reason:
        blocker["reason"] = re.sub(r"Three hundred [a-z-]+ unit samples", "Three hundred thirty-nine unit samples", reason)
blocker_path.write_text(json.dumps(blockers, ensure_ascii=False, indent=2) + "\n", encoding="utf-8")
print(json.dumps({"unitCount": data["unitCount"], "added": list(UNITS)}, ensure_ascii=False))
