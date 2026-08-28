"""獨立替換 Ac 字彙題。"""
from __future__ import annotations
import json
from pathlib import Path

ROOT=Path(__file__).resolve().parents[1]
SOURCE="https://www.grow22.com/download/114/114_cp/02-1_114P_English.pdf"
CURRICULUM=json.loads((ROOT/"curriculum/english/content-ac.json").read_text())["source"]["url"]
LESSON="lesson-english-content-ac"; KNOWLEDGE="kg-english-content-ac"
ITEMS=[
("In \"Please close the door,\" what does \"close\" mean?",["shut","open","paint","move"],"A","Close means shut in this sentence."),
("Which word is closest in meaning to \"quick\"?",["fast","heavy","quiet","late"],"A","Fast and quick both describe something that happens at a high speed."),
("Which word is opposite in meaning to \"empty\"?",["full","small","clean","early"],"A","Full is the opposite of empty."),
("Choose the best word: \"Mina felt ___ because she passed the test.\"",["proud","thirsty","broken","narrow"],"A","Passing a test can make Mina feel proud."),
("Which word is a noun in the sentence \"The children visited the museum\"?",["museum","visited","the","children's"],"A","Museum names a place, so it is a noun."),
("Which word best completes the phrase \"___ a decision\"?",["make","do","take up","put"],"A","The natural collocation is make a decision."),
("What does \"borrow\" mean in \"Can I borrow your pen?\"?",["use it and return it later","give it away forever","buy a new one","throw it away"],"A","Borrow means take and use something with the intention of returning it."),
("Which word best completes the sentence: \"The road was wet, ___ we walked carefully.\"",["so","but","or","if"],"A","So introduces the result: the road was wet, so we walked carefully."),
("Which word means a place where books can be borrowed?",["library","bakery","station","factory"],"A","A library is a place where people can borrow books."),
("In \"The glass is fragile,\" what does \"fragile\" mean?",["easily broken","very heavy","full of water","made of metal"],"A","Fragile describes something that can break easily."),
]
def main():
 for i,(prompt,options,_answer,explanation) in enumerate(ITEMS,1):
  path=ROOT/"questions/english"/f"question-english-content-ac-{i}.json"; data=json.loads(path.read_text()); shift=i%4; rotated=options[shift:]+options[:shift]
  data["prompt"]=prompt; data["options"]=[{"id":chr(65+j),"text":v} for j,v in enumerate(rotated)]; data["answer"]={"value":chr(65+((4-shift)%4)),"explanation":explanation}; data["knowledgeIds"]=[KNOWLEDGE]; data["lessonId"]=LESSON; data["difficulty"]="medium"
  data["provenance"]={"origin":"original","license":"All rights reserved","sourceUrl":SOURCE,"sourceLocator":f"114 年國中教育會考英語科閱讀公開試題；研究上下文詞義、同反義詞、詞性、搭配與生活情境字彙能力方向；課綱：{CURRICULUM}","authoringNote":"獨立改編，未重製原題文字、選項、圖表或答案；待第二輪 AI 內容複核。"}; data["reviewStatus"]="draft"; data["updatedAt"]="2026-08-28"; path.write_text(json.dumps(data,ensure_ascii=False,indent=2)+"\n")
 print("replaced 10 vocabulary questions")
if __name__=="__main__": main()
