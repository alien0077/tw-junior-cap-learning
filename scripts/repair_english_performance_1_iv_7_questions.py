import json
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
OUT = ROOT / "questions/english"

SOURCES = {
    "yc": {
        "url": "https://www.ycjh.hlc.edu.tw/modules/tad_uploader/index.php?cat_sn=432&cfsn=2875&fn=113-1-%E7%AC%AC1%E6%AC%A1%E6%AE%B5%E8%80%839%E5%B9%B4%E7%B4%9A%E8%8B%B1%E8%AA%9E%E7%A7%91%E9%A1%8C%E7%9B%AE%E8%88%87%E7%AD%94%E6%A1%88-%E9%82%B1%E6%9B%89%E8%96%87.pdf&op=dlfile",
        "title": "花蓮縣立宜昌國中113學年度第一學期九年級第一次段考英文試題與答案",
        "year": "113-1", "locator": "PDF第3頁第27題（用途判讀）",
        "pattern": "以短篇說明／產品資訊詢問文本用途；本題改用校園雨水設備，僅借用目的判讀能力，不沿用原材料、文字、答案或選項。",
    },
    "yc_main": {
        "url": "https://www.ycjh.hlc.edu.tw/modules/tad_uploader/index.php?cat_sn=432&cfsn=2875&fn=113-1-%E7%AC%AC1%E6%AC%A1%E6%AE%B5%E8%80%839%E5%B9%B4%E7%B4%9A%E8%8B%B1%E8%AA%9E%E7%A7%91%E9%A1%8C%E7%9B%AE%E8%88%87%E7%AD%94%E6%A1%88-%E9%82%B1%E6%9B%89%E8%96%87.pdf&op=dlfile",
        "title": "花蓮縣立宜昌國中113學年度第一學期九年級第一次段考英文試題與答案",
        "year": "113-1", "locator": "PDF第3頁第30題（閱讀主旨）",
        "pattern": "讀完整篇後整合跨句重點判讀主旨；本題採全新海岸觀測短文與不同推理線索。",
    },
    "yc_fact": {
        "url": "https://www.ycjh.hlc.edu.tw/modules/tad_uploader/index.php?cat_sn=432&cfsn=2875&fn=113-1-%E7%AC%AC1%E6%AC%A1%E6%AE%B5%E8%80%839%E5%B9%B4%E7%B4%9A%E8%8B%B1%E8%AA%9E%E7%A7%91%E9%A1%8C%E7%9B%AE%E8%88%87%E7%AD%94%E6%A1%88-%E9%82%B1%E6%9B%89%E8%96%87.pdf&op=dlfile",
        "title": "花蓮縣立宜昌國中113學年度第一學期九年級第一次段考英文試題與答案",
        "year": "113-1", "locator": "PDF第3頁第31題（根據文章判斷正確敘述）",
        "pattern": "逐項比對陳述與短文明示資訊；新題使用不同情境且選項均由新文本生成。",
    },
    "yc_cause": {
        "url": "https://www.ycjh.hlc.edu.tw/modules/tad_uploader/index.php?cat_sn=432&cfsn=2875&fn=113-1-%E7%AC%AC1%E6%AC%A1%E6%AE%B5%E8%80%839%E5%B9%B4%E7%B4%9A%E8%8B%B1%E8%AA%9E%E7%A7%91%E9%A1%8C%E7%9B%AE%E8%88%87%E7%AD%94%E6%A1%88-%E9%82%B1%E6%9B%89%E8%96%87.pdf&op=dlfile",
        "title": "花蓮縣立宜昌國中113學年度第一學期九年級第一次段考英文試題與答案",
        "year": "113-1", "locator": "PDF第4頁第36題（閱讀中的原因判讀）",
        "pattern": "從說明文辨認造成結果的明示原因；本題另寫圖書修補情境，未重用來源敘事。",
    },
    "yc_chart": {
        "url": "https://www.ycjh.hlc.edu.tw/modules/tad_uploader/index.php?cat_sn=432&cfsn=2875&fn=113-1-%E7%AC%AC1%E6%AC%A1%E6%AE%B5%E8%80%839%E5%B9%B4%E7%B4%9A%E8%8B%B1%E8%AA%9E%E7%A7%91%E9%A1%8C%E7%9B%AE%E8%88%87%E7%AD%94%E6%A1%88-%E9%82%B1%E6%9B%89%E8%96%87.pdf&op=dlfile",
        "title": "花蓮縣立宜昌國中113學年度第一學期九年級第一次段考英文試題與答案",
        "year": "113-1", "locator": "PDF第4頁第37題（比較圖表資訊）",
        "pattern": "跨類別比較圖表中不同區段的數值；本題自行提供全新圖書館借閱表與比較目標。",
    },
    "ks_infer": {
        "url": "https://csjh.kl.edu.tw/books/file/528/111-1%E7%AC%AC%E4%B8%89%E6%AC%A1%E5%9C%8B%E4%B8%89%E6%AE%B5%E8%80%83%E8%A9%A6%E9%A1%8C.pdf",
        "title": "基隆市立中山高級中學國中部111學年度第一學期九年級第三次段考英文試題",
        "year": "111-1", "locator": "PDF第4頁第34題（由事件線索推測後續）",
        "pattern": "整合事件及人物處境推測有文本支持的後續行動；本題採天文社借用器材的全新事件。",
    },
    "ks_topic": {
        "url": "https://csjh.kl.edu.tw/books/file/528/111-1%E7%AC%AC%E4%B8%89%E6%AC%A1%E5%9C%8B%E4%B8%89%E6%AE%B5%E8%80%83%E8%A9%A6%E9%A1%8C.pdf",
        "title": "基隆市立中山高級中學國中部111學年度第一學期九年級第三次段考英文試題",
        "year": "111-1", "locator": "PDF第4頁第36題（說明文主題）",
        "pattern": "辨認說明文涵蓋的整體主題，而非擷取單一細節；本題另寫城市屋頂農園介紹。",
    },
    "ks_main": {
        "url": "https://csjh.kl.edu.tw/books/file/528/111-1%E7%AC%AC%E4%B8%89%E6%AC%A1%E5%9C%8B%E4%B8%89%E6%AE%B5%E8%80%83%E8%A9%A6%E9%A1%8C.pdf",
        "title": "基隆市立中山高級中學國中部111學年度第一學期九年級第三次段考英文試題",
        "year": "111-1", "locator": "PDF第4頁第33題（閱讀主旨）",
        "pattern": "從多段資訊整合文章整體主旨；本題自行撰寫午餐減少剩食的全新說明文。",
    },
    "jx_true": {
        "url": "https://www.chhs.tp.edu.tw/uploads/1642655973756S6WiICcM.pdf",
        "title": "臺北市立景興國民中學110學年度第一學期第三次定期評量八年級英文試題",
        "year": "110-1", "locator": "PDF第2頁第31題（依故事判斷正確敘述）",
        "pattern": "辨識敘事中可由明示內容支持的事實；本題另寫校園物品遺失公告，不重用人物或情節。",
    },
    "jx_cause": {
        "url": "https://www.chhs.tp.edu.tw/uploads/1642655973756S6WiICcM.pdf",
        "title": "臺北市立景興國民中學110學年度第一學期第三次定期評量八年級英文試題",
        "year": "110-1", "locator": "PDF第2頁第32題（說明違規原因）",
        "pattern": "將行為與明示規則連結，選出事件原因；本題另寫博物館保存措施。",
    },
    "jx_infer": {
        "url": "https://www.chhs.tp.edu.tw/uploads/1642655973756S6WiICcM.pdf",
        "title": "臺北市立景興國民中學110學年度第一學期第三次定期評量八年級英文試題",
        "year": "110-1", "locator": "PDF第2頁第33題（由對話反推言外事實）",
        "pattern": "從角色話語及前文情境推回最受支持的隱含事實；新題改採校園修繕通知的語篇線索。",
    },
}

ITEMS = [
    {
        "answer": "C", "source": "yc_main", "skill": "主旨統整",
        "passage": "A group of students visits the same beach every month. They record the amount of litter, photograph changes in the sand, and send the results to the town office. The project does not clean the whole coast in one day; it helps the town decide where to place more bins.",
        "ask": "Which is the best main idea?",
        "options": ["The students opened a new beach restaurant.", "The town closed the beach for a month.", "Students collect beach data to help the town plan waste bins.", "Photographs are the only useful part of the project."],
        "why": "每月記錄垃圾與沙灘變化，最後把資料交給鎮公所決定垃圾桶位置；核心是以觀察資料協助規劃，而不是清完海岸或經營餐廳。",
        "steps": ["先看題目問整篇主旨，不是某個細節。", "找出學生反覆做的事：記錄垃圾、拍攝變化、回報資料。", "再讀最後一句，確認資料的用途是協助決定垃圾桶位置。", "比較選項：C 同時涵蓋觀察和規劃用途，其餘不是文中重點或與文意相反。", "答案選 C；可用「誰做什麼、為了什麼」濃縮全文。"],
    },
    {
        "answer": "A", "source": "yc", "skill": "寫作目的",
        "passage": "Before the science room closes, place the sensor in its case, wipe the table with a dry cloth, and write any broken parts on the checkout sheet. Leave the case on the blue shelf so the next class can find it.",
        "ask": "Why was this note most likely written?",
        "options": ["To explain how to put shared science equipment away", "To invite students to a sports contest", "To describe how sensors are made", "To tell students to take the equipment home"],
        "why": "連續的祈使句交代歸還、清潔、登記與放置方法，目的是讓使用者照步驟整理共用器材。",
        "steps": ["先辨認文本形式：它是一張操作提醒，不是故事。", "圈出動作詞 place、wipe、write、leave。", "確認這些動作都發生在關門前，且指向整理器材。", "排除比賽邀請、製造說明及帶回家等沒有文本線索的選項。", "答案選 A；讀操作告示時，用動詞串出作者希望讀者完成的任務。"],
    },
    {
        "answer": "D", "source": "ks_topic", "skill": "說明文主題",
        "passage": "Several apartment buildings have turned unused rooftops into small gardens. Residents grow herbs in light containers, collect rain for watering, and take turns checking the plants. The gardens also give neighbors a place to meet after work.",
        "ask": "Which topic best covers the whole passage?",
        "options": ["How to build a tall apartment building", "Why herbs should never be watered", "A schedule for residents to commute", "How rooftop gardens serve residents and their neighborhood"],
        "why": "短文涵蓋屋頂種植、收集雨水、輪值照料，以及鄰居交流；D 能包住各層資訊，其他只提到無關或片面內容。",
        "steps": ["將每句的關鍵對象標出：公寓屋頂花園。", "整理用途一：種香草、節水、照顧植物。", "整理用途二：提供鄰居下班後見面的地方。", "挑選能涵蓋兩類用途的選項，避免把單一細節當全文主題。", "答案選 D；主題範圍要剛好能統整全部重要句子。"],
    },
    {
        "answer": "B", "source": "yc_fact", "skill": "明示細節查找",
        "passage": "The school repair team meets in Room 204 on Thursday afternoons. Students may bring a broken umbrella, but they should attach a note with their name. The team repairs small parts; it cannot replace a missing handle.",
        "ask": "Which statement is true according to the notice?",
        "options": ["The team meets every morning.", "Students should put their names on a note.", "The team replaces every missing umbrella handle.", "The repair room is open on Sunday."],
        "why": "告示明確要求學生在物品上附姓名便條；聚會時間是週四下午，且不會補換遺失的傘柄。",
        "steps": ["這題問 true statement，逐項都要回文章核對。", "選項 A 的 morning 與 Thursday afternoons 不符。", "選項 B 對照 attach a note with their name，內容吻合。", "選項 C 把「不能補換傘柄」說成會補換；D 的 Sunday 未出現。", "答案選 B；不要憑常識判斷，需找到原文句子作證。"],
    },
    {
        "answer": "C", "source": "yc_cause", "skill": "因果線索",
        "passage": "The library's oldest picture books were losing pages. Many had been stored beside a sunny window, where heat made the paper dry and easy to crack. The librarian moved them to closed boxes in a cooler room.",
        "ask": "What made the pages easy to crack?",
        "options": ["The books were moved to another room.", "The librarian put the books in boxes.", "Heat near the sunny window dried the paper.", "The library stopped lending picture books."],
        "why": "文中以 where 連接原因：窗邊熱度使紙張乾燥，乾燥後更容易裂；搬到盒中是後續保護措施。",
        "steps": ["先定位結果：紙頁變乾、容易裂，這是題目追問的現象。", "往前找和 where 相連的環境線索：靠窗且受熱。", "按因果順序整理：窗邊熱 → 紙張乾 → 容易裂。", "排除裝盒和移房，因為那是館員後來採取的保護行動。", "答案選 C；分清造成問題的原因與事後處理方法。"],
    },
    {
        "answer": "D", "source": "yc_chart", "skill": "圖表比較",
        "passage": "The school library recorded the number of graphic novels borrowed in one week. Grade 7: 18; Grade 8: 26; Grade 9: 21. The librarian plans to order more books for the grade with the highest borrowing number.",
        "ask": "Which grade should receive the largest new order based on the record?",
        "options": ["Grade 7, because 18 is the smallest number", "Grade 9, because it is the oldest grade", "All grades equally; the numbers are identical", "Grade 8, because 26 is the largest number"],
        "why": "三個數值依序為 18、26、21；26 最大，且規則說要為借閱最多的年級多訂書。",
        "steps": ["把題目要求轉成比較目標：找借閱數最高的年級。", "逐一對照資料：七年級 18、八年級 26、九年級 21。", "先比較 26 與 18，再比較 26 與 21，確認 26 最大。", "依館員規則，最高借閱量對應最多新書訂購。", "答案選 D；圖表題先讀比較條件，再找最大／最小值，不要被年級年齡帶偏。"],
    },
    {
        "answer": "A", "source": "jx_cause", "skill": "規則與原因",
        "passage": "A museum keeps its paper maps in a dim room. Visitors may view one map at a time, but they must return it before taking another. The guide explains that bright light can fade the ink, so the maps are shown only briefly.",
        "ask": "Why are the maps shown only briefly?",
        "options": ["Bright light can make the ink fade.", "Visitors are not allowed to read maps.", "The museum has no paper maps.", "The guide wants visitors to draw on the maps."],
        "why": "because 引出的原因是強光會使墨色褪去，所以展示時間受到限制。",
        "steps": ["找到問句中的 why，回文尋找因果標記。", "文中 because 後面直接說明 bright light can fade the ink。", "把因果方向確認一次：怕褪色，所以縮短展示時間。", "其餘選項與規則相反或無文本支持。", "答案選 A；看到 because、so 時，檢查原因和結果是否配對。"],
    },
    {
        "answer": "B", "source": "ks_infer", "skill": "線索推論",
        "passage": "The astronomy club borrowed two rooftop lenses for Friday's sky watch. On Thursday evening, the forecast changed to heavy rain. The club leader posted that members should bring their notebooks to the library at the same time instead.",
        "ask": "What will the club most likely do on Friday?",
        "options": ["Cancel every meeting for the rest of the year", "Meet indoors and use notebooks instead of watching the sky", "Leave the lenses outside during the storm", "Start the sky watch earlier on Thursday"],
        "why": "天氣預報變成大雨，負責人改通知在相同時間到圖書館帶筆記本；因此活動轉為室內，並非直接取消整年或仍在屋頂觀星。",
        "steps": ["先整理時間線：原定週五屋頂觀星，週四預報改變。", "抓住新指令：同一時間改到圖書館，帶筆記本。", "推論活動形式因雨而轉室內，並用筆記本進行替代安排。", "排除超出文本的全年取消、把器材留在雨中及改到週四。", "答案選 B；推論只走到線索支持的最近一步，不加上文中沒有的計畫。"],
    },
    {
        "answer": "C", "source": "jx_true", "skill": "多條件細節核對",
        "passage": "NOTICE: The lost-and-found desk is beside the gym office. Items are kept for two weeks. To claim an item, describe one feature that is not written on its label. Unclaimed items are then sent to the community reuse shelf.",
        "ask": "Which statement matches the notice?",
        "options": ["The desk is inside the school cafeteria.", "Students can claim an item by reading its label aloud.", "A claimant needs to tell a feature not shown on the label.", "Unclaimed items are thrown away the same day."],
        "why": "告示要求領取者說出標籤未寫的一項特徵；其他選項分別錯置地點、反轉辨認規則、改掉保留期限與後續去向。",
        "steps": ["把告示拆成地點、期限、領取條件、未領物品去向四類資訊。", "題目選項 C 對應領取條件 describe one feature not written on its label。", "核查 A：gym office 旁，不是 cafeteria 內。", "核查 B、D：需提供標籤外特徵；未領物送到 reuse shelf，不是當天丟棄。", "答案選 C；細節題可逐欄比對，留意選項把限定詞悄悄改掉。"],
    },
    {
        "answer": "D", "source": "ks_main", "skill": "跨句整合與摘要",
        "passage": "For three weeks, the school cafeteria weighed untouched fruit left after lunch. The amount fell when students could choose a smaller first serving and return for more. The nutrition teacher says the change reduced waste without limiting anyone's choice of fruit.",
        "ask": "Which sentence best summarizes the report?",
        "options": ["The cafeteria stopped serving fruit at lunch.", "Students were required to finish every meal.", "The teacher replaced lunch with a nutrition class.", "Offering flexible portions helped reduce leftover fruit while keeping choice."],
        "why": "摘要須同時保留做法、結果與限制條件：可先取小份、不夠再添，剩果減少，而且仍可選水果。",
        "steps": ["先標出報告目的：追蹤午餐後未吃水果的量。", "找出改變措施：可先取小份，需要時再添。", "找出結果與條件：剩果下降，水果選擇沒有被限制。", "逐項排除把供應取消、強迫吃完或改上課等捏造資訊。", "答案選 D；完整摘要要保留核心做法和結果，不能只抓一個數字或細節。"],
    },
]


def make(index, item):
    src = SOURCES[item["source"]]
    ref = {
        "url": src["url"], "title": src["title"] + "；僅參考閱讀題型，不複製原文、人物、數據、選項或答案。",
        "year": src["year"], "subject": "english", "locator": src["locator"],
        "observedPattern": src["pattern"], "reuseDecision": "pattern-only", "status": "recorded", "locatorLevel": "item",
    }
    choices = item["options"]
    options = [{"id": chr(65 + n), "text": text} for n, text in enumerate(choices)]
    return {
        "id": f"question-english-performance-1-iv-7-{index}", "subject": "english", "type": "single-choice",
        "prompt": item["passage"] + "\n\n" + item["ask"], "options": options,
        "knowledgeIds": ["kg-english-performance-1-iv-7"], "difficulty": "medium",
        "answer": {"value": item["answer"], "explanation": item["why"] + f" 正確答案：{item['answer']}。"},
        "provenance": {"origin": "original", "license": "All rights reserved", "sourceUrl": src["url"],
            "sourceLocator": src["locator"] + "；僅改寫閱讀能力模式，不複製原題內容。",
            "authoringNote": "題幹、短文、選項、解析與遷移內容均為原創；以公立學校公開英文原卷的指定閱讀題型作 pattern-only 參照。內容維持 draft；Terra 審查已依使用者指示取消。"},
        "reviewStatus": "draft", "updatedAt": "2026-09-24", "lessonId": "lesson-english-performance-1-iv-7",
        "examPatternRefs": [ref],
        "solutionStrategy": f"{item['skill']}：先把題目要求轉成明確閱讀任務，再圈出支持答案的原文線索，逐一排除與文本矛盾或超出文本的說法。",
        "solutionSteps": item["steps"],
    }


for index, item in enumerate(ITEMS, 1):
    path = OUT / f"question-english-performance-1-iv-7-{index}.json"
    path.write_text(json.dumps(make(index, item), ensure_ascii=False, indent=2) + "\n", encoding="utf-8")
print(f"rewrote {len(ITEMS)} original reading questions with item-level public-exam patterns")
