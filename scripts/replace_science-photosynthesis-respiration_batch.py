"""獨立替換 Ba-Ⅳ-2 光合作用與呼吸作用題。"""
from __future__ import annotations
import json
from pathlib import Path

ROOT=Path(__file__).resolve().parents[1]
SOURCE="https://www.grow22.com/download/114/114_cp/05_114P_Nature.pdf"
CURRICULUM=json.loads((ROOT/"curriculum/science/content-ba-iv-2.json").read_text())["source"]["url"]
LESSON="lesson-science-content-ba-iv-2"; KNOWLEDGE="kg-science-content-ba-iv-2"
ITEMS=[
("綠色植物進行光合作用時，主要利用哪兩種原料？",["二氧化碳和水","氧氣和葡萄糖","氮氣和氧氣","葡萄糖和水蒸氣"],"A","光合作用以二氧化碳和水為原料，在光能作用下製造有機物並釋放氧氣。"),
("植物細胞中進行光合作用的主要構造為何？",["葉綠體","細胞壁","液胞","細胞膜"],"A","葉綠體含有葉綠素，是植物進行光合作用的主要場所。"),
("若將葉片一部分遮光數小時，再以碘液檢驗，遮光處較不易呈藍黑色，最能支持何種結論？",["光是製造澱粉的必要條件之一","氧氣會使澱粉消失","碘液只能染沒有葉綠素的部位","遮光處一定沒有水"],"A","遮光處缺少光照，澱粉形成較少，顯示光是光合作用製造澱粉的重要條件。"),
("光合作用產生的氧氣，主要來自哪一種原料？",["水","二氧化碳","葡萄糖","葉綠素"],"A","在光合作用的整體反應中，釋放的氧氣主要來自水的分解。"),
("植物在夜間沒有光照時，仍會進行哪項作用？",["呼吸作用","光合作用必定加快","只吸收二氧化碳不進行反應","完全停止所有細胞活動"],"A","呼吸作用不需光照，植物日夜都需以此釋放能量供細胞使用。"),
("光合作用與呼吸作用在氣體進出上的關係，何者較正確？",["光合作用吸收二氧化碳並釋放氧氣；呼吸作用消耗氧氣並產生二氧化碳","兩者都只吸收氧氣","兩者都只釋放二氧化碳","光合作用消耗葡萄糖、呼吸作用製造葡萄糖"],"A","兩者的氣體進出方向相反，且分別和有機物的製造、分解及能量釋放相關。"),
("要檢驗葉片是否產生澱粉，使用碘液前先把葉片放入酒精隔水加熱，主要是為了？",["去除葉綠素以便觀察顏色","增加葉片的水分","製造更多澱粉","使碘液變成藍色"],"A","酒精可溶解葉綠素，去除綠色後較容易觀察碘液與澱粉的顏色反應。"),
("密閉透明瓶中放入綠色植物並照光，若二氧化碳濃度下降，最合理的解釋為何？",["光合作用吸收二氧化碳","呼吸作用吸收二氧化碳","水蒸發變成二氧化碳","植物停止所有作用"],"A","照光下若光合作用速率大於呼吸作用，植物會淨吸收二氧化碳。"),
("細胞進行呼吸作用時，葡萄糖中的能量主要轉換成何者供細胞使用？",["可利用的化學能（ATP）","光能","聲能","重力位能"],"A","呼吸作用分解有機物，將部分能量轉存於 ATP 等可供細胞利用的形式。"),
("若植物長期處於黑暗且缺乏二氧化碳，最直接受影響的作用為何？",["光合作用速率降低","呼吸作用必然完全停止","水的沸點升高","細胞壁立刻消失"],"A","黑暗缺光且缺乏二氧化碳，光合作用缺少必要條件，速率會降低。"),
]
def main():
 for i,(prompt,options,_answer,explanation) in enumerate(ITEMS,1):
  path=ROOT/"questions/science"/f"question-science-content-ba-iv-2-{i}.json"; data=json.loads(path.read_text()); shift=i%4; rotated=options[shift:]+options[:shift]
  data["prompt"]=prompt; data["options"]=[{"id":chr(65+j),"text":v} for j,v in enumerate(rotated)]; data["answer"]={"value":chr(65+((4-shift)%4)),"explanation":explanation}; data["knowledgeIds"]=[KNOWLEDGE]; data["lessonId"]=LESSON; data["difficulty"]="medium"
  data["provenance"]={"origin":"original","license":"All rights reserved","sourceUrl":SOURCE,"sourceLocator":f"114 年國中教育會考自然科公開試題；研究光合作用原料與產物、葉綠體、實驗證據、呼吸作用及能量轉換能力方向；課綱：{CURRICULUM}","authoringNote":"獨立改編，未重製原題文字、選項、圖表或答案；待第二輪 AI 內容複核。"}; data["reviewStatus"]="draft"; data["updatedAt"]="2026-08-28"; path.write_text(json.dumps(data,ensure_ascii=False,indent=2)+"\n")
 print("replaced 10 photosynthesis-respiration questions")
if __name__=="__main__": main()
