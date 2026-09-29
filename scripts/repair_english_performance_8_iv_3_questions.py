import json
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
OUT = ROOT / "questions/english"
SOURCES = [
    ("https://www.yacjh.kh.edu.tw/upload/221/101_30637/114%E4%B8%8B%E5%AD%B8%E6%9C%9F%E7%AC%AC%E4%B8%80%E6%AC%A1%E6%AE%B5%E8%80%83%E4%B8%89%E5%B9%B4%E7%B4%9A%E8%8B%B1%E6%96%87.pdf", "高雄市立鹽埕國民中學公開英文段考", "comparing cultural celebrations, activities, purposes, and evidence"),
    ("https://www.bhjh.ntpc.edu.tw/p/406-1000-10627%2Cr111.php?Lang=zh-tw", "新北市立北投國民中學公開定期評量試題頁", "similarities, differences, cultural practices, and comparison language"),
    ("https://www.hcjh.ntpc.edu.tw/p/406-1000-7527%2Cr146.php", "新北市立新埔國民中學公開段考試題頁", "cross-cultural reading, comparison, respect, and synthesis"),
]

DATA = [
    ("comparison dimension", "A student compares a local lantern event with Diwali. Which comparison dimension is most useful?", ["How light is used and what meaning each celebration gives it", "Which country has the better people", "Which festival should replace the other", "How many unrelated sports are played"], "A", "Light-related activities can be compared through their meanings and practices without ranking cultures."),
    ("shared purpose", "One festival features family moon viewing and another features a community harvest meal. What possible similarity is supported?", ["Both bring people together around a meaningful celebration", "Both must occur on the exact same day", "Both use the same food and language", "Neither includes a social activity"], "A", "The descriptions support a shared social purpose even though the activities differ."),
    ("difference in activity", "A local festival includes boat races, while a foreign festival includes a street parade. What is the clearest difference?", ["Their main public activities are different", "One celebration has no participants", "Both activities are exactly the same", "The festivals cannot be compared at all"], "A", "Boat racing and a street parade are distinct activities named in the descriptions."),
    ("comparison evidence", "A student claims two festivals have the same purpose. Which evidence would best support the claim?", ["Both descriptions explicitly say the events express thanks and bring families together", "Both festival names have the same number of letters", "The events are held in countries with different flags", "One festival has a longer poster"], "A", "Shared stated purposes are relevant evidence for a comparison claim."),
    ("careful wording", "Which sentence makes a fair comparison between a lantern festival and a light festival?", ["Both use light in celebrations, but their stories and local practices may differ.", "One tradition is correct and the other is foolish.", "They are identical because both include light.", "No cultural event can be compared using evidence."], "A", "The sentence identifies a similarity while leaving room for meaningful differences."),
    ("avoid stereotype", "A visitor sees one unusual custom at a festival. What should the visitor avoid concluding?", ["That every person in the culture always behaves exactly that way", "That the custom may have a specific context", "That the event should be understood from reliable explanations", "That different communities may celebrate in different ways"], "A", "One observed practice cannot support a universal claim about every person or event."),
    ("same activity different meaning", "Two festivals both include special clothing, but one uses it for a procession and the other for a family ceremony. What does this show?", ["The same visible feature can have different meanings in different contexts", "Clothing always has one universal meaning", "The festivals must be the same event", "The clothing makes cultural context unnecessary"], "A", "Purpose and setting determine how a shared feature should be interpreted."),
    ("organization", "Which organizer best supports a paragraph comparing two festivals?", ["Festival A: time and purpose → Festival B: time and purpose → shared point → key difference", "List random foods from both events → change to weather → stop", "Describe only Festival A → claim the comparison is complete", "Give opinions first and never identify either festival"], "A", "The organizer gives each event context before synthesizing a similarity and difference."),
    ("respectful response", "A classmate says a foreign festival looks strange. Which response encourages informed comparison?", ["Let's read about its purpose and ask how participants understand the practice.", "Yes, unfamiliar customs are always wrong.", "We should copy it without learning anything.", "There is no reason to discuss another culture."], "A", "The response replaces quick judgment with context and participants' perspectives."),
    ("integrated comparison", "A presentation compares a Taiwanese festival and an overseas festival using dates, main activities, family or community roles, and meanings. Which conclusion is best?", ["They differ in practices and history, yet both show how communities use celebrations to express shared values.", "One must be better because its date comes first.", "Dates are enough; activities and meanings do not matter.", "The presentation proves all festivals are identical."], "A", "The conclusion synthesizes specific differences with a supported broader similarity."),
]


def make(index, row):
    topic, prompt, choices, answer, explanation = row
    options = [{"id": chr(65 + i), "text": text} for i, text in enumerate(choices)]
    refs = [{"url": url, "title": f"{title}；僅取國內外節慶的比較維度、共同點、差異、證據、尊重與整合表達能力方向，未複製原題、選項、圖表或答案。", "year": "113-114", "subject": "english", "locator": locator, "observedPattern": "公開英文評量常以兩則節慶資料要求比較日期、活動、目的、角色與意義，並以證據表達相同與相異之處，避免價值排序；本題為獨立改寫。", "reuseDecision": "pattern-only", "status": "recorded", "locatorLevel": "paper"} for url, title, locator in SOURCES]
    steps = [
        f"Read both festival descriptions and identify the comparison target: {topic}.",
        "Create the same comparison categories for both events, such as time, activity, purpose, participants, practice, and meaning.",
        f"Use only matching evidence and choose the fair similarity, difference, organization, or conclusion; the correct answer is {answer}.",
        f"Explain how the evidence supports comparison without ranking or stereotyping cultures: {explanation}",
        "Reread both descriptions and check that the conclusion distinguishes what is shared from what is specific to one event.",
    ]
    return {"id": f"question-english-performance-8-iv-3-{index}", "subject": "english", "type": "single-choice", "prompt": prompt, "options": options, "knowledgeIds": ["kg-english-performance-8-iv-3"], "difficulty": "medium", "answer": {"value": answer, "explanation": explanation + f" Correct answer: {answer}"}, "provenance": {"origin": "original", "license": "All rights reserved", "sourceUrl": SOURCES[0][0], "sourceLocator": "Public-school English assessment materials; this item studies cross-cultural festival comparison, evidence, respectful wording, similarities, differences, and synthesis only and does not reproduce an original question, option, image, or text.", "authoringNote": "Written independently from the official English curriculum KG and three public-school English assessment sources; comparison contexts, options, explanations, and transfer tasks are original; pending second-round AI/Terra content review."}, "reviewStatus": "draft", "updatedAt": "2026-09-09", "lessonId": "lesson-english-performance-8-iv-3", "examPatternRefs": refs, "solutionStrategy": "Compare the same categories in both descriptions, cite evidence for each claim, and state similarities and differences with respectful, non-ranking language.", "solutionSteps": steps}


for index, row in enumerate(DATA, 1):
    (OUT / f"question-english-performance-8-iv-3-{index}.json").write_text(json.dumps(make(index, row), ensure_ascii=False, indent=2) + "\n", encoding="utf-8")
print(f"rewrote {len(DATA)} questions")
