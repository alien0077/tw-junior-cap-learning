"""獨立替換 Ae-Ⅳ-7 敘事者觀點、態度與目的題。"""
from __future__ import annotations
import json
from pathlib import Path

ROOT=Path(__file__).resolve().parents[1]
SOURCE="https://www.grow22.com/download/114/114_cp/02-1_114P_English.pdf"
CURRICULUM=json.loads((ROOT/"curriculum/english/content-ae-iv-7.json").read_text())["source"]["url"]
LESSON="lesson-english-content-ae-iv-7"; KNOWLEDGE="kg-english-content-ae-iv-7"
ITEMS=[
("Read: \"I used to think the empty lot was useless. After neighbors planted flowers there, I began visiting it every evening.\" What is the narrator's attitude now?",["Appreciative of the garden","Angry about the flowers","Uninterested in the lot","Afraid of the neighbors"],"A","The narrator now visits the flower garden and values the change."),
("Read: \"Our class tried a silent lunch. At first it felt strange, but by the end we noticed how much food noise we usually made.\" What is the narrator mainly doing?",["Reflecting on an experience","Advertising a restaurant","Giving directions to a cafeteria","Reporting a sports score"],"A","The narrator describes and thinks about what was learned from the experience."),
("Read: \"The poster says the river is clean, yet the photo shows plastic along the bank. I want readers to check claims before believing them.\" What is the writer's purpose?",["To encourage careful evaluation of information","To invite readers to a picnic","To explain how to swim","To praise the poster's design"],"A","The writer contrasts claim and evidence to encourage readers to check information."),
("Read: \"Of course the bus was late again—but at least I enjoyed the sunrise while waiting.\" What tone does the sentence show?",["Slightly annoyed but able to find something positive","Completely terrified","Strictly scientific","Uninterested and emotionless"],"A","Again suggests annoyance, while enjoying the sunrise shows a positive response."),
("Read: \"According to the survey, 8 of 10 students prefer reusable bottles. The result is interesting, but it represents only our class.\" What limitation does the narrator mention?",["The survey covers only one class.","The survey has no numbers.","Every student prefers disposable bottles.","The result was collected worldwide."],"A","The narrator explicitly limits the result to the writer's class."),
("Read: \"Please bring a small towel, water, and comfortable shoes. We will meet at the gym at 8:00.\" What is the writer's purpose?",["To give preparation instructions","To tell a mystery story","To compare two books","To complain about shoes"],"A","The writer lists what to bring and where and when to meet."),
("Read: \"When Mei returned the lost wallet, she did not wait for a reward. Her action reminded me that honesty can be quiet.\" How does the narrator view Mei?",["With respect","With suspicion","With jealousy","With confusion about her name"],"A","The narrator praises Mei's honest action as quiet but meaningful."),
("Read: \"The new rule may sound inconvenient, but it gives every student a chance to use the computer.\" What is the narrator's position?",["The rule has a disadvantage but also a fair benefit.","The rule is entirely useless.","The narrator has never seen a computer.","The rule benefits only one student."],"A","May sound inconvenient signals a drawback, while every student signals a fairness benefit."),
("Read: \"I describe the steps below so anyone can grow bean sprouts at home.\" Why did the narrator write the passage?",["To explain a process","To describe a holiday","To tell readers a joke","To compare two cities"],"A","The phrase describe the steps shows that the purpose is to explain a process."),
("Read: \"Some people call the old bridge ugly. I see its worn stones as reminders of the town's history.\" What viewpoint does the narrator express?",["The bridge has historical value despite its worn appearance.","The bridge should be removed immediately.","The bridge has never been used.","The narrator dislikes all history."],"A","The narrator gives a personal, positive interpretation of the old stones."),
]
def main():
 for i,(prompt,options,_answer,explanation) in enumerate(ITEMS,1):
  path=ROOT/"questions/english"/f"question-english-content-ae-iv-7-{i}.json"; data=json.loads(path.read_text()); shift=i%4; rotated=options[shift:]+options[:shift]
  data["prompt"]=prompt; data["options"]=[{"id":chr(65+j),"text":v} for j,v in enumerate(rotated)]; data["answer"]={"value":chr(65+((4-shift)%4)),"explanation":explanation}; data["knowledgeIds"]=[KNOWLEDGE]; data["lessonId"]=LESSON; data["difficulty"]="medium"
  data["provenance"]={"origin":"original","license":"All rights reserved","sourceUrl":SOURCE,"sourceLocator":f"114 年國中教育會考英語科閱讀公開試題；研究敘事者觀點、態度、語氣、寫作目的、證據限制與推論能力方向；課綱：{CURRICULUM}","authoringNote":"自編短文與選項，未重製任何原題文章、圖表或答案；待第二輪 AI 內容複核。"}; data["reviewStatus"]="draft"; data["updatedAt"]="2026-08-28"; path.write_text(json.dumps(data,ensure_ascii=False,indent=2)+"\n")
 print("replaced 10 narrator-attitude-purpose questions")
if __name__=="__main__": main()
