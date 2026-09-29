import json
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
OUT = ROOT / "questions/english"
SOURCES = [
    (
        "https://www.yacjh.kh.edu.tw/upload/221/101_30637/114%E4%B8%8B%E5%AD%B8%E6%9C%9F%E7%AC%AC%E4%B8%80%E6%AC%A1%E6%AE%B5%E8%80%83%E4%B8%89%E5%B9%B4%E7%B4%9A%E8%8B%B1%E6%96%87.pdf",
        "高雄市立鹽埕國民中學公開英文段考",
        "sentence reading, pronunciation cues, and contextual English use",
    ),
    (
        "https://www.bhjh.ntpc.edu.tw/p/406-1000-10627%2Cr111.php?Lang=zh-tw",
        "新北市立北投國民中學公開定期評量試題頁",
        "English listening-and-reading item formats and sentence meaning",
    ),
    (
        "https://www.hcjh.ntpc.edu.tw/p/406-1000-7527%2Cr146.php",
        "新北市立新埔國民中學公開段考試題頁",
        "English sentence patterns, question forms, and contextual application",
    ),
]

DATA = [
    (
        "statement intonation",
        "Which description best matches the natural intonation of the complete statement, 'The bus leaves at six.'?",
        [
            "The voice usually falls at the end because the speaker is giving complete information.",
            "The voice must rise sharply at the end because every sentence is a question.",
            "The voice rises on every word and never signals an ending.",
            "The speaker should stress only the first sound and whisper the final word.",
        ],
        "The voice usually falls at the end because the speaker is giving complete information.",
        "A complete statement commonly uses falling intonation at the end. The fall signals that the information is presented as finished, not that every word has the same pitch.",
    ),
    (
        "yes-no question",
        "Which intonation is most natural for the yes-no question, 'Are you ready?' when the speaker genuinely expects yes or no?",
        [
            "The voice commonly rises at the end to invite the listener's answer.",
            "The voice must fall because all questions end with a fall.",
            "The voice stays completely flat so the question cannot be heard.",
            "The voice rises only on the word you and falls before the question ends.",
        ],
        "The voice commonly rises at the end to invite the listener's answer.",
        "A genuine yes-no question commonly has rising final intonation. The rise helps mark the utterance as open for a response; it is not a rule that every word must rise.",
    ),
    (
        "wh-question",
        "Which description best fits the natural ending of the information question, 'Where did Mia put the key?'?",
        [
            "The voice commonly falls because the speaker is asking for specific information.",
            "The voice must rise as high as possible because Where begins a question.",
            "The voice should stop after Where and ignore the rest of the sentence.",
            "The voice must be louder on every word than in a statement.",
        ],
        "The voice commonly falls because the speaker is asking for specific information.",
        "Wh-questions commonly use falling intonation at the end. The question word identifies the information needed, but it does not require the whole sentence to rise.",
    ),
    (
        "contrastive stress",
        "In the exchange 'I ordered the green notebook, not the blue one,' which word should receive the strongest contrastive stress?",
        [
            "green",
            "the",
            "not",
            "one",
        ],
        "green",
        "Green contrasts with blue, so stressing green makes the correction clear. The word not also carries meaning, but the color pair supplies the specific contrast being corrected.",
    ),
    (
        "content-word stress",
        "If a speaker says 'The small bird found a shiny coin,' which group is most likely to carry the main information stress?",
        [
            "small, bird, shiny, coin",
            "the, a",
            "the, found, a",
            "only found",
        ],
        "small, bird, shiny, coin",
        "Content words such as nouns and meaningful adjectives usually carry more stress than short grammatical articles. The exact focus can shift with context, but the content words carry the scene's main information.",
    ),
    (
        "compound-word stress",
        "Which pronunciation plan is most natural for the compound noun 'GREENhouse' when it means a glass building for plants?",
        [
            "Give the first part stronger stress: GREEN-house.",
            "Give the second part stronger stress: green-HOUSE.",
            "Give exactly equal stress to every sound and erase the word boundary.",
            "Stress only the final /s/ sound.",
        ],
        "Give the first part stronger stress: GREEN-house.",
        "Many compound nouns place stronger stress on the first element. Greenhouse as a plant-growing building is therefore commonly heard as GREEN-house, not green-HOUSE.",
    ),
    (
        "choice-question intonation",
        "Which intonation pattern best completes the choice question, 'Would you like tea or coffee?' when the listener must choose one?",
        [
            "Rise on tea, then fall on coffee.",
            "Fall on tea, then rise on coffee.",
            "Rise equally at the end of both tea and coffee.",
            "Use a flat pitch and stress neither choice.",
        ],
        "Rise on tea, then fall on coffee.",
        "In a choice question, the first alternative often rises and the final alternative falls, showing that the list is complete and the listener should select one option.",
    ),
    (
        "tag question meaning",
        "A speaker says, 'You finished the project, didn't you?' with a falling ending. What attitude is most likely?",
        [
            "The speaker expects agreement and is checking information already believed.",
            "The speaker has no idea and is asking a completely open yes-no question.",
            "The speaker is listing two choices for the listener.",
            "The speaker is changing the meaning of finished to a place name.",
        ],
        "The speaker expects agreement and is checking information already believed.",
        "A falling tag question often shows that the speaker expects the listener to agree or confirm an assumption. A rising tag more often signals genuine uncertainty.",
    ),
    (
        "stress changes focus",
        "In the sentence 'Lena borrowed my dictionary,' which interpretation is highlighted if MY receives the strongest stress?",
        [
            "The dictionary belongs to me rather than to someone else.",
            "Lena, rather than another person, borrowed it.",
            "The action was borrowing rather than buying.",
            "The object was a dictionary rather than a notebook.",
        ],
        "The dictionary belongs to me rather than to someone else.",
        "Contrastive stress directs the listener to the corrected or important element. Stressing my highlights ownership, while stressing Lena, borrowed, or dictionary would shift the focus.",
    ),
    (
        "transfer through delivery",
        "A student reads 'Please close the window.' to a classmate who is far away and cannot see the speaker. Which delivery is clearest?",
        [
            "Stress close and window, use a clear pause after Please, and finish with an appropriately firm falling tone.",
            "Whisper every word with equal pitch so the request sounds like background noise.",
            "Stress only Please and let the voice rise as if offering two choices.",
            "Rush the sentence without a final boundary so the listener must guess the request.",
        ],
        "Stress close and window, use a clear pause after Please, and finish with an appropriately firm falling tone.",
        "A clear request needs prominent content words, a boundary that separates the polite opener from the action, and an ending that signals the request is complete. Delivery should support meaning rather than simply become louder.",
    ),
]


def make_question(index, row):
    tag, prompt, option_texts, answer_text, explanation = row
    options = [{"id": chr(65 + i), "text": text} for i, text in enumerate(option_texts)]
    answer_id = next(option["id"] for option in options if option["text"] == answer_text)
    refs = [
        {
            "url": url,
            "title": f"{title}; pattern-only study, no original item or option copied.",
            "year": "113-114",
            "subject": "english",
            "locator": locator,
            "observedPattern": "Public-school English assessments use sentence-level reading, question forms, contextual meaning, and practical delivery cues; this item independently rewrites the skill focus without copying wording, options, figures, or answers.",
            "reuseDecision": "pattern-only",
            "status": "recorded",
            "locatorLevel": "paper",
        }
        for url, title, locator in SOURCES
    ]
    steps = [
        f"Read the sentence and identify the pronunciation focus: {tag}.",
        f"Mark the words that carry the sentence's meaning and decide whether the utterance is a statement, question, correction, choice, or request; the key principle is: {explanation}",
        f"Check option {answer_id}: {answer_text}",
        "Reject the other options by comparing their stress placement or pitch movement with the sentence purpose, rather than assuming that every question rises or every word receives equal emphasis.",
        "Say the complete sentence aloud once, listen for the final boundary and the focused word, then explain how the delivery changes or preserves the intended meaning.",
    ]
    return {
        "id": f"question-english-content-ab-iv-1-{index}",
        "subject": "english",
        "type": "single-choice",
        "prompt": prompt,
        "options": options,
        "knowledgeIds": ["kg-english-content-ab-iv-1"],
        "difficulty": "medium",
        "answer": {"value": answer_id, "explanation": explanation + f" Correct answer: {answer_text}"},
        "provenance": {
            "origin": "original",
            "license": "All rights reserved",
            "sourceUrl": SOURCES[0][0],
            "sourceLocator": "Public-school English assessment materials; this item studies assessment patterns only and does not reproduce an original question, option, image, or answer.",
            "authoringNote": "Written independently from the official English curriculum KG and three public-school English assessment sources; pronunciation focus, sentence contexts, options, explanation, and transfer task are original; pending second-round AI/Terra content review.",
        },
        "reviewStatus": "draft",
        "updatedAt": "2026-09-09",
        "lessonId": "lesson-english-content-ab-iv-1",
        "examPatternRefs": refs,
        "solutionStrategy": "First classify the utterance's purpose, then locate its information focus and choose the stress and intonation pattern that makes that purpose clear; finally say the whole sentence again to test whether the meaning is signaled.",
        "solutionSteps": steps,
    }


for index, row in enumerate(DATA, 1):
    (OUT / f"question-english-content-ab-iv-1-{index}.json").write_text(
        json.dumps(make_question(index, row), ensure_ascii=False, indent=2) + "\n",
        encoding="utf-8",
    )

print(f"rewrote {len(DATA)} questions")
