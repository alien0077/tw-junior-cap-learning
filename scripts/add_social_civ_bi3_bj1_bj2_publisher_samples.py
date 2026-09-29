#!/usr/bin/env python3
"""Record public-school publisher-linked evidence for Civ Bi-IV-3, Bj-IV-1 and Bj-IV-2."""
from __future__ import annotations

import json
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
REPORT = ROOT / "implementation/reports/publisher-chapter-evidence-samples.json"
LICENSE = "只記錄公立學校課程計畫的版本、章節重點與評量方向，不複製教材、圖表、題目或答案。"
NANI = "https://course.cyc.edu.tw/upfile/course110/sub1/14791548699293455.pdf"
KANG = "https://course.cyc.edu.tw/upfile/course114/file_school/15952869896665246.pdf"
HANLIN_CRIMINAL = "https://www.tsjh.ntpc.edu.tw/app/index.php?Action=downloadfile&cg=119&file=WVhSMFlXTm9MemN3TDNCMFlWOHhNamc0Tmw4Mk9UVXhPVFF4WHpjNE9Ea3pMbkJrWmc9PQ%3D%3D&fname=WSGGXSQKRKDCOOYXLOLKWWXTZSPKWTRL14JCB114A1A1DCB5WSJCPP5414HGJGA0VWPOXT154404MOWS1430ICNPOP34XSGC01YTNOB5WSB001PODGGGQKUSTWPOXXKKVSNOXWXTMKJCUSIC14JCSW20LKKKQOJCTWICZTA1LKQPSWYWKORK00SSPKROKK04POPO"
HANLIN_CIVIL = "https://course.cyc.edu.tw/upfile/course109/sub1/14503064157465443.pdf"

SAMPLES = [
    {
        "lessonId": "lesson-social-content-civ-bi-iv-3",
        "title": "公 Bi-Ⅳ-3：刑事追訴中的警察、檢察官與法官",
        "core": [
            "刑事案件的追訴是由偵查、起訴、審判到執行等不同階段組成，各職務有不同權限與責任，不能把警察、檢察官、法官視為同一種追訴角色",
            "理解分工要區分蒐集與保全證據、決定是否起訴、判斷證據與作成裁判等功能，並留意無罪推定、正當程序與司法審查",
            "以案件流程圖、角色權限卡與程序資料，判斷某一步驟由誰負責、需要哪些理由及人民可以如何行使防禦與救濟權利",
        ],
        "diff": [
            "南一把刑事訴訟置於法律與生活的制度單元，適合從刑法與刑罰先備概念銜接追訴程序",
            "康軒以刑事案件追訴章節連接刑法、責任與司法角色，安排討論、紙筆、作業與課堂問答",
            "翰林以刑事追訴流程及警察、檢察官、法官職權比較為核心，使用摘要、自我解釋和練習本檢核",
        ],
        "sources": [
            ("nani", NANI, "嘉義縣梅山國中公立課程計畫；南一版法律與生活脈絡由刑法與刑罰銜接刑事訴訟，列公 Bi-Ⅳ-3 的追訴角色與程序"),
            ("kanghsuan", KANG, "嘉義縣阿里山國中公立課程計畫；教材明載康軒版第4冊，刑事案件追訴章節安排公 Bi-Ⅳ-3 與多元課堂評量"),
            ("hanlin", HANLIN_CRIMINAL, "新北市淡水國中公立課程計畫；教材明載翰林版，列公 Bi-Ⅳ-3 並比較警察、檢察官、法官及律師等角色權限"),
        ],
        "representations": ["偵查—起訴—審判—執行流程圖", "刑事司法角色權限比較矩陣", "證據、程序保障與救濟關聯圖"],
        "assessment": ["刑事追訴階段排序", "角色與權限案例配對", "程序保障口頭說明", "摘要、自我解釋、課堂參與與紙筆評量"],
    },
    {
        "lessonId": "lesson-social-content-civ-bj-iv-1",
        "title": "公 Bj-Ⅳ-1：契約合意、登記與不履行責任",
        "core": [
            "契約通常以雙方意思表示合致形成，但特定契約可能還需要書面、交付或登記等要件；判斷效力必須把合意、形式與法律特別規定分開",
            "契約不履行可能涉及債務人是否有可歸責事由、履行內容與損害結果，責任判斷不能只看一方主張或結果是否不公平",
            "用契約成立要件表、履行時間線與爭議處理流程，分析生活交易中的權利義務、證據和可行救濟",
        ],
        "diff": [
            "南一把契約放在民法與民事責任脈絡，適合從民法功能與日常交易先建立合意和責任概念",
            "康軒以生活中的契約章節拆分契約種類、成立、登記與不履行，安排案例討論、紙筆、作業和心得表達",
            "翰林以民法意涵、契約與民事責任展開，搭配契約成立與救濟的練習本和課堂問答",
        ],
        "sources": [
            ("nani", NANI, "嘉義縣梅山國中公立課程計畫；南一版法律與生活／民法脈絡涵蓋契約成立、責任與公 Bj-Ⅳ-1"),
            ("kanghsuan", KANG, "嘉義縣阿里山國中公立課程計畫；教材明載康軒版第4冊，生活中的契約章節列公 Bj-Ⅳ-1，採討論、紙筆、作業、問答與心得"),
            ("hanlin", HANLIN_CIVIL, "嘉義縣東榮國中公立課程計畫；教材明載翰林版第四冊，公 Bj-Ⅳ-1 安排契約合意、登記、不履行責任與紙筆／討論評量"),
        ],
        "representations": ["合意—形式—登記—效力檢核表", "契約履行時間線與責任分支", "交易爭議的證據—責任—救濟流程"],
        "assessment": ["契約成立條件判讀", "登記與效力案例比較", "不履行責任的理由說明", "分組討論、紙筆、作業與課堂問答"],
    },
    {
        "lessonId": "lesson-social-content-civ-bj-iv-2",
        "title": "公 Bj-Ⅳ-2：限制行為能力人的契約",
        "core": [
            "行為能力制度依年齡與身心狀況安排法律行為的獨立程度，限制行為能力人不是完全不能訂約，而是特定契約通常需要法定代理人同意或事後承認",
            "判斷契約效力要檢查行為人身分、交易種類、是否屬日常生活所需、同意或承認是否存在，不能用『未成年』三字直接推定所有行為無效",
            "以購物、網路服務與財產交易案例建立身分—交易—同意—效力決策樹，練習兼顧交易安全與未成年人保護",
        ],
        "diff": [
            "南一把限制行為能力放在民法與契約單元，從法律行為與家庭／代理關係說明保護與交易安全的平衡",
            "康軒把公 Bj-Ⅳ-2 與契約種類及民法責任連續安排，重視案例討論和多階段課堂練習",
            "翰林以行為能力、法定代理人同意與契約效力為重點，使用紙筆、討論與課堂問答確認判斷步驟",
        ],
        "sources": [
            ("nani", NANI, "嘉義縣梅山國中公立課程計畫；南一版民法與契約脈絡列限制行為能力與法定代理人同意的公 Bj-Ⅳ-2"),
            ("kanghsuan", KANG, "嘉義縣阿里山國中公立課程計畫；康軒版第4冊生活中的契約章節明列公 Bj-Ⅳ-2，安排多元討論與紙筆／作業評量"),
            ("hanlin", HANLIN_CIVIL, "嘉義縣東榮國中公立課程計畫；翰林版第四冊列公 Bj-Ⅳ-2，連結行為能力、法定代理人同意與契約案例"),
        ],
        "representations": ["身分—交易類型—同意—效力決策樹", "日常交易與法定代理比較表", "未成年人保護與交易安全的利益平衡圖"],
        "assessment": ["行為能力情境分類", "同意／承認與契約效力判讀", "交易安全與保護理由短講", "分組討論、紙筆、作業與課堂問答"],
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
            blocker["reason"] = reason.replace("Four hundred ninety-two unit samples", "Four hundred ninety-five unit samples")
    blockers_path.write_text(json.dumps(blockers, ensure_ascii=False, indent=2) + "\n", encoding="utf-8")
    print(json.dumps({"unitCount": data["unitCount"], "added": added}, ensure_ascii=False))


if __name__ == "__main__":
    main()
