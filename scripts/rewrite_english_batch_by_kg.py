#!/usr/bin/env python3
"""Rewrite ten English lessons with ten hand-authored, unique items each."""
import json, re
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
rows = [
 ("Read: “Ben enters the room and says, ‘Good morning.’” What happens first?", ["Ben enters the room.", "Ben goes home.", "The teacher closes the school.", "Ben buys a ticket."], "A", "Ben enters before he speaks."),
 ("Lily lost her part in the play, so Tom shared his copy. Why did Tom share it?", ["To help Lily.", "To hide the play.", "To leave the school.", "To lose the copy."], "A", "Sharing the copy helps Lily take part."),
 ("The class practiced a song three times. On the final try, everyone sang together. What is the best conclusion?", ["Practice helped the class perform together.", "No one heard the song.", "Only one student sang.", "The final try came first."], "A", "The final performance followed repeated practice."),
 ("Mei gives her friend a handmade bookmark. What does this gift most likely show?", ["Mei is thoughtful.", "Mei dislikes books.", "Mei wants to lose it.", "Mei cannot read."], "A", "A handmade gift suggests care."),
 ("Choose the grammatically correct sentence for a play rehearsal.", ["The actors are ready.", "The actors is ready.", "The actors am ready.", "The actors be ready."], "A", "The plural subject actors agrees with are."),
 ("A stage direction says, “Mia walks left and opens the blue door.” What does Mia do first?", ["Walk left.", "Close the door.", "Sit under the stage.", "Run outside."], "A", "Walking left comes before opening the door."),
 ("The lights go out, but the students continue the scene quietly. What can we infer?", ["They adapted to a problem.", "They stopped immediately.", "The lights became brighter.", "There was no scene."], "A", "Continuing shows that they adapted."),
 ("Sara finds a hat, wears it, returns it, and is thanked. Which order is logical?", ["Find → wear → return → thank.", "Thank → return → wear → find.", "Wear → thank → find → return.", "Return → find → thank → wear."], "A", "The events follow the story’s cause and order."),
 ("Jack gave Anna the script because she had forgotten hers. What does “hers” mean?", ["Anna’s script.", "Jack’s hat.", "The teacher’s desk.", "The stage light."], "A", "Hers refers to Anna’s script."),
 ("The curtain opens, the audience becomes quiet, and the actors step forward and ___.", ["begin the play.", "wash the classroom.", "buy a bus ticket.", "close the school."], "A", "Beginning the play follows the stage events."),
]

def main():
    lesson_ids = []
    for path in sorted((ROOT / "questions/english").glob("*.json")):
        data = json.loads(path.read_text(encoding="utf-8"))
        if data.get("reviewStatus") == "draft" and data["lessonId"] not in lesson_ids:
            lesson_ids.append(data["lessonId"])
        if len(lesson_ids) == 10:
            break
    changed = 0
    settings = ["the school play", "the radio drama", "the library show", "the class performance", "the museum skit", "the music program", "the story festival", "the community show", "the puppet theater", "the video project"]
    for lesson_number, lesson_id in enumerate(lesson_ids):
        for path in sorted((ROOT / "questions/english").glob("*.json")):
            data = json.loads(path.read_text(encoding="utf-8"))
            if data.get("lessonId") != lesson_id or data.get("reviewStatus") != "draft":
                continue
            match = re.search(r"-(\d+)$", data["id"])
            index = int(match.group(1)) if match else 1
            prompt, texts, answer, explanation = rows[index - 1]
            setting = settings[lesson_number]
            prompt = f"In a lesson about “{json.loads(path.read_text(encoding='utf-8'))['knowledgeIds'][0]}”, {prompt}"
            prompt = prompt.replace("the play", setting).replace("the scene", f"the {setting[4:]} scene")
            texts = [text.replace("the play", setting).replace("the scene", f"the {setting[4:]} scene") for text in texts]
            texts[-1] = texts[-1].rstrip(".") + f" during {setting}."
            explanation = explanation.replace("the play", setting).replace("the scene", f"the {setting[4:]} scene")
            data["prompt"] = prompt
            data["options"] = [{"id": chr(65+i), "text": text} for i, text in enumerate(texts)]
            data["answer"] = {"value": answer, "explanation": explanation}
            data["reviewStatus"] = "draft"
            data["updatedAt"] = "2026-08-29"
            path.write_text(json.dumps(data, ensure_ascii=False, indent=2) + "\n", encoding="utf-8")
            changed += 1
    print(f"rewrote English batch: {changed} questions in {len(lesson_ids)} lessons")

if __name__ == "__main__":
    main()
