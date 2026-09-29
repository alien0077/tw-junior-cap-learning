#!/usr/bin/env python3
"""Rewrite English 3-Ⅳ-4 questions from checked public-school chart items."""

import json
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
BASE = ROOT / "questions/english/question-english-performance-3-iv-4-{}.json"

SOURCES = {
    "sanduo": {
        "url": "https://www.sdjh.ntpc.edu.tw/app/index.php?Action=downloadfile&cg=837&file=WVhSMFlXTm9Mekk0TDNCMFlWOHpORFUyWHpFd01EazJNalZmT1RNek56Z3VjR1Jt&fname=WW54RPOKRK4411HHHCLKRKZWQOTWWT14QO3435HGTX25LK40FCNKA054WW54KLOKZTPOEH00A40405JG34MOTSRLSTB0WSHCGGRLDCTSROB0WXSWUSGGCDFCPK44JD25DGA0XWZWXSJCDCWS50B0CCNKVX51UTOOLKUSFCSWIGOOYSUSROXWQP104410VWYWOO14CGNPIGRO14KKUTXT04B5DCMKNKB0WSDCKLQKYWLKCD01WW04NKMOB03035HCKLB0QL14LPZTQP21UWTSVTKLSS54PKSW",
        "title": "新北市立三多國中113學年度第一學期八年級第一次段考英語科試題卷",
        "year": "113-1",
        "locator": "PDF第4頁第42–45題：依社團偏好、可參加時段、聚會日期與時間表交叉判讀",
        "pattern": "題目把個人偏好／空閒時段和多列社團時地表對照，要求找出可行選項或由固定例行活動推知當下活動；本題改用全新資料。",
    },
    "neihu": {
        "url": "https://www.nhjh.tp.edu.tw/uploads/1753839175199ERtbxbag.pdf",
        "title": "臺北市立內湖國中113學年度第二學期七年級第三次段考英語科試題卷",
        "year": "113-2",
        "locator": "PDF第3頁第52–54題：讀泳池開放時段表並結合星期、目前時間作判斷",
        "pattern": "先辨認平日與週末不同開放時段，再依對話中的星期及現在時間推斷可否入場；本題改寫成全新場館與時刻。",
    },
}

ITEMS = [
    {
        "source": "sanduo", "locator": "PDF第4頁第43題：依社團成員興趣推定最可能參加的活動", "answer": "C",
        "prompt": "A youth center chart lists: Robotics—Tue 4:00–5:30, Lab A; Choir—Wed 4:00–5:00, Music Room; Garden Team—Sat 9:00–11:00, Courtyard. Mia is free Wednesday after 4:00 and wants to sing. Which activity fits both clues?",
        "options": ["Robotics in Lab A", "Garden Team in the Courtyard", "Choir in the Music Room", "Any activity on Tuesday"],
        "explanation": "The chart gives Choir on Wednesday from 4:00 to 5:00 in the Music Room. That matches both Mia’s available day and her interest in singing; the other rows fail at least one condition.",
        "strategy": "把人物條件拆成「哪天有空」和「想做什麼」兩欄，逐列同時核對，不能只命中其中一項。",
        "steps": ["先圈出兩個條件：Mia 星期三四點後有空，而且想唱歌。", "在表中找星期三的列，不先用活動名稱猜答案。", "該列是 Choir，時間 4:00–5:00，地點為 Music Room。", "合唱同時符合星期和興趣；機器人是星期二，園藝是星期六，皆不合。", "因此選 C。讀表格的人物配對題要用所有限制交集，不可只看偏好。"],
    },
    {
        "source": "sanduo", "locator": "PDF第4頁第43題：把個人偏好欄與社團活動配對", "answer": "B",
        "prompt": "A school survey table shows each learner’s two favorite activities: Evan—drawing and coding; Nia—dance and cooking; Omar—coding and chess. The Coding Studio meets on Thursday. Who has a stated interest that matches the studio?",
        "options": ["Nia only", "Evan and Omar", "Evan and Nia", "All three students"],
        "explanation": "Coding appears in Evan’s and Omar’s preference entries, but not Nia’s. The meeting day is extra information and does not change which preferences match.",
        "strategy": "先鎖定題目問的是「誰的偏好符合」，再逐格搜尋關鍵活動；不要被多出的星期資訊帶偏。",
        "steps": ["確認任務是找出偏好欄含 coding 的學生。", "逐格讀 Evan：drawing、coding，符合。", "再讀 Nia：dance、cooking，不符合；Omar：coding、chess，符合。", "Thursday 只說明社團何時開，不是判斷偏好的條件。", "答案為 B。資料表題先分清必要條件和背景資訊。"],
    },
    {
        "source": "sanduo", "locator": "PDF第4頁第42題：將可參加的週末時段與活動時間表比對", "answer": "D",
        "prompt": "A community class schedule says: Photo Walk—Saturday 8:30–10:00 a.m.; Board Games—Saturday 2:00–4:00 p.m.; Story Circle—Sunday 10:00–11:30 a.m. A student is free at 9:00 a.m. on Saturday and wants an outdoor activity. Which class is the match?",
        "options": ["Board Games", "Story Circle", "None, because classes begin after noon", "Photo Walk"],
        "explanation": "At 9:00 a.m. Saturday, Photo Walk is already within its 8:30–10:00 time window and is the outdoor activity. The other listed options occur at different times or on a different day.",
        "strategy": "把日期、時間區間、活動特性分開核對；時刻落在起訖端點之間才算可參加。",
        "steps": ["把可用時段寫成 Saturday 9:00 a.m.，另記需求是戶外活動。", "逐列比日期：Photo Walk 和 Board Games 在星期六，Story Circle 在星期日。", "比較兩個星期六時段：9:00 落在 8:30–10:00 之內，不在 2:00–4:00 之內。", "Photo Walk 是戶外散步；故日期、時間和活動需求三項都吻合。", "答案選 D。閱讀行程表時不要只看同一天，還要做區間比較。"],
    },
    {
        "source": "sanduo", "locator": "PDF第4頁第44題：由社團時刻表及活動內容判斷所在場次", "answer": "A",
        "prompt": "A chart gives these weekly club meetings: Debate—Monday 3:30 p.m., Room 12; Orchestra—Wednesday 4:00 p.m., Music Hall; Climbing—Saturday 9:00 a.m., Sports Center. Leo says, 'I am in the music hall at 4:00 on Wednesday.' Which club is he attending?",
        "options": ["Orchestra", "Debate", "Climbing", "The chart does not give a club at that time"],
        "explanation": "Only Orchestra is scheduled in the Music Hall at 4:00 p.m. on Wednesday. The other entries differ by day, time, or place.",
        "strategy": "將人提供的時間和地點當作兩個索引，先找同時符合的資料列，再讀活動名稱。",
        "steps": ["從敘述抽出 Wednesday、4:00 p.m.、Music Hall 三個線索。", "依星期先比對表格，只有 Orchestra 在星期三。", "核對時間為下午四點，地點也正是 Music Hall。", "Debate 在星期一且在 Room 12；Climbing 在星期六且在 Sports Center。", "所以 Leo 參加 Orchestra，選 A。多條件定位須三項都相符。"],
    },
    {
        "source": "sanduo", "locator": "PDF第4頁第42–44題：從活動、時間、地點欄位取得表內資訊", "answer": "C",
        "prompt": "A club chart has columns for Activity, Day, Time, and Place. Which question can be answered directly from those columns?",
        "options": ["Why does a student enjoy the activity?", "How many new friends will a student make?", "Where does the activity meet?", "Will the club become more popular next year?"],
        "explanation": "The Place column states the meeting location, so C is directly supported. The chart contains no evidence about personal reasons, future popularity, or friendships.",
        "strategy": "答案範圍不能超過圖表提供的欄位；直接資料、合理推論和沒有證據的預測要分開。",
        "steps": ["逐一讀出表頭：Activity、Day、Time、Place。", "把選項改寫成要找的資料種類：原因、交友情況、地點、未來人氣。", "只有 meeting place 對應表格明列的 Place 欄。", "其餘三項都需要表外的個人感受或未來資料，不能由表格證明。", "答案是 C。資料判讀要拒絕看似合理但沒有欄位支持的延伸。"],
    },
    {
        "source": "neihu", "locator": "PDF第3頁第52題：讀取泳池平日／週末分段開放時刻表", "answer": "B",
        "prompt": "A riverside pool lists weekday hours as 6:30–11:00 a.m. and 4:30–8:00 p.m.; weekend hours are 9:00 a.m.–6:00 p.m. A family arrives at 7:15 p.m. on Friday. What does the schedule show?",
        "options": ["The pool is closed all day Friday.", "The pool is open, because 7:15 p.m. falls in its Friday evening session.", "The family must use the weekend hours.", "The pool closes at 8:00 a.m."],
        "explanation": "Friday is a weekday, so use the weekday row. 7:15 p.m. is later than 4:30 p.m. and earlier than 8:00 p.m.; it falls within the evening session.",
        "strategy": "先決定套用平日或週末那列，再把到達時刻放進上午／下午的開放區間檢查。",
        "steps": ["先分類星期：Friday 屬於 weekday，不使用 weekend 欄。", "從平日資料讀出晚間時段 4:30–8:00 p.m.。", "確認 7:15 p.m. 晚於 4:30 且早於 8:00。", "所以抵達時間落在仍開放的區間；D 把 p.m. 誤看成 a.m.。", "答案選 B。多時段表要先選正確列，再核對時間端點與 a.m./p.m.。"],
    },
    {
        "source": "neihu", "locator": "PDF第3頁第53題：依星期及當下時刻判斷距離開放時間", "answer": "D",
        "prompt": "A science center is open Monday–Friday from 9:00 a.m. to 5:00 p.m. and on weekends from 10:00 a.m. to 4:00 p.m. It is Sunday, 9:40 a.m. Which conclusion is supported?",
        "options": ["It closed at 9:00 a.m.", "The weekday schedule applies because it is before noon.", "It will stay open until 5:00 p.m. today.", "It has not opened yet; the Sunday opening time is 10:00 a.m."],
        "explanation": "Sunday uses the weekend row, which begins at 10:00 a.m. Since it is 9:40 a.m., the center has not opened yet. The weekday hours do not apply.",
        "strategy": "別用時間先後取代星期分類；選到正確欄後，才判斷現在是未開、營業中或已關門。",
        "steps": ["先確定 today is Sunday，選用 weekends 的時段。", "週末開放時間是 10:00 a.m.–4:00 p.m.。", "現在 9:40 a.m. 比開門時間早 20 分鐘。", "因此尚未開放；C 把平日 5:00 p.m. 套到星期日。", "答案 D。先選對日別資料，再比較目前時間。"],
    },
    {
        "source": "sanduo", "locator": "PDF第4頁第42題：比對同伴共同空閒時段與社團時間", "answer": "A",
        "prompt": "A schedule shows two weekend options: Nature Sketching, Saturday 9:00–11:00 a.m. at Hill Park; and Indoor Chess, Sunday 1:00–3:00 p.m. in Room 5. Both Kai and Uma are free Saturday morning. Which statement is supported?",
        "options": ["They can attend Nature Sketching together if they choose it.", "They can attend both activities at the same time.", "Chess meets at Hill Park.", "They are free on Sunday afternoon."],
        "explanation": "Both students share the Saturday-morning availability, which overlaps the Nature Sketching session. The chart does not say they are free Sunday, and the two activities occur at different times and places.",
        "strategy": "比較兩人的共同空檔和活動時段；只有交集能支持「一起參加」，不能把兩個不同場次混成同時。",
        "steps": ["找出兩人共同有空的時間：Saturday morning。", "Nature Sketching 在星期六上午 9–11 點，時間重疊。", "地點是 Hill Park，對一起參加這個戶外課程沒有衝突。", "Chess 在星期日下午且位於 Room 5，不是兩人已知共同空檔，也非同一時段。", "故 A 可由資料支持。判斷共同活動要看時間交集與場地資訊。"],
    },
    {
        "source": "sanduo", "locator": "PDF第4頁第42–44題：以表內數值與欄位支持有限結論", "answer": "C",
        "prompt": "A library chart records visitors: Monday 42, Tuesday 55, Wednesday 55, Thursday 38. Which statement is exactly supported by the data?",
        "options": ["Thursday had the most visitors.", "Tuesday had more visitors than every other day.", "Tuesday and Wednesday tied for the highest count.", "The library was busiest because of a special event."],
        "explanation": "Tuesday and Wednesday both show 55, which is greater than Monday’s 42 and Thursday’s 38. The chart gives counts but no cause for the higher attendance.",
        "strategy": "先比較最大值並留意並列；接著檢查選項是否偷偷加入表格未提供的原因。",
        "steps": ["把四天的數字按大小比較：42、55、55、38。", "最大值是 55，且出現兩次，分別屬於 Tuesday 和 Wednesday。", "所以兩天並列最高，並非 Tuesday 單獨超過所有日子。", "特殊活動可能是原因，但表格沒有活動紀錄，不能據此下結論。", "答案為 C。表格能支持數值比較，不一定能解釋造成數值的原因。"],
    },
    {
        "source": "sanduo", "locator": "PDF第4頁第42、44題：合併活動類型與時段篩選", "answer": "D",
        "prompt": "A school event table lists: Art Show—Friday 1:00–2:00 p.m., Room A; Science Demo—Friday 2:30–3:30 p.m., Lab; Book Swap—Saturday 10:00–11:00 a.m., Library. You are free Friday after 2:00 and want a science activity. Which event meets both conditions?",
        "options": ["Art Show", "Book Swap", "No event fits because the Lab is closed", "Science Demo"],
        "explanation": "Science Demo is the only science activity and takes place Friday 2:30–3:30 p.m., which is after 2:00. The other choices do not satisfy the subject and time conditions together.",
        "strategy": "把「星期／時間」和「活動類型」做交叉篩選，逐筆刪去不符合者，避免只憑關鍵字作答。",
        "steps": ["記下限制：星期五兩點後有空，且想參加科學活動。", "檢查 Art Show：雖在星期五，但一點到兩點，沒有符合兩點後。", "檢查 Science Demo：星期五兩點半到三點半，且是科學活動。", "Book Swap 在星期六，也不是科學活動；表內沒有 Lab 關閉資訊。", "所以選 D。選項要同時通過每個條件，不能自行補入未列出的限制。"],
    },
]


def main():
    for number, item in enumerate(ITEMS, start=1):
        path = BASE.with_name(BASE.name.format(number))
        question = json.loads(path.read_text())
        source = SOURCES[item["source"]]
        ref = {
            "url": source["url"], "title": source["title"], "year": source["year"],
            "subject": "english", "locator": item.get("locator", source["locator"]),
            "observedPattern": source["pattern"], "pattern": source["pattern"],
            "reuseDecision": "pattern-only", "status": "recorded", "locatorLevel": "item",
        }
        question["prompt"] = item["prompt"]
        question["options"] = [{"id": chr(65 + i), "text": text} for i, text in enumerate(item["options"])]
        question["answer"] = {"value": item["answer"], "explanation": item["explanation"]}
        question["provenance"]["sourceUrl"] = source["url"]
        question["provenance"]["sourceLocator"] = item.get("locator", source["locator"])
        question["provenance"]["authoringNote"] = "依公立學校公開段考的圖表／時刻表判讀能力模式獨立創作；原始情境、資料、題幹、選項、答案與解析均重新撰寫，僅作 pattern-only 參照。仍待完整內容與版權 QA。"
        question["examPatternRefs"] = [ref]
        question["solutionStrategy"] = item["strategy"]
        question["solutionSteps"] = item["steps"]
        question["reviewStatus"] = "draft"
        question["updatedAt"] = "2026-09-24"
        path.write_text(json.dumps(question, ensure_ascii=False, indent=2) + "\n")
    print(f"rewrote {len(ITEMS)} original chart-reading questions")


if __name__ == "__main__":
    main()
