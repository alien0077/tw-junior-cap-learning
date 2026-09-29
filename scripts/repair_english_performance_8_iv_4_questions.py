import json
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
OUT = ROOT / "questions/english"
SOURCES = [
    ("https://www.yacjh.kh.edu.tw/upload/221/101_30637/114%E4%B8%8B%E5%AD%B8%E6%9C%9F%E7%AC%AC%E4%B8%80%E6%AC%A1%E6%AE%B5%E8%80%83%E4%B8%89%E5%B9%B4%E7%B4%9A%E8%8B%B1%E6%96%87.pdf", "高雄市立鹽埕國民中學公開英文段考", "cultural respect, appreciation, differences, and inclusive interaction"),
    ("https://www.bhjh.ntpc.edu.tw/p/406-1000-10627%2Cr111.php?Lang=zh-tw", "新北市立北投國民中學公開定期評量試題頁", "perspective taking, cultural evidence, and respectful behavior"),
    ("https://www.hcjh.ntpc.edu.tw/p/406-1000-7527%2Cr146.php", "新北市立新埔國民中學公開段考試題頁", "appreciating different cultures and responding without stereotypes"),
]

DATA = [
    ("respectful curiosity", "A classmate describes a family custom that is unfamiliar to you. Which response shows respectful curiosity?", ["Could you tell me what the custom means to your family?", "That custom is strange and must be wrong.", "I already know everything about your culture.", "Please stop speaking because my custom is better."], "A", "The question invites the classmate to explain meaning from personal experience without judging it."),
    ("avoid stereotype", "A student sees one person from a country enjoying a certain food. What should the student avoid concluding?", ["Everyone from that country always likes the same food", "This person has a personal preference", "Food choices can vary within a culture", "More information is needed before making a broad claim"], "A", "One person's choice cannot support a universal statement about an entire culture."),
    ("perspective", "A visitor is quiet during a group activity because listening carefully is valued in the visitor's community. What is a respectful interpretation?", ["The visitor may be showing respect in a different way", "The visitor definitely dislikes every person there", "Quiet behavior always means anger", "The visitor cannot understand any activity"], "A", "Considering the visitor's cultural perspective prevents a rushed negative judgment."),
    ("asking before participating", "You want to join a cultural dance at a public event. What should you do first?", ["Check whether visitors may join and follow the organizers' instructions", "Walk into the center without asking", "Change the dance to match your favorite music", "Film every participant without considering privacy"], "A", "Permission and guidance help visitors participate respectfully."),
    ("inclusive language", "Which sentence discusses cultural difference without ranking people?", ["People may celebrate the same value through different traditions.", "Some cultures are better because they are more familiar to me.", "A different custom is automatically less civilized.", "Only one way of celebrating should be allowed."], "A", "The sentence recognizes variation without assigning unequal value."),
    ("evidence over assumption", "A poster shows a traditional garment, but gives no explanation. What is the best next step?", ["Read a reliable explanation or ask a respectful question before interpreting it", "Invent a meaning and present it as fact", "Assume the garment is worn by every person every day", "Mock the garment because it looks different"], "A", "Reliable context is needed before making a cultural interpretation."),
    ("responding to correction", "A classmate explains that your description of a tradition is inaccurate. Which response is best?", ["Thank them, correct the description, and check a reliable source", "Argue that your first guess must be correct", "Tell them their culture is too complicated to learn", "Ignore the correction and repeat the error"], "A", "Accepting correction and verifying information shows respect and intellectual honesty."),
    ("appreciation", "After learning a traditional craft, which response shows appreciation rather than treating it as a novelty?", ["Explain its skill, history, and meaning, and credit the community that practices it", "Use the craft as a joke without learning its context", "Claim you invented it after one short activity", "Judge the craft only by whether it looks modern"], "A", "Appreciation recognizes knowledge, history, skill, and the people connected to the practice."),
    ("inclusive group work", "A group includes students with different cultural backgrounds. Which plan supports everyone?", ["Invite each person to share if comfortable, agree on respectful language, and use evidence when discussing customs.", "Require one student to speak for an entire country.", "Avoid all cultural topics because differences cannot be discussed.", "Choose one culture as the standard for every decision."], "A", "The plan gives choice, avoids overgeneralization, and supports informed discussion."),
    ("integrated reflection", "After comparing two celebrations, which reflection best demonstrates respect and learning?", ["I found both shared human purposes and culture-specific practices; I should ask for context instead of judging unfamiliar details.", "I now know every person in each culture celebrates identically.", "One celebration is valuable and the other has no meaning.", "Learning about culture means copying every practice immediately."], "A", "The reflection combines common ground, difference, context, and humility."),
]


def make(index, row):
    topic, prompt, choices, answer, explanation = row
    options = [{"id": chr(65 + i), "text": text} for i, text in enumerate(choices)]
    refs = [{"url": url, "title": f"{title}；僅取文化尊重、同理、證據、避免刻板印象、包容互動與反思能力方向，未複製原題、選項、圖表或答案。", "year": "113-114", "subject": "english", "locator": locator, "observedPattern": "公開英文評量與文化情境常要求理解不同觀點、以證據修正假設、使用尊重語言、避免以個人經驗概括群體並提出合宜行動；本題為獨立改寫。", "reuseDecision": "pattern-only", "status": "recorded", "locatorLevel": "paper"} for url, title, locator in SOURCES]
    steps = [
        f"Read the cultural interaction and identify the respect target: {topic}.",
        "Separate the observed fact from an assumption, then mark the speaker's perspective, permission, privacy, evidence, correction, and inclusion cues.",
        f"Choose the response that is curious, fair, evidence-based, and non-stereotyping; the correct answer is {answer}.",
        f"Explain how the response respects people and cultural context: {explanation}",
        "Reread the situation and check that the answer neither ranks cultures nor speaks for every person in a community.",
    ]
    return {"id": f"question-english-performance-8-iv-4-{index}", "subject": "english", "type": "single-choice", "prompt": prompt, "options": options, "knowledgeIds": ["kg-english-performance-8-iv-4"], "difficulty": "medium", "answer": {"value": answer, "explanation": explanation + f" Correct answer: {answer}"}, "provenance": {"origin": "original", "license": "All rights reserved", "sourceUrl": SOURCES[0][0], "sourceLocator": "Public-school English assessment materials; this item studies cultural respect, perspective taking, evidence, inclusive interaction, appreciation, and stereotype avoidance only and does not reproduce an original question, option, image, or text.", "authoringNote": "Written independently from the official English curriculum KG and three public-school English assessment sources; cultural situations, options, explanations, and transfer tasks are original; pending second-round AI/Terra content review."}, "reviewStatus": "draft", "updatedAt": "2026-09-09", "lessonId": "lesson-english-performance-8-iv-4", "examPatternRefs": refs, "solutionStrategy": "Observe carefully, ask for context, distinguish individual experience from group claims, and choose inclusive actions grounded in respect and evidence.", "solutionSteps": steps}


for index, row in enumerate(DATA, 1):
    (OUT / f"question-english-performance-8-iv-4-{index}.json").write_text(json.dumps(make(index, row), ensure_ascii=False, indent=2) + "\n", encoding="utf-8")
print(f"rewrote {len(DATA)} questions")
