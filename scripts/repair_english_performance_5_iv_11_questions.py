#!/usr/bin/env python3
"""Repair sources, keys, and table-reading explanations for English 5-IV-11."""
from __future__ import annotations

import json
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
QDIR = ROOT / "questions/english"
CATALOG = ROOT / "data/public-exam-sources.json"
TODAY = "2026-09-26"

SOURCES = [
    {
        "id": "nhjh-110-2-term1-grade7-english",
        "school": "臺北市立內湖國民中學", "grade": "7", "subject": "english",
        "exam": "110學年度第2學期第1次段考", "year": "110-2",
        "url": "https://www.nhjh.tp.edu.tw/uploads/1660183128201jpNsop8i.pdf",
        "title": "臺北市立內湖國中110學年度第2學期七年級英語科第一次段考",
        "examLocator": "PDF第2頁課程表及第19至21題；依星期、活動欄交叉讀取行程資料",
    },
    {
        "id": "kcjh-110-2-term1-grade8-english",
        "school": "高雄市立國昌國民中學", "grade": "8", "subject": "english",
        "exam": "110學年度第2學期第1次段考", "year": "110-2",
        "url": "https://www.kcjh.kh.edu.tw/upload/190/104_34764/%E5%9C%8B%E4%BA%8C%E8%8B%B1%E6%96%87%E6%AE%B5%E8%80%83%E8%A9%A6%E9%A1%8C.pdf",
        "title": "高雄市立國昌國中110學年度第2學期二年級第一次段考英文科試題",
        "examLocator": "PDF第3頁第19至21題；高鐵時刻與票種折扣表的多欄資料判讀",
    },
    {
        "id": "zsjh-110-1-term1-grade7-english",
        "school": "臺中市立至善國民中學", "grade": "7", "subject": "english",
        "exam": "110學年度第1學期第1次定期評量", "year": "110-1",
        "url": "https://school.tc.edu.tw/open-message/193521/get-file/61f258cbaea6987a0f46560a.pdf",
        "title": "臺中市立至善國中110學年度第1學期七年級第一次定期評量英語科試題卷",
        "examLocator": "PDF第6頁第38至40題；牙科診所星期、時段與醫師工作表",
    },
]

# key, options A-D, exact page/item locators, distinct strategy, five authored steps
ITEMS = {
    1: ("A", ["Name: Mia; Grade: 8; Activity: hiking", "Name: hiking; Grade: Mia; Activity: 8", "Name: 8; Grade: hiking; Activity: Mia", "Name: Mia; Grade: hiking; Activity: 8"], ["PDF第2頁第19至21題", "PDF第3頁第19至21題", "PDF第6頁第38至40題"], "把表單欄位當作固定標籤逐格配對，姓名、年級與活動三項都要回到題目資料核對。", ["先抄出表單三欄的意義：Full Name 是人名、Grade 是年級、Favorite Activity 是活動。", "將題目給的資料分別標記：Mia 是姓名，Grade 8 是年級，hiking 是活動。", "逐格比對候選列，確認每個值都進到相同語意的欄位，而非只看某一格。", "B、C、D 都把至少一項資料放錯欄；只有 A 保留三組正確配對。", "答案 A：Name: Mia; Grade: 8; Activity: hiking。"]),
    2: ("B", ["The concert", "The science show", "The book fair", "The school holiday"], ["PDF第2頁第19至21題", "PDF第3頁第19至21題", "PDF第6頁第38至40題"], "先把 Wednesday 對準表格的星期欄，再沿同一列／欄找交會的活動，避免被其他日期吸引。", ["在題目中圈出 Wednesday，這是要查找的欄標。", "將表格的活動與星期配對：book fair—Monday、science show—Wednesday、concert—Friday。", "只保留與 Wednesday 同列的 science show，不把 Monday 或 Friday 的活動混進來。", "The concert 和 The book fair 分別對應 Friday、Monday；school holiday 未列在表中。", "答案 B：Wednesday 欄對應 The science show。"]),
    3: ("C", ["Class A", "Class B", "Class C", "All classes need the same number"], ["PDF第2頁第19至21題", "PDF第3頁第19至21題", "PDF第6頁第38至40題"], "這題要比較數量而非欄位名稱；先抄出三個數值，再用最大值回答。", ["把各班需求整理成 A=12、B=9、C=15，確保數字沒有抄錯。", "題目問 needs the most，因此尋找最大數，而不是最小或平均。", "15 大於 12 和 9，最大值屬於 Class C。", "Class A、Class B 的數量較少；「相同」也與表中的三個不同數字矛盾。", "答案 C：Class C 需要15支，是三班中最多的。"]),
    4: ("D", ["Breakfast", "Lunch", "Dessert only", "Snack"], ["PDF第2頁第19至21題", "PDF第3頁第19至21題", "PDF第6頁第38至40題"], "分類表題要先找到目標項目 milk，再追溯它所在的分類標頭；不要依個人飲食常識猜類別。", ["先定位目標項目 milk，而不是從 soup 或 salad 開始搜尋。", "表中 Lunch 包含 tomato soup 和 salad；Snack 包含 fruit 和 milk。", "沿著 milk 所在分組回看標題，得到 Snack。", "Lunch、Breakfast 與 Dessert only 都不是題目列出的 milk 所屬分類。", "答案 D：milk 被放在 Snack 分類。"]),
    5: ("A", ["Jay's class", "The book title", "The return date", "The student's name"], ["PDF第2頁第19至21題", "PDF第3頁第19至21題", "PDF第6頁第38至40題"], "缺漏欄位題先列出表單要求，再劃掉已填資料；剩下未提供的欄位就是答案。", ["需求欄位是 Name、Book、Return date 和 Class，共四項。", "現有表單已提供 Jay、The Sea、June 12，分別填妥姓名、書名與歸還日。", "把已滿足的三欄劃掉，只剩 Class 尚未出現。", "其他三個選項已在表單中，不是缺漏資訊。", "答案 A：還需要補上 Jay 所屬班級。"]),
    6: ("B", ["Both leave at the same time", "Bus 2", "Bus 1", "Neither bus has a time"], ["PDF第2頁第19至21題", "PDF第3頁第19至21題", "PDF第6頁第38至40題"], "比較時間時依時鐘先後轉成同一日的時間線，較晚出發者才是答案。", ["先讀清兩班車的出發時間：Bus 1 為 8:10，Bus 2 為 8:25。", "兩個時間都在上午同一時段，可直接比較分鐘數。", "8:25 比 8:10 晚15分鐘，因此 Bus 2 較晚離開。", "Bus 1 更早；兩者不相同，而且兩班車都有明確時間。", "答案 B：Bus 2 在 8:25 出發，比 8:10 晚。"]),
    7: ("C", ["Choose every workshop and omit all contact information.", "Write only a name and leave the required box blank.", "Select one workshop, add a phone number, and complete the emergency contact.", "Submit the form without reading the instructions."], ["PDF第2頁第19至21題", "PDF第3頁第19至21題", "PDF第6頁第38至40題"], "把指令拆成必做、數量限制與禁止留白三種條件，逐項確認選項全部遵守。", ["第一句要求選一個 workshop；one 限定只能選一項。", "第二句要求填 phone number，不能只寫姓名。", "第三句明確禁止 emergency-contact 欄空白，因此也必須完成該欄。", "A 同時符合單選、電話與緊急聯絡三條規則；其餘選項至少違反一條。", "答案 C：選一個工作坊、留下電話並填妥緊急聯絡人。"]),
    8: ("D", ["Collect them", "Wash them before collecting", "Sell them at the school gate", "Sort them"], ["PDF第2頁第19至21題", "PDF第3頁第19至21題", "PDF第6頁第38至40題"], "流程題用箭頭保留原順序，再從指定終點往前退一格，避免選到更早但非緊接的步驟。", ["把流程照題目寫成 collect → wash → sort → place in blue bin。", "問題指定 cans 入桶之前「立即」發生的步驟，不是任意較早步驟。", "從 place in blue bin 往前一格是 sort them。", "Collect 和 wash 雖然也在前面，但不是緊接放入藍桶前的動作；sell 未列入流程。", "答案 D：放入藍桶之前，先完成分類。"]),
    9: ("B", ["Oranges are more popular than apples.", "Apples are the most popular of the three.", "Bananas and apples have equal numbers.", "No student chose fruit."], ["PDF第2頁第19至21題", "PDF第3頁第19至21題", "PDF第6頁第38至40題"], "判斷資料是否支持敘述時，逐一核對數值和比較詞；supported 不代表聽起來合理，而是能被表格證明。", ["先讀出調查數值：apples 14、bananas 10、oranges 6。", "把選項的比較關係轉成數字檢查：蘋果高於香蕉與柳橙。", "因此 apples are the most popular of the three 可由表格直接支持。", "柳橙並未高於蘋果；蘋果與香蕉不相等；三種水果都有人選。", "答案 B：蘋果14票最多，該敘述是表格能支持的結論。"]),
    10: ("C", ["Choose the most expensive destination because it has the longest name.", "Choose any Friday destination and ignore the required item column.", "Choose the Saturday destination with the lowest listed price among the hat-required options.", "Choose the Saturday row without checking its price or item requirement."], ["PDF第2頁第19至21題", "PDF第3頁第19至21題", "PDF第6頁第38至40題"], "多條件選擇採逐層篩選：先符合星期，再符合必備物品，最後只在合格列中比較價格。", ["先圈定三項條件：Saturday、requires a hat、cheapest。", "在行程表先保留星期六的目的地，再查看必備物品欄，只留下含 hat 的列。", "只在符合前兩項的候選中比較價格，選最低者；不能跨出條件集合比較。", "A 以名稱長短猜價錢，B 忽略星期與必備物品，D 漏查價格或物品條件。", "答案 C：只在星期六且需要帽子的行程中，選標價最低的一項。"]),
}

OBSERVED = "只參照公開公校英文評量中以行程表、時段表、表單／資料表作答的資訊定位、跨欄配對、比較、條件篩選與順序判讀；站內題幹與數據獨立撰寫，未複製原卷。"


def make_refs(locators: list[str]) -> list[dict]:
    return [{"url": source["url"], "title": source["title"], "year": source["year"], "subject": "english", "locator": locator, "locatorLevel": "page", "observedPattern": OBSERVED, "reuseDecision": "pattern-only", "status": "recorded"} for source, locator in zip(SOURCES, locators, strict=True)]


def main() -> None:
    catalog = json.loads(CATALOG.read_text(encoding="utf-8"))
    known = {source["id"] for source in catalog["sources"]}
    for source in SOURCES:
        if source["id"] not in known:
            catalog["sources"].append({"id": source["id"], "school": source["school"], "grade": source["grade"], "subject": source["subject"], "exam": source["exam"], "questionUrl": source["url"], "answerLocator": source["examLocator"], "usePolicy": "僅研究表格／表單閱讀與資料判讀能力方向；不保存或重製原題文字、表格、選項或答案。", "verifiedAt": TODAY})
    catalog["updatedAt"] = TODAY
    CATALOG.write_text(json.dumps(catalog, ensure_ascii=False, indent=2) + "\n", encoding="utf-8")

    for number, (key, options, locators, strategy, steps) in ITEMS.items():
        path = QDIR / f"question-english-performance-5-iv-11-{number}.json"
        data = json.loads(path.read_text(encoding="utf-8"))
        data["options"] = [{"id": chr(65 + i), "text": text} for i, text in enumerate(options)]
        data["answer"]["value"] = key
        data["answer"]["explanation"] = steps[-1]
        data["solutionStrategy"] = strategy
        data["solutionSteps"] = steps
        data["examPatternRefs"] = make_refs(locators)
        data["provenance"]["sourceUrl"] = SOURCES[0]["url"]
        data["provenance"]["sourceLocator"] = "內湖、國昌、至善三所公立國中英語段考的表格／表單閱讀題；逐題頁碼、題號及 pattern-only 界線列於 examPatternRefs。"
        data["provenance"]["authoringNote"] = "依官方課綱與 KG-english-performance-5-iv-11，參照三所公立學校公開英語評量的資料定位與跨欄判讀能力方向獨立撰寫；人物、情境、數值、選項與解析均為原創，仍待完整內容及版權 gate。"
        data["updatedAt"] = TODAY
        path.write_text(json.dumps(data, ensure_ascii=False, indent=2) + "\n", encoding="utf-8")

    print("updated ten table/form-reading questions with three public-school sources each")


if __name__ == "__main__":
    main()
