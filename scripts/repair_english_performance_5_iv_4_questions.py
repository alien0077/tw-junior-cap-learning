#!/usr/bin/env python3
"""Repair English 5-IV-4 answer mapping, read-aloud reasoning, and public-school exam provenance."""
from __future__ import annotations

import json
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
OUT = ROOT / "questions/english"
CATALOG = ROOT / "data/public-exam-sources.json"
LESSON = "lesson-english-performance-5-iv-4"
KG = "kg-english-performance-5-iv-4"
TODAY = "2026-09-26"
SOURCES = [
    {
        "id": "kcjh-112-1-term2-grade9-tone-reading",
        "school": "高雄市立國昌國民中學", "grade": "9", "subject": "english",
        "exam": "112學年度第1學期第2次段考", "year": "112-1",
        "url": "https://www.kcjh.kh.edu.tw/upload/190/104_34764/%E5%9C%8B%E6%98%8C--%E4%B8%89%E5%B9%B4%E7%B4%9A--%E8%8B%B1%E8%AA%9E%E7%A7%91_1.pdf",
        "title": "高雄市立國昌國中112學年度第1學期九年級第2次段考英文科試題",
        "locator": "PDF第6頁第33至35題；詩作語調、文本事實與推論判讀",
        "level": "page",
    },
    {
        "id": "nhjh-111-1-term3-grade8-tone-reading",
        "school": "臺北市立內湖國民中學", "grade": "8", "subject": "english",
        "exam": "111學年度第1學期第3次段考", "year": "111-1",
        "url": "https://www.nhjh.tp.edu.tw/uploads/1675416243777dXcSuX4X.pdf",
        "title": "臺北市立內湖國中111學年度第1學期八年級第3次段考英語科試題",
        "locator": "PDF第4頁第46至47題；詩作語氣及關鍵語句指涉判讀",
        "level": "page",
    },
    {
        "id": "dam-103-1-term1-grade9-tone-reading",
        "school": "高雄市立大社國民中學", "grade": "9", "subject": "english",
        "exam": "103學年度第1學期第1次段考", "year": "103-1",
        "url": "https://www.dam.kh.edu.tw/upload/68/101_28414/%E4%B8%89%E5%B9%B4%E7%B4%9A%20%20%E5%9C%8B%E6%96%87%E3%80%81%E8%8B%B1%E6%96%87%E3%80%81%E8%87%AA%E7%84%B6%E3%80%81%E6%AD%B7%E5%8F%B2%E3%80%81%E5%85%AC%E6%B0%91.pdf",
        "title": "高雄市立大社國中103學年度第1學期九年級段考跨科試題卷（含英語）",
        "locator": "PDF第3頁閱讀測驗第1題；依短文內容判斷語氣／筆調",
        "level": "page",
    },
    {
        "id": "lkjh-114-1-term2-grade9-oral-dialogue",
        "school": "彰化縣立鹿港國民中學", "grade": "9", "subject": "english",
        "exam": "114學年度第1學期第2次段考口說測驗", "year": "114-1",
        "url": "https://lkjh.chc.edu.tw/storage/074502/posts/1545/files/114-1-2%E8%8B%B1%E6%96%87%E7%A7%91%E5%90%84%E5%B9%B4%E7%B4%9A%E7%AC%AC%E4%B8%80%E6%AC%A1%E6%AE%B5%E8%80%83%E7%BF%BB%E8%AD%AF%E5%8F%A5%E5%9E%8B%E9%A1%8C%E5%BA%AB%E5%8F%8A%E7%AF%84%E5%9C%8D%E6%B3%A8%E6%84%8F%E4%BA%8B%E9%A0%85.docx.pdf",
        "title": "彰化縣立鹿港國中114學年度第1學期九年級第2次段考英語口說測驗",
        "locator": "校方口說試題（二）Dialogue對話部分；以發音及語調表現評分",
        "level": "paper",
    },
]

SOLUTIONS = {
    1: ("D", "把標點轉成朗讀動作與語氣；逗號提示短停，驚嘆號加強警示語勢。", [
        "先找出句中的逗號與驚嘆號，確認題目要判讀的是朗讀表現。",
        "逗號把 Please 與 be careful 稍作切分，讀者應短暫停頓而不是中斷整句。",
        "驚嘆號讓提醒帶有較強的警覺感；內容是小心，語氣應清楚而急切。",
        "低聲耳語、跳過句子或改成詢問日期，都沒有同時對應這兩個標點線索。",
        "正解是 D：先短停，再以明確急切的語氣提醒對方。",
    ]),
    2: ("B", "角色提示是朗讀的直接證據；先照舞台指示調整音量，再用台詞核對情境。", [
        "方括號內的 whispers 是作者給演員的聲音提示，不是角色說出的台詞。",
        "whisper 表示降低音量，因此讀 Maya 的句子時應輕聲。",
        "someone is outside 帶有不確定感，低聲說與情境相容。",
        "大聲、開心或完全不出聲都違反明示的 whisper 指示。",
        "正解是 B：依 stage direction 輕聲朗讀，不自行添加相反情緒。",
    ]),
    3: ("C", "用 First／Then／Finally 建立三格時間線；朗讀第二個事件時讓 Then 成為轉折提示。", [
        "先圈出 First、Then、Finally，這三個字分別標記先後位置。",
        "把 packed the map 放在第一格，因為它跟著 First。",
        "checked the weather 跟著 Then，位於第一件事之後、離家之前。",
        "left home 是 Finally 的最後事件；買房子則沒有出現在敘述中。",
        "正解是 C：第二個事件是檢查天氣，朗讀時可用 Then 帶出次序轉換。",
    ]),
    4: ("A", "從失而復得的事件與跳起來的動作合併推斷情緒，避免只看驚嘆號或單一字詞。", [
        "核心事件是有人找到 Ben 走失的狗，失物重新出現通常解除擔心。",
        "jumps up 描寫立即而明顯的反應，顯示情緒不是平淡無感。",
        "把情境的 relief 與動作帶出的 excitement 合併，作為朗讀時的情緒方向。",
        "疲倦、作業憤怒或圖書館恐懼都沒有文本證據支持。",
        "正解是 A：聲音呈現鬆一口氣並帶著興奮，而非無關情緒。",
    ]),
    5: ("D", "先找 not 建立的對比兩端，再把重音放在真正區分選項的顏色詞。", [
        "not the blue one 表示說話者正在修正一個容易弄錯的選擇。",
        "句子的對比是 red notebook 與 blue one，不是詢問動作或冠詞。",
        "red 明確指出真正要的顏色；加重它最能避免聽者拿錯。",
        "asked、the、one 都不能單獨說明紅色與藍色的差異。",
        "正解是 D：重讀 red，讓更正的焦點清楚傳達。",
    ]),
    6: ("C", "沿著 Although 的讓步關係分成障礙與持續行動，讀出前後反差。", [
        "Although 引出一項本來可能阻止行動的困難。",
        "steep 說明路很陡，是前半句的阻礙。",
        "continued 表示健行者仍然繼續，後半句呈現決心。",
        "放棄、道路平坦或只談天氣都與句子提供的對比不符。",
        "正解是 C：先帶出路徑困難，再讓聲音落在持續前進的決心。",
    ]),
    7: ("B", "把舞台動作與台詞的剩餘時間相互印證，再推斷加快語速的理由。", [
        "looks at the clock 是舞台動作，提醒讀者注意時間線索。",
        "only five minutes left 明確表示時間所剩不多。",
        "動作與台詞相互支持 time pressure，因此角色可能急促地說話。",
        "時鐘不固定代表快樂；食譜或沒有時間資訊都與文本矛盾。",
        "正解是 B：讀出時間壓力造成的急迫，而不是把 clock 當成情緒詞。",
    ]),
    8: ("A", "把 No 放回前一個主張的對話脈絡，再用 didn't break 檢查是否為否認。", [
        "先辨認對話中有一項關於花瓶被打破的前置說法。",
        "句首 No 表示說話者不接受該說法。",
        "didn't break 再次明確否認打破花瓶的行為。",
        "同意、命令離開或宣布生日都不是這句話的功能。",
        "正解是 A：No 加上 didn't break，表示正在更正或否認指控。",
    ]),
    9: ("C", "把破折號視為語流中斷的可見標記；停頓後保留問句的驚訝語調。", [
        "破折號位於 Wait 與後面的問句之間，代表說話節奏突然轉折。",
        "先把 Wait 當作即時反應，接著做短暫停頓。",
        "停頓後再以疑問語調讀 did you hear that，讓驚訝和確認都聽得出來。",
        "不停頓、唱歌或忽略驚訝都沒有利用標點和對話情境。",
        "正解是 C：在破折號處稍停，再清楚提出驚訝的問題。",
    ]),
    10: ("B", "同時檢查舞台提示的位置與全體演員的動作，判斷它屬於謝幕而非新劇情。", [
        "[All characters bow] 出現在 final line 之後，位置本身提供重要線索。",
        "all characters 說明是全體演員一起做的動作，不是某個角色偷偷進場。",
        "演出結束後集體鞠躬是謝幕訊號，表示表演告一段落。",
        "故事尚未開始、觀眾提前離場或換成醫院場景都沒有文本根據。",
        "正解是 B：最後一句後全體鞠躬，表示演出已結束。",
    ]),
}

PATTERN_NOTES = [
    "本題練習標點與語勢線索的轉譯；公校朗讀／對話口說評分包含語調，並以短文語氣題補充文本情緒判讀。",
    "本題以角色明示的低聲提示決定朗讀方式；公校口說對話考核發音與語調，短文試題則要求從文字證據判讀語氣。",
    "本題把順序詞轉成朗讀節奏提示；公校閱讀題會要求依詩文與敘事線索掌握內容先後及其表達效果。",
    "本題依事件結果和動作推斷朗讀情緒；公校詩文題直接要求判斷文本語調／筆調，口說卷另評對話語調。",
    "本題練習以重音突顯更正焦點；公校口說測驗明列發音與語調為評分面向，文本語氣題提供語意證據判讀。",
    "本題依轉折連接詞表達障礙與決心；公校閱讀題透過詩文情緒與語氣選擇檢查是否掌握轉折後的態度。",
    "本題由動作提示和時間句推斷急迫語氣；公校閱讀題要求以短文線索推論情緒，口說對話測驗評量語調表現。",
    "本題辨認對話中的否認立場及其語勢；公校閱讀題要求從關鍵語句推論說話者立場與文本情緒。",
    "本題把破折號轉成自然停頓；公校口說對話評量語調與可理解表達，閱讀語氣題則要求回到標點與語境證據。",
    "本題依劇本位置和群體動作推斷表演功能；公校閱讀測驗常由文本線索推論事件意義，校內口說卷以對話表現評量語調。",
]

def make_refs(number: int) -> list[dict]:
    note = PATTERN_NOTES[number - 1]
    return [{
        "url": source["url"], "title": source["title"], "year": source["year"], "subject": "english",
        "locator": source["locator"], "locatorLevel": source["level"],
        "observedPattern": note + " 僅採能力與評量型態作 pattern-only 參照，不複製原卷題文、選項、詩文或答案。",
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
                "usePolicy": "僅研究公立學校公開英文閱讀語氣題及口說對話評量中的朗讀、語調與文本線索；不保存或重製原卷題文、選項、詩文或答案。",
                "verifiedAt": TODAY,
            })
    catalog["updatedAt"] = TODAY
    CATALOG.write_text(json.dumps(catalog, ensure_ascii=False, indent=2) + "\n", encoding="utf-8")

    for number, (key, strategy, steps) in SOLUTIONS.items():
        path = OUT / f"question-english-performance-5-iv-4-{number}.json"
        data = json.loads(path.read_text(encoding="utf-8"))
        options = {option["id"]: option["text"] for option in data["options"]}
        correct = options[data["answer"]["value"]]
        assert data["answer"]["value"] == "A", f"unexpected original key for item {number}"
        distractors = [option["text"] for option in data["options"] if option["text"] != correct]
        distractors.insert(ord(key) - ord("A"), correct)
        data["options"] = [{"id": chr(65 + index), "text": text} for index, text in enumerate(distractors)]
        data["answer"]["value"] = key
        data["answer"]["explanation"] = steps[-1]
        data["solutionStrategy"] = strategy
        data["solutionSteps"] = steps
        data["provenance"]["sourceUrl"] = SOURCES[0]["url"]
        data["provenance"]["sourceLocator"] = "國昌112-1九年級詩作語調題、內湖111-1八年級詩作語氣／語句推論題、大社103-1九年級閱讀語氣題，以及鹿港114-1九年級口說對話語調評量；頁碼與段落定位詳列於 examPatternRefs。"
        data["provenance"]["authoringNote"] = "依官方課綱 KG-english-performance-5-iv-4，參照三所公立學校公開英文試題的短文語氣判讀及鹿港國中口說對話語調評分方式，獨立撰寫朗讀理解題；情境、台詞、選項與解析均為原創，未複製試卷文字或音檔；內容與發布審查仍待完成。"
        data["updatedAt"] = TODAY
        data["examPatternRefs"] = make_refs(number)
        assert data["lessonId"] == LESSON and data["knowledgeIds"] == [KG]
        path.write_text(json.dumps(data, ensure_ascii=False, indent=2) + "\n", encoding="utf-8")
    print("repaired ten English 5-IV-4 answer mappings, read-aloud reasoning, and public-school exam refs")

if __name__ == "__main__":
    main()
