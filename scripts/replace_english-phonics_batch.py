"""獨立替換 Ab 語音題。"""
from __future__ import annotations
import json
from pathlib import Path

ROOT=Path(__file__).resolve().parents[1]
SOURCE="https://www.grow22.com/download/114/114_cp/02-1_114P_English.pdf"
CURRICULUM=json.loads((ROOT/"curriculum/english/content-ab.json").read_text())["source"]["url"]
LESSON="lesson-english-content-ab"; KNOWLEDGE="kg-english-content-ab"
ITEMS=[
("Which word begins with the same sound as \"sun\"?",["sock","chair","fish","moon"],"A","Sun and sock both begin with the /s/ sound."),
("Which word ends with the same sound as \"map\"?",["cup","man","make","bag"],"A","Map and cup both end with the /p/ sound."),
("Which word has the same short vowel sound as \"cat\"?",["bag","cake","bike","bed"],"A","Cat and bag both have the short /æ/ vowel sound."),
("Which word has the long vowel sound in \"cake\"?",["name","cap","pet","sit"],"A","Cake and name have the long A sound /eɪ/."),
("Which pair rhymes?",["light and night","book and back","pen and pan","dog and dig"],"A","Light and night share the same final sound pattern and rhyme."),
("Which word begins with the /ʃ/ sound, like the first sound in \"ship\"?",["shoe","sip","chip","zip"],"A","Shoe begins with /ʃ/, the same sound as ship; sip begins with /s/."),
("Which word has a different beginning sound from the others?",["chair","cheese","school","chicken"],"A","School begins with /sk/, while chair, cheese, and chicken begin with /tʃ/."),
("Which word has the short /ɪ/ sound, as in \"sit\"?",["fish","feet","fan","food"],"A","Fish has the short /ɪ/ sound, like sit."),
("Which word has a silent final \"e\" that changes the vowel sound?",["bike","bit","big","bin"],"A","In bike, the final e is silent and makes i a long vowel; the other words have short i."),
("Which pair begins with the same sound?",["phone and fish","goat and chair","this and thin","van and whale"],"A","Phone and fish both begin with the /f/ sound; ph and f represent that sound here."),
]
def main():
 for i,(prompt,options,_answer,explanation) in enumerate(ITEMS,1):
  path=ROOT/"questions/english"/f"question-english-content-ab-{i}.json"; data=json.loads(path.read_text()); shift=i%4; rotated=options[shift:]+options[:shift]
  data["prompt"]=prompt; data["options"]=[{"id":chr(65+j),"text":v} for j,v in enumerate(rotated)]; data["answer"]={"value":chr(65+((4-shift)%4)),"explanation":explanation}; data["knowledgeIds"]=[KNOWLEDGE]; data["lessonId"]=LESSON; data["difficulty"]="medium"
  data["provenance"]={"origin":"original","license":"All rights reserved","sourceUrl":SOURCE,"sourceLocator":f"114 年國中教育會考英語科閱讀公開試題；研究字首、字尾、母音、子音、長短母音與押韻的語音辨識能力方向；課綱：{CURRICULUM}","authoringNote":"獨立改編，未重製原題文字、選項、圖表或答案；待第二輪 AI 內容複核。"}; data["reviewStatus"]="draft"; data["updatedAt"]="2026-08-28"; path.write_text(json.dumps(data,ensure_ascii=False,indent=2)+"\n")
 print("replaced 10 phonics questions")
if __name__=="__main__": main()
