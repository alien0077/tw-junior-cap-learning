"""獨立替換 Ba-Ⅳ-3 化學反應吸熱與放熱題。"""
from __future__ import annotations
import json
from pathlib import Path

ROOT=Path(__file__).resolve().parents[1]
SOURCE="https://www.grow22.com/download/114/114_cp/05_114P_Nature.pdf"
CURRICULUM=json.loads((ROOT/"curriculum/science/content-ba-iv-3.json").read_text())["source"]["url"]
LESSON="lesson-science-content-ba-iv-3"; KNOWLEDGE="kg-science-content-ba-iv-3"
ITEMS=[
("化學反應進行後，溶液溫度由 25°C 升至 32°C，較合理的判斷為何？",["反應放熱","反應吸熱","沒有能量變化","溫度計一定故障"],"A","反應後溶液升溫，表示反應釋放的能量傳給周圍，屬於放熱反應。"),
("若反應使周圍溶液溫度下降，表示反應主要從周圍吸收何者？",["熱量","質量","氧原子","光的顏色"],"A","周圍降溫代表反應從周圍吸收熱量，屬於吸熱現象。"),
("木炭燃燒時，火焰附近會變熱，主要是因為燃燒反應？",["將化學能轉為熱能並釋放","吸收所有周圍熱能","使質量憑空增加","只改變物質顏色"],"A","燃燒是放熱反應，反應物的化學能部分轉換為熱能與光能。"),
("下列哪個現象最可能是吸熱反應造成？",["某些冷敷包啟用後表面變冷","酒精燃燒使容器變熱","蠟燭火焰加熱金屬","木材燃燒放出熱光"],"A","冷敷包反應吸收周圍熱量，因而使外部溫度下降。"),
("比較兩種反應的吸熱或放熱程度時，實驗中最需要固定哪項條件？",["反應物質量與溶液體積等條件","觀察者的身高","教室牆壁顏色","報告字體大小"],"A","固定反應物量、溶液體積與初溫等條件，才能公平比較溫度變化。"),
("酸與鹼混合後溫度上升，且沒有外加熱源，最合理的說法是？",["中和反應釋放熱量","中和反應吸收全部熱量","水被分解成金屬","溫度上升與反應無關"],"A","酸鹼中和常伴隨能量釋放，若溫度上升表示熱量傳給溶液。"),
("吸熱反應若持續進行，周圍環境可能出現何種變化？",["溫度降低","溫度必定升高","質量變成零","光速變慢"],"A","吸熱反應從周圍取得熱量，周圍可能因失去熱量而降溫。"),
("在量測反應溫度變化時，反應前先量初始溫度的主要用途為何？",["作為比較溫度變化的基準","讓反應自動加熱","增加反應物質量","使所有反應變成放熱"],"A","有初始溫度才能計算或比較反應前後的溫度差。"),
("若同一反應使用的反應物量增加，在其他條件相同時，放出的總熱量通常如何？",["通常增加","一定減少到零","完全不變且與用量無關","必定變成吸熱"],"A","反應物量增加通常代表反應進行的量增加，放出的總熱量也會增加。"),
("下列哪項最能說明吸熱與放熱是能量轉移的描述，而非能量消失？",["反應能量改變可由周圍溫度變化觀察","反應後所有能量都不存在","只有溫度計能創造能量","熱量不能在物體間傳遞"],"A","溫度變化顯示能量在反應系統與周圍間轉移，符合能量守恆。"),
]
def main():
 for i,(prompt,options,_answer,explanation) in enumerate(ITEMS,1):
  path=ROOT/"questions/science"/f"question-science-content-ba-iv-3-{i}.json"; data=json.loads(path.read_text()); shift=i%4; rotated=options[shift:]+options[:shift]
  data["prompt"]=prompt; data["options"]=[{"id":chr(65+j),"text":v} for j,v in enumerate(rotated)]; data["answer"]={"value":chr(65+((4-shift)%4)),"explanation":explanation}; data["knowledgeIds"]=[KNOWLEDGE]; data["lessonId"]=LESSON; data["difficulty"]="medium"
  data["provenance"]={"origin":"original","license":"All rights reserved","sourceUrl":SOURCE,"sourceLocator":f"114 年國中教育會考自然科公開試題；研究化學反應吸熱與放熱、溫度變化、能量轉移及實驗控制變因能力方向；課綱：{CURRICULUM}","authoringNote":"獨立改編，未重製原題文字、選項、圖表或答案；待第二輪 AI 內容複核。"}; data["reviewStatus"]="draft"; data["updatedAt"]="2026-08-28"; path.write_text(json.dumps(data,ensure_ascii=False,indent=2)+"\n")
 print("replaced 10 endothermic-exothermic questions")
if __name__=="__main__": main()
