"""獨立替換 Ac-Ⅳ-4 國中基本字詞題。"""
from __future__ import annotations
import json
from pathlib import Path

ROOT=Path(__file__).resolve().parents[1]
SOURCE="https://www.grow22.com/download/114/114_cp/02-1_114P_English.pdf"
CURRICULUM=json.loads((ROOT/"curriculum/english/content-ac-iv-4.json").read_text())["source"]["url"]
LESSON="lesson-english-content-ac-iv-4"; KNOWLEDGE="kg-english-content-ac-iv-4"
ITEMS=[
("The weather is ___ today, so take an umbrella.",["rainy","hungry","quiet","expensive"],"A","Rainy describes weather with rain."),
("Please ___ the lights before you leave the room.",["turn off","look after","get up","put on"],"A","Turn off means stop a light from shining."),
("Leo was late because he ___ the bus.",["missed","made","caught up","built"],"A","Missed the bus means Leo arrived too late to ride it."),
("Which word means \"a place where sick people receive medical care\"?",["hospital","stadium","market","bridge"],"A","A hospital provides medical care."),
("The opposite of \"dangerous\" is ___.",["safe","noisy","deep","weak"],"A","Safe is the opposite of dangerous."),
("We need to ___ the problem before choosing a solution.",["understand","borrow","invite","wear"],"A","Understand means know the meaning or situation clearly."),
("Which sentence uses \"light\" to mean not heavy?",["This bag is light.","Please light the candle.","The light is bright.","Light comes from the sun."],"A","In This bag is light, light describes the bag's small weight."),
("The teacher asked us to work ___ and share one answer.",["together","yesterday","outside only","never"],"A","Together means with one another."),
("If a store gives you a lower price than usual, it offers a ___.",["discount","direction","message","season"],"A","A discount is a reduction in price."),
("Which word best completes the phrase \"take a ___\"?",["break","homework","rain","music"],"A","Take a break is a common phrase meaning rest for a short time."),
]
def main():
 for i,(prompt,options,_answer,explanation) in enumerate(ITEMS,1):
  path=ROOT/"questions/english"/f"question-english-content-ac-iv-4-{i}.json"; data=json.loads(path.read_text()); shift=i%4; rotated=options[shift:]+options[:shift]
  data["prompt"]=prompt; data["options"]=[{"id":chr(65+j),"text":v} for j,v in enumerate(rotated)]; data["answer"]={"value":chr(65+((4-shift)%4)),"explanation":explanation}; data["knowledgeIds"]=[KNOWLEDGE]; data["lessonId"]=LESSON; data["difficulty"]="medium"
  data["provenance"]={"origin":"original","license":"All rights reserved","sourceUrl":SOURCE,"sourceLocator":f"114 年國中教育會考英語科閱讀公開試題；研究國中基本字詞的句中詞義、片語搭配、詞性與生活情境判讀能力方向；課綱：{CURRICULUM}","authoringNote":"獨立改編，未重製原題文字、選項、圖表或答案；待第二輪 AI 內容複核。"}; data["reviewStatus"]="draft"; data["updatedAt"]="2026-08-28"; path.write_text(json.dumps(data,ensure_ascii=False,indent=2)+"\n")
 print("replaced 10 basic-1200 vocabulary questions")
if __name__=="__main__": main()
