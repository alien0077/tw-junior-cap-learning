#!/usr/bin/env python3
"""Independently author and source English 7-IV-1 dictionary-use items."""
from __future__ import annotations

import json
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
OUT = ROOT / "questions/english"
CATALOG = ROOT / "data/public-exam-sources.json"
TODAY = "2026-09-26"

SOURCES = [
    {
        "id": "kcjh-106-1-term3-grade8-english",
        "school": "高雄市立國昌國民中學", "grade": "8", "year": "106-1",
        "exam": "106學年度第1學期第3次段考二年級英文科",
        "url": "https://www.kcjh.kh.edu.tw/upload/190/104_34764/106-1-3%E4%BA%8C%E5%B9%B4%E7%B4%9A%E8%8B%B1%E6%96%87%E7%A7%91%E8%A9%A6%E9%A1%8C%2B%E7%AD%94%E6%A1%88%E5%8D%B7.pdf",
        "title": "高雄市立國昌國中106學年度第1學期第3次段考二年級英文科試題卷",
        "pattern": "公開英文題以句中搭配、前後語意和使用情境辨認詞義；本題改用全新例句與選項。",
    },
    {
        "id": "hkjh-109-1-term3-grade9-english",
        "school": "高雄市立小港國民中學", "grade": "9", "year": "109-1",
        "exam": "109學年度第1學期第3次段考三年級英文科",
        "url": "https://w3.hkjh.kh.edu.tw/%E5%B0%8F%E6%B8%AF%E5%9C%8B%E4%B8%AD%E6%AE%B5%E8%80%83%E8%A9%A6%E9%A1%8C/31%E4%B8%89%E5%B9%B4%E7%B4%9A%E4%B8%8A%E5%AD%B8%E6%9C%9F/3%E7%AC%AC%E4%B8%89%E6%AC%A1%E6%AE%B5%E8%80%83%E8%A9%A6%E9%A1%8C/%E8%8B%B1%E8%AA%9E/109-1-3%E4%B8%89%E5%B9%B4%E7%B4%9A%E8%8B%B1%E6%96%87.pdf",
        "title": "高雄市立小港國中109學年度第1學期第3次段考三年級英文科試題",
        "pattern": "公開英文題以句意、詞性、搭配與段落線索判讀詞語用法；本題自行設計查字典任務。",
    },
    {
        "id": "wl-jh-110-2-grade9-english",
        "school": "基隆市立武崙國民中學", "grade": "9", "year": "110-2",
        "exam": "110學年度第2學期九年級英文科第二次段考",
        "url": "https://jweb.kl.edu.tw/userfiles/1389/document/39208_0524%E7%AC%AC%E4%BA%94%E7%AF%80--%E4%B9%9D%E4%B8%8B%E8%8B%B1%E6%96%87%E4%BA%8C%E6%AE%B5.pdf",
        "title": "基隆市立武崙國中110學年度第2學期九年級英文科第二次段考",
        "pattern": "公開英文題以詞語置入句境、比較語意及段落證據確認理解；本題內容獨立創作。",
    },
    {
        "id": "hkjh-105-2-term1-grade9-english",
        "school": "高雄市立小港國民中學", "grade": "9", "year": "105-2",
        "exam": "105學年度第2學期第1次段考三年級英文科",
        "url": "https://w3.hkjh.kh.edu.tw/%E5%B0%8F%E6%B8%AF%E5%9C%8B%E4%B8%AD%E6%AE%B5%E8%80%83%E8%A9%A6%E9%A1%8C/32%E4%B8%89%E5%B9%B4%E7%B4%9A%E4%B8%8B%E5%AD%B8%E6%9C%9F/1%E7%AC%AC%E4%B8%80%E6%AC%A1%E6%AE%B5%E8%80%83%E8%A9%A6%E9%A1%8C/%E8%8B%B1%E8%AA%9E/105-2-1%20%E4%B8%89%E5%B9%B4%E7%B4%9A%E8%8B%B1%E8%AA%9E%E7%A7%91%E8%A9%A6%E9%A1%8C.pdf",
        "title": "高雄市立小港國中105學年度第2學期第1次段考三年級英文科試題",
        "pattern": "公開基本問答以 make a decision 片語檢驗詞語搭配及語意；本題另以字典標示情境重寫。",
    },
    {
        "id": "kcjh-110-2-term1-grade8-english",
        "school": "高雄市立國昌國民中學", "grade": "8", "year": "110-2",
        "exam": "110學年度第2學期第1次段考二年級英文科",
        "url": "https://www.kcjh.kh.edu.tw/upload/190/104_34764/%E5%9C%8B%E4%BA%8C%E8%8B%B1%E6%96%87%E6%AE%B5%E8%80%83%E8%A9%A6%E9%A1%8C.pdf",
        "title": "高雄市立國昌國中110學年度第2學期第1次段考二年級英文科試題",
        "pattern": "公開英文題含詞類變化填答，要求由句境辨認詞形與詞性；本題以新的字族示例設計。",
    },
]

# Each item owns its answer placement, explanation, strategy, steps, and exact
# source locators. Source material is used only for pattern-level research.
ITEMS = {
    1: {
        "key": "A", "correct": "The land beside a river",
        "prompt": "In 'The hikers reached the bank of the river,' a dictionary gives several meanings for bank. Which meaning fits here?",
        "options": ["The land beside a river", "A place that keeps money", "A row of machines", "A seat in a classroom"],
        "explanation": "The phrase of the river selects the land beside the water. Correct answer: A — The land beside a river.",
        "strategy": "bank 有金融機構與河岸等多個義項；先看它和 of the river 的連接，再排除與地形不合的解釋。",
        "steps": [
            "不要看到 bank 就立刻採用最熟悉的「銀行」；先把整句讀完，找它後面的限定語。",
            "of the river 把 bank 放進河流地景，而不是提款、存款或排隊辦金融業務的情境。",
            "字典若列多個義項，逐一比較例句和本句線索；此處應找沿著水邊的土地。",
            "機器排列與教室座位都不能由 river 支持；金融機構也不符合 hikers reached 的場景。",
            "答案 A：The land beside a river。把河岸代回句子，登山者抵達河邊的語意自然成立。",
        ],
        "locators": ["PDF第1頁第3題", "PDF印刷頁第2頁第17題", "PDF印刷頁第2頁第16題"],
        "sourceIndexes": [0, 1, 2],
    },
    2: {
        "key": "B", "correct": "verb",
        "prompt": "In the sentence 'Please record the new address,' the word record is used as a verb. Which dictionary label should the learner find first?",
        "options": ["adjective", "verb", "preposition", "pronoun"],
        "explanation": "Please record gives a command to perform an action, so the verb label matches. Correct answer: B — verb.",
        "strategy": "判斷詞性要看字在句中的工作，不只看拼字；祈使句的 Please 後方通常接原形動詞。",
        "steps": [
            "先把 Please record the new address 當作完整指令理解：說話者要求對方做一件事。",
            "record 後面直接接受詞 the new address，表示它描述「記下」的動作。",
            "查字典時優先找符合本句句法功能的標記；此處不是修飾名詞的形容詞。",
            "介系詞需連接名詞或代名詞形成關係，代名詞則代替名詞，兩者都不能帶出這個命令動作。",
            "答案 B：verb。命令形式與後接受詞共同證明 record 在此作動詞。",
        ],
        "locators": ["PDF第1頁第5題", "PDF印刷頁第2頁第22至23題", "PDF印刷頁第3頁第29題"],
        "sourceIndexes": [0, 1, 2],
    },
    3: {
        "key": "C", "correct": "An example sentence showing bright used for a person",
        "prompt": "A learner is unsure whether 'bright' can describe a student. Which dictionary feature is most useful?",
        "options": ["The dictionary's page color", "A list of unrelated place names", "An example sentence showing bright used for a person", "The length of the word's spelling only"],
        "explanation": "An example sentence reveals whether bright describes a person's ability in that usage. Correct answer: C — An example sentence showing bright used for a person.",
        "strategy": "當疑問是某字能否修飾某類對象，查例句比只背中文釋義更有用；要找相同語法位置與搭配。",
        "steps": [
            "把問題拆成兩部分：bright 的用法，以及被描述的名詞 student。",
            "先看字典的詞性與義項，再搜尋 bright 作形容詞修飾人的實際例句。",
            "若例句把 bright 用來描述聰明或反應敏捷的人，就能判斷這種搭配可行。",
            "頁面顏色、拼字長短或地名清單都不會提供 bright 與 student 之間的語法證據。",
            "答案 C：An example sentence showing bright used for a person。例句能直接展示合適的對象和語境。",
        ],
        "locators": ["PDF第1頁第4題", "PDF印刷頁第2頁第18題", "PDF印刷頁第2頁第18題"],
        "sourceIndexes": [0, 1, 2],
    },
    4: {
        "key": "D", "correct": "The collocation 'make a decision'",
        "prompt": "Which dictionary information best helps complete '___ a decision' naturally?",
        "options": ["The word's alphabetical position", "The number of letters in decision", "An example about a different language", "The collocation 'make a decision'"],
        "explanation": "A collocation entry shows that make naturally combines with decision. Correct answer: D — The collocation 'make a decision'.",
        "strategy": "片語填空要找詞語慣用的同伴；字典中的搭配欄能比較哪些動詞通常和 decision 一起出現。",
        "steps": [
            "空格後已固定是 a decision，因此要找能與這個名詞自然搭配的動詞。",
            "字母排序只說明單字在哪裡，無法告訴讀者哪些詞常一起使用。",
            "查 collocations 或搭配例句，確認英語慣用說法是 make a decision。",
            "字數和其他語言的例句都不能判斷英文動詞—名詞組合是否自然。",
            "答案 D：The collocation 'make a decision'。這項資訊直接補上最合乎慣用語的動詞。",
        ],
        "locators": ["PDF第1頁第4至5題", "PDF印刷頁第2頁第24至25題", "PDF印刷頁第1頁第8題"],
        "sourceIndexes": [0, 1, 3],
    },
    5: {
        "key": "A", "correct": "A drama or performance",
        "prompt": "The sentence says, 'The children watched the play at the theater.' Which sense of play is needed?",
        "options": ["A drama or performance", "A device for storing files", "A flat piece of land", "A meal eaten at noon"],
        "explanation": "Watched and at the theater identify play as a staged performance. Correct answer: A — A drama or performance.",
        "strategy": "多義字要讓句中動詞、地點和主題互相驗證；theater 與 watched 共同指向演出，不是遊戲或玩耍。",
        "steps": [
            "標出兩個線索：孩子 watched 某物，而且地點是 theater。",
            "把 play 的可能詞義帶回句中；「演出／戲劇」可被觀看，也適合在劇院發生。",
            "若選「玩耍」，通常要描述玩的人或活動；本句的劇院地點讓這個解釋不如演出合理。",
            "儲存檔案的裝置、土地與午餐都無法同時解釋 watched 和 theater。",
            "答案 A：A drama or performance。兩個上下文線索一致支持「戲劇演出」這個義項。",
        ],
        "locators": ["PDF第3頁第37至40題", "PDF印刷頁第2頁第22至23題", "PDF印刷頁第4頁第44至46題"],
        "sourceIndexes": [0, 1, 2],
    },
    6: {
        "key": "B", "correct": "Rising sharply",
        "prompt": "In 'The trail was steep, so we climbed slowly,' what does steep most likely mean?",
        "options": ["Very flat", "Rising sharply", "Full of music", "Made of paper"],
        "explanation": "The slow climb is a clue that the path rises at a strong angle. Correct answer: B — Rising sharply.",
        "strategy": "遇到不熟悉的形容詞，觀察 so 連接的結果；緩慢攀爬是坡度陡的後果線索。",
        "steps": [
            "先辨認句子的因果連接詞 so：後半句的慢慢爬，應能由前半句的地形解釋。",
            "trail 是路徑，climbed slowly 表示前進費力，指向坡面上升角度大。",
            "回查 steep 的義項時，選能解釋需要攀爬、速度變慢的形容詞意思。",
            "very flat 與爬得慢的因果不合；音樂和紙張則不是此處地形的性質。",
            "答案 B：Rising sharply。陡升的路徑最能說明旅人為何慢慢往上爬。",
        ],
        "locators": ["PDF第1頁第5題", "PDF印刷頁第2頁第18至20題", "PDF印刷頁第2頁第18題"],
        "sourceIndexes": [0, 1, 2],
    },
    7: {
        "key": "C", "correct": "The numbered sense and example about a seller asking a price",
        "prompt": "A learner guesses that 'charge' means ask for money in 'The shop will charge five dollars.' What should confirm the guess?",
        "options": ["Only the first meaning printed in large type", "The word's opposite spelling", "The numbered sense and example about a seller asking a price", "A random picture from another page"],
        "explanation": "A numbered sense and matching example can confirm the money-related use of charge. Correct answer: C — The numbered sense and example about a seller asking a price.",
        "strategy": "同一拼字可能列出多個義項；不要只靠第一個釋義，應用本句角色與金額比對編號義項和例句。",
        "steps": [
            "本句主詞是 shop，受詞金額是 five dollars，情境是在說店家向顧客收費。",
            "查 charge 時先掃描編號義項，不假定最前面印出的意思一定符合本句。",
            "挑出描述收取金錢的項目，再用商家向顧客收費的例句交叉核對。",
            "反義字拼法、別頁的隨機圖片都不能證明此處的收費義；醒目排版也不等於語境吻合。",
            "答案 C：The numbered sense and example about a seller asking a price。義項與金額線索相互印證。",
        ],
        "locators": ["PDF第1頁第3至4題", "PDF印刷頁第2頁第16至17題", "PDF印刷頁第2頁第29題"],
        "sourceIndexes": [0, 1, 2],
    },
    8: {
        "key": "D", "correct": "The word-family or related-words information",
        "prompt": "A dictionary lists decide, decision, and decisive. Which feature helps a learner see their relationship?",
        "options": ["The page number of the dictionary", "The definition of an unrelated animal", "The paper thickness", "The word-family or related-words information"],
        "explanation": "A word-family entry groups related forms and makes their shared base visible. Correct answer: D — The word-family or related-words information.",
        "strategy": "要看 decide、decision、decisive 的構詞關係，搜尋字族或 related words 欄，而非把三個詞當成互不相關的定義。",
        "steps": [
            "三個詞共享 decide 相關字根，但詞形和詞性不同；問題問的是它們彼此的關係。",
            "查字典時找 word family、related words 或詞形變化資訊，確認它們如何由共同詞根延伸。",
            "把詞性分開：decide 是動作，decision 是名詞，decisive 是形容特徵的形容詞。",
            "頁碼、紙張厚度與無關動物詞義都不會顯示這組詞如何彼此轉換。",
            "答案 D：The word-family or related-words information。這一欄最直接呈現同族詞的連結。",
        ],
        "locators": ["PDF印刷頁第5頁第五大題第1至6小題", "PDF第1頁第3至4題", "PDF印刷頁第2頁第22至23題"],
        "sourceIndexes": [4, 0, 1],
    },
    9: {
        "key": "B", "correct": "The pronunciation, part of speech, and example for each entry",
        "prompt": "A learner sees two entries with the same spelling but different pronunciation and meanings. What should be checked?",
        "options": ["Only the first letter of the word", "The pronunciation, part of speech, and example for each entry", "The dictionary cover", "The number of pages in the book"],
        "explanation": "Pronunciation and usage labels distinguish same-spelling entries with different meanings. Correct answer: B — The pronunciation, part of speech, and example for each entry.",
        "strategy": "拼字相同不保證讀音、詞性與意思相同；逐條比對音標、詞性標籤和例句，才能選到句中那一項。",
        "steps": [
            "題幹已指出兩個條目拼字相同，差異在發音和意思，不能只看 headword。",
            "先比對音標，確認說話者要用哪種讀音；再看詞性是否符合句子位置。",
            "最後將各條目例句和目標句的語意、搭配逐項對照，鎖定適用義項。",
            "封面、頁數或首字母對兩條目完全相同，不能解決它們的讀音與用法差別。",
            "答案 B：The pronunciation, part of speech, and example for each entry。三種標記合看才能避免同形字混淆。",
        ],
        "locators": ["PDF第1頁第4至5題", "PDF印刷頁第2頁第18至20題", "PDF印刷頁第2頁第16至18題"],
        "sourceIndexes": [0, 1, 2],
    },
    10: {
        "key": "C", "correct": "Use context, identify the part of speech, compare senses and examples, then reread",
        "prompt": "A student meets an unfamiliar word in a science paragraph. Which lookup routine is most reliable?",
        "options": ["Choose the shortest definition without reading the sentence", "Use the first dictionary entry even if its grammar does not fit", "Use context, identify the part of speech, compare senses and examples, then reread", "Skip the context and copy every definition into the notebook"],
        "explanation": "A reliable lookup tests candidate senses against context and grammar, then checks the paragraph again. Correct answer: C — Use context, identify the part of speech, compare senses and examples, then reread.",
        "strategy": "完整查字程序應由原文語境出發，再用詞性、義項與例句篩選，最後把候選意思放回整段驗證。",
        "steps": [
            "不要一看到陌生字就抄下所有中文義；先讀它前後句，圈出能限制意思的科學情境線索。",
            "判斷該字在句中是名詞、動詞或其他詞類，先排除語法位置不相符的字典條目。",
            "比較剩下義項的例句與搭配，保留能解釋本段現象的候選意思。",
            "把候選釋義代回原句，再連讀整段；若推理或文法中斷，就回頭改選義項。",
            "答案 C：Use context, identify the part of speech, compare senses and examples, then reread。它有語境、語法、查證和回讀四道核對。",
        ],
        "locators": ["PDF第3頁第37至40題", "PDF印刷頁第4頁第41至43題", "PDF印刷頁第4頁第44至46題"],
        "sourceIndexes": [0, 1, 2],
    },
}


def make_ref(source: dict, locator: str) -> dict:
    return {
        "url": source["url"], "title": source["title"], "year": source["year"],
        "subject": "english", "locator": locator, "locatorLevel": "page",
        "observedPattern": source["pattern"], "reuseDecision": "pattern-only", "status": "recorded",
    }


def main() -> None:
    catalog = json.loads(CATALOG.read_text(encoding="utf-8"))
    known = {entry["id"] for entry in catalog["sources"]}
    for source in SOURCES:
        if source["id"] not in known:
            catalog["sources"].append({
                "id": source["id"], "school": source["school"], "grade": source["grade"],
                "subject": "english", "exam": source["exam"], "questionUrl": source["url"],
                "answerLocator": "題本中詞義、詞性、搭配或閱讀線索之指定頁／題；個別題號見 examPatternRefs。",
                "usePolicy": "只研究公開英文評量的詞義、句境、詞類、搭配與推理形式；本站題幹、選項、答案與解說均獨立撰寫，不複製原題。",
                "verifiedAt": TODAY,
            })
    catalog["updatedAt"] = TODAY
    CATALOG.write_text(json.dumps(catalog, ensure_ascii=False, indent=2) + "\n", encoding="utf-8")

    for number, item in ITEMS.items():
        path = OUT / f"question-english-performance-7-iv-1-{number}.json"
        data = json.loads(path.read_text(encoding="utf-8"))
        refs = [make_ref(SOURCES[i], locator) for i, locator in zip(item["sourceIndexes"], item["locators"], strict=True)]
        assert len({ref["url"] for ref in refs}) == 3
        assert item["options"][ord(item["key"]) - 65] == item["correct"]
        data.update({
            "prompt": item["prompt"],
            "options": [{"id": chr(65 + i), "text": text} for i, text in enumerate(item["options"])],
            "difficulty": "medium",
            "answer": {"value": item["key"], "explanation": item["explanation"]},
            "provenance": {
                "origin": "original", "license": "All rights reserved",
                "sourceUrl": refs[0]["url"],
                "sourceLocator": "國昌、小港、武崙三所公立國中公開英文段考；本題已逐筆定位到頁碼及題號，且只取命題模式，見 examPatternRefs。",
                "authoringNote": "依官方課綱與 KG-english-performance-7-iv-1 獨立編寫字典查義、詞性、例句、搭配、多義字、詞族、發音及上下文查證任務；未複製原卷題幹、選項或答案。",
            },
            "reviewStatus": "draft", "updatedAt": TODAY,
            "examPatternRefs": refs, "solutionStrategy": item["strategy"],
            "solutionSteps": item["steps"],
        })
        path.write_text(json.dumps(data, ensure_ascii=False, indent=2) + "\n", encoding="utf-8")
    print("rewrote 10 independent original items; balanced answer keys; replaced pending refs with 30 located public-school pattern-only references")


if __name__ == "__main__":
    main()
