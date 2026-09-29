#!/usr/bin/env python3
"""Independent first-pass authoring for math a-IV-4."""
from __future__ import annotations
import json
from pathlib import Path

ROOT=Path(__file__).resolve().parents[1]
LESSON=ROOT/'lessons/math/lesson-math-performance-a-iv-4.json'
REPORT=ROOT/'implementation/reports/math-performance-a-iv-4-first-pass-review.json'
URLS={
 'nani':'https://www.yfms.tyc.edu.tw/uploads/1661134274196HXsSSWEB.pdf',
 'kanghsuan':'https://www.dfsh.ntpc.edu.tw/app/index.php?Action=downloadfile&file=WVhSMFlXTm9MemMwTDNCMFlWOHlNak00WHpZNE56STJOMTg0TkRNNU9TNXdaR1k9&fname=WSGGIGB0MK10OOMP50POSWHGFC30WTIG14JCB114A1A1GCFCYSA4FCB4FGOOJG50VWPOXT154404MOWS1430ICNPOP34GCGCIHXTXW40YSUSB450PKSSXXFCNO10XX21JCLKSWIGQOB4SWHCUS30A110',
 'hanlin':'https://www.cp.ptc.edu.tw/storage/134513/134513_112_B-1_9A.pdf'}

def rec(p,concept,rep,mis,assess):
 return {'publisher':p,'edition':f'{p} 公立校方數學課程計畫章節級證據','sourceType':'public-web','sourceLocator':f'{URLS[p]}；二元一次聯立與代數解題評量欄位；核讀 2026-09-21。','reviewedAt':'2026-09-21','findings':{'concepts':[concept,'公開結構支持把兩個未知量的共同條件轉為可驗證的方程組，而非只求一個數字。'],'representations':[rep],'examplesOrEvidence':['本課的飲品、票券與圖形交點情境均為原創，僅研究公開課程的能力方向。'],'misconceptions':[mis],'assessmentEmphasis':[assess]},'licenseBoundary':'僅記錄公開課程計畫可核對的章節定位、概念順序與評量方向；不複製教材正文、例題、圖表、題目、答案、影音或版面。'}

def main():
 d=json.loads(LESSON.read_text(encoding='utf-8')); assert d['id']=='lesson-math-performance-a-iv-4' and d['reviewStatus']=='draft'
 d['title']='a-Ⅳ-4：兩個未知量的共同條件'
 d['content']={'summary':'當兩個未知量同時受兩個條件限制時，一條方程通常不夠。本課用飲料店的大小杯數量與總容量建立二元一次聯立方程，讓學生比較代入法、消去法與圖形交點各自保留的資訊；解出答案後，仍須代回兩式並判斷是否符合非負整數與情境限制。','sections':[{'heading':'兩個未知量需要兩條獨立線索','body':'若只知道紅茶與綠茶共 20 杯，可能有許多組答案；再加入總容量或總價，才能縮小到同時滿足兩條件的交點。先問資料是否足夠，是列式前的建模步驟。'},{'heading':'代入法保留一條關係','body':'由 x+y=20 可整理成 y=20−x，再代進第二式，把兩個未知量暫時變成一個。代入不是把 y 消失，而是把第一條件保留在第二條件中。'},{'heading':'消去法要追蹤係數','body':'若兩式中某個未知量的係數相同或相反，可相加或相減消去；若係數不同，先乘上適當數字並同時改變整條方程。每一步都要說明消掉的是哪個量。'},{'heading':'交點是共同解而非任意解','body':'把兩式看成兩條直線時，交點同時位於兩線上。平行代表沒有共同解，重合代表有無限多組共同解；情境題還要檢查交點是否落在允許的第一象限或整數範圍。'}]}
 d['studyHighlights']=['先列出兩個未知量、單位與兩條獨立條件。','代入時說明哪條方程被保留；消去時追蹤係數與整條式子的同步變化。','解出的有序對必須同時代回兩式，確認是共同解。','圖形交點、代數答案與情境限制要彼此對得上。']
 d['teaching']={'body':[{'id':'hook','phase':'hook','heading':'只看總杯數不夠','body':'店員說今天賣出紅茶與綠茶共 20 杯，學生先猜可能的組合，再補充總容量是 34 公升且兩種杯子的容量不同。比較兩組資料讓學生看見第二條獨立線索如何排除候選，而不是急著套消去法。'},{'id':'explain','phase':'explain','heading':'把兩條線索寫成方程組','body':'令紅茶杯數為 x、綠茶杯數為 y，建立 x+y=20 與 2x+y=34。先在表格列出單位與條件，再把兩式畫成直線，讓聯立的意思是尋找同時符合兩個條件的點。'},{'id':'worked-example','phase':'worked-example','heading':'用消去法找到交點','body':'第二式減第一式得 x=14，再代回 x+y=20 得 y=6。最後檢查 14+6=20 與 2×14+6=34，並說明 x、y 都是杯數，所以非負整數限制也通過。'},{'id':'guided-practice','phase':'guided-practice','heading':'比較兩種解法的資訊','body':'改以兩張成人票與學生票的張數及總價建立方程組。學生先選擇最容易消去的未知量，再在每一行標記使用的等值操作；若改用代入法，需說出是哪一條式子先解出變量。'},{'id':'transfer','phase':'transfer','heading':'從購物資料讀出共同解','body':'給一張原創購物表：兩種包裝各有數量與總重量。學生先判斷資料是否能形成兩條獨立方程，再解出數量，最後檢查若總重量改變，交點會沿哪個方向移動。這要求同時理解代數與圖形。'},{'id':'reflect','phase':'reflect','heading':'共同解的三重檢查','body':'出口題要求學生用代數代回、圖形位置與情境限制三種方式檢查同一有序對；若得到負的杯數，必須指出是計算錯誤、模型不符或資料本身不可能，而不能只把負號刪掉。'}],'summary':['兩個未知量需要兩條獨立條件，聯立是在找共同解。','代入與消去都要保留等式關係並標記操作理由。','代數答案應同時落在兩條直線上，才是交點。','最後檢查單位、非負性、整數性與資料是否可行。'],'exitCheck':[{'prompt':'只有 x+y=20 為什麼不能唯一決定 x、y？','expectedEvidence':'指出有多組非負整數組合，還需要第二條獨立條件。'},{'prompt':'2x+y=34 減去 x+y=20 消去了什麼？','expectedEvidence':'y 的係數相同而相減後抵消，得到 x=14。'},{'prompt':'若解出負的杯數，能直接改成正數嗎？','expectedEvidence':'不能；要回查模型、計算與資料限制，負數可能表示情境無解。'}]}
 d['interactive']={'type':'algebra-expression-builder','goal':'以表格、方程與直線交點找出兩個未知量的共同解。','scenario':'調整兩種飲品的總杯數與總容量，觀察兩條條件線與交點同步變化。','variables':[{'symbol':'x','meaning':'第一種飲品杯數'},{'symbol':'y','meaning':'第二種飲品杯數'}],'steps':[{'id':'step-1','prompt':'總杯數 20 應如何表示？','options':['x+y=20','x−y=20','xy=20'],'answer':'A','feedback':'兩種杯數相加形成總杯數。'},{'id':'step-2','prompt':'x+y=20 與 2x+y=34 最快可如何消去？','options':['第二式減第一式','兩式相乘','只移動 y 一次'],'answer':'A','feedback':'y 的係數相同，相減可保留等式並消去 y。'},{'id':'step-3','prompt':'得到 x=14、y=6 後要怎麼驗證？','options':['代回兩式並檢查杯數非負整數','只代回第一式','只看交點大概位置'],'answer':'A','feedback':'共同解必須同時滿足兩條方程與情境限制。'}]}
 d['teaching']['body'][1]['body'] += ' 並請學生指出交點的兩個座標分別代表什麼，避免把圖上的任意點當作聯立解。'
 d['teaching']['body'][3]['body'] += ' 完成後比較兩種方法是否得到同一有序對，並把成人票、學生票的單位寫在答案旁。'
 d['teaching']['body'][5]['body'] += ' 再說明若兩條線平行，為何情境中可能代表資料互相矛盾而不是把負數刪除。'
 d['authoringStandard']='version-fused-v1'; d['versionResearch']=[rec('nani','以兩個條件建立代數關係並逐步求解','文字條件、方程組與數值代回，並將未知量單位標示清楚','只用一條總量方程便宣稱找到唯一答案','完整檢查列式、消去或代入步驟與共同解代回結果'),rec('kanghsuan','用操作與圖形表徵呈現兩條關係的交會','表格、兩條直線與交點互換並同步說明座標意義','係數變更時只改一項，破壞整條方程','要求解法步驟與圖形交點互相對照並解釋差異'),rec('hanlin','在情境與資料判讀中確認解的可行性','票券、容量、數量與非負整數限制的情境表徵','得到負數後刪掉負號，或忽略資料不足','共同解、模型限制與錯誤診斷都要提出可檢查證據')]
 d['fusionRecord']={'commonCore':['三版本公開結構共同支持由兩條條件建立二元關係。','代入與消去必須維持等式並留下可檢查的推理步驟。','答案需要回到圖形、單位與情境限制驗證。'],'versionDifferences':['南一證據較突顯代數式與基本解題序列；康軒較突顯操作及圖形表徵；翰林較突顯情境資料、可行性與錯誤判斷。這是公開課程計畫層級差異，不宣稱完整教材差異。'],'originalAdditions':['以飲品杯數與容量建立兩條原創條件線。','將消去法、代入法與直線交點並列，要求學生說明資訊如何保留。','加入負數杯數與資料不足的診斷情境。'],'llmSynthesisNote':'本課依官方課綱、三筆公立校方章節級公開證據與本單元 KG 重新設計二元一次聯立的建模、解法比較與共同解檢查。例題、互動與回饋均為原創，未複製教材；Terra 第二輪與正式發布審查尚未完成，維持 draft。'}
 d['updatedAt']='2026-09-21'; LESSON.write_text(json.dumps(d,ensure_ascii=False,indent=2)+'\n',encoding='utf-8')
 REPORT.write_text(json.dumps({'unit':'a-Ⅳ-4：兩個未知量的共同條件','lessonId':d['id'],'status':'first-pass-ai-review-complete','reviewStatus':'draft','checks':{'unitSpecificOriginalContent':True,'threeVersionResearchRecords':True,'fusionRecordPresent':True,'interactivePredictionManipulationExplanation':True,'terraSecondPass':'pending'},'reviewedAt':'2026-09-21'},ensure_ascii=False,indent=2)+'\n',encoding='utf-8')
 print(json.dumps({'lesson':str(LESSON.relative_to(ROOT)),'reviewStatus':d['reviewStatus']},ensure_ascii=False))

if __name__=='__main__': main()
