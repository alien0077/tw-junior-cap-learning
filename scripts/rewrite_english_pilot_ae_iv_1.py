#!/usr/bin/env python3
"""Hand-author the first English lesson pilot before scaling the method."""
import json
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
LESSON = "lesson-english-content-ae-iv-1"
items = [
 ("Read the short script: “Ben enters the room and says, ‘Good morning.’ The teacher answers, ‘Good morning, Ben.’” What happens first?", ["Ben enters the room.", "The teacher leaves the room.", "Ben goes home.", "The teacher closes the school."], "A", "The script says that Ben enters before the greeting."),
 ("A story says: “Lily lost her part in the play, so Tom shared his copy with her.” Why did Tom share his copy?", ["He wanted to help Lily.", "He wanted to hide the play.", "He disliked reading.", "He was going home."], "A", "Sharing the copy helps Lily take part in the play."),
 ("Read: “The class practiced the song three times. On the final try, everyone sang together.” What is the best conclusion?", ["Practice helped the class perform together.", "The class never heard the song.", "Only one student sang.", "The final try happened before practice."], "A", "The final performance improved after repeated practice."),
 ("In the story “A Small Gift,” Mei gives her friend a handmade bookmark. What does the gift most likely show?", ["Mei is thoughtful.", "Mei is angry about books.", "Mei wants to lose the bookmark.", "Mei cannot read."], "A", "A handmade gift for a friend suggests care and thoughtfulness."),
 ("Choose the grammatically correct sentence for a play rehearsal.", ["The actors are ready.", "The actors is ready.", "The actors am ready.", "The actors be ready."], "A", "The plural subject “actors” agrees with “are.”"),
 ("A stage direction says: “Mia walks to the left and opens the blue door.” What should Mia do first?", ["Walk to the left.", "Close the blue door.", "Sit under the stage.", "Run outside."], "A", "The direction places walking to the left before opening the door."),
 ("Read: “The lights went out, but the students continued the scene quietly.” What can we infer?", ["The students adapted to a problem.", "The students stopped the scene immediately.", "The lights became brighter.", "The students were not in a scene."], "A", "Continuing quietly shows that the students adjusted to the lights going out."),
 ("Four events occur in a story: (1) Sara finds a hat, (2) Sara wears the hat, (3) Sara returns it, (4) the owner thanks her. Which order is logical?", ["1 → 2 → 3 → 4", "4 → 3 → 2 → 1", "2 → 4 → 1 → 3", "3 → 1 → 4 → 2"], "A", "Sara must find and wear the hat before returning it and receiving thanks."),
 ("Read: “Jack gave Anna the script because she had forgotten hers.” In this sentence, “hers” means ___.", ["Anna’s script", "Jack’s hat", "the teacher’s desk", "the stage light"], "A", "The possessive pronoun “hers” refers to Anna’s script."),
 ("Which sentence best completes this short story? “The curtain opened. The audience became quiet. The actors stepped forward and ___.”", ["began the play", "washed the classroom yesterday", "bought a bus ticket", "closed the school for a month"], "A", "Beginning the play logically follows the curtain opening and actors stepping forward."),
]

for i, (prompt, texts, answer, explanation) in enumerate(items, 1):
    path = ROOT / "questions/english" / f"question-english-content-ae-iv-1-{i}.json"
    data = json.loads(path.read_text(encoding="utf-8"))
    data.update({"prompt": prompt, "options": [{"id": chr(65+j), "text": t} for j, t in enumerate(texts)], "answer": {"value": answer, "explanation": explanation}, "reviewStatus": "draft", "updatedAt": "2026-08-29"})
    path.write_text(json.dumps(data, ensure_ascii=False, indent=2) + "\n", encoding="utf-8")
print(f"rewrote {len(items)} questions in {LESSON}")
