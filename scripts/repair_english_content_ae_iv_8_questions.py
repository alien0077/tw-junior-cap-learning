import json
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
OUT = ROOT / "questions/english"
SOURCES = [
    ("https://www.yacjh.kh.edu.tw/upload/221/101_30637/114%E4%B8%8B%E5%AD%B8%E6%9C%9F%E7%AC%AC%E4%B8%80%E6%AC%A1%E6%AE%B5%E8%80%83%E4%B8%89%E5%B9%B4%E7%B4%9A%E8%8B%B1%E6%96%87.pdf", "高雄市立鹽埕國民中學公開英文段考", "short story, main idea, details, and English reading comprehension"),
    ("https://www.bhjh.ntpc.edu.tw/p/406-1000-10627%2Cr111.php?Lang=zh-tw", "新北市立北投國民中學公開定期評量試題頁", "story comprehension, title, summary, and contextual inference"),
    ("https://www.hcjh.ntpc.edu.tw/p/406-1000-7527%2Cr146.php", "新北市立新埔國民中學公開段考試題頁", "English short passages, main idea, evidence, and application"),
]

DATA = [
    ("main idea", "Story: 'Every morning, Aya carried a small bag to the park. She picked up three pieces of litter before feeding the birds. After a month, other walkers began carrying bags too.' What is the main idea?", ["One person's steady care can inspire a cleaner community.", "Birds should never eat in parks.", "Aya visits the park only once a month.", "Walkers always leave more litter behind."], "One person's steady care can inspire a cleaner community.", "The story emphasizes Aya's repeated action and the way others follow her example. That community change is the central idea, not a claim about avoiding parks or birds."),
    ("best title", "Story: 'Ben practiced the difficult piano passage for ten minutes each evening. At first he made many mistakes, but by the school concert he could play it smoothly.' Which title is best?", ["Small Practice, Big Progress", "The Empty Swimming Pool", "A Lost Lunch Box", "Why Concerts Must Stop"], "Small Practice, Big Progress", "The title captures the repeated practice, early difficulty, and later improvement. The other titles do not match the story's main events."),
    ("supporting detail", "Story: 'Lily wanted to join the cycling trip, so she checked the tires, packed water, and studied the route the night before.' Which detail best supports the idea that Lily prepared carefully?", ["She checked the tires, packed water, and studied the route.", "She wanted to join a trip.", "The trip involved cycling.", "The story happened at night only."], "She checked the tires, packed water, and studied the route.", "The three listed actions are specific evidence of preparation. Wanting to join and the activity itself do not prove how carefully she prepared."),
    ("cause and result", "Story: 'The class placed a bowl of water outside during the hot afternoon. By sunset, the bowl was empty, and a thirsty cat waited nearby.' What most likely caused the empty bowl?", ["The cat or another animal drank the water.", "The class filled it with stones.", "The sun made the bowl sing.", "The cat planted a tree in it."], "The cat or another animal drank the water.", "The nearby thirsty cat and the hot afternoon support the inference that an animal used the water. The text does not prove exactly which animal, so the cautious wording is best."),
    ("summary", "Story: 'Mina forgot her lunch. She shared a table with Zoe, who offered half a sandwich. The next day Mina brought extra fruit to share with Zoe.' Which is the best summary?", ["Zoe helped Mina, and Mina returned the kindness the next day.", "Mina ate every lunch alone for a week.", "Zoe lost a sandwich and stopped going to school.", "Mina refused all food from Zoe."], "Zoe helped Mina, and Mina returned the kindness the next day.", "The summary includes the problem, Zoe's help, and Mina's later response without adding unrelated events. It captures the story's complete arc."),
    ("character change", "Story: 'At the beginning, Omar kept his invention hidden because he feared mistakes. After his team tested it and suggested changes, he presented it to the class.' What changed?", ["Omar became more willing to share after receiving helpful feedback.", "Omar stopped building inventions forever.", "The team refused to test anything.", "Omar became afraid of every classmate."], "Omar became more willing to share after receiving helpful feedback.", "The contrast between hiding the invention and presenting it, plus the team's feedback, shows a change toward confidence and collaboration."),
    ("central lesson", "Story: 'A fox tried to jump over a stream alone and fell in. On the next attempt, it used the stepping stones slowly and reached the other side.' What lesson is most supported?", ["Careful planning can be better than rushing.", "Streams should never be crossed.", "Falling once means every attempt must fail.", "Speed is always more important than safety."], "Careful planning can be better than rushing.", "The fox fails when rushing and succeeds when using the stones slowly. The lesson is about changing strategy and working carefully, not avoiding all streams."),
    ("detail versus main idea", "Story: 'Nora planted a sunflower. She watered it, moved it toward the light, and measured its height every Friday. It grew taller and opened a bright flower.' Which statement is a main idea rather than a single detail?", ["Patient care helped Nora's plant grow.", "Nora measured its height every Friday.", "The flower was bright.", "The plant was a sunflower."], "Patient care helped Nora's plant grow.", "The main idea connects several actions and the result. The other choices are individual details from the story."),
    ("inference boundary", "Story: 'Kai heard music from the empty hall and found a speaker playing beside an open window. He closed the window and turned off the speaker.' What can be concluded?", ["The open window allowed the music to be heard outside.", "A full orchestra was hiding in the hall.", "Kai wrote a song during the night.", "The hall had no windows at all."], "The open window allowed the music to be heard outside.", "The speaker, open window, and Kai's actions support the conclusion about the sound. The other choices add details not stated in the story."),
    ("integrated main idea", "Story: 'When the neighborhood pond became cloudy, three children tested the water, asked adults to remove fallen trash, and placed a reminder sign nearby. The pond was clearer after several weeks.' Which statement best expresses the story's main idea?", ["Small, informed actions can help solve a community problem.", "Children should never visit ponds.", "The pond became cloudy because of music.", "A sign alone immediately cleans every pond."], "Small, informed actions can help solve a community problem.", "The children investigate, seek help, act, and observe improvement. The main idea combines their informed teamwork and the community result without exaggerating what one sign can do."),
]


def make(index, row):
    tag, prompt, choices, answer, explanation = row
    options = [{"id": chr(65 + i), "text": text} for i, text in enumerate(choices)]
    answer_id = next(option["id"] for option in options if option["text"] == answer)
    refs = [{
        "url": url, "title": f"{title}; pattern-only study, no original item or option copied.", "year": "113-114", "subject": "english", "locator": locator,
        "observedPattern": "Public-school English assessments use short stories, main idea, title, details, summary, cause-result, lesson, and evidence-limited inference; this is an independent rewrite without copying wording, options, figures, or answers.",
        "reuseDecision": "pattern-only", "status": "recorded", "locatorLevel": "paper"
    } for url, title, locator in SOURCES]
    steps = [
        f"Read the story and identify the comprehension focus: {tag}.",
        f"Separate the central change or message from supporting details, then apply this rule: {explanation}",
        f"Check option {answer_id}: {answer}",
        "Reject the other options by checking whether they cover the whole story and whether every inference remains within the evidence rather than adding an invented event.",
        "Retell the story in one or two sentences, cite the details that support the answer, and explain why the selected statement is broader or safer than the distractors.",
    ]
    return {
        "id": f"question-english-content-ae-iv-8-{index}", "subject": "english", "type": "single-choice", "prompt": prompt,
        "options": options, "knowledgeIds": ["kg-english-content-ae-iv-8"], "difficulty": "medium",
        "answer": {"value": answer_id, "explanation": explanation + f" Correct answer: {answer}"},
        "provenance": {"origin": "original", "license": "All rights reserved", "sourceUrl": SOURCES[0][0], "sourceLocator": "Public-school English assessment materials; this item studies assessment patterns only and does not reproduce an original question, option, image, or answer.", "authoringNote": "Written independently from the official English curriculum KG and three public-school English assessment sources; story contexts, options, explanation, and transfer task are original; pending second-round AI/Terra content review."},
        "reviewStatus": "draft", "updatedAt": "2026-09-09", "lessonId": "lesson-english-content-ae-iv-8", "examPatternRefs": refs,
        "solutionStrategy": "Compress the story into problem, key actions, change, result, and message; keep the main idea broad enough to cover the whole text but narrow enough to stay supported.", "solutionSteps": steps,
    }


for index, row in enumerate(DATA, 1):
    (OUT / f"question-english-content-ae-iv-8-{index}.json").write_text(json.dumps(make(index, row), ensure_ascii=False, indent=2) + "\n", encoding="utf-8")
print(f"rewrote {len(DATA)} questions")
