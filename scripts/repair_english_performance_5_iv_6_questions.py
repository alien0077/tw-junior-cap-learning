import json
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
OUT = ROOT / "questions" / "english"
LESSON = "lesson-english-performance-5-iv-6"
KG = "kg-english-performance-5-iv-6"
SOURCES = [
    {"url": "https://www.dwm.kh.edu.tw/upload/344/104_64184/105-2-2%E8%8B%B1%E6%96%87%E4%B8%89%E5%B9%B4%E7%B4%9A%E9%A1%8C%E7%9B%AE%E5%8D%B7.pdf", "title": "高雄市大灣國中105學年度第二學期第二次段考三年級英文題目卷", "year": "105-2"},
    {"url": "https://www.dwm.kh.edu.tw/upload/344/104_64186/111%E5%AD%B8%E5%B9%B4%E5%BA%A6%E7%AC%AC%E4%B8%80%E5%AD%B8%E6%9C%9F%E7%AC%AC%E4%BA%8C%E6%AC%A1%E6%AE%B5%E8%80%83%E8%8B%B1%E6%96%87%E4%B8%89%E5%B9%B4%E7%B4%9A%E8%A7%A3%E7%AD%94%28%E4%BD%B3%E9%9F%B3%29.pdf", "title": "高雄市大灣國中111學年度第一學期第二次段考九年級英文答案卷", "year": "111-1"},
    {"url": "https://www.kcjh.kh.edu.tw/upload/190/104_34764/%E5%9C%8B%E6%98%8C--%E4%BA%8C%E5%B9%B4%E7%B4%9A--%E8%8B%B1%E8%AA%9E%E7%A7%91_4.pdf", "title": "高雄市立國昌國民中學112學年度第二學期第二次段考二年級英語科試題卷", "year": "112-2"},
    {"url": "https://www.dam.kh.edu.tw/upload/68/101_28414/107-1-1%E4%BA%8C%E5%B9%B4%E7%B4%9A%E7%AC%AC1%E6%AC%A1%E8%A9%95%E9%87%8F%E8%A9%A6%E9%A1%8C%E6%9A%A8%E8%A7%A3%E7%AD%94.pdf", "title": "高雄市立大社國中107學年度第一學期第一次段考二年級英語試題暨解答", "year": "107-1"},
]

def refs(i):
    if i in {5, 10}:
        locators = [
            (0, "第2頁第25題", "以 whether／if 引導間接問句，辨認時態與子句結構錯誤。"),
            (0, "第2頁第21題", "以 where 引導的名詞子句檢查間接問句採陳述語序，而非疑問倒裝。"),
            (1, "第4頁第六大題第2、3題", "答案卷要求把 yes-no 與 wh-直接問句改成間接問句，列有 if／whether 與 wh 子句。"),
        ]
    elif i in {4, 7, 8}:
        locators = [
            (2, "第3頁第20題", "對話脈絡以 asked him + to V 表達請求；本題只取轉述請求的動詞補語形式。"),
            (2, "第3頁第22題", "對話直接引語轉述含 told me not to + 原形動詞；本題只取否定祈使轉述形式。"),
            (0, "第2頁第29題", "克漏字以 They said ... would not miss 檢查 said 後轉述子句的時態呼應。"),
        ]
    elif i == 9:
        locators = [
            (0, "第2頁第29題", "克漏字以 They said ... would not miss 呈現過去報導動詞後的時態呼應。"),
            (3, "第1頁第10題", "對話明確以 Is this your notebook?／it is not mine／Tom's 判讀物主代名詞與所有權；本題只取依指涉對象更換物主形式的能力。"),
            (2, "第3頁第20題", "對話題以 asked him to help 表達他人轉述的請求；本題僅取報導動詞搭配子句的句型方向。"),
        ]
    else:
        locators = [
            (0, "第2頁第29題", "克漏字以 They said ... would not miss 檢查過去報導動詞後的時態呼應。"),
            (1, "第4頁第六大題第2、3題", "答案卷逐題把直接問句改成含 if／whether 或 wh 子句的間接問句；本題只取視角轉換後重述訊息的能力方向。"),
            (2, "第3頁第20題", "對話脈絡使用 asked him to help 轉述請求；本題只取報導動詞帶出他人訊息的句型方向。"),
        ]
    return [{**SOURCES[source_index], "subject": "english", "locator": locator,
        "observedPattern": pattern + " 本題僅借鑑題型／能力方向；題幹、對話、選項及答案均自行創作，未摘錄或改寫原卷句子。",
             "reuseDecision": "pattern-only", "status": "recorded", "locatorLevel": "item"}
            for source_index, locator, pattern in locators]

def make(i, prompt, options, answer, explanation, strategy, steps, difficulty):
    return {"id": f"question-english-performance-5-iv-6-{i}", "subject": "english", "type": "single-choice", "prompt": prompt, "options": [{"id": k, "text": v} for k, v in options.items()], "knowledgeIds": [KG], "difficulty": difficulty, "answer": {"value": answer, "explanation": explanation}, "provenance": {"origin": "original", "license": "All rights reserved", "sourceUrl": SOURCES[0]["url"], "sourceLocator": "已核對大灣國中英文公開段考第2頁第21、25、29題及答案卷第4頁改寫題，國昌國中公開試題第3頁第20、22題；僅參考題型能力方向，未複製原卷內容。", "authoringNote": "本題情境、對話、選項、答案與解說皆為原創；公校來源僅作 pattern-only 題型研究，內容維持 draft，尚未通過全庫發布 gate。"}, "reviewStatus": "draft", "updatedAt": "2026-09-26", "lessonId": LESSON, "examPatternRefs": refs(i), "solutionStrategy": strategy, "solutionSteps": steps}

Q = [
make(1, "Mia said, 'I am tired.' Which sentence correctly reports her words?", {"A": "Mia said that she was tired.", "B": "Mia said that I am tired.", "C": "Mia says that she tired.", "D": "Mia said that he was tired."}, "A", "When Mia's past words are reported, I changes to she and am changes to was.", "先找說話者與原句主詞，再同步處理人稱與過去轉述時態。", ["圈出說話者 Mia，確定 I 在轉述時要指 Mia。", "將 I 改成 she。", "因為 said 是過去式，am 轉為 was。", "比較四個選項，只有 A 同時完成兩項變化。", "選 A，回讀 Mia said that she was tired，確認主詞與時態一致。"], "easy"),
make(2, "Ben said, 'I will call you tomorrow.' What did Ben say?", {"A": "Ben said that he would call me the next day.", "B": "Ben said that I will call you tomorrow.", "C": "Ben says he called me yesterday.", "D": "Ben said that he calls you today."}, "A", "In reported speech, I becomes he, will becomes would, you becomes me for the reporter, and tomorrow becomes the next day.", "先標記每個需要依轉述視角改變的代詞與時間詞，再檢查助動詞。", ["辨認 Ben 是原句 I 的指涉對象，改成 he。", "將 will call 改為 would call。", "依轉述者視角將 you 改為 me。", "將 tomorrow 改成 the next day，保持時間關係。", "選 A，逐項核對人稱、時態與時間詞。"], "hard"),
make(3, "Lena said yesterday, 'I finished my project yesterday.' Which sentence reports her words today?", {"A": "Lena said that she had finished her project two days before.", "B": "Lena said that I finish my project tomorrow.", "C": "Lena says that she finishes her project yesterday.", "D": "Lena said that he had finished my project today."}, "A", "Because Lena spoke yesterday about finishing the project the day before that, today's report places the completed action two days earlier; I/my also become she/her.", "先畫出說話日與完成日，再同步換算人稱、所有格及回述時間。", ["把 Lena 說話日標成昨天，避免直接沿用報導日的 yesterday。", "確認原句 I 與 my 指 Lena，因此換成 she 與 her。", "finished 早於說話日，置於 said 後可用 had finished。", "從今天往回算，完成日是 two days before，不是 yesterday。", "以 today 為基準回讀，檢查人稱、時態及兩天的時間距離。"], "hard"),
make(4, "Tom said, 'Please close the door.' Which sentence reports the request?", {"A": "Tom asked me to close the door.", "B": "Tom asked me closing the door.", "C": "Tom said me close the door.", "D": "Tom asked that I closed the door yesterday."}, "A", "A polite imperative is commonly reported with asked someone to plus the base verb.", "先辨認 Please 是請求，再使用 ask＋人＋to V 的轉述結構。", ["圈出 Please close，判斷原句是禮貌請求。", "找出轉述者要表達的受話者 me。", "套用 asked me to 加原形 close。", "補上原句受詞 the door，檢查資訊完整。", "選 A，確認不是動名詞或錯誤的 said me 結構。"], "medium"),
make(5, "Sara asked, 'Are you ready?' Which sentence reports her question to me?", {"A": "Sara asked me if I was ready.", "B": "Sara asked me if you are ready.", "C": "Sara said me I was ready.", "D": "Sara asked that I ready."}, "A", "A yes-no question is reported with asked me if and the reporter's I, with are changing to was after asked.", "先辨認 yes/no 問句，再檢查 if、受詞、人稱與時態。", ["確認 Are you ready? 沒有疑問詞，是 yes/no 問句。", "使用 asked me if 引入轉述。", "原句 you 指轉述者，改成 I。", "將 are 改為 was 配合過去式 asked。", "選 A，回讀整句確認問句資訊保留。"], "medium"),
make(6, "Kai said, 'We are meeting at the station tonight.' Which report is correct?", {"A": "Kai said that they were meeting at the station that night.", "B": "Kai said that we are meeting at the station tomorrow.", "C": "Kai says they met at the station tonight.", "D": "Kai said that they was meeting in station today."}, "A", "We becomes they from the reporter's viewpoint, are meeting becomes were meeting, and tonight becomes that night.", "依說話者群體與報導時間重新定位代詞、進行式與時間詞。", ["判斷原句 We 指 Kai 與同伴，轉述時用 they。", "將 are meeting 改為 were meeting。", "保留地點 the station。", "將 tonight 改成 that night。", "選 A，確認複數 be 動詞與全部時間資訊正確。"], "hard"),
make(7, "The teacher said, 'Do not run in the hall.' What did the teacher tell students?", {"A": "The teacher told students not to run in the hall.", "B": "The teacher told students do not ran in the hall.", "C": "The teacher said students not running hall.", "D": "The teacher asked students ran in the hall."}, "A", "A negative command is reported with told someone not to plus the base verb.", "看出 Do not 是禁止命令，再轉成 tell＋人＋not to V。", ["圈出 Do not run，確認語意是禁止而非詢問。", "找出受話者 students。", "套用 told students not to。", "保留原地點 in the hall，並使用原形 run。", "選 A，確認否定位置與動詞形式正確。"], "medium"),
make(8, "Nora said, 'I can help with the boxes.' Which sentence reports her offer?", {"A": "Nora said that she could help with the boxes.", "B": "Nora said that I can helped with the boxes.", "C": "Nora asked that she can help boxes.", "D": "Nora told she could helping the boxes."}, "A", "In reported speech, I becomes she, can becomes could, and help remains the base form after could.", "把能力或主動提供協助的句型視為陳述，再檢查情態動詞後的原形。", ["將原句 I 對應到 Nora，改為 she。", "將 can 轉為 could。", "保留 could 後的原形 help。", "保留 with the boxes 這個完整搭配。", "選 A，逐項排除 helped、helping 與錯誤受詞結構。"], "medium"),
make(9, "David said, 'This book is mine.' Which report is correct when David points to the book?", {"A": "David said that the book was his.", "B": "David said that this book is mine.", "C": "David said that the book were him.", "D": "David asked that the book was my."}, "A", "The demonstrative this becomes the book in the report, is becomes was, and mine becomes his because David is the owner.", "將指示詞、be 動詞與所有代名詞分別換成第三人稱轉述形式。", ["確認 David 指著眼前的書，this 可明確改寫為 the book。", "把 is 改為 was。", "將 mine 對應 David 的所有權，改為 his。", "排除 B、C、D，逐一檢查視角、be 動詞與所有代名詞。", "選 A，回讀確認所有資訊仍指同一本書。"], "hard"),
make(10, "Amy said, 'Where did you put my keys?' Which sentence reports her question to me?", {"A": "Amy asked me where I had put her keys.", "B": "Amy asked me where did I put my keys.", "C": "Amy said where I put her keys?", "D": "Amy asked where had you put my keys."}, "A", "A wh-question keeps where but changes to statement word order; you becomes I, my becomes her, and did put becomes had put.", "保留疑問詞但改成陳述語序，再依轉述視角調整代詞與時態。", ["保留 where，因為它是原問句的疑問詞。", "將 did you put 改成 I had put，不倒裝。", "將原說話者 Amy 的 my 改成 her。", "加入 asked me，標示問題是問轉述者。", "選 A，確認 wh 詞、語序、人稱與時態全部一致。"], "hard"),
]

answer_positions = ["B", "C", "D", "A", "B", "D", "C", "A", "D", "B"]
step_four = {
    1: "核對選項是否同時把 Mia 的 I 改為 she，並把 am 回推為 was。",
    2: "逐一核對 he、would call、me 與 the next day 四項視角變化。",
    3: "以今天為基準往回算兩天，確認不是把引述中的 yesterday 錯當成報導日的前一天。",
    4: "排除把受詞直接接動名詞，或把 said 誤當成可直接接 me 的選項。",
    5: "檢查 if 後採主詞在動詞前的陳述語序，並保留詢問對象 me。",
    6: "檢查 they 對應複數 were，並讓 that night 與回述時間一致。",
    7: "比對禁止語意是否放在 not to 後，再確認 run 保持原形。",
    8: "確認 could 後接原形 help，且提供協助的對象仍是 the boxes。",
    9: "排除把 David 的物主身分改成 mine，或把 book 配上錯誤代名詞的句子。",
    10: "核對 where 子句使用主詞在動詞前的語序，並把 Amy 的 my 換成 her。",
}
step_five = {
    1: "回讀 Mia 的引述，確認說話者、代名詞與過去狀態一致。",
    2: "用 Ben 對我說話的情境回代代名詞，確認明天仍指通話的次日。",
    3: "從今天回算 Lena 說話日與完工日，確認答案是 two days before。",
    4: "把 Tom 的禮貌請求完整轉成受詞加 to close，不改變關門這件事。",
    5: "回讀 Sara 問我的 yes-no 問題，確認 if 子句保留 ready 狀態。",
    6: "從 Kai 與同伴的角度重述，確認聚會時間和集合地點沒有變動。",
    7: "確認老師傳達的是『不要在走廊奔跑』，而非肯定命令或過去動作。",
    8: "回讀 Nora 的意願，確定情態語氣及 with the boxes 的搭配都保留。",
    9: "以 David 為物主回讀整句，確認指涉的是同一本書及他的所有權。",
    10: "從 Amy 問我的視角重讀，確認鑰匙屬於 Amy、放置動作者是我。",
}
explanations_zh = {
    1: "Mia 轉述自己的原話時，第一人稱 I 要改成 she；主句 said 是過去式，因此 am 通常回推為 was。只有同時保留說話者身分與時間關係的選項正確。",
    2: "Ben 原話中的 I 指 Ben，所以改成 he；will call 隨過去式 said 回推為 would call。Ben 對我說的 you 從我的轉述視角是 me；tomorrow 依報導時間移成 the next day。",
    3: "Lena 在昨天說 finished yesterday，完成日是昨天的前一天，也就是今天往前兩天。轉述時 I/my 改成 she/her，said 後以 had finished 表示先於說話日完成，時間詞應為 two days before。",
    4: "Please close the door 是直接提出的禮貌請求。轉述請求使用 ask + 受詞 + to + 原形動詞，因此為 asked me to close；不能寫 asked me closing，也不能說 said me。",
    5: "Are you ready? 是沒有疑問詞的 yes-no 問句，間接轉述以 if 引入，子句採 I was 的陳述語序；問句中的 you 指受話者我，所以改成 I。",
    6: "We 指 Kai 與同行者，從外部轉述時改為 they；are meeting 配合過去報導動詞改成 were meeting，tonight 也依報導時間移為 that night。",
    7: "Do not run 是禁止命令，轉述用 tell + 受詞 + not to + 原形動詞：told students not to run。否定詞放在 to 前，地點 in the hall 保留。",
    8: "原句 I 指 Nora，改成 she；過去轉述常將 can 回推為 could，而情態動詞後仍接原形 help，不能接 helped 或 helping。",
    9: "David 指著的 this book 可在轉述中明確說成 the book；is 隨 said 回推成 was。mine 表示 David 所有，第三人稱物主代名詞應為 his。",
    10: "Where 疑問詞保留，但間接問句要用主詞在動詞前的陳述語序：where I had put。Amy 原話的 you 指我，改為 I；my keys 屬於 Amy，改為 her keys。",
}
for question, target_key in zip(Q, answer_positions):
    number = int(question["id"].rsplit("-", 1)[1])
    question["answer"]["explanation"] = explanations_zh[number]
    original = {option["id"]: option["text"] for option in question["options"]}
    correct_text = original[question["answer"]["value"]]
    distractors = [text for key, text in original.items() if key != question["answer"]["value"]]
    ordered = [None, None, None, None]
    ordered[ord(target_key) - ord("A")] = correct_text
    slots = iter(distractors)
    for index in range(4):
        if ordered[index] is None:
            ordered[index] = next(slots)
    question["options"] = [{"id": chr(65 + index), "text": value} for index, value in enumerate(ordered)]
    question["answer"]["value"] = target_key
    if number == 2:
        question["prompt"] = "Ben told me, 'I will call you tomorrow.' Which sentence reports his words from my point of view?"
    if number == 1:
        question["solutionSteps"][1] = "將第一人稱 I 換成第三人稱 she，讓代名詞指回 Mia。"
    if number == 6:
        question["solutionSteps"][2] = "保留 at the station，避免轉述時遺漏 Kai 說明的集合地點。"
    if number == 8:
        question["solutionSteps"][1] = "把表示能力或意願的 can 依 said 的過去報導轉成 could。"
    if number == 9:
        question["solutionSteps"][1] = "把現在式 is 依過去報導視角回推為 was。"
    if number == 10:
        question["solutionSteps"][0] = "保留 where 這個疑問詞，因為它詢問的是鑰匙被放置的位置。"
    question["solutionSteps"][3] = step_four[number]
    question["solutionSteps"][4] = step_five[number]
    (OUT / f"{question['id']}.json").write_text(json.dumps(question, ensure_ascii=False, indent=2) + "\n", encoding="utf-8")
print(f"rewrote {len(Q)} questions")
