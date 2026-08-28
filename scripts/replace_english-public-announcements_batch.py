"""獨立替換 Ae-Ⅳ-3 公共場所廣播閱讀題。"""
from __future__ import annotations
import json
from pathlib import Path

ROOT=Path(__file__).resolve().parents[1]
SOURCE="https://www.grow22.com/download/114/114_cp/02-1_114P_English.pdf"
CURRICULUM=json.loads((ROOT/"curriculum/english/content-ae-iv-3.json").read_text())["source"]["url"]
LESSON="lesson-english-content-ae-iv-3"; KNOWLEDGE="kg-english-content-ae-iv-3"
ITEMS=[
("Announcement: \"The 3:20 train to Hsinchu will leave from Platform 2, not Platform 4.\" Where should passengers go?",["Platform 2","Platform 4","The ticket office","The parking lot"],"A","The announcement changes the departure platform to Platform 2."),
("Announcement: \"Attention shoppers: the bookstore will close at 9 p.m. today.\" When will it close?",["At 9 p.m.","At 7 p.m.","At noon","Tomorrow morning"],"A","The announcement says the bookstore will close at 9 p.m."),
("Announcement: \"A blue backpack was found near the west entrance. Please claim it at the information desk.\" Where can the owner get it?",["At the information desk","At the west entrance floor","In the bookstore","On the train"],"A","The owner is asked to claim the backpack at the information desk."),
("Announcement: \"Due to rain, today's outdoor concert has moved to the community hall.\" Why was it moved?",["Because of rain","Because the hall is closed","Because the concert ended","Because tickets were free"],"A","The phrase Due to rain gives the reason for moving the concert."),
("Announcement: \"Please keep your ticket until you leave the museum.\" What should visitors do?",["Keep their tickets","Give tickets to the bus driver","Throw tickets away immediately","Buy a new ticket every hour"],"A","Visitors should keep the ticket until they leave."),
("Announcement: \"The elevator is being repaired. Use the stairs beside the east entrance.\" What should people use?",["The stairs by the east entrance","The repaired elevator","The west parking lot","The roof"],"A","The announcement directs people to the stairs beside the east entrance."),
("Announcement: \"Flight 208 is delayed for thirty minutes. Please wait at Gate 6.\" What is delayed?",["Flight 208","Gate 6","The airport bus","The announcement"],"A","The flight number named in the announcement is 208."),
("Announcement: \"Library members may return books through the box outside the main door after closing.\" When may they use the box?",["After the library closes","Only before opening","During a concert","Before borrowing any book"],"A","The word after indicates that the return box is available after closing."),
("Announcement: \"For safety, do not stand behind the yellow line while the bus is moving.\" What is the announcement about?",["A safety rule on a bus","A new bus route","A lost wallet","A library schedule"],"A","The instruction tells passengers how to stay safe while the bus moves."),
("Announcement: \"The school office will answer phone calls from 8:00 to 4:30 on weekdays.\" When can people call?",["On weekdays between 8:00 and 4:30","Every night after 10:00","Only on Sundays","At any time"],"A","The stated calling hours are 8:00 to 4:30 on weekdays."),
]
def main():
 for i,(prompt,options,_answer,explanation) in enumerate(ITEMS,1):
  path=ROOT/"questions/english"/f"question-english-content-ae-iv-3-{i}.json"; data=json.loads(path.read_text()); shift=i%4; rotated=options[shift:]+options[:shift]
  data["prompt"]=prompt; data["options"]=[{"id":chr(65+j),"text":v} for j,v in enumerate(rotated)]; data["answer"]={"value":chr(65+((4-shift)%4)),"explanation":explanation}; data["knowledgeIds"]=[KNOWLEDGE]; data["lessonId"]=LESSON; data["difficulty"]="medium"
  data["provenance"]={"origin":"original","license":"All rights reserved","sourceUrl":SOURCE,"sourceLocator":f"114 年國中教育會考英語科閱讀公開試題；研究公共場所廣播的時間、地點、物品、行動、原因與安全資訊判讀能力方向；課綱：{CURRICULUM}","authoringNote":"自編廣播內容與選項，未重製任何原題文字、圖表或答案；待第二輪 AI 內容複核。"}; data["reviewStatus"]="draft"; data["updatedAt"]="2026-08-28"; path.write_text(json.dumps(data,ensure_ascii=False,indent=2)+"\n")
 print("replaced 10 public-announcement questions")
if __name__=="__main__": main()
