import json
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
OUT = ROOT / "questions/chinese"
SOURCES = [
    ("https://www.sdjh.ntpc.edu.tw/var/file/0/1000/attach/16/pta_2229_1166226_19803.pdf", "新北市立石碇國中公開國文試題", "文言詞義與語詞結構"),
    ("https://www.yacjh.kh.edu.tw/upload/221/101_30637/114%E4%B8%8B%E5%AD%B8%E6%9C%9F%E7%AC%AC%E4%B8%80%E6%AC%A1%E6%AE%B5%E8%80%83%E4%B8%89%E5%B9%B4%E7%B4%9A%E5%9C%8B%E6%96%87.pdf", "高雄市立鹽埕國中公開國文段考", "文言閱讀與語意判讀"),
    ("https://www.jlsh.mlc.edu.tw/var/file/12/1012/img/113-2-7-4.pdf", "國立卓蘭高中附設國中部公開課程與試題資料", "古典語文與句法分析"),
]
DATA = [
    ("之", "『學而時習之，不亦說乎』中的『之』，最接近下列哪一句的用法？", ["擇其善者而從之", "水陸草木之花", "何陋之有", "久之，目似瞑"], "擇其善者而從之", "兩句的『之』都作代詞，指前面提到的學習內容或善者，作為動詞的對象。"),
    ("其", "『其人捨然大喜』中的『其』，最接近哪個意思？", ["那個、那位", "難道", "大概", "自己"], "那個、那位", "『其人』是指那個人，『其』作指示代詞；不能只因常見義項而固定翻成大概或難道。"),
    ("詞義轉換", "『先天下之憂而憂』中的『先』，在句中最適合解作？", ["把天下人的憂患放在自己之前", "先前曾經", "首先出生", "領先取得物品"], "把天下人的憂患放在自己之前", "此處『先』由時間順序轉為意動或次序上的優先，須配合『憂而憂』的語境理解。"),
    ("偏正結構", "下列哪一組最適合判定為偏正結構，前字修飾後字？", ["高山", "山高", "讀書", "國家"], "高山", "『高山』中『高』修飾『山』；『山高』較接近主謂，『讀書』是動賓。"),
    ("動賓結構", "下列哪一組屬於動賓結構？", ["觀魚", "甚善", "白日", "國事"], "觀魚", "『觀魚』可分成動詞『觀』與受詞『魚』；其餘各組分別偏向主謂或偏正。"),
    ("主謂結構", "『水落石出』若依語詞結構分析，較接近哪一種關係？", ["主謂：水落、石出各自形成主謂關係", "動賓：水是動作，落是受詞", "偏正：水修飾落", "介賓：石是介詞"], "主謂：水落、石出各自形成主謂關係", "『水落』是水作主語、落作謂語；『石出』同理，不能只看兩字相鄰就套偏正。"),
    ("古今義", "『可以無饑矣』中的『可以』，依文言語境應理解為？", ["可以憑藉這個、能夠因此", "表示讚美的形容詞", "現代口語的同意回答", "可愛而且美麗"], "可以憑藉這個、能夠因此", "文言『可以』常可拆為『可』與『以』，表示可以憑藉或能夠；不能直接套現代固定詞義。"),
    ("詞性判斷", "『朝服衣冠』中的第一個『服』，依句意最適合判定為？", ["名詞作動詞，穿戴朝服", "形容詞，表示服裝漂亮", "代詞，指某個人", "語氣詞，表示感嘆"], "名詞作動詞，穿戴朝服", "『服』在此與衣冠搭配，作穿戴解；文言常有名詞活用為動詞的現象，需回到句意確認。"),
    ("結構與語境", "若只看到『明日』兩字，沒有上下文，最妥當的做法是？", ["先以『明天』等常見義項提出暫解，再查上下文確認詞性與句中功能", "不論句子都固定翻成光明的日子", "直接判定為動賓結構", "只看字形就能確定它一定是時間名詞"], "先以『明天』等常見義項提出暫解，再查上下文確認詞性與句中功能", "文言字詞可能有多義與活用；沒有上下文時應保留暫定，不可把猜測當成唯一解釋。"),
    ("資料界線", "同一個『故』字在兩個句子中分別可能表示原因或故意；要判斷正確義項，最需要哪項證據？", ["完整句子的前後文、搭配與人物行動", "只看『故』字的筆畫數", "只看現代成語中最常見的意思", "不需要句子，直接選固定翻譯"], "完整句子的前後文、搭配與人物行動", "多義文言詞必須以語境、搭配與句法功能判讀，單字本身不足以決定義項。"),
]

def make_question(index, row):
    tag, prompt, options, answer, explanation = row
    opts = [{"id": chr(65 + i), "text": t} for i, t in enumerate(options)]
    aid = next(x["id"] for x in opts if x["text"] == answer)
    refs = [{"url": u, "title": f"{t}；僅研究公開題型與能力方向，未複製原題。", "year": "113-114", "subject": "chinese", "locator": l, "observedPattern": "公立學校國文公開試題以文言詞義、詞性、活用與語詞結構考查上下文判讀；本題重新設計。", "reuseDecision": "pattern-only", "status": "recorded", "locatorLevel": "paper"} for u, t, l in SOURCES]
    steps = [
        f"讀題定位：圈出「{tag}」與完整句子的主語、動作、受詞、修飾關係及上下文線索。",
        f"建立文言判準：先辨認詞性與義項，再檢查偏正、動賓、主謂或活用；本題核心是「{explanation}」",
        f"核對正解：選項 {aid}「{answer}」放回句中後，詞義、句法與語境均能成立。",
        "排除誘答：逐項檢查是否把現代義硬套文言、忽略詞性轉換，或只因字詞相鄰就誤判結構。",
        "結論回查：重新翻譯整句，確認答案沒有脫離前後文；若資料不足，應保留暫解並尋找完整語境。",
    ]
    return {"id": f"question-chinese-content-ab-iv-6-{index}", "subject": "chinese", "type": "single-choice", "prompt": prompt, "options": opts, "knowledgeIds": ["kg-chinese-content-ab-iv-6"], "difficulty": "medium", "answer": {"value": aid, "explanation": explanation}, "provenance": {"origin": "original", "license": "All rights reserved", "sourceUrl": SOURCES[0][0], "sourceLocator": "公立學校公開國文段考與課程資料；本題只研究公開試題與課程評量的能力結構。", "authoringNote": "依官方語文領域課綱、單元 KG 與三個公立學校公開來源的題型方向，獨立改寫文言詞義、代詞、古今義、偏正、動賓、主謂、詞性活用與資料界線；未複製原文、選項、篇章、圖表或答案；待第二輪 AI／Terra 內容複核。"}, "reviewStatus": "draft", "updatedAt": "2026-09-09", "lessonId": "lesson-chinese-content-ab-iv-6", "examPatternRefs": refs, "solutionStrategy": "先讀完整句子，辨認詞性與語境，再用句法結構拆解；文言詞不可固定翻譯，最後要用整句語意回查。", "solutionSteps": steps}

for index, row in enumerate(DATA, 1):
    (OUT / f"question-chinese-content-ab-iv-6-{index}.json").write_text(json.dumps(make_question(index, row), ensure_ascii=False, indent=2) + "\n", encoding="utf-8")
print(f"rewrote {len(DATA)} questions")
