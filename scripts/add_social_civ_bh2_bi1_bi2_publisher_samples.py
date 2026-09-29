#!/usr/bin/env python3
"""Record public-school publisher-linked evidence for Civ Bh-IV-2, Bi-IV-1 and Bi-IV-2."""
from __future__ import annotations

import json
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
REPORT = ROOT / "implementation/reports/publisher-chapter-evidence-samples.json"
LICENSE = "只記錄公立學校課程計畫的版本、章節重點與評量方向，不複製教材、圖表、題目或答案。"

NANI = "https://course.cyc.edu.tw/upfile/course110/sub1/14791548699293455.pdf"
KANG = "https://www.bish.tp.edu.tw/get_file.php?file_dir=data10710%2F&file_name=928eba2556705d3480c7ffbafd847108.pdf&rename=%E4%B9%9D%E5%B9%B4%E7%B4%9A%E7%A4%BE%E6%9C%83%28%E5%85%AC%E6%B0%91%E8%88%87%E7%A4%BE%E6%9C%83%29.pdf"
KANG_BI = "https://course.cyc.edu.tw/upfile/course114/file_school/15952869896665246.pdf"
HANLIN = "https://course.cyc.edu.tw/upfile/course109/sub1/14503135146558035.pdf"
HANLIN_CURRENT = "https://www.tsjh.ntpc.edu.tw/app/index.php?Action=downloadfile&cg=119&file=WVhSMFlXTm9MemN3TDNCMFlWOHhNamc0Tmw4Mk9UVXhPVFF4WHpjNE9Ea3pMbkJrWmc9PQ%3D%3D&fname=WSGGXSQKRKDCOOYXLOLKWWXTZSPKWTRL14JCB114A1A1DCB5WSJCPP5414HGJGA0VWPOXT154404MOWS1430ICNPOP34XSGC01YTNOB5WSB001PODGGGQKUSTWPOXXKKVSNOXWXTMKJCUSIC14JCSW20LKKKQOJCTWICZTA1LKQPSWYWKORK00SSPKROKK04POPO"

SAMPLES = [
    {
        "lessonId": "lesson-social-content-civ-bh-iv-2",
        "title": "公 Bh-Ⅳ-2：行政管制與行政救濟",
        "core": [
            "行政管制是政府為了公共安全、秩序、健康或其他公共目的，依法對人民活動設定條件、要求或限制；判斷正當性要同時看目的、法源、必要程度與受影響者",
            "當行政決定影響人民權益，行政救濟提供重新檢查與主張權利的制度途徑；救濟不是保證結果符合個人期待，而是要求權限、程序與理由可被檢驗",
            "以許可、裁罰、交通或公共衛生管制案例追蹤行政機關的決定流程，區分事前參與、事中陳述與事後救濟的功能",
        ],
        "diff": [
            "南一把行政管制與救濟放在依法行政章節，從日常行政措施連結人民權益和法治程序",
            "康軒把行政法規納入法律生活與法治教育，透過管制案例、權利救濟和多元評量建立制度理解",
            "翰林以行政法規與行政救濟章節安排摘要、自我解釋與練習本，強調行政責任和生活案例的理解",
        ],
        "sources": [
            ("nani", NANI, "嘉義縣梅山國中公立課程計畫；教材明載南一版第3、4冊，法律與生活章節列公 Bh-Ⅳ-2 行政管制與行政救濟"),
            ("kanghsuan", KANG, "臺北市靜修中學公立課程計畫；教材明載康軒版，公 Bh-Ⅳ-2 與行政法規、權利救濟及法治教育並列"),
            ("hanlin", HANLIN_CURRENT, "新北市淡水國中公立課程計畫；教材明載翰林版，行政法規與行政救濟章節列公 Bh-Ⅳ-2，安排摘要與課堂參與"),
        ],
        "representations": ["行政管制目的—法源—措施—影響表", "行政決定與救濟流程圖", "事前參與／事中陳述／事後救濟比較表"],
        "assessment": ["行政管制案例判讀", "法源與權利影響配對", "救濟途徑流程說明", "摘要、自我解釋、課堂參與與紙筆評量"],
    },
    {
        "lessonId": "lesson-social-content-civ-bi-iv-1",
        "title": "公 Bi-Ⅳ-1：刑法、罪刑法定與國家刑罰權",
        "core": [
            "刑法以明確規範哪些行為構成犯罪及其法律效果，國家處罰人民必須以行為時已存在的法律為依據，避免事後任意定罪",
            "判斷罪刑法定不只看有沒有處罰，還要檢查行為時點、法律明文、構成要件、法律解釋界線與國家刑罰權的限制",
            "用時間線、法條要件與生活案例分開分析行為事實、法律依據和責任判斷，避免把道德不喜歡直接等同刑事犯罪",
        ],
        "diff": [
            "南一把刑法意義和罪刑法定放在法律與生活單元，先從刑法功能建立國家處罰權的界線",
            "康軒以刑法與刑罰章節同時處理罪刑法定、刑罰目的與法律基本原則，安排討論、紙筆與課堂問答",
            "翰林從刑法制定、犯罪與法律明文限制切入，再連到刑罰種類與刑事追訴流程，使用摘要和案例練習",
        ],
        "sources": [
            ("nani", NANI, "嘉義縣梅山國中公立課程計畫；南一版法律與生活章節列公 Bi-Ⅳ-1，安排刑法意義、犯罪與法治教育評量"),
            ("kanghsuan", KANG_BI, "嘉義縣公立國中康軒版課程計畫；公 Bi-Ⅳ-1 明列刑法制定理由、行為時法律明文限制與刑事法治評量"),
            ("hanlin", HANLIN, "嘉義縣太保國中公立課程計畫；教材明載翰林版第三冊，公 Bi-Ⅳ-1 位於刑法與刑罰章節，並列罪刑法定與基本權利實作"),
        ],
        "representations": ["行為時點—法條明文—構成要件時間線", "犯罪成立要件檢核表", "刑罰權限制與人民保障概念圖"],
        "assessment": ["罪刑法定案例判讀", "行為事實與法律要件配對", "刑法功能口頭說明", "問題討論、紙筆測驗與活動練習"],
    },
    {
        "lessonId": "lesson-social-content-civ-bi-iv-2",
        "title": "公 Bi-Ⅳ-2：刑罰目的與制裁方式",
        "core": [
            "刑罰目的涉及責任回應、一般預防、特別預防與社會安全等不同考量；分析政策時應把目的、比例、程序與受影響者分開，不把重罰直覺當成唯一答案",
            "刑罰種類與法律效果各有不同，判讀制裁方式要留意行為責任、法定刑、個案情節及避免再犯的制度功能",
            "以刑罰目的矩陣、制裁方式比較和模擬判決理由活動，練習在保護社會與保障人權之間提出有證據的判斷",
        ],
        "diff": [
            "南一將刑法目的、犯罪與刑罰種類放在法律與生活章節，偏重概念整理與法治原則連結",
            "康軒把刑罰目的和制裁方式安排在刑法與刑罰單元，結合分組討論、紙筆、作業、隨堂練習和心得表達",
            "翰林以刑罰目的、種類、責任能力和刑事追訴連續編排，使用新聞式案例、練習本與課堂測驗",
        ],
        "sources": [
            ("nani", NANI, "嘉義縣梅山國中公立課程計畫；南一版刑法與刑罰章節列公 Bi-Ⅳ-2，安排刑罰目的、種類與法治教育評量"),
            ("kanghsuan", KANG_BI, "嘉義縣公立國中康軒版課程計畫；第三篇刑法與刑罰章節明列公 Bi-Ⅳ-2，採討論、紙筆、作業、隨堂練習與問答"),
            ("hanlin", HANLIN, "嘉義縣太保國中公立課程計畫；翰林版第三冊刑法與刑罰章節列公 Bi-Ⅳ-2，銜接刑罰種類、責任能力與刑事訴訟"),
        ],
        "representations": ["刑罰目的比較矩陣", "制裁方式—法律效果—制度功能表", "判決理由的比例與人權檢核流程"],
        "assessment": ["刑罰目的與案例配對", "制裁方式比較", "比例與人權理由短講", "分組討論、紙筆、作業、隨堂練習與心得報告"],
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
            blocker["reason"] = reason.replace("Four hundred eighty-nine unit samples", "Four hundred ninety-two unit samples")
    blockers_path.write_text(json.dumps(blockers, ensure_ascii=False, indent=2) + "\n", encoding="utf-8")
    print(json.dumps({"unitCount": data["unitCount"], "added": added}, ensure_ascii=False))


if __name__ == "__main__":
    main()
