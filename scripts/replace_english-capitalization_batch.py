"""獨立替換 Aa-Ⅳ-1 大小寫辨識與書寫題。"""
from __future__ import annotations
import json
from pathlib import Path

ROOT=Path(__file__).resolve().parents[1]
SOURCE="https://www.grow22.com/download/114/114_cp/02-1_114P_English.pdf"
CURRICULUM=json.loads((ROOT/"curriculum/english/content-aa-iv-1.json").read_text())["source"]["url"]
LESSON="lesson-english-content-aa-iv-1"; KNOWLEDGE="kg-english-content-aa-iv-1"
ITEMS=[
("Which sentence is written correctly?",["My name is Amy.","my name is Amy.","My name is amy.","my Name is amy."],"A","A sentence begins with a capital letter, and Amy is a name, so both My and Amy are capitalized."),
("Which word should begin with a capital letter in this sentence: \"we live in Taipei.\"?",["We","live","in","Taipei only"],"A","The first word of a sentence begins with a capital letter, so we should be We."),
("Which is the correct lowercase form of \"G\"?",["g","q","j","y"],"A","The lowercase form of uppercase G is g."),
("Which is the correct uppercase form of \"r\"?",["R","P","B","K"],"A","The uppercase form of lowercase r is R."),
("Which sentence uses the pronoun \"I\" correctly?",["I like music.","i like music.","My friend and i play.","I like Music."],"A","The pronoun I is always capitalized; music is not a proper name here."),
("Which day is written correctly?",["Monday","monday","MONday","monDAY"],"A","Days of the week begin with a capital letter, so Monday is correct."),
("Which month is written correctly?",["August","august","AUGust","augUST"],"A","Months of the year begin with a capital letter, so August is correct."),
("Which sentence has the correct capitalization for a person's name?",["Ken helps Lisa.","ken helps lisa.","Ken helps lisa.","ken helps Lisa."],"A","Both personal names, Ken and Lisa, begin with capital letters."),
("Which pair has the same letter in uppercase and lowercase?",["D and d","D and b","F and t","N and u"],"A","D is uppercase and d is its lowercase pair."),
("Which title is written with a capital first letter?",["English class","english class","ENGLISH class","English Class only"],"A","English is the name of a language and begins with a capital letter; class is a common noun here."),
]
def main():
 for i,(prompt,options,_answer,explanation) in enumerate(ITEMS,1):
  path=ROOT/"questions/english"/f"question-english-content-aa-iv-1-{i}.json"; data=json.loads(path.read_text()); shift=i%4; rotated=options[shift:]+options[:shift]
  data["prompt"]=prompt; data["options"]=[{"id":chr(65+j),"text":v} for j,v in enumerate(rotated)]; data["answer"]={"value":chr(65+((4-shift)%4)),"explanation":explanation}; data["knowledgeIds"]=[KNOWLEDGE]; data["lessonId"]=LESSON; data["difficulty"]="medium"
  data["provenance"]={"origin":"original","license":"All rights reserved","sourceUrl":SOURCE,"sourceLocator":f"114 年國中教育會考英語科閱讀公開試題；研究句首、姓名、地名、月份、星期與代名詞 I 的大小寫辨識能力方向；課綱：{CURRICULUM}","authoringNote":"獨立改編，未重製原題文字、選項、圖表或答案；待第二輪 AI 內容複核。"}; data["reviewStatus"]="draft"; data["updatedAt"]="2026-08-28"; path.write_text(json.dumps(data,ensure_ascii=False,indent=2)+"\n")
 print("replaced 10 capitalization questions")
if __name__=="__main__": main()
