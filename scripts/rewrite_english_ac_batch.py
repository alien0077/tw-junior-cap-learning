#!/usr/bin/env python3
"""Rewrite four Ac English lessons with vocabulary-specific item banks."""
import json
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
BANKS = {
    "lesson-english-content-ac": [
        ("What does “borrow” mean?", "use something and return it later", ["break something on purpose", "sell something immediately", "hide something forever"]),
        ("What does “ancient” mean?", "very old", ["very noisy", "very wet", "very new"]),
        ("What does “crowded” mean?", "full of people", ["full of empty seats", "far from a town", "easy to carry"]),
        ("What does “repair” mean?", "fix something damaged", ["throw something away", "paint something blue", "find something new"]),
        ("What does “protect” mean?", "keep someone or something safe", ["make something heavier", "leave something outside", "make something invisible"]),
        ("What does “delicious” mean?", "pleasant to taste", ["difficult to spell", "dangerous to touch", "too far to reach"]),
        ("What does “journey” mean?", "a trip from one place to another", ["a kind of food", "a classroom rule", "a type of weather"]),
        ("What does “patient” mean?", "calmly willing to wait", ["unable to hear", "ready to run", "full of anger"]),
        ("What does “discover” mean?", "find something for the first time", ["close a door", "forget a name", "copy a sentence"]),
        ("What does “quiet” mean?", "making little noise", ["moving very fast", "having many colors", "costing a lot"]),
    ],
    "lesson-english-content-ac-iv-1": [
        ("A sign says “EXIT.” Where should visitors go?", "out of the building", ["into the building", "to the kitchen", "to the roof"]),
        ("A sign says “PUSH.” What should you do?", "press the door", ["pull the door", "paint the door", "lock every window"]),
        ("A sign says “DANGER.” What should you do?", "be careful", ["run toward the danger", "take a nap", "buy a ticket"]),
        ("A sign says “ENTRANCE.” What does it show?", "a way to go in", ["a way to go out", "a place to sleep", "a place to park only"]),
        ("A sign says “NO FOOD.” What is not allowed?", "eating", ["reading", "walking", "asking a question"]),
        ("A sign says “WET FLOOR.” What should people do?", "walk carefully", ["run quickly", "sit on the floor", "turn off the sun"]),
        ("A sign says “KEEP LEFT.” Where should people walk?", "on the left side", ["on the roof", "in the parking lot", "behind the building"]),
        ("A sign says “OPEN.” What does it tell customers?", "the place is not closed", ["the place is underwater", "the place is dangerous", "the place has no door"]),
        ("A sign says “WAIT HERE.” What should visitors do?", "stay in that place", ["leave immediately", "climb the wall", "open the cash register"]),
        ("A sign says “NO PHOTOS.” What is forbidden?", "taking pictures", ["wearing shoes", "reading maps", "drinking water"]),
    ],
    "lesson-english-content-ac-iv-2": [
        ("What does “Please open your book” ask a student to do?", "open the book", ["close the window", "leave the room", "draw a map"]),
        ("What does “Work with a partner” mean?", "work with another student", ["work alone", "go home", "erase the board"]),
        ("What does “Listen and repeat” ask students to do?", "listen and say it again", ["write a long letter", "run outside", "turn off the light"]),
        ("What does “Raise your hand” mean?", "lift your hand", ["lower your voice", "open your bag", "stand at the door"]),
        ("What does “Take out your pencil” mean?", "get your pencil", ["take a bus", "close your eyes", "wash your hands"]),
        ("What does “Look at the board” ask students to do?", "watch the board", ["read under the desk", "leave school", "play a game"]),
        ("What does “Circle the answer” mean?", "draw a circle around it", ["cross out every answer", "read the title aloud", "put it in a bag"]),
        ("What does “Check your partner’s work” mean?", "look over a partner’s work", ["hide the paper", "write a new story", "go to the library"]),
        ("What does “Read aloud” mean?", "read so others can hear", ["read only at home", "close the book", "draw a picture"]),
        ("What does “Hand in your paper” mean?", "give your paper to the teacher", ["tear up the paper", "borrow a pencil", "open a window"]),
    ],
    "lesson-english-content-ac-iv-3": [
        ("A: “Would you like some tea?” B: “___”", "Yes, please.", ["It is under the chair.", "I am fourteen years old.", "At the bus stop."]),
        ("A: “How was your trip?” B: “___”", "It was exciting.", ["It starts at noon.", "It is next to the door.", "Yes, I have a pencil."]),
        ("A: “Could you help me?” B: “___”", "Sure. What do you need?", ["It is very sunny.", "I am on the second floor.", "No, it was yesterday."]),
        ("A: “I’m sorry I’m late.” B: “___”", "That’s all right.", ["It costs ten dollars.", "It is behind the bus.", "Yes, I am late yesterday."]),
        ("A: “What time shall we meet?” B: “___”", "At half past three.", ["Near the window.", "I met my cousin.", "Yes, we are meeting."]),
        ("A: “Where is your umbrella?” B: “___”", "It is beside the door.", ["At seven o’clock.", "I am thirteen.", "Yes, I can umbrella."]),
        ("A: “May I use your ruler?” B: “___”", "Of course. Here you are.", ["It is very tall.", "I used it tomorrow.", "No, I am a ruler."]),
        ("A: “Why are you wearing a coat?” B: “___”", "Because it is cold.", ["On the blue chair.", "At four o’clock.", "Yes, I wore yesterday."]),
        ("A: “Have you finished the task?” B: “___”", "Yes, I finished it.", ["It is a long task.", "At the front gate.", "No, I am fifteen."]),
        ("A: “What does this word mean?” B: “___”", "It means “very old.”", ["It is on the page.", "At lunchtime.", "Yes, I read it."]),
    ],
}

def main():
    changed = 0
    for lesson_id, bank in BANKS.items():
        for index, (prompt, correct, wrong) in enumerate(bank, 1):
            path = ROOT / "questions/english" / f"question-english-{lesson_id.removeprefix('lesson-english-')}-{index}.json"
            if not path.exists():
                matches = [p for p in (ROOT / "questions/english").glob("*.json") if json.loads(p.read_text(encoding="utf-8")).get("lessonId") == lesson_id and p.name.endswith(f"-{index}.json")]
                if not matches: raise FileNotFoundError(f"{lesson_id} question {index}")
                path = matches[0]
            data = json.loads(path.read_text(encoding="utf-8"))
            data.update({"prompt": prompt, "options": [{"id": chr(65+i), "text": text} for i, text in enumerate([correct] + wrong)], "answer": {"value": "A", "explanation": f"The correct answer is: {correct}."}, "reviewStatus": "draft", "updatedAt": "2026-08-29"})
            path.write_text(json.dumps(data, ensure_ascii=False, indent=2) + "\n", encoding="utf-8")
            changed += 1
    print(f"rewrote Ac English batch: {changed} questions")

if __name__ == "__main__":
    main()
