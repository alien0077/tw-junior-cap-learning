"""獨立替換 Ae-Ⅳ-8 故事短文主旨題。"""
from __future__ import annotations
import json
from pathlib import Path

ROOT=Path(__file__).resolve().parents[1]
SOURCE="https://www.grow22.com/download/114/114_cp/02-1_114P_English.pdf"
CURRICULUM=json.loads((ROOT/"curriculum/english/content-ae-iv-8.json").read_text())["source"]["url"]
LESSON="lesson-english-content-ae-iv-8"; KNOWLEDGE="kg-english-content-ae-iv-8"
ITEMS=[
("Read: \"Lena wanted to win the cooking contest. Her first soup was too salty, so she asked for advice and tried again. The second soup was better, and she thanked her helper.\nWhat is the main idea?\"",["Learning from a mistake can lead to improvement.","Winning never requires practice.","Soup should always be salty.","Lena refused all advice."],"A","Lena improves after recognizing a mistake and accepting advice."),
("Read: \"A small bird could not reach the birdhouse. It carried twigs one at a time and built a lower nest in a tree. Soon, its chicks were safe.\nWhat is the story mainly about?\"",["Finding a creative way to solve a problem","Why birds cannot fly","How to cut down a tree","A bird that dislikes its chicks"],"A","The bird changes its plan and solves the nesting problem creatively."),
("Read: \"Noah found a watch in the school hall. He wanted to keep it, but he gave it to the teacher. Later, its owner came back, and Noah felt glad.\nWhat is the main idea?\"",["Doing the right thing brings satisfaction.","Watches are difficult to use.","Teachers should keep lost things.","Noah wanted to lose his watch."],"A","Noah returns the watch and feels glad about his honest choice."),
("Read: \"The old bicycle had a rusty chain. Mei cleaned it every weekend and learned to repair it. By summer, she could ride it to the market.\nWhat is the story mainly about?\"",["Patience and learning can restore something useful.","Markets are always far away.","Bicycles cannot be repaired.","Mei never used the bicycle."],"A","Mei patiently learns repair skills and makes the bicycle useful again."),
("Read: \"A fox saw grapes high on a wall. Instead of leaving, it found a box and used it as a step. The grapes were within reach.\nWhat is the main idea?\"",["A new approach can help overcome an obstacle.","Boxes are only for carrying fruit.","Grapes grow under the ground.","The fox was afraid of the wall."],"A","The fox changes its approach and uses a box to reach the grapes."),
("Read: \"During the hike, Tom noticed that his friend was tired. He shared his water and slowed down. They reached the lookout together.\nWhat is the story mainly about?\"",["Helping a friend makes a difficult journey possible.","Tom wanted to hike alone.","The lookout was closed.","Water made the trail longer."],"A","Tom helps his tired friend, and they complete the hike together."),
("Read: \"The class planted a tree, but strong wind bent it. The students added a support stick and checked it each day. Months later, the tree stood straight.\nWhat is the main idea?\"",["Care and continued effort help things grow.","Wind is never strong.","Students should remove every tree.","The tree grew without any help."],"A","The students keep caring for the bent tree until it grows straight."),
("Read: \"Ruby was nervous before speaking on stage. She practiced with her brother and marked places to pause. Her talk went smoothly.\nWhat is the story mainly about?\"",["Practice can build confidence.","Stages are always empty.","Ruby forgot every word.","Pauses make talks impossible."],"A","Practice helps Ruby manage her nervousness and speak smoothly."),
("Read: \"A fisherman caught more fish than he needed. He returned the smallest ones to the river and kept only enough for dinner.\nWhat is the main idea?\"",["Using only what is needed protects resources.","Rivers have no fish.","Dinner should include every fish caught.","The fisherman wanted to empty the river."],"A","The fisherman avoids waste by keeping only enough fish for dinner."),
("Read: \"Ella's paper model fell apart before the exhibition. She used stronger folds and rebuilt it with a classmate. The new model stayed together.\nWhat is the story mainly about?\"",["Cooperation and revision can improve a project.","Paper models cannot stand.","Ella canceled the exhibition.","Classmates should never help."],"A","Ella revises the model with help, and the improved project succeeds."),
]
def main():
 for i,(prompt,options,_answer,explanation) in enumerate(ITEMS,1):
  path=ROOT/"questions/english"/f"question-english-content-ae-iv-8-{i}.json"; data=json.loads(path.read_text()); shift=i%4; rotated=options[shift:]+options[:shift]
  data["prompt"]=prompt; data["options"]=[{"id":chr(65+j),"text":v} for j,v in enumerate(rotated)]; data["answer"]={"value":chr(65+((4-shift)%4)),"explanation":explanation}; data["knowledgeIds"]=[KNOWLEDGE]; data["lessonId"]=LESSON; data["difficulty"]="medium"
  data["provenance"]={"origin":"original","license":"All rights reserved","sourceUrl":SOURCE,"sourceLocator":f"114 年國中教育會考英語科閱讀公開試題；研究故事短文的事件、轉折、結局與主旨統整能力方向；課綱：{CURRICULUM}","authoringNote":"自編故事短文與選項，未重製任何現成作品、歌詞、詩文或原題文字；待第二輪 AI 內容複核。"}; data["reviewStatus"]="draft"; data["updatedAt"]="2026-08-28"; path.write_text(json.dumps(data,ensure_ascii=False,indent=2)+"\n")
 print("replaced 10 story-main-idea questions")
if __name__=="__main__": main()
