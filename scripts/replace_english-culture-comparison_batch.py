"""獨立替換 C-Ⅳ-3 文化習俗比較題。"""
from __future__ import annotations
import json
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
SOURCE = "https://www.yacjh.kh.edu.tw/upload/221/101_30637/114%E4%B8%8B%E5%AD%B8%E6%9C%9F%E7%AC%AC%E4%B8%80%E6%AC%A1%E6%AE%B5%E8%80%83%E4%B8%89%E5%B9%B4%E7%B4%9A%E8%8B%B1%E6%96%87.pdf"
CURRICULUM = json.loads((ROOT / "curriculum/english/content-c-iv-3.json").read_text())["source"]["url"]
LESSON = "lesson-english-content-c-iv-3"
KNOWLEDGE = "kg-english-content-c-iv-3"
ITEMS = [
    ("Region A serves a shared dish at family meals; Region B gives each person a separate plate. What is a fair comparison?", ["The serving customs differ, but both meals can be family meals.", "Region A has no families.", "Only separate plates show respect.", "The two regions must eat the same food."], "A", "The statement identifies a difference without claiming that one custom is universally correct."),
    ("In one school, students greet teachers with a bow; in another, they say hello and smile. What can we conclude?", ["Both are greeting practices, expressed in different ways.", "Smiling can never be respectful.", "A bow is not a greeting.", "Students in one school do not speak."], "A", "Both actions can communicate respect while their forms differ."),
    ("A report compares two festivals and lists the date, main activity, and reason for each. Why is this useful?", ["It compares the same categories in an organized way.", "It proves one festival is better.", "It removes all cultural context.", "It shows that dates are unimportant."], "A", "Using the same categories makes similarities and differences easier to see."),
    ("Country X gives small gifts when visiting a home; Country Y usually brings flowers. Which statement is supported?", ["Visitors in the two countries may show appreciation with different gifts.", "People in Country Y dislike hosts.", "Gifts have the same form everywhere.", "Neither country welcomes visitors."], "A", "The evidence supports different forms of a similar social purpose."),
    ("A student says, 'This custom is strange because I have never seen it.' What is a better approach?", ["Learn its purpose and context before evaluating it.", "Tell everyone to stop the custom.", "Assume unfamiliar means wrong.", "Describe all members with one label."], "A", "Familiarity is not a fair standard; context helps prevent judgment."),
    ("Two communities use different foods in a harvest celebration because their crops differ. What explains the difference?", ["Local environments and resources can shape traditions.", "Food never relates to place.", "Both communities have identical crops.", "A celebration cannot change over time."], "A", "Different local crops can influence what communities prepare."),
    ("Which question best compares two customs without ranking them?", ["What is similar, and what is different, about how each custom is practiced?", "Which custom is correct for everyone?", "Why is one custom bad?", "Which people should give up their custom?"], "A", "The question asks for evidence-based similarities and differences rather than a premature ranking."),
    ("A class finds that both regions celebrate family reunions, but one does so in spring and the other in autumn. What is the comparison?", ["They share a purpose but differ in timing.", "They have no shared feature.", "Both celebrations must happen in spring.", "The seasons have no names."], "A", "The information gives one similarity and one difference."),
    ("A student interviews people from two communities before writing a comparison. Why is this better than guessing?", ["It uses information from people connected with the practices.", "Interviews always make customs identical.", "Guessing is more accurate than evidence.", "People cannot explain their own customs."], "A", "Community voices provide relevant evidence for a respectful comparison."),
    ("Which conclusion is appropriately limited after comparing two examples?", ["These two examples differ in greeting style; they do not represent every person in either place.", "Everyone in both places greets exactly this way.", "One example proves a whole country has no culture.", "The comparison tells us nothing at all."], "A", "A careful conclusion states the evidence's scope and avoids overgeneralization."),
]

def main() -> None:
    for i, (prompt, options, _correct, explanation) in enumerate(ITEMS, 1):
        path = ROOT / "questions/english" / f"question-english-content-c-iv-3-{i}.json"
        data = json.loads(path.read_text())
        shift = i % 4
        rotated = options[shift:] + options[:shift]
        data["prompt"] = prompt
        data["options"] = [{"id": chr(65 + j), "text": text} for j, text in enumerate(rotated)]
        data["answer"] = {"value": chr(65 + ((4 - shift) % 4)), "explanation": explanation}
        data["knowledgeIds"] = [KNOWLEDGE]
        data["lessonId"] = LESSON
        data["difficulty"] = "medium"
        data["provenance"] = {"origin": "original", "license": "All rights reserved", "sourceUrl": SOURCE,
            "sourceLocator": "鹽埕國中 114 學年度第 2 學期英文段考；研究兩種文化的相同目的、不同做法、比較類別、訪談證據與結論範圍；課綱：" + CURRICULUM,
            "authoringNote": "自編文化比較情境與選項，未重製公開試題文字、選項或圖片；待第二輪 AI 內容複核。"}
        data["reviewStatus"] = "draft"
        data["updatedAt"] = "2026-08-28"
        path.write_text(json.dumps(data, ensure_ascii=False, indent=2) + "\n")
    print("replaced 10 culture-comparison questions")

if __name__ == "__main__":
    main()
