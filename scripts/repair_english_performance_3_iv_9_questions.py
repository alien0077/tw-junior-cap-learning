import json
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
OUT = ROOT / "questions/english"
SOURCES = [
    ("https://www.yacjh.kh.edu.tw/upload/221/101_30637/114%E4%B8%8B%E5%AD%B8%E6%9C%9F%E7%AC%AC%E4%B8%80%E6%AC%A1%E6%AE%B5%E8%80%83%E4%B8%89%E5%B9%B4%E7%B4%9A%E8%8B%B1%E6%96%87.pdf", "高雄市立鹽埕國民中學公開英文段考", "short narratives, sequence, and story comprehension"),
    ("https://www.bhjh.ntpc.edu.tw/p/406-1000-10627%2Cr111.php?Lang=zh-tw", "新北市立北投國民中學公開定期評量試題頁", "narrative details, character intention, and inference"),
    ("https://www.hcjh.ntpc.edu.tw/p/406-1000-7527%2Cr146.php", "新北市立新埔國民中學公開段考試題頁", "story events, conflict, and outcome reading"),
]

DATA = [
    ("main idea", "A story follows a student who keeps losing her bus card, makes a labeled pocket for it, and finally arrives on time. What is the main idea?", ["A practical habit helps solve a repeated problem.", "Buses should stop running after school.", "Labels make every trip longer.", "The student wants to buy a new backpack."], "A", "The repeated loss and the pocket solution show the story's focus on a helpful habit."),
    ("sequence", "First, Ben finds an injured bird. Next, he calls the wildlife center. Finally, a worker takes the bird for care. What happens second?", ["Ben calls the wildlife center.", "A worker takes the bird.", "Ben builds a large cage at home.", "The bird returns before Ben finds it."], "A", "Calling the wildlife center occurs after finding the bird and before the worker arrives."),
    ("character goal", "Mina practices a speech each evening because she wants to welcome new students confidently. What is Mina's goal?", ["To welcome new students confidently", "To avoid meeting any students", "To become the school bus driver", "To cancel the welcome event"], "A", "The because-clause states why Mina practices and reveals her goal."),
    ("conflict", "A team wants to plant a garden, but the chosen space has no sunlight. What is the main conflict?", ["The planned space cannot provide the sunlight the garden needs.", "The team has too many seeds and too much sunlight.", "The garden is already finished and needs no care.", "The team wants to plant only at night for fun."], "A", "The team's plan conflicts with the environmental condition of the space."),
    ("turning point", "After ignoring a map, Leo gets lost. He then asks a shop owner for directions and reaches the station. What is the turning point?", ["Leo decides to ask the shop owner for directions.", "Leo first ignores the map.", "Leo arrives at the station after everything is solved.", "The map is printed in a different color."], "A", "Asking for directions changes the situation from being lost to finding the route."),
    ("cause and effect", "A storm knocks out the power, so the family uses candles and plays a word game. What caused the family to use candles?", ["The storm caused a power outage.", "The word game caused the storm.", "The candles caused the family to leave.", "The family planned a game before the storm in the story."], "A", "The storm's power outage is the stated cause of needing candles."),
    ("emotion change", "At first, Aya is nervous about presenting. After classmates listen kindly, she smiles and speaks more clearly. What changes?", ["Aya becomes more confident.", "Aya becomes angry at the audience.", "Aya forgets why she is presenting.", "Aya decides never to speak again."], "A", "The supportive audience changes Aya from nervous to more confident."),
    ("title", "A short story describes a child returning a wallet, finding its owner, and receiving thanks. Which title fits best?", ["The Wallet That Found Its Way Home", "A Race Across the Ocean", "The Silent Science Lab", "How to Bake a Red Bicycle"], "A", "The title captures the wallet's return and the story's gentle resolution."),
    ("ending inference", "A character repairs a neighbor's broken fence, leaves a note, and later sees the neighbor planting flowers beside it. What can readers reasonably infer?", ["The neighbor appreciated the help and is improving the shared space.", "The fence was never broken.", "The character moved to another country that day.", "The neighbor dislikes all gardens."], "A", "The note, repaired fence, and flowers support a positive response and shared improvement."),
    ("integrated plot", "A story begins with a missing class trophy, follows two friends checking the gym and office, reveals it was stored for cleaning, and ends with the friends labeling the storage shelf. What is the best summary?", ["The friends solve the trophy mystery and create a system to prevent another loss.", "The trophy is stolen and the friends stop searching immediately.", "The office loses every object because labels are forbidden.", "The friends spend the story playing a game unrelated to the trophy."], "A", "The summary includes the problem, investigation, explanation, and preventive ending."),
]


def make(index, row):
    topic, prompt, choices, answer, explanation = row
    options = [{"id": chr(65 + i), "text": text} for i, text in enumerate(choices)]
    refs = [{"url": url, "title": f"{title}；僅取故事主旨、情節順序、角色與結局判讀能力方向，未複製原題、選項、圖表或答案。", "year": "113-114", "subject": "english", "locator": locator, "observedPattern": "公開英文評量常以短篇敘事測量主旨、順序、目標、衝突、轉折、因果、情緒、標題與結局推論；本題為獨立改寫。", "reuseDecision": "pattern-only", "status": "recorded", "locatorLevel": "paper"} for url, title, locator in SOURCES]
    steps = [
        f"Read the narrative and identify the story-reading target: {topic}.",
        "Mark the characters, goal, setting, problem, actions in order, turning point, emotional change, and ending evidence.",
        f"Compare each choice with the full plot and select the interpretation supported by the events; the correct answer is {answer}.",
        f"Explain the plot evidence: {explanation}",
        "Retell the beginning, middle, and ending briefly, then check that the answer does not introduce an event absent from the story.",
    ]
    return {"id": f"question-english-performance-3-iv-9-{index}", "subject": "english", "type": "single-choice", "prompt": prompt, "options": options, "knowledgeIds": ["kg-english-performance-3-iv-9"], "difficulty": "medium", "answer": {"value": answer, "explanation": explanation + f" Correct answer: {answer}"}, "provenance": {"origin": "original", "license": "All rights reserved", "sourceUrl": SOURCES[0][0], "sourceLocator": "Public-school English assessment materials; this item studies original narrative-comprehension patterns only and does not reproduce an original question, option, image, or story.", "authoringNote": "Written independently from the official English curriculum KG and three public-school English assessment sources; narratives, options, explanations, and transfer tasks are original; pending second-round AI/Terra content review."}, "reviewStatus": "draft", "updatedAt": "2026-09-09", "lessonId": "lesson-english-performance-3-iv-9", "examPatternRefs": refs, "solutionStrategy": "Track the plot from problem to action to consequence, separate explicit events from reasonable inferences, and select the summary or interpretation that covers the story without adding facts.", "solutionSteps": steps}


for index, row in enumerate(DATA, 1):
    (OUT / f"question-english-performance-3-iv-9-{index}.json").write_text(json.dumps(make(index, row), ensure_ascii=False, indent=2) + "\n", encoding="utf-8")
print(f"rewrote {len(DATA)} questions")
