import json
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
OUT = ROOT / "questions/english"
SOURCES = [
    ("https://www.yacjh.kh.edu.tw/upload/221/101_30637/114%E4%B8%8B%E5%AD%B8%E6%9C%9F%E7%AC%AC%E4%B8%80%E6%AC%A1%E6%AE%B5%E8%80%83%E4%B8%89%E5%B9%B4%E7%B4%9A%E8%8B%B1%E6%96%87.pdf", "高雄市立鹽埕國民中學公開英文段考", "cultural respect, social response, and contextual reading"),
    ("https://www.bhjh.ntpc.edu.tw/p/406-1000-10627%2Cr111.php?Lang=zh-tw", "新北市立北投國民中學公開定期評量試題頁", "functional exchanges and respectful communication"),
    ("https://www.hcjh.ntpc.edu.tw/p/406-1000-7527%2Cr146.php", "新北市立新埔國民中學公開段考試題頁", "social situations, audience, and inference"),
]

DATA = [
    ("use the preferred name", "A classmate tells you the community group prefers its traditional name, not a nickname. What should you do?", ["Use the preferred name and thank the classmate for explaining.", "Keep using the nickname because it is shorter.", "Invent a new name for the group.", "Avoid speaking to anyone from the group."], "A", "Using the name people request recognizes their identity, and thanking the classmate shows that the explanation was heard."),
    ("ask before participating", "You want to join a ceremony, but you do not know whether visitors may enter a certain area. What is the best first step?", ["Ask an organizer or read the visitor instructions before entering.", "Enter quickly before anyone notices.", "Guess based on a movie.", "Tell the participants to change the ceremony."], "A", "Checking with an organizer or written instruction avoids disrupting a meaningful practice and respects boundaries."),
    ("learn context", "A museum label explains that a pattern has a special meaning in its community. How should a student use the pattern in a project?", ["Research its meaning and credit the community or museum source.", "Copy it onto products and claim to have invented it.", "Use it as a random decoration without reading the label.", "Say that one pattern represents every culture."], "A", "Understanding context and naming the source prevents misrepresentation and shows appreciation rather than careless borrowing."),
    ("respond to a stereotype", "Someone says, 'Everyone from that place behaves exactly the same.' Which reply is most respectful and accurate?", ["People in a place are diverse; we should avoid judging every person from one example.", "Yes, one story proves it about everyone.", "We should never learn about any culture.", "The stereotype is funny, so repeat it."], "A", "The reply recognizes diversity and rejects a broad judgment based on one example."),
    ("correct a mistake", "You pronounce a guest's name incorrectly, and the guest gently corrects you. What should you say?", ["Thank you for correcting me. Could you say it once more so I can practice?", "Your name is too difficult, so I will not try.", "Pretend you did not hear the correction.", "Make a joke about the pronunciation."], "A", "The response accepts correction, asks for help, and treats the person's name as worth learning."),
    ("respectful observation", "A student visits a cultural exhibit. Which note records an observation without making an unsupported judgment?", ["The display explains how families use this object during a specific ceremony.", "This object is strange and people who use it are strange.", "Everyone in the country owns this object.", "The object must have no meaning."], "A", "The first note reports the exhibit's explanation and limits the claim to the stated ceremony."),
    ("include a community voice", "Your group is preparing a presentation about a local tradition. Which research plan is strongest?", ["Use reliable sources and, when possible, include information or comments from people in the community.", "Use only a stereotype from a comedy video.", "Choose details that make the tradition look exotic.", "Remove the tradition's own explanation."], "A", "Reliable research plus community perspectives gives context and reduces the chance of presenting outsiders' assumptions as facts."),
    ("handle unfamiliar food", "At a shared meal, you do not recognize a dish and are unsure how to eat it. What is a considerate response?", ["Ask politely about the dish or watch the host's guidance without insulting it.", "Call it disgusting before tasting it.", "Throw it away while others are watching.", "Tell everyone that your food is superior."], "A", "A polite question or quiet observation shows curiosity without insulting food that may carry personal or cultural meaning."),
    ("appreciation language", "Which sentence expresses appreciation without claiming to speak for an entire culture?", ["I learned how this song is used in this community, and I appreciate the explanation.", "This song proves that all people there feel the same.", "I understand the whole culture after hearing one song.", "Their culture is valuable only when I use it."], "A", "The sentence identifies a specific learning experience and appreciation while avoiding an oversized claim."),
    ("integrated respectful action", "A visiting student wants to photograph a craft demonstration, share the maker's story online, and buy a small item. Which plan is most responsible?", ["Ask before photographing, use the maker's stated name and story, and pay the requested price if buying.", "Photograph secretly and rewrite the story as your own.", "Post the image without context and bargain aggressively.", "Touch every unfinished item before asking."], "A", "Permission, accurate attribution, fair payment, and careful handling respect both the maker and the meaning of the work."),
]


def make(index, row):
    topic, prompt, choices, answer, explanation = row
    options = [{"id": chr(65 + i), "text": text} for i, text in enumerate(choices)]
    refs = [{
        "url": url, "title": f"{title}；僅取文化理解與合宜溝通能力方向，未複製原題、選項、圖表或答案。",
        "year": "113-114", "subject": "english", "locator": locator,
        "observedPattern": "公開英文評量常以文化情境、人物互動、社會規範與短文判讀測量合宜回應、脈絡理解、尊重差異與證據界線；本題為獨立改寫。",
        "reuseDecision": "pattern-only", "status": "recorded", "locatorLevel": "paper",
    } for url, title, locator in SOURCES]
    steps = [
        f"Read the situation and identify the respect or appreciation skill: {topic}.",
        "Check whose identity, boundary, voice, property, or explanation is involved and what permission or context is missing.",
        f"Choose the response that is curious, accurate, non-stereotyping, and fair; the correct answer is {answer}.",
        f"Connect the choice to the evidence: {explanation}",
        "State one concrete respectful action and explain how it avoids speaking over, mocking, copying, or generalizing about the community.",
    ]
    return {
        "id": f"question-english-content-c-iv-4-{index}", "subject": "english", "type": "single-choice", "prompt": prompt,
        "options": options, "knowledgeIds": ["kg-english-content-c-iv-4"], "difficulty": "medium",
        "answer": {"value": answer, "explanation": explanation + f" Correct answer: {answer}"},
        "provenance": {"origin": "original", "license": "All rights reserved", "sourceUrl": SOURCES[0][0],
            "sourceLocator": "Public-school English assessment materials; this item studies respectful cultural participation and contextual communication patterns only and does not reproduce an original question, option, image, or answer.",
            "authoringNote": "Written independently from the official English curriculum KG and three public-school English assessment sources; situations, options, explanations, and transfer tasks are original; pending second-round AI/Terra content review."},
        "reviewStatus": "draft", "updatedAt": "2026-09-09", "lessonId": "lesson-english-content-c-iv-4", "examPatternRefs": refs,
        "solutionStrategy": "Identify the people and cultural context involved, then choose an action that asks permission, uses accurate attribution, respects boundaries, and avoids stereotypes or careless appropriation.", "solutionSteps": steps,
    }


for index, row in enumerate(DATA, 1):
    (OUT / f"question-english-content-c-iv-4-{index}.json").write_text(json.dumps(make(index, row), ensure_ascii=False, indent=2) + "\n", encoding="utf-8")
print(f"rewrote {len(DATA)} questions")
