#!/usr/bin/env python3
"""Record public-school publisher-linked evidence for Civ Bf-IV-2, Bg-IV-1 and Bh-IV-1."""
from __future__ import annotations

import json
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
REPORT = ROOT / "implementation/reports/publisher-chapter-evidence-samples.json"
LICENSE = "只記錄公立學校課程計畫的版本、章節重點與評量方向，不複製教材、圖表、題目或答案。"

NANI = "https://course.cyc.edu.tw/upfile/course110/sub1/14791548699293455.pdf"
KANG = "https://www.mtjh.tp.edu.tw/wp-content/uploads/doc/mtjh212/113_%E5%85%AB%E5%B9%B4%E7%B4%9A%E7%A4%BE%E6%9C%83%E9%A0%98%E5%9F%9F%28%E5%85%AC%E6%B0%91%E7%A7%91%29%E8%AA%B2%E7%A8%8B%E8%A8%88%E7%95%AB.pdf"
HANLIN_LAW = "https://www.ctbc.ntpc.edu.tw/wp-content/uploads/2025/09/%E7%BF%B0%E6%9E%97%E7%89%88_%E5%85%AB%E5%B9%B4%E7%B4%9A%E7%A4%BE%E6%9C%83%E5%85%AC%E6%B0%91.pdf"
HANLIN_ADMIN = "https://www.tsjh.ntpc.edu.tw/app/index.php?Action=downloadfile&cg=119&file=WVhSMFlXTm9MemN3TDNCMFlWOHhNamc0Tmw4Mk9UVXhPVFF4WHpjNE9Ea3pMbkJrWmc9PQ%3D%3D&fname=WSGGXSQKRKDCOOYXLOLKWWXTZSPKWTRL14JCB114A1A1DCB5WSJCPP5414HGJGA0VWPOXT154404MOWS1430ICNPOP34XSGC01YTNOB5WSB001PODGGGQKUSTWPOXXKKVSNOXWXTMKJCUSIC14JCSW20LKKKQOJCTWICZTA1LKQPSWYWKORK00SSPKROKK04POPO"

SAMPLES = [
    {
        "lessonId": "lesson-social-content-civ-bf-iv-2",
        "title": "公 Bf-Ⅳ-2：憲法、法律與命令的位階",
        "core": [
            "法規範位階是為了處理規範衝突：憲法設定最高層次的基本原則，法律由立法機關制定，命令須在法律授權與憲法界線內執行",
            "判斷一項命令或行政規則是否合法，要沿著制定機關、授權依據、規範內容與是否牴觸上位規範逐層檢查，不能只因規則寫得具體就視為最高效力",
            "以規範階層圖、授權鏈與生活行政案例，練習找出衝突規範、說明位階理由並提出可查證的救濟或監督方向",
        ],
        "diff": [
            "南一把法治、人治與法律內涵安排在同一法治單元，適合先建立法治目的再處理位階與授權",
            "康軒以政府與權力分立、憲法權利保障的連續章節支撐位階判讀，重視民主正當性與權力限制",
            "翰林以法治社會章節明列憲法、法律、命令的位階，搭配圖表、案例與討論／紙筆檢核",
        ],
        "sources": [
            ("nani", NANI, "嘉義縣梅山國中公立課程計畫；教材明載南一版第3、4冊，法治基本概念單元列公 Bf-Ⅳ-2 與法律位階"),
            ("kanghsuan", KANG, "臺北市民族實驗國中公立課程計畫；教材明載康軒版，憲法與權利保障章節列公 Bf-Ⅳ-2，安排討論、紙筆與隨堂練習"),
            ("hanlin", HANLIN_LAW, "新北市公立國中翰林版八年級公民課程計畫；公 Bf-Ⅳ-2 明列憲法、法律、命令位階與法律位階圖表／案例教學"),
        ],
        "representations": ["憲法—法律—命令階層圖", "授權來源—制定機關—規範效力鏈", "規範衝突案例的逐層檢核表"],
        "assessment": ["規範位階排序", "授權與牴觸上位規範的案例判讀", "法治概念口頭解釋", "討論、紙筆測驗與隨堂練習"],
    },
    {
        "lessonId": "lesson-social-content-civ-bg-iv-1",
        "title": "公 Bg-Ⅳ-1：憲法作為人民權利的保障書",
        "core": [
            "憲法不只是政府組織說明書，也透過基本權利、國家權力界線與救濟制度把人民置於權利主體的位置",
            "判斷憲法保障要把事件事實、涉及的基本權、限制目的、法律依據與程序正當性分開，不能只看到政府宣稱公益就結束分析",
            "用權利—限制—審查—救濟流程處理生活或新聞式案例，練習以規範文字和多方利益說明保障與限制之間的張力",
        ],
        "diff": [
            "南一把 Bg-Ⅳ-1 與法治、人治及法律位階放在法治基本概念單元，從憲法最高性與權利保障連接制度理解",
            "康軒將 Bg-Ⅳ-1 放在憲法與權利保障章節，透過人權教育與討論、紙筆、隨堂練習反覆檢核權利意義",
            "翰林以憲法與權利保障章節處理基本權利及憲法特性，使用案例、分組討論與紙筆評量建立權利判讀",
        ],
        "sources": [
            ("nani", NANI, "嘉義縣梅山國中公立課程計畫；南一版法治基本概念單元同列公 Bg-Ⅳ-1，連結憲法與人民權利保障"),
            ("kanghsuan", KANG, "臺北市民族實驗國中公立課程計畫；康軒版憲法與權利保障章節明列公 Bg-Ⅳ-1，使用人權教育與多元評量"),
            ("hanlin", HANLIN_LAW, "新北市公立國中翰林版八年級公民課程計畫；憲法與權利保障章節明列公 Bg-Ⅳ-1，安排基本權利與憲法特性案例"),
        ],
        "representations": ["基本權利—限制目的—法律依據—救濟流程", "憲法特性與權利保障概念圖", "權利衝突的多方觀點證據表"],
        "assessment": ["基本權利情境辨識", "權利限制的目的與程序判讀", "憲法保障理由短講", "分組討論、紙筆測驗與隨堂練習"],
    },
    {
        "lessonId": "lesson-social-content-civ-bh-iv-1",
        "title": "公 Bh-Ⅳ-1：行政法與依法行政",
        "core": [
            "行政法規範政府與人民互動時的權限、程序與責任，使行政機關在發證、管制、裁罰或提供服務時有可檢查的法律依據",
            "依法行政包含法律保留與法律優位的檢查：行政機關須在權限範圍內作成決定，內容不得牴觸上位法律，程序也要讓人民理解、參與或救濟",
            "從日常許可、交通管制、校園或公共安全措施追蹤行政決定的法源、目的、影響與救濟路徑，區分方便管理與合法行政",
        ],
        "diff": [
            "南一把行政法放入公民權利保障與規範，適合從人民日常接觸的行政措施建立法源與權利意識",
            "康軒以法律生活與行政法規章節搭配行政管制、依法行政及人權教育，重視生活案例與紙筆／觀察評量",
            "翰林安排行政法規與行政救濟章節，使用教科書與練習本、摘要／自我解釋策略及行政案例課堂參與",
        ],
        "sources": [
            ("nani", NANI, "嘉義縣梅山國中公立課程計畫；南一版第3、4冊法律與生活脈絡，將行政法與依法行政納入公民權利保障／規範"),
            ("kanghsuan", "https://www.bish.tp.edu.tw/get_file.php?file_dir=data10710%2F&file_name=928eba2556705d3480c7ffbafd847108.pdf&rename=%E4%B9%9D%E5%B9%B4%E7%B4%9A%E7%A4%BE%E6%9C%83%28%E5%85%AC%E6%B0%91%E8%88%87%E7%A4%BE%E6%9C%83%29.pdf", "臺北市靜修中學公立課程計畫；教材明載康軒版，公 Bh-Ⅳ-1 與行政法、依法行政及法治教育並列，採觀察、自評、同儕與紙筆評量"),
            ("hanlin", HANLIN_ADMIN, "新北市淡水國中公立課程計畫；教材明載翰林版公民與社會，公 Bh-Ⅳ-1 置於行政法規與行政救濟章節，安排摘要、自我解釋與課堂參與"),
        ],
        "representations": ["行政決定的法源—目的—權限—程序鏈", "行政管制與人民權益影響表", "申訴／行政救濟路徑圖"],
        "assessment": ["行政措施法源判讀", "依法行政要件配對", "日常案例的權利影響說明", "課堂參與、摘要、自我解釋與紙筆評量"],
    },
]


def main() -> None:
    data = json.loads(REPORT.read_text(encoding="utf-8"))
    existing = {item["lessonId"] for item in data["units"]}
    added = []
    for sample in SAMPLES:
        sources = []
        for publisher, url, locator in sample["sources"]:
            sources.append({
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
            "sources": sources,
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
            blocker["reason"] = reason.replace("Four hundred eighty-six unit samples", "Four hundred eighty-nine unit samples")
    blockers_path.write_text(json.dumps(blockers, ensure_ascii=False, indent=2) + "\n", encoding="utf-8")
    print(json.dumps({"unitCount": data["unitCount"], "added": added}, ensure_ascii=False))


if __name__ == "__main__":
    main()
