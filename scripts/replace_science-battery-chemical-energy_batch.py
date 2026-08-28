"""獨立替換 Ba-Ⅳ-4 電池化學能轉電能題。"""
from __future__ import annotations
import json
from pathlib import Path

ROOT=Path(__file__).resolve().parents[1]
SOURCE="https://www.grow22.com/download/114/114_cp/05_114P_Nature.pdf"
CURRICULUM=json.loads((ROOT/"curriculum/science/content-ba-iv-4.json").read_text())["source"]["url"]
LESSON="lesson-science-content-ba-iv-4"; KNOWLEDGE="kg-science-content-ba-iv-4"
ITEMS=[
("一般電池供電給燈泡時，主要的能量轉換為何？",["化學能轉為電能，再轉為光能與熱能","光能轉為核能","聲能轉為化學能","熱能憑空變成電能"],"A","電池內部化學反應提供電能，燈泡再將部分電能轉成光能與熱能。"),
("下列哪種液體通常可作為電解質，因為含有可移動的離子？",["食鹽水","蒸餾油","乾燥砂糖固體","塑膠溶液"],"A","食鹽溶於水後解離成可移動離子，水溶液可導電並作為電解質。"),
("電池、導線與燈泡組成的電路若要使燈泡發光，最重要的條件為何？",["電路形成閉合回路","導線一定要很長","燈泡不能接觸導線","電池必須放在燈泡上方"],"A","閉合回路才能讓電荷持續移動，電能才可傳到燈泡。"),
("化學電池的兩個電極浸在電解質中，主要作用為何？",["提供化學反應與電子移動的界面","只用來增加電池重量","使電解質變成固體","阻止所有電荷移動"],"A","電極是氧化還原反應與電子進出的界面，連接外電路後可產生電流。"),
("兩個相同電池串聯，通常可得到何種效果？",["總電壓增加","總電壓一定變成零","只能使電流方向消失","電池化學能變成質量"],"A","同方向串聯時各電池的電壓相加，總電壓增加。"),
("電池使用一段時間後電壓逐漸降低，最合理的原因為何？",["反應物逐漸消耗，提供電能的化學反應能力降低","電池質量一定增加","電子全部消失在空氣中","導線自動變成絕緣體"],"A","電池內的反應物消耗後，化學反應提供電能的能力會下降。"),
("充電電池充電時，外加電源主要使哪種轉換發生？",["電能轉回化學能儲存","化學能全部轉成重力位能","光能轉成聲能","熱能轉成質量"],"A","充電時外加電能促使電池內的化學狀態恢復，將能量以化學能儲存。"),
("若只把電池兩端用導線直接相連，可能造成什麼情況？",["短路，電流過大而使電池發熱","電池完全不會有反應","電壓變成無限大","導線立刻變成電解質"],"A","直接相連形成低電阻短路，可能有大電流與發熱，應避免此危險操作。"),
("在相同電池與燈泡下，接觸不良時燈泡可能變暗，主要是因為？",["電路電阻增加，電流減小","電池化學能立刻增加","燈泡的質量變大","電壓必定增加"],"A","接觸不良使電路電阻增加，電流減小，燈泡得到的功率可能降低。"),
("電池可使電流在外電路中流動，關於電子移動的說法何者較合理？",["電子由負電極經外電路移向正電極","電子由正電極移向負電極且不需電池反應","電子只在燈泡內產生","電子在電路中被消耗殆盡"],"A","在一般電池外電路中，電子由負電極經導線移向正電極；電池反應維持電位差。"),
]
def main():
 for i,(prompt,options,_answer,explanation) in enumerate(ITEMS,1):
  path=ROOT/"questions/science"/f"question-science-content-ba-iv-4-{i}.json"; data=json.loads(path.read_text()); shift=i%4; rotated=options[shift:]+options[:shift]
  data["prompt"]=prompt; data["options"]=[{"id":chr(65+j),"text":v} for j,v in enumerate(rotated)]; data["answer"]={"value":chr(65+((4-shift)%4)),"explanation":explanation}; data["knowledgeIds"]=[KNOWLEDGE]; data["lessonId"]=LESSON; data["difficulty"]="medium"
  data["provenance"]={"origin":"original","license":"All rights reserved","sourceUrl":SOURCE,"sourceLocator":f"114 年國中教育會考自然科公開試題；研究電池化學能轉電能、電解質、電路、電極、串聯與充電能力方向；課綱：{CURRICULUM}","authoringNote":"獨立改編，未重製原題文字、選項、圖表或答案；待第二輪 AI 內容複核。"}; data["reviewStatus"]="draft"; data["updatedAt"]="2026-08-28"; path.write_text(json.dumps(data,ensure_ascii=False,indent=2)+"\n")
 print("replaced 10 battery questions")
if __name__=="__main__": main()
