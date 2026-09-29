#!/usr/bin/env python3
"""Independent English Ad-IV-1 grammar and sentence-pattern rewrite."""
import json
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
OUT = ROOT / "questions/english"
LESSON = "lesson-english-content-ad-iv-1"
SOURCES = [
    ("https://www.kusjh.kh.edu.tw/upload/files/110%E4%B8%8A%E7%AC%AC1%E6%AC%A1%E6%AE%B5%E8%80%83%E5%9C%8B%E4%B8%AD%E4%B8%80%E5%B9%B4%E7%B4%9A%E8%A9%A6%E9%A1%8C.pdf", "高雄市立鼓山高中國中部七年級公開英語段考", "基礎句型、文法與對話"),
    ("https://www.kcjh.kh.edu.tw/upload/190/104_34764/%E5%9C%8B%E6%98%8C--%E4%B8%80%E5%B9%B4%E7%B4%9A--%E8%8B%B1%E6%96%87%E7%A7%91.pdf", "高雄市立國昌國中七年級公開英語段考", "基本時態、代名詞與問答"),
    ("https://www.dam.kh.edu.tw/upload/68/101_28414/114-1%E4%B8%83%E5%B9%B4%E7%B4%9A%E7%AC%AC%E4%B8%80%E6%AC%A1%E6%AE%B5%E8%80%83%E8%A9%A6%E5%8D%B7%E6%9A%A8%E8%A7%A3%E7%AD%94.pdf", "高雄市立大社國中七年級公開英語段考", "句型選擇、文意與生活語境"),
]

def refs():
    return [{"url": u, "title": f"{t}；僅研究公開題型與能力方向，未複製原題。", "year": "110-114", "subject": "english", "locator": l, "observedPattern": "公立學校國中英語評量要求在生活句子中判斷 be 動詞、一般動詞、主詞代名詞、疑問詞、否定、複數與基本時態；本題採全新句子。", "reuseDecision": "pattern-only", "status": "recorded", "locatorLevel": "paper"} for u, t, l in SOURCES]

DATA = [
    ("My brother ______ a student at this school.", ["am", "is", "are", "be"], "A", "The subject My brother is third-person singular, so the present form of be is is.", "先找主詞人稱與單複數，再選相符的 be 動詞。", ["Locate the subject My brother.", "Classify it as third-person singular.", "Recall the present be form for this subject.", "Choose is.", "Read the whole sentence to confirm agreement."]),
    ("These apples ______ sweet.", ["is", "am", "are", "be"], "A", "These apples is plural, so the correct present be form is are.", "看到 these 加複數名詞時，先判斷主詞為複數。", ["Identify the subject These apples.", "Notice the plural noun apples.", "Choose the plural be form.", "Select are.", "Check that is and am do not agree with a plural subject."]),
    ("Ella ______ tennis every Saturday.", ["play", "plays", "playing", "to play"], "A", "Ella is third-person singular, and a repeated Saturday activity takes the simple present plays.", "由時間頻率判斷現在簡單式，再處理第三人稱單數。", ["Notice every Saturday as a repeated habit.", "Choose the simple present tense.", "Identify Ella as third-person singular.", "Add s to play.", "Choose plays."]),
    ("______ you have a library card?", ["Is", "Are", "Do", "Does"], "A", "The main verb have is an ordinary verb and the subject you takes the auxiliary Do in a present question.", "先分辨一般動詞和 be 動詞，再配合主詞選助動詞。", ["Find the main verb have.", "Recognize that the sentence is not using be.", "Identify the subject you.", "Choose Do for a present question.", "Keep have in its base form after Do."]),
    ("We ______ not watch TV before finishing our homework.", ["does", "do", "are", "is"], "A", "We uses do in the present negative, so the sentence begins We do not watch.", "主詞 we 配 do，否定句用 do not 加原形動詞。", ["Identify the subject We.", "Recognize watch as an ordinary verb.", "Choose do for this subject.", "Add not after do.", "Keep watch in the base form."]),
    ("Where ______ your parents work?", ["do", "does", "is", "are"], "A", "Your parents is plural and work is an ordinary verb, so the question uses do.", "疑問詞後先檢查主詞單複數，再判斷一般動詞助動詞。", ["Find the subject your parents.", "Classify it as plural.", "Identify work as an ordinary verb.", "Choose do.", "Keep work unchanged after the auxiliary."]),
    ("Tom and I ______ going to the museum tomorrow.", ["am", "is", "are", "be"], "A", "Tom and I means we, so the present progressive form is are going.", "並列主詞視為複數，再用 be 加 V-ing 表示計畫或進行。", ["Combine Tom and I as a plural subject.", "Notice the -ing word going.", "Choose the plural be form.", "Select are.", "Read are going to confirm the pattern."]),
    ("There ______ two computers in the room.", ["is", "am", "are", "be"], "A", "The noun two computers is plural, so the existential pattern takes are.", "There be 句型要看後面的真正名詞單複數。", ["Find the noun after the blank.", "Notice the quantity two computers.", "Classify the noun as plural.", "Choose are.", "Check that is would fit one computer, not two."]),
    ("This is my jacket. ______ is blue.", ["He", "She", "It", "They"], "A", "A jacket is a singular thing, so the subject pronoun is It.", "先確認代替對象是人或物，再判斷單複數。", ["Identify what the pronoun replaces: jacket.", "Classify it as a singular object.", "Choose the singular non-human pronoun.", "Select It.", "Check that He and She refer to people and They is plural."]),
    ("I was hungry, ______ I made a sandwich.", ["but", "so", "or", "because"], "A", "Being hungry is the reason and making a sandwich is the result, so so connects them.", "判斷前後句是原因、結果、轉折或選擇，再選連接詞。", ["Read both clauses.", "Identify hungry as the situation.", "Identify making a sandwich as the result.", "Choose so.", "Reject but, or and because because they express other relations here."]),
]

assert len(DATA) == 10
TARGETS = ["A", "B", "C", "D", "B", "C", "D", "A", "B", "C"]
for i, (prompt, options, answer, explanation, strategy, steps) in enumerate(DATA, 1):
    target = TARGETS[i - 1]
    if target != answer:
        oi, ti = ord(answer) - 65, ord(target) - 65
        correct = options[oi]
        rest = [v for j, v in enumerate(options) if j != oi]
        options = rest[:ti] + [correct] + rest[ti:]
        answer = target
    item = {"id": f"question-english-content-ad-iv-1-{i}", "subject": "english", "type": "single-choice", "prompt": prompt, "options": [{"id": chr(65+j), "text": t} for j, t in enumerate(options)], "knowledgeIds": ["kg-english-content-ad-iv-1"], "difficulty": "medium", "answer": {"value": answer, "explanation": explanation}, "provenance": {"origin": "original", "license": "All rights reserved", "sourceUrl": SOURCES[0][0], "sourceLocator": "公立學校七年級英語段考；只研究基本句型、主詞動詞一致、疑問否定、代名詞與連接詞題型。", "authoringNote": "依官方英語文領域課綱、單元 KG 與三個公立學校公開來源，獨立改寫國中文法句型題；未複製原文、選項、篇章、圖片或答案；待第二輪 AI／Terra 內容複核。"}, "reviewStatus": "draft", "updatedAt": "2026-09-13", "lessonId": LESSON, "examPatternRefs": refs(), "solutionStrategy": strategy, "solutionSteps": steps}
    (OUT / f"question-english-content-ad-iv-1-{i}.json").write_text(json.dumps(item, ensure_ascii=False, indent=2) + "\n", encoding="utf-8")
print(f"rewrote {len(DATA)} independent questions for {LESSON}")
