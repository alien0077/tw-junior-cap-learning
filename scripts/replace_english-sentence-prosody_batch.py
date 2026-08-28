"""獨立替換 Ab-Ⅳ-1 句子發音、重音與語調題。"""
from __future__ import annotations
import json
from pathlib import Path

ROOT=Path(__file__).resolve().parents[1]
SOURCE="https://www.grow22.com/download/114/114_cp/02-1_114P_English.pdf"
CURRICULUM=json.loads((ROOT/"curriculum/english/content-ab-iv-1.json").read_text())["source"]["url"]
LESSON="lesson-english-content-ab-iv-1"; KNOWLEDGE="kg-english-content-ab-iv-1"
ITEMS=[
("Which sentence normally ends with a rising intonation?",["Are you ready?","I am ready.","She lives here.","They play soccer."],"A","A yes-or-no question commonly ends with rising intonation."),
("Which sentence normally ends with a falling intonation?",["Where do you live?","Do you like tea?","Is it raining?","Can he swim?"],"A","A wh-question such as Where do you live? commonly ends with falling intonation."),
("In the sentence \"I wanted the BLUE bag,\" which word receives the main stress?",["BLUE","I","wanted","bag"],"A","The capitalized word BLUE carries the main stress and contrasts with other possible colors."),
("Which choice shows a natural pause in the sentence \"After dinner, we went home\"?",["After dinner / we went home","After / dinner we / went home","After dinner we went / home","Afterdinner / wewenthome"],"A","A short pause after the introductory phrase After dinner makes the sentence clear."),
("Which speaking style is best for a safety instruction?",["Clear words, an appropriate pace, and strong stress on important actions","Very fast speech with no pauses","A whisper that hides key words","A different meaning for every repetition"],"A","Safety instructions should be clear and emphasize important actions so listeners can follow them."),
("If a speaker says \"You finished the project?\" with rising intonation, what is the speaker most likely doing?",["Checking or confirming information","Giving a final command","Ending a story with certainty","Reading a list of names"],"A","Rising intonation can signal a question or a request for confirmation."),
("Which word should be stressed to correct the meaning: \"Mia borrowed my notebook, not Leo's.\"?",["Mia","borrowed","notebook","my"],"A","Stress on my contrasts the notebook with Leo's and clarifies ownership."),
("Why can a pause change how a listener understands a sentence?",["It separates ideas and highlights the sentence structure","It changes every noun into a verb","It makes all words silent","It removes the need for grammar"],"A","Pauses divide phrases and can make relationships between ideas easier to follow."),
("Which delivery is most suitable for reading a short news report?",["Steady pace, clear articulation, and appropriate sentence stress","Random volume changes on every word","No punctuation pauses","Speaking too softly to hear"],"A","A news report needs steady, intelligible delivery with stress that supports the information."),
("A speaker slows down before saying \"the most important rule.\" What is the likely effect?",["It draws attention to the important information","It proves the rule is false","It makes the sentence a question automatically","It removes the listener's attention"],"A","Slowing down before key information can signal emphasis and help listeners notice it."),
]
def main():
 for i,(prompt,options,_answer,explanation) in enumerate(ITEMS,1):
  path=ROOT/"questions/english"/f"question-english-content-ab-iv-1-{i}.json"; data=json.loads(path.read_text()); shift=i%4; rotated=options[shift:]+options[:shift]
  data["prompt"]=prompt; data["options"]=[{"id":chr(65+j),"text":v} for j,v in enumerate(rotated)]; data["answer"]={"value":chr(65+((4-shift)%4)),"explanation":explanation}; data["knowledgeIds"]=[KNOWLEDGE]; data["lessonId"]=LESSON; data["difficulty"]="medium"
  data["provenance"]={"origin":"original","license":"All rights reserved","sourceUrl":SOURCE,"sourceLocator":f"114 年國中教育會考英語科閱讀公開試題；研究句子重音、疑問與直述語調、停頓、語速及口語表達能力方向；課綱：{CURRICULUM}","authoringNote":"獨立改編，未重製原題文字、選項、圖表或答案；待第二輪 AI 內容複核。"}; data["reviewStatus"]="draft"; data["updatedAt"]="2026-08-28"; path.write_text(json.dumps(data,ensure_ascii=False,indent=2)+"\n")
 print("replaced 10 sentence-prosody questions")
if __name__=="__main__": main()
