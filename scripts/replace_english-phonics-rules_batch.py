"""獨立替換 Ab-Ⅳ-3 字母拼讀規則題。"""
from __future__ import annotations
import json
from pathlib import Path

ROOT=Path(__file__).resolve().parents[1]
SOURCE="https://www.grow22.com/download/114/114_cp/02-1_114P_English.pdf"
CURRICULUM=json.loads((ROOT/"curriculum/english/content-ab-iv-3.json").read_text())["source"]["url"]
LESSON="lesson-english-content-ab-iv-3"; KNOWLEDGE="kg-english-content-ab-iv-3"
ITEMS=[
("Which word begins with the /k/ sound spelled with the letter c?",["cat","city","cent","cycle"],"A","The c in cat has the /k/ sound; before e, i, or y, c often has /s/."),
("Which word has the consonant blend /st/ at the beginning?",["stop","shop","chip","thin"],"A","Stop begins with the blend /st/, in which both consonant sounds are heard."),
("Which word contains the consonant digraph \"sh\"?",["ship","sip","chip","shopper only"],"A","The letters sh in ship represent one /ʃ/ sound."),
("Which word shows a short vowel sound?",["hop","hope","hide","cube"],"A","Hop has a short o sound; the final e in the other examples signals a long vowel pattern."),
("Which word has a silent final e?",["make","mat","map","man"],"A","The final e in make is not pronounced and helps make a long a sound."),
("Which word has the long i sound in \"time\"?",["ride","rid","red","rod"],"A","Ride has the same long i pattern i-consonant-e as time."),
("Which word begins with the /tʃ/ sound?",["chair","share","care","there"],"A","Chair begins with /tʃ/, represented by ch."),
("Which spelling completes the word \"_ake\" to make a word meaning a body of water?",["lake","like","luck","leek"],"A","Lake is spelled l-a-k-e and means a body of water."),
("Which word contains the vowel team \"ee\"?",["green","grab","grin","ground"],"A","Green contains ee, a common spelling for the long e sound."),
("Which word follows the pattern consonant-vowel-consonant (CVC)?",["sun","shoe","tree","cake"],"A","Sun has one consonant, one vowel, and one consonant: s-u-n."),
]
def main():
 for i,(prompt,options,_answer,explanation) in enumerate(ITEMS,1):
  path=ROOT/"questions/english"/f"question-english-content-ab-iv-3-{i}.json"; data=json.loads(path.read_text()); shift=i%4; rotated=options[shift:]+options[:shift]
  data["prompt"]=prompt; data["options"]=[{"id":chr(65+j),"text":v} for j,v in enumerate(rotated)]; data["answer"]={"value":chr(65+((4-shift)%4)),"explanation":explanation}; data["knowledgeIds"]=[KNOWLEDGE]; data["lessonId"]=LESSON; data["difficulty"]="medium"
  data["provenance"]={"origin":"original","license":"All rights reserved","sourceUrl":SOURCE,"sourceLocator":f"114 年國中教育會考英語科閱讀公開試題；研究常見子音、子音組合、長短母音、magic e、母音組合與 CVC 拼讀能力方向；課綱：{CURRICULUM}","authoringNote":"獨立改編，未重製原題文字、選項、圖表或答案；待第二輪 AI 內容複核。"}; data["reviewStatus"]="draft"; data["updatedAt"]="2026-08-28"; path.write_text(json.dumps(data,ensure_ascii=False,indent=2)+"\n")
 print("replaced 10 phonics-rules questions")
if __name__=="__main__": main()
