import json
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
OUT = ROOT / "questions/english"
SOURCES = [
    ("https://www.yacjh.kh.edu.tw/upload/221/101_30637/114%E4%B8%8B%E5%AD%B8%E6%9C%9F%E7%AC%AC%E4%B8%80%E6%AC%A1%E6%AE%B5%E8%80%83%E4%B8%89%E5%B9%B4%E7%B4%9A%E8%8B%B1%E6%96%87.pdf", "高雄市立鹽埕國民中學公開英文段考", "songs, rhyme, rhythm, and sound patterns"),
    ("https://www.bhjh.ntpc.edu.tw/p/406-1000-10627%2Cr111.php?Lang=zh-tw", "新北市立北投國民中學公開定期評量試題頁", "short verse, pronunciation, and listening clues"),
    ("https://www.hcjh.ntpc.edu.tw/p/406-1000-7527%2Cr146.php", "新北市立新埔國民中學公開段考試題頁", "language form, stress, and contextual performance"),
]

DATA = [
    ("end rhyme", "Read the line pair: 'The bright kite flies high / It dances in the sky.' Which words rhyme?", ["bright and dances", "kite and high", "flies and in", "the and sky"], "B", "Kite and high share the same final sound in this line pair, making them the rhyming words."),
    ("syllable count", "Which word has two syllables?", ["rain", "sunshine", "cloud", "wind"], "B", "Sun-shine has two spoken parts, while rain, cloud, and wind each have one syllable."),
    ("rhythm pattern", "A chant repeats 'Clap, clap, step, stop' on every line. What mainly creates its rhythm?", ["A repeated sequence of stressed actions", "A silent paragraph", "Different punctuation in every word", "The number of characters in the title"], "A", "Repeating the action sequence gives listeners a predictable beat and makes the chant easy to perform."),
    ("alliteration", "Which line uses alliteration?", ["Silver snakes slide slowly.", "The bird is in the tree.", "We went home at noon.", "A small boat crossed the lake."], "A", "Silver, snakes, slide, and slowly begin with the repeated /s/ sound, which is alliteration."),
    ("word stress", "In the word 'SUNshine,' which syllable receives the main stress in ordinary pronunciation?", ["sun", "shine", "both equally in every context", "neither syllable"], "A", "The first syllable is stronger in SUNshine, so the main stress falls on sun."),
    ("repeated refrain", "A song ends each verse with the same line, 'We can try again.' What is the function of that repeated line?", ["It creates a refrain that emphasizes the central message.", "It changes the song into a dictionary.", "It removes the rhythm from the song.", "It proves every verse has a different speaker."], "A", "A repeated line is a refrain; its return highlights the message and helps listeners follow the song's structure."),
    ("vowel sound", "Which pair has the same vowel sound in the common pronunciation of 'feet' and 'team'?", ["feet and team", "feet and head", "team and time", "feet and food"], "A", "Feet and team both use the long /iː/ vowel sound in common pronunciation."),
    ("pause and meaning", "A performer pauses after 'When the rain stops' before saying 'we run outside.' What does the pause help listeners hear?", ["The condition comes before its result.", "The speaker has forgotten every word.", "The sentence has no relationship between its parts.", "The rain is a person speaking."], "A", "The pause separates the condition from the result and makes the sentence's sequence easier to follow."),
    ("intonation in a chant", "A question in a playful chant is 'Are you ready?' Which delivery best signals that it is a question?", ["Use a rising intonation toward the end.", "Whisper every syllable with no change.", "Stress only the first word and stop.", "Read it exactly like a finished statement."], "A", "A rising ending commonly signals a yes-no question and invites a response from listeners."),
    ("integrated sound analysis", "A poem uses four short lines, rhymes night/light, repeats 'listen close,' and stresses the first beat of each line. What combination is described?", ["End rhyme, refrain, and a regular rhythmic stress", "Only a silent reading list", "A paragraph with no sound pattern", "A single adjective without a poem"], "A", "Night/light gives end rhyme, listen close is a refrain, and repeated first-beat stress creates regular rhythm."),
]


def make(index, row):
    topic, prompt, choices, answer, explanation = row
    options = [{"id": chr(65 + i), "text": text} for i, text in enumerate(choices)]
    refs = [{"url": url, "title": f"{title}；僅取歌謠韻文音韻與節奏能力方向，未複製原題、選項、圖表或答案。", "year": "113-114", "subject": "english", "locator": locator, "observedPattern": "公開英文評量常以歌謠、韻文、押韻、音節、重音、重複句、語調與聲音辨識測量語音韻律理解；本題為獨立改寫。", "reuseDecision": "pattern-only", "status": "recorded", "locatorLevel": "paper"} for url, title, locator in SOURCES]
    steps = [
        f"Read or say the verse aloud and identify the sound skill: {topic}.",
        "Listen to final sounds, syllable parts, repeated beginnings or lines, stressed beats, pauses, and pitch movement rather than relying only on spelling.",
        f"Compare the choices with the spoken evidence; the correct answer is {answer}.",
        f"Explain the sound pattern: {explanation}",
        "Perform the line again, mark the relevant sound or beat, and check that the explanation names the actual pronunciation or rhythmic feature.",
    ]
    return {"id": f"question-english-performance-1-iv-10-{index}", "subject": "english", "type": "single-choice", "prompt": prompt, "options": options, "knowledgeIds": ["kg-english-performance-1-iv-10"], "difficulty": "medium", "answer": {"value": answer, "explanation": explanation + f" Correct answer: {answer}"}, "provenance": {"origin": "original", "license": "All rights reserved", "sourceUrl": SOURCES[0][0], "sourceLocator": "Public-school English assessment materials; this item studies song, verse, rhythm, stress, and sound patterns only and does not reproduce an original question, option, image, or answer.", "authoringNote": "Written independently from the official English curriculum KG and three public-school English assessment sources; verse lines, options, explanations, and performance tasks are original; pending second-round AI/Terra content review."}, "reviewStatus": "draft", "updatedAt": "2026-09-09", "lessonId": "lesson-english-performance-1-iv-10", "examPatternRefs": refs, "solutionStrategy": "Say the verse aloud, isolate the requested sound or beat, compare pronunciation and position, and explain how the feature supports the song's rhythm or meaning.", "solutionSteps": steps}


for index, row in enumerate(DATA, 1):
    (OUT / f"question-english-performance-1-iv-10-{index}.json").write_text(json.dumps(make(index, row), ensure_ascii=False, indent=2) + "\n", encoding="utf-8")
print(f"rewrote {len(DATA)} questions")
