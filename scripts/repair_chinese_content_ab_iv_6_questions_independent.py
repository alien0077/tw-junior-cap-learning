#!/usr/bin/env python3
"""Independently rewrite Chinese Ab-IV-6 classical word and phrase questions."""
import json
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
OUT = ROOT / "questions/chinese"
LESSON = "lesson-chinese-content-ab-iv-6"
SOURCES = [
    ("https://www.sdjh.ntpc.edu.tw/var/file/0/1000/attach/16/pta_2229_1166226_19803.pdf", "新北市立石碇國中公開國文試題", "文言詞義、虛詞與句法"),
    ("https://www.yacjh.kh.edu.tw/upload/221/101_30637/114%E4%B8%8B%E5%AD%B8%E6%9C%9F%E7%AC%AC%E4%B8%80%E6%AC%A1%E6%AE%B5%E8%80%83%E4%B8%89%E5%B9%B4%E7%B4%9A%E5%9C%8B%E6%96%87.pdf", "高雄市立鹽埕國中公開國文段考", "古文詞義、結構與語境"),
    ("https://www.jlsh.mlc.edu.tw/var/file/12/1012/img/113-2-7-4.pdf", "國立卓蘭高中附設國中部公開課程與試題資料", "文言字詞活用與句法辨析"),
]


def refs():
    return [{
        "url": url, "title": f"{title}；僅研究公開題型與能力方向，未複製原題。",
        "year": "113-114", "subject": "chinese", "locator": locator,
        "observedPattern": "公立學校國文評量把文言字詞、虛詞、詞類活用與短語結構放入句子，要求依上下文判斷義項與語法功能；本題採全新語料。",
        "reuseDecision": "pattern-only", "status": "recorded", "locatorLevel": "paper"
    } for url, title, locator in SOURCES]


DATA = [
    ("之的代詞", "「學而時習之」中的「之」若代指所學內容，哪一句的用法最接近？", ["吾欲之南海。", "送孟浩然之廣陵。", "擇其善者而從之。", "何陋之有？"], "C", "題句的之是代詞，代指前文的所學；「擇其善者而從之」的之也承接前文內容，作代詞。", "先找之前面是否已有可被指代的名詞或事情，再排除到、的與賓語前置的功能。"),
    ("其的指示", "「其人未至，眾皆久候」中的「其」最適合譯為？", ["自己的", "那個、那位", "其中的", "難道"], "B", "其人可譯為那個人或那位人士，是指示限定；句中沒有反問或部分關係。", "把其和後面的名詞合讀，再看它是在指人、指物、指代整體，或表反問語氣。"),
    ("先的優先", "「先民而後己」中的「先」最適合解作？", ["先前的", "把他人放在前面、優先", "首先發言", "領先取勝"], "B", "先民而後己表示先考慮人民、再考慮自己，先是把對象置於優先位置。", "比較先修飾的對象與後接的對比詞，若句中有而後，通常要判斷先後次序與價值排序。"),
    ("偏正結構", "下列哪一組最能判定為偏正結構，前字修飾後字？", ["國破", "高山", "學而", "知人"], "B", "高山中高修飾山，說明山的高度；其他組合分別較接近主謂、連接或動賓關係。", "先問前字是在描述後字，還是在和後字共同敘述事件或形成動作關係。"),
    ("動賓結構", "下列哪一組屬於動詞帶受詞的動賓結構？", ["甚善", "讀書", "日落", "非常"], "B", "讀是動詞，書是讀的對象，構成動賓；其餘不是動詞帶受詞。", "把詞組改寫成『誰做什麼』，若後字能回答動作作用的對象，才是動賓。"),
    ("並列主謂", "「風止雲開」若依語詞結構分析，較接近哪一種關係？", ["兩個主謂短語並列", "偏正修飾", "動詞帶賓語", "介詞結構"], "A", "風止是風停止、雲開是雲散開，兩個主謂短語並列呈現景象變化。", "分別切開短語，找每一段的主體與狀態，再判斷兩段是並列還是前後修飾。"),
    ("可以的語境", "「積善之家，必有餘慶」若改問「可以無憂矣」中的「可以」，依文言語境應理解為？", ["可以拿來食用的東西", "能夠、就可以", "可以的樣子", "因為可以"], "B", "可以在此表示具備條件後能夠達成某結果，即能夠不憂慮；不是名詞或原因連詞。", "把可以放回整句，檢查後面接的是動作、狀態或原因，並用現代語改寫整句驗證。"),
    ("名詞活用", "「朝服衣冠」中的「服」最適合判定為？", ["名詞，衣服", "動詞，穿戴", "形容詞，服飾的", "語氣詞，表命令"], "B", "服衣冠是穿戴衣帽，服由名詞活用為動詞，後面接衣冠作動作對象。", "先看該字後面是否帶受詞，再用『穿戴什麼』測試詞性，不被現代常用義限制。"),
    ("明日的時間脈絡", "若只看到「明日」兩字、沒有上下文，最妥當的做法是？", ["一定只能譯成今天。", "一定只能譯成明亮的日子。", "直接依現代口語決定，不必查證。", "先列出常見義，再要求補足句子與時間脈絡。"], "D", "明日常可指第二天或明天，但準確翻譯仍要看敘事時間與上下文；單獨兩字不足以判定完整語意。", "先承認字詞可能有多個義項，再找時間參照點、敘事視角與前後事件。"),
    ("故的因果與故意", "同一個「故」可能表示原因、所以，也可能出現在「故意」中表示有意；要判斷義項最需要哪項證據？", ["與故相連的詞及前後句的因果或目的關係。", "故字的筆畫數。", "文章共有幾個標點符號。", "把現代最常見的意思固定套用。"], "A", "故的意義受搭配與句間邏輯制約；必須看它是在說原因結果，還是和意組成故意表目的或心態。", "先觀察固定搭配，再畫出前後句的因果、轉折或目的關係，避免只用單字直覺翻譯。"),
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
        f"讀題定位：圈出「{tag}」及其前後詞，標記主體、動作、受詞、時間或句間關係。",
        f"拆解語境：先把文言句改成白話，再依「{explanation}」辨認詞義或結構。",
        f"核對正解：選項 {target} 能同時符合句法位置、搭配與上下文，而非只符合單字表面意思。",
        "排除誘答：檢查是否把古今義混用、忽略詞類活用、誤認結構，或在缺少上下文時過度確定。",
        "回讀驗證：把答案放回原句，重新檢查翻譯、句法關係與前後邏輯是否順暢。",
    ]
    item = {
        "id": f"question-chinese-content-ab-iv-6-{i}", "subject": "chinese", "type": "single-choice",
        "prompt": prompt, "options": [{"id": chr(65 + j), "text": text} for j, text in enumerate(options)],
        "knowledgeIds": ["kg-chinese-content-ab-iv-6"], "difficulty": "medium",
        "answer": {"value": target, "explanation": explanation},
        "provenance": {"origin": "original", "license": "All rights reserved", "sourceUrl": SOURCES[0][0],
                       "sourceLocator": "三所公立學校公開國文資料；只研究文言詞義、虛詞、活用、結構與上下文判讀。",
                       "authoringNote": "依官方語文領域課綱、單元 KG 與三個公立學校公開來源，重新撰寫 Ab-Ⅳ-6 古今詞義與句法辨析題；未複製原文、選項、篇章或答案；待第二輪 AI／Terra 內容複核。"},
        "reviewStatus": "draft", "updatedAt": "2026-09-13", "lessonId": LESSON,
        "examPatternRefs": refs(), "solutionStrategy": strategy, "solutionSteps": steps,
    }
    (OUT / f"question-chinese-content-ab-iv-6-{i}.json").write_text(json.dumps(item, ensure_ascii=False, indent=2) + "\n", encoding="utf-8")

print(f"rewrote {len(DATA)} independent questions for {LESSON}")
