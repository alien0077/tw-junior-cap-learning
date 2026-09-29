import json
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
OUT = ROOT / "questions/english"
SOURCES = [
    ("https://www.yacjh.kh.edu.tw/upload/221/101_30637/114%E4%B8%8B%E5%AD%B8%E6%9C%9F%E7%AC%AC%E4%B8%80%E6%AC%A1%E6%AE%B5%E8%80%83%E4%B8%89%E5%B9%B4%E7%B4%9A%E8%8B%B1%E6%96%87.pdf", "高雄市立鹽埕國民中學公開英文段考", "rhyming, reading aloud, and contextual English use"),
    ("https://www.bhjh.ntpc.edu.tw/p/406-1000-10627%2Cr111.php?Lang=zh-tw", "新北市立北投國民中學公開定期評量試題頁", "English sound patterns, vocabulary, and sentence reading"),
    ("https://www.hcjh.ntpc.edu.tw/p/406-1000-7527%2Cr146.php", "新北市立新埔國民中學公開段考試題頁", "English pronunciation, word recognition, and contextual application"),
]

DATA = [
    ("end rhyme", "Which word rhymes with 'light' in the line 'We see a bright light'?", ["night", "late", "let", "long"], "night", "Night and light share the same stressed ending sound /aɪt/. Similar spelling alone is not enough; late, let, and long end with different sounds."),
    ("rhyme versus spelling", "Which pair rhymes even though the spellings are different?", ["blue / shoe", "rough / cough", "head / hide", "food / good"], "blue / shoe", "Blue and shoe both end with the /uː/ sound. The letters do not have to look identical for the spoken endings to rhyme."),
    ("syllable count", "How many syllables are in the word 'banana' when it is spoken naturally?", ["three", "one", "two", "four"], "three", "Banana is commonly divided as ba-na-na, so it has three spoken beats or syllables. Count sound units, not letters."),
    ("strong beat", "In the chant 'CLAP your HANDS and STAMP your FEET,' which words should receive the strongest beats?", ["clap, hands, stamp, feet", "your, and, your", "only and", "every sound equally"], "clap, hands, stamp, feet", "The action words carry the chant's main meaning and naturally receive the prominent beats; short connecting words usually fit between them."),
    ("alliteration", "Which line uses alliteration most clearly?", ["Seven small shells shine.", "The moon is bright tonight.", "A bird flew over the lake.", "We walked home after lunch."], "Seven small shells shine.", "Seven, small, shells, and shine repeat the initial /s/ sound. Alliteration concerns repeated beginning sounds, not merely repeated letters anywhere in a line."),
    ("rhythm adjustment", "A chant sounds crowded in 'Take the red bus to school today.' Which change best keeps the meaning while making the beat easier to follow?", ["Pause slightly after bus and stress red, bus, school, and today.", "Say every word faster with equal stress.", "Remove school and today even though they carry the destination and time.", "Whisper red and bus so the line has no clear beat."], "Pause slightly after bus and stress red, bus, school, and today.", "A short boundary and meaningful beat points make a line easier to perform without removing important information or forcing every word to be equally strong."),
    ("vowel sound", "Which word has the same main vowel sound as 'rain' in this sound-focused rhyme activity?", ["train", "ran", "ring", "round"], "train", "Rain and train share the long /eɪ/ vowel sound. The task asks for the spoken vowel, so the first letter is not the deciding test."),
    ("line ending", "A four-line poem ends with day, play, moon, and tune. Which pattern does it show?", ["The first two lines rhyme and the last two lines rhyme.", "All four lines must rhyme with one another.", "Only the first and third lines rhyme.", "No lines rhyme because the words have different spellings."], "The first two lines rhyme and the last two lines rhyme.", "Day/play form one rhyme pair, and moon/tune form another. A poem can use paired rhymes without making every line share one ending."),
    ("stress in a word", "Which syllable is normally stronger in the noun 'TAble'?", ["the first syllable", "the second syllable", "both syllables equally", "neither syllable"], "the first syllable", "The common noun table is pronounced with stronger stress on the first syllable: TA-ble. Stress is a prominence pattern, not simply a louder final letter."),
    ("integrated performance", "A student must perform the couplet 'The tiny kite can fly / Across the evening sky.' Which plan is clearest?", ["Keep a steady beat, stress tiny, kite, fly, evening, and sky, and let fly/sky form the end rhyme.", "Stress every article and ignore the line endings.", "Change sky to a word that does not rhyme so the lines sound less predictable.", "Read both lines without a pause or any change in prominence."], "Keep a steady beat, stress tiny, kite, fly, evening, and sky, and let fly/sky form the end rhyme.", "A good performance coordinates rhythm, meaningful stress, a line boundary, and the repeated /aɪ/ ending in fly and sky. These features work together to make the verse intelligible."),
]


def make(index, row):
    tag, prompt, choices, answer, explanation = row
    options = [{"id": chr(65 + i), "text": text} for i, text in enumerate(choices)]
    answer_id = next(option["id"] for option in options if option["text"] == answer)
    refs = [{
        "url": url, "title": f"{title}; pattern-only study, no original item or option copied.", "year": "113-114", "subject": "english", "locator": locator,
        "observedPattern": "Public-school English assessments use sound recognition, vocabulary context, sentence reading, and practical language tasks; this is an independent rewrite of the skill pattern without copying wording, options, figures, or answers.",
        "reuseDecision": "pattern-only", "status": "recorded", "locatorLevel": "paper"
    } for url, title, locator in SOURCES]
    steps = [
        f"Read the verse or sound task and identify the focus: {tag}.",
        f"Say the relevant word or line aloud, mark the ending sound, syllable beat, initial sound, or prominent word, and apply this rule: {explanation}",
        f"Check option {answer_id}: {answer}",
        "Reject the other options by comparing spoken sounds and beat placement, not by counting letters or assuming that every line must use the same pattern.",
        "Perform or reread the complete line, listen for the intended sound relationship and rhythm, then explain how the selected feature supports meaning and fluency.",
    ]
    return {
        "id": f"question-english-content-ab-iv-2-{index}", "subject": "english", "type": "single-choice", "prompt": prompt,
        "options": options, "knowledgeIds": ["kg-english-content-ab-iv-2"], "difficulty": "medium",
        "answer": {"value": answer_id, "explanation": explanation + f" Correct answer: {answer}"},
        "provenance": {"origin": "original", "license": "All rights reserved", "sourceUrl": SOURCES[0][0], "sourceLocator": "Public-school English assessment materials; this item studies assessment patterns only and does not reproduce an original question, option, image, or answer.", "authoringNote": "Written independently from the official English curriculum KG and three public-school English assessment sources; sound focus, verse contexts, options, explanation, and transfer task are original; pending second-round AI/Terra content review."},
        "reviewStatus": "draft", "updatedAt": "2026-09-09", "lessonId": "lesson-english-content-ab-iv-2", "examPatternRefs": refs,
        "solutionStrategy": "Listen before looking at spelling: identify the sound or beat relationship, connect it to the line's meaning, and then reread or perform the verse to verify the pattern.", "solutionSteps": steps,
    }


for index, row in enumerate(DATA, 1):
    (OUT / f"question-english-content-ab-iv-2-{index}.json").write_text(json.dumps(make(index, row), ensure_ascii=False, indent=2) + "\n", encoding="utf-8")
print(f"rewrote {len(DATA)} questions")
