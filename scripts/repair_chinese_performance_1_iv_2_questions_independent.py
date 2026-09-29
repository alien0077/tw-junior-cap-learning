#!/usr/bin/env python3
"""Independently rewrite Chinese oral-expression questions for Ab-IV-2."""
import json
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
OUT = ROOT / "questions/chinese"
LESSON = "lesson-chinese-performance-1-iv-2"
KG = "kg-chinese-performance-1-iv-2"
SOURCES = [
    ("https://www.sdjh.ntpc.edu.tw/var/file/0/1000/attach/16/pta_2229_1166226_19803.pdf", "新北市立石碇國中公開國文試題", "口語語氣、修辭與受眾"),
    ("https://www.yacjh.kh.edu.tw/upload/221/101_30637/114%E4%B8%8B%E5%AD%B8%E6%9C%9F%E7%AC%AC%E4%B8%80%E6%AC%A1%E6%AE%B5%E8%80%83%E4%B8%89%E5%B9%B4%E7%B4%9A%E5%9C%8B%E6%96%87.pdf", "高雄市立鹽埕國中公開國文段考", "演講表達、反問與同理"),
    ("https://www.jlsh.mlc.edu.tw/var/file/12/1012/img/113-2-7-4.pdf", "國立卓蘭高中附設國中部公開課程與試題資料", "聲情、非語言線索與溝通"),
]


def refs():
    return [{
        "url": url, "title": f"{title}；僅研究公開題型與能力方向，未複製原題。",
        "year": "113-114", "subject": "chinese", "locator": locator,
        "observedPattern": "公立學校國文評量以聲情、重音、停頓、修辭、受眾調整、同理回應、反諷與異議處理要求學生判讀表達效果；本題採全新語料。",
        "reuseDecision": "pattern-only", "status": "recorded", "locatorLevel": "paper"
    } for url, title, locator in SOURCES]


DATA = [
    ("支持聲情", "班長對即將上台的同學說「慢慢來，我們都在這裡」；最可能傳達什麼聲情？", ["嘲笑和催促", "正式宣布比賽結果", "冷漠的命令", "安定、支持與鼓勵"], "D", "慢慢來與我們都在這裡結合情境和陪伴意象，形成支持語氣，不能只看單一詞。", "把語句放回說話情境，再觀察措辭、對象與陪伴效果，不脫離上下文。"),
    ("重音焦點", "朗讀「你現在就可以再試一次」時重讀「現在」，最可能強調什麼？", ["行動時機就在當下，而非無限延後", "對方永遠不可能成功", "說話者已取消提議", "句子只描述過去"], "A", "重讀現在會把聽者注意力集中在時間與立即行動，而不改變句子基本的鼓勵方向。", "先找被突出詞的語意，再比較重音改變的是時間、對象、程度還是立場焦點。"),
    ("停頓分寸", "演講者說「這個方案……還有幾個地方需要討論」時停頓，最合理的效果是？", ["證明方案完全失敗", "表示忘記所有內容", "保留思考與緩和語氣，提醒聽者結論尚未定案", "讓聽者確定沒人能提出意見"], "C", "停頓可製造思考空間與分寸，配合後句表示方案仍可討論，不能直接推成失敗或遺忘。", "把停頓前後的句意連起來，再判斷它是緩和、轉折、保留或強調，而非孤立解讀。"),
    ("比喻功能", "宣導文寫「把每一滴水都留給明天」；這句比喻主要想達成什麼？", ["精確公布每日用水量", "證明水滴真的能被保存到明天", "取消所有節水規定", "把節水行動和未來生活連結，提升記憶與行動意願"], "D", "比喻把節水和未來生活連結，具有形象與感召功能，但不能取代數據或制度說明。", "先說明字面不可能的地方，再找它要讓讀者記住的抽象行動與情感效果。"),
    ("反問效果", "文章問「難道我們要等到河流乾涸才開始節水嗎？」最可能的表達效果是？", ["真正詢問一項可用是非回答的資料", "表示作者不在乎節水", "以反問凸顯延後行動的風險，促使讀者重新思考", "證明河流已經乾涸"], "C", "反問強化作者立場並催促思考，句子本身不能證明河流現況或提供統計資料。", "辨認問句是否期待讀者反駁字面答案，再寫出它實際要強調的立場。"),
    ("受眾調整", "同一項校園減塑方案要對小學生說明，哪種表達最合宜？", ["只使用碳排與供應鏈術語", "用具體例子和簡短步驟說明如何借用、清洗與歸還餐具", "用責罵語氣說不配合的人都不愛地球", "只說方案偉大，不告知如何做"], "B", "依受眾調整詞語、步驟與語氣，能讓訊息可理解、可執行；羞辱或抽象口號不能完成說明。", "先判斷聽眾的先備知識與可操作任務，再改寫詞彙、例子與行動順序。"),
    ("同理協助", "朋友說「我覺得報告做不好」；哪種回應最能兼顧同理和具體協助？", ["別想太多，你一定做得很好。", "那就全部重做，不必說明原因。", "我也覺得很糟，先不要再談。", "聽起來你很擔心；我們先找最卡的段落，再決定改資料還是結構。"], "D", "回應先承接感受，再把模糊焦慮轉成可處理的問題與選項，不用空泛保證取代協助。", "先反映情緒，再提出小範圍診斷與可選下一步，避免否定、代決或跟著放大焦慮。"),
    ("反諷判讀", "同學笑著說「你可真準時啊」，但對方已遲到二十分鐘；判斷聲情最需要什麼？", ["只看準時兩字就確定是真心稱讚", "因為遲到，任何語氣都一定是責罵", "完全不必考慮說話情境", "結合表情、聲音、前後對話與雙方關係，判斷可能是反諷並保留不確定"], "D", "字面稱讚和遲到事實形成落差，仍需非語言線索與關係確認，不能只憑一句話定論。", "把字面意思和情境落差並列，再尋找聲音、表情與後文證據，使用可能而非一定。"),
    ("尊重異議", "討論中有人提出不同意見；哪句回應最能尊重對方又保留自己的立場？", ["你完全不懂，不用再說。", "既然不同意，就代表你不在乎大家。", "我理解你重視執行速度；我仍擔心安全資料不足，能否先做一週觀察？", "好啦你說什麼都對，我不想討論。"], "C", "回應先重述對方關注，再提出自身理由與可行提議，不把不同意見攻擊成品格問題。", "先確認對方重視的價值，再用我訊息說明疑慮，最後提出能共同檢驗的下一步。"),
    ("完整口頭說明", "為社區會議準備一段口頭說明，哪套做法最完整？", ["只用最大聲的語氣壓過不同意見", "堆疊華麗比喻，不交代行動或資料", "固定每句語氣，不管內容和聽眾是否改變", "依受眾與目的安排語氣，以重音停頓突出重點，用資料支持主張，並預留回應疑問與修正方案的空間"], "D", "完整表達把聲情、技巧、證據、受眾與互動目的連在一起；技巧是為了理解與回應，不是取代內容。", "先定義聽眾與目的，再安排資訊順序、聲情重點、證據與提問回應。"),
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
        f"讀題定位：圈出「{tag}」與說話者、聽眾、重音、停頓、修辭或回應線索。",
        f"拆解效果：先分字面內容、聲情效果與溝通目的，再依「{explanation}」判斷。",
        f"核對正解：選項 {target} 能符合情境與受眾需求，並沒有把可能效果誇大成必然事實。",
        "排除誘答：檢查是否只看單字、用責罵取代說明、用華麗技巧取代資料，或把異議變成人身攻擊。",
        "回讀驗證：把答案放回完整對話，確認語氣、內容、證據與下一步彼此一致。",
    ]
    item = {
        "id": f"question-chinese-performance-1-iv-2-{i}", "subject": "chinese", "type": "single-choice",
        "prompt": prompt, "options": [{"id": chr(65 + j), "text": text} for j, text in enumerate(options)],
        "knowledgeIds": [KG], "difficulty": "medium",
        "answer": {"value": target, "explanation": explanation},
        "provenance": {"origin": "original", "license": "All rights reserved", "sourceUrl": SOURCES[0][0],
                       "sourceLocator": "三所公立學校公開國文資料；只研究聲情、重音、停頓、受眾調整、同理、反諷與異議處理。",
                       "authoringNote": "依官方語文領域課綱、單元 KG 與三個公立學校公開來源，重新撰寫中文聆聽與溝通表現 Ab-Ⅳ-2 題；未複製原文、選項、篇章或答案；待第二輪 AI／Terra 內容複核。"},
        "reviewStatus": "draft", "updatedAt": "2026-09-13", "lessonId": LESSON,
        "examPatternRefs": refs(), "solutionStrategy": strategy, "solutionSteps": steps,
    }
    (OUT / f"question-chinese-performance-1-iv-2-{i}.json").write_text(json.dumps(item, ensure_ascii=False, indent=2) + "\n", encoding="utf-8")

print(f"rewrote {len(DATA)} independent questions for {LESSON}")
