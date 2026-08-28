"""獨立替換 Ae-Ⅳ-1 短文、短劇與故事閱讀題。"""
from __future__ import annotations
import json
from pathlib import Path

ROOT=Path(__file__).resolve().parents[1]
SOURCE="https://www.grow22.com/download/114/114_cp/02-1_114P_English.pdf"
CURRICULUM=json.loads((ROOT/"curriculum/english/content-ae-iv-1.json").read_text())["source"]["url"]
LESSON="lesson-english-content-ae-iv-1"; KNOWLEDGE="kg-english-content-ae-iv-1"
ITEMS=[
("Read: \"Ben found a small key on the playground. He asked three classmates about it, then gave it to the office when no one claimed it.\nWhat did Ben do in the end?\"",["He gave the key to the office.","He kept the key.","He threw it away.","He hid it under a tree."],"A","The final sentence says Ben gave the unclaimed key to the office."),
("Read: \"Sara wanted to join the race, but her shoelace broke. Tom lent her a spare lace, and she finished the race.\nWhy could Sara finish the race?\"",["Tom lent her a spare lace.","She left the race early.","The race was canceled.","She bought new shoes after the race."],"A","Tom's help fixed the broken shoelace, allowing Sara to continue."),
("Read: \"At first, the class was nervous about performing the play. After practicing together every afternoon, they smiled and spoke clearly on stage.\nHow did the class change?\"",["They became more confident.","They stopped practicing.","They forgot the play.","They became angry with the audience."],"A","The practice led from nervousness to clearer, happier performance."),
("Read: \"Milo the dog barked at the empty box. Lily opened it and found a note saying, \"Look under the blue chair.\" There she found Milo's missing toy.\nWhere was the toy?\"",["Under the blue chair","Inside the box","Beside the dog","On the stage"],"A","The note directed Lily to look under the blue chair, where she found the toy."),
("In a short play, a character says, \"Please take my umbrella; I have a spare one.\" What is the character doing?",["Offering help","Asking for directions","Refusing a gift","Starting a race"],"A","Offering the umbrella and mentioning a spare shows willingness to help."),
("Read: \"The little boat moved slowly at first. When the wind grew stronger, it reached the island before sunset.\nWhat caused the boat to move faster?\"",["The stronger wind","The island becoming closer","The sunset stopping","The boat becoming smaller"],"A","The text directly connects the stronger wind with the boat's faster movement."),
("Read: \"Ava wrote a poem about rain. Each line ended with a similar sound, making the poem easy to remember.\nWhat feature does the poem use?\"",["Rhyme","A map","A recipe","A question list"],"A","Lines ending with similar sounds create rhyme."),
("Which order best completes the story? 1. Kai found a seed. 2. ___ 3. A green shoot appeared.",["He planted it and watered the soil.","He ate the seed.","He lost the garden.","He closed the book."],"A","Planting and watering logically come between finding a seed and seeing it grow."),
("Read: \"The queen could not open the old gate. A child noticed a small mark on the wall and pressed it. The gate opened, and everyone entered safely.\nWhat solved the problem?\"",["The child's observation","The queen's loud voice","A storm","A new castle"],"A","The child noticed and pressed the hidden mark, which opened the gate."),
("Read: \"Although the picnic was moved indoors because of rain, the family played board games and laughed together.\nWhat is the best conclusion?\"",["The family still enjoyed the picnic time.","The family went swimming outside.","The rain never fell.","The board games were missing."],"A","Moving indoors changed the plan, but the family still had fun together."),
]
def main():
 for i,(prompt,options,_answer,explanation) in enumerate(ITEMS,1):
  path=ROOT/"questions/english"/f"question-english-content-ae-iv-1-{i}.json"; data=json.loads(path.read_text()); shift=i%4; rotated=options[shift:]+options[:shift]
  data["prompt"]=prompt; data["options"]=[{"id":chr(65+j),"text":v} for j,v in enumerate(rotated)]; data["answer"]={"value":chr(65+((4-shift)%4)),"explanation":explanation}; data["knowledgeIds"]=[KNOWLEDGE]; data["lessonId"]=LESSON; data["difficulty"]="medium"
  data["provenance"]={"origin":"original","license":"All rights reserved","sourceUrl":SOURCE,"sourceLocator":f"114 年國中教育會考英語科閱讀公開試題；研究自編短文、短劇與故事的角色、事件順序、情緒、因果、韻文特徵與結局判讀能力方向；課綱：{CURRICULUM}","authoringNote":"自編短文、對話與選項，未重製任何現成作品、歌詞、詩文或原題文字；待第二輪 AI 內容複核。"}; data["reviewStatus"]="draft"; data["updatedAt"]="2026-08-28"; path.write_text(json.dumps(data,ensure_ascii=False,indent=2)+"\n")
 print("replaced 10 short-story questions")
if __name__=="__main__": main()
