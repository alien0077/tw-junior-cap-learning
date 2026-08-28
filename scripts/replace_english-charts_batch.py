"""獨立替換 Ae-Ⅳ-2 圖表閱讀題。"""
from __future__ import annotations
import json
from pathlib import Path

ROOT=Path(__file__).resolve().parents[1]
SOURCE="https://www.grow22.com/download/114/114_cp/02-1_114P_English.pdf"
CURRICULUM=json.loads((ROOT/"curriculum/english/content-ae-iv-2.json").read_text())["source"]["url"]
LESSON="lesson-english-content-ae-iv-2"; KNOWLEDGE="kg-english-content-ae-iv-2"
ITEMS=[
("A table shows library visits: Monday 12, Tuesday 18, Wednesday 15. Which day had the most visits?",["Tuesday","Monday","Wednesday","All days had the same number"],"A","Tuesday has 18 visits, more than Monday's 12 and Wednesday's 15."),
("A chart shows four students' reading minutes: Amy 20, Ben 35, Cara 25, Dan 10. Who read 15 minutes more than Amy?",["Ben","Cara","Dan","No one"],"A","Ben read 35 minutes, and 35－20＝15."),
("A class survey has 40 students. 10 choose walking, 20 choose the bus, and 10 choose bicycles. What fraction choose the bus?",["1/2","1/4","1/3","3/4"],"A","Twenty out of forty students choose the bus, so the fraction is 20/40＝1/2."),
("A line graph records a plant's height: Week 1 4 cm, Week 2 6 cm, Week 3 9 cm. What happened from Week 2 to Week 3?",["It grew 3 cm.","It grew 2 cm.","It became 9 cm shorter.","It did not change."],"A","The height increased from 6 cm to 9 cm, a gain of 3 cm."),
("A pie chart shows snacks: fruit 25%, bread 25%, yogurt 50%. Which statement is correct?",["Yogurt is half of the choices.","Fruit is more popular than yogurt.","Bread is 75% of the choices.","All snacks are equally popular."],"A","The yogurt section is labeled 50%, which is half of the total."),
("A bar chart compares temperatures: City A 18°C, City B 23°C, City C 20°C. Which city is 5°C warmer than City A?",["City B","City C","Both B and C","No city"],"A","City B is 23－18＝5°C warmer than City A."),
("A timetable lists a bus at 7:10, 7:40, and 8:10. How often does a bus arrive?",["Every 30 minutes","Every 10 minutes","Every 40 minutes","Once a day"],"A","The difference between each listed time is 30 minutes."),
("A graph's vertical axis is labeled \"number of books\" and marked 0, 10, 20, 30. What does a bar reaching 20 represent?",["20 books","20 students","30 books","10 books"],"A","The axis unit is books, so a height of 20 means 20 books."),
("A survey result changes from 60% in April to 45% in May. What is the change?",["It decreased by 15 percentage points.","It increased by 15 percentage points.","It decreased by 45 percentage points.","It stayed the same."],"A","The difference is 60－45＝15 percentage points, so the result decreased."),
("A chart shows water use: shower 30 L, washing dishes 20 L, laundry 50 L. What is the total?",["100 L","80 L","90 L","120 L"],"A","Add the three amounts: 30＋20＋50＝100 L."),
]
def main():
 for i,(prompt,options,_answer,explanation) in enumerate(ITEMS,1):
  path=ROOT/"questions/english"/f"question-english-content-ae-iv-2-{i}.json"; data=json.loads(path.read_text()); shift=i%4; rotated=options[shift:]+options[:shift]
  data["prompt"]=prompt; data["options"]=[{"id":chr(65+j),"text":v} for j,v in enumerate(rotated)]; data["answer"]={"value":chr(65+((4-shift)%4)),"explanation":explanation}; data["knowledgeIds"]=[KNOWLEDGE]; data["lessonId"]=LESSON; data["difficulty"]="medium"
  data["provenance"]={"origin":"original","license":"All rights reserved","sourceUrl":SOURCE,"sourceLocator":f"114 年國中教育會考英語科閱讀公開試題；研究表格、長條圖、折線圖、圓餅圖、比例、趨勢與座標標示判讀能力方向；課綱：{CURRICULUM}","authoringNote":"自編資料與圖表文字，未重製任何原題圖表、文字或答案；待第二輪 AI 內容複核。"}; data["reviewStatus"]="draft"; data["updatedAt"]="2026-08-28"; path.write_text(json.dumps(data,ensure_ascii=False,indent=2)+"\n")
 print("replaced 10 chart questions")
if __name__=="__main__": main()
