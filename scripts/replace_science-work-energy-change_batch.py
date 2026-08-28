"""獨立替換 Ba-Ⅳ-5 力作功與能量改變題。"""
from __future__ import annotations
import json
from pathlib import Path

ROOT=Path(__file__).resolve().parents[1]
SOURCE="https://www.grow22.com/download/114/114_cp/05_114P_Nature.pdf"
CURRICULUM=json.loads((ROOT/"curriculum/science/content-ba-iv-5.json").read_text())["source"]["url"]
LESSON="lesson-science-content-ba-iv-5"; KNOWLEDGE="kg-science-content-ba-iv-5"
ITEMS=[
("水平力 15 N 推動物體沿力方向 4 m，力所作的功為何？",["60 J","19 J","11 J","3.75 J"],"A","功＝力×沿力方向位移＝15×4＝60 J。"),
("手提書包水平行走時，手的支持力方向向上、書包位移方向水平，支持力對書包所作的功為何？",["0 J","正值","負值且等於重量×路程","無限大"],"A","力與位移互相垂直，力在位移方向的分量為零，因此作功為 0。"),
("物體受到與位移方向相反的摩擦力時，摩擦力通常對物體作何種功？",["負功","正功","一定為零","功率必為零"],"A","摩擦力與位移方向相反，會使物體機械能減少，通常作負功。"),
("質量 2 kg 的物體在地面上升高 5 m，若取 g=10 m/s²，重力位能增加多少？",["100 J","10 J","25 J","50 J"],"A","重力位能增加量＝mgh＝2×10×5＝100 J。"),
("物體由高處落下且忽略空氣阻力時，重力對物體作正功會使其？",["動能增加","動能減少","質量減少","速度必為零"],"A","重力方向與下落位移同向，作正功使物體動能增加。"),
("若 200 J 的功在 10 s 內完成，平均功率為何？",["20 W","2000 W","210 W","0.05 W"],"A","平均功率＝功÷時間＝200÷10＝20 W。"),
("同樣大小的力作用下，位移增加為原來 3 倍且方向不變，所作的功如何變化？",["變為原來 3 倍","不變","變為原來 1/3","變為原來 9 倍"],"A","功與力在同方向的位移成正比，位移 3 倍時功也 3 倍。"),
("物體在粗糙水平面上被拉動且速度保持不變，拉力所作的功與摩擦力所作的功關係為何？",["大小相等、正負相反","兩者都為正且相等","拉力功一定為零","摩擦力功一定為正"],"A","速度不變表示動能不變，合功為零，因此兩力作功大小相等、符號相反。"),
("將物體垂直向上提升時，若不計阻力，外力作功主要增加物體的何種能量？",["重力位能","化學能","聲能","核能"],"A","提升高度使物體的重力位能增加，外力作功轉為位能。"),
("兩人搬同樣重的物體到同樣高度，甲用時較短，甲的平均功率為何？",["較大","較小","一定相同且與時間無關","一定為零"],"A","兩人作功相同，甲用時較短，功率＝功÷時間因此較大。"),
]
def main():
 for i,(prompt,options,_answer,explanation) in enumerate(ITEMS,1):
  path=ROOT/"questions/science"/f"question-science-content-ba-iv-5-{i}.json"; data=json.loads(path.read_text()); shift=i%4; rotated=options[shift:]+options[:shift]
  data["prompt"]=prompt; data["options"]=[{"id":chr(65+j),"text":v} for j,v in enumerate(rotated)]; data["answer"]={"value":chr(65+((4-shift)%4)),"explanation":explanation}; data["knowledgeIds"]=[KNOWLEDGE]; data["lessonId"]=LESSON; data["difficulty"]="medium"
  data["provenance"]={"origin":"original","license":"All rights reserved","sourceUrl":SOURCE,"sourceLocator":f"114 年國中教育會考自然科公開試題；研究功、力與位移、摩擦力、重力位能、動能及功率能力方向；課綱：{CURRICULUM}","authoringNote":"獨立改編，未重製原題文字、選項、圖表或答案；待第二輪 AI 內容複核。"}; data["reviewStatus"]="draft"; data["updatedAt"]="2026-08-28"; path.write_text(json.dumps(data,ensure_ascii=False,indent=2)+"\n")
 print("replaced 10 work-energy-change questions")
if __name__=="__main__": main()
