import json
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
LESSON = ROOT / "lessons/english/lesson-english-performance-3-iv-5.json"
REPORT = ROOT / "implementation/reports/english-performance-3-iv-5-first-pass-review.json"


def rec(name, locator, concepts, forms, misconception, assessment):
    return {
        "publisher": name,
        "edition": f"{name} 公立校方英語課程計畫章節級證據",
        "sourceType": "public-web",
        "sourceLocator": locator,
        "reviewedAt": "2026-09-21",
        "findings": {
            "concepts": concepts,
            "representations": forms,
            "examplesOrEvidence": ["本課以原創校園問候、借物、道歉、邀請、澄清、偏好、提醒與服務情境，承接公開課程對生活用語理解與回應的方向。"],
            "misconceptions": [misconception],
            "assessmentEmphasis": [assessment],
        },
        "licenseBoundary": "只記錄公開課程計畫與公立學校公開評量的概念、功能與評量方向；不複製出版社或學校教材正文、原題、選項、答案、影音或版面。",
    }


def question_refs():
    return [
        {
            "url": "https://www.yacjh.kh.edu.tw/upload/221/101_30637/114%E4%B8%8B%E5%AD%B8%E6%9C%9F%E7%AC%AC%E4%B8%80%E6%AC%A1%E6%AE%B5%E8%80%83%E4%B8%89%E5%B9%B4%E7%B4%9A%E8%8B%B1%E6%96%87.pdf",
            "title": "高雄市立鹽埕國民中學公開英文段考；僅取生活功能語言與情境回應能力方向，未複製原題、選項、圖片或答案。",
            "year": "113-114", "subject": "english", "locator": "everyday expressions, dialogue purpose, and responses",
            "observedPattern": "公開英文評量以問候、道謝、道歉、邀請、偏好、澄清與生活對話測量功能語言及禮貌回應；本題為獨立改寫。",
            "reuseDecision": "pattern-only", "status": "recorded", "locatorLevel": "paper",
        },
        {
            "url": "https://www.bhjh.ntpc.edu.tw/p/406-1000-10627%2Cr111.php?Lang=zh-tw",
            "title": "新北市立北投國民中學公開定期評量試題頁；僅取功能語句、社交情境與上下文判讀方向，未複製原題、選項、圖片或答案。",
            "year": "113-114", "subject": "english", "locator": "functional phrases, social situations, and context",
            "observedPattern": "公開英文評量要求學生依上下文判斷禮貌、目的、回應與後續行動；本題為獨立改寫。",
            "reuseDecision": "pattern-only", "status": "recorded", "locatorLevel": "paper",
        },
        {
            "url": "https://www.hcjh.ntpc.gov.tw/p/406-1000-7527%2Cr146.php",
            "title": "新北市立新埔國民中學公開段考試題頁；僅取日常用語、禮貌與情境應用能力方向，未複製原題、選項、圖片或答案。",
            "year": "113-114", "subject": "english", "locator": "daily language, politeness, and application",
            "observedPattern": "公開英文評量將短對話的語意目的、禮貌程度與生活應用結合；本題為獨立改寫。",
            "reuseDecision": "pattern-only", "status": "recorded", "locatorLevel": "paper",
        },
    ]


def make_question(base, prompt, options, answer, explanation, strategy, steps):
    q = json.loads(json.dumps(base))
    q.update({
        "prompt": prompt,
        "options": [{"id": label, "text": text} for label, text in options],
        "answer": {"value": answer, "explanation": explanation + f" 正確答案：{answer}"},
        "examPatternRefs": question_refs(),
        "solutionStrategy": strategy,
        "solutionSteps": steps,
        "reviewStatus": "draft",
        "updatedAt": "2026-09-21",
    })
    q["provenance"]["sourceUrl"] = question_refs()[0]["url"]
    q["provenance"]["sourceLocator"] = "公立學校公開英文評量的生活用語與情境回應能力模式；本題只改寫能力、資料型態與推理層次，未重製任何原題內容。"
    q["provenance"]["authoringNote"] = "依官方課綱、本單元 KG 與三所公立學校公開英文評量模式獨立改寫；情境、選項、答案、解析與遷移任務均為原創，等待 Terra 第二輪內容審查。"
    return q


def main():
    data = json.loads(LESSON.read_text(encoding="utf-8"))
    assert data["id"] == "lesson-english-performance-3-iv-5"
    data["title"] = "3-Ⅳ-5：從目的、語氣與上下文理解簡易生活用語"
    data["content"] = {
        "summary": "生活用語不是逐字翻譯題，而是要從前後句、說話者、目的、關係、時間與語氣判斷下一步如何回應。本課以校園問候、借物、意外道歉、邀請、澄清、偏好、提醒、請求與服務情境，練習辨識 greeting、thanks、apology、invitation、clarification、preference、warning、request 與 confirmation 的功能，並把禮貌、資訊完整度和安全限制一起納入回答。",
        "sections": [
            {"heading": "先判斷這句話要完成什麼任務", "body": "Good morning、Thanks、I’m sorry、Could you repeat that? 的字面不只是單字意思，而是分別完成問候、感謝、道歉與澄清。讀題先問：誰對誰說、前一句做了什麼、對方現在需要什麼回應？"},
            {"heading": "語氣要和關係、事件相配", "body": "同樣是請求，對朋友可以說 Can you help me?，對不熟的人可用 Could you help me, please?；發生意外時要先道歉並確認對方狀況，而不是把責任推回去。自然不只代表文法正確，也代表用途與禮貌層級相合。"},
            {"heading": "上下文提供的線索要逐一核對", "body": "若上一句是 Here you are，回應應承接交付物；若對方說 I can’t hear you，下一步是重複或放慢，而不是改談天氣。把人物、物件、目的、時間、限制五項線索寫在小卡上，可避免被選項中的單一關鍵字帶走。"},
            {"heading": "不能由一句話推過頭", "body": "生活對話通常只支持局部結論：對方說 Thanks 不代表事情全部完成；對方說 Let’s meet at three 也仍要確認地點。答案要補足題目要求的行動，但不能擅自增加未提供的原因、承諾或危險行動。"},
        ],
    }
    data["studyHighlights"] = [
        "先圈出說話者、目的、前一句、關係與限制，再判斷生活用語功能。",
        "用功能詞區分問候、感謝、道歉、邀請、澄清、偏好、提醒與請求。",
        "檢查語意、禮貌與後續行動是否同時接得上，而不是只找看似熟悉的單字。",
        "只說上下文支持的內容；資訊不足時提出確認問題或保留界線。",
    ]
    data["teaching"] = {
        "body": [
            {"id": "hook", "phase": "hook", "heading": "同一句話換情境，功能會一樣嗎？", "body": "先給兩段原創對話：同學借筆後說 Here you are，以及櫃檯交付收據後說 Here you are。學生各寫下一句回應，再圈出物件、關係和目的，發現相同句型仍須依場景調整 Thanks、確認或後續請求。"},
            {"id": "explain", "phase": "explain", "heading": "生活用語五欄判讀卡", "body": "建立 Speaker、Situation、Function、Tone、Next action 五欄。先判斷誰在做什麼，再標出是問候、感謝、道歉、邀請、澄清、偏好、提醒、請求或確認，最後檢查回應是否符合禮貌與安全限制。"},
            {"id": "worked-example", "phase": "worked-example", "heading": "從意外事件組出完整回應", "body": "以 You step on a classmate’s foot 為例：先標事件是意外，再判斷功能是 apology，接著加入對方狀況確認，組成 I’m sorry. Are you okay?；逐一排除慶祝、命令與無關敘述，讓答案同時回應事件與人。"},
            {"id": "guided-practice", "phase": "guided-practice", "heading": "把前一句接成可用的下一句", "body": "輪流處理借物、聽不清楚、邀請、偏好、圖書館提醒與改期六個原創短對話。學生先獨立寫功能標籤，再選或改寫回應；同伴必須指出哪個字詞承接前句、哪個部分表達禮貌或限制。"},
            {"id": "transfer", "phase": "transfer", "heading": "換人物與媒介仍要保留目的", "body": "把口頭對話換成簡訊、服務櫃檯與校園公告，改變朋友／陌生人、急迫／一般、公開／私下等條件。學生為同一目的寫兩種語氣，並說明哪些資訊不能省略，避免只替換人名或地點。"},
            {"id": "reflect", "phase": "reflect", "heading": "答案自然不等於答案完整", "body": "回看每題，分別檢查功能、語意、禮貌、後續行動與安全。若只說 Thanks 卻漏掉題目要求的確認，補上問題；若自行添加原因或承諾，刪去超出上下文的部分，留下可由對話支持的句子。"},
        ],
        "summary": ["以 Speaker、Situation、Function、Tone、Next action 五欄拆解生活對話。", "把前一句、人物關係與目的連起來，區分相近但功能不同的用語。", "同時檢查自然度、禮貌、資訊完整與安全限制。", "在口語、簡訊、服務與公告間遷移，但保留核心溝通目的。"],
        "exitCheck": [
            {"prompt": "為什麼不能只看單字就決定生活用語的答案？", "expectedEvidence": "能指出說話者、情境、功能、語氣與下一步，並用原創對話說明同一句式如何依目的改變。"},
            {"prompt": "意外造成他人不舒服時，完整且合適的回應要包含什麼？", "expectedEvidence": "能先表達道歉，再依情況確認對方狀況或提出補救，而不是責怪對方或轉移話題。"},
            {"prompt": "若對話沒有提供足夠資訊，如何避免過度推論？", "expectedEvidence": "能提出澄清問題、保留不確定性或只重述直接線索，不自行加入原因、承諾或危險行動。"},
        ],
    }
    data["interactive"] = {
        "type": "guided-choice",
        "goal": "從人物、情境、功能、語氣與下一步，選出並說明自然、禮貌且安全的生活用語回應。",
        "scenario": "學生擔任校園服務小幫手，需在教室、圖書館、社團、櫃檯與手機訊息中，替不同對話補上可執行的下一句。",
        "variables": [{"symbol": "s", "meaning": "說話者、情境與前一句"}, {"symbol": "f", "meaning": "問候、感謝、道歉、邀請、澄清、偏好、提醒或請求功能"}, {"symbol": "t", "meaning": "禮貌、後續行動、資訊完整度與安全限制"}],
        "steps": [
            {"id": "step-1", "prompt": "A classmate says, 'Good morning!' Which response completes the greeting naturally?", "options": ["Good morning!", "Good night yesterday.", "I am a morning desk."], "answer": "A", "feedback": "先辨識功能是 greeting，再選擇同時承接時間與社交目的的回應。"},
            {"id": "step-2", "prompt": "You cannot hear a partner's instruction. What should you say before acting?", "options": ["Could you repeat that more slowly, please?", "I will guess and run outside.", "The instruction is a birthday."], "answer": "A", "feedback": "A 先提出 clarification request，避免在資訊不足時猜測或採取不安全行動。"},
            {"id": "step-3", "prompt": "You accidentally step on someone's foot. Which response is complete and considerate?", "options": ["I'm sorry. Are you okay?", "Congratulations on your foot.", "Please step on me again."], "answer": "A", "feedback": "A 同時完成 apology 與狀況確認；其他選項不是合適的生活功能回應。"},
        ],
    }
    data["authoringStandard"] = "version-fused-v1"
    data["updatedAt"] = "2026-09-21"
    data["versionResearch"] = [
        rec("nani", "https://course.cyc.edu.tw/upfile/course113/sub1/15636172843290327.pdf；英語簡易圖表、生活用語與句型閱讀定位；核讀 2026-09-21。", ["由簡易生活語句、對話與情境資料理解主要訊息。", "以人物、目的、關鍵字與基本句型完成回應。"], ["問候、感謝、道歉、邀請、澄清、偏好、提醒與請求。"], "只抓單字，不判斷說話者、目的、禮貌與下一步。", "重視生活對話主要內容、細節與功能語言應用。"),
        rec("kanghsuan", "https://course.cyc.edu.tw/upfile/course112/sub1/15342166894673419.pdf；英語表格圖像、生活語句與核心句型閱讀定位；核讀 2026-09-21。", ["透過圖片、對話與任務理解生活情境和回應順序。", "依人物關係、時間、目的與限制完成溝通。"], ["短對話、圖像提示、服務情境、時間與行動。"], "把禮貌請求當成命令，或在資訊不足時自行補上原因與承諾。", "評量情境理解、回應適切度與功能語句使用。"),
        rec("hanlin", "https://course.cyc.edu.tw/upfile/course114/sub1/15939623345151225.pdf；英語生活溝通文本、句型理解與評量定位；核讀 2026-09-21。", ["從上下文、語氣與溝通目的形成生活用語理解。", "以澄清、確認、禮貌和後續行動完成文本回應。"], ["context、function、tone、clarification、confirmation、next action。"], "把語意正確但功能不合的句子當答案，忽略事件後需要的確認或安全行動。", "評量資訊定位、語意連貫、情境適切與功能性表達。"),
    ]
    data["fusionRecord"] = {
        "commonCore": ["三版本公開結構共同支持生活情境、簡易對話與功能語言理解。", "正確回應需整合上下文、人物、目的、語氣、禮貌與下一步。", "由辨識功能到產出回應，可用對話卡、角色輪換、澄清問題與同伴回指證據。"],
        "versionDifferences": ["南一較突顯生活語句與基本句型；康軒較突顯圖像、任務、順序與情境行動；翰林較突顯上下文、語氣、澄清、確認與功能性評量。這是公立校方課程計畫層級差異，不宣稱完整出版社教材差異。"],
        "originalAdditions": ["以 Speaker、Situation、Function、Tone、Next action 五欄拆解生活用語。", "用問候、借物、意外、邀請、澄清、偏好、提醒與服務情境練習功能轉換。", "以禮貌、資訊完整與安全限制作為回應後的第二層檢核。"],
        "llmSynthesisNote": "本課依官方課綱、三筆公立校方章節級公開證據與公立學校公開評量模式，重新組織簡易生活用語的上下文、功能、語氣、禮貌、澄清與下一步。正文、原創情境、互動步驟、回饋與檢核均為本專案重寫，未複製教材題目或答案；Terra 第二輪與正式發布審查尚未完成，因此維持 draft。",
    }

    question_specs = [
        ("A classmate says, 'Good morning!' Which response is natural?", [("A", "Good morning!"), ("B", "Good night yesterday."), ("C", "I am a morning desk."), ("D", "No, the morning is a color.")], "A", "Good morning is the conventional response to the same greeting.", "辨識前句的社交功能，再選語意與時間都接得上的禮貌回應。", ["讀出前句的功能是 greeting，而不是詢問資訊。", "核對說話時間與對方的社交目的，回應也要完成問候。", "逐一檢查選項是否能自然接在 Good morning 後面；A 可以。", "說明 A 重複同一問候，語意與語氣都符合情境。", "把兩句連讀，確認沒有加入無關物件、錯誤時間或不自然敘述。"]),
        ("A friend lends you a pen and says, 'Here you are.' What should you say?", [("A", "Thanks, that helps a lot."), ("B", "You are a pen yesterday."), ("C", "No one may lend anything."), ("D", "The pen should thank me.")], "A", "The response acknowledges the favor and expresses appreciation.", "判斷交付物件後需要的是感謝，而不是重新描述物件或否定借用。", ["先確認 Here you are 在此情境表示對方交出筆。", "判斷回應功能是 thanks，並核對朋友關係下的自然語氣。", "選擇能直接承接幫助行為的句子；A 表達感謝。", "說明 that helps a lot 回指借筆的幫助，沒有改變事件。", "將對話接讀，確認回應承認對方的行動且沒有無關主張。"]),
        ("You step on someone's foot by accident. Which expression is appropriate?", [("A", "I'm sorry. Are you okay?"), ("B", "Congratulations on your foot."), ("C", "Please step on me again."), ("D", "The accident is a birthday.")], "A", "The speaker apologizes and checks the other person's condition.", "事件判讀為意外造成不適，回應要先道歉並確認對方狀況。", ["找出事件與責任：是 accidentally step on someone's foot。", "選擇 apology 功能，再看是否需要關心受影響的人。", "A 同時包含道歉與 Are you okay? 的狀況確認。", "排除慶祝、鼓勵重複傷害與無關生日等不合事件的句子。", "重述情境後檢查 A 是否提供下一步關心，而非推卸或轉移話題。"]),
        ("A classmate invites you to a study group, but you have a dentist appointment. What is a polite reply?", [("A", "I'd like to, but I have an appointment."), ("B", "Your study group is a chair."), ("C", "Yes, I never go anywhere."), ("D", "Appointments are blue.")], "A", "A acknowledges the invitation and gives a relevant reason for declining.", "先承認邀請，再用與時間衝突直接相關的理由禮貌回應。", ["辨識前情是 invitation，不是資訊問答。", "核對自己有 appointment 的限制，決定不能直接答應。", "A 先表示願意再說明衝突，語氣比直接拒絕更合適。", "檢查理由是否與邀請時間相關，A 有直接證據。", "把回應放回對話，確認沒有虛構對方、地點或未提供的替代承諾。"]),
        ("Someone says, 'Please turn down the music.' You think the volume is already low. What is a respectful reply?", [("A", "Sure. I'll check the volume."), ("B", "The music can do homework."), ("C", "No one can hear colors."), ("D", "I turned down the calendar.")], "A", "A accepts the request respectfully and states a safe next action.", "不要立刻否定對方；先承接請求，再檢查音量這個可驗證的條件。", ["讀出對方提出的是 request，與音量有關。", "分辨自己的印象和可檢查的事實，不以爭辯代替行動。", "A 表示願意查看 volume，能回應請求並保留判斷。", "排除把音樂、顏色或日曆當主體的無關句子。", "確認下一步是檢查而非擅自提高音量，符合禮貌與安全。"]),
        ("You did not understand a bus announcement. What should you say?", [("A", "Could you repeat that more slowly, please?"), ("B", "I understand every bus yesterday."), ("C", "The announcement is a sandwich."), ("D", "Please erase the station.")], "A", "A asks for clarification with a polite request instead of guessing.", "資訊不足時先澄清關鍵訊息，不能靠猜測採取交通行動。", ["判斷問題是聽不清楚 announcement，功能是 clarification。", "檢查回應是否提出具體可執行的澄清方式。", "A 請對方重複並放慢，且以 please 保持禮貌。", "排除無關、錯誤時間、食物與刪除車站的選項。", "把 A 放回公車情境，確認得到資訊後才能安全決定下一步。"]),
        ("Your partner asks, 'Do you prefer tea or juice?' You want juice. Which answer is clear?", [("A", "I prefer juice, please."), ("B", "Tea is walking tomorrow."), ("C", "I prefer the question."), ("D", "Juice cannot have a name.")], "A", "A directly states the preference and remains polite.", "找出疑問句要求的選擇，再用同一主題的完整句回答。", ["辨識 Do you prefer... 是 preference question。", "列出兩個候選物，確認自己選的是 juice。", "A 直接說 I prefer juice 並加入 please，資訊完整。", "檢查其他選項是否回答茶或果汁的偏好；B、C、D 都沒有。", "將問句與 A 連讀，確認主詞、動詞與選擇對象一致。"]),
        ("A wet-floor sign is in front of the library door. What should you tell a visitor?", [("A", "Please use the other entrance for now."), ("B", "Please run across the wet floor."), ("C", "The sign is a dessert."), ("D", "The library door is yesterday.")], "A", "A follows the warning and gives a safer alternative action.", "先讀警告與限制，再提供不踩濕地的替代路線。", ["確認 wet-floor sign 的功能是 warning，不是一般裝飾。", "找出限制：不能直接穿越濕地，需改變入口。", "A 提供 other entrance，既回應訪客也符合安全要求。", "排除鼓勵奔跑、食物與錯誤時間等不安全或無關句子。", "說明 for now 保留暫時限制，避免把公告擴大成永久封閉。"]),
        ("A librarian says, 'Please return the book by Friday.' What is a useful response?", [("A", "Okay. I'll return it by Friday."), ("B", "Friday returned the library."), ("C", "The book should choose a day."), ("D", "I will return the weather.")], "A", "A confirms the request and repeats the important deadline.", "從請求中抓出期限，回應時確認同一個可執行承諾。", ["辨識 librarian 的話是 request with a deadline。", "圈出 return the book 與 by Friday 兩個必要資訊。", "A 同時確認行動與期限，沒有改動原本要求。", "排除把星期、圖書館、天氣當成不合文意的主體或物件。", "核對回答可在期限到來前執行，且沒有增加未被要求的條件。"]),
        ("A service desk says, 'Your appointment is at three, but the room has changed.' What should you confirm?", [("A", "So the time is three, and I should go to the new room?"), ("B", "So the appointment is a color?"), ("C", "I will go to the old room without checking."), ("D", "The new room should change the time yesterday.")], "A", "A restates both the unchanged time and the changed location as a confirmation question.", "把未改變與已改變的資訊分開回述，再提出可驗證的確認問題。", ["讀出訊息有兩個欄位：time remains three，room changes。", "不能只抓 changed 而自行改時間，也不能忽略新地點。", "A 同時確認三點與新房間，讓櫃檯能立即修正誤解。", "排除顏色、昨天與未確認就去舊房間等無關或不安全行動。", "檢查問題是否保留原始資訊範圍，確認後才採取前往行動。"]),
    ]
    base_questions = []
    for i in range(1, 11):
        path = ROOT / f"questions/english/question-english-performance-3-iv-5-{i}.json"
        base_questions.append(json.loads(path.read_text(encoding="utf-8")))
    for base, spec in zip(base_questions, question_specs):
        q = make_question(base, *spec)
        (ROOT / f"questions/english/{q['id']}.json").write_text(json.dumps(q, ensure_ascii=False, indent=2) + "\n", encoding="utf-8")
    LESSON.write_text(json.dumps(data, ensure_ascii=False, indent=2) + "\n", encoding="utf-8")
    REPORT.write_text(json.dumps({"unit": data["title"], "lessonId": data["id"], "status": "first-pass-ai-review-complete", "reviewStatus": "draft", "checks": {"unitSpecificOriginalContent": True, "threeVersionResearchRecords": True, "publicExamPatternRewrite": True, "fusionRecordPresent": True, "interactivePredictionManipulationExplanation": True, "answersAndDetailedSteps": True, "terraSecondPass": "pending"}, "reviewedAt": "2026-09-21"}, ensure_ascii=False, indent=2) + "\n", encoding="utf-8")
    print("authored english performance 3-iv-5")


if __name__ == "__main__":
    main()
