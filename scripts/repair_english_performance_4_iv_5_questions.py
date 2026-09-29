import json
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
OUT = ROOT / "questions" / "english"
LESSON = "lesson-english-performance-4-iv-5"
KG = "kg-english-performance-4-iv-5"
SOURCES = [
    {
        "url": "https://www.sdjh.ntpc.edu.tw/app/index.php?Action=downloadfile&cg=837&file=WVhSMFlXTm9Mek15TDNCMFlWOHpOVEUxWHpZM09ETTRPREpmT1RNME9UWXVjR1Jt&fname=WW54RPOKRK4411HH50LKKPHG1430WT24KLB0XSXSTXA1LK40NKROSTB4WW54A0OKWW5400HHA404LK14MOPKTSLOOPB0QLYWXTYTXWA0SWZWCDVWSSOKXSFCUS00HH25DGA0DCZWFCMO40201434ZWMKUTGDUT21SSUSJGB0GGA401USTWLKUXJHGG04DC14MKB4JDIGKLEG35WWMLXTPOFCSSRO54SWUSDCROFCNOXW41KKWW04DHHG",
        "title": "新北市立三多國中113學年度第1學期第2次段考七年級英文科試題",
        "year": "113-1",
        "locator": "PDF第6頁第52至55題：依提示將祈使句改否定、依句中成分造原問句；本題只取句型轉換能力。",
        "observedPattern": "提示作答需辨認句子功能與指定資訊，再調整助動詞、詞序或否定形式；本題另用全新語料與答案。",
    },
    {
        "url": "https://w3.hkjh.kh.edu.tw/%E5%B0%8F%E6%B8%AF%E5%9C%8B%E4%B8%AD%E6%AE%B5%E8%80%83%E8%A9%A6%E9%A1%8C/21%E4%BA%8C%E5%B9%B4%E7%B4%9A%E4%B8%8A%E5%AD%B8%E6%9C%9F/1%E7%AC%AC%E4%B8%80%E6%AC%A1%E6%AE%B5%E8%80%83%E8%A9%A6%E9%A1%8C/%E8%8B%B1%E8%AA%9E/108-1-1%E4%BA%8C%E5%B9%B4%E7%B4%9A%E8%8B%B1%E6%96%87%E7%A7%91%E8%A9%A6%E9%A1%8C.pdf",
        "title": "高雄市立小港國中108學年度第1學期第1次段考八年級英文科試題",
        "year": "108-1",
        "locator": "PDF第2頁第30至32題：從四個句子中辨識語序、動詞搭配及時間表達正確者。",
        "observedPattern": "正確句判讀要同時檢查詞序、主動詞形式與時間語意；本題使用新人物、事件及詞彙。",
    },
    {
        "url": "https://www.dwm.kh.edu.tw/upload/344/104_64184/112%E5%AD%B8%E5%B9%B4%E5%BA%A6%E7%AC%AC%E4%B8%80%E5%AD%B8%E6%9C%9F%E7%AC%AC%E4%B8%89%E6%AC%A1%E6%AE%B5%E8%80%83%E8%8B%B1%E6%96%87%E4%B8%80%E5%B9%B4%E7%B4%9A%E8%A9%A6%E9%A1%8C.pdf",
        "title": "高雄市立大灣國中112學年度第1學期第3次段考一年級英文科試題",
        "year": "112-1",
        "locator": "PDF第2頁第26至28題：比較請求／命令、現在進行式與否定祈使等正確句型。",
        "observedPattern": "依句意判斷祈使、否定祈使及進行動作，再核對動詞型態與句子完整性；本題情境和措辭為原創。",
    },
]


def refs():
    return [
        {
            **source,
            "subject": "english",
            "reuseDecision": "pattern-only",
            "status": "recorded",
            "locatorLevel": "item",
        }
        for source in SOURCES
    ]


ITEMS = [
    {
        "prompt": "提示：Lina / practice the violin / every Friday. Choose the sentence that keeps the habitual time clue and correct verb form.",
        "options": {"A": "Lina practices the violin every Friday.", "B": "Lina practice the violin every Friday.", "C": "Every Friday practices Lina the violin.", "D": "Lina is practice the violin every Friday."},
        "answer": "A",
        "explanation": "Every Friday marks a repeated habit, so use the simple present. Lina is one person, so practice takes -s; the object follows the verb and the time phrase can close the sentence.",
        "strategy": "把頻率／時間線索和主詞一起判斷：先定現在習慣，再檢查第三人稱單數動詞，最後核對受詞位置。",
        "steps": ["從提示中找時間線索 every Friday，判斷這是規律習慣。", "確認主詞 Lina 是第三人稱單數。", "把 practice 改為 practices，因為現在簡單式單數主詞要加 -s。", "按主詞＋動詞＋受詞＋時間的順序組句。", "選 A；B 少了動詞字尾，C 詞序錯，D 的 is 後不能直接接原形 practice。"],
    },
    {
        "prompt": "提示：The two cooks / not / use plastic cups / at work. Which sentence expresses their usual practice correctly?",
        "options": {"A": "The two cooks does not use plastic cups at work.", "B": "The two cooks do not use plastic cups at work.", "C": "The two cooks do not uses plastic cups at work.", "D": "The two cooks not use plastic cups at work."},
        "answer": "B",
        "explanation": "The two cooks is plural, so simple-present negation uses do not. The auxiliary carries tense and number, leaving the main verb in its base form use.",
        "strategy": "否定句先選 do／does，再讓主要動詞維持原形；主詞是複數 cooks，因此用 do。",
        "steps": ["讀提示中的 not，確認要組現在簡單式否定句。", "找主詞 the two cooks，two 表示複數。", "複數主詞搭配 do not，而不是 does not。", "do 已承擔時態，主要動詞使用原形 use。", "選 B；A 助動詞不合主詞，C 多加 -s，D 缺少否定助動詞。"],
    },
    {
        "prompt": "提示：please / leave / your bicycle / beside the blue rack. Choose the polite instruction with correct word order.",
        "options": {"A": "Please leaves your bicycle beside the blue rack.", "B": "Please to leave your bicycle beside the blue rack.", "C": "Please leave your bicycle beside the blue rack.", "D": "Please are leaving your bicycle beside the blue rack."},
        "answer": "C",
        "explanation": "A polite imperative may begin with Please, followed by the base verb leave, its object, and the location phrase. Imperatives address the listener, so no subject is needed.",
        "strategy": "辨認 please 開頭的禮貌指示：Please＋原形動詞，接受詞與地點，不加第三人稱字尾或 be 動詞。",
        "steps": ["看到 please，判斷句子是在禮貌地指示對方做事。", "祈使句省略 you，動詞直接用原形 leave。", "把受詞 your bicycle 放在動詞後。", "把地點 beside the blue rack 放在受詞後。", "選 C；A 的 leaves、B 的 to leave、D 的 are leaving 都不符合此祈使句骨架。"],
    },
    {
        "prompt": "提示：where / your aunt / buy / fresh bread? Choose the correctly formed present-simple question.",
        "options": {"A": "Where your aunt does buy fresh bread?", "B": "Where do your aunt buys fresh bread?", "C": "Where is your aunt buy fresh bread?", "D": "Where does your aunt buy fresh bread?"},
        "answer": "D",
        "explanation": "Your aunt is singular, so the present-simple wh-question uses does before the subject. After does, buy stays in the base form; where asks for the place.",
        "strategy": "疑問詞問地點時，依序組成 Where＋does＋單數主詞＋原形動詞；助動詞已帶第三人稱形式。",
        "steps": ["由 where 判斷問題要詢問地點，答案應是某個地方。", "主詞 your aunt 是單數，選助動詞 does。", "將 does 放在主詞前：Where does your aunt…?", "does 後接原形 buy，不加 -s，也不另加 is。", "選 D；確認 where、does、主詞和原形 buy 的詞序正確，最後使用問號。"],
    },
    {
        "prompt": "提示：Last night / Omar / take / the earlier train. Which sentence reports the completed past event correctly?",
        "options": {"A": "Omar takes the earlier train last night.", "B": "Omar took the earlier train last night.", "C": "Omar did took the earlier train last night.", "D": "Last night Omar taking the earlier train."},
        "answer": "B",
        "explanation": "Last night places the event in the past. Take has the irregular past form took; a positive past statement does not add did before that past-tense verb.",
        "strategy": "先用明確過去時間定時態，再查不規則動詞；肯定句只保留 took，不和 did 疊用。",
        "steps": ["圈出 Last night，確定事件已在過去完成。", "找出主要動詞 take，辨認它是不規則變化。", "將 take 改成過去式 took。", "依主詞 Omar＋動詞＋受詞＋時間完成句子。", "選 B；A 是現在式，C 重複標記過去，D 缺少有限動詞。"],
    },
    {
        "prompt": "提示：Look! / the children / build / a paper bridge / now. Choose the sentence that describes the action in progress.",
        "options": {"A": "The children are building a paper bridge now.", "B": "The children is building a paper bridge now.", "C": "The children building are a paper bridge now.", "D": "The children build a paper bridge now."},
        "answer": "A",
        "explanation": "Look! and now point to an action happening at this moment. The plural subject children takes are, followed by the -ing form building.",
        "strategy": "看到 Look!／now，先判斷此刻正在發生，再用 be＋V-ing；be 動詞依複數主詞選 are。",
        "steps": ["從 Look! 和 now 找到「正在發生」的時間訊號。", "把動作 build 改成 building。", "確認 children 是複數，搭配 are。", "按主詞＋are＋V-ing＋受詞＋時間排列。", "選 A；B 主詞與 be 不一致，C 詞序錯，D 沒有表現進行中的形式。"],
    },
    {
        "prompt": "提示：Maya / can / carry / both boxes. Which sentence uses the modal correctly?",
        "options": {"A": "Maya cans carry both boxes.", "B": "Maya can carries both boxes.", "C": "Maya can carry both boxes.", "D": "Maya can to carry both boxes."},
        "answer": "C",
        "explanation": "Can is a modal auxiliary and is followed directly by the base verb carry. It does not take -s for Maya and does not require to.",
        "strategy": "情態助動詞後面直接放原形動詞；不要依單數主詞替 can 或 carry 加字尾，也不要插入 to。",
        "steps": ["從提示辨認情態助動詞 can。", "can 後面要接原形 carry。", "即使主詞 Maya 是單數，can 不加 -s。", "把受詞 both boxes 接在 carry 後。", "選 C；A 把 -s 加錯位置，B 動詞變化錯，D 多了 to。"],
    },
    {
        "prompt": "提示：The team stayed indoors / because / heavy rain / block the trail. Which sentence gives the reason with correct clause structure?",
        "options": {"A": "The team because heavy rain blocked the trail stayed indoors.", "B": "The team stayed indoors because heavy rain blocked the trail.", "C": "Because the team stayed indoors heavy rain blocked the trail.", "D": "The team stayed indoors because blocked heavy rain the trail."},
        "answer": "B",
        "explanation": "The main clause states the result, and because introduces the reason clause. In that clause, heavy rain is the subject and blocked is its past-tense verb.",
        "strategy": "先分出結果與原因，再讓 because 緊接完整原因子句；每個子句都要保留主詞和正確動詞。",
        "steps": ["把 stayed indoors 標成結果，把 heavy rain… 標成原因。", "用 because 引入原因子句，放在結果句之後。", "在原因子句中讓 heavy rain 作主詞、blocked 作過去式動詞。", "逐句檢查主詞與動詞相連，並確認 trail 是 blocked 的受詞。", "選 B；其他選項把子句切開、顛倒因果或打亂原因子句詞序。"],
    },
    {
        "prompt": "提示：There / two empty seats / near the window. Which sentence correctly introduces the seats?",
        "options": {"A": "There is two empty seats near the window.", "B": "There two empty seats are near the window.", "C": "There are an empty seats near the window.", "D": "There are two empty seats near the window."},
        "answer": "D",
        "explanation": "The noun phrase two empty seats is plural, so the existential sentence begins There are. The location phrase then tells where the seats are.",
        "strategy": "There be 句型要看 be 後面的真正名詞主語；two seats 是複數，因此使用 are。",
        "steps": ["先找 There 後面的名詞核心 seats。", "two 表示 seats 為複數。", "複數名詞前選 are，而非 is。", "將完整名詞片語 two empty seats 放在 are 後，再加地點。", "選 D；A 主動詞單複數錯，B 詞序錯，C 的 an 與複數名詞衝突。"],
    },
    {
        "prompt": "提示：Let’s / not / post the class photo / until everyone agrees. Choose the sentence that makes the suggestion negative without changing its meaning.",
        "options": {"A": "Let’s not post the class photo until everyone agrees.", "B": "Let’s don’t post the class photo until everyone agrees.", "C": "Let’s not posts the class photo until everyone agrees.", "D": "Let not’s post the class photo until everyone agrees."},
        "answer": "A",
        "explanation": "A negative suggestion with let’s places not after let’s and before the base verb: Let’s not post. Until everyone agrees remains the time condition and does not alter the main verb form.",
        "strategy": "let’s 的否定位置固定在 let’s 後、原形動詞前；保留後面的 until 子句作為行動條件。",
        "steps": ["先辨認提示 Let’s，判斷這是邀請／共同提議。", "把否定詞 not 放在 let’s 後面。", "not 後使用原形 post，不加助動詞 do 或 -s。", "將 until everyone agrees 留在句尾，表達同意前先不張貼。", "選 A；B 多加 don’t，C 動詞型態錯，D 把 let’s 拆錯。"],
    },
]

for index, item in enumerate(ITEMS, start=1):
    item_id = f"question-english-performance-4-iv-5-{index}"
    source = SOURCES[(index - 1) % len(SOURCES)]
    question = {
        "id": item_id,
        "subject": "english",
        "type": "single-choice",
        "prompt": item["prompt"],
        "options": [{"id": key, "text": value} for key, value in item["options"].items()],
        "knowledgeIds": [KG],
        "difficulty": "medium" if index in {2, 4, 5, 8, 10} else "easy",
        "answer": {"value": item["answer"], "explanation": item["explanation"]},
        "provenance": {
            "origin": "original",
            "license": "All rights reserved",
            "sourceUrl": source["url"],
            "sourceLocator": source["locator"],
            "authoringNote": "依官方課綱知識節點及三所公立國中公開英文評量呈現的提示組句、句型轉換與正確句判讀能力方向自行創作；未複製原卷內容。完整教材與授權界線仍待審查。",
        },
        "reviewStatus": "draft",
        "updatedAt": "2026-09-26",
        "lessonId": LESSON,
        "examPatternRefs": refs(),
        "solutionStrategy": item["strategy"],
        "solutionSteps": item["steps"],
    }
    (OUT / f"{item_id}.json").write_text(json.dumps(question, ensure_ascii=False, indent=2) + "\n")

print(json.dumps({"rewritten": len(ITEMS), "unit": LESSON, "draftPreserved": True}, ensure_ascii=False))
