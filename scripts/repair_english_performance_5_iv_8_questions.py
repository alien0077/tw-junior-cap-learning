import json
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
OUT = ROOT / "questions/english"

SOURCES = {
    "dawwan": {
        "url": "https://www.dwm.kh.edu.tw/upload/344/104_64184/109-1-1%E8%8B%B1%E6%96%87%E4%B8%89%E5%B9%B4%E7%B4%9A%E8%A9%A6%E9%A1%8C.pdf",
        "title": "高雄市立大灣國中109學年度第1學期第1次段考九年級英語科試題",
        "year": "109-1",
        "locator": "PDF第4頁閱讀測驗第1-3題；故事人物、原因、事件結果",
        "pattern": "以連續故事中的角色關係、行動原因及發生結果作理解，不挪用夢境、角色、句子或選項。",
    },
    "guochang": {
        "url": "https://www.kcjh.kh.edu.tw/upload/190/104_34764/3-%E8%8B%B1%E6%96%87.pdf",
        "title": "高雄市立國昌國中113學年度第2學期第1次段考九年級英語科試題",
        "year": "113-2",
        "locator": "PDF第7頁閱讀測驗第46-47題；篇章主旨與由事件證據推論",
        "pattern": "以篇章主旨和跨句證據判斷事件關係，不挪用畫作主題、年代、人物、句子或選項。",
    },
    "xiaogang": {
        "url": "https://w3.hkjh.kh.edu.tw/%E5%B0%8F%E6%B8%AF%E5%9C%8B%E4%B8%AD%E6%AE%B5%E8%80%83%E8%A9%A6%E9%A1%8C/32%E4%B8%89%E5%B9%B4%E7%B4%9A%E4%B8%8B%E5%AD%B8%E6%9C%9F/1%E7%AC%AC%E4%B8%80%E6%AC%A1%E6%AE%B5%E8%80%83%E8%A9%A6%E9%A1%8C/%E8%8B%B1%E8%AA%9E/105-2-1%20%E4%B8%89%E5%B9%B4%E7%B4%9A%E8%8B%B1%E8%AA%9E%E7%A7%91%E8%A9%A6%E9%A1%8C.pdf",
        "title": "高雄市立小港國中105學年度第2學期第1次段考九年級英語科試題",
        "year": "105-2",
        "locator": "PDF第5頁閱讀測驗第48-50題；人物感受、代名詞指涉與證據推論",
        "pattern": "根據篇章線索辨識感受及推論可支持的結論，不挪用新聞人物、事件或選項。",
    },
    "keelung": {
        "url": "https://csjh.kl.edu.tw/books/file/528/111-1%E7%AC%AC%E4%B8%89%E6%AC%A1%E5%9C%8B%E4%B8%89%E6%AE%B5%E8%80%83%E8%A9%A6%E9%A1%8C.pdf",
        "title": "基隆市立中山高級中學111學年度第1學期第3次段考國中部九年級英文科試題",
        "year": "111-1",
        "locator": "PDF第7頁第33-35題；篇章主旨、下一步推論與代名詞指涉",
        "pattern": "以整篇訊息和前後文證據判斷主旨、可能後續及指涉，不挪用原文事件或選項。",
    },
}

# 每題均為新寫情境；只借用公校試題測量的能力，不重製其文本或答案。
DATA = [
    {
        "focus": "setting",
        "prompt": "In the story, a family reaches the ferry pier just before sunrise. Where and when does the first scene happen?",
        "options": ["At a library after lunch", "At a ferry pier before sunrise", "In a gym at midnight", "At a farm on a summer afternoon"],
        "answer": "B",
        "explanation": "The opening places the family at the ferry pier and fixes the time as just before sunrise; none of the other settings appears in the story.",
        "strategy": "先聽開場的地點與時間線索，分別記成「哪裡／何時」，再檢查選項是否把其中一欄偷換。",
        "steps": ["圈定題目只問故事開場的場景，不要把後來的事件當成起點。", "從開頭抓出 ferry pier，記為地點；抓出 just before sunrise，記為時間。", "對照四個選項，B同時吻合兩欄，其他選項至少有地點或時段不符。", "選B；不因故事後面可能提到別處，就替開場補上未出現的資訊。", "回想原始線索能否各自支持地點與時間，確認沒有只靠常識猜測。"],
        "refs": ["dawwan", "guochang", "keelung"],
    },
    {
        "focus": "characters",
        "prompt": "Mina asks her cousin Leo to help repair their neighbor's kite. Later, the neighbor joins them. Which people take part in the story's main events?",
        "options": ["Mina's teacher and a bus driver", "Leo's doctor and two hikers", "Mina, Leo, and their neighbor", "A shopkeeper and three visitors"],
        "answer": "C",
        "explanation": "Mina and Leo carry out the repair, and the neighbor owns the kite and joins them; the other people are never involved.",
        "strategy": "把每個重要動作旁的行動者列出來；主角群要由故事中的行動和關係支持，不用名詞出現次數猜。",
        "steps": ["先找出誰提出修理風箏，再追蹤誰實際協助。", "接著辨認風箏的主人及後續加入的人，確認三者都參與主要事件。", "比較選項的人物組合；C含有提出請求者、協助者和物主。", "排除提到教師、司機、醫師、登山者或店員的選項，因為故事沒有這些角色。", "選C並用「共同修理與物品歸屬」兩條證據回查角色名單。"],
        "refs": ["dawwan", "xiaogang", "keelung"],
    },
    {
        "focus": "event order",
        "prompt": "Nora noticed a wet footprint, followed it to the greenhouse, and then found the missing watering can beside the door. What did she do immediately before finding the can?",
        "options": ["She bought a new can", "She watered every plant", "She called the fire station", "She followed the footprint to the greenhouse"],
        "answer": "D",
        "explanation": "The sequence is notice the footprint → follow it to the greenhouse → find the can; following the clue is the event immediately before discovery.",
        "strategy": "把事件按連接詞或動作先後排成短時間線；問 immediately before 時，只取答案事件前一格。",
        "steps": ["確認 immediately before 要找的是發現水壺前一個動作。", "依故事排列三件事：看見濕腳印、沿著腳印走到溫室、在門邊找到水壺。", "在時間線上往發現水壺前退一格，得到跟著腳印到溫室。", "選D；另外三項不是前一刻發生的內容，也沒有故事證據。", "再順讀一次箭頭，確保沒有把線索出現順序和結果倒置。"],
        "refs": ["dawwan", "guochang", "keelung"],
    },
    {
        "focus": "problem",
        "prompt": "Evan brings a model boat to the school fair, but one wheel on its carrying cart breaks at the entrance. What problem interrupts his plan?",
        "options": ["The cart breaks while he is bringing the boat in", "The fair is canceled because of snow", "He forgets how to build a boat", "A judge takes the boat home"],
        "answer": "A",
        "explanation": "The broken cart is the obstacle described at the entrance; the story does not say the fair is canceled or that the boat is taken away.",
        "strategy": "辨認「原本要做什麼」與「哪件事卡住它」；不要把後果或想像中的災難當作問題本身。",
        "steps": ["先說出 Evan 的原計畫：把模型船帶進校園園遊會。", "找出 but 後面改變進展的訊息：推車的一個輪子在入口壞掉。", "將障礙縮寫為「搬運工具故障」，保持在故事明說的範圍。", "選A；B、C、D分別增加未提到的取消、忘記及拿走情節。", "確認A同時交代發生什麼與它如何中斷原計畫。"],
        "refs": ["dawwan", "guochang", "xiaogang"],
    },
    {
        "focus": "motive",
        "prompt": "After the picnic, Rafi walks back to the hill because he left his grandfather's walking stick there. Why does he return?",
        "options": ["To start another picnic with strangers", "To bring back his grandfather's walking stick", "To look for a bus ticket he never had", "To close the park before sunset"],
        "answer": "B",
        "explanation": "The because-clause states the reason directly: the walking stick was left on the hill, so Rafi returns to retrieve it.",
        "strategy": "聽到角色再次行動時，追問「他想完成什麼」；because 後的原因通常能直接連到目標。",
        "steps": ["把題目中的 return 定位成需要解釋原因的行動。", "擷取 because 後面的遺失物：祖父的手杖留在山丘上。", "把原因轉成角色目標：回去拿回手杖，而非另起新活動。", "選B，排除沒有線索支持的野餐、車票和關園任務。", "檢查答案是否回答 why；若只重述地點而未說目的，就不完整。"],
        "refs": ["dawwan", "guochang", "keelung"],
    },
    {
        "focus": "feeling",
        "prompt": "When the last lantern finally lights, Sora smiles and says, 'I was afraid we'd have to walk home in the dark.' What feeling best fits her reaction?",
        "options": ["Anger at the moon", "Boredom with the festival", "Relief", "Pride in winning a race"],
        "answer": "C",
        "explanation": "Sora feared the lights would fail, and the lantern now works; the worry has eased, which signals relief.",
        "strategy": "用「原先擔心什麼→現在發生什麼→感受如何改變」推情緒，並以台詞而非表情單獨判斷。",
        "steps": ["找出 Sora 先前擔心的結果：天黑後沒有燈可照路。", "確認轉折：最後一盞燈亮起，回家不必摸黑。", "把擔憂解除後的感受命名為 relief，而不是把原因誤認為憤怒。", "選C；月亮、節慶厭倦和比賽都沒有在情境中出現。", "用她說的擔心和燈亮的結果交叉驗證，確認感受有文本依據。"],
        "refs": ["dawwan", "xiaogang", "guochang"],
    },
    {
        "focus": "cause and effect",
        "prompt": "The creek rose after hours of heavy rain, so the hikers chose the higher trail. What caused them to change routes?",
        "options": ["The higher trail caused the rain", "They wanted to find a restaurant", "A guide lost the trail map", "Heavy rain made the creek rise"],
        "answer": "D",
        "explanation": "The rain came first and raised the creek; that unsafe condition led the hikers to choose another trail.",
        "strategy": "先辨認結果，再沿 so / because 追溯前因；要分清事件先後和因果方向。",
        "steps": ["標出要解釋的結果：登山者改走較高的路線。", "讀 so 前的事件，找到溪水因長時間大雨而上漲。", "建立因果箭頭：大雨→溪水上漲→改道；直接原因是溪水高漲，根源是大雨。", "選D，它指出引發改道的天候與水位變化；其餘選項沒有因果證據。", "回看句子的 so，確認答案位於結果之前且能解釋安全考量。"],
        "refs": ["dawwan", "guochang", "keelung"],
    },
    {
        "focus": "turning point",
        "prompt": "The class has searched the garden for its astronomy notebook all afternoon. Just as they prepare to stop, a quiet student remembers seeing it inside the telescope case. What changes the search?",
        "options": ["The student's memory gives them a new place to check", "The class decides to buy a telescope", "The garden closes for winter", "The notebook turns into a star map"],
        "answer": "A",
        "explanation": "The remembered clue redirects the class to a specific place, changing the search from stopping to checking the telescope case.",
        "strategy": "轉折點不是任何新事件，而是讓角色方向、選擇或局勢開始改變的那個訊息。",
        "steps": ["先概括轉折前的狀態：大家找了一下午，正準備停止。", "找到使局勢變化的新線索：學生想起筆記本可能在望遠鏡盒裡。", "檢查它造成的行動差異：全班有了下一個明確搜尋地點。", "選A；買望遠鏡、冬季關園和物品變形都不是故事線索。", "用「之前準備放棄／之後去檢查盒子」確認這條記憶確實推動情節。"],
        "refs": ["dawwan", "guochang", "keelung"],
    },
    {
        "focus": "ending",
        "prompt": "At the end, the two teams compare their maps, correct the wrong turn, and reach the lookout together. How does the story end?",
        "options": ["One team hides the map and leaves", "They solve the route problem and arrive together", "They forget why they started walking", "The lookout moves to another town"],
        "answer": "B",
        "explanation": "Comparing and correcting the maps fixes the navigation problem, and both teams reach the lookout together; the conflict is resolved cooperatively.",
        "strategy": "用最後一個問題是否被解決、角色最後到哪裡、關係有何變化來概括結局。",
        "steps": ["回到故事開頭的核心困難：隊伍走錯方向。", "追蹤結尾的處理：兩隊對照地圖並修正錯誤路線。", "記下最後結果：大家一起抵達觀景點，問題已解除。", "選B；其他選項與故事明確的合作及抵達結果相反或憑空新增。", "確認結局摘要包含「修正路線」和「共同到達」，而不是只重述途中片段。"],
        "refs": ["dawwan", "guochang", "keelung"],
    },
    {
        "focus": "integrated summary",
        "prompt": "A story follows a seed packet blown from a classroom window, three classmates searching different places, and a note that reveals it landed in the art room, where they find it. Which is the best brief note?",
        "options": ["Classmates paint a window while seeds grow outdoors", "The art room sends a note asking for a new classroom", "Seed packet blows away → classmates search → note points to art room → packet found", "A seed packet is lost, but no one looks for it"],
        "answer": "C",
        "explanation": "A keeps the central problem, search, decisive clue, and resolution in order while leaving out minor details.",
        "strategy": "摘要只保留「問題—關鍵線索／行動—結果」主幹，並按故事順序連接，不把枝節塞進筆記。",
        "steps": ["先確認故事主問題是種子包不見，而不是美術活動本身。", "抓出推進事件：同學分頭搜尋，便條提供新的地點線索。", "讀結尾確認結果及順序：線索指向美術教室，最後找到種子包。", "選C，因為它保留問題、搜尋、線索和解決；其他選項都有錯置或遺漏。", "逐箭頭核對原故事的先後，確保摘要簡潔且沒有添寫情節。"],
        "refs": ["dawwan", "xiaogang", "keelung"],
    },
]


def make(index, row):
    refs = []
    for key in row["refs"]:
        source = SOURCES[key]
        refs.append({
            "url": source["url"], "title": source["title"], "year": source["year"],
            "subject": "english", "locator": source["locator"],
            "observedPattern": source["pattern"], "reuseDecision": "pattern-only",
            "status": "recorded", "locatorLevel": "item",
        })
    options = [{"id": chr(65 + n), "text": text} for n, text in enumerate(row["options"])]
    rationale = f"正確答案：{row['answer']}。{row['explanation']}"
    return {
        "id": f"question-english-performance-5-iv-8-{index}",
        "subject": "english", "type": "single-choice", "prompt": row["prompt"],
        "options": options, "knowledgeIds": ["kg-english-performance-5-iv-8"],
        "difficulty": "medium", "answer": {"value": row["answer"], "explanation": rationale},
        "provenance": {
            "origin": "original", "license": "All rights reserved",
            "sourceUrl": refs[0]["url"], "sourceLocator": "; ".join(ref["locator"] for ref in refs),
            "authoringNote": "原創英文簡易故事筆記理解題；參考四所公立學校公開段考中具精確頁碼及題號的篇章理解能力型態，不複製原卷文本、選項、人物或答案。題組維持draft，待完整單元內容與內容／版權檢查。",
        },
        "reviewStatus": "draft", "updatedAt": "2026-09-26",
        "lessonId": "lesson-english-performance-5-iv-8", "examPatternRefs": refs,
        "solutionStrategy": row["strategy"], "solutionSteps": row["steps"],
    }


for index, row in enumerate(DATA, 1):
    path = OUT / f"question-english-performance-5-iv-8-{index}.json"
    path.write_text(json.dumps(make(index, row), ensure_ascii=False, indent=2) + "\n", encoding="utf-8")
print(f"rewrote {len(DATA)} original questions with item-located pattern-only refs")
