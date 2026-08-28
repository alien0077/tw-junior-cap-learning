"""獨立替換 Ab 物質形態、性質及分類題。"""
from __future__ import annotations
import json
from pathlib import Path

ROOT=Path(__file__).resolve().parents[1]
SOURCE="https://www.grow22.com/download/114/114_cp/05_114P_Nature.pdf"
CURRICULUM=json.loads((ROOT/"curriculum/science/content-ab.json").read_text())["source"]["url"]
LESSON="lesson-science-content-ab"; KNOWLEDGE="kg-science-content-ab"
ITEMS=[
("下列何者屬於物質的物理性質？",["密度","可燃性","會與酸反應","容易氧化"],"A","密度可在不改變物質種類的情況下測量，屬於物理性質。"),
("在相同溫度下，氣體通常比液體容易被壓縮，主要原因為何？",["粒子間距較大","粒子完全沒有運動","粒子本身沒有質量","氣體一定沒有分子"],"A","氣體粒子間距較大，施壓時有較多空間可被壓縮。"),
("冰塊熔化成水的過程，物質種類有何變化？",["仍是水，只有狀態改變","變成氧氣","變成另一種化合物","質量必定消失"],"A","熔化是狀態變化，冰與水都是 H₂O，物質種類不變。"),
("下列何者是純物質？",["蒸餾水","海水","空氣","糖水"],"A","蒸餾水主要只含水，海水、空氣與糖水都含有多種成分。"),
("食鹽水外觀均勻，且各處濃度相近，較適合分類為何者？",["均勻混合物","元素","化合物","非物質"],"A","食鹽與水混合後各處組成均勻，屬於均勻混合物。"),
("要從沙子與水的混合物中分離沙子，最適合的方法為何？",["過濾","蒸餾","磁鐵吸引","結晶"],"A","沙子不溶於水且顆粒較大，可用過濾分離。"),
("要從食鹽水取得食鹽固體，較適合採用何種方法？",["蒸發結晶","過濾","磁選","沉澱後倒掉水且不乾燥"],"A","除去水分並使食鹽析出，可利用蒸發結晶。"),
("某固體質量 20 g、體積 5 cm³，其密度為何？",["4 g/cm³","0.25 g/cm³","15 g/cm³","100 g/cm³"],"A","密度＝質量÷體積＝20÷5＝4 g/cm³。"),
("同一物質在不同形態下，質量相同但體積改變，最可能是因為？",["粒子排列與間距改變","原子種類全部改變","質子數變成零","物質不再受重力作用"],"A","狀態改變時粒子排列與間距會變化，因而體積可能改變。"),
("下列哪項最能區分『化合物』與『混合物』？",["組成成分是否以固定比例結合並形成新物質","顏色是否好看","樣品大小是否相同","是否都能被看見"],"A","化合物由元素以固定比例形成新物質；混合物成分比例可變且各成分仍保有性質。"),
]
def main():
 for i,(prompt,options,_answer,explanation) in enumerate(ITEMS,1):
  path=ROOT/"questions/science"/f"question-science-content-ab-{i}.json"; data=json.loads(path.read_text()); shift=i%4; rotated=options[shift:]+options[:shift]
  data["prompt"]=prompt; data["options"]=[{"id":chr(65+j),"text":v} for j,v in enumerate(rotated)]; data["answer"]={"value":chr(65+((4-shift)%4)),"explanation":explanation}; data["knowledgeIds"]=[KNOWLEDGE]; data["lessonId"]=LESSON; data["difficulty"]="medium"
  data["provenance"]={"origin":"original","license":"All rights reserved","sourceUrl":SOURCE,"sourceLocator":f"114 年國中教育會考自然科公開試題；研究物理性質、物質三態、純物質與混合物、分離方法及密度判讀方向；課綱：{CURRICULUM}","authoringNote":"獨立改編，未重製原題文字、選項、圖表或答案；待第二輪 AI 內容複核。"}; data["reviewStatus"]="draft"; data["updatedAt"]="2026-08-28"; path.write_text(json.dumps(data,ensure_ascii=False,indent=2)+"\n")
 print("replaced 10 matter-classification questions")
if __name__=="__main__": main()
