#!/usr/bin/env python3
"""Independent English Aa-IV-1 upper/lowercase and handwriting rewrite."""
import json
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
OUT = ROOT / "questions/english"
LESSON = "lesson-english-content-aa-iv-1"
SOURCES = [
    ("https://www.kusjh.kh.edu.tw/upload/files/110%E4%B8%8A%E7%AC%AC1%E6%AC%A1%E6%AE%B5%E8%80%83%E5%9C%8B%E4%B8%AD%E4%B8%80%E5%B9%B4%E7%B4%9A%E8%A9%A6%E9%A1%8C.pdf", "高雄市立鼓山高中國中部七年級公開英語段考", "字母大小寫、字母表順序與書寫格式"),
    ("https://www.kcjh.kh.edu.tw/upload/190/104_34764/%E5%9C%8B%E6%98%8C--%E4%B8%80%E5%B9%B4%E7%B4%9A--%E8%8B%B1%E6%96%87%E7%A7%91.pdf", "高雄市立國昌國中七年級公開英語段考", "基礎英語辨識、拼寫與題幹閱讀"),
    ("https://www.dam.kh.edu.tw/upload/68/101_28414/114-1%E4%B8%83%E5%B9%B4%E7%B4%9A%E7%AC%AC%E4%B8%80%E6%AC%A1%E6%AE%B5%E8%80%83%E8%A9%A6%E5%8D%B7%E6%9A%A8%E8%A7%A3%E7%AD%94.pdf", "高雄市立大社國中七年級公開英語段考", "字母與基礎閱讀題型"),
]

def refs():
    return [{"url": u, "title": f"{t}；僅研究公開題型與能力方向，未複製原題。", "year": "110-114", "subject": "english", "locator": l, "observedPattern": "公立學校國中英語評量要求辨認英文字母、大小寫、字母順序、單字開頭與書寫格式；本題採全新字詞與情境。", "reuseDecision": "pattern-only", "status": "recorded", "locatorLevel": "paper"} for u, t, l in SOURCES]

DATA = [
    ("Which choice shows the correct lowercase form of the first letter in **River**?", ["r", "R", "v", "V"], "A", "River begins with uppercase R; its lowercase form is r. The other choices either keep uppercase or use the wrong letter.", "先找目標字母，再區分同一字母的大小寫，不要被後面的字母干擾。", ["Locate the first letter in River.", "Identify it as uppercase R.", "Recall the matching lowercase pair.", "Choose r because it is the same letter in lowercase.", "Check that v/V are different letters, not case forms of R."]),
    ("Which word follows **apple** in alphabetical order?", ["ant", "apron", "banana", "April"], "B", "Compare letters from left to right: ap comes after an, and apron comes after apple because r comes after p at the first differing position.", "逐字母比較，遇到第一個不同字母就決定順序。", ["Write the first letters of all choices.", "Put ant before the words beginning with ap.", "Compare apple and apron after ap.", "Place apron after apple at the first difference.", "Confirm banana and April do not come immediately after apple in this set."]),
    ("A student writes **good morning** as **Goodmorning.** Which correction is needed first?", ["Add a space between Good and morning.", "Change every letter to uppercase.", "Remove the period.", "Change morning to a number."], "A", "The phrase has two words, so the missing space is the first format problem. Capitalization and punctuation can be checked after the word boundary is restored.", "先檢查單字邊界，再檢查大小寫與標點。", ["Read the intended phrase aloud.", "Count the two words: Good and morning.", "Find the missing boundary.", "Insert one space between the words.", "Recheck capitalization and the final period afterward."]),
    ("Which choice uses capitalization most appropriately for a sentence beginning with **my name is Leo.**?", ["my name is Leo.", "My name is Leo.", "MY NAME IS leo.", "My Name Is Leo."], "B", "An English sentence normally begins with a capital letter, while the common words remain lowercase and the proper name Leo stays capitalized.", "先找句首與專有名詞，再避免把每個字都大寫。", ["Locate the beginning of the sentence.", "Capitalize the first word My.", "Keep name is in ordinary lowercase.", "Keep Leo capitalized as a name.", "Choose the complete sentence with normal spacing and punctuation."]),
    ("Which pair contains the same letter in different cases?", ["b and B", "b and d", "M and N", "p and q"], "A", "b and B are the same alphabet letter in lowercase and uppercase; the other pairs contain different letters.", "把字母轉成同一種大小寫後再比對，不用只看外形。", ["Convert the first letter of each pair mentally to lowercase.", "Compare b with B.", "Check whether the remaining pairs become identical.", "Reject pairs that change letter identity.", "Select b and B as the case pair."]),
    ("Which line is written with consistent letter case for a list of classroom labels?", ["Desk, chair, window", "desk, Chair, window", "DESK, chair, Window", "desk, chair, WINDOW"], "A", "The first choice uses the same initial-capital style for every label; the other choices mix styles without a stated reason.", "先找整組標籤的共同格式，再檢查每個詞是否一致。", ["Identify that the items form one list.", "Observe the first-letter pattern in each choice.", "Check whether all three labels follow one style.", "Reject mixed capitalization when no purpose is given.", "Choose Desk, chair, window as the consistent label set."]),
    ("Which option correctly changes **SUN** to lowercase?", ["sun", "sUn", "Sun", "SUN"], "A", "Lowercase means every alphabet letter is written in its lowercase form, so SUN becomes sun.", "逐字檢查每個字母，不要只改第一個字母。", ["Read the three letters S-U-N.", "Change S to s.", "Change U to u.", "Change N to n.", "Confirm the result contains no uppercase letters."]),
    ("A sign should show the place name **Green Park**. Which version preserves the two-word name and clear capitalization?", ["greenpark", "Green park", "Green Park", "GREENpark"], "A", "Green Park has two words and each word begins with a capital in this place name; the other choices lose the space or use inconsistent capitalization.", "先保留字詞邊界，再依名稱的每個主要字詞檢查大小寫。", ["Identify Green Park as a two-word place name.", "Keep one space between Green and Park.", "Capitalize the first letter of Green.", "Capitalize the first letter of Park.", "Choose the version that satisfies both spacing and case."]),
    ("Which choice is the clearest way to copy the letter sequence **q r s**?", ["q r s", "Q r S", "qrs", "q  r   s"], "A", "The target sequence uses lowercase letters separated by single spaces, so the first choice preserves both case and spacing.", "同時核對字母大小寫、順序與空格數量。", ["Read the target sequence from left to right.", "Check that q, r and s are lowercase.", "Check their order.", "Check for one space between adjacent letters.", "Select the exact-format copy q r s."]),
    ("Which correction makes **Welcome, tina!** a properly capitalized greeting?", ["Welcome, Tina!", "welcome, Tina!", "Welcome,Tina!", "WELCOME, tina!"], "A", "Welcome begins the sentence and Tina is a name, so both require capitals; the comma also needs its normal following space.", "把句首、專有名詞、標點後空格分開檢查。", ["Find the sentence-opening word Welcome.", "Find the proper name tina.", "Capitalize both relevant initial letters.", "Check the comma and insert one following space.", "Choose Welcome, Tina! as the complete correction."]),
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
    item = {"id": f"question-english-content-aa-iv-1-{i}", "subject": "english", "type": "single-choice", "prompt": prompt, "options": [{"id": chr(65+j), "text": t} for j, t in enumerate(options)], "knowledgeIds": ["kg-english-content-aa-iv-1"], "difficulty": "easy", "answer": {"value": answer, "explanation": explanation}, "provenance": {"origin": "original", "license": "All rights reserved", "sourceUrl": SOURCES[0][0], "sourceLocator": "公立學校七年級英語段考；只研究字母大小寫、順序、拼寫格式與基礎辨識題型。", "authoringNote": "依官方英語文領域課綱、單元 KG 與三個公立學校公開來源，獨立改寫字母書寫題；未複製原文、選項、篇章、圖片或答案；待第二輪 AI／Terra 內容複核。"}, "reviewStatus": "draft", "updatedAt": "2026-09-13", "lessonId": LESSON, "examPatternRefs": refs(), "solutionStrategy": strategy, "solutionSteps": steps}
    (OUT / f"question-english-content-aa-iv-1-{i}.json").write_text(json.dumps(item, ensure_ascii=False, indent=2) + "\n", encoding="utf-8")
print(f"rewrote {len(DATA)} independent questions for {LESSON}")
