#!/usr/bin/env python3
"""Record three public-school publisher-linked records for Civ Da-IV-1."""
from __future__ import annotations

import json
import re
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
REPORT = ROOT / "implementation/reports/publisher-chapter-evidence-samples.json"
SOURCES = {
    "nani": ("https://www.jlsh.mlc.edu.tw/var/file/12/1012/img/113-2-7-4.pdf", "國立卓蘭高中附設國中部 113 學年度七年級社會領域；單元 2 性別平權／公民，使用南一版教科書，明列公 Da-IV-1 日常生活中的公平例子及判斷原則，並採口頭問答、觀察、上機實作、討論及學習歷程評量。"),
    "kanghsuan": ("https://cmsb.tc.edu.tw/var/file/89/1089/attach/30/pta_72815_9642405_34898.pdf", "臺中市立啟明學校國民教育階段課程計畫；學習內容明列公 Da-Ⅳ-1 日常生活中的公平例子與判斷原則，教材資源明載以國中康軒版社會領域課本為主要教材，並安排生活資料、討論、觀察、口問與紙筆等多元評量。"),
    "hanlin": ("https://www.ckjhs.ntpc.edu.tw/app/index.php?Action=downloadfile&file=WVhSMFlXTm9MelU0TDNCMFlWODJNakU1WHpZNU1USXlNREJmTkRJMU1qTXVjR1Jt&fname=WSGGXSQKRKDCOOOYXLOLKWWXTZSPKWTRL14JCB114A1A1GCFCYSA4FCB4FGOOJG50VWPOXT154404MOWS1430ICNPOP34XSGC01YTNOB5WSB001PODGGGQKUSTWPOXXKKVSNOXWXTMKJCUSIC14JCSW20HDNPMLRKLKUSOPTWQOA4TS50DGQO210024LKNOWTVW30LKKKWSNORKMP21XTLKB5POMKOPB400SSPKROKK04POPO", "新北市立溪崑國民中學 114 學年度七年級第二學期部定課程計畫；公平正義章節明列公 Da-IV-1，教材資源標示翰林版教科書，從平等取得機會、資源與弱勢照顧的案例討論公平原則，並採課堂觀察、學習單與隨堂測驗。"),
}
CONCEPTS = ["從分配結果、程序、機會與需求等角度辨識日常情境中的公平與不公平", "比較平等分配、依貢獻分配、依需求補助與程序正義，說明不同原則適用的條件與限制", "用案例中的身分、規則、資源與結果提出有證據的判斷，並檢查是否忽略弱勢者的實際障礙"]
REPRESENTATIONS = ["案例身分—規則—資源—結果四欄分析表", "公平原則與情境條件的對照矩陣", "機會、程序、結果與需求補助的決策流程圖"]
ASSESSMENT = ["生活公平案例閱讀", "原則套用與理由說明", "多觀點課堂討論", "學習單資料分析", "紙筆或隨堂測驗"]


def main() -> None:
    records = []
    for publisher, (url, locator) in SOURCES.items():
        records.append({"publisher": publisher, "sourceUrl": url, "sourceKind": "public-school-course-plan-identifying-publisher-material", "locator": f"{locator} 核讀 2026-09-20。", "accessedAt": "2026-09-20", "observedConcepts": CONCEPTS, "observedRepresentations": REPRESENTATIONS, "observedAssessment": ASSESSMENT, "licenseBoundary": "只記錄公立學校課程計畫的章節、學習重點與評量方向，不複製教材、影片、圖表、題目或答案。"})
    record = {"lessonId": "lesson-social-content-civ-da-iv-1", "title": "公 Da-Ⅳ-1：日常公平原則", "evidenceStatus": "chapter-level-recorded-pending-fusion-review", "sources": records, "fusionReview": {"commonCore": CONCEPTS, "differencesToReview": ["南一以性別平權單元從生活經驗辨識公平與不公平，需融合不同群體與規範變動的視角。", "康軒以特殊教育課程將公平概念調整為具體生活材料，需保留原則判斷又避免把簡化案例誤當完整公民論證。", "翰林以公平正義章節處理平等機會、資源與弱勢照顧，並以 ORID／資料討論引導理由表達。"], "originalSynthesisBoundary": "本樣本只記錄三筆公立學校章節級證據；lesson 正文、圖表、互動與題目仍須逐單元融合、內容／版權審查與 Terra 複核，維持 draft，不升級 publisher status。"}}
    data = json.loads(REPORT.read_text(encoding="utf-8")); existing = {item["lessonId"] for item in data["units"]}; added = []
    if record["lessonId"] not in existing:
        data["units"].append(record)
        added.append(record["lessonId"])
    data["unitCount"] = len(data["units"])
    data["updatedAt"] = "2026-09-20"
    REPORT.write_text(json.dumps(data, ensure_ascii=False, indent=2) + "\n", encoding="utf-8")
    blockers_path = ROOT / "implementation/reports/blockers.json"
    blockers = json.loads(blockers_path.read_text(encoding="utf-8"))
    for blocker in blockers.get("blockers", []):
        reason = blocker.get("reason")
        if isinstance(reason, str) and "unit samples" in reason:
            blocker["reason"] = re.sub(r"Three hundred [a-z-]+ unit samples", "Three hundred eighty-nine unit samples", reason)
    blockers_path.write_text(json.dumps(blockers, ensure_ascii=False, indent=2) + "\n", encoding="utf-8")
    print(json.dumps({"unitCount": data["unitCount"], "added": added}, ensure_ascii=False))


if __name__ == "__main__":
    main()
