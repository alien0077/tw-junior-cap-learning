import json
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
CURRICULUM_PATH = ROOT / "curriculum/english/performance-2.json"
CURRICULUM = json.loads(CURRICULUM_PATH.read_text())
SOURCE = CURRICULUM["source"]["url"]
LESSON_ID = "lesson-english-performance-2"
KG_ID = "kg-english-performance-2"

items = [
    ("在英文自我介紹中，哪一句最完整？", ["I am Kevin. I am from Tainan, and I like drawing.", "Kevin Tainan drawing.", "From Tainan Kevin.", "Drawing is Kevin."]),
    ("同學問：\"What do you usually do after school?\" 哪一個回答最合適？", ["I usually play basketball with my friends.", "At the library is my answer.", "Because it was sunny yesterday.", "Yes, I did it last week."]),
    ("你要描述教室裡的物品位置，哪一句資訊最清楚？", ["The clock is above the whiteboard, and the bag is under my desk.", "Things are in the classroom.", "The classroom is very nice.", "I went there yesterday."]),
    ("你想請同學重複剛才的說明，哪一句最適當？", ["Could you say that again, please?", "You say again yesterday.", "I am saying the classroom.", "That is not a question."]),
    ("你要表達自己支持校園二手書交換活動並說明理由，哪一句最完整？", ["I support it because students can reuse books and save money.", "I support books yesterday.", "Because the activity is a question.", "No, I am at home."]),
    ("你要向外國朋友說明從校門到圖書館的路線，哪一段最合適？", ["Go straight to the end of the hall, turn left, and the library is next to the office.", "The library likes reading.", "I went to school by bus.", "The office was open last year."]),
    ("你要報告小組活動的先後順序，哪一句最清楚？", ["First, we chose a topic. Then, we collected information and practiced the presentation.", "We topic information presentation.", "The presentation is next to the topic.", "I like practicing because it is blue."]),
    ("朋友邀請你參加週末讀書會，你想接受並確認時間，哪一句最合適？", ["Sure. What time should we meet?", "No, the time is a pencil.", "I met the book yesterday.", "Yes, I am a meeting."]),
    ("你要比較兩種交通方式並提出偏好，哪一句符合口語表達任務？", ["Taking the bus is cheaper, but I prefer riding a bike because it is healthier.", "The bus and bike are yesterday.", "Health is under the transportation.", "I do not compare any sentence."]),
    ("同學說明得不清楚，你想確認他的意思，哪一句最恰當？", ["Do you mean we should finish the poster today?", "You mean finished poster yesterday.", "The poster is a question mark.", "I am not meaning the classroom."]),
]

for index, (prompt, options) in enumerate(items, start=1):
    shift = (index - 1) % 4
    rotated = options[shift:] + options[:shift]
    answer = chr(65 + ((4 - shift) % 4))
    path = ROOT / f"questions/english/question-english-performance-2-{index}.json"
    data = {
        "id": f"question-english-performance-2-{index}",
        "subject": "english",
        "type": "single-choice",
        "prompt": prompt,
        "options": [{"id": chr(65 + i), "text": text} for i, text in enumerate(rotated)],
        "knowledgeIds": [KG_ID],
        "difficulty": "medium",
        "answer": {
            "value": answer,
            "explanation": "本題依官方英語文課綱「語言能力（說）」設計生活溝通情境；正解能完成題目指定的描述、問答、理由、順序、邀請、比較或澄清任務，其餘選項語意不完整、答非所問或不合英文表達。",
        },
        "provenance": {
            "origin": "original",
            "license": "All rights reserved",
            "sourceUrl": SOURCE,
            "sourceLocator": "官方課綱正文第 8～15 頁／PDF 第 10～17 頁；國民中學教育階段學習表現「語言能力（說）」；參考公立國中英文段考常見基本問答、生活溝通、描述與問答題型；本題為獨立改寫。",
            "authoringNote": "自編英文口語情境與選項，未重製公開試題文字、選項或圖片；待第二輪 AI 內容複核。",
        },
        "reviewStatus": "draft",
        "updatedAt": "2026-08-28",
        "lessonId": LESSON_ID,
    }
    path.write_text(json.dumps(data, ensure_ascii=False, indent=2) + "\n")

print(f"replaced {len(items)} questions for {LESSON_ID}")
