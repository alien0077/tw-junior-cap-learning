"""獨立替換 Ae-Ⅳ-5 不同體裁主題文章閱讀題。"""
from __future__ import annotations
import json
from pathlib import Path

ROOT=Path(__file__).resolve().parents[1]
SOURCE="https://www.grow22.com/download/114/114_cp/02-1_114P_English.pdf"
CURRICULUM=json.loads((ROOT/"curriculum/english/content-ae-iv-5.json").read_text())["source"]["url"]
LESSON="lesson-english-content-ae-iv-5"; KNOWLEDGE="kg-english-content-ae-iv-5"
ITEMS=[
("Read the notice: \"The art room is closed on Wednesday for cleaning. Students may use it again on Thursday.\" When may students use it again?",["On Thursday","On Tuesday","On Friday only","During cleaning"],"A","The notice says the room may be used again on Thursday."),
("Read the diary: \"I planned to ride my bike, but the tire was flat. I repaired it with Dad, so I can ride tomorrow.\" What happened first?",["The tire was flat.","The writer rode tomorrow.","Dad bought a new bike.","The writer went swimming."],"A","The flat tire was discovered before the repair and the planned ride tomorrow."),
("Read the recipe: \"Mix one egg with milk. Add flour slowly, then cook the mixture in a pan.\" What should be added after the egg and milk?",["Flour","Sugar only","A pan","Cooked rice"],"A","The recipe says to add flour slowly after mixing the egg with milk."),
("Read the short news item: \"A group of students collected 120 cans during the beach cleanup on Saturday. The cans will be recycled.\" What will happen to the cans?",["They will be recycled.","They will be buried on the beach.","They will be used as chairs.","They will be returned to the sea."],"A","The final sentence states that the cans will be recycled."),
("Read the advertisement: \"Try our new fruit drink! Buy two bottles and get one free this weekend.\" What is the offer?",["Buy two and get one free","Get two free with one bottle","Free drinks every day","A free meal with each bottle"],"A","The offer gives one free bottle when two are bought during the weekend."),
("Read the explanation: \"A thermometer measures temperature. Its liquid rises when it becomes warmer and falls when it becomes cooler.\" What does a thermometer measure?",["Temperature","Distance","Weight","Time"],"A","The first sentence directly identifies temperature as what it measures."),
("Read the personal account: \"When I moved to a new class, I knew no one. I joined the chess club and soon made two friends.\" How did the writer make friends?",["By joining the chess club","By moving to another city","By staying home","By winning a running race"],"A","The writer joined the chess club and then made two friends."),
("Read the schedule: \"9:00 Welcome; 9:30 Science show; 10:30 Lunch; 11:30 Bus home.\" What happens at 10:30?",["Lunch","The science show","Welcome time","The bus home"],"A","The schedule lists lunch at 10:30."),
("Read the advice: \"Bring a hat and water on a sunny hike. Take short rests, especially when the path goes uphill.\" What is the advice mainly about?",["Staying safe and comfortable while hiking","Buying a new bicycle","Cooking lunch indoors","Choosing a school subject"],"A","The advice gives practical ways to prepare for and manage a sunny hike."),
("Read the comparison: \"Both buses and trains carry many passengers. Trains usually travel on fixed tracks, while buses can use different roads.\" What is one difference?",["Trains travel on fixed tracks.","Buses cannot carry passengers.","Trains always use roads.","Buses never move in cities."],"A","The text contrasts trains' fixed tracks with buses' use of different roads."),
]
def main():
 for i,(prompt,options,_answer,explanation) in enumerate(ITEMS,1):
  path=ROOT/"questions/english"/f"question-english-content-ae-iv-5-{i}.json"; data=json.loads(path.read_text()); shift=i%4; rotated=options[shift:]+options[:shift]
  data["prompt"]=prompt; data["options"]=[{"id":chr(65+j),"text":v} for j,v in enumerate(rotated)]; data["answer"]={"value":chr(65+((4-shift)%4)),"explanation":explanation}; data["knowledgeIds"]=[KNOWLEDGE]; data["lessonId"]=LESSON; data["difficulty"]="medium"
  data["provenance"]={"origin":"original","license":"All rights reserved","sourceUrl":SOURCE,"sourceLocator":f"114 年國中教育會考英語科閱讀公開試題；研究公告、日記、食譜、新聞、廣告、說明文、經驗分享、行程與比較文章的理解能力方向；課綱：{CURRICULUM}","authoringNote":"自編不同體裁短文與選項，未重製任何原題文章、圖表或答案；待第二輪 AI 內容複核。"}; data["reviewStatus"]="draft"; data["updatedAt"]="2026-08-28"; path.write_text(json.dumps(data,ensure_ascii=False,indent=2)+"\n")
 print("replaced 10 genres-topics questions")
if __name__=="__main__": main()
