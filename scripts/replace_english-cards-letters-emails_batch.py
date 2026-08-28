"""獨立替換 Ae-Ⅳ-4 卡片、書信與電郵閱讀題。"""
from __future__ import annotations
import json
from pathlib import Path

ROOT=Path(__file__).resolve().parents[1]
SOURCE="https://www.grow22.com/download/114/114_cp/02-1_114P_English.pdf"
CURRICULUM=json.loads((ROOT/"curriculum/english/content-ae-iv-4.json").read_text())["source"]["url"]
LESSON="lesson-english-content-ae-iv-4"; KNOWLEDGE="kg-english-content-ae-iv-4"
ITEMS=[
("Read: \"Dear Emma, Thanks for the birthday card. I will visit you next Saturday. —Lily\" Who wrote the message?",["Lily","Emma","Lily's teacher","The birthday card"],"A","The signature at the end identifies Lily as the writer."),
("Read: \"Hi Dad, The soccer practice starts at 4:00 p.m. today, not 5:00. Please pick me up at 6:00. —Kevin\" What time should Dad pick Kevin up?",["At 6:00 p.m.","At 4:00 p.m.","At 5:00 p.m.","Tomorrow morning"],"A","Kevin asks Dad to pick him up at 6:00."),
("Read: \"To: Sara\nSubject: Group project\nCan we meet in the library after school on Tuesday?\n—Mia\" Why did Mia write the email?",["To arrange a meeting","To cancel school","To buy a library book","To wish Sara happy birthday"],"A","The question about meeting in the library concerns the group project."),
("Read: \"Dear Uncle Tom, I am sending you a photo of our class garden. We planted tomatoes last month.\" What is attached or sent?",["A photo","A ticket","A recipe","A map"],"A","The message says the writer is sending a photo of the class garden."),
("Read: \"Happy New Year! I hope your family has a wonderful holiday.\" What kind of message is this?",["A holiday greeting","A complaint","A school rule","A shopping list"],"A","The greeting wishes someone a happy New Year and holiday."),
("Read: \"Dear Coach, I cannot attend practice today because I have a fever. I will return on Friday. —Sam\" Why will Sam miss practice?",["Sam has a fever.","Sam has a new coach.","Practice is on Friday only.","Sam is traveling for a game."],"A","Sam directly gives a fever as the reason for missing practice."),
("Which opening is most suitable for a formal email to a school office?",["Dear Office Staff,","Hey buddy,","Yo!","Hi, my best friend!"],"A","Dear Office Staff is polite and suitable for an official recipient."),
("Read: \"Please reply by Wednesday if you can join the field trip.\" What should the reader do?",["Reply by Wednesday","Wait until next month","Go to the field trip without replying","Send a birthday card"],"A","The message requests a reply no later than Wednesday."),
("Read: \"Dear Maya, Thank you for watering my plants while I was away. They look healthy! —Jin\" What did Maya do?",["She watered Jin's plants.","She bought new plants.","She went away with Jin.","She wrote the thank-you note."],"A","Jin thanks Maya for watering the plants during Jin's absence."),
("Which closing is most suitable for a friendly email?",["Best wishes,","End of report.","No reply needed ever.","Warning:"],"A","Best wishes is a common polite closing for a friendly email."),
]
def main():
 for i,(prompt,options,_answer,explanation) in enumerate(ITEMS,1):
  path=ROOT/"questions/english"/f"question-english-content-ae-iv-4-{i}.json"; data=json.loads(path.read_text()); shift=i%4; rotated=options[shift:]+options[:shift]
  data["prompt"]=prompt; data["options"]=[{"id":chr(65+j),"text":v} for j,v in enumerate(rotated)]; data["answer"]={"value":chr(65+((4-shift)%4)),"explanation":explanation}; data["knowledgeIds"]=[KNOWLEDGE]; data["lessonId"]=LESSON; data["difficulty"]="medium"
  data["provenance"]={"origin":"original","license":"All rights reserved","sourceUrl":SOURCE,"sourceLocator":f"114 年國中教育會考英語科閱讀公開試題；研究卡片、書信、電郵的寄件人、收件人、日期、目的、行動與回覆判讀能力方向；課綱：{CURRICULUM}","authoringNote":"自編卡片、書信、電郵與選項，未重製任何原題文字、版面或答案；待第二輪 AI 內容複核。"}; data["reviewStatus"]="draft"; data["updatedAt"]="2026-08-28"; path.write_text(json.dumps(data,ensure_ascii=False,indent=2)+"\n")
 print("replaced 10 cards-letters-emails questions")
if __name__=="__main__": main()
