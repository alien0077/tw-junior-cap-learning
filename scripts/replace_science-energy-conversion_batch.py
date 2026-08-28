"""獨立替換 Ba 能量形式與轉換題。"""
from __future__ import annotations
import json
from pathlib import Path

ROOT=Path(__file__).resolve().parents[1]
SOURCE="https://www.grow22.com/download/114/114_cp/05_114P_Nature.pdf"
CURRICULUM=json.loads((ROOT/"curriculum/science/content-ba.json").read_text())["source"]["url"]
LESSON="lesson-science-content-ba"; KNOWLEDGE="kg-science-content-ba"
ITEMS=[
("物體從高處落下時，重力位能主要轉換成哪種能量？",["動能","化學能","核能","聲能"],"A","物體下落速度增加，重力位能主要轉換為動能。"),
("電風扇通電運轉時，主要的能量轉換為何？",["電能轉為機械能並伴隨熱能與聲能","熱能轉為核能","光能轉為化學能","機械能轉為電能且沒有其他能量"],"A","馬達將電能轉為葉片轉動的機械能，也會產生熱與聲等能量。"),
("摩擦煞車使車速降低，車輛的動能主要轉換成何者？",["內能（熱能）","重力位能","化學能","電能"],"A","煞車摩擦使動能轉為煞車片與輪胎的內能，溫度升高。"),
("若不計摩擦，物體在自由落下過程中，重力位能與動能的總和如何？",["大致保持不變","一直增加","一直減少到零","只等於重力位能"],"A","無摩擦時機械能守恆，重力位能與動能互相轉換但總和不變。"),
("某機器輸入能量 100 J，輸出有用能量 80 J，效率為何？",["80%","20%","100%","125%"],"A","效率＝有用輸出能量÷輸入能量＝80÷100＝80%。"),
("手電筒使用電池發光，能量轉換順序較合理的是？",["化學能→電能→光能（並有熱能）","光能→化學能→電能","熱能→核能→光能","聲能→電能且沒有光能"],"A","電池的化學能先轉為電能，燈泡再將部分電能轉為光能與熱能。"),
("太陽能板把陽光用來發電，主要是將哪種能量轉換成電能？",["光能","聲能","重力位能","彈性位能"],"A","太陽能板利用光能轉換成電能。"),
("同樣加熱時間下，鍋底火力越大，水溫上升通常越快，主要因為？",["單位時間傳入水的能量較多","水的質量立刻變小","水的比熱變成零","熱能不需傳遞"],"A","火力較大代表單位時間輸入的熱能較多，因此升溫通常較快。"),
("下列哪種能源屬於再生能源？",["風力","煤炭","石油","天然氣"],"A","風力可由自然循環持續補充，屬於再生能源；化石燃料形成需長時間。"),
("能量轉換裝置不可能達到 100% 有用效率，常見原因為何？",["部分能量散失為熱能或聲能","能量可以憑空消失","輸入能量一定小於零","所有能量都不能轉換"],"A","實際裝置會因摩擦、電阻等使部分能量轉為不希望的熱或聲。"),
]
def main():
 for i,(prompt,options,_answer,explanation) in enumerate(ITEMS,1):
  path=ROOT/"questions/science"/f"question-science-content-ba-{i}.json"; data=json.loads(path.read_text()); shift=i%4; rotated=options[shift:]+options[:shift]
  data["prompt"]=prompt; data["options"]=[{"id":chr(65+j),"text":v} for j,v in enumerate(rotated)]; data["answer"]={"value":chr(65+((4-shift)%4)),"explanation":explanation}; data["knowledgeIds"]=[KNOWLEDGE]; data["lessonId"]=LESSON; data["difficulty"]="medium"
  data["provenance"]={"origin":"original","license":"All rights reserved","sourceUrl":SOURCE,"sourceLocator":f"114 年國中教育會考自然科公開試題；研究能量形式、轉換、守恆、效率、熱能與能源分類能力方向；課綱：{CURRICULUM}","authoringNote":"獨立改編，未重製原題文字、選項、圖表或答案；待第二輪 AI 內容複核。"}; data["reviewStatus"]="draft"; data["updatedAt"]="2026-08-28"; path.write_text(json.dumps(data,ensure_ascii=False,indent=2)+"\n")
 print("replaced 10 energy-conversion questions")
if __name__=="__main__": main()
