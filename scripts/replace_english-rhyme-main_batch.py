"""獨立替換 1-Ⅳ-5 簡易歌謠韻文主要內容題。"""
from __future__ import annotations
import json
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
SOURCE = "https://www.grow22.com/download/114/114_cp/02-1_114P_English.pdf"
CURRICULUM = json.loads((ROOT / "curriculum/english/performance-1-iv-5.json").read_text())["source"]["url"]
LESSON = "lesson-english-performance-1-iv-5"
KNOWLEDGE = "kg-english-performance-1-iv-5"
ITEMS = [
    ("Read the original rhyme: 'Tap, tap, little rain / Green leaves wake along the lane.' What is it mainly about?", ["Rain helping plants wake and grow.", "A train leaving the lane.", "A child losing a green book.", "A dry road with no weather."], "A", "The rain and waking green leaves create a nature scene about growth."),
    ("Read: 'One small step, then one more / We reach the bright classroom door.' What idea is expressed?", ["Steady steps can help us reach a goal.", "The classroom door is locked forever.", "The speaker refuses to walk.", "The poem is about buying a door."], "A", "The repeated steps lead to reaching the classroom, suggesting steady progress."),
    ("Read: 'Round moon, quiet night / Stars sprinkle silver light.' What scene is described?", ["A calm night sky.", "A noisy market at noon.", "A storm under the ocean.", "A classroom without windows."], "A", "Moon, stars, and quietness together describe a calm night sky."),
    ("Read: 'Clap for friends, cheer for all / We rise together when some fall.' What is the main message?", ["Support from friends helps people keep going.", "Everyone should compete alone.", "Clapping makes people fall.", "The lines describe a silent room."], "A", "Cheering and rising together express encouragement and cooperation."),
    ("Read: 'Pack a hat and fill your cup / Morning hikers, wake up!' What are the lines mainly doing?", ["Giving a short reminder for hikers.", "Describing a sleeping fish.", "Explaining how to repair a cup.", "Saying that mornings should be dark."], "A", "The lines remind hikers to prepare with a hat and water."),
    ("Read: 'Blue waves roll, white clouds glide / A small boat moves with the tide.' What is the setting?", ["A boat traveling on the sea.", "A train crossing a desert.", "A bird inside a classroom.", "A market under the ground."], "A", "Waves, clouds, a boat, and the tide establish a sea setting."),
    ("Read: 'Share the seeds, share the sun / A garden grows for everyone.' What value is emphasized?", ["Sharing can benefit the whole group.", "Gardens grow without any care.", "Sunlight belongs to one person.", "Seeds should never be shared."], "A", "Sharing resources is linked with a garden that benefits everyone."),
    ("Read: 'Slowly, softly, snowflakes fall / White roofs cover one and all.' What is the main image?", ["Snow covering roofs in a quiet scene.", "Rain flooding a busy airport.", "Leaves falling in summer heat.", "A roof flying above the clouds."], "A", "The image focuses on softly falling snow covering roofs."),
    ("Read: 'Turn the page, begin again / New ideas bloom like rain.' What does the verse encourage?", ["Starting again can bring new ideas.", "Never reading another page.", "Watering books with rain.", "Closing every notebook forever."], "A", "Turning the page and beginning again are connected with fresh ideas."),
    ("Read: 'Listen close to every beat / Walking makes the day complete.' What is the verse mainly about?", ["Finding rhythm and enjoyment in walking.", "Avoiding every sound outdoors.", "A beat that stops all movement.", "A day spent repairing shoes."], "A", "The beat and walking are joined to express enjoyment of movement and rhythm."),
]

def main() -> None:
    for i, (prompt, options, _correct, explanation) in enumerate(ITEMS, 1):
        path = ROOT / "questions/english" / f"question-english-performance-1-iv-5-{i}.json"
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
            "sourceLocator": "114 年國中教育會考英語科閱讀公開試題；研究簡易韻文的情境、意象、主旨、訊息與價值判讀；課綱：" + CURRICULUM,
            "authoringNote": "自編短韻文與選項，未重製任何歌曲、歌詞、詩文、公開試題文字或音檔；待第二輪 AI 內容複核。"}
        data["reviewStatus"] = "draft"
        data["updatedAt"] = "2026-08-28"
        path.write_text(json.dumps(data, ensure_ascii=False, indent=2) + "\n")
    print("replaced 10 rhyme-main questions")

if __name__ == "__main__":
    main()
