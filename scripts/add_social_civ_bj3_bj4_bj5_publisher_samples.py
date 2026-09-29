#!/usr/bin/env python3
"""Record public-school publisher-linked evidence for Civ Bj-IV-3, Bj-IV-4 and Bj-IV-5."""
from __future__ import annotations

import json
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
REPORT = ROOT / "implementation/reports/publisher-chapter-evidence-samples.json"
LICENSE = "只記錄公立學校課程計畫的版本、章節重點與評量方向，不複製教材、圖表、題目或答案。"
NANI = "https://www.jlsh.mlc.edu.tw/var/file/12/1012/img/113-2-8-4.pdf"
KANG = "https://cmsb.tc.edu.tw/var/file/89/1089/attach/5/pta_233170_327217_47876.pdf"
HANLIN = "https://course.cyc.edu.tw/upfile/course114/file_school/15952869896665246.pdf"

SAMPLES = [
    {
        "lessonId": "lesson-social-content-civ-bj-iv-3",
        "title": "公 Bj-Ⅳ-3：侵權行為的概念與責任",
        "core": [
            "侵權責任處理的是非契約關係中，行為造成他人權利或法益受損的法律責任；判斷時要分開行為、損害、因果關係與可歸責事由",
            "同一結果不必然代表行為人負侵權責任，還要檢查故意／過失、違法性、正當防衛或緊急避難等抗辯，以及損害是否能被證明",
            "用生活事故、網路侵害或財物損壞案例建立事實—權利—損害—因果—責任—救濟的分析鏈，避免把道德責備直接當作法律結論",
        ],
        "diff": [
            "南一把侵權行為放在民事糾紛解決途徑中，強調生活案例、權利受損與多元學習歷程",
            "康軒以民法責任和法律生活為脈絡，將侵權要件連結契約責任、法律責任與生活資料判讀",
            "翰林以民事責任章節處理侵權行為概念，安排紙筆、討論與問答，重視概念辨識及理由表達",
        ],
        "sources": [
            ("nani", NANI, "國立卓蘭高中附設國中部公立課程計畫；教材明載南一版，民事糾紛解決途徑單元列公 Bj-Ⅳ-3，採問答、觀察、實作、討論與學習歷程"),
            ("kanghsuan", KANG, "臺中市立啟明學校公立課程計畫；教材資源明載以康軒版社會領域課本為主要教材，學習內容列公 Bj-Ⅳ-3 侵權行為與責任"),
            ("hanlin", HANLIN, "嘉義縣阿里山公立課程計畫；教材明載翰林版第6冊，課程內容列公 Bj-Ⅳ-3 並以討論、紙筆、作業與課堂問答評量"),
        ],
        "representations": ["行為—損害—因果—可歸責要件鏈", "侵權責任與抗辯比較表", "民事請求與證據整理流程"],
        "assessment": ["侵權要件案例判讀", "契約責任與侵權責任比較", "損害與因果證據說明", "問答、討論、紙筆與學習歷程評量"],
    },
    {
        "lessonId": "lesson-social-content-civ-bj-iv-4",
        "title": "公 Bj-Ⅳ-4：智慧財產權與合理使用",
        "core": [
            "智慧財產權讓創作、發明與識別標誌在一定條件和期間內受到法律保護，目的在於平衡創作者利益、公共利用與知識流通",
            "合理使用不是看到『教育用途』就一律免責，仍要檢查使用目的、使用比例與重要性、對原作品市場的影響及適用的法律例外",
            "以圖片、音樂、影片、程式或網路文章的使用情境建立來源—授權—使用範圍—標示—風險檢核，練習提出合法替代方案",
        ],
        "diff": [
            "南一以法律與生活和資訊倫理脈絡引導智慧財產權，適合從日常創作與網路使用建立權利意識",
            "康軒將智慧財產權放入科技與法律生活交會處，明列著作、專利、商標及侵權責任的生活案例",
            "翰林以科技發展章節連結著作權、專利法與商標法，安排資料蒐集、課堂問答、心得與習作評量",
        ],
        "sources": [
            ("nani", NANI, "國立卓蘭高中附設國中部公立課程計畫；南一版公民課程將智慧財產權與法律／資訊生活脈絡連結，安排資料與討論活動"),
            ("kanghsuan", KANG, "臺中市立啟明學校公立課程計畫；主要教材明載康軒版，學習內容列公 Bj-Ⅳ-4 智慧財產權、合理使用與法律責任"),
            ("hanlin", HANLIN, "嘉義縣阿里山公立課程計畫；教材明載翰林版第6冊，科技發展章節列公 Bj-Ⅳ-4，涵蓋著作權、專利、商標與習作評量"),
        ],
        "representations": ["著作／專利／商標保護範圍比較表", "來源—授權—比例—市場影響檢核卡", "侵權風險與合法替代方案決策樹"],
        "assessment": ["智慧財產權類型辨識", "合理使用情境判讀", "授權與引用方案說明", "資料蒐集、課堂問答、心得與習作評量"],
    },
    {
        "lessonId": "lesson-social-content-civ-bj-iv-5",
        "title": "公 Bj-Ⅳ-5：民事紛爭的解決方式與優缺點",
        "core": [
            "民事紛爭的處理方式可包括協商、調解、仲裁與訴訟，各自的第三方介入程度、程序正式性、成本、時間、結果拘束力與公開程度不同",
            "選擇解決方式要先界定爭議事實、證據與需求，再比較是否需要保全關係、快速終結、取得可執行結果或建立法律判決，不能只以『誰贏』判斷好壞",
            "以同一民事案例模擬不同程序，製作利弊矩陣與決策建議，理解當事人自主、程序公平與司法救濟的關係",
        ],
        "diff": [
            "南一以民事糾紛解決途徑結合問答、資料蒐集與學習歷程，強調從生活問題提出處理方案",
            "康軒以民事紛爭與法治生活脈絡介紹協商、調解、仲裁及訴訟的差異，使用生活資料和多元評量",
            "翰林把民事紛爭放在民事責任與訴訟章節，連結權利救濟、方法優缺點及討論／紙筆檢核",
        ],
        "sources": [
            ("nani", NANI, "國立卓蘭高中附設國中部公立課程計畫；教材明載南一版，民事糾紛解決途徑單元列公 Bj-Ⅳ-5，採問答、觀察、實作、討論與學習歷程"),
            ("kanghsuan", KANG, "臺中市立啟明學校公立課程計畫；主要教材明載康軒版，學習內容列公 Bj-Ⅳ-5 民事紛爭及各解決方法優缺點"),
            ("hanlin", HANLIN, "嘉義縣阿里山公立課程計畫；教材明載翰林版，民事法律脈絡列公 Bj-Ⅳ-5，安排分組討論、紙筆、作業、問答與心得"),
        ],
        "representations": ["協商／調解／仲裁／訴訟比較矩陣", "爭議事實—證據—需求—程序選擇流程", "成本、時間、拘束力與關係維持雷達表"],
        "assessment": ["民事解決方式分類", "程序優缺點資料判讀", "依需求提出程序選擇理由", "分組討論、紙筆、作業、問答與心得報告"],
    },
]


def main() -> None:
    data = json.loads(REPORT.read_text(encoding="utf-8"))
    existing = {item["lessonId"] for item in data["units"]}
    added = []
    for sample in SAMPLES:
        records = []
        for publisher, url, locator in sample["sources"]:
            records.append({
                "publisher": publisher,
                "sourceUrl": url,
                "sourceKind": "public-school-course-plan-identifying-publisher-material",
                "locator": f"{locator}；核讀 2026-09-21。",
                "accessedAt": "2026-09-21",
                "observedConcepts": sample["core"],
                "observedRepresentations": sample["representations"],
                "observedAssessment": sample["assessment"],
                "licenseBoundary": LICENSE,
            })
        record = {
            "lessonId": sample["lessonId"],
            "title": sample["title"],
            "evidenceStatus": "chapter-level-recorded-pending-fusion-review",
            "sources": records,
            "fusionReview": {
                "commonCore": sample["core"],
                "differencesToReview": sample["diff"],
                "originalSynthesisBoundary": "逐單元融合、內容／版權審查與 Terra 複核前維持 draft，不升級 publisher status。",
            },
        }
        if record["lessonId"] not in existing:
            data["units"].append(record)
            added.append(record["lessonId"])
    data["unitCount"] = len(data["units"])
    data["updatedAt"] = "2026-09-21"
    REPORT.write_text(json.dumps(data, ensure_ascii=False, indent=2) + "\n", encoding="utf-8")
    blockers_path = ROOT / "implementation/reports/blockers.json"
    blockers = json.loads(blockers_path.read_text(encoding="utf-8"))
    for blocker in blockers.get("blockers", []):
        reason = blocker.get("reason")
        if isinstance(reason, str):
            blocker["reason"] = reason.replace("Four hundred ninety-five unit samples", "Four hundred ninety-eight unit samples")
    blockers_path.write_text(json.dumps(blockers, ensure_ascii=False, indent=2) + "\n", encoding="utf-8")
    print(json.dumps({"unitCount": data["unitCount"], "added": added}, ensure_ascii=False))


if __name__ == "__main__":
    main()
