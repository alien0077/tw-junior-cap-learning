import json
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
url = "https://www.zmjhs.tyc.edu.tw/uploads/neilfilefolder/14file/file/4_63_5112%E8%8B%B1%E8%AA%9E%E9%A0%98%E5%9F%9F%E8%AA%B2%E7%A8%8B%E8%A8%88%E7%95%AB.pdf"
labels = ["複習國小 Starter", "Lesson 1 What's This?", "Lesson 2 Where Is Annie From?", "Lesson 3 Please Bring Your Favorite Dish", "Lesson 4 There Are Two Hippos in the House", "Lesson 5 My Friend Is Showing Me Around", "Lesson 6 What Are You Doing?", "Reading Corner I"]
entries = [{"chapterCode": f"unit-{i}", "chapterLabel": label, "knowledgeIds": ["kg-english-learning-content"], "relation": "primary", "confidence": "medium", "notes": "仁美國中公開課程計畫列為南一版國中英語 7 上單元；KG 先掛英文內容根節點，逐碼對照待核驗。"} for i, label in enumerate(labels, 1)]
out = {"id":"mapset-english-nani-schoolplan-2026","subject":"english","publisher":"nani","academicYear":"115","source":{"type":"book-inspection","url":url,"locator":"桃園市仁美國中 112 學年度英語領域課程計畫；南一版國中英語 7 上 Starter、Lesson 1–6 與 Reading Corner I","verifiedAt":"2026-08-26","verifiedBy":"Codex public school-plan verification","confidence":"medium","editionNote":"校方公開課程計畫為 112 學年度，作為南一版本單元交叉證據；不等同南一出版社正式目次。"},"mappingMethod":"school-plan-unit-index-to-official-english-kg-conservative-cross-reference","volumes":[{"volume":"1","grade":"7","semester":"上","entries":entries}],"status":"verified","notes":"保存 8 筆單元 metadata；其餘南一英文冊別仍待公開可核驗單元來源。"}
(ROOT/"textbook-mapping/english/nani-schoolplan-2026.json").write_text(json.dumps(out,ensure_ascii=False,indent=2)+"\n")
print("wrote",len(entries),"entries")
