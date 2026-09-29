import json
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
OUT = ROOT / "questions/english"
SOURCES = [
    ("https://www.yacjh.kh.edu.tw/upload/221/101_30637/114%E4%B8%8B%E5%AD%B8%E6%9C%9F%E7%AC%AC%E4%B8%80%E6%AC%A1%E6%AE%B5%E8%80%83%E4%B8%89%E5%B9%B4%E7%B4%9A%E8%8B%B1%E6%96%87.pdf", "高雄市立鹽埕國民中學公開英文段考", "short stories, drama, sequence, and inference"),
    ("https://www.bhjh.ntpc.edu.tw/p/406-1000-10627%2Cr111.php?Lang=zh-tw", "新北市立北投國民中學公開定期評量試題頁", "narrative details, dialogue, and character response"),
    ("https://www.hcjh.ntpc.edu.tw/p/406-1000-7527%2Cr146.php", "新北市立新埔國民中學公開段考試題頁", "story purpose, mood, and contextual reading"),
]

DATA = [
    ("character goal", "Story: Maya finds a broken kite and spends the afternoon fixing it because she wants to fly it with her younger brother. What is Maya's goal?", ["To repair the kite for a shared flight", "To sell her brother a new bicycle", "To hide from the wind", "To win a cooking contest"], "A", "The story directly states that Maya fixes the kite so she and her brother can fly it together."),
    ("event sequence", "Short play: [Tom enters with a wet coat.] He hangs it by the heater, borrows a towel, and then joins the rehearsal. What does Tom do first after entering?", ["He joins the rehearsal.", "He hangs the coat by the heater.", "He borrows a towel after rehearsal.", "He leaves the theater."], "B", "The stage direction and action order show that Tom hangs the wet coat by the heater first."),
    ("conflict", "Story: Two friends both want the last seat on the bus. Lina suggests taking turns and standing together at the next stop. What problem are they solving?", ["A disagreement about the last seat", "A missing homework assignment", "A broken stage light", "A late birthday cake"], "A", "Both friends want the same last seat, creating the conflict that Lina tries to solve fairly."),
    ("turning point", "Story: Jin forgets his speech, sees a note from his partner, and begins again with confidence. Which event is the turning point?", ["Jin walks onto the stage", "Jin sees the supportive note", "The audience enters the room", "The speech ends before it starts"], "B", "Seeing the note changes Jin's confidence and leads him to restart, so it is the turning point."),
    ("dialogue intention", "Short play: 'You may use my umbrella,' said Rosa, 'but please bring it back before the rain stops.' What does Rosa intend?", ["To offer help while asking for the umbrella to be returned", "To tell her friend never to go outside", "To sell a raincoat", "To cancel the weather"], "A", "Rosa offers the umbrella and states a return request; the line is both helpful and specific."),
    ("stage direction", "A script reads: [Sam looks at the empty chair and lowers his voice.] 'I thought she would be here.' What does the stage direction help show?", ["Sam feels disappointed or worried.", "Sam is loudly celebrating.", "Sam is cooking dinner.", "Sam has forgotten where the stage is."], "A", "Looking at an empty chair and lowering his voice provide evidence of quiet disappointment or worry."),
    ("character change", "Story: At first, Ella refuses to ask for help. After seeing her team struggle, she explains the problem and accepts a suggestion. How does Ella change?", ["She becomes more willing to communicate and cooperate.", "She stops caring about the team.", "She decides never to solve the problem.", "She becomes unable to hear suggestions."], "A", "Ella moves from refusing help to explaining and accepting a suggestion, showing increased cooperation."),
    ("ending inference", "Story: A boy loses the race but congratulates the winner and asks to practice together next week. What does the ending suggest?", ["He values improvement and sportsmanship.", "He plans to quit every activity.", "He believes the winner cheated without evidence.", "He only wants a new uniform."], "A", "Congratulating the winner and planning practice support a positive attitude toward improvement and fair play."),
    ("theme", "A short drama shows neighbors sharing tools to repair a playground and celebrating when children return. What is the likely message?", ["Cooperation can improve a community.", "People should keep useful tools secret.", "Playgrounds repair themselves.", "Celebrations must always happen indoors."], "A", "The neighbors' shared tools and work lead to a repaired playground, emphasizing cooperation."),
    ("integrated summary", "Short play: [Rain begins.] A family moves its outdoor show into a garage, a child finds a flashlight, and everyone performs for the neighbors. Which summary is best?", ["The family adapts the show to the rain and continues performing together.", "The family cancels the show and sends everyone home.", "The child loses the flashlight before the rain begins.", "The neighbors leave because no performance occurs."], "A", "The stage direction, move into the garage, flashlight, and final performance all support the adaptive family-show summary."),
]


def make(index, row):
    topic, prompt, choices, answer, explanation = row
    options = [{"id": chr(65 + i), "text": text} for i, text in enumerate(choices)]
    refs = [{"url": url, "title": f"{title}；僅取故事短劇內容理解能力方向，未複製原題、選項、圖表或答案。", "year": "113-114", "subject": "english", "locator": locator, "observedPattern": "公開英文評量常以短故事、對話、舞台指示與情節測量人物目標、順序、衝突、轉折、情緒、結局與主旨；本題為獨立改寫。", "reuseDecision": "pattern-only", "status": "recorded", "locatorLevel": "paper"} for url, title, locator in SOURCES]
    steps = [
        f"Read the story or stage directions and identify the narrative task: {topic}.",
        "Track who acts, what the character wants, what problem appears, how the character responds, and what changes at the end.",
        f"Choose the option supported by the dialogue or action; the correct answer is {answer}.",
        f"Point to the story evidence: {explanation}",
        "Retell the relevant beginning, change, and result in order, checking that the answer does not add an event absent from the script.",
    ]
    return {"id": f"question-english-performance-1-iv-6-{index}", "subject": "english", "type": "single-choice", "prompt": prompt, "options": options, "knowledgeIds": ["kg-english-performance-1-iv-6"], "difficulty": "medium", "answer": {"value": answer, "explanation": explanation + f" Correct answer: {answer}"}, "provenance": {"origin": "original", "license": "All rights reserved", "sourceUrl": SOURCES[0][0], "sourceLocator": "Public-school English assessment materials; this item studies short-story and short-drama comprehension patterns only and does not reproduce an original question, option, image, or answer.", "authoringNote": "Written independently from the official English curriculum KG and three public-school English assessment sources; stories, dialogue, stage directions, options, and transfer tasks are original; pending second-round AI/Terra content review."}, "reviewStatus": "draft", "updatedAt": "2026-09-09", "lessonId": "lesson-english-performance-1-iv-6", "examPatternRefs": refs, "solutionStrategy": "Follow the character's goal, problem, actions, dialogue, stage cues, turning point, and outcome to identify the best supported story interpretation.", "solutionSteps": steps}


for index, row in enumerate(DATA, 1):
    (OUT / f"question-english-performance-1-iv-6-{index}.json").write_text(json.dumps(make(index, row), ensure_ascii=False, indent=2) + "\n", encoding="utf-8")
print(f"rewrote {len(DATA)} questions")
