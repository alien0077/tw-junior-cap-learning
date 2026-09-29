#!/usr/bin/env python3
"""Independently rewrite Chinese Ab-IV-7 classical function-word questions."""
import json
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
OUT = ROOT / "questions/chinese"
LESSON = "lesson-chinese-content-ab-iv-7"
SOURCES = [
    ("https://www.sdjh.ntpc.edu.tw/var/file/0/1000/attach/16/pta_2229_1166226_19803.pdf", "新北市立石碇國中公開國文試題", "文言虛詞與語境"),
    ("https://www.yacjh.kh.edu.tw/upload/221/101_30637/114%E4%B8%8B%E5%AD%B8%E6%9C%9F%E7%AC%AC%E4%B8%80%E6%AC%A1%E6%AE%B5%E8%80%83%E4%B8%89%E5%B9%B4%E7%B4%9A%E5%9C%8B%E6%96%87.pdf", "高雄市立鹽埕國中公開國文段考", "虛詞功能與古今詞義"),
    ("https://www.jlsh.mlc.edu.tw/var/file/12/1012/img/113-2-7-4.pdf", "國立卓蘭高中附設國中部公開課程與試題資料", "文言句法與語氣判讀"),
]


def refs():
    return [{
        "url": url, "title": f"{title}；僅研究公開題型與能力方向，未複製原題。",
        "year": "113-114", "subject": "chinese", "locator": locator,
        "observedPattern": "公立學校國文評量以完整文言句檢驗之、以、而、其等虛詞的句法功能、語氣與古今詞義；本題採全新語料。",
        "reuseDecision": "pattern-only", "status": "recorded", "locatorLevel": "paper"
    } for url, title, locator in SOURCES]


DATA = [
    ("之作受詞", "「讀書而思其義」中的「之」若代指書中內容，哪一句的「之」也作動詞受詞？", ["吾欲之南海。", "山川之美。", "擇其善者而從之。", "何陋之有。"], "C", "題句的之代指內容，是思考的受詞；「擇其善者而從之」的之也承接前文對象，作從的受詞。", "先找之前是否有可被指代的對象，再判斷前面的動詞能否直接支配它。"),
    ("之作結構助詞", "「溪流之清，令人忘憂」中的「之」最適合判斷為？", ["代指溪流。", "結構助詞，的。", "動詞，到往。", "反問語氣。"], "B", "溪流之清可譯為溪流的清澈，之連接修飾語與中心語，作結構助詞。", "把之改成『的』試讀，若前後形成修飾與被修飾關係，就不能當代詞或動詞。"),
    ("以的工具", "「以繩繫舟」中的「以」依語境應解作？", ["因為。", "用、拿。", "已經。", "來、以便。"], "B", "以繩繫舟表示用繩子繫船，以介紹完成動作所用的工具。", "看以後面的名詞是否是工具，再用『用什麼做』替換驗證。"),
    ("以的原因", "「以山路險遠，行者多止」中的「以」較接近哪個功能？", ["因為、由於。", "拿著。", "以及。", "到、往。"], "A", "因山路險遠所以行者停下，前後是原因與結果，故以引出原因。", "先找句中結果，再回問前半句是否回答『為什麼』，不要只依以後面的字猜。"),
    ("而的轉折", "「眾皆勸行，而我獨留」中的「而」最適合解作？", ["並且。", "可是、卻。", "就要。", "因此。"], "B", "前句說眾人勸行，後句說我獨留，兩分句相反，表示轉折。", "比較而前後的主體與事件方向；若後句逆轉前句期待，譯為卻或可是。"),
    ("其的反問", "「其真可成邪？其未嘗試也！」前一個「其」最接近哪個語氣？", ["大概。", "那個。", "自己的。", "難道、豈。"], "D", "其真可成邪是反問，意為難道真的可以成功嗎；後文再說明尚未嘗試。", "把其和句末疑問語氣一起讀，若是在質疑可能性，通常不是指示代詞。"),
    ("古今交通", "「兩岸交通，舟楫往來」中的「交通」若依古文式語境解讀，最接近？", ["道路或水路交錯相通。", "現代的交通工具。", "人與人交換意見。", "交通規則管理。"], "A", "句中接著寫舟楫往來，交通是路線彼此相通；不能直接套用現代運輸工具義。", "先看搭配對象與後續畫面，再比較古義是否描述通達，而非現代制度名詞。"),
    ("古今妻子", "「攜妻子與老幼避亂」中的「妻子」古義最接近？", ["妻子的個性。", "妻子一人。", "妻子和兒女。", "女性的孩子。"], "C", "妻子在此是妻子與兒女的合稱，後面又以老幼補充家人範圍。", "遇到古今皆通的詞，先看它是否和並列家人詞共同出現，再判斷古義範圍。"),
    ("虛詞判讀流程", "下列哪個判斷最能說明閱讀文言虛字的方法？", ["同一虛字在全文只能有一種意思。", "先看句法位置，再用前後文與語氣驗證功能。", "只要查現代辭典第一義即可。", "虛字沒有意義，不需要分析。"], "B", "虛字功能受句法、搭配與語氣影響，必須放回上下文判斷，不能把同字固定成單一義。", "先定位虛字連接的成分，再用翻譯、句間邏輯與語氣三項交叉驗證。"),
    ("以的多功能", "只看到「以」字、沒有完整句子或前後文，最妥當的做法是？", ["直接固定翻成用。", "只看它後面可能接的字就下結論。", "把所有義項同時當成答案。", "先列出工具、原因、目的等候選功能，再要求補充語境。"], "D", "以可表示工具、原因、目的或憑藉，單獨一字不足以唯一判斷，必須補足句法與上下文。", "先列出可行義項，再要求能區分功能的受詞、句法位置與前後邏輯，避免過早定案。"),
]
TARGETS = ["A", "B", "C", "D", "B", "C", "D", "A", "B", "C"]

for i, (tag, prompt, options, answer, explanation, strategy) in enumerate(DATA, 1):
    target = TARGETS[i - 1]
    correct_index = ord(answer) - 65
    target_index = ord(target) - 65
    correct = options[correct_index]
    rest = [value for index, value in enumerate(options) if index != correct_index]
    options = rest[:target_index] + [correct] + rest[target_index:]
    steps = [
        f"讀題定位：圈出「{tag}」與同句的動詞、名詞、修飾語、語氣或分句連接線索。",
        f"拆解功能：先將句子翻成白話，再依「{explanation}」判斷虛詞功能或古今義。",
        f"核對正解：選項 {target} 能在句法位置與前後邏輯中成立，而非只因字面相似。",
        "排除誘答：檢查是否把同字固定成單一義、把古義換成今義，或忽略轉折、因果與受詞。",
        "回讀驗證：把答案放回原句，確認翻譯、語氣與分句關係均前後一致。",
    ]
    item = {
        "id": f"question-chinese-content-ab-iv-7-{i}", "subject": "chinese", "type": "single-choice",
        "prompt": prompt, "options": [{"id": chr(65 + j), "text": text} for j, text in enumerate(options)],
        "knowledgeIds": ["kg-chinese-content-ab-iv-7"], "difficulty": "medium",
        "answer": {"value": target, "explanation": explanation},
        "provenance": {"origin": "original", "license": "All rights reserved", "sourceUrl": SOURCES[0][0],
                       "sourceLocator": "三所公立學校公開國文資料；只研究文言虛詞、古今詞義、句法功能與語氣判讀。",
                       "authoringNote": "依官方語文領域課綱、單元 KG 與三個公立學校公開來源，重新撰寫 Ab-Ⅳ-7 文言虛詞與古今詞義題；未複製原文、選項、篇章或答案；待第二輪 AI／Terra 內容複核。"},
        "reviewStatus": "draft", "updatedAt": "2026-09-13", "lessonId": LESSON,
        "examPatternRefs": refs(), "solutionStrategy": strategy, "solutionSteps": steps,
    }
    (OUT / f"question-chinese-content-ab-iv-7-{i}.json").write_text(json.dumps(item, ensure_ascii=False, indent=2) + "\n", encoding="utf-8")

print(f"rewrote {len(DATA)} independent questions for {LESSON}")
