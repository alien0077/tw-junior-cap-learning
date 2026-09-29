#!/usr/bin/env python3
"""Author original 3-Ⅳ-8 reading items from verified public-exam patterns.

Public exams are pattern-only references. None of their text, choices, tables,
or answers are reproduced here.
"""
from __future__ import annotations

import json
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
OUT = ROOT / "questions/english"

SOURCES = {
    "neihu-report": {
        "url": "https://www.nhjh.tp.edu.tw/uploads/1675417163713PBpnsLYp.pdf",
        "title": "臺北市立內湖國中111學年度第1學期九年級第2次段考英語科",
        "year": "111學年度第1學期",
        "locator": "PDF第3頁第44至46題：節慶資料報告的詞義、未提及資訊辨識及有根據推論",
        "observedPattern": "短篇報告以不同欄位呈現節慶時間、活動、歷史與意義，題目分別檢查詞義、未提及資訊和跨欄推論；本題僅取閱讀能力型態。",
    },
    "guochang-story": {
        "url": "https://www.kcjh.kh.edu.tw/upload/190/104_34764/%E4%B8%89%E5%B9%B4%E7%B4%9A-%E8%8B%B1%E6%96%87_1.pdf",
        "title": "高雄市立國昌國中110學年度第1學期第1次段考三年級英語科",
        "year": "110學年度第1學期",
        "locator": "PDF第3頁第21至23題：依前後情節線索補足故事事件並判讀發展順序",
        "observedPattern": "連續敘事以先前線索、人物行動與後續結果建立事件因果；題目要求由上下文判斷缺漏事件或合理順序，不靠孤立字詞作答。",
    },
    "yancheng-diary": {
        "url": "https://www.yacjh.kh.edu.tw/upload/221/101_30637/114%E4%B8%8B%E5%AD%B8%E6%9C%9F%E7%AC%AC%E4%B8%80%E6%AC%A1%E6%AE%B5%E8%80%83%E4%B8%89%E5%B9%B4%E7%B4%9A%E8%8B%B1%E6%96%87.pdf",
        "title": "高雄市立鹽埕國中114學年度第2學期九年級第1次段考英文科",
        "year": "114學年度第2學期",
        "locator": "PDF第3頁閱讀題組第39至44題：追蹤日記事件及敘述者前後理解變化",
        "observedPattern": "日記型連續文本需綜合事件前後、敘述者反應與原因，辨認內容理解及想法變化；本題更換人物、情境與所有文字。",
    },
    "yancheng-notice": {
        "url": "https://www.yacjh.kh.edu.tw/upload/221/101_30637/114%E4%B8%8B%E5%AD%B8%E6%9C%9F%E7%AC%AC%E4%B8%80%E6%AC%A1%E6%AE%B5%E8%80%83%E4%B8%89%E5%B9%B4%E7%B4%9A%E8%8B%B1%E6%96%87.pdf",
        "title": "高雄市立鹽埕國中114學年度第2學期九年級第1次段考英文科",
        "year": "114學年度第2學期",
        "locator": "PDF第3頁閱讀題組第45至47題：辨識消防安全訊息的對象、行動呼籲與目的",
        "observedPattern": "以生活安全文字檢查讀者是否能辨認訊息對象及應採取的行動；僅吸收目的／行動判讀能力，不沿用原情境。",
    },
    "guochang-letter": {
        "url": "https://www.kcjh.kh.edu.tw/upload/190/104_34764/%E5%9C%8B%E6%98%8C--%E4%B8%89%E5%B9%B4%E7%B4%9A--%E8%8B%B1%E8%AA%9E%E7%A7%91.pdf",
        "title": "高雄市立國昌國中112學年度第1學期三年級第1次段考英文科",
        "year": "112學年度第1學期",
        "locator": "閱讀題組第19至21題：由父女往返信件理解寫信者感受、原因與溝通意圖",
        "observedPattern": "往返信件依稱呼、第一人稱內容與回信反應呈現人物關係及寫信動機；本題另創角色、事件和完整文字。",
    },
    "neihu-notice": {
        "url": "https://www.nhjh.tp.edu.tw/uploads/1706770089045DwNPg1SE.pdf",
        "title": "臺北市立內湖國中112學年度第1學期七年級第3次段考英文科",
        "year": "112學年度第1學期",
        "locator": "PDF第4頁閱讀題組（二）第51至52題：整合時間表與公告註記的不同資訊",
        "observedPattern": "須先辨認時間表與附註各自提供的資訊，再組合開放時間及例外條件；本題自行撰寫公告與日期。",
    },
    "neihu-missing": {
        "url": "https://www.nhjh.tp.edu.tw/uploads/1675417163713PBpnsLYp.pdf",
        "title": "臺北市立內湖國中111學年度第1學期九年級第2次段考英語科",
        "year": "111學年度第1學期",
        "locator": "PDF第3頁第45題：依節慶資料報告辨認未提及資訊",
        "observedPattern": "以多欄短報告區分明示資訊與文本未交代的細節；須逐項回查證據，不以常識補答。",
    },
    "sanduo-poster": {
        "url": "https://www.sdjh.ntpc.edu.tw/var/file/0/1000/attach/16/pta_2231_9842586_19803.pdf",
        "title": "新北市立三多國中112學年度第1學期七年級第2次段考英語科",
        "year": "112學年度第1學期",
        "locator": "PDF第3頁第36題：由海報整體訊息判斷溝通目的與對象",
        "observedPattern": "海報閱讀將受眾與活動目的放在同一視覺文本中判讀；本題轉為全新文字通知與行動資訊。",
    },
    "fengjia-main": {
        "url": "https://www.fjm.kh.edu.tw/upload/226/101_44845/113%E5%B9%B4%E5%9C%8B%E4%B8%AD%E7%B5%84%E9%96%B1%E8%AE%80%E7%B4%A0%E9%A4%8A%E8%A9%A6%E9%A1%8C%28%E7%AD%94%E6%A1%88%E5%85%AC%E5%91%8A%29.pdf",
        "title": "高雄市113學年度國中組閱讀素養試題（高雄市立鳳甲國中校方公開）",
        "year": "113學年度",
        "locator": "PDF第6頁第41題：整合故事內容辨識其主旨",
        "observedPattern": "需從故事多處事件統整主旨，而非用單一細節替全文命名；本題另創通學問題與校園合作情節。",
    },
}


ITEMS = [
    {
        "answer": "D", "difficulty": "medium", "focus": "作者目的與讀者行動",
        "prompt": "Read the message.\n\nHi, everyone,\nThe photo walk will still take place this Saturday, but we will meet at the library entrance instead of the station. The weather report says the riverside path may be closed after heavy rain. Please bring your camera and arrive by 8:40 so we can leave together at 8:50. If you cannot come, text me tonight.\n—Mina\n\nWhy did Mina most likely send this message?",
        "options": ["To cancel the photo walk because the library is closed", "To ask the group to take pictures of the weather report", "To tell everyone that the walk has moved to Sunday", "To update the meeting place and remind the group what to do"],
        "explanation": "她明確說活動仍在星期六舉行，只把集合地點改到圖書館入口，並提醒帶相機、到場時間及缺席時的回覆方式。訊息目的在更新安排，不是取消或改期。",
        "strategy": "先抓訊息中「原安排—變更—讀者要做什麼」三層，再判斷寫信者最主要想避免的誤會。",
        "steps": ["先讀開頭和結尾，確認這是寄給團體成員的活動通知。", "比較前後安排：活動仍是 Saturday，變更的是集合地點，不是日期。", "把提醒事項整理為帶相機、8:40 到場、不能參加要回訊息。", "逐項排除把活動取消、要求拍天氣報告或改成星期日的選項。", "用一句話概括：Mina 更新集合點並提醒參加者採取的行動；因此選 D。"],
        "refs": ["yancheng-notice", "sanduo-poster"],
    },
    {
        "answer": "A", "difficulty": "easy", "focus": "書信收件人與寫信關係",
        "prompt": "Read the letter.\n\nDear Mr. Hsu,\nThank you for letting our class interview you at the old train station. Your story about repairing clocks helped us understand why the station bell matters to the town. We have finished the history display and would like to invite you to see it next Thursday. Please let our teacher know if that afternoon works for you.\nSincerely,\nClass 903\n\nWho is the letter mainly written to?",
        "options": ["Mr. Hsu, who shared local history with the class", "The students in Class 903", "The teacher who organized the interview", "Visitors who want to repair the station clock"],
        "explanation": "稱呼 Dear Mr. Hsu、感謝他接受訪問，以及邀請他看成果，都指向同一位收件人。Class 903 是署名的寄件者，不是收件者。",
        "strategy": "書信題不要只看正文提到誰；把稱呼、正文中的 you 與署名三個位置互相核對。",
        "steps": ["先找信件稱呼 Dear 後面的對象，得到 Mr. Hsu。", "檢查正文的 you：被感謝的是接受班級訪問的人。", "閱讀邀請句，Mr. Hsu 也是被邀請看展覽的人。", "對照署名 Class 903，確認它代表寄件者而非收件者。", "三個線索一致指向分享地方歷史的 Mr. Hsu，所以選 A。"],
        "refs": ["guochang-letter"],
    },
    {
        "answer": "C", "difficulty": "medium", "focus": "期限、條件與下一步",
        "prompt": "Read the email.\n\nSubject: Science Fair Team\nOur team has been accepted for the school science fair. Please choose one of the two setup times in the shared form before 6 p.m. Wednesday. The room number will be sent after the teacher confirms our choice. You do not need to bring the model on Wednesday; bring it on Friday morning. If you cannot open the form, tell me your preferred time in a reply.\n—Evan\n\nWhat should a team member do by Wednesday evening?",
        "options": ["Bring the model to the classroom", "Wait for the room number before choosing a time", "Select a setup time or reply with a preference if the form does not work", "Ask the teacher to send the room number again"],
        "explanation": "期限前要完成的是在表單選一個布置時段；若表單不能開啟，就回信告知偏好的時段。模型要到星期五早上才帶來，教室號碼則要等老師確認時段後才會寄出。",
        "strategy": "遇到多個日期時，先把每個日期連到它負責的動作，再處理條件句提供的替代方案。",
        "steps": ["圈出 before 6 p.m. Wednesday，這是題目指定的期限。", "找期限前的動作：choose one of the two setup times in the form。", "讀 If 子句；表單無法開啟時，替代作法是回信說偏好時段。", "把 Friday morning 的帶模型和事後寄教室號碼排除，兩者都不是星期三前的任務。", "完整回答須涵蓋一般作法及表單故障的備案，因此選 C。"],
        "refs": ["yancheng-notice", "neihu-notice"],
    },
    {
        "answer": "B", "difficulty": "medium", "focus": "通知中的例外規則",
        "prompt": "Read the library notice.\n\nSTUDY ROOM UPDATE\nThe second-floor study room is open from 4:00 to 7:00 p.m. Monday through Thursday. On Friday, it closes at 5:00 because staff prepare the weekend book sale. Students may still return books at the box beside the main door after the room closes. Food is not allowed, but water bottles with lids are welcome.\n\nWhich statement is correct?",
        "options": ["Students can study in the room until 7:00 every weekday.", "On Friday, the room closes earlier than it does on the other listed days.", "Books cannot be returned after 5:00 on Friday.", "Students may bring any food if they also bring water."],
        "explanation": "星期一至四開到晚上七點，星期五因員工準備週末書展而五點關門，所以星期五較早關閉。關門後仍可從大門旁的箱子還書；食物仍禁止。",
        "strategy": "公告常把一般規則與例外放在相鄰句；答題時要同時保留比較基準和例外條件。",
        "steps": ["先辨認開放時間的基準：星期一至四是 4:00–7:00 p.m.。", "再找明確例外：星期五在 5:00 關閉。", "比較兩個關門時間，星期五比其他列出的日子早兩小時。", "檢查其他選項：每日七點、關門不能還書、可帶食物都與公告相反。", "只有 B 同時符合星期五例外與平日基準。"],
        "refs": ["neihu-notice"],
    },
    {
        "answer": "D", "difficulty": "medium", "focus": "敘事事件先後與因果",
        "prompt": "Read the diary entry.\n\nAt first, I thought the empty blue box outside the art room was just trash. Then Ms. Lin asked our class to leave one clean jar inside it. The next morning, the box was full of jars, each with a note from a student about where it came from. We washed them and used them to hold paintbrushes. Now the box has a label that says, “Give a jar a second job.” I did not know an ordinary container could start a class project.\n\nWhat happened after Ms. Lin made her request?",
        "options": ["The class threw away the jars because the box was full.", "The students bought new containers for paint.", "Ms. Lin moved the art room to another building.", "Students brought jars, and the class reused them for paintbrushes."],
        "explanation": "日記依序寫出老師請學生放入乾淨玻璃罐、隔天罐子增加、全班清洗後拿來裝畫筆。D 保留了關鍵行動與結果；其他選項不是文中事件。",
        "strategy": "故事順序題把轉折詞和動作動詞排成時間線，再確認選項是否包含文本真正交代的結果。",
        "steps": ["標出時間提示 At first、Then、The next morning、Now。", "依提示排列：看到空箱 → 老師提出請求 → 學生帶罐子 → 清洗再利用。", "題目問 request 之後，從 Then 開始追蹤後續，而非只看開頭。", "再往下確認用途是 hold paintbrushes，不是丟掉或購買新容器。", "D 對應帶罐與再利用兩個連續事件，且因果吻合。"],
        "refs": ["guochang-story"],
    },
    {
        "answer": "A", "difficulty": "hard", "focus": "由前後事件推論人物態度",
        "prompt": "Read the note.\n\nI almost quit the school radio team after my first weather report. I spoke too quickly, and a few classmates laughed when I mixed up two street names. The next day, Kai stayed after school and helped me mark pauses in the script. We recorded the report again on Friday. This time, a student who had missed the bus used our update to find the indoor waiting area. Kai says the best part was not the clear recording but that someone could use it. I think I finally understand why we practice.\n\nHow does the writer most likely feel about the radio team now?",
        "options": ["More willing to continue because the work helped someone", "Angry that Kai changed the script without permission", "Certain that every report must sound perfect", "Uninterested because the first recording was difficult"],
        "explanation": "作者起初因失誤和同學發笑而想退出，但後來與 Kai 重錄，並得知資訊真的幫到錯過公車的學生。結尾說終於理解練習的原因，表示作者重新看見團隊工作的價值，較願意繼續。",
        "strategy": "態度推論要比較人物在事件前後的想法與行動；不能把單一負面情緒當成全文結論。",
        "steps": ["找前段態度：almost quit，顯示作者曾受挫並想退出。", "追蹤改變原因：Kai 陪練，重新錄製後的資訊幫助了另一位學生。", "讀結尾的 finally understand why we practice，辨認作者新的理解。", "排除仍生氣、追求完美或完全沒興趣等沒有文本支持的選項。", "從受挫轉為看見實際幫助，最合理是更願意留下，因此選 A。"],
        "refs": ["yancheng-diary"],
    },
    {
        "answer": "C", "difficulty": "easy", "focus": "閱讀邀請中的時間地點",
        "prompt": "Read the invitation.\n\nDear neighbors,\nOur community garden will open its new herb corner on May 18. Please meet at the east gate at 9:30 a.m. Volunteers will show visitors how to label the plants, and children can take home one small herb pot after the tour. The event will move to the covered court if it rains. Please bring a reusable bag if you plan to take a pot home.\n—Green Lane Garden Group\n\nWhere should visitors go if it rains?",
        "options": ["The east gate at 9:30 p.m.", "The new herb corner on May 19", "The covered court", "The garden office after the tour"],
        "explanation": "邀請函直接交代下雨時活動改到 covered court（有遮棚的球場）。東門是原定集合地點；遇雨時要用條件句中的替代地點。",
        "strategy": "看到 if 條件句時，把「平常安排」與「條件成立後的替代安排」分開記。",
        "steps": ["先確認題目問的是雨天去處，不是原定集合點或日期。", "在邀請函找天氣條件：The event will move ... if it rains。", "擷取 move to 後面的地點 covered court。", "比對選項並排除把時間、日期寫錯或自行增加的辦公室地點。", "雨天方案唯一是 covered court，因此選 C。"],
        "refs": ["yancheng-notice", "sanduo-poster"],
    },
    {
        "answer": "B", "difficulty": "medium", "focus": "辨認文本未提供的資訊",
        "prompt": "Read the short report.\n\nA group of students started a “quiet corner” beside the school garden. During lunch, students can borrow a book, sit under the trees, or write in a journal. The group chose the spot because it is away from the basketball court. Two student volunteers tidy the area each day. The corner is open whenever the garden gate is unlocked.\n\nWhich information is NOT given?",
        "options": ["What students may do there", "How many books a student may borrow", "Why the group chose the location", "Who tidies the area"],
        "explanation": "報告列出可借書、休息或寫日記，說明選址遠離球場，也交代每天由兩位學生志工整理；沒有說明每位學生能借幾本書。",
        "strategy": "NOT 題先把每個選項改寫成待查核命題，再逐一在全文尋找；不可把合理猜測當作文章資訊。",
        "steps": ["圈出 NOT，提醒自己要找全文沒有交代的細節。", "查選項 A：borrow a book、sit、write 均出現在第二句。", "查選項 C 和 D：遠離球場是選址原因，兩位學生志工負責整理。", "全文只有 borrow a book，沒有設定每人可借的數量。", "缺少明確證據的是 B；不能用校園常規自行補出冊數。"],
        "refs": ["neihu-missing"],
    },
    {
        "answer": "D", "difficulty": "hard", "focus": "整合多段資訊選擇主旨",
        "prompt": "Read the passage.\n\nWhen the old footbridge closed for repairs, students in Maple Village had to take a longer road to school. At first, the morning bus was often late. The student council collected arrival times for two weeks and shared the results with the village office. The office changed the bus schedule for the repair period. Students also made a walking map showing the safest route. The bridge is not fixed yet, but families say the new plan has made mornings less stressful.\n\nWhat is the best title for the passage?",
        "options": ["Why Every Student Should Ride a Bus", "A New Bridge Built in Maple Village", "The Student Council Cancels the Morning Route", "How Students and the Village Adjusted to a Bridge Repair"],
        "explanation": "全文先說橋梁維修造成通學不便，再寫學生蒐集到校時間、村公所調整公車、學生製作安全步行圖，最後交代新安排減輕早晨壓力。D 涵蓋問題、合作調整與結果；文章並未說橋已修好。",
        "strategy": "標題需涵蓋整篇的問題、主要回應與結果，不能只抓一個道具或把尚未完成的事寫成已完成。",
        "steps": ["用一句話標記開端問題：橋梁維修使學生通學路線變長。", "整理中段兩項回應：蒐集資料促成公車改時，另製作安全步行圖。", "讀結尾結果：橋仍未修好，但新的安排讓早晨較不緊張。", "檢查標題範圍；A、B、C 分別過度概括、虛構完工或誤稱取消路線。", "D 同時涵蓋學生與村公所的調整及維修背景，是最完整的主旨。"],
        "refs": ["fengjia-main"],
    },
    {
        "answer": "C", "difficulty": "medium", "focus": "依書信內容推論寫信者需求",
        "prompt": "Read the email.\n\nDear Coach Rivera,\nI can attend the Saturday practice, but I will arrive about fifteen minutes late because my piano lesson ends at 9:00. I have already read the new passing-drill instructions you sent. Could you ask a teammate to save me a copy of the team map? I will join the warm-up as soon as I get there.\nThanks,\nNoah\n\nWhat is Noah asking the coach to do?",
        "options": ["Move the piano lesson to another day", "Send the passing-drill instructions for the first time", "Ask a teammate to keep a team map for him", "Let him skip all Saturday practice"],
        "explanation": "Noah 已經讀過傳球練習說明；他具體請教練請隊友替他留一份隊伍地圖。他只會遲到約十五分鐘，並說到場後加入暖身，沒有要求缺席。",
        "strategy": "書信行動題要區分已完成事項、原因說明與真正的請求句，尤其留意 Could you...?。",
        "steps": ["找情態問句 Could you ask ...，它標出 Noah 對教練的請求。", "讀完整請求內容：請隊友替他留一份 team map。", "把前文已讀過的 drill instructions 標成已完成，避免誤選重寄。", "遲到原因是鋼琴課；他仍會參加練習並加入暖身。", "只有 C 忠實描述請求對象與物件，不增添改課或缺席。"],
        "refs": ["guochang-letter"],
    },
]


def source_ref(key: str) -> dict:
    source = SOURCES[key]
    return {
        "url": source["url"],
        "title": source["title"] + "；只參照閱讀能力與題型，不複製原卷文字、選項、資料表或答案。",
        "year": source["year"],
        "subject": "english",
        "locator": source["locator"],
        "locatorLevel": "item",
        "observedPattern": source["observedPattern"],
        "reuseDecision": "pattern-only",
        "status": "recorded",
    }


def main() -> None:
    for index, item in enumerate(ITEMS, 1):
        options = [{"id": chr(65 + i), "text": value} for i, value in enumerate(item["options"])]
        data = {
            "id": f"question-english-performance-3-iv-8-{index}",
            "subject": "english",
            "type": "single-choice",
            "prompt": item["prompt"],
            "options": options,
            "knowledgeIds": ["kg-english-performance-3-iv-8"],
            "difficulty": item["difficulty"],
            "answer": {"value": item["answer"], "explanation": item["explanation"]},
            "provenance": {
                "origin": "original",
                "license": "All rights reserved",
                "sourceUrl": SOURCES[item["refs"][0]]["url"],
                "sourceLocator": "僅將公立學校公開英語評量的短篇閱讀理解能力作 pattern-only 參照；本文、選項、答案與解析均獨立撰寫。",
                "authoringNote": "Original English text and item authored for KG 3-Ⅳ-8; public-school exam references inform only the skill pattern. Publisher-version fusion, rights/content review, and second-round review remain incomplete; keep draft.",
            },
            "reviewStatus": "draft",
            "updatedAt": "2026-09-26",
            "lessonId": "lesson-english-performance-3-iv-8",
            "examPatternRefs": [source_ref(key) for key in item["refs"]],
            "solutionStrategy": item["strategy"],
            "solutionSteps": item["steps"],
        }
        path = OUT / f"question-english-performance-3-iv-8-{index}.json"
        path.write_text(json.dumps(data, ensure_ascii=False, indent=2) + "\n", encoding="utf-8")
    print(f"rewrote {len(ITEMS)} original questions; answers: " + ",".join(item["answer"] for item in ITEMS))


if __name__ == "__main__":
    main()
