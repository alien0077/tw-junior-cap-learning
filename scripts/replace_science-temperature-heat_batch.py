"""獨立替換 Bb 溫度與熱量題。"""
from __future__ import annotations
import json
from pathlib import Path

ROOT=Path(__file__).resolve().parents[1]
SOURCE="https://www.grow22.com/download/114/114_cp/05_114P_Nature.pdf"
CURRICULUM=json.loads((ROOT/"curriculum/science/content-bb.json").read_text())["source"]["url"]
LESSON="lesson-science-content-bb"; KNOWLEDGE="kg-science-content-bb"
ITEMS=[
("攝氏 25°C 約等於華氏幾度？",["77°F","45°F","57°F","100°F"],"A","華氏溫度＝攝氏×9/5＋32＝25×9/5＋32＝77°F。"),
("兩物體接觸後，若物體甲溫度下降、物體乙溫度上升，熱量傳遞方向為何？",["由甲傳給乙","由乙傳給甲","兩者都傳給環境且無互傳","熱量由低溫傳向高溫"],"A","熱量自發由高溫物體傳向低溫物體，因此由甲傳給乙。"),
("下列哪種傳熱方式不需要物質直接接觸？",["輻射","傳導","對流","三者都必須接觸"],"A","輻射可藉電磁波傳遞能量，不需介質直接接觸。"),
("金屬湯匙放入熱湯後，握柄逐漸變熱，主要是何種傳熱？",["傳導","對流","輻射","蒸發"],"A","熱能沿著金屬由高溫端傳到低溫端，屬於傳導。"),
("煮水時鍋內水受熱上升、冷水下降形成循環，主要是何種傳熱？",["對流","傳導","輻射","凝結"],"A","液體受熱密度變小而上升、冷液下降，形成對流。"),
("相同質量的水與砂土吸收相同熱量，水的溫度上升較少，表示水的何種特性較大？",["比熱","密度一定較大","熔點一定較低","導電度"],"A","吸收相同熱量與質量時，升溫較少表示比熱較大。"),
("冰在 0°C 熔化成水的過程中，若持續加熱，溫度通常如何？",["大致維持 0°C","立即升到 100°C","持續降到負溫","一定變成 50°C"],"A","純物質相變時，輸入熱量主要用於改變狀態，熔點附近溫度大致維持不變。"),
("黑色衣物在陽光下通常比白色衣物吸收較多何種能量？",["輻射能","聲能","化學能","核能"],"A","深色表面通常較易吸收光的輻射能，因而升溫較明顯。"),
("保溫杯的主要作用是什麼？",["減少內外熱量交換","讓飲料自行產生熱量","使所有熱傳遞停止","改變飲料的質量"],"A","保溫結構降低傳導、對流與輻射造成的熱量交換，延緩溫度變化。"),
("一物體由 20°C 加熱到 35°C，溫度變化量為何？",["15°C","55°C","-15°C","35°C"],"A","溫度變化量＝35－20＝15°C。"),
]
def main():
 for i,(prompt,options,_answer,explanation) in enumerate(ITEMS,1):
  path=ROOT/"questions/science"/f"question-science-content-bb-{i}.json"; data=json.loads(path.read_text()); shift=i%4; rotated=options[shift:]+options[:shift]
  data["prompt"]=prompt; data["options"]=[{"id":chr(65+j),"text":v} for j,v in enumerate(rotated)]; data["answer"]={"value":chr(65+((4-shift)%4)),"explanation":explanation}; data["knowledgeIds"]=[KNOWLEDGE]; data["lessonId"]=LESSON; data["difficulty"]="medium"
  data["provenance"]={"origin":"original","license":"All rights reserved","sourceUrl":SOURCE,"sourceLocator":f"114 年國中教育會考自然科公開試題；研究溫標、熱傳播、熱平衡、比熱、相變與保溫能力方向；課綱：{CURRICULUM}","authoringNote":"獨立改編，未重製原題文字、選項、圖表或答案；待第二輪 AI 內容複核。"}; data["reviewStatus"]="draft"; data["updatedAt"]="2026-08-28"; path.write_text(json.dumps(data,ensure_ascii=False,indent=2)+"\n")
 print("replaced 10 temperature-heat questions")
if __name__=="__main__": main()
