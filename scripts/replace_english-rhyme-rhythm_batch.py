"""獨立替換 Ab-Ⅳ-2 歌謠韻文節奏音韻題。"""
from __future__ import annotations
import json
from pathlib import Path

ROOT=Path(__file__).resolve().parents[1]
SOURCE="https://www.grow22.com/download/114/114_cp/02-1_114P_English.pdf"
CURRICULUM=json.loads((ROOT/"curriculum/english/content-ab-iv-2.json").read_text())["source"]["url"]
LESSON="lesson-english-content-ab-iv-2"; KNOWLEDGE="kg-english-content-ab-iv-2"
ITEMS=[
("Which pair of words rhymes?",["day and play","day and dog","play and tree","sun and soon"],"A","Day and play share the same final sound /eɪ/ and rhyme."),
("Which pair does NOT rhyme?",["light and night","cake and lake","book and look","rain and run"],"A","Rain and run have different vowel and final sound patterns, so they do not rhyme."),
("How many syllables are in the word \"happy\"?",["2","1","3","4"],"A","Happy is pronounced hap-py, with two syllables."),
("Which word has the main stress on the second syllable?",["begin","happy","window","table"],"A","Begin is commonly stressed on the second syllable: be-GIN."),
("Which short line has a repeated rhythm pattern?",["Run and jump; run and jump.","Run quickly to the station.","The blue bird is in the tree.","Please open the window now."],"A","The repeated words create a regular, easily heard rhythm."),
("In a chant, why are stressed words often spoken more strongly?",["They help listeners hear the beat and key meaning","They make every word silent","They remove all pauses","They change nouns into verbs"],"A","Strong stress marks the beat and draws attention to important words."),
("Which word has the same ending sound as \"sing\"?",["ring","song","sit","sink"],"A","Sing and ring both end with the /ɪŋ/ sound."),
("Which line is most suitable for a steady four-beat chant?",["Clap, clap, step, stop.","The interesting little animal moved slowly.","Yesterday I visited my grandmother.","Could you please explain the answer?"],"A","The four short action words can naturally receive four regular beats."),
("What can a repeated rhyme pattern help a learner remember?",["The sound sequence and the words","Only the page color","The writer's address","A completely unrelated rule"],"A","Rhyme and repetition make sound patterns memorable and support recall."),
("Which pair has the same number of syllables?",["sun (1) and bright (1)","happy (2) and wonderful (3)","teacher (2) and school (1)","elephant (3) and cat (1)"],"A","Sun and bright each contain one syllable."),
]
def main():
 for i,(prompt,options,_answer,explanation) in enumerate(ITEMS,1):
  path=ROOT/"questions/english"/f"question-english-content-ab-iv-2-{i}.json"; data=json.loads(path.read_text()); shift=i%4; rotated=options[shift:]+options[:shift]
  data["prompt"]=prompt; data["options"]=[{"id":chr(65+j),"text":v} for j,v in enumerate(rotated)]; data["answer"]={"value":chr(65+((4-shift)%4)),"explanation":explanation}; data["knowledgeIds"]=[KNOWLEDGE]; data["lessonId"]=LESSON; data["difficulty"]="medium"
  data["provenance"]={"origin":"original","license":"All rights reserved","sourceUrl":SOURCE,"sourceLocator":f"114 年國中教育會考英語科閱讀公開試題；研究歌謠韻文的押韻、節奏、音節、重音與重複語句能力方向；課綱：{CURRICULUM}","authoringNote":"使用自編短語與句子，未重製任何歌詞、詩文或原題文字；待第二輪 AI 內容複核。"}; data["reviewStatus"]="draft"; data["updatedAt"]="2026-08-28"; path.write_text(json.dumps(data,ensure_ascii=False,indent=2)+"\n")
 print("replaced 10 rhyme-rhythm questions")
if __name__=="__main__": main()
