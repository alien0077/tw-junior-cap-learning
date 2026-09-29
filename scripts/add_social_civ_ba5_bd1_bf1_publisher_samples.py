#!/usr/bin/env python3
"""Record public-school publisher-linked evidence for Civ Ba-IV-5, Bd-IV-1 and Bf-IV-1."""
from __future__ import annotations

import json
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
REPORT = ROOT / "implementation/reports/publisher-chapter-evidence-samples.json"
LICENSE = "只記錄公立學校課程計畫的版本、章節重點與評量方向，不複製教材、圖表、題目或答案。"

SOURCES = {
    "nani": "https://course.cyc.edu.tw/upfile/course109/sub1/14535426760482702.pdf",
    "kanghsuan": "https://course.cyc.edu.tw/upfile/course114/file_school/15952869896665246.pdf",
    "hanlin_ba5": "https://www.fljh.hc.edu.tw/uploads/1754456224257QKHVY0qn.pdf",
    "hanlin_bd1": "https://course.cyc.edu.tw/upfile/course114/sub1/15939200304379868.pdf",
    "hanlin_bf1": "https://www.ctbc.ntpc.edu.tw/wp-content/uploads/2025/09/%E7%BF%B0%E6%9E%97%E7%89%88_%E5%85%AB%E5%B9%B4%E7%B4%9A%E7%A4%BE%E6%9C%83%E5%85%AC%E6%B0%91.pdf",
}

SAMPLES = [
    {
        "lessonId": "lesson-social-content-civ-ba-iv-5",
        "title": "公 Ba-Ⅳ-5：家庭中的權利與義務及家庭平權",
        "core": [
            "家庭平權不是把每個人的責任切成相同份量，而是讓家庭成員不因性別、年齡或身分被預設只能做某些事，並能在安全、尊重與可協商的條件下共同決定",
            "判斷家庭權利義務要區分法律保障、照顧責任、家務分工與個人意願，不能把傳統習慣直接當成正當規範",
            "以家庭分工紀錄、法律／制度摘要與角色觀點討論如何辨識不平等、協商改變並尋求支持",
        ],
        "diff": [
            "南一課程計畫把公 Ba-Ⅳ-5 放在平權家庭脈絡，強調性別平等與家庭互動中的權利義務",
            "康軒課程計畫以家庭權利義務、性別角色與日常分工案例連結生活判讀與討論",
            "翰林課程計畫把家庭平權安排在家庭生活單元，從家庭間的權利義務延伸到多樣家庭與制度支持",
        ],
        "sources": [
            ("nani", SOURCES["nani"], "嘉義縣公立國中南一版課程計畫；公 Ba-Ⅳ-5 與平權家庭、家庭權利義務及性別平等脈絡並列"),
            ("kanghsuan", SOURCES["kanghsuan"], "嘉義縣公立國中康軒版課程計畫；公 Ba-Ⅳ-5 的家庭平權、性別角色與生活分工安排"),
            ("hanlin", SOURCES["hanlin_ba5"], "新竹市公立國中翰林版課程計畫；教材明載翰林版，課程目標明列家庭間權利義務與落實家庭平權"),
        ],
        "representations": ["家庭分工時數與決策權比較表", "權利／義務／支持資源三欄案例卡", "家庭衝突的觀點—證據—協商流程"],
        "assessment": ["家庭分工資料判讀", "權利義務與性別刻板印象辨識", "角色立場口頭說明", "協商方案學習單", "討論、口頭與紙筆評量"],
    },
    {
        "lessonId": "lesson-social-content-civ-bd-iv-1",
        "title": "公 Bd-Ⅳ-1：國家與政府的區別",
        "core": [
            "國家是由人民、領土、政府與主權等要素構成的政治共同體；政府是負責統治、管理公共事務與行使公權力的組織，兩者不能互換",
            "辨識政府變動與國家持續的差異，要同時檢查組成要素、主權歸屬、公共功能與制度責任",
            "用國家要素表、政府機關案例與國際／地方資料，說明政府如何代表國家行使權力以及為何仍須受法律與人民監督",
        ],
        "diff": [
            "南一課程計畫由國家構成與公共治理切入，適合先建立四要素與政府功能的分類基礎",
            "康軒課程計畫把國家、政府、主權與公共政策安排在民主政治脈絡，著重概念辨析和生活案例",
            "翰林課程計畫明列人民、領土、政府、主權四要素與國家主要功能，並以討論和課堂問答檢核理解",
        ],
        "sources": [
            ("nani", SOURCES["nani"], "嘉義縣公立國中南一版課程計畫；國家組成、政府功能與公 Bd-Ⅳ-1 的國家／政府辨析"),
            ("kanghsuan", SOURCES["kanghsuan"], "嘉義縣公立國中康軒版課程計畫；公 Bd-Ⅳ-1 與國家治理、政府組織及公共權力脈絡並列"),
            ("hanlin", SOURCES["hanlin_bd1"], "國立嘉科實驗高中國中部公立課程計畫；教材明載翰林版第3冊，公 Bd-Ⅳ-1 明列國家四要素與主要功能"),
        ],
        "representations": ["國家四要素檢核表", "國家／政府／機關三層概念圖", "政府更替但國家延續的時間線與案例卡"],
        "assessment": ["概念分類與反例辨識", "國家要素資料判讀", "政府功能案例解釋", "小組討論、課堂問答與紙筆測驗"],
    },
    {
        "lessonId": "lesson-social-content-civ-bf-iv-1",
        "title": "公 Bf-Ⅳ-1：法治與人治的差異",
        "core": [
            "人治以統治者或少數人的意志決定公共規則，規則可能隨人變動；法治要求政府與人民都受公開、一般、可預期且符合正當程序的法律拘束",
            "判斷一個情境是否接近法治，不能只看是否有法律文字，還要檢查法律是否平等適用、權力是否受限制、人民是否有救濟與監督途徑",
            "從校園規範、行政措施與新聞式資料建立規則—權力—權利—救濟的因果鏈，辨識以個人好惡取代程序的風險",
        ],
        "diff": [
            "南一課程計畫以民主政治中的權利保障與法治觀念建立人治／法治對照，需保留人民監督與權利救濟",
            "康軒課程計畫以法治社會單元連接法律位階、權力限制與生活事件，適合用規範層級和案例比較",
            "翰林課程計畫明列人治、法治與權力／權利差異，使用新聞情境、分組討論、紙筆測驗與課堂觀察",
        ],
        "sources": [
            ("nani", SOURCES["nani"], "嘉義縣公立國中南一版課程計畫；法治／人治、人民權利保障與民主政治脈絡"),
            ("kanghsuan", SOURCES["kanghsuan"], "嘉義縣公立國中康軒版課程計畫；教材明載康軒版第3冊，公 Bf-Ⅳ-1 以法治、人治、權利與權力案例安排"),
            ("hanlin", SOURCES["hanlin_bf1"], "新北市公立國中翰林版課程計畫；公 Bf-Ⅳ-1 明列法治與人治差異，安排權利／權力、新聞情境與討論評量"),
        ],
        "representations": ["法治／人治特徵對照矩陣", "規則—權力—權利—救濟因果鏈", "公共措施的程序檢核流程圖"],
        "assessment": ["法治與人治情境分類", "法律適用與程序證據閱讀", "權利保障與救濟路徑說明", "小組討論、紙筆測驗與課堂觀察"],
    },
]


def main() -> None:
    data = json.loads(REPORT.read_text(encoding="utf-8"))
    existing = {item["lessonId"] for item in data["units"]}
    added = []
    for sample in SAMPLES:
        source_records = []
        for publisher, url, locator in sample["sources"]:
            source_records.append({
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
            "sources": source_records,
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
            blocker["reason"] = reason.replace("Four hundred eighty-three unit samples", "Four hundred eighty-six unit samples")
    blockers_path.write_text(json.dumps(blockers, ensure_ascii=False, indent=2) + "\n", encoding="utf-8")
    print(json.dumps({"unitCount": data["unitCount"], "added": added}, ensure_ascii=False))


if __name__ == "__main__":
    main()
