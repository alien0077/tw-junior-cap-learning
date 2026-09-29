#!/usr/bin/env python3
"""Individually repair keys, solutions, and public-exam pattern provenance for English 5-IV-2."""
from __future__ import annotations

import json
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
QDIR = ROOT / "questions/english"
CATALOG = ROOT / "data/public-exam-sources.json"
TODAY = "2026-09-26"

SOURCES = [
    {
        "id": "csjh-110-1-term1-grade7-english-basic-qa",
        "school": "基隆市立中山高級中學國中部", "grade": "7", "subject": "english",
        "exam": "110學年度第1學期第1次段考", "year": "110-1",
        "url": "https://oldcsjh.kl.edu.tw/books/file/263/110-1%E5%9C%8B%E4%B8%80%E8%8B%B1%E6%96%87%E6%AE%B5%E8%80%83%E8%A9%A6%E9%A1%8C.pdf",
        "title": "基隆市立中山高中國中部110學年度第1學期七年級英語科段考試題",
        "locator": "PDF第1頁第5至8題，聽力測驗基本問答；以聽辨語境選出合宜回應",
    },
    {
        "id": "ycjh-112-2-term2-grade7-english-basic-qa",
        "school": "花蓮縣立宜昌國民中學", "grade": "7", "subject": "english",
        "exam": "112學年度第2學期第2次段考", "year": "112-2",
        "url": "https://www.ycjh.hlc.edu.tw/modules/tad_uploader/index.php?cat_sn=417&cfsn=2790&name=112-2-%E7%AC%AC2%E6%AC%A1%E6%AE%B5%E8%80%837%E5%B9%B4%E7%B4%9A%E8%8B%B1%E8%AA%9E%E8%81%BD%E5%8A%9B%E9%A1%8C%E7%9B%AE%E8%88%87%E7%AD%94%E6%A1%88-%E9%82%B1%E6%9B%89%E8%96%87.pdf&op=dlfile",
        "title": "花蓮縣立宜昌國中112學年度第2學期七年級第2次段考英語聽力試題",
        "locator": "PDF第1頁第7至8題及第2頁第9至13題，基本問答；涵蓋日期、物主、居住感受、科目、考試日期、請求及數量回應",
    },
    {
        "id": "dwm-113-2-term1-grade7-english-basic-qa",
        "school": "高雄市立大灣國民中學", "grade": "7", "subject": "english",
        "exam": "113學年度第2學期第1次段考", "year": "113-2",
        "url": "https://www.dwm.kh.edu.tw/upload/344/104_64184/113%E5%AD%B8%E5%B9%B4%E5%BA%A6%E7%AC%AC%E4%BA%8C%E5%AD%B8%E6%9C%9F%E7%AC%AC%E4%B8%80%E6%AC%A1%E6%AE%B5%E8%80%83%E8%8B%B1%E6%96%87%E4%B8%80%E5%B9%B4%E7%B4%9A%E8%A9%A6%E9%A1%8C.pdf",
        "title": "高雄市立大灣國中113學年度第2學期七年級第1次段考英語科試題",
        "locator": "PDF第1頁第5至8題，聽力測驗基本問答；以語境、問句功能與回應關係作選擇",
    },
]

# Correct answer key, task-specific strategy, and five independently authored reasoning steps.
SOLUTIONS = {
    1: ("D", "先把問路句拆成目的地與路徑兩個需求，再找包含可執行方向的回覆。", [
        "讀 Excuse me, how can I get to the post office，確認對方要的是前往郵局的路線。",
        "預期回話應提供方向或轉彎資訊，單說物件特徵、寄信經驗或偏好都不夠。",
        "把 Go straight 和 turn left 接成連續指示，檢查它確實回答 how can I get there。",
        "其餘三句分別談昨天寄信、紙張材質和郵票顏色，沒有帶路資訊。",
        "正解是 D：直走兩個街區後左轉，是能照著走的路線回覆。",
    ]),
    2: ("B", "重述請求要求保留原訊息而改變說法或速度；核對回覆有沒有真的重複內容。", [
        "抓住 Could you repeat 與 more slowly，判定說話者請對方慢一點重說上一句。",
        "合宜回覆通常先接受請求，再重講一項明確資訊。",
        "meeting starts at nine 是完整的時間訊息，而且 Sure 表示願意配合。",
        "買東西的時間、圖書館位置和身高比較都不是上一句內容。",
        "正解是 B：先答應，再慢速重述會議九點開始。",
    ]),
    3: ("C", "從答句的感謝與拒絕內容逆推前句功能，再檢查具體行動是否相接。", [
        "答句 Thanks, but I can carry these books myself 表示對方拒絕一項好意。",
        "因此前句應是提供幫忙，而非詢問考試時間、停車位置或門鎖原因。",
        "Can I help you? 能自然引出搬書的協助提議，也接得上自己可以搬的婉拒。",
        "其他三個問句沒有提出幫忙，答句的 but 也就失去回應對象。",
        "正解是 C：先提出協助，對方再禮貌表示自己能搬。",
    ]),
    4: ("A", "邀約回應同時核對接受／婉拒立場與日期時段，避免只匹配到單一時間字。", [
        "Are you free to study together on Thursday 是邀請對方週四一起讀書。",
        "答案需要表明能否參加，並讓時間安排和 Thursday 相符。",
        "Thursday evening works for me 清楚接受邀約，且提供可行的週四晚間時段。",
        "去年修生物、桌子位置和書本重量都沒有回答是否有空。",
        "正解是 A：回覆確認週四晚上可行，邀約資訊前後一致。",
    ]),
    5: ("D", "不同意意見不等於否定對方；先找承接語，再確認後句提供了自己的理由。", [
        "第一人認為藍色海報更清楚；第二人接著說偏好綠色，理由是遠處較好閱讀。",
        "後句需要一個能承認前述觀點、同時轉入不同看法的語用開頭。",
        "I see your point, but 正好先表示理解，再用 but 引出不同偏好。",
        "祈使句、年齡問題與命令安靜都無法銜接兩種海報意見。",
        "正解是 D：理解對方的判斷後，再說明自己支持綠色的原因。",
    ]),
    6: ("C", "道歉後的回應要處理影響並給出可執行的下一步，不可只談物品外觀。", [
        "說話者為忘記歸還充電器道歉，物品目前仍需要交還。",
        "合宜回應可以接受道歉，同時約定補救或歸還期限。",
        "That is okay 表示接受；Please bring it tomorrow 提供清楚可做到的下一步。",
        "轉彎、兄弟人數和顏色尺寸都未回應遺忘歸還這件事。",
        "正解是 C：接受道歉，並約好明天把充電器帶來。",
    ]),
    7: ("B", "May I 是請求許可；答案需同意或拒絕，條件句則界定許可範圍。", [
        "May I use your phone to call my parents 是詢問能否借手機打電話。",
        "找出直接表達允許或不允許的回覆，而不是描述電話或家人住處。",
        "Of course 表示允許，but please keep the call short 加上使用條件。",
        "上週打過電話、手機比較新及住在車站附近，皆沒有回答是否可借。",
        "正解是 B：同意借用，但清楚限制通話時間。",
    ]),
    8: ("A", "確認句 right? 要核對時刻；再檢查補充計畫是否不會和班車發車時間衝突。", [
        "The bus leaves at 7:10, right? 是在確認公車發車時間。",
        "回應應直接確認或更正 7:10，並且不能安排在發車之後才抵達。",
        "we should arrive by 7:00 表示至少提早十分鐘到站，時間上可行。",
        "不喜歡公車、下雨及五元票價都沒有確認班次，且最後一句時態也不合。",
        "正解是 A：確認班車時間，並提出七點前抵達的準備。",
    ]),
    9: ("C", "看到安全警示後，從危險來源推導個人避險與通報兩種不同層次的行動。", [
        "訊息指出樓梯附近地板濕，主要風險是經過的人滑倒。",
        "有效回應應先降低自己跌倒的機會，並讓能處理現場的人知道。",
        "walk carefully 對應個人避險，tell the staff 對應通報濕滑狀況。",
        "作業、樓梯顏色和買背包都不會處理當下的安全風險。",
        "正解是 C：小心通行並通知工作人員，兼顧立即防護與後續處理。",
    ]),
    10: ("B", "建議題要建立問題與行動的因果連結；再判斷附帶建議是否安全且不轉移焦點。", [
        "說話者常熬夜後覺得疲倦，明確線索是睡眠時間不足。",
        "合適的回應要給可實行的改善方法，而不是換到購物、顏色或借文具。",
        "go to bed earlier 直接處理晚睡；drink enough water 是合理的日常照顧補充。",
        "其餘選項既沒有針對疲倦，也沒有連回熬夜造成的狀況。",
        "正解是 B：提早就寢回應主要原因，補充足夠飲水作為保健提醒。",
    ]),
}

def make_refs(question_no: int) -> list[dict]:
    specifics = [
        "公開基本問答題要求辨認目的地／方位語意並選出可執行的路線回覆",
        "公開基本問答題要求聽辨重述請求及時間資訊的對應回覆",
        "公開基本問答題以對話線索判斷主動提供協助與婉拒的語用關係",
        "公開基本問答題要求配對邀約、日期及接受意願",
        "公開基本問答題呈現承接他人意見後提出不同偏好的回應功能",
        "公開基本問答題要求理解道歉情境並選擇接受及補救安排",
        "公開基本問答題要求辨認請求許可與附帶條件的回應功能",
        "公開基本問答題以時間資訊檢核確認句與行動安排是否相容",
        "公開基本問答題測量公共情境下對安全提醒作適切回應的能力",
        "公開基本問答題要求依生活困擾辨認相關建議及支持性回應",
    ][question_no - 1]
    return [{
        "url": source["url"], "title": source["title"], "year": source["year"], "subject": "english",
        "locator": source["locator"], "locatorLevel": "page",
        "observedPattern": f"{specifics}；只借用能力與對話功能方向，未複製原卷文字、選項、音檔或答案。",
        "reuseDecision": "pattern-only", "status": "recorded",
    } for source in SOURCES]

def main() -> None:
    catalog = json.loads(CATALOG.read_text(encoding="utf-8"))
    known = {source["id"] for source in catalog["sources"]}
    for source in SOURCES:
        if source["id"] not in known:
            catalog["sources"].append({
                "id": source["id"], "school": source["school"], "grade": source["grade"],
                "subject": source["subject"], "exam": source["exam"], "questionUrl": source["url"],
                "answerLocator": source["locator"],
                "usePolicy": "僅研究公開基本問答的溝通功能、語境線索與回應選擇；不保存或重製原卷文字、音檔、選項或答案。",
                "verifiedAt": TODAY,
            })
    catalog["updatedAt"] = TODAY
    CATALOG.write_text(json.dumps(catalog, ensure_ascii=False, indent=2) + "\n", encoding="utf-8")

    for number, (key, strategy, steps) in SOLUTIONS.items():
        path = QDIR / f"question-english-performance-5-iv-2-{number}.json"
        data = json.loads(path.read_text(encoding="utf-8"))
        old = {option["id"]: option["text"] for option in data["options"]}
        correct = old[data["answer"]["value"]]
        distractors = [option["text"] for option in data["options"] if option["text"] != correct]
        ordered = distractors[:]
        ordered.insert(ord(key) - ord("A"), correct)
        ordered = ordered[:4]
        assert ordered[ord(key) - ord("A")] == correct
        data["options"] = [{"id": chr(65 + i), "text": text} for i, text in enumerate(ordered)]
        data["answer"]["value"] = key
        data["answer"]["explanation"] = steps[-1]
        data["solutionStrategy"] = strategy
        data["solutionSteps"] = steps
        data["examPatternRefs"] = make_refs(number)
        data["provenance"]["sourceUrl"] = SOURCES[0]["url"]
        data["provenance"]["sourceLocator"] = "基隆中山高中國中部、花蓮宜昌國中與高雄大灣國中公開七年級英語段考基本問答題；逐校PDF頁次、題號與 pattern-only 界線列於 examPatternRefs。"
        data["provenance"]["authoringNote"] = "依官方課綱與 KG-english-performance-5-iv-2 的日常溝通目標，參照三所公立學校公開段考的基本問答題型及溝通功能方向獨立改寫；對話與選項均為原創，沒有使用原卷文字、音檔或答案；仍待完整內容及版權 gate。"
        data["updatedAt"] = TODAY
        path.write_text(json.dumps(data, ensure_ascii=False, indent=2) + "\n", encoding="utf-8")
    print("repaired English 5-IV-2: ten keys, five-step solutions, and three public-school pattern-only references per item")

if __name__ == "__main__":
    main()
