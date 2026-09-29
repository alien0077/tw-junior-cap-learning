import json
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
OUT = ROOT / "questions/english"
SOURCES = [
    ("https://www.yacjh.kh.edu.tw/upload/221/101_30637/114%E4%B8%8B%E5%AD%B8%E6%9C%9F%E7%AC%AC%E4%B8%80%E6%AC%A1%E6%AE%B5%E8%80%83%E4%B8%89%E5%B9%B4%E7%B4%9A%E8%8B%B1%E6%96%87.pdf", "高雄市立鹽埕國民中學公開英文段考", "songs, simple verse, and main-idea reading"),
    ("https://www.bhjh.ntpc.edu.tw/p/406-1000-10627%2Cr111.php?Lang=zh-tw", "新北市立北投國民中學公開定期評量試題頁", "short texts, sequence, detail, and inference"),
    ("https://www.hcjh.ntpc.edu.tw/p/406-1000-7527%2Cr146.php", "新北市立新埔國民中學公開段考試題頁", "purpose, mood, audience, and contextual response"),
]

DATA = [
    ("main idea", "Verse: 'Pack a seed and take a spade, / Help the little garden grow. / Share the sun and share the shade; / Watch the green leaves show.' What is the main idea?", ["Working together can help a garden grow.", "Buying the most expensive tools", "Walking alone in a dark cave", "Winning a running race"], "A", "The lines repeatedly connect sharing tools, sunlight, and care with helping the garden grow."),
    ("best title", "Song: 'The morning bell rings clear. / We open books and friends draw near. / A question starts our busy day.' Which title fits best?", ["A Busy Learning Morning", "The Empty Beach", "A Lost Umbrella", "Midnight at the Station"], "A", "The bell, books, friends, and question all describe a school morning focused on learning."),
    ("key detail", "Rhyme: 'Lena feeds the bird at four, / Then she sweeps beside the door.' What does Lena do after feeding the bird?", ["She sweeps beside the door.", "She goes to the store at noon.", "She feeds a fish at five.", "She closes the window at night."], "A", "The second line directly states that Lena sweeps beside the door after feeding the bird."),
    ("sequence", "Song: 'First we choose a bright blue thread. / Next we weave the careful line. / Last we hang the flag overhead.' What happens second?", ["They hang the flag.", "They choose the thread.", "They weave the line.", "They go home before starting."], "C", "The sequence markers show choose first, weave next, and hang last."),
    ("speaker feeling", "Verse: 'My kite fell down beside the tree. / I fixed the string and tried once more. / The wind came back and carried me.' How does the speaker feel at the end?", ["Hopeful and pleased", "Angry at every friend", "Sleepy and confused", "Afraid of all trees"], "A", "The speaker tries again and succeeds when the wind returns, supporting a hopeful and pleased feeling."),
    ("purpose", "A short chant repeats, 'Wash, rinse, dry!' before each verse about preparing fruit. What is the chant mainly meant to do?", ["Remind listeners of the steps for clean preparation", "Tell a story about a lost ship", "Describe a winter sport", "Ask listeners to stop eating fruit"], "A", "The repeated three-step line functions as a reminder of the preparation process."),
    ("setting", "Rhyme: 'Lanterns glow along the street, / Drums are calling with the beat. / Families walk beneath the moon.' Where does the scene most likely take place?", ["On a street during an evening community event", "Inside a silent classroom at noon", "Underwater in the afternoon", "In an empty office before sunrise"], "A", "Lanterns, a street, families, drums, and the moon create an evening community scene."),
    ("inference", "Song: 'I keep one shell inside my hand; / It came from far across the sand. / When I hear the ocean's sound, / I remember friends I found.' What can be inferred?", ["The shell reminds the singer of a past seaside experience.", "The singer has never seen the ocean.", "The shell is used to measure a race.", "The friends live inside the shell."], "A", "The shell and ocean sound trigger a memory of friends and a past seaside experience."),
    ("audience", "A simple school song says, 'Join our circle, clap with me; / Every voice can set us free.' Who is the song inviting?", ["People in the group or audience", "Only a sleeping baby", "A weather reporter alone", "A museum statue"], "A", "Join, clap with me, and every voice address listeners who can participate in the group."),
    ("integrated summary", "Verse: 'Rain taps softly on the roof. / We move our picnic to the hall. / When clouds pass, we laugh and run; / The day still welcomes one and all.' Which summary is best?", ["The group changes its picnic place because of rain but continues enjoying the day.", "The group cancels every activity forever.", "The group runs outside during the heaviest rain.", "The verse is mainly about repairing a roof."], "A", "The summary includes the weather problem, the move indoors, and the group's continued enjoyment without adding an unsupported ending."),
]


def make(index, row):
    topic, prompt, choices, answer, explanation = row
    options = [{"id": chr(65 + i), "text": text} for i, text in enumerate(choices)]
    refs = [{"url": url, "title": f"{title}；僅取簡易歌謠韻文內容理解能力方向，未複製原題、選項、圖表或答案。", "year": "113-114", "subject": "english", "locator": locator, "observedPattern": "公開英文評量常以短歌謠、韻文與押韻文本測量主旨、標題、細節、順序、情緒、目的、場景與推論；本題為獨立改寫。", "reuseDecision": "pattern-only", "status": "recorded", "locatorLevel": "paper"} for url, title, locator in SOURCES]
    steps = [
        f"Read the whole song or verse and identify the comprehension task: {topic}.",
        "Underline repeated ideas, sequence words, actions, setting clues, feeling words, and the ending change.",
        f"Compare each answer with the lines and choose the one directly supported; the correct answer is {answer}.",
        f"Explain the text evidence: {explanation}",
        "Say the main event or message in your own words, checking that the answer covers the passage instead of one attractive but minor word.",
    ]
    return {"id": f"question-english-performance-1-iv-5-{index}", "subject": "english", "type": "single-choice", "prompt": prompt, "options": options, "knowledgeIds": ["kg-english-performance-1-iv-5"], "difficulty": "medium", "answer": {"value": answer, "explanation": explanation + f" Correct answer: {answer}"}, "provenance": {"origin": "original", "license": "All rights reserved", "sourceUrl": SOURCES[0][0], "sourceLocator": "Public-school English assessment materials; this item studies simple song/verse content comprehension only and does not reproduce an original question, option, image, or answer.", "authoringNote": "Written independently from the official English curriculum KG and three public-school English assessment sources; poems, options, explanations, and transfer tasks are original; pending second-round AI/Terra content review."}, "reviewStatus": "draft", "updatedAt": "2026-09-09", "lessonId": "lesson-english-performance-1-iv-5", "examPatternRefs": refs, "solutionStrategy": "Read the entire short song, follow its actions and sequence, connect repeated clues to the central message, and infer only what the lines support.", "solutionSteps": steps}


for index, row in enumerate(DATA, 1):
    (OUT / f"question-english-performance-1-iv-5-{index}.json").write_text(json.dumps(make(index, row), ensure_ascii=False, indent=2) + "\n", encoding="utf-8")
print(f"rewrote {len(DATA)} questions")
