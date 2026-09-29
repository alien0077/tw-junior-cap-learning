import json
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
OUT = ROOT / "questions/english"
SOURCES = [
    ("https://www.yacjh.kh.edu.tw/upload/221/101_30637/114%E4%B8%8B%E5%AD%B8%E6%9C%9F%E7%AC%AC%E4%B8%80%E6%AC%A1%E6%AE%B5%E8%80%83%E4%B8%89%E5%B9%B4%E7%B4%9A%E8%8B%B1%E6%96%87.pdf", "高雄市立鹽埕國民中學公開英文段考", "phonics, word recognition, and contextual English use"),
    ("https://www.bhjh.ntpc.edu.tw/p/406-1000-10627%2Cr111.php?Lang=zh-tw", "新北市立北投國民中學公開定期評量試題頁", "English spelling-sound patterns and vocabulary context"),
    ("https://www.hcjh.ntpc.edu.tw/p/406-1000-7527%2Cr146.php", "新北市立新埔國民中學公開段考試題頁", "English word forms, pronunciation, and application"),
]

DATA = [
    ("initial consonant sound", "Which word begins with the same sound as 'city'?", ["circle", "cat", "goat", "ship"], "circle", "City begins with the soft c sound /s/, and circle begins with the same sound. Cat begins with /k/, while goat and ship begin with different consonants."),
    ("silent-e pattern", "Which word has the same long-vowel spelling pattern as 'home'?", ["hope", "hot", "horse", "house"], "hope", "Home and hope use a final silent e to signal a long o sound. Hot has a short o sound, and horse and house follow different vowel patterns."),
    ("vowel team", "Which word contains the same vowel sound as 'team'?", ["dream", "bread", "head", "great"], "dream", "Team and dream use ea for the long /iː/ sound. Bread and head use a short /e/ sound, while great commonly has /eɪ/."),
    ("consonant digraph", "Which word begins with the same two-letter sound as 'ship'?", ["sheep", "skip", "sip", "chip"], "sheep", "Ship and sheep begin with the digraph sh, which represents one /ʃ/ sound. Skip and sip begin with /s/, while chip begins with ch."),
    ("consonant blend", "In which word can both consonant sounds in the opening blend be heard?", ["flag", "phone", "chair", "knee"], "flag", "Flag begins with fl, and both /f/ and /l/ can be heard. Ph, ch, and kn are digraph or silent-letter patterns rather than a two-sound opening blend in these choices."),
    ("past-tense ending", "Which word most likely pronounces the -ed ending as a separate syllable?", ["wanted", "washed", "jumped", "laughed"], "wanted", "Wanted ends with /ɪd/, so -ed creates an extra syllable. The other choices normally pronounce -ed as /t/ rather than a separate syllable."),
    ("plural ending", "Which word has a plural ending pronounced /ɪz/?", ["boxes", "books", "cups", "maps"], "boxes", "Boxes ends in a hissing sound, so the plural -es is pronounced /ɪz/. The other plurals end with /s/ in these examples."),
    ("silent letter", "Which word contains a silent initial letter?", ["knife", "kind", "kite", "king"], "knife", "The k in knife is silent, so the word begins with /n/. The k is pronounced in kind, kite, and king."),
    ("syllable division", "Which division best helps a learner read the two-syllable word 'sunset'?", ["sun / set", "s / unse / t", "sunse / t", "su / nset"], "sun / set", "Sunset is a compound word made from sun and set. Dividing it into those meaningful parts supports both pronunciation and meaning."),
    ("transfer by pattern", "A learner knows how to read 'rain.' Which new word can be decoded most directly by applying the same vowel-team pattern?", ["train", "ran", "ring", "round"], "train", "Rain and train share the ai spelling for the long /eɪ/ sound. The other choices require different vowel patterns, so the known pattern transfers most directly to train."),
]


def make(index, row):
    tag, prompt, choices, answer, explanation = row
    options = [{"id": chr(65 + i), "text": text} for i, text in enumerate(choices)]
    answer_id = next(option["id"] for option in options if option["text"] == answer)
    refs = [{
        "url": url, "title": f"{title}; pattern-only study, no original item or option copied.", "year": "113-114", "subject": "english", "locator": locator,
        "observedPattern": "Public-school English assessments use spelling-sound recognition, word forms, vocabulary context, and reading transfer; this is an independent rewrite of those ability patterns without copying wording, options, figures, or answers.",
        "reuseDecision": "pattern-only", "status": "recorded", "locatorLevel": "paper"
    } for url, title, locator in SOURCES]
    steps = [
        f"Read the word task and identify the phonics focus: {tag}.",
        f"Say the target word slowly, mark the letter pattern and its sound, and apply this rule: {explanation}",
        f"Check option {answer_id}: {answer}",
        "Reject the alternatives by comparing the actual spoken sound and letter pattern, not by choosing words that merely share a letter or look similar.",
        "Read the selected word in the complete context, verify the sound one more time, and explain how the pattern can help decode another unfamiliar word.",
    ]
    return {
        "id": f"question-english-content-ab-iv-3-{index}", "subject": "english", "type": "single-choice", "prompt": prompt,
        "options": options, "knowledgeIds": ["kg-english-content-ab-iv-3"], "difficulty": "medium",
        "answer": {"value": answer_id, "explanation": explanation + f" Correct answer: {answer}"},
        "provenance": {"origin": "original", "license": "All rights reserved", "sourceUrl": SOURCES[0][0], "sourceLocator": "Public-school English assessment materials; this item studies assessment patterns only and does not reproduce an original question, option, image, or answer.", "authoringNote": "Written independently from the official English curriculum KG and three public-school English assessment sources; phonics focus, word contexts, options, explanation, and transfer task are original; pending second-round AI/Terra content review."},
        "reviewStatus": "draft", "updatedAt": "2026-09-09", "lessonId": "lesson-english-content-ab-iv-3", "examPatternRefs": refs,
        "solutionStrategy": "Map letters to sounds in small chunks, test the pattern in the whole word, and transfer only the sound-spelling relationship that is actually shared.", "solutionSteps": steps,
    }


for index, row in enumerate(DATA, 1):
    (OUT / f"question-english-content-ab-iv-3-{index}.json").write_text(json.dumps(make(index, row), ensure_ascii=False, indent=2) + "\n", encoding="utf-8")
print(f"rewrote {len(DATA)} questions")
