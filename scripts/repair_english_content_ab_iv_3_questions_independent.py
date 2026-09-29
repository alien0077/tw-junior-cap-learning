#!/usr/bin/env python3
"""Independent English Ab-IV-3 phonics-rule rewrite."""
import json
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
OUT = ROOT / "questions/english"
LESSON = "lesson-english-content-ab-iv-3"
SOURCES = [
    ("https://www.kusjh.kh.edu.tw/upload/files/110%E4%B8%8A%E7%AC%AC1%E6%AC%A1%E6%AE%B5%E8%80%83%E5%9C%8B%E4%B8%AD%E4%B8%80%E5%B9%B4%E7%B4%9A%E8%A9%A6%E9%A1%8C.pdf", "高雄市立鼓山高中國中部七年級公開英語段考", "字母拼讀、單字與聲音辨識"),
    ("https://www.kcjh.kh.edu.tw/upload/190/104_34764/%E5%9C%8B%E6%98%8C--%E4%B8%80%E5%B9%B4%E7%B4%9A--%E8%8B%B1%E6%96%87%E7%A7%91.pdf", "高雄市立國昌國中七年級公開英語段考", "字音、拼字與基礎閱讀"),
    ("https://www.dam.kh.edu.tw/upload/68/101_28414/114-1%E4%B8%83%E5%B9%B4%E7%B4%9A%E7%AC%AC%E4%B8%80%E6%AC%A1%E6%AE%B5%E8%80%83%E8%A9%A6%E5%8D%B7%E6%9A%A8%E8%A7%A3%E7%AD%94.pdf", "高雄市立大社國中七年級公開英語段考", "拼讀規則與聽辨題型"),
]

def refs():
    return [{"url": u, "title": f"{t}；僅研究公開題型與能力方向，未複製原題。", "year": "110-114", "subject": "english", "locator": l, "observedPattern": "公立學校國中英語評量要求依字母與字母組合推讀常見字音、辨識短母音與子音及用拼讀規則解碼新字；本題採全新字詞。", "reuseDecision": "pattern-only", "status": "recorded", "locatorLevel": "paper"} for u, t, l in SOURCES]

DATA = [
    ("Which word has the short /æ/ sound as in **cat**?", ["map", "make", "me", "moon"], "A", "map has the short /æ/ vowel sound like cat; make has a long vowel and the other choices use different vowels.", "先找目標母音音，再比較每個選項的核心母音。", ["Say cat and isolate /æ/.", "Read each option aloud.", "Listen to the vowel in map.", "Match map with the short /æ/ sound.", "Reject make because the silent e changes the vowel."]),
    ("In the word **ship**, what sound does **sh** usually represent?", ["/s/", "/ʃ/", "/tʃ/", "/k/"], "B", "The letter pair sh commonly represents the /ʃ/ sound at the beginning of ship.", "把兩個字母視為一個常見字母組合，再讀整個字。", ["Locate the initial pair sh.", "Recall the common sound for sh.", "Say ship slowly.", "Match sh with /ʃ/.", "Compare it with single s, which has a different sound here."]),
    ("Which word follows a common short-vowel pattern like **hop**?", ["hope", "hot", "home", "horse"], "C", "hot has a consonant-short vowel-consonant pattern with the short /ɒ/ or /ɑ/ sound, while silent e changes hope and home.", "先辨認子音—短母音—子音的結構，再排除 silent e。", ["Break hop into beginning consonant, vowel and ending consonant.", "Check each option for the same short pattern.", "Notice hot has one medial short vowel.", "Choose hot.", "Explain why hope and home have final silent e."]),
    ("Which word uses a final silent **e** to make the vowel sound long?", ["kit", "kite", "rid", "plan"], "B", "In kite, the final e is not pronounced but helps i say its long /aɪ/ sound.", "先找字尾 e，再比較去掉 e 前後的母音變化。", ["Read each word and mark the final letter.", "Find the word ending in silent e.", "Compare kit and kite as a useful pair.", "Identify the long vowel in kite.", "Choose kite because final e changes the vowel without adding a syllable."]),
    ("Which beginning sound is shared by **chair** and **chicken**?", ["/ʃ/", "/tʃ/", "/k/", "/j/"], "C", "Both words begin with the common ch sound /tʃ/ in these examples.", "辨認字首組合 ch 的常見音，再用兩個詞交叉確認。", ["Say chair clearly.", "Say chicken clearly.", "Compare the first sound of both words.", "Match it to /tʃ/.", "Do not choose /k/, which can occur with c in other patterns."]),
    ("Which word has the long **o** sound in this set?", ["not", "rock", "note", "stop"], "D", "note uses the final silent e pattern to give o a long sound; the other choices have short o in common pronunciation.", "找出母音與字尾 e 的關係，再比較短母音與長母音。", ["Read all four words.", "Locate the word ending in silent e.", "Listen to the vowel in note.", "Identify its long o sound.", "Compare it with short o in not, rock and stop."]),
    ("A learner sees the new word **flim**. Which decoding step is most useful first?", ["Break it into the beginning blend fl, vowel i and final m.", "Guess from the length only.", "Ignore every consonant.", "Read only the final letter."], "A", "Dividing the word into a beginning blend, a vowel and a final consonant applies phonics systematically instead of guessing from appearance.", "由字首組合、核心母音、字尾音逐段拼合，不靠字形猜答案。", ["Mark the initial consonant blend fl.", "Identify the middle vowel i.", "Identify the final consonant m.", "Blend the sounds from left to right.", "Check the result against the surrounding sentence if one is provided."]),
    ("Which pair shows a consonant blend in which both consonant sounds can be heard?", ["stop", "ship", "chat", "thin"], "A", "stop begins with the blend st, and both /s/ and /t/ are heard; sh, ch and th are digraphs representing one combined sound in these examples.", "區分 blend（兩個音都聽見）和 digraph（兩字母合成一音）。", ["Say the beginning of each word slowly.", "Count the consonant sounds, not just letters.", "Listen for /s/ and /t/ in stop.", "Choose stop as the consonant blend.", "Compare it with sh, ch and th as common digraphs."]),
    ("Which word can be decoded with the common **ee** long-vowel pattern?", ["green", "great", "bread", "head"], "B", "green contains ee, which commonly represents the long /iː/ sound; the other choices use different vowel spellings.", "先找字母組合 ee，再確認它在詞中的母音音值。", ["Locate ee in the options.", "Say green aloud.", "Identify the long /iː/ sound.", "Choose green.", "Avoid choosing words whose ea spelling follows a different pattern in this set."]),
    ("When reading **sunset**, which strategy is most helpful?", ["Blend each syllable or word part, sun + set, then check the combined meaning.", "Read only the first letter.", "Treat it as an unrelated single sound.", "Skip the second part."], "C", "sunset is a compound word, so reading sun and set separately and blending them helps both pronunciation and meaning.", "先分解複合字，再拼讀各部分並合併意義。", ["Notice that sunset contains two familiar parts.", "Read sun.", "Read set.", "Join the two parts smoothly.", "Check that the combined meaning fits the word sunset."]),
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
    item = {"id": f"question-english-content-ab-iv-3-{i}", "subject": "english", "type": "single-choice", "prompt": prompt, "options": [{"id": chr(65+j), "text": t} for j, t in enumerate(options)], "knowledgeIds": ["kg-english-content-ab-iv-3"], "difficulty": "easy", "answer": {"value": answer, "explanation": explanation}, "provenance": {"origin": "original", "license": "All rights reserved", "sourceUrl": SOURCES[0][0], "sourceLocator": "公立學校七年級英語段考；只研究短母音、字母組合、silent e、blend、digraph 與複合字拼讀題型。", "authoringNote": "依官方英語文領域課綱、單元 KG 與三個公立學校公開來源，獨立改寫字母拼讀規則題；未複製原文、選項、篇章、圖片或答案；待第二輪 AI／Terra 內容複核。"}, "reviewStatus": "draft", "updatedAt": "2026-09-13", "lessonId": LESSON, "examPatternRefs": refs(), "solutionStrategy": strategy, "solutionSteps": steps}
    (OUT / f"question-english-content-ab-iv-3-{i}.json").write_text(json.dumps(item, ensure_ascii=False, indent=2) + "\n", encoding="utf-8")
print(f"rewrote {len(DATA)} independent questions for {LESSON}")
