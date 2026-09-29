import json
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
OUT = ROOT / "questions/english"

SOURCES = {
    "guochang": {
        "url": "https://www.kcjh.kh.edu.tw/upload/190/104_34764/2-%E8%8B%B1%E6%96%87_4.pdf",
        "title": "高雄市立國昌國民中學114學年度第1學期第2次八年級英文段考",
        "year": "114-1",
    },
    "fengjia": {
        "url": "https://www.fjm.kh.edu.tw/upload/226/101_44845/113%E5%B9%B4%E5%9C%8B%E4%B8%AD%E7%B5%84%E9%96%B1%E8%AE%80%E7%B4%A0%E9%A4%8A%E8%A9%A6%E9%A1%8C%28%E7%AD%94%E6%A1%88%E5%85%AC%E5%91%8A%29.pdf",
        "title": "高雄市113學年度允文允武國中組閱讀素養試題與答案（鳳甲國中校方公開）",
        "year": "113",
    },
    "yanchao": {
        "url": "https://www.ycm.kh.edu.tw/upload/297/104_62703/111-1%282%29%E4%B8%83%E5%B9%B4%E7%B4%9A%E8%8B%B1%E6%96%87%E8%A9%A6%E9%A1%8C.pdf",
        "title": "高雄市立燕巢國民中學111學年度第1學期七年級第2次段考英文科試題卷",
        "year": "111-1",
    },
}

ITEMS = [
    ("C", "guochang", "人物動機", "Rehearsal scene: Each time the bell rings, Mara checks beneath the painted bridge. She tells the stagehand, 'The silver key must be there before the gate opens.' What is Mara trying to do?", ["Hide the bell from the audience.", "Replace the bridge with a gate.", "Find the key needed for the next scene.", "Stop the stagehand from entering."], "她反覆在橋下尋找，並明說銀鑰匙要在門打開前找到；行動與台詞都指向為下一幕找道具。", ["先找出重複動作：每次鈴響，她都查看橋下。", "讀她說的關鍵句，確認銀鑰匙和gate opening的時間關係。", "將行動目的連到下一場景需要的道具。", "排除藏鈴、換布景或阻止工作人員等沒有線索支持的解讀。", "選C；推論動機要讓角色反覆行動和台詞中的目標互相印證。"], "PDF第3頁第26題：由人物前後行動推論未直接明說的動機；本題改寫為舞台道具任務。", "用行動證據推理角色追求的目標，而不是只抓住一個相同名詞。"),
    ("B", "guochang", "由行動判斷性格", "Backstage, Theo notices that the new actor has no script copy. Without being asked, he shares his marked pages and quietly points to the actor's first entrance. Which quality does Theo show?", ["Carelessness about the performance.", "Consideration for a teammate.", "Anger about changing the cast.", "A wish to take the lead role."], "Theo主動分享台本並協助新演員找到上場處，行動顯示體貼；題目沒有他生氣或想搶角色的證據。", ["把注意焦點放在Theo做了什麼，而非替他貼個性標籤。", "找兩項行動證據：分享有標記的台本、指出上場位置。", "判斷這些行動如何幫助剛加入的隊友。", "排除粗心、生氣和爭取主角等沒有文本依據的選項。", "選B；人物特質由有目的的行為支持，不能單靠猜測。"], "PDF第3頁第27題：根據故事行動辨識人物性格；本題另創排演合作情境。", "以具體行動作為性格判斷依據，不把未出現的想法當成事實。"),
    ("A", "yanchao", "表演者的情緒與目標", "In an original rehearsal scene, the lanterns go dark one by one. Sumi grips the script, takes one slow breath, and says, 'I can still guide everyone to the exit.' What does her line show?", ["She is worried but determined to help.", "She is pleased that the show has ended.", "She wants the audience to leave without the actors.", "She has forgotten where the exit is."], "燈逐漸熄滅和緊握台本顯示緊張，但她深呼吸後承諾帶大家出去，表現出擔心中仍決心協助。", ["先用舞台情境判斷壓力來源：燈光正在熄滅。", "把握緊台本和慢慢深呼吸視為情緒線索。", "再讀她說的guide everyone to the exit，確認她準備採取的行動。", "排除慶祝、趕走演員或不知道出口等與台詞相反的答案。", "選A；表演情緒常有兩層，需同時解讀害怕線索與角色選擇。"], "PDF第1頁非選擇第27題：依場景描述時間、地點、行動與心情；本題另創劇場停電片段。", "將情境、人物動作和自述合併判斷角色當下的感受與意圖。"),
    ("D", "guochang", "合作解決衝突", "During a costume scene, Ivy needs the only green scarf for the river spirit, while Max wants it as a market seller's banner. The director suggests Ivy wear a green sash and Max use a matching cloth strip on the stall. Why is this solution effective?", ["It removes both characters from the play.", "It changes the story into a market lesson.", "It gives the scarf to Max and cancels Ivy's role.", "It preserves both scene ideas with different costume pieces."], "導演沒有取消任一角色，而是用綠腰帶保留河之精靈的視覺線索，再用相配布條呈現攤位；兩個表演需求都被照顧。", ["先列出衝突兩方各自需要什麼：Ivy要角色服飾，Max要攤位布置。", "檢查導演提出的兩件替代物是否分別回應需求。", "確認方案沒有移除角色或改掉故事主題。", "排除只滿足其中一人的選項。", "選D；排演協調的好方案會保留雙方戲劇功能，同時調整實際道具。"], "PDF第3頁第28題：連結善意行動及故事後續結果；本題改為排演衝突的雙方協調。", "評估角色選擇造成的影響，特別檢查它是否兼顧情境中的多項需求。"),
    ("C", "fengjia", "道具作為情節線索", "In a short play, the detective finds a torn blue ticket under a chair. Later, a matching half appears in the caretaker's coat pocket. Which object most directly helps the detective connect the two scenes?", ["The chair.", "The caretaker's coat by itself.", "The two matching ticket halves.", "The detective's notebook."], "兩半藍色票根能直接互相拼合，形成跨場景的連結線索；椅子、外套或筆記本沒有同樣的匹配證據。", ["確認問題問的是連接兩幕的線索，不是場景中任意道具。", "比較先後出現的物件，找出後來重現且能配對的部分。", "判斷票根的兩半如何把椅下發現與管理員口袋連起來。", "排除只提供位置或記錄功能、卻不能證明關聯的物品。", "選C；道具推理要追蹤它如何帶來新資訊，而非只看它是否醒目。"], "PDF第6頁第42題：辨識故事中支持關鍵推論的線索物件；本題另創票根與舞台情節。", "從角色後續能驗證的物件線索推理，避免把醒目道具直接等同答案。"),
    ("B", "guochang", "依線索整理事件時間", "Stage notes: 7:10—the caretaker locks the west door; 7:20—Rae hears a bell in the hall; 7:25—the cast finds the prop box open. What is the earliest event?", ["The cast finds the box open.", "The caretaker locks the west door.", "Rae hears a bell.", "The cast starts the final scene."], "時間表中7:10早於7:20和7:25；題目問最早事件，因此是管理員鎖上西門。", ["把三個時間先按由早到晚排序。", "辨認7:10、7:20、7:25的先後，不被事件嚴重程度影響。", "將最早時間7:10配回相應動作。", "排除後兩個較晚發生的事件和沒有列出的final scene。", "選B；劇本時間線先看時間標記，再配對事件，不要按閱讀順序猜。"], "PDF第4頁第29至30題：根據人物紀錄與時間推斷事件先後；本題改為排演場記。", "透過時間標記核對事件順序；改寫資料和事件完全不同。"),
    ("A", "fengjia", "從結局推論故事主題", "At the end of the play, Noor returns the borrowed sound recorder, and the other actors invite her to help plan the next show. Which idea is best supported by this ending?", ["Trust can grow when people take responsibility.", "A successful show needs expensive equipment.", "Actors should avoid working with new people.", "Borrowed objects are safer if no one uses them."], "Noor歸還器材負起責任，團員接著邀她共同規劃新演出；結局支持信任與合作關係增進，而非器材價格或拒絕新夥伴。", ["先比較結局前後人物關係的變化。", "找出Noor做了什麼：歸還借用的錄音器。", "注意團員後續邀她參與新計畫，作為信任提升的結果。", "排除文中未談到的設備價格及拒絕合作主張。", "選A；主題要由重要行動和結局共同支持，不是抽出某個道具。"], "PDF第6頁第41題：由故事整體推論主旨；本題以責任行動及團隊邀請另創結局。", "由故事行動和結局歸納主題，避免把單一情節細節擴大成全篇主張。"),
    ("D", "yanchao", "舞台停頓的效果", "In an original performance, after asking 'Which path did the map show?', the actor pauses, turns the map toward the audience, and points to a faded arrow. What is the pause mainly for?", ["To show that the actor has forgotten every line.", "To let the scene end before the clue appears.", "To ask the audience to answer aloud.", "To give the audience time to notice the map clue."], "停頓後演員把地圖轉向觀眾並指出褪色箭頭，這個節奏讓觀眾能看見並理解線索；沒有忘詞或結束場景的證據。", ["把pause前後的動作連起來看，不要孤立解讀停頓。", "找停頓之後新增的舞台訊息：地圖轉向觀眾、箭頭被指出。", "推斷停頓如何改變觀眾看線索的時間。", "排除忘詞、直接邀觀眾發言及提前結束等無根據說法。", "選D；舞台節奏可以安排觀眾何時看見關鍵資訊。"], "PDF第1頁非選擇第27題：以場景線索組織英語口頭敘述；本題聚焦觀眾讀取舞台線索的時機。", "結合舞台提示和觀眾視角推斷停頓的溝通目的。"),
    ("C", "fengjia", "辨認角色採取的方法", "The stage directions show Ken comparing two halves of a paper badge, then asking the ticket keeper where the matching half came from. What method does Ken use to identify the missing performer?", ["He guesses from the loudest voice.", "He asks every actor to change costumes.", "He matches the badge evidence and checks its source.", "He cancels the performance and searches the street."], "Ken先比對徽章兩半，再追問來源，方法是用物件證據配對並查證來源；其餘選項都未出現在舞台提示。", ["把行動依序拆成比對徽章和詢問保管者兩步。", "找出兩步共同目的：驗證徽章線索與來源。", "判斷這種查證如何協助縮小失蹤演員的身分範圍。", "排除猜聲音、換服裝或取消演出等未記錄行動。", "選C；回答方法題應重述文本明確呈現的步驟，不自行增加調查方式。"], "PDF第6頁第43題：從角色使用的線索辨識其尋找方法；本題更換角色、物件與事件。", "按劇本實際行動還原角色的方法，避免只依結果猜測過程。"),
    ("B", "guochang", "整合短劇的事件與結局", "A wind sound begins. Leena notices a loose paper lantern near the stage edge. She warns the cast, and they secure it before continuing the outdoor scene. What is the main development?", ["The actors abandon the play because they dislike the script.", "The cast responds to a stage hazard and safely continues.", "Leena hides the lantern so the audience cannot see it.", "The wind helps the cast finish without any change."], "風聲和鬆動的燈籠帶出安全問題；Leena提醒後劇組先固定道具，再繼續演出，主軸是處理危險並安全完成表演。", ["先辨認事件轉折：風聲出現，燈籠的位置不穩。", "追蹤角色回應：Leena警告，演員固定道具。", "把處理方式和結局連起來，確認演出得以安全繼續。", "排除不喜歡劇本、藏起道具或完全不改變等內容外推。", "選B；抓短劇大意時依問題、角色反應、結果三段串起事件。"], "PDF第3頁第28題：連結角色善意選擇及故事結果；本題另創舞台風險與共同應對。", "以轉折事件、人物行動及最後結果共同概括短劇，不只摘錄某一句台詞。"),
]


def make(index, item):
    answer, source_key, skill, prompt, options, explanation, steps, locator, pattern = item
    source = SOURCES[source_key]
    ref = {
        "url": source["url"],
        "title": source["title"] + "；僅參照故事理解與人物／線索／結局推論，不複製原題。",
        "year": source["year"],
        "subject": "english",
        "locator": locator,
        "observedPattern": pattern,
        "reuseDecision": "pattern-only",
        "status": "recorded",
        "locatorLevel": "item",
    }
    return {
        "id": f"question-english-performance-2-iv-11-{index}",
        "subject": "english",
        "type": "single-choice",
        "prompt": prompt,
        "options": [{"id": chr(65 + i), "text": value} for i, value in enumerate(options)],
        "knowledgeIds": ["kg-english-performance-2-iv-11"],
        "difficulty": "medium",
        "answer": {"value": answer, "explanation": explanation + f" 正確答案：{answer}。"},
        "provenance": {
            "origin": "original",
            "license": "All rights reserved",
            "sourceUrl": source["url"],
            "sourceLocator": locator + "；人物、台詞、舞台指示、選項與答案均重新創作。",
            "authoringNote": "原創簡易短劇理解題；只參照公立學校公開試題中人物動機、行動證據、事件順序、故事線索及結局判讀的能力型態，不複製來源內容。",
        },
        "reviewStatus": "draft",
        "updatedAt": "2026-09-24",
        "lessonId": "lesson-english-performance-2-iv-11",
        "examPatternRefs": [ref],
        "solutionStrategy": f"{skill}：把台詞、舞台指示和事件結果連讀，先找可見證據，再判斷它支持的表演意圖或故事意義。",
        "solutionSteps": steps,
    }


for index, item in enumerate(ITEMS, 1):
    path = OUT / f"question-english-performance-2-iv-11-{index}.json"
    path.write_text(json.dumps(make(index, item), ensure_ascii=False, indent=2) + "\n", encoding="utf-8")
print(f"rewrote {len(ITEMS)} original short-drama questions")
