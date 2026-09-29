#!/usr/bin/env python3
"""Independent English Ab-IV-2 rhyme, rhythm and sound rewrite."""
import json
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
OUT = ROOT / "questions/english"
LESSON = "lesson-english-content-ab-iv-2"
SOURCES = [
    ("https://www.kusjh.kh.edu.tw/upload/files/110%E4%B8%8A%E7%AC%AC1%E6%AC%A1%E6%AE%B5%E8%80%83%E5%9C%8B%E4%B8%AD%E4%B8%80%E5%B9%B4%E7%B4%9A%E8%A9%A6%E9%A1%8C.pdf", "高雄市立鼓山高中國中部七年級公開英語段考", "基礎英語聽辨與字詞聲音"),
    ("https://www.kcjh.kh.edu.tw/upload/190/104_34764/%E5%9C%8B%E6%98%8C--%E4%B8%80%E5%B9%B4%E7%B4%9A--%E8%8B%B1%E6%96%87%E7%A7%91.pdf", "高雄市立國昌國中七年級公開英語段考", "韻文、聽力與語音辨識"),
    ("https://www.dam.kh.edu.tw/upload/68/101_28414/114-1%E4%B8%83%E5%B9%B4%E7%B4%9A%E7%AC%AC%E4%B8%80%E6%AC%A1%E6%AE%B5%E8%80%83%E8%A9%A6%E5%8D%B7%E6%9A%A8%E8%A7%A3%E7%AD%94.pdf", "高雄市立大社國中七年級公開英語段考", "基礎音韻、拼讀與聽辨題型"),
]

def refs():
    return [{"url": u, "title": f"{t}；僅研究公開題型與能力方向，未複製原題。", "year": "110-114", "subject": "english", "locator": l, "observedPattern": "公立學校國中英語評量要求從歌謠、韻文與聽辨活動判斷押韻、節奏、音節及字詞開頭聲音；本題採全新字詞與句子。", "reuseDecision": "pattern-only", "status": "recorded", "locatorLevel": "paper"} for u, t, l in SOURCES]

DATA = [
    ("Which word rhymes with **light**?", ["late", "night", "let", "lot"], "B", "light and night share the final /aɪt/ sound, so they rhyme. Similar spelling alone is not enough.", "比較字尾的發音，不只看字母拼法。", ["Say light aloud.", "Listen to the final stressed sound.", "Say each option aloud.", "Match night because its ending sound is /aɪt/.", "Reject late even though its spelling begins similarly."]),
    ("Which pair begins with the same sound?", ["sun / soup", "cat / city", "go / giant", "ship / sip"], "A", "sun and soup both begin with the /s/ sound; the other pairs begin with different consonant sounds.", "先只聽字首音，再忽略字母外形與字義。", ["Say the first word in each pair.", "Isolate the first sound.", "Compare it with the second word.", "Choose sun and soup for /s/.", "Check that spelling alone did not decide the answer."]),
    ("In a chant with four beats, which line fits the same beat pattern as **Clap your hands now**?", ["Clap / your / hands / now", "Clap your hands / now / everyone", "Everyone clap your hands now", "Your hands are clapping now"], "A", "The first choice has four clear one-beat words, matching the four-beat pattern most directly.", "把句子拆成可拍手的重讀單位，再比較節拍數。", ["Read the model line with one clap per beat.", "Count its four main words.", "Read every option at a steady pace.", "Choose the line with the same four-beat shape.", "Notice that extra unstressed words can change the rhythm."]),
    ("Which pair has the same ending sound in this short rhyme?", ["play / day", "book / back", "fish / face", "rain / run"], "A", "play and day both end with the /eɪ/ sound, so they form a rhyme.", "把注意力放在最後的重讀音節與母音音質。", ["Say both words slowly.", "Ignore their first consonants.", "Compare the final vowel and ending sound.", "Select play and day.", "Check that book/back differ in the final vowel sound."]),
    ("In this classroom chant, which word has two syllables?", ["sun", "green", "happy", "fish"], "C", "happy is commonly pronounced with two syllables, hap-py; the other choices have one syllable.", "用自然口語拍手或下巴動作數音節。", ["Say each word at normal speed.", "Count the vowel beats you hear.", "Split happy as hap-py.", "Confirm the other choices have one beat.", "Choose happy as the two-syllable word."]),
    ("A poem repeats **go, go, go** at the start of each line. What does the repetition mainly help create?", ["A steady rhythm and memorable pattern", "A change from English to Chinese", "A silent pause after every word", "A new spelling rule"], "A", "Repeating the same short word gives listeners a predictable beat and makes the chant easier to remember.", "觀察重複字詞如何影響節奏與記憶，而非把它當成拼字規則。", ["Locate the repeated word.", "Read the line several times with a beat.", "Notice the predictable timing.", "Connect that timing to memorability.", "Choose the rhythm-and-pattern explanation."]),
    ("Which word has the same vowel sound as **cake**?", ["make", "back", "kick", "cook"], "A", "cake and make share the long /eɪ/ vowel sound; the other choices use different vowel sounds.", "先讀出目標字，再比較核心母音，不被字尾 k 迷惑。", ["Say cake clearly.", "Identify its main vowel sound /eɪ/.", "Say each choice.", "Match make with the same vowel sound.", "Check that back has a short /æ/ sound."]),
    ("When students clap on the strong beats of **We PLAY in the PARK**, which words should receive the clearest claps?", ["we / in", "play / park", "the / the", "all words equally"], "B", "Content words play and park carry the main meaning and are naturally more prominent than the small function words.", "找出內容詞與功能詞，再把節拍放在主要資訊。", ["Read the phrase naturally.", "Identify the action and place words.", "Separate them from we, in and the.", "Clap more clearly on play and park.", "Explain why equal stress would sound less natural."]),
    ("Which line is easiest to make into a simple rhyme with **The cat sat**?", ["The cat sat on a mat.", "The cat is very happy today.", "The cat can run to school.", "The cat looks at the moon."], "A", "cat, sat and mat repeat the /æt/ ending, creating a clear and simple rhyme pattern.", "找出重複的字尾音，再確認句意仍然自然。", ["Say cat and sat aloud.", "Identify the shared /æt/ sound.", "Read each line ending.", "Choose the line ending in mat.", "Confirm that the repeated sound occurs at the line endings."]),
    ("A learner confuses **ship** and **sheep** in a song. What should the learner compare first?", ["The vowel sound in the middle", "The number of letters only", "The meaning of the whole song", "The capital letters"], "A", "ship has a short /ɪ/ sound while sheep has a long /iː/ sound, so the vowel contrast is the key listening clue.", "先鎖定最可能造成差異的音位，再用成對字詞聽辨。", ["Say ship and sheep slowly.", "Hold the middle vowel sound.", "Compare short /ɪ/ with long /iː/.", "Listen for that contrast in the song.", "Use the vowel difference rather than spelling length as the clue."]),
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
    item = {"id": f"question-english-content-ab-iv-2-{i}", "subject": "english", "type": "single-choice", "prompt": prompt, "options": [{"id": chr(65+j), "text": t} for j, t in enumerate(options)], "knowledgeIds": ["kg-english-content-ab-iv-2"], "difficulty": "easy", "answer": {"value": answer, "explanation": explanation}, "provenance": {"origin": "original", "license": "All rights reserved", "sourceUrl": SOURCES[0][0], "sourceLocator": "公立學校七年級英語段考；只研究歌謠韻文、節奏、押韻、音節與音韻聽辨題型。", "authoringNote": "依官方英語文領域課綱、單元 KG 與三個公立學校公開來源，獨立改寫歌謠韻文與音韻題；未複製原文、選項、篇章、圖片或答案；待第二輪 AI／Terra 內容複核。"}, "reviewStatus": "draft", "updatedAt": "2026-09-13", "lessonId": LESSON, "examPatternRefs": refs(), "solutionStrategy": strategy, "solutionSteps": steps}
    (OUT / f"question-english-content-ab-iv-2-{i}.json").write_text(json.dumps(item, ensure_ascii=False, indent=2) + "\n", encoding="utf-8")
print(f"rewrote {len(DATA)} independent questions for {LESSON}")
