"""獨立替換 Ba-Ⅳ-6 功率題。"""
from __future__ import annotations
import json
from pathlib import Path

ROOT=Path(__file__).resolve().parents[1]
SOURCE="https://www.grow22.com/download/114/114_cp/05_114P_Nature.pdf"
CURRICULUM=json.loads((ROOT/"curriculum/science/content-ba-iv-6.json").read_text())["source"]["url"]
LESSON="lesson-science-content-ba-iv-6"; KNOWLEDGE="kg-science-content-ba-iv-6"
ITEMS=[
("某機器在 5 s 內完成 200 J 的功，平均功率為何？",["40 W","1000 W","205 W","0.025 W"],"A","平均功率＝功÷時間＝200÷5＝40 W。"),
("甲、乙做相同的功，甲花 4 s、乙花 10 s，誰的功率較大？",["甲","乙","兩者相同","無法由時間判斷"],"A","功相同時，完成時間越短，功÷時間越大，因此甲功率較大。"),
("1 kW 等於多少 W？",["1000 W","100 W","10 W","0.001 W"],"A","k（千）表示 1000，所以 1 kW＝1000 W。"),
("一部 60 W 電燈連續使用 5 s，消耗的電能為何？",["300 J","12 J","65 J","0.083 J"],"A","電能＝功率×時間＝60×5＝300 J。"),
("兩人以相同速度爬上同一高度，體重較大者所需克服重力作功較多，因此其功率通常？",["較大","較小","一定為零","與體重無關"],"A","相同時間內，體重較大者提升所作的功較多，平均功率較大。"),
("若一裝置 2 s 輸出 150 J 有用能量，其有用功率為何？",["75 W","300 W","152 W","0.013 W"],"A","有用功率＝有用能量÷時間＝150÷2＝75 W。"),
("某電熱器標示 1200 W，表示它每秒轉換或消耗的能量約為多少？",["1200 J","1200 W·s²","12 J","0.0012 J"],"A","1 W＝1 J/s，因此 1200 W 表示每秒約 1200 J。"),
("若完成相同功的時間增加為原來 2 倍，平均功率變為原來幾倍？",["1/2 倍","2 倍","4 倍","不變"],"A","功率＝功÷時間，功相同而時間 2 倍，功率變為 1/2。"),
("一台馬達輸入功率 500 W、有用輸出功率 400 W，效率為何？",["80%","20%","125%","900%"],"A","效率＝有用輸出功率÷輸入功率＝400÷500＝80%。"),
("功率的 SI 單位 W 可用哪個單位表示？",["J/s","J·s","N/m","kg/m"],"A","功率表示單位時間做功量，1 W＝1 J/s。"),
]
def main():
 for i,(prompt,options,_answer,explanation) in enumerate(ITEMS,1):
  path=ROOT/"questions/science"/f"question-science-content-ba-iv-6-{i}.json"; data=json.loads(path.read_text()); shift=i%4; rotated=options[shift:]+options[:shift]
  data["prompt"]=prompt; data["options"]=[{"id":chr(65+j),"text":v} for j,v in enumerate(rotated)]; data["answer"]={"value":chr(65+((4-shift)%4)),"explanation":explanation}; data["knowledgeIds"]=[KNOWLEDGE]; data["lessonId"]=LESSON; data["difficulty"]="medium"
  data["provenance"]={"origin":"original","license":"All rights reserved","sourceUrl":SOURCE,"sourceLocator":f"114 年國中教育會考自然科公開試題；研究功率公式、單位換算、功率比較、電器功率與效率能力方向；課綱：{CURRICULUM}","authoringNote":"獨立改編，未重製原題文字、選項、圖表或答案；待第二輪 AI 內容複核。"}; data["reviewStatus"]="draft"; data["updatedAt"]="2026-08-28"; path.write_text(json.dumps(data,ensure_ascii=False,indent=2)+"\n")
 print("replaced 10 power questions")
if __name__=="__main__": main()
