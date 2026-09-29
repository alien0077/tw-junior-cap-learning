import json
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
OUT = ROOT / "questions/english"
SOURCES = [
    ("https://www.yacjh.kh.edu.tw/upload/221/101_30637/114%E4%B8%8B%E5%AD%B8%E6%9C%9F%E7%AC%AC%E4%B8%80%E6%AC%A1%E6%AE%B5%E8%80%83%E4%B8%89%E5%B9%B4%E7%B4%9A%E8%8B%B1%E6%96%87.pdf", "高雄市立鹽埕國民中學公開英文段考", "communication, dialogue, and practical English use"),
    ("https://www.bhjh.ntpc.edu.tw/p/406-1000-10627%2Cr111.php?Lang=zh-tw", "新北市立北投國民中學公開定期評量試題頁", "short exchanges, intent, and contextual response"),
    ("https://www.hcjh.ntpc.edu.tw/p/406-1000-7527%2Cr146.php", "新北市立新埔國民中學公開段考試題頁", "functional language, interaction, and application"),
]

DATA = [
    ("tone", "A friend says, 'Could you help me for a minute?' Which spoken tone best communicates willingness?", ["Use a warm, calm voice: 'Sure, what do you need?'", "Shout, 'Why are you bothering me?'", "Whisper so softly that no one can hear.", "Laugh without answering the request."], "Use a warm, calm voice: 'Sure, what do you need?'", "A warm and calm tone matches a helpful response. Volume, facial expression, and words should work together to show willingness rather than anger or avoidance."),
    ("gesture meaning", "During a presentation, a classmate points to the next slide while saying, 'This part shows our result.' What does the gesture help the audience do?", ["Notice which part of the visual the speaker is explaining.", "Know that the presentation is finished forever.", "Understand that the speaker wants everyone to leave.", "Hear a sound that replaces every spoken word."], "Notice which part of the visual the speaker is explaining.", "Pointing directs visual attention to a specific part of the slide. It supports the words but does not replace the whole message."),
    ("active listening", "Which behavior best shows active listening during a partner's explanation?", ["Face the speaker, avoid interrupting, and ask a relevant follow-up question.", "Look at a phone and change the topic repeatedly.", "Interrupt after every word.", "Turn away and guess the speaker's meaning."], "Face the speaker, avoid interrupting, and ask a relevant follow-up question.", "Active listening combines attention, respectful turn-taking, and a question connected to what was said. It is more than merely being physically present."),
    ("clarification strategy", "You hear an unfamiliar word in a group discussion. Which sentence is the best clarification strategy?", ["Could you explain what that word means in this sentence?", "I will pretend I understood everything.", "That word is wrong because I have not heard it.", "Please stop all future discussions."], "Could you explain what that word means in this sentence?", "The question politely identifies the missing meaning and asks for context. Pretending or rejecting an unfamiliar word does not repair understanding."),
    ("eye contact and respect", "When listening to a classmate, what is a respectful strategy?", ["Look at the speaker naturally while also allowing comfortable pauses.", "Stare without blinking to force an answer.", "Keep your back turned throughout the conversation.", "Close your eyes and interrupt with a new topic."], "Look at the speaker naturally while also allowing comfortable pauses.", "Natural eye contact can show attention, but respectful communication also allows pauses and personal comfort. Excessive staring or turning away can interfere with the interaction."),
    ("turn-taking", "Two students want to answer at once. Which strategy keeps the discussion fair?", ["One student finishes, then the other speaks after a brief turn-taking signal.", "Both students speak louder until one gives up.", "Neither student listens or answers.", "The teacher's question is erased."], "One student finishes, then the other speaks after a brief turn-taking signal.", "Turn-taking gives each speaker space and a predictable signal. Volume competition prevents people from hearing the ideas."),
    ("visual communication", "A visitor does not understand a spoken direction, but the helper draws a simple map and marks the entrance with an arrow. Why is this useful?", ["The visual gives another route to understand the location and action.", "The drawing changes the entrance into a different building.", "The arrow proves that every road is closed.", "The map removes the need to communicate anything."], "The visual gives another route to understand the location and action.", "A simple map and arrow supplement spoken language by showing place and direction. They make the message more accessible without inventing a new building."),
    ("cultural respect", "A visitor notices that people in a new place use a greeting different from the one at home. What is the best communication strategy?", ["Observe respectfully, learn the local meaning, and follow the setting's appropriate practice.", "Laugh at the greeting and refuse to listen.", "Assume the greeting means exactly the opposite without checking.", "Tell everyone that only one culture can communicate correctly."], "Observe respectfully, learn the local meaning, and follow the setting's appropriate practice.", "Communication practices can vary across cultures. Observation, respectful questions, and attention to context reduce misunderstanding without judging another group."),
    ("nonverbal ambiguity", "A classmate is silent and looks down after a question. What is the safest interpretation?", ["The classmate may be thinking or uncomfortable, so ask gently rather than assuming the reason.", "The classmate definitely agrees with every idea.", "The classmate definitely hates the speaker.", "Silence always means the person is asleep."], "The classmate may be thinking or uncomfortable, so ask gently rather than assuming the reason.", "The same nonverbal behavior can have different causes. A gentle check prevents the listener from treating an uncertain signal as proof of a particular feeling."),
    ("integrated communication", "A group member explains a difficult plan quickly. Which response uses both language and non-language strategies well?", ["Say, 'Could you slow down and show that step on the diagram?' while facing the speaker and pointing to the unclear step.", "Look away, interrupt loudly, and say, 'Whatever.'", "Nod without understanding and submit a different plan.", "Use only a hand wave and leave without explaining."], "Say, 'Could you slow down and show that step on the diagram?' while facing the speaker and pointing to the unclear step.", "The response uses polite language to request clarification, attention through facing the speaker, and a precise gesture toward the unclear diagram step. Together these signals repair communication."),
]


def make(index, row):
    tag, prompt, choices, answer, explanation = row
    options = [{"id": chr(65 + i), "text": text} for i, text in enumerate(choices)]
    answer_id = next(option["id"] for option in options if option["text"] == answer)
    refs = [{
        "url": url, "title": f"{title}; pattern-only study, no original item or option copied.", "year": "113-114", "subject": "english", "locator": locator,
        "observedPattern": "Public-school English assessments use functional exchanges, context, intent, response, and practical communication; this is an independent rewrite that adds nonverbal strategy analysis without copying wording, options, figures, or answers.",
        "reuseDecision": "pattern-only", "status": "recorded", "locatorLevel": "paper"
    } for url, title, locator in SOURCES]
    steps = [
        f"Read the interaction and identify the communication strategy: {tag}.",
        f"Separate spoken words, tone, gesture, gaze, timing, visual support, culture, and uncertainty, then apply this rule: {explanation}",
        f"Check option {answer_id}: {answer}",
        "Reject the other options by checking whether they support the speaker's goal, preserve respect, and avoid treating an ambiguous signal as certain evidence.",
        "Act out or visualize the exchange, explain how the verbal and nonverbal signals work together, and state how the strategy improves understanding.",
    ]
    return {
        "id": f"question-english-content-b-iv-3-{index}", "subject": "english", "type": "single-choice", "prompt": prompt,
        "options": options, "knowledgeIds": ["kg-english-content-b-iv-3"], "difficulty": "medium",
        "answer": {"value": answer_id, "explanation": explanation + f" Correct answer: {answer}"},
        "provenance": {"origin": "original", "license": "All rights reserved", "sourceUrl": SOURCES[0][0], "sourceLocator": "Public-school English assessment materials; this item studies assessment patterns only and does not reproduce an original question, option, image, or answer.", "authoringNote": "Written independently from the official English curriculum KG and three public-school English assessment sources; interaction contexts, verbal and nonverbal analysis, options, explanation, and transfer task are original; pending second-round AI/Terra content review."},
        "reviewStatus": "draft", "updatedAt": "2026-09-09", "lessonId": "lesson-english-content-b-iv-3", "examPatternRefs": refs,
        "solutionStrategy": "Read words and observe behavior together, identify the communication goal, and choose a respectful strategy that clarifies meaning without over-interpreting uncertain nonverbal signals.", "solutionSteps": steps,
    }


for index, row in enumerate(DATA, 1):
    (OUT / f"question-english-content-b-iv-3-{index}.json").write_text(json.dumps(make(index, row), ensure_ascii=False, indent=2) + "\n", encoding="utf-8")
print(f"rewrote {len(DATA)} questions")
