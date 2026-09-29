#!/usr/bin/env python3
"""Independently rewrite 7-IV-4 discussion-transfer questions and evidence."""
import json
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
QDIR = ROOT / "questions/english"
TODAY = "2026-09-27"
SOURCES = [
    {
        "url": "https://www.kcjh.kh.edu.tw/upload/190/104_34764/%E4%B8%80%E5%B9%B4%E7%B4%9A-%E8%8B%B1%E8%AA%9E.pdf",
        "title": "高雄市立國昌國中110學年度第1學期第1次段考七年級英文科試題",
        "year": "110-1",
        "locator": "PDF第2頁第21至25題對話回應及第3頁第32至33題對話理解；只參考題型，不重用原題",
        "level": "item",
        "pattern": "公開卷以情境對話及合宜回應檢查語意理解；本題轉為小組討論中提出理由、釐清與協作的全新語境。",
    },
    {
        "url": "https://www.ycm.kh.edu.tw/upload/297/104_62703/111-1%282%29%E4%B8%83%E5%B9%B4%E7%B4%9A%E8%8B%B1%E6%96%87%E8%A9%A6%E9%A1%8C.pdf",
        "title": "高雄市立燕巢國中111學年度第1學期第2次段考七年級英文科試題",
        "year": "111-1",
        "locator": "整份七年級英文試卷；只參考對話選句與情境語意評量型態",
        "level": "paper",
        "pattern": "卷內有依情境選出合宜回應的對話題型；本站獨立設計討論目的、理由品質、澄清及結論整理。",
    },
    {
        "url": "https://www.ycjh.hlc.edu.tw/modules/tad_uploader/index.php?cat_sn=417&cfsn=2790&name=112-2-%E7%AC%AC2%E6%AC%A1%E6%AE%B5%E8%80%837%E5%B9%B4%E7%B4%9A%E8%8B%B1%E8%AA%9E%E8%81%BD%E5%8A%9B%E9%A1%8C%E7%9B%AE%E8%88%87%E7%AD%94%E6%A1%88-%E9%82%B1%E6%9B%89%E8%96%87.pdf&op=dlfile",
        "title": "花蓮縣立宜昌國中112學年度第2學期第2次段考七年級英文聽力試題與答案",
        "year": "112-2",
        "locator": "聽力PDF第1頁第7至8題及第2頁第9至13題基本問答；僅參考情境回應型態",
        "level": "item",
        "pattern": "公開七年級聽力卷以提問、請求及情境回應檢查理解；本題另加入共同推理與任務遷移，不沿用原對話。",
    },
]

ITEMS = [
    {
        "answer": "C",
        "options": ["The project has a title and a deadline.", "Maybe someone brought a pencil yesterday.", "I think a school garden is best because we can observe it every week.", "I will not say anything about the project or its purpose."],
        "explanation": "正確答案是 C。這句先清楚表明偏好（school garden），再用每週可觀察作為理由，聽者能檢查理由是否支持選擇。B 只是猜測昨天發生的事，沒有回應專題選擇；A 是事實資訊，D 則沒有提出立場。",
        "strategy": "辨認一個完整意見至少包含「主張＋相關理由」；再檢查理由能否說明為什麼該方案適合目前任務。",
        "steps": ["題目要選出小組專題的意見句，所以先找出明確的方案立場。", "A 說的是標題與期限等事實，沒有選擇；B 是與專題無關的猜測；D 沒有表態。", "C 的主張是選校園菜園，because 後提供每週可觀察的原因。", "每週觀察直接支持這個專題適合持續研究，故答案為 C。", "討論時仍可接著問觀察哪些指標，確認理由能否轉成可執行的研究計畫。"],
    },
    {
        "answer": "A",
        "options": ["It connects the recommendation to survey evidence.", "It repeats the recommendation without support.", "It changes the topic to a sports score.", "It says evidence is never useful."],
        "explanation": "正確答案是 A。調查顯示多數學生每天帶飲料，這項資料和「使用可重複使用杯」的建議有直接關聯，讓主張不只停留在個人喜好。資料仍只描述調查對象與習慣，並未證明實施後一定減少多少垃圾。",
        "strategy": "檢查資料是否與主張同題、能否支持主張，以及證據實際允許多強的結論；不要把相關資料誇大成因果證明。",
        "steps": ["先摘出主張：班級應使用可重複使用的杯子。", "再看資料內容：調查發現多數同學每天會帶飲料，這和杯子的使用頻率有關。", "A 把建議連到可檢查的調查結果；其餘選項不是無證據重說，就是離題或否定證據。", "因此答案是 A，理由與建議之間有可說明的關聯。", "若要預測減廢效果，還須蒐集一次性杯使用量等資料，不能只憑這份習慣調查下因果結論。"],
    },
    {
        "answer": "D",
        "options": ["Why do you have any schedule at all?", "Can we ignore every idea and leave?", "Did the schedule happen in a different century?", "Which part of the schedule should we change, and why?"],
        "explanation": "正確答案是 D。夥伴只說要改行程，尚未指出哪一段不合適，也沒有交代原因；D 同時追問修改位置和理由，能把模糊意見轉為可討論的資訊。其他問句沒有聚焦目前決策。",
        "strategy": "面對沒有細節的建議，提出一個聚焦且不帶指責的追問，先釐清修改對象，再了解背後條件或證據。",
        "steps": ["目前收到的訊息只有「改行程」，尚不知道要改哪個時段或活動。", "小組需要定位問題並理解原因，才可能比較替代方案。", "D 分別詢問要改的部分和理由；A、B、C 都沒有取得這兩項決策資訊。", "選 D 作為最能推進討論的追問。", "得到回答後，可把需求改寫成具體條件，例如保留集合時間但縮短某段活動，再檢查全組是否同意。"],
    },
    {
        "answer": "B",
        "options": ["Pictures are words, so no explanation is needed.", "I agree; pictures could help readers understand the process.", "Your idea is useless, and I will erase it.", "I agree with nothing, so the report is finished."],
        "explanation": "正確答案是 B。這句先明確同意，再解釋圖片如何幫助讀者理解流程，既回應同學的提議，也交代支持理由。A 把圖像和文字混為一談，C 帶有貶抑，D 則把個人態度當成結束合作的理由。",
        "strategy": "表達同意時不要只說 yes；指出提議的哪個功能有幫助，讓團隊知道可保留的優點及預期讀者效果。",
        "steps": ["同學提議在報告中加入圖片，題目要判斷哪句是尊重且有內容的同意。", "B 的 I agree 直接表明立場，後半句則指出圖片可協助讀者理解流程。", "這個理由連結到報告受眾；A 混淆圖文，C 否定同學，D 停止合作。", "所以選 B，因為它兼有同意訊號與具體理由。", "團隊接著可討論圖片要標示哪些步驟，避免只有裝飾而沒有說明功能。"],
    },
    {
        "answer": "D",
        "options": ["That is a terrible idea, and no one may discuss it.", "The cost is high, so I will change the entire subject.", "I disagree but will not explain or suggest anything.", "I see the benefit, but the cost may be too high; could we compare a cheaper option?"],
        "explanation": "正確答案是 D。這句先承認活動可能有好處，再指出成本疑慮，最後提出比較較便宜方案的下一步；反對意見因此聚焦問題並保留協作空間。其餘選項不是人身否定，就是逃避討論，或只反對而不說明。",
        "strategy": "建設性不同意可依序說出對方方案的價值、自己的具體顧慮，再提出可比較或可查證的替代方向。",
        "steps": ["題目不是要找最強硬的反對，而是要處理活動預算可能超支。", "A 先承認方案的好處，顯示有理解對方提案，而非直接否定提議者。", "接著把不同意的焦點限定在成本，並邀請比較較便宜的選項。", "故答案選 A：它把分歧轉成可共同檢查的選擇。", "小組應再列出費用與必要條件；若便宜方案仍符合活動目的，就能用資料而非音量決定。"],
    },
    {
        "answer": "C",
        "options": ["We canceled Friday and will not share any work.", "One person will do every task without a deadline.", "We will meet Friday, divide tasks, and share drafts Monday.", "The group discussed weather but made no plan."],
        "explanation": "正確答案是 C。討論已形成三項約定：週五見面、分配工作、週一分享草稿。C 保留了行動、分工與期限；其他選項竄改或遺漏決議內容。",
        "strategy": "會後摘要要逐項核對「做什麼、誰或哪些人負責、何時完成」；只保留討論中真正同意的資訊。",
        "steps": ["把原決議切成可核對的欄位：週五碰面、分配任務、週一交草稿。", "檢視 C，三項資訊都在且順序清楚。", "A 否認週五與草稿，B 添加單人負責且刪掉期限，D 把主題改成天氣。", "答案是 C，因為它沒有新增或刪除任何約定。", "發送摘要前，團隊還可補上每項任務負責人；若原討論未決定人選，就標示待確認而非自行填入。"],
    },
    {
        "answer": "B",
        "options": ["Only my topic matters, so stop talking.", "Could we combine the topics or compare them using the project requirements?", "We should choose without hearing either reason.", "Let us abandon the assignment immediately."],
        "explanation": "正確答案是 B。兩位同學各有不同題目，B 提出兩條公平路徑：檢查能否整合，或依共同的作業條件比較；它不預設誰的偏好更重要。其餘選項壓制發言、跳過理由或直接放棄任務。",
        "strategy": "衝突時先找共享的決策標準，再比較方案如何符合標準；若可整合，也要檢查整合後是否仍能完成任務。",
        "steps": ["目前有兩個不同主題，還沒有共同的比較依據。", "B 先詢問能否合併，若不能，再依作業要求比較，讓雙方提案使用同一標準。", "A 強迫服從；C 不聽理由；D 尚未分析就放棄。", "所以答案選 B，因為它促成公平而有程序的選擇。", "下一步要把作業要求轉成檢核點，例如資料是否找得到、能否在期限內完成，再逐項比較兩個主題。"],
    },
    {
        "answer": "D",
        "options": ["Pretend the reason was clear and vote randomly.", "Interrupt with an unrelated complaint.", "Reject the proposal only because the speaker paused.", "Ask a focused follow-up question and restate what you understood."],
        "explanation": "正確答案是 D。理由聽不清楚時，先用聚焦問題補足資訊，再覆述自己聽到的意思，能讓提出者確認有沒有理解錯。隨機投票或依停頓猜測都不是在檢查理由，插入無關抱怨則讓討論偏離主題。",
        "strategy": "把聽到的理由以自己的話重述，再用一個具體追問確認關鍵因果或證據；確認前先不把它當作已理解。",
        "steps": ["先標記理解缺口：對方提出理由，但你目前無法說明它如何支持方案。", "D 同時安排追問和重述，能檢查缺少的細節並讓對方糾正誤解。", "其餘做法以隨機、離題或無根據的語音線索代替理由檢查。", "因此選 D，先釐清再決定是否接受提案。", "覆述時保持中性；若對方修正你的理解，就更新摘要，避免把錯誤版本帶進最後表決。"],
    },
    {
        "answer": "A",
        "options": ["Invite a partner's evidence, compare explanations, and reach a reasoned conclusion.", "Copy the first answer without listening to anyone.", "Avoid all questions because science has one voice.", "Choose the loudest person's conclusion without evidence."],
        "explanation": "正確答案是 A。科學探究中的討論要讓不同觀察或證據進入比較，再說明哪個解釋最能符合資料；A 保留了聆聽、比較與有理由結論。複製第一個答案或依聲量決定，都沒有檢查證據。",
        "strategy": "把一般討論流程帶進學科任務：邀請不同觀察，區分觀察結果與解釋，再用證據比較而非憑人數或音量下結論。",
        "steps": ["這是把討論技巧轉移到科學探究，不是單純選出最快的答案。", "A 邀請夥伴提供證據，讓小組能比較不同解釋和觀察。", "科學結論仍需接受提問；抄答案和選最大聲者都避開了資料檢查。", "所以正解是 A：聽取證據、比較解釋，再形成有根據的結論。", "若兩種解釋目前都可能，應記下尚缺的觀察或測量，而不是把暫時結論說成確定事實。"],
    },
    {
        "answer": "C",
        "options": ["Vote before hearing any reason and ignore safety information.", "Let one person decide and prevent questions.", "State preferences, ask for route evidence, clarify safety concerns, compare options, and summarize the decision.", "Discuss only personal preferences and record no conclusion."],
        "explanation": "正確答案是 C。選校外教學路線牽涉偏好與安全，C 讓成員先提出想法、檢查路線證據、釐清安全疑慮、比較方案，最後留下決定摘要。其他選項先投票或交由一人決定，會跳過重要資料；只聊偏好則無法形成行動方案。",
        "strategy": "多條件決策依序處理偏好、可核實資料、風險與共同標準，最後記錄決定及仍待確認事項。",
        "steps": ["辨認任務是選路線，且題目明確指出安全資訊不可忽略。", "C 先讓成員表達偏好，再要求路線證據並釐清安全疑問。", "比較選項後才整理共同決定，順序符合審慎小組討論。", "答案選 C；其餘做法跳過安全、壓制提問或不留下決策結果。", "若安全資料不足，摘要應註明需再查證的路段與負責人，不要把未確認的路線寫成已核定。"],
    },
]


def refs_for(i: int) -> list[dict]:
    focus = [
        "辨認主張並判斷理由是否切合小組任務",
        "檢查建議和調查資料的關聯及推論界線",
        "追問模糊提案以補足決策所需資訊",
        "以理由回應同伴提議並維持合作語氣",
        "提出有根據的不同意見與可比較替代方案",
        "忠實整理行動、分工與期限等會議結論",
        "使用共同標準公平比較彼此提案",
        "透過澄清及覆述檢查是否理解對方理由",
        "把聆聽證據與比較解釋遷移到學科探究",
        "整合偏好、證據、安全條件並形成決議",
    ][i - 1]
    return [{
        "url": src["url"], "title": src["title"], "year": src["year"],
        "subject": "english", "locator": src["locator"],
        "observedPattern": f"{src['pattern']}本題改寫焦點：{focus}。",
        "reuseDecision": "pattern-only", "status": "recorded",
        "locatorLevel": src["level"],
    } for src in SOURCES]


for i, item in enumerate(ITEMS, 1):
    path = QDIR / f"question-english-performance-7-iv-4-{i}.json"
    data = json.loads(path.read_text(encoding="utf-8"))
    data["options"] = [{"id": chr(65 + j), "text": text} for j, text in enumerate(item["options"])]
    data["answer"] = {"value": item["answer"], "explanation": item["explanation"]}
    data["examPatternRefs"] = refs_for(i)
    data["provenance"]["sourceUrl"] = SOURCES[0]["url"]
    data["provenance"]["sourceLocator"] = "國昌、燕巢、宜昌三所公立國中公開七年級英文評量；僅研究情境對話、提問及回應的題型，不複製原題、選項或答案。"
    data["provenance"]["authoringNote"] = "依官方英語課綱 KG 與三所公立國中公開英文評量的情境互動型態，獨立撰寫本題題幹、選項、正解、繁中解析、策略及五步解法；未複製原卷，完整內容與版權 QA 尚待完成。"
    data["solutionStrategy"] = item["strategy"]
    data["solutionSteps"] = item["steps"]
    data["updatedAt"] = TODAY
    data["reviewStatus"] = "draft"
    path.write_text(json.dumps(data, ensure_ascii=False, indent=2) + "\n", encoding="utf-8")

print(f"rewrote {len(ITEMS)} original 7-IV-4 questions; all remain draft")
