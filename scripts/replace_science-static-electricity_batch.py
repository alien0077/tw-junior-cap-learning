"""獨立替換 Kc-Ⅳ-1 靜電與電荷題，僅研究公開會考能力方向。"""
from __future__ import annotations
import json
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
SOURCE = "https://www.grow22.com/download/114/114_cp/05_114P_Nature.pdf"
CURRICULUM = json.loads((ROOT / "curriculum/science/content-kc-iv-1.json").read_text())["source"]["url"]
LESSON = "lesson-science-content-kc-iv-1"
KNOWLEDGE = "kg-science-content-kc-iv-1"
ITEMS = [
 ("毛衣脫下後，塑膠梳子能吸引小紙屑，最合理的解釋為何？", ["摩擦使電荷重新分布，梳子帶靜電", "紙屑一定帶正電", "梳子溫度升高產生磁力", "紙屑被重力吸向梳子"], "A", "摩擦可造成電荷轉移或重新分布，使帶電梳子吸引輕小紙屑。"),
 ("兩個帶正電的小球互相靠近時，通常會發生什麼現象？", ["互相排斥", "互相吸引", "完全沒有作用", "其中一球立刻變中性"], "A", "同種電荷互相排斥，異種電荷互相吸引。"),
 ("帶負電的氣球靠近不帶電的鋁罐，鋁罐可能被吸引，主要原因為何？", ["鋁罐內電荷受影響而重新分布", "鋁罐整體立刻帶負電", "氣球產生地球引力", "鋁罐變成永久磁鐵"], "A", "導體中的電荷可移動，受帶電氣球影響會重新分布，近端異號電荷造成吸引。"),
 ("下列哪一種材料通常較適合製作驗電器的金屬接觸端？", ["銅", "橡膠", "玻璃", "乾燥木棒"], "A", "銅是良導體，電荷容易在其中移動；其餘通常是絕緣材料。"),
 ("驗電器兩片金屬箔因帶同種電荷而張開，若用手碰觸金屬球，金屬箔可能合起，原因為何？", ["人體可讓電荷經由接地分散", "手使金屬箔變成磁鐵", "金屬箔溫度下降", "手把重力消除了"], "A", "人體可提供通往大地的導電路徑，使多餘電荷分散，金屬箔間斥力減小。"),
 ("摩擦起電時，較合理的描述為何？", ["電子在物體間轉移，電荷總量仍守恆", "質子可自由離開原子核", "物體憑空產生大量電荷", "摩擦只會改變物體重量"], "A", "一般摩擦起電主要是電子轉移，系統總電荷符合守恆。"),
 ("兩物體互相摩擦後，甲帶正電、乙帶負電，表示什麼？", ["電子由甲轉移到乙", "電子由乙轉移到甲", "質子由甲轉移到乙", "兩物體都失去所有電子"], "A", "甲失去電子而帶正電，乙得到電子而帶負電。"),
 ("若兩帶電小球距離增加，在其他條件相同下，靜電作用通常如何改變？", ["作用減弱", "作用增強", "一定變成零", "方向必定反轉"], "A", "帶電量相同時，距離增加會使靜電作用減弱。"),
 ("下列哪項做法最能避免驗電器殘留電荷影響下一次觀察？", ["先接地使多餘電荷分散", "只擦拭外殼", "把金屬球塗成黑色", "提高室內音量"], "A", "接地可提供電荷流動路徑，使驗電器恢復較中性的狀態。"),
 ("乾燥天氣比潮濕天氣更容易看到脫毛衣的靜電現象，主要因為潮濕時？", ["水分使電荷較容易經表面傳導散失", "空氣中的氧氣消失", "衣物一定不會摩擦", "重力變得比較小"], "A", "潮濕表面較容易導電，累積的電荷較快散失，因此現象較不明顯。"),
]
def main() -> None:
 for i,(prompt,options,_answer,explanation) in enumerate(ITEMS,1):
  path=ROOT/"questions/science"/f"question-science-content-kc-iv-1-{i}.json"
  data=json.loads(path.read_text()); shift=i%4; rotated=options[shift:]+options[:shift]
  data["prompt"]=prompt; data["options"]=[{"id":chr(65+j),"text":v} for j,v in enumerate(rotated)]
  data["answer"]={"value":chr(65+((4-shift)%4)),"explanation":explanation}; data["knowledgeIds"]=[KNOWLEDGE]; data["lessonId"]=LESSON; data["difficulty"]="medium"
  data["provenance"]={"origin":"original","license":"All rights reserved","sourceUrl":SOURCE,"sourceLocator":f"114 年國中教育會考自然科公開試題；研究摩擦起電、電荷作用、導體、接地與靜電現象的能力方向；課綱：{CURRICULUM}","authoringNote":"獨立改編，未重製原題文字、選項、圖表或答案；待第二輪 AI 內容複核。"}
  data["reviewStatus"]="draft"; data["updatedAt"]="2026-08-28"; path.write_text(json.dumps(data,ensure_ascii=False,indent=2)+"\n")
 print("replaced 10 static-electricity questions")
if __name__ == "__main__": main()
