"""獨立替換 Ac-Ⅳ-3 常見生活用語題。"""
from __future__ import annotations
import json
from pathlib import Path

ROOT=Path(__file__).resolve().parents[1]
SOURCE="https://www.grow22.com/download/114/114_cp/02-1_114P_English.pdf"
CURRICULUM=json.loads((ROOT/"curriculum/english/content-ac-iv-3.json").read_text())["source"]["url"]
LESSON="lesson-english-content-ac-iv-3"; KNOWLEDGE="kg-english-content-ac-iv-3"
ITEMS=[
("A: Good morning! B: ___",["Good morning!","Good night!","I'm sorry.","See you yesterday."],"A","Good morning is the natural response to a morning greeting."),
("A: Could you open the window, please? B: ___",["Sure, no problem.","You are welcome.","Never mind yesterday.","I am twelve years old."],"A","Sure, no problem politely accepts the request."),
("A: I stepped on your foot. B: ___",["I'm sorry.","Thank you.","Here you are.","Congratulations!"],"A","I'm sorry is used to apologize for causing a problem."),
("A: Thanks for helping me. B: ___",["You're welcome.","Excuse me.","That's too bad.","Be careful!"],"A","You're welcome is a polite response to thanks."),
("A: Would you like to join our game? B: ___",["Yes, I'd love to.","It is on the desk.","No, I don't know his name.","At three meters."],"A","Yes, I'd love to is a suitable acceptance of an invitation."),
("A: How much is this notebook? B: ___",["It is fifty dollars.","It is next to the door.","I bought it yesterday.","Yes, I have a notebook."],"A","A price question is answered with the cost: It is fifty dollars."),
("A: Excuse me, how can I get to the library? B: ___",["Go straight and turn left.","I read there last week.","It is a large building.","The book is interesting."],"A","Directions such as Go straight and turn left answer how to get somewhere."),
("A: I'm afraid I can't come tonight. B: ___",["That's okay. Maybe next time.","Here is your ticket.","Turn right at the corner.","Happy birthday!"],"A","That's okay. Maybe next time shows understanding when an invitation is declined."),
("A: May I use your phone? B: ___",["Of course, but please be careful.","I used it last year.","It is a phone call.","No, I am at home."],"A","Of course grants permission and the reminder is a polite condition."),
("A: Have a nice weekend! B: ___",["You too!","I am sorry.","It costs ten dollars.","Open the book."],"A","You too returns the same good wish."),
]
def main():
 for i,(prompt,options,_answer,explanation) in enumerate(ITEMS,1):
  path=ROOT/"questions/english"/f"question-english-content-ac-iv-3-{i}.json"; data=json.loads(path.read_text()); shift=i%4; rotated=options[shift:]+options[:shift]
  data["prompt"]=prompt; data["options"]=[{"id":chr(65+j),"text":v} for j,v in enumerate(rotated)]; data["answer"]={"value":chr(65+((4-shift)%4)),"explanation":explanation}; data["knowledgeIds"]=[KNOWLEDGE]; data["lessonId"]=LESSON; data["difficulty"]="medium"
  data["provenance"]={"origin":"original","license":"All rights reserved","sourceUrl":SOURCE,"sourceLocator":f"114 年國中教育會考英語科閱讀公開試題；研究問候、請求、道歉、感謝、邀請、購物、問路與日常回應能力方向；課綱：{CURRICULUM}","authoringNote":"獨立改編，未重製原題文字、選項、圖表或答案；待第二輪 AI 內容複核。"}; data["reviewStatus"]="draft"; data["updatedAt"]="2026-08-28"; path.write_text(json.dumps(data,ensure_ascii=False,indent=2)+"\n")
 print("replaced 10 daily-expression questions")
if __name__=="__main__": main()
