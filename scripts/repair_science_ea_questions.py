import json,re
from pathlib import Path
ROOT=Path(__file__).resolve().parents[1]; D=ROOT/'questions/science'
DATA=[
("2.5 km 等於多少 m？",["2500 m","25 m","250 m","25000 m"],"A","1 km＝1000 m，所以 2.5×1000＝2500 m。","先寫換算關係，再依公里到公尺放大 1000 倍。"),
("一粒砂的直徑約 0.0003 m，科學記號可寫成？",["3×10⁻⁴ m","3×10⁴ m","0.3×10⁴ m","30×10⁻⁴ m"],"A","小數點向右移 4 位成 3，故為 3×10⁻⁴ m。","數出小數點移動位數與方向。"),
("量筒讀值為 36.0 mL，最適合表達的有效數字是？",["三位有效數字，末位到 0.1 mL","只有一位有效數字","精確到 1 L","可寫成無限精確"],"A","36.0 的末尾 0 表示量測到 0.1 mL，含三位有效數字。","從儀器最小刻度判斷可報告的末位。"),
("要量測一根細線的直徑，哪種方法較能降低單次讀值誤差？",["量多圈總長再除以圈數","只量最短的一小段","用眼睛猜測","改變單位但不量測"],"A","量多圈可把直徑造成的總長放大，再除以圈數求平均，降低相對讀值誤差。","把小量測量轉成較大的總量，再除以數量。"),
("地圖比例尺 1:50,000，圖上 2 cm 代表實際距離多少？",["1 km","100 m","10 km","25 m"],"A","2 cm×50,000＝100,000 cm＝1,000 m＝1 km。","先乘比例尺，再將公分換成公尺或公里。"),
("測量反應時間時，同一人重複五次讀值接近但都比標準值慢，較可能是哪種誤差？",["系統誤差","完全沒有誤差","隨機誤差必定為零","單位錯誤"],"A","讀值集中但整體偏離標準，可能是儀器校正或方法造成的系統誤差。","比較分散程度與整體偏移方向。"),
("若細菌長度約 2 μm，換算成 mm 為何？",["0.002 mm","0.02 mm","2 mm","2000 mm"],"A","1 mm＝1000 μm，所以 2 μm＝2÷1000＝0.002 mm。","確認微米到毫米是除以 1000。"),
("比較兩個城市面積時，一個用 km²、另一個用 m²，首先應做什麼？",["統一單位後再比較","直接比較數字大小","刪掉較大數字","只看城市名稱"],"A","不同單位的數字不能直接比較，需先換成相同面積單位。","先檢查單位，再進行數值與比例判讀。"),
("天平最小刻度為 0.1 g，合理記錄物體質量應為？",["例如 12.3 g，並依儀器規格記錄","12 g 但宣稱精確到 0.0001 g","只記大約很重","改寫成 km"],"A","記錄位數應符合儀器解析度，不能假造超出儀器能力的精確度。","由最小刻度決定報告位數。"),
("估算操場周長時，先量一段直線再數相同長度段數，這種方法主要利用？",["尺度化與分段估算","化學反應","天體公轉","隨機猜測"],"A","將難以直接量測的長度拆成可量測單位，再累加估算整體尺度。","先建立單位基準，再用段數推回總長。"),
]
for i,(prompt,opts,ans,ex,strategy) in enumerate(DATA,1):
 p=D/f'question-science-content-ea-{i}.json'; old=json.loads(p.read_text()); text=opts[ord(ans)-65]
 target_letters=['A','B','C','D','B','C','D','A','C','B'];target=target_letters[i-1];distractors=[x for x in opts if x != text];ordered=[];di=0
 for letter in ['A','B','C','D']:
  if letter == target: ordered.append(text)
  else: ordered.append(distractors[di]);di+=1
 old.update({'prompt':prompt,'options':[{'id':chr(65+j),'text':x} for j,x in enumerate(ordered)],'answer':{'value':target,'explanation':ex+f' 正確答案為選項 {target}：「{text}」。'},'solutionStrategy':strategy,'solutionSteps':['定位概念：圈出 Ea 的尺度、單位、換算、有效數字或量測誤差。','整理證據：先確認數值、單位、儀器解析度與比例尺。',f'套用原理：{ex}',f'排除干擾：檢查換算方向、有效數字與報告精度，正確選項是「{text}」。',f'最後回查：答案「{text}」符合題幹，沒有超出單位或儀器能支持的精確度。'],'reviewStatus':'draft','updatedAt':'2026-09-08'})
 p.write_text(json.dumps(old,ensure_ascii=False,indent=2)+'\n')
print(f'rewrote {len(DATA)} questions')
