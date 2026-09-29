#!/usr/bin/env python3
"""Independently rewrite Chinese literacy and writing questions for Ab-IV-1."""
import json
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
OUT = ROOT / "questions/chinese"
LESSON = "lesson-chinese-performance-4-iv-1"
KG = "kg-chinese-performance-4-iv-1"
SOURCES = [
    ("https://www.sdjh.ntpc.edu.tw/var/file/0/1000/attach/16/pta_2229_1166226_19803.pdf", "新北市立石碇國中公開國文試題", "字形、字音、詞義與語體"),
    ("https://www.yacjh.kh.edu.tw/upload/221/101_30637/114%E4%B8%8B%E5%AD%B8%E6%9C%9F%E7%AC%AC一%E6%AC%A1%E6%AE%B5%E8%80%83%E4%B8%89%E5%B9%B4%E7%B4%9A%E5%9C%8B%E6%96%87.pdf", "高雄市立鹽埕國中公開國文段考", "常用字形音義與成語"),
    ("https://www.jlsh.mlc.edu.tw/var/file/12/1012/img/113-2-7-4.pdf", "國立卓蘭高中附設國中部公開課程與試題資料", "語境、搭配與查證"),
]


def refs():
    return [{
        "url": url, "title": f"{title}；僅研究公開題型與能力方向，未複製原題。",
        "year": "113-114", "subject": "chinese", "locator": locator,
        "observedPattern": "公立學校國文評量以形近字、詞義、搭配、語體、同音辨識、成語查證與上下文推理要求精確識字與書寫；本題採全新語料。",
        "reuseDecision": "pattern-only", "status": "recorded", "locatorLevel": "paper"
    } for url, title, locator in SOURCES]


DATA = [
    ("形近字", "研究團隊持續＿＿集雨量資料；哪個字最符合語意？", ["搜", "艘", "蒐", "嗖"], "C", "蒐集表示廣泛收集資料，需依詞義辨識形近字，不能只看讀音相近。", "先看詞語整體要表達的動作，再比較字形、字義與常見搭配。"),
    ("目的詞義", "「這項措施旨在降低通勤風險」中的「旨在」最接近哪個意思？", ["已經造成", "目的在於", "不願意面對", "暫時停止"], "B", "旨在用來指出目的，句中說明措施想達成降低風險的方向。", "把詞語換成白話，確認它在句中連接的是目的、結果、態度還是時間。"),
    ("證據搭配", "哪個詞最適合填入「＿＿證據後再提出結論」？", ["品嚐", "聆賞", "栽培", "檢視"], "D", "證據需要查閱、檢查與評估，檢視的語意和提出結論前的動作搭配自然。", "看動詞的受詞與後續行動，再排除只適合食物、藝術或植物的搭配。"),
    ("多義字", "「他把事情說得很透」中的「透」最接近哪個意思？", ["穿過物體", "液體滲出", "清楚深入", "光線明亮"], "C", "說得很透指解釋清楚、深入，是透在抽象語境中的引申義。", "先找透修飾的對象，再比較空間、液體、光線與理解程度等義項。"),
    ("正式語體", "給校方的正式建議書中，哪個詞語最合適？", ["超讚啦", "有點扯", "建請研議", "隨便弄弄"], "C", "建請研議語氣穩定、清楚且符合正式書面對象；其餘是口語或隨便的表達。", "先判斷收件者與文本用途，再檢查詞語的正式程度、禮貌與明確性。"),
    ("同音辨識", "下列哪一組詞語的加點字讀音相同？", ["行走／行業", "長短／成長", "和平／唱和", "便宜／方便"], "D", "便宜與方便的便都讀ㄅㄧㄢˋ；其他組的字在不同詞中有不同讀音。", "逐詞朗讀並把字放回完整詞語，不用單字最熟悉的讀音直接套用。"),
    ("搭配修訂", "「他用很精準的眼光觀察問題」若要使詞語更自然，哪項修訂較佳？", ["他用甜美的眼光觀察問題", "他用敏銳的眼光觀察問題", "他用沉重的眼光觀察問題", "他用遙遠的眼光觀察問題"], "B", "敏銳能修飾觀察力與判斷力，和眼光觀察問題的語境搭配自然。", "先確認名詞需要的是感官、能力或情緒形容，再檢查修飾關係是否成立。"),
    ("場景詞義", "雨勢稍歇，街角又恢復＿＿；哪個詞最能表現人車活動重新出現？", ["寂寥", "凝滯", "荒蕪", "喧闐"], "D", "喧闐描述聲音與人群熱鬧，符合雨停後街角活動恢復的場景。", "把詞語放進畫面，檢查它描寫的是熱鬧、安靜、停滯還是荒廢。"),
    ("查證順序", "遇到不確定的成語用字，哪種查證順序最可靠？", ["只依手機自動選字，不看句意", "選筆畫最少的字", "先看完整語境，再查權威辭典例句，最後回讀句子確認", "問朋友一次就當確定"], "C", "字詞判斷要結合語境與可靠工具；查到義項後仍需回到原句驗證搭配。", "先由上下文提出候選，再查權威解釋與例句，最後確認字形、字音和語意都吻合。"),
    ("陌生詞推理", "閱讀科普短文遇到陌生詞，哪套方法最能保留理解又避免誤解？", ["看到陌生詞就跳過整段", "只記最像的同音字", "把第一次猜的詞義固定不改", "先用上下文推測，再拆解詞素或查辭典，最後以後文證據修正"], "D", "成熟的字詞學習是可修正的推理流程，讓語境、構詞、工具與後文共同驗證。", "先利用前後句保留暫定意思，再查詞素與辭典，最後用後文檢查是否需要修正。"),
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
        f"讀題定位：圈出「{tag}」與詞語搭配、語體、讀音、字形或上下文線索。",
        f"拆解字詞：先用語境提出義項，再依「{explanation}」比較字音、字形與搭配。",
        f"核對正解：選項 {target} 能在完整詞語與句子中成立，而非只因單字外觀或直覺相似。",
        "排除誘答：檢查是否混淆形近字、古今義、詞性、語體或把自動選字當成查證結果。",
        "回讀驗證：將答案放回原句，確認字形、讀音、詞義、搭配與文本目的均一致。",
    ]
    item = {
        "id": f"question-chinese-performance-4-iv-1-{i}", "subject": "chinese", "type": "single-choice",
        "prompt": prompt, "options": [{"id": chr(65 + j), "text": text} for j, text in enumerate(options)],
        "knowledgeIds": [KG], "difficulty": "medium",
        "answer": {"value": target, "explanation": explanation},
        "provenance": {"origin": "original", "license": "All rights reserved", "sourceUrl": SOURCES[0][0],
                       "sourceLocator": "三所公立學校公開國文資料；只研究形音義、語境搭配、語體、成語與查證流程。",
                       "authoringNote": "依官方語文領域課綱、單元 KG 與三個公立學校公開來源，重新撰寫中文識字與寫字表現 Ab-Ⅳ-1 題；未複製原文、選項、篇章或答案；待第二輪 AI／Terra 內容複核。"},
        "reviewStatus": "draft", "updatedAt": "2026-09-13", "lessonId": LESSON,
        "examPatternRefs": refs(), "solutionStrategy": strategy, "solutionSteps": steps,
    }
    (OUT / f"question-chinese-performance-4-iv-1-{i}.json").write_text(json.dumps(item, ensure_ascii=False, indent=2) + "\n", encoding="utf-8")

print(f"rewrote {len(DATA)} independent questions for {LESSON}")
