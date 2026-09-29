#!/usr/bin/env python3
"""Independently rewrite Chinese character-making questions for Ab-IV-2."""
import json
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
OUT = ROOT / "questions/chinese"
LESSON = "lesson-chinese-performance-4-iv-2"
KG = "kg-chinese-performance-4-iv-2"
SOURCES = [
    ("https://www.sdjh.ntpc.edu.tw/var/file/0/1000/attach/16/pta_2229_1166226_19803.pdf", "新北市立石碇國中公開國文試題", "六書、部件與字形證據"),
    ("https://www.yacjh.kh.edu.tw/upload/221/101_30637/114%E4%B8%8B%E5%AD%B8%E6%9C%9F%E7%AC%AC一%E6%AC%A1%E6%AE%B5%E8%80%83%E4%B8%89%E5%B9%B4%E7%B4%9A%E5%9C%8B%E6%96%87.pdf", "高雄市立鹽埕國中公開國文段考", "造字法、形音義與演變"),
    ("https://www.jlsh.mlc.edu.tw/var/file/12/1012/img/113-2-7-4.pdf", "國立卓蘭高中附設國中部公開課程與試題資料", "構件推理與字源查證"),
]


def refs():
    return [{
        "url": url, "title": f"{title}；僅研究公開題型與能力方向，未複製原題。",
        "year": "113-114", "subject": "chinese", "locator": locator,
        "observedPattern": "公立學校國文評量以象形、指事、會意、形聲、假借、轉注、義符／聲符限制與古今字形演變要求依證據判讀造字原則；本題採全新語料。",
        "reuseDecision": "pattern-only", "status": "recorded", "locatorLevel": "paper"
    } for url, title, locator in SOURCES]


DATA = [
    ("象形取象", "下列說明哪一項最符合象形造字？", ["把兩個抽象概念相加表示新義", "用聲符提示讀音並用義符限定範圍", "借用已有字形表示另一個讀音", "依事物外形描繪，如以簡化圖形表示日、月"], "D", "象形從可觀察事物的形體取象，字形雖會簡化，仍可追溯描摹關係。", "先問字形是否直接取自可見事物，再排除構件組合、聲音提示與借字功能。"),
    ("指事標記", "「本」在字形上以根部標記表示樹的根，主要展現哪種原則？", ["象形", "形聲", "轉注", "指事"], "D", "指事用抽象符號或標記指出位置、方向或概念，本是在象形木上標示根部。", "比較整體是否描摹物形，以及是否另加標記指出原本難以描畫的位置或概念。"),
    ("會意組合", "「休」由人倚靠木組合出休息意義，最適合用哪個分類理解？", ["假借", "指事", "形聲", "會意"], "D", "會意把兩個以上有意義的構件組合，從彼此關係推得新義，不能只因讀音相近判斷。", "先說明每個構件的意義，再檢查新義是否由構件關係共同形成。"),
    ("形聲分工", "哪一項最能說明「清」的形聲特徵？", ["以整個字描畫清晨景象", "把清楚與水兩個抽象概念並列", "借另一字只表示相同讀音", "以氵提示水義範圍，以青提示讀音線索"], "D", "形聲通常由義符與聲符分工，聲符是讀音線索而非絕對保證，義符也不等於完整詞義。", "分別標出可能提示意義與讀音的構件，再回到實際詞義確認線索是否成立。"),
    ("聲符限制", "由「青」作聲符的字讀音不一定完全相同，最合理的解釋是？", ["聲符一出現就保證現代讀音完全相同", "聲符只表示筆畫數", "聲符和讀音沒有關係", "聲符提供歷史或近似音線索，語音演變與方言差異會造成變化"], "D", "聲符是線索而非保證，歷史音變與方言差異可能使同聲符字的現代讀音不同。", "先把聲符當候選讀音提示，再用現代讀音、語境與工具查證，不把線索當定律。"),
    ("義符推論", "看到「木」作為構件時，哪個推論最穩妥？", ["直接判定整字只表示一棵樹", "只依構件讀音判斷字義", "所有含木字旁的字都同一詞性", "先把它當與樹木或木材相關的線索，再回到完整字義與語境確認"], "D", "義符能縮小意義範圍，卻不等於完整定義，還要考慮構形、詞義與實際語境。", "先提出範圍性假設，再檢查整字構件、詞語搭配與上下文是否支持。"),
    ("假借原則", "把原本已有的字形借來表示同音或近音的新義，較接近哪項造字原則？", ["象形", "會意", "指事", "假借"], "D", "假借是借現成字形表示新語義，重點在使用關係而非另造新形，仍須看語境與字源說明。", "先問字形是否為既有字，再判斷新義是否透過音近借用而來。"),
    ("轉注界線", "學習轉注時，哪項說法較謹慎？", ["凡形狀相近的字都一定是轉注", "只要兩字讀音不同就不是轉注", "轉注就是把外語翻成漢字", "涉及同一語源或義類的字互相解釋，不能只看現代字形相似"], "D", "六書分類需要字源與義類證據；轉注不能以表面相似或單一讀音條件直覺判定。", "先找字源、義類與互訓證據，再說明不確定處，不用現代外形直接下結論。"),
    ("字形演變", "古文字與現代字形差異很大時，哪種方法最能避免誤判？", ["把現代部件直接當古代原始圖形", "只計算筆畫數", "看到不像圖畫就判定沒有關係", "比較字形演變資料與構件功能，再以詞義和語境交叉確認"], "D", "文字演變會改變筆形與構件位置，需要結合歷史字形、功能、詞義與語境而非只看外觀。", "先查不同時期字形，再追蹤構件功能與語義，最後用現代詞語回讀驗證。"),
    ("形聲查證", "遇到陌生形聲字時，哪套推理最完整？", ["只按聲符猜讀音並確定詞義", "只看部首就不必查證", "把所有構件都當獨立完整詞義相加", "先辨認義符和聲符，提出音義假設，再放回詞語查辭典與例句修正"], "D", "造字原則是推理工具而非免查證答案，形、音、義線索要在實際詞語中互相校正。", "先分構件功能，再保留暫定音義，最後用詞語、辭典與例句確認或修正。"),
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
        f"讀題定位：圈出「{tag}」與構件、字形演變、聲音線索、意義或字源資料。",
        f"拆解造字：先說明構件功能，再依「{explanation}」比較象形、指事、會意、形聲或借用。",
        f"核對正解：選項 {target} 能由字形、構件或歷史資料支持，且保留聲符／義符的限制。",
        "排除誘答：檢查是否把現代外形當古文字、把聲符當讀音保證，或用單一構件直接決定整字。",
        "回讀驗證：把造字判斷放回實際字形與詞語，確認形、音、義和語境沒有互相矛盾。",
    ]
    item = {
        "id": f"question-chinese-performance-4-iv-2-{i}", "subject": "chinese", "type": "single-choice",
        "prompt": prompt, "options": [{"id": chr(65 + j), "text": text} for j, text in enumerate(options)],
        "knowledgeIds": [KG], "difficulty": "medium",
        "answer": {"value": target, "explanation": explanation},
        "provenance": {"origin": "original", "license": "All rights reserved", "sourceUrl": SOURCES[0][0],
                       "sourceLocator": "三所公立學校公開國文資料；只研究六書、形音義、構件功能、字形演變與造字查證。",
                       "authoringNote": "依官方語文領域課綱、單元 KG 與三個公立學校公開來源，重新撰寫中文識字與寫字表現 Ab-Ⅳ-2 題；未複製原文、選項、篇章或答案；待第二輪 AI／Terra 內容複核。"},
        "reviewStatus": "draft", "updatedAt": "2026-09-13", "lessonId": LESSON,
        "examPatternRefs": refs(), "solutionStrategy": strategy, "solutionSteps": steps,
    }
    (OUT / f"question-chinese-performance-4-iv-2-{i}.json").write_text(json.dumps(item, ensure_ascii=False, indent=2) + "\n", encoding="utf-8")

print(f"rewrote {len(DATA)} independent questions for {LESSON}")
