#!/usr/bin/env python3
"""Independently rewrite Chinese polyphonic-word questions for Ab-IV-3."""
import json
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
OUT = ROOT / "questions/chinese"
LESSON = "lesson-chinese-performance-4-iv-3"
KG = "kg-chinese-performance-4-iv-3"
SOURCES = [
    ("https://www.sdjh.ntpc.edu.tw/var/file/0/1000/attach/16/pta_2229_1166226_19803.pdf", "新北市立石碇國中公開國文試題", "多音多義字、詞語與語境"),
    ("https://www.yacjh.kh.edu.tw/upload/221/101_30637/114%E4%B8%8B%E5%AD%B8%E6%9C%9F%E7%AC%AC一%E6%AC%A1%E6%AE%B5%E8%80%83%E4%B8%89%E5%B9%B4%E7%B4%9A%E5%9C%8B%E6%96%87.pdf", "高雄市立鹽埕國中公開國文段考", "字音、字義與辭典查證"),
    ("https://www.jlsh.mlc.edu.tw/var/file/12/1012/img/113-2-7-4.pdf", "國立卓蘭高中附設國中部公開課程與試題資料", "古今混用、正式語體與詞義"),
]


def refs():
    return [{
        "url": url, "title": f"{title}；僅研究公開題型與能力方向，未複製原題。",
        "year": "113-114", "subject": "chinese", "locator": locator,
        "observedPattern": "公立學校國文評量以多音多義字、完整詞語讀音、詞義、辭典例句、古今混用與正式改寫要求依語境查證；本題採全新語料。",
        "reuseDecision": "pattern-only", "status": "recorded", "locatorLevel": "paper"
    } for url, title, locator in SOURCES]


DATA = [
    ("行的詞語音", "下列「行」字讀音與「銀行」相同的是哪一項？", ["行列", "行走", "行業", "行動"], "C", "銀行與行業的行都讀ㄏㄤˊ；同一字要放入完整詞語辨讀，不能只看單字。", "先確認詞語整體，再比較辭典音項與詞義，不用最熟悉的讀音套用所有詞。"),
    ("長的音義", "下列哪一組「長」的讀音前後相同？", ["長大／長短", "成長／長官", "擅長／長短", "長期／長子"], "D", "長期與長子的長都讀ㄔㄤˊ；多音字要依詞義與固定詞組判斷。", "逐詞朗讀並說明長在詞中的意思，再排除同字不同音或同音不同義的組合。"),
    ("便的音義", "「便利」與「便宜」中的「便」，哪項說明正確？", ["兩者都讀ㄅㄧㄢˋ，但詞義分別是方便與價格低廉", "兩者都讀ㄆㄧㄢˊ，意思完全相同", "前者讀ㄆㄧㄢˊ，後者讀ㄅㄧㄢˋ且都指便利", "只要看見便就固定讀ㄅㄧㄢˋ，不必看語境"], "A", "兩詞的便都讀ㄅㄧㄢˋ，但便利指方便，便宜在此指價格低廉；同音不等於同義。", "先查完整詞語讀音，再用句中搭配分辨不同義項。"),
    ("當的查證", "「當作」與「當鋪」的「當」讀音不同，最好的查證方法是？", ["只查當的第一個讀音", "依字的筆畫數猜讀音", "把兩詞讀成相同音方便記憶", "查兩個完整詞語的辭典音義與例句，再比較語境功能"], "D", "多音多義字必須以完整詞語查證，辭典例句能同時確認讀音、詞義與用法。", "以詞語而非單字為查詢單位，再用例句檢查它在原句的功能。"),
    ("重的義項", "「重視」和「重量」的「重」雖讀音相同，詞義為何不同？", ["前者表示再次，後者表示重新", "兩者詞義完全相同，只是詞性不同", "前者表示看待重要，後者表示物體所受的重量概念", "前者指沉重天氣，後者指尊敬他人"], "C", "重視的重表示看待重要，重量的重涉及物體重量概念；同音字仍可能有不同義項。", "從詞語搭配和句子功能推定義項，不把讀音當成詞義。"),
    ("為的音義", "「作為」和「因為」中的「為」讀音與功能不同，哪項判斷正確？", ["兩詞都讀ㄨㄟˊ且都表示原因", "作為讀ㄨㄟˋ、因為讀ㄨㄟˊ", "讀音由前一字聲調決定，詞義不用考慮", "作為讀ㄨㄟˊ表示當作；因為讀ㄨㄟˋ表示原因"], "D", "為的讀音和詞義、句法功能連動，完整詞語與句中角色是判斷依據。", "先分辨詞語功能，再查音項，最後用句子回讀確認音義一致。"),
    ("數的策略", "「數落」與「數學」的「數」，哪項策略最能避免誤讀？", ["看到數一律讀ㄕㄨˋ", "看到數一律讀ㄕㄨˇ", "只看詞尾不看數的作用", "先判斷詞義，再查完整詞語音項，不把數字義套在所有詞中"], "D", "多音字詞義會牽動讀音，先判斷數在詞中的功能，再用辭典驗證較可靠。", "把字放回詞語，先理解是計算、數說還是責備等功能，再核對讀音。"),
    ("薄的詞語", "查到「薄」有多個義項時，哪個步驟能選出「薄荷」的正確解釋？", ["只選最常見的厚薄意思", "看部首直接決定讀音", "把所有義項平均套進同一句", "以完整詞語查讀音與詞義，並用例句確認它是植物名"], "D", "辭典條目要依完整詞語和例句定位，單字常見意思不一定適用於複合詞。", "先查薄荷整詞，再以例句確認詞性、讀音與植物義項。"),
    ("正式改寫", "把「他很會說話」改寫成正式報告語句時，哪項最需先查證？", ["把會固定改成將來時", "只替換同音字讓字面正式", "刪掉整句避免多義字", "確認會在此表示擅長，再依語境改成具備良好口語表達能力等精確說法"], "D", "改寫前要確認多義字原句義項，再依正式語體選擇明確表達。", "先解釋原句的會，再檢查報告需要的正式程度與可測量表達。"),
    ("整句查證", "遇到含三個多音多義字的古今混用句，哪套流程最完整？", ["逐字查第一音後直接拼回句子", "只依朗讀習慣不查辭典", "列出所有音義但不選定", "切分詞語與句法，逐詞查音義和例句，再回讀整句檢查語意與語體"], "D", "查典不是羅列所有可能，而是從詞語、句法與語境逐步排除，建立可核對的整句理解。", "先切詞與找句法角色，再逐詞查證，最後用整句語意和語體淘汰不合者。"),
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
        f"讀題定位：圈出「{tag}」與完整詞語、句法功能、語體或古今語境線索。",
        f"切分查證：先把字放回詞語與句子，再依「{explanation}」比較音義與用法。",
        f"核對正解：選項 {target} 能同時符合辭典音項、詞義、搭配與原句語體。",
        "排除誘答：檢查是否只查單字第一音、把同音當同義、把現代直覺套古文，或羅列可能卻不做判定。",
        "回讀驗證：重新朗讀完整句子，確認字音、詞義、句法與正式程度彼此一致。",
    ]
    item = {
        "id": f"question-chinese-performance-4-iv-3-{i}", "subject": "chinese", "type": "single-choice",
        "prompt": prompt, "options": [{"id": chr(65 + j), "text": text} for j, text in enumerate(options)],
        "knowledgeIds": [KG], "difficulty": "medium",
        "answer": {"value": target, "explanation": explanation},
        "provenance": {"origin": "original", "license": "All rights reserved", "sourceUrl": SOURCES[0][0],
                       "sourceLocator": "三所公立學校公開國文資料；只研究多音多義字、完整詞語、辭典例句、古今混用與正式語體。",
                       "authoringNote": "依官方語文領域課綱、單元 KG 與三個公立學校公開來源，重新撰寫中文識字與寫字表現 Ab-Ⅳ-3 題；未複製原文、選項、篇章或答案；待第二輪 AI／Terra 內容複核。"},
        "reviewStatus": "draft", "updatedAt": "2026-09-13", "lessonId": LESSON,
        "examPatternRefs": refs(), "solutionStrategy": strategy, "solutionSteps": steps,
    }
    (OUT / f"question-chinese-performance-4-iv-3-{i}.json").write_text(json.dumps(item, ensure_ascii=False, indent=2) + "\n", encoding="utf-8")

print(f"rewrote {len(DATA)} independent questions for {LESSON}")
