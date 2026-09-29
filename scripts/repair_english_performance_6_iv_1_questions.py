import json
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
OUT = ROOT / "questions" / "english"
LESSON = "lesson-english-performance-6-iv-1"
KG = "kg-english-performance-6-iv-1"
SOURCES = [
    {"url": "https://www.yacjh.kh.edu.tw/upload/221/101_30637/114%E4%B8%8B%E5%AD%B8%E6%9C%9F%E7%AC%AC%E4%B8%80%E6%AC%A1%E6%AE%B5%E8%80%83%E4%B8%89%E5%B9%B4%E7%B4%9A%E8%8B%B1%E6%96%87.pdf", "title": "高雄市立鹽埕國民中學公開英文評量", "year": "113-114"},
    {"url": "https://jweb.kl.edu.tw/userfiles/1389/document/40425_%E5%85%AB%E5%B9%B4%E7%B4%9A1%E6%AE%B5%E8%8B%B1%E6%96%87.pdf", "title": "基隆市立武崙國中111學年度第2學期八年級第1次段考英文科", "year": "111-2"},
    {"url": "https://www.kcjh.kh.edu.tw/upload/190/104_34764/%E4%B8%80%E5%B9%B4%E7%B4%9A-%E8%8B%B1%E8%AA%9E.pdf", "title": "高雄市立國昌國民中學110學年度第1學期七年級英文科第1次段考", "year": "110-1"},
]

def refs():
    patterns = [
        ("PDF第1頁聽力第6至15題：基本問答及言談理解", "辨認提問並選擇合宜回應或理解對話；只借鑑英語互動評量形式。"),
        ("PDF第2頁聽力第6至8題基本問答；後續言談理解題", "依聽到的生活情境選擇回應並核對語意連貫；本站另寫課堂澄清、合作與參與情境。"),
        ("PDF第2頁第21至25題對話回應；第3頁第32至33題校園對話理解", "評量對話銜接與從交流內容找訊息；只借鑑回應／理解形式，不沿用原文、角色或答案。"),
    ]
    return [{**s, "subject": "english", "locator": patterns[i][0], "observedPattern": patterns[i][1], "reuseDecision": "pattern-only", "status": "recorded", "locatorLevel": "page" if i != 1 else "paper"} for i, s in enumerate(SOURCES)]

def make(i, prompt, options, answer, explanation, strategy, steps, difficulty):
    return {"id": f"question-english-performance-6-iv-1-{i}", "subject": "english", "type": "single-choice", "prompt": prompt, "options": [{"id": k, "text": v} for k, v in options.items()], "knowledgeIds": [KG], "difficulty": difficulty, "answer": {"value": answer, "explanation": explanation}, "provenance": {"origin": "original", "license": "All rights reserved", "sourceUrl": SOURCES[0]["url"], "sourceLocator": "三份公立學校公開英文評量的聽辨、對話回應及對話理解題型；本站僅參考能力形式，未複製原題或選項。", "authoringNote": "依官方課綱與本單元課堂參與能力，參考三份公立學校公開英文評量的互動題型，獨立撰寫情境、選項、答案與解法；未複製來源內容，維持 draft 待後續內容／版權 QA。"}, "reviewStatus": "draft", "updatedAt": "2026-09-26", "lessonId": LESSON, "examPatternRefs": refs(), "solutionStrategy": strategy, "solutionSteps": steps}

Q = [
make(1, "The teacher asks students to practice the new dialogue in pairs. Which action shows active participation?", {"A": "Take a role, speak the lines, and listen for the partner's turn.", "B": "Wait silently and let the partner do both roles.", "C": "Copy the title without reading the dialogue.", "D": "Leave the room before practice begins."}, "A", "Taking a role, speaking, and listening are observable actions that directly complete the pair practice task.", "把『積極』轉成可觀察的任務行動，再檢查是否完成說與聽兩個角色。", ["找出任務核心 practice the dialogue in pairs。", "列出完成任務需要的角色、朗讀與聆聽行動。", "檢查 A 是否同時包含 speak 與 listen。", "排除 B、C、D，因為它們沒有實際完成兩人練習。", "選 A，回到課堂任務確認行動與要求完全對應。"], "easy"),
make(2, "You do not understand the teacher's English instruction. What is the best classroom response?", {"A": "Could you say that again more slowly, please?", "B": "I will guess and never check.", "C": "I will talk to a friend about an unrelated game.", "D": "I will put my head down."}, "A", "A politely asks for repetition and slower speech, allowing the student to re-enter the learning task.", "先找能澄清指示的英語句型，再判斷是否禮貌且直接解決理解問題。", ["確認問題是不理解 instruction，而不是缺少文具。", "尋找包含 repeat 與 slower 的澄清請求。", "檢查 Could you...please 的禮貌形式。", "排除 B、C、D，因為它們放棄或轉移學習任務。", "選 A，確認回應能取得必要資訊並繼續參與。"], "easy"),
make(3, "During group work, one classmate has not spoken. Which sentence best invites that person to participate?", {"A": "What do you think, Maya?", "B": "You cannot join us.", "C": "I will answer every question alone.", "D": "Please stop listening."}, "A", "Asking Maya for her opinion gives her a clear, respectful opportunity to contribute.", "觀察小組互動的缺口，再選能分配發言機會而非排除同伴的句子。", ["找出問題中的關鍵：一位同學尚未發言。", "判斷需要的是邀請意見的問句。", "檢查 What do you think, Maya? 直接指定且尊重同學。", "排除 B、C、D，因為它們排斥、壟斷或禁止參與。", "選 A，確認句子能把討論發言權交回同伴。"], "easy"),
make(4, "The class is checking answers together. Which behavior gives useful evidence of participation?", {"A": "Explain why you chose an answer and compare it with a partner.", "B": "Say only 'I don't know' for every item.", "C": "Circle answers without looking at the clues.", "D": "Copy the first answer you see."}, "A", "Explaining a choice and comparing evidence makes the learner's reasoning visible during answer checking.", "用『可觀察證據』判斷參與品質，而不是只看是否在紙上留下記號。", ["確認活動是 check answers together，重點包含理由與證據。", "找出能說明選擇並與同伴核對的行動。", "檢查 A 同時有 explain 與 compare。", "排除 B、C、D，因為它們沒有呈現理解或推理。", "選 A，確認行為可讓教師與同儕看見學習證據。"], "medium"),
make(5, "A partner says, 'I am not sure how to pronounce this word.' What is a helpful response?", {"A": "Let's listen to the model and try it together.", "B": "It is your problem; do nothing.", "C": "Change the subject to lunch.", "D": "Laugh before the partner tries."}, "A", "Listening to a model and trying together supports pronunciation practice and keeps both students engaged.", "回應同儕困難時，選能提供共同練習與可操作下一步的句子。", ["找出同儕的困難是 pronunciation，不是字義或作業日期。", "尋找包含聽示範與再次嘗試的方案。", "檢查 Let's... together 同時表達合作與行動。", "排除 B、C、D，因為它們拒絕、離題或破壞安全學習氣氛。", "選 A，確認回應直接支援發音練習。"], "medium"),
make(6, "The teacher gives three minutes to rehearse a presentation. Which plan uses the practice time well?", {"A": "Read the opening, rehearse the key sentence, and ask for one correction.", "B": "Wait until the three minutes end without speaking.", "C": "Decorate the notebook instead of rehearsing.", "D": "Memorize a different subject's paragraph."}, "A", "A uses the limited time to practice relevant parts and obtain focused feedback.", "把時間限制與任務目標一起檢查，選有順序、相關且能得到回饋的行動。", ["圈出 three minutes 與 rehearse a presentation。", "列出相關步驟：開頭、關鍵句、一次修正。", "確認 A 的三個行動都直接服務簡報。", "排除 B、C、D，因為它們浪費時間或偏離主題。", "選 A，回讀確認計畫可在限定時間內執行。"], "medium"),
make(7, "After a speaking activity, which reflection best helps a learner improve next time?", {"A": "I used the past tense correctly, but I need to pause between ideas.", "B": "Everything was bad and I learned nothing.", "C": "My partner's answer was the only important thing.", "D": "I will never speak English again."}, "A", "A names one successful language feature and one specific next improvement, making reflection actionable.", "找同時包含具體證據與下一步的反思，不用籠統自責取代分析。", ["確認題目問的是活動後 reflection。", "尋找一項已做到的語言證據與一項可改進技巧。", "檢查 A 的 past tense 與 pausing 都是可觀察項目。", "排除 B、C、D，因為它們過度籠統、轉移焦點或放棄學習。", "選 A，確認反思能直接轉成下一次練習目標。"], "medium"),
make(8, "Your group must choose a topic for an English poster. Which action is most cooperative?", {"A": "Suggest one topic, listen to two ideas, and vote with reasons.", "B": "Choose secretly and refuse all comments.", "C": "Wait for the teacher to do the group work.", "D": "Delete every idea except your own."}, "A", "A contributes an idea, listens, and uses a transparent decision process with reasons.", "將合作拆成提出、聆聽與共同決策三個可檢查行動。", ["找出任務是小組選 topic，不是個人獨自作答。", "列出合作證據：suggest、listen、vote with reasons。", "檢查 A 三項都具備且順序合理。", "排除 B、C、D，因為它們拒絕討論或把責任交給別人。", "選 A，確認決策過程讓所有成員有參與機會。"], "medium"),
make(9, "A student answers incorrectly during a class game. What response supports continued participation?", {"A": "Use the hint, try again, and explain the new choice.", "B": "Hide the answer and stop joining.", "C": "Blame a teammate immediately.", "D": "Shout the same answer without checking."}, "A", "Using feedback, retrying, and explaining the revised choice turns an error into another learning attempt.", "把錯誤視為修正循環，選能使用提示、重試並說明證據的行動。", ["確認情境是答錯後仍可繼續的 class game。", "找出 feedback、retry 與 explanation 的完整循環。", "檢查 A 三步都直接處理錯誤與學習。", "排除 B、C、D，因為它們退出、指責或拒絕檢查。", "選 A，確認錯誤後仍保持可觀察的參與。"], "medium"),
make(10, "When a pair finishes early, which action extends the English practice meaningfully?", {"A": "Switch roles and create one new example using the same pattern.", "B": "Close the book and distract nearby groups.", "C": "Repeat the exact answer without changing anything.", "D": "Leave before the teacher checks the work."}, "A", "Switching roles and creating a new example transfers the practiced pattern instead of merely repeating it.", "判斷延伸活動是否保留核心語言並增加新情境與角色轉換。", ["確認原任務已完成，題目問的是 meaningful extension。", "找能保留 same pattern 又改變角色與例子的行動。", "檢查 A 同時有 switch roles 與 new example。", "排除 B、C、D，因為它們干擾、機械重複或提早退出。", "選 A，確認延伸仍是英語練習且增加遷移。"], "hard"),
]

KEYS = ["B", "D", "A", "C", "B", "D", "C", "A", "D", "B"]
CUSTOM_STEPS = [
    ["先確認指令要求兩人輪流演練，而不是只完成書面抄寫。", "把任務拆成扮演角色、說出台詞、聽懂搭檔三種參與證據。", "對照四個選項，只有原正解同時照顧說與聽。", "排除旁觀、抄標題和離開等沒有投入對話練習的行動。", "答案是 B：實際接演並留意搭檔回合，完成雙向練習。"],
    ["把卡點界定為聽不懂教師指示，先不要猜活動內容。", "需要的下一步是請對方重說或放慢，而非轉移話題。", "逐項檢查語句是否禮貌、是否指出自己需要的協助。", "忽略、離題或趴下都不會補回缺失的指令資訊。", "答案是 D：禮貌請求重述後，就能接續課堂任務。"],
    ["觀察小組目前的問題是有人尚未取得發言機會。", "此時應把話輪交給該同學，而不是替她回答。", "檢查選項是否以開放問句邀請觀點、沒有預設答案。", "排除拒絕加入、獨占回答或要求停止聆聽的做法。", "答案是 A：直接詢問 Maya 的看法，讓她能加入討論。"],
    ["答案核對不只要留下記號，還要讓理由可被檢視。", "選出同時包含說明依據和同伴比對的行為。", "看題目線索能否支持所選答案，不能只照抄。", "未看線索的圈選、盲從及反覆說不知道都缺乏證據。", "答案是 C：解釋並與搭檔比對，呈現自己如何判斷。"],
    ["先聽出同伴需要的是發音協助，不是換話題或代做。", "有效支援應給一個可立即採取的共同練習步驟。", "核對建議是否包含聽示範及親自再試一次。", "嘲笑、置之不理與轉移到午餐都不能回應發音困難。", "答案是 B：一起聽範例再試讀，保留雙方的練習機會。"],
    ["三分鐘是有限資源，先圈定簡報而非其他科目的目標。", "排出可在短時間完成的優先序：開場、核心句、一次回饋。", "檢查每一步是否能讓口頭呈現更清楚。", "等待、裝飾筆記或背別科段落都偏離演練目標。", "答案是 D：用短回合練習核心內容，再取得一項修正建議。"],
    ["反思要能回答『哪裡做到了』及『下次改什麼』。", "比較四句，找出同時指出語言表現與具體調整者。", "過去式使用和想法間停頓都能在下一次觀察。", "全盤否定、只評論搭檔或拒絕開口都沒有設定可行目標。", "答案是 C：保留一項成功證據，再把停頓列為下一步練習。"],
    ["小組任務的產出是共同選題，不是個人決定。", "合作過程要容納不同提案並讓決策理由透明。", "檢視選項是否依序做到提案、聆聽與共同選擇。", "暗中決定、等老師代做或刪除別人的想法都排除成員。", "答案是 A：提出想法、聽取同學並說明投票理由。"],
    ["把答錯視為回饋訊號，題目問的是如何留在活動中。", "先利用提示重新檢查，而不是立刻歸咎隊友。", "再選一次後要說明新判斷依據，才能確認修正有效。", "退出、重複喊同一答案或責怪他人都沒有使用回饋。", "答案是 D：看提示、再嘗試並交代理由，完成一次修正循環。"],
    ["兩人已完成第一輪，延伸活動應增加遷移而非干擾。", "保留原句型，同時換角色或自造新例子。", "判斷活動是否讓兩人都能再輸出一次英語。", "單純重複、離場和打擾別組都沒有增加語言練習。", "答案是 B：交換角色並造新例句，把熟悉形式帶到新內容。"],
]
for index, question in enumerate(Q):
    correct_text = question["options"][0]["text"]
    distractors = [option["text"] for option in question["options"][1:]]
    ordered_texts = distractors[:]
    ordered_texts.insert(ord(KEYS[index]) - ord("A"), correct_text)
    question["options"] = [{"id": chr(65 + i), "text": text} for i, text in enumerate(ordered_texts)]
    question["answer"]["value"] = KEYS[index]
    question["solutionSteps"] = CUSTOM_STEPS[index]
    question["answer"]["explanation"] = CUSTOM_STEPS[index][-1]
    question["provenance"]["authoringNote"] = "依官方課綱與該單元課堂參與能力，參考三份公立學校公開英文評量的聽辨、對話理解與情境回應型態，獨立撰寫題幹、選項、答案與解法；未複製來源內容，維持 draft 待後續內容／版權 QA。"

for question in Q:
    (OUT / f"{question['id']}.json").write_text(json.dumps(question, ensure_ascii=False, indent=2) + "\n", encoding="utf-8")
print(f"rewrote {len(Q)} questions")
