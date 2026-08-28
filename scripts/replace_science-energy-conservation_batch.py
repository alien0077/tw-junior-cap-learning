"""獨立替換 Ba-Ⅳ-1 能量形式、轉換與守恆題。"""
from __future__ import annotations
import json
from pathlib import Path

ROOT=Path(__file__).resolve().parents[1]
SOURCE="https://www.grow22.com/download/114/114_cp/05_114P_Nature.pdf"
CURRICULUM=json.loads((ROOT/"curriculum/science/content-ba-iv-1.json").read_text())["source"]["url"]
LESSON="lesson-science-content-ba-iv-1"; KNOWLEDGE="kg-science-content-ba-iv-1"
ITEMS=[
("質量相同的兩物體位於同一高度，哪一項可判斷其重力位能相同？",["兩物體的重力位能相同","速度較快者位能較大","質量相同所以動能必相同","高度與位能無關"],"A","重力位能與質量及高度有關；質量與高度都相同時，位能相同。"),
("一物體速度變為原來的 2 倍，質量不變時動能變為原來幾倍？",["4 倍","2 倍","1/2 倍","8 倍"],"A","動能與速度平方成正比，速度變 2 倍後動能為 2^2＝4 倍。"),
("功率相同的兩部電暖器，運轉相同時間時消耗的電能如何？",["相同","功率較大者較少","一定相差一半","無法由功率與時間判斷"],"A","消耗能量＝功率×時間；功率與時間都相同，消耗電能相同。"),
("物體受到 20 N 的力，在力方向移動 3 m，所作的功為何？",["60 J","23 J","17 J","6.7 J"],"A","功＝力×沿力方向的位移＝20×3＝60 J。"),
("水力發電時，水的重力位能主要先轉換為何種能量？",["水流的動能","化學能","核能","聲能"],"A","水由高處流下，重力位能先轉為水流的動能，再帶動發電機。"),
("若一裝置輸入 500 J 能量、輸出有用能量 350 J，能量損失為何？",["150 J","350 J","500 J","850 J"],"A","損失能量＝輸入－有用輸出＝500－350＝150 J。"),
("下列哪個例子最能表示彈性位能轉為動能？",["壓縮的彈簧放手後推動小車","電池使燈泡發光","水沸騰產生蒸氣","石頭停在桌面上"],"A","壓縮彈簧儲存彈性位能，放手後轉為小車的動能。"),
("若忽略空氣阻力，物體由高處落下時，機械能如何變化？",["總機械能保持不變","總機械能持續增加","總機械能變成零","只有動能保持不變"],"A","無非保守力作功時，重力位能與動能互換，機械能守恆。"),
("同樣提升 100 N 重物 2 m，甲用 4 s、乙用 8 s，誰的功率較大？",["甲","乙","兩者相同且與時間無關","無法判斷"],"A","兩者作功同為 200 J，但甲用時較短，功率較大。"),
("能源轉換過程中，即使有用輸出減少，總能量仍符合哪項原則？",["能量守恆，部分能量可能轉成熱或聲","能量會憑空消失","輸出能量必大於輸入","只有電能遵守守恆"],"A","能量不會憑空消失，只是轉換成不同形式，部分可能成為不易利用的熱或聲。"),
]
def main():
 for i,(prompt,options,_answer,explanation) in enumerate(ITEMS,1):
  path=ROOT/"questions/science"/f"question-science-content-ba-iv-1-{i}.json"; data=json.loads(path.read_text()); shift=i%4; rotated=options[shift:]+options[:shift]
  data["prompt"]=prompt; data["options"]=[{"id":chr(65+j),"text":v} for j,v in enumerate(rotated)]; data["answer"]={"value":chr(65+((4-shift)%4)),"explanation":explanation}; data["knowledgeIds"]=[KNOWLEDGE]; data["lessonId"]=LESSON; data["difficulty"]="medium"
  data["provenance"]={"origin":"original","license":"All rights reserved","sourceUrl":SOURCE,"sourceLocator":f"114 年國中教育會考自然科公開試題；研究機械能、功、功率、能量守恆、效率與能源轉換能力方向；課綱：{CURRICULUM}","authoringNote":"獨立改編，未重製原題文字、選項、圖表或答案；待第二輪 AI 內容複核。"}; data["reviewStatus"]="draft"; data["updatedAt"]="2026-08-28"; path.write_text(json.dumps(data,ensure_ascii=False,indent=2)+"\n")
 print("replaced 10 energy-conservation questions")
if __name__=="__main__": main()
