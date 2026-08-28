"""獨立替換 Ae 篇章閱讀題。"""
from __future__ import annotations
import json
from pathlib import Path

ROOT=Path(__file__).resolve().parents[1]
SOURCE="https://www.grow22.com/download/114/114_cp/02-1_114P_English.pdf"
CURRICULUM=json.loads((ROOT/"curriculum/english/content-ae.json").read_text())["source"]["url"]
LESSON="lesson-english-content-ae"; KNOWLEDGE="kg-english-content-ae"
ITEMS=[
("Read: \"Nora planted three herbs on her balcony. She waters them before school, and after two weeks, new leaves appear.\nWhat is the main idea?\"",["Nora cares for herbs and sees them grow.","Nora goes to school late.","The balcony has no sunlight.","Herbs never need water."],"A","The sentences focus on Nora's care and the herbs' growth."),
("Read: \"The town added a water station near the park. Runners can refill bottles there instead of buying new ones.\nWhy did the town add the station?\"",["To reduce the use of disposable bottles","To close the park","To sell more plastic bottles","To stop people from running"],"A","The station lets runners refill bottles and helps reduce disposable-bottle use."),
("Read: \"Leo forgot his lunch, so his classmate shared a sandwich with him. He thanked her and later returned the favor by lending her a book.\nWhat does \"her\" refer to?\"",["Leo's classmate","Leo's lunch","the sandwich","the book"],"A","The pronoun her refers to the female classmate who shared the sandwich."),
("Read: \"The school library will close at five on Friday. Students who need to print reports should arrive before four-thirty.\nWhat should students do?\"",["Arrive before 4:30 if they need to print reports.","Print reports after five.","Visit the library on Saturday morning.","Wait until the library closes."],"A","The notice advises students to arrive before 4:30 for printing."),
("Read: \"Mia moved the seedling from the dark shelf to a sunny window. A few days later, its stem became stronger.\nWhat can we infer?\"",["The seedling benefited from more light.","The seedling received no water.","The window made the plant smaller.","Darkness always makes stems stronger."],"A","The change after moving to sunlight suggests that more light helped the seedling."),
("Which sentence should come first in a set of instructions?",["First, wash the apple.","Next, cut it into small pieces.","Then, put the pieces in a bowl.","Finally, share the snack."],"A","First signals the beginning of the procedure."),
("Read: \"Some students walk to school. Others ride bicycles, and a few take the bus. All three choices can reduce the number of cars near the school.\nWhat does \"Others\" refer to?\"",["Other students","Other schools","Other buses","Other cars"],"A","Others refers to students different from those who walk."),
("Read: \"The science club tested two paper planes. Plane A flew farther, but Plane B stayed in the air longer. The club recorded both results instead of naming one plane the winner.\nWhy did the club record both results?\"",["Each plane performed better in a different way.","Both planes were made of metal.","The club forgot to measure distance.","Plane B never flew."],"A","The text gives two different measures, so each plane had a different strength."),
("Which title best fits this short paragraph: \"A reusable cup can be washed and used many times. Taking one to a drink shop may reduce the number of single-use cups.\"",["A Small Way to Use Less Waste","How to Build a Shop","The Fastest Drink","Why Cups Cannot Be Washed"],"A","The paragraph explains how a reusable cup may reduce waste."),
("Read: \"The rain stopped, but the field was still muddy. Therefore, the soccer game was moved to the gym.\nWhy was the game moved?\"",["The field remained muddy.","The gym was outdoors.","The rain continued all day.","The players disliked soccer."],"A","The word Therefore introduces the result of the muddy field: moving the game indoors."),
]
def main():
 for i,(prompt,options,_answer,explanation) in enumerate(ITEMS,1):
  path=ROOT/"questions/english"/f"question-english-content-ae-{i}.json"; data=json.loads(path.read_text()); shift=i%4; rotated=options[shift:]+options[:shift]
  data["prompt"]=prompt; data["options"]=[{"id":chr(65+j),"text":v} for j,v in enumerate(rotated)]; data["answer"]={"value":chr(65+((4-shift)%4)),"explanation":explanation}; data["knowledgeIds"]=[KNOWLEDGE]; data["lessonId"]=LESSON; data["difficulty"]="medium"
  data["provenance"]={"origin":"original","license":"All rights reserved","sourceUrl":SOURCE,"sourceLocator":f"114 年國中教育會考英語科閱讀公開試題；研究篇章主旨、細節、指代、因果、推論、順序與標題判讀能力方向；課綱：{CURRICULUM}","authoringNote":"自編短文與選項，未重製任何原題文章、圖表或答案；待第二輪 AI 內容複核。"}; data["reviewStatus"]="draft"; data["updatedAt"]="2026-08-28"; path.write_text(json.dumps(data,ensure_ascii=False,indent=2)+"\n")
 print("replaced 10 text-discourse questions")
if __name__=="__main__": main()
