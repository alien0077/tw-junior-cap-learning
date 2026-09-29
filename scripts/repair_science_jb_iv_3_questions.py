import json
from pathlib import Path
ROOT=Path(__file__).resolve().parents[1]; OUT=ROOT/'questions/science'
URL='https://www.yacjh.kh.edu.tw/upload/221/101_30637/114%E4%B8%8B%E5%AD%B8%E6%9C%9F%E7%AC%AC%E4%B8%80%E6%AC%A1%E6%AE%B5%E8%80%83%E4%B8%89%E5%B9%B4%E7%B4%9A%E8%87%AA%E7%84%B6.pdf'
DATA=[
('電解質','氯化鈉固體不導電，但溶於水後溶液能導電，主要原因？',['水中出現可移動的 Na⁺ 與 Cl⁻','固體變成金屬','水本身變成電子','氯化鈉分子變得更大'],'水中出現可移動的 Na⁺ 與 Cl⁻','溶液中帶電粒子能移動並傳遞電荷；固體離子被晶格束縛，移動性不同。'),
('解離表示','NaCl 溶於水可表示為何種粒子變化？',['NaCl → Na⁺＋Cl⁻','NaCl → Na²⁺＋Cl²⁻','NaCl → N⁺＋Cl⁻','NaCl → Na＋Cl₂'],'NaCl → Na⁺＋Cl⁻','一個 NaCl 單位解離成一個 Na⁺ 與一個 Cl⁻，電荷總和仍為零。'),
('離子電荷','MgCl₂ 溶於水後，合理的離子比例為何？',['Mg²⁺：Cl⁻＝1：2','Mg⁺：Cl²⁻＝1：2','Mg²⁺：Cl⁻＝2：1','Mg：Cl＝1：1'],'Mg²⁺：Cl⁻＝1：2','化學式下標表示一個單位含一個 Mg 與兩個 Cl，解離後電荷也必須守恆。'),
('沉澱反應','Ag⁺ 與 Cl⁻ 在溶液中反應形成難溶物，最明顯的觀察證據？',['出現沉澱使溶液混濁','溶液一定變成氣體','電流必然變成零','所有離子消失成原子'],'出現沉澱使溶液混濁','難溶物析出會形成沉澱；仍可用對照確認不是污染或原有固體。'),
('離子交換','Ba²⁺ 與 SO₄²⁻ 形成 BaSO₄ 沉澱後，哪項最合理？',['溶液中這兩種離子的自由數量降低','Ba 原子序改變','硫酸根變成電子束','水分子全部消失'],'溶液中這兩種離子的自由數量降低','沉澱把離子固定在固體中，使溶液中可自由移動的離子減少。'),
('導電比較','等濃度的糖水與食鹽水相比，食鹽水通常導電性較強，因為？',['食鹽解離產生離子，糖主要以中性分子存在','糖水含有金屬導線','食鹽水一定溫度較高','糖分子會吸收所有電荷'],'食鹽解離產生離子，糖主要以中性分子存在','導電性與可移動帶電粒子有關；分子溶液不一定能提供相同數量的離子。'),
('電荷守恆','溶液中的離子反應配平時，除了元素數量還要檢查什麼？',['反應前後總電荷相等','每個離子都變成中性原子','所有係數都必須是 1','溶液顏色一定相同'],'反應前後總電荷相等','離子方程式必須同時符合元素守恆與電荷守恆。'),
('離子觀點','兩種溶液混合沒有沉澱、氣體或弱電解質生成，最合理的離子層次描述？',['主要離子仍在溶液中共存，未觀察到明顯離子反應','所有離子必定消失','每個離子都變成另一元素','一定發生燃燒'],'主要離子仍在溶液中共存，未觀察到明顯離子反應','沒有反應驅動證據時，不能任意宣稱離子已生成新物質或完全消失。'),
('濃度與導電','同一電解質逐步加水稀釋，通常導電度如何變化？',['單位體積可移動離子變少，導電度通常下降','離子數密度增加，導電度必定上升','離子變成中性原子','導電度與濃度完全無關'],'單位體積可移動離子變少，導電度通常下降','稀釋降低單位體積的離子數；實際讀值仍要控制溫度與電極條件。'),
('證據判讀','測得溶液能導電，哪項結論最恰當？',['溶液含有可移動帶電粒子，但未必能只靠導電判定是哪種離子','已確定溶液只有 Na⁺','已確定發生沉澱反應','已確定所有溶質都是金屬'],'溶液含有可移動帶電粒子，但未必能只靠導電判定是哪種離子','導電測試能支持存在移動電荷，不能單獨辨認離子種類或反應產物。')]
TARGET_ANSWERS='ABCDBCDACB'
def make(i,row):
 tag,prompt,opts,ans,reason=row; target=TARGET_ANSWERS[i-1]; position=ord(target)-65; distractors=[v for v in opts if v != ans]; arranged=distractors[:position]+[ans]+distractors[position:]; options=[{'id':chr(65+j),'text':v} for j,v in enumerate(arranged)]; aid=target
 steps=[f'讀題定位：抓出「{tag}」的離子、解離、導電或沉澱條件。',f'建立判準：{reason}',f'核對答案：選項 {aid}「{ans}」符合判準。','排除誘答：檢查元素數量、電荷、粒子可移動性與溶液證據，不把離子任意改成原子。','最後回查：確認結論只延伸到題目提供的離子反應證據，必要時加入對照或濃度條件。']
 return {'id':f'question-science-content-jb-iv-3-{i}','subject':'science','type':'single-choice','prompt':prompt,'options':options,'knowledgeIds':['kg-science-content-jb-iv-3'],'difficulty':'medium','answer':{'value':aid,'explanation':reason},'provenance':{'origin':'original','license':'All rights reserved','sourceUrl':URL,'sourceLocator':'公立國中段考自然科；研究水溶液離子、解離、導電與離子反應的能力方向。','authoringNote':'依官方課綱 KG 與公立國中公開試題能力方向獨立改寫，未複製原文、選項、圖表或答案；待第二輪 AI／Terra 內容複核。'},'reviewStatus':'draft','updatedAt':'2026-09-08','lessonId':'lesson-science-content-jb-iv-3','examPatternRefs':[{'url':URL,'title':'公立國中段考自然科；僅研究題型與能力方向，未複製原題。','year':'114','subject':'science','locator':'水溶液離子、解離、導電與離子反應','observedPattern':'能力方向研究後原創改寫','reuseDecision':'pattern-only','status':'recorded','locatorLevel':'paper'}],'solutionStrategy':'先寫出水溶液中的粒子，再核對電荷、元素守恆與可觀察證據。','solutionSteps':steps}
for i,row in enumerate(DATA,1): (OUT/f'question-science-content-jb-iv-3-{i}.json').write_text(json.dumps(make(i,row),ensure_ascii=False,indent=2)+'\n')
print('rewrote',len(DATA),'questions')
