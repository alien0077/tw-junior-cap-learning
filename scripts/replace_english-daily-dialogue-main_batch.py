"""獨立替換 1-Ⅳ-4 日常對話主要內容題。"""
from __future__ import annotations
import json
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
SOURCE = "https://www.yacjh.kh.edu.tw/upload/221/101_30637/114%E4%B8%8B%E5%AD%B8%E6%9C%9F%E7%AC%AC%E4%B8%80%E6%AC%A1%E6%AE%B5%E8%80%83%E4%B8%89%E5%B9%B4%E7%B4%9A%E8%8B%B1%E6%96%87.pdf"
CURRICULUM = json.loads((ROOT / "curriculum/english/performance-1-iv-4.json").read_text())["source"]["url"]
LESSON = "lesson-english-performance-1-iv-4"
KNOWLEDGE = "kg-english-performance-1-iv-4"
ITEMS = [
    ("Dialogue: A: Did you finish the science project? B: Not yet. I need to add the chart. What is the dialogue mainly about?", ["Finishing a science project.", "Buying a new bicycle.", "Planning a birthday cake.", "Finding a lost key."], "A", "Both speakers discuss the unfinished science project and its remaining chart."),
    ("Dialogue: A: Why are you carrying an umbrella? B: It may rain on my walk home. What is the main point?", ["The speaker is preparing for possible rain.", "The speaker is going swimming.", "The umbrella belongs to the school.", "The walk home was canceled yesterday."], "A", "The second speaker explains carrying an umbrella because rain may occur."),
    ("Dialogue: A: Shall we meet at the station at six? B: Six is too early. How about seven? What are they discussing?", ["The time and place to meet.", "A train's color.", "A new station job.", "The weather last month."], "A", "The speakers negotiate a meeting place and time."),
    ("Dialogue: A: I cannot find my library card. B: Check the pocket of your backpack. What problem is being discussed?", ["A missing library card.", "A broken backpack strap.", "A late library opening.", "A new card design."], "A", "The first speaker cannot find a library card, and the second suggests where to look."),
    ("Dialogue: A: Which club will you join? B: The photography club because I enjoy taking pictures. What is the answer mainly about?", ["A club choice and its reason.", "How to repair a camera.", "Where to buy pictures.", "A sports competition result."], "A", "The response names a club and explains the speaker's reason for choosing it."),
    ("Dialogue: A: Can you help me carry this box? B: Sure, but let's use the cart. What are they mainly doing?", ["Finding a safer way to move a box.", "Ordering food at a restaurant.", "Choosing a classroom color.", "Returning a book tomorrow."], "A", "The speakers address carrying a box and choose to use a cart."),
    ("Dialogue: A: The movie starts at eight, but we still need tickets. B: I will buy them online now. What is the main idea?", ["Getting tickets before a movie.", "Writing a movie review.", "Changing the movie's ending.", "Cleaning a theater."], "A", "The problem is obtaining tickets before the movie begins."),
    ("Dialogue: A: You look tired. B: I studied late for the test. What does the conversation explain?", ["Why the student is tired.", "Where the test will be held next year.", "Why the teacher left school.", "How to buy a desk."], "A", "The second speaker gives late studying as the reason for being tired."),
    ("Dialogue: A: This soup is too hot. B: Wait a few minutes before eating it. What advice is given?", ["Let the soup cool before eating.", "Add ice to every drink.", "Leave the restaurant immediately.", "Cook a different meal tomorrow."], "A", "Waiting allows the hot soup to cool before it is eaten."),
    ("Dialogue: A: Did you send the invitation? B: Yes, and three friends have replied. What is the dialogue mainly about?", ["An invitation and the replies to it.", "A canceled train trip.", "A recipe for three friends.", "A school uniform order."], "A", "The speakers discuss sending an invitation and receiving responses."),
]

def main() -> None:
    for i, (prompt, options, _correct, explanation) in enumerate(ITEMS, 1):
        path = ROOT / "questions/english" / f"question-english-performance-1-iv-4-{i}.json"
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
            "sourceLocator": "鹽埕國中 114 學年度第 2 學期英文段考；研究日常對話主旨、問題、理由、時間地點、建議與細節判讀；課綱：" + CURRICULUM,
            "authoringNote": "自編日常對話與選項，未重製公開試題文字、選項或圖片；待第二輪 AI 內容複核。"}
        data["reviewStatus"] = "draft"
        data["updatedAt"] = "2026-08-28"
        path.write_text(json.dumps(data, ensure_ascii=False, indent=2) + "\n")
    print("replaced 10 daily-dialogue-main questions")

if __name__ == "__main__":
    main()
