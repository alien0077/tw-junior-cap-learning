"""獨立替換 Aa 物質組成與元素週期性題。"""
from __future__ import annotations
import json
from pathlib import Path

ROOT=Path(__file__).resolve().parents[1]
SOURCE="https://www.grow22.com/download/114/114_cp/05_114P_Nature.pdf"
CURRICULUM=json.loads((ROOT/"curriculum/science/content-aa.json").read_text())["source"]["url"]
LESSON="lesson-science-content-aa"; KNOWLEDGE="kg-science-content-aa"
ITEMS=[
("氧元素的化學符號為何？",["O","Ox","O2","Og"],"A","氧元素的標準化學符號是 O；O2 表示氧分子，不是元素符號本身。"),
("一個中性鈉原子失去 1 個電子後，形成何種粒子？",["Na⁺","Na⁻","Ne","Mg⁺"],"A","失去電子後帶 1 個正電荷，鈉原子形成 Na⁺。"),
("碳原子的原子序為 6，表示其原子核內有幾個質子？",["6","12","3","18"],"A","原子序就是原子核內的質子數，因此有 6 個質子。"),
("同一週期的元素在週期表中具有何種共同特徵？",["電子層數相同","質子數相同","都是金屬","最外層電子數必相同"],"A","週期表同一週期的元素具有相同的電子層數。"),
("下列何者通常屬於金屬元素？",["鐵 Fe","氧 O","氯 Cl","硫 S"],"A","鐵是常見金屬；氧、氯、硫通常歸為非金屬。"),
("化學式 CO₂ 表示一個二氧化碳分子含有幾個氧原子？",["2 個","1 個","3 個","4 個"],"A","CO₂ 中氧元素右下角的 2 表示含有 2 個氧原子。"),
("若某原子核有 8 個質子、8 個中子，且原子保持中性，電子數為何？",["8","16","0","4"],"A","中性原子的電子數等於質子數，所以有 8 個電子。"),
("元素週期表中，同族元素的化學性質常相近，主要與何者有關？",["最外層電子排列相近","原子質量完全相同","都位於同一週期","中子數一定相同"],"A","同族元素的最外層電子排列具有相似性，影響其化學反應特性。"),
("下列哪個式子表示 2 個氫分子？",["2H₂","H₄","2H","H₂²"],"A","化學式前的係數 2 表示有 2 個 H₂ 分子。"),
("氯原子得到 1 個電子後，電荷如何改變？",["形成 Cl⁻","形成 Cl⁺","仍是中性且少 1 個質子","變成氬原子"],"A","得到 1 個電子後電子數多於質子數，形成帶 1 負電的 Cl⁻。"),
]
def main():
 for i,(prompt,options,_answer,explanation) in enumerate(ITEMS,1):
  path=ROOT/"questions/science"/f"question-science-content-aa-{i}.json"; data=json.loads(path.read_text()); shift=i%4; rotated=options[shift:]+options[:shift]
  data["prompt"]=prompt; data["options"]=[{"id":chr(65+j),"text":v} for j,v in enumerate(rotated)]; data["answer"]={"value":chr(65+((4-shift)%4)),"explanation":explanation}; data["knowledgeIds"]=[KNOWLEDGE]; data["lessonId"]=LESSON; data["difficulty"]="medium"
  data["provenance"]={"origin":"original","license":"All rights reserved","sourceUrl":SOURCE,"sourceLocator":f"114 年國中教育會考自然科公開試題；研究元素符號、原子與離子、週期表及化學式判讀方向；課綱：{CURRICULUM}","authoringNote":"獨立改編，未重製原題文字、選項、圖表或答案；待第二輪 AI 內容複核。"}; data["reviewStatus"]="draft"; data["updatedAt"]="2026-08-28"; path.write_text(json.dumps(data,ensure_ascii=False,indent=2)+"\n")
 print("replaced 10 elements-periodic questions")
if __name__=="__main__": main()
