"""獨立替換 Aa 字母題。"""
from __future__ import annotations
import json
from pathlib import Path

ROOT=Path(__file__).resolve().parents[1]
SOURCE="https://www.grow22.com/download/114/114_cp/02-1_114P_English.pdf"
CURRICULUM=json.loads((ROOT/"curriculum/english/content-aa.json").read_text())["source"]["url"]
LESSON="lesson-english-content-aa"; KNOWLEDGE="kg-english-content-aa"
ITEMS=[
("Which letter comes after H in the alphabet?",["I","G","J","K"],"A","The alphabet order around H is G, H, I, so I comes after H."),
("Which lowercase letter matches the uppercase letter M?",["m","n","w","r"],"A","The lowercase form of uppercase M is m."),
("Which letter is a vowel?",["E","B","D","T"],"A","A, E, I, O, and U are the basic vowels; E is the vowel here."),
("Which list is in alphabetical order?",["cat, dog, fish","dog, cat, fish","fish, cat, dog","cat, fish, dog"],"A","Compare the first letters: c comes before d, and d comes before f."),
("Which capital letter should begin the sentence: \"___e is my friend.\"?",["H","h","e","i"],"A","The first word of a sentence begins with a capital letter, so use H in He."),
("Which word begins with the letter S?",["sun","run","fun","bun"],"A","The first letter of sun is S."),
("Which letter comes between P and R?",["Q","O","S","T"],"A","The alphabet sequence is P, Q, R, so Q is between P and R."),
("Which pair shows the same letter in uppercase and lowercase?",["T and t","T and f","B and d","P and q"],"A","T is the uppercase form and t is the lowercase form of the same letter."),
("Which word has the letter A as its first letter?",["apple","orange","eagle","ice"],"A","The first letter of apple is A."),
("Which letter is the last letter of the English alphabet?",["Z","Y","X","W"],"A","The English alphabet ends with Z."),
]
def main():
 for i,(prompt,options,_answer,explanation) in enumerate(ITEMS,1):
  path=ROOT/"questions/english"/f"question-english-content-aa-{i}.json"; data=json.loads(path.read_text()); shift=i%4; rotated=options[shift:]+options[:shift]
  data["prompt"]=prompt; data["options"]=[{"id":chr(65+j),"text":v} for j,v in enumerate(rotated)]; data["answer"]={"value":chr(65+((4-shift)%4)),"explanation":explanation}; data["knowledgeIds"]=[KNOWLEDGE]; data["lessonId"]=LESSON; data["difficulty"]="medium"
  data["provenance"]={"origin":"original","license":"All rights reserved","sourceUrl":SOURCE,"sourceLocator":f"114 年國中教育會考英語科閱讀公開試題；研究字母辨識、大小寫、字母順序與基礎閱讀能力方向；課綱：{CURRICULUM}","authoringNote":"獨立改編，未重製原題文字、選項、圖表或答案；待第二輪 AI 內容複核。"}; data["reviewStatus"]="draft"; data["updatedAt"]="2026-08-28"; path.write_text(json.dumps(data,ensure_ascii=False,indent=2)+"\n")
 print("replaced 10 English letter questions")
if __name__=="__main__": main()
