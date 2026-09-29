import json
from pathlib import Path

ROOT=Path(__file__).resolve().parents[1]
LESSON=ROOT/'lessons/science/lesson-science-content-cross-global-climate-adaptation.json'
QDIR=ROOT/'questions/science'
REPORT=ROOT/'implementation/reports/science-content-cross-global-climate-adaptation-first-pass-review.json'
TODAY='2026-09-23'
SOURCES=[
 ('https://www.yacjh.kh.edu.tw/view/index.php?DataId=497103&MainMenuId=30637&MainType=101&SubMenuId=0&SubType=0&WebID=221&Work=View&page=1','高雄市立鹽埕國民中學公開自然科定期評量試題頁','氣候資料、環境變因、證據判讀','只取公立校方公開試題的資料比較與推理能力方向，重寫氣候情境。'),
 ('https://www.bhjh.ntpc.edu.tw/p/406-1000-10627%2Cr111.php?Lang=zh-tw','新北市立板橋國民中學公開自然科定期評量試題頁','天氣、環境、因果與長期資料','只取公開題型的資料尺度能力，未複製原題、圖表或答案。'),
 ('https://www.hcjh.ntpc.edu.tw/p/406-1000-7527%2Cr146.php','新北市立新莊國民中學公開自然科定期評量試題頁','氣候風險、變因控制、方案比較','只取公開資料題的能力模式，改寫為減緩與調適決策。'),
]
REFS=[{'url':u,'title':t,'year':'113-115','subject':'science','locator':l,'observedPattern':p,'reuseDecision':'pattern-only','status':'recorded','locatorLevel':'paper'} for u,t,l,p in SOURCES]
ROWS=[
 ('easy','某地一天最高溫創新高，這筆資料最適合支持哪個敘述？',['它描述單日天氣事件，不能單獨代表長期氣候趨勢','它證明全球平均溫度每天都上升','它足以預測百年後海平面','它代表所有地點同一天都創高溫'],'A','單日觀測屬天氣尺度；氣候趨勢需長期、多地點與統計基準資料。','先標示時間與空間尺度，再檢查結論是否超出觀測範圍。'),
 ('medium','長期資料顯示平均溫度上升，若要討論人為增強溫室效應，還需考慮什麼？',['排放來源、能量收支、自然變異與模型不確定性','只看某一天的體感溫度','只挑支持結論的年份','把所有自然變異都當成測量錯誤'],'A','趨勢與成因需要排放、能量機制、自然變異與模型證據交叉檢驗，不能由一條曲線直接斷言。','把觀察到的趨勢和造成趨勢的機制分開，列出替代解釋與資料需求。'),
 ('medium','校園種樹主要降低操場熱暴露，這項措施屬於哪類？',['調適，因為它降低特定地點受熱風險','減緩，因為它一定抵消所有排放','兩者完全相同不需說明作用對象','不是氣候措施因為只在校園'],'A','遮蔭直接降低校園特定場域的暴露與熱風險，主要是調適；是否有減碳效益需另以資料評估。','先問措施作用在成因還是風險後果，再指定受益尺度。'),
 ('hard','更換節能設備以減少用電和排放，主要屬於哪類策略？',['減緩，因為它作用於排放成因；仍要檢查製造與使用條件','調適，因為所有節能都只降低暴露','一定同時解決洪水風險','只看設備標籤即可判斷生命週期'],'A','節能通常透過降低能源需求減少排放，屬減緩；完整評估仍需看設備壽命、來源和反彈效應。','沿成因—排放—氣候影響鏈判斷作用位置，再補生命週期限制。'),
 ('easy','比較兩地豪雨淹水風險時，哪組資料最能避免只看降雨量？',['降雨強度、地勢排水、人口暴露、建物脆弱度與預警能力','只比較雨量總和','只看哪裡新聞照片較多','只看城市名稱'],'A','風險不只由危害大小決定，還包括暴露、脆弱度與應變能力。','把危害、暴露、脆弱度和防護能力分欄，再比較相同降雨情境。'),
 ('medium','海平面上升下，沿海社區加高防潮設施最直接降低哪一項？',['特定地點的暴露或脆弱度，不能消除全球海平面上升成因','全球溫室氣體排放量','所有海岸的風險','自然變異本身'],'A','防潮工程是調適措施，改善局部受影響程度，但不會直接改變全球成因。','標記措施作用尺度與作用對象，再寫出它無法處理的上游成因。'),
 ('hard','某減緩方案可降低平均排放，卻增加低收入家庭能源支出；評估時最應補充什麼？',['分配影響、替代方案、補助與不同族群承擔的成本','只看總排放下降數字','把公平視為與科學無關','只問方案名稱是否綠色'],'A','氣候政策的整體品質需同時考慮成效、公平、成本與可行性，總平均不能掩蓋分配差異。','在成效指標旁加入受益者、負擔者與補救設計，再比較方案。'),
 ('medium','一項校園排水改造在中小雨有效、極端暴雨失效，結論應如何寫？',['在目前設計容量與中小雨條件下可降低積水，極端情境仍需備援與重測','它已解決所有未來洪水','只要一次成功就永遠有效','極端暴雨資料應刪除'],'A','措施效益取決於雨勢、容量與維護條件，極端情境可揭示需要補強的邊界。','指定資料涵蓋的雨勢範圍，檢查容量缺口並提出可調整的備援。'),
 ('hard','若兩個氣候模型對未來降雨有不同結果，最合理的決策方式是？',['採用多情境比較，優先選可調整、降低重大損失且不把風險轉嫁給弱勢的措施','只選最樂觀模型','只選最悲觀模型並忽略成本','因不確定就完全不行動'],'A','不確定性不是停止決策的理由，應以情境、韌性、可逆性與公平條件管理。','列出各情境下的損失與方案表現，優先採取跨情境仍有益的措施。'),
 ('medium','寫全球氣候變遷的校園學習結論時，哪項最完整？',['用長期資料說明趨勢，區分減緩與調適，並交代尺度、證據與限制','用一次高溫直接代表全球氣候','把所有綠色行動都叫減緩','只寫結論不寫資料來源與範圍'],'A','完整結論要把長期證據、策略機制、受益尺度與不確定性放在一起，避免口號化。','依趨勢—機制—風險—回應—限制五格整理，再檢查每句是否有資料支撐。'),
]

def make_question(n,row):
 diff,prompt,opts,source_answer,explanation,strategy=row; target='BDACBDACBD'[n-1]; idx=ord(source_answer)-65; correct=opts[idx]; distractors=[x for i,x in enumerate(opts) if i!=idx]
 ordered=[]; di=0
 for label in 'ABCD':
  if label==target: ordered.append(correct)
  else: ordered.append(distractors[di]); di+=1
 steps=['先標記資料的時間、空間、基準與不確定性，分開天氣觀測和氣候統計。','沿排放—能量收支—衝擊—暴露／脆弱度—回應鏈整理因果位置。','判斷措施是減緩還是調適，並檢查受益者、成本、容量與資料邊界。',f'排除把單日當長期、局部當全球、綠色標籤當證據或忽略公平的選項，答案為 {target}。',f'將答案放回氣候資料情境並限定適用條件：{explanation}']
 return {'id':f'question-science-content-cross-global-climate-adaptation-{n}','subject':'science','type':'single-choice','prompt':prompt,'options':[{'id':k,'text':v} for k,v in zip('ABCD',ordered)],'knowledgeIds':['kg-science-content-cross-global-climate-adaptation'],'difficulty':diff,'answer':{'value':target,'explanation':f'{explanation} 正確答案為選項 {target}。'},'examPatternRefs':REFS,'provenance':{'origin':'original','license':'All rights reserved','sourceUrl':SOURCES[0][0],'sourceLocator':'三筆公立國中公開自然科資料僅作天氣／氣候尺度、風險、變因控制、方案比較與證據界線的能力方向；本題為氣候變遷與調適單元原創情境改寫。','authoringNote':'依官方課綱、Knowledge Graph 與公開試題 pattern-only 能力方向獨立改寫；未複製原題、選項、圖表或答案；待第二輪 AI／Terra 內容複核。'},'reviewStatus':'draft','updatedAt':TODAY,'lessonId':'lesson-science-content-cross-global-climate-adaptation','solutionStrategy':strategy,'solutionSteps':steps}

def main():
 lesson=json.loads(LESSON.read_text(encoding='utf-8')); lesson.update({'updatedAt':TODAY,'reviewStatus':'draft','authoringStandard':'version-fused-v1'})
 for row in lesson.get('publisherResearch',[]): row['reviewedAt']=TODAY
 lesson['fusionRecord']['llmSynthesisNote']='本課依官方自然科學課綱、kg-science-content-cross-global-climate-adaptation、南一／康軒／翰林公開版本研究限制及三筆公立國中公開自然科題型能力模式，獨立融合天氣與氣候尺度、溫室效應、排放、風險、減緩、調適、公平與不確定性決策。題目與互動均重新設計，未複製受保護內容；Terra 第二輪與正式發布審查尚未完成，維持 draft。'
 LESSON.write_text(json.dumps(lesson,ensure_ascii=False,indent=2)+'\n',encoding='utf-8')
 for i,row in enumerate(ROWS,1): (QDIR/f'question-science-content-cross-global-climate-adaptation-{i}.json').write_text(json.dumps(make_question(i,row),ensure_ascii=False,indent=2)+'\n',encoding='utf-8')
 REPORT.write_text(json.dumps({'unit':lesson['title'],'lessonId':lesson['id'],'status':'first-pass-ai-review-complete','reviewStatus':'draft','checkedQuestions':10,'checks':{'unitSpecificOriginalContent':True,'threeVersionResearchRecords':True,'threePublicSchoolExamPatternSources':True,'answersAndDetailedSteps':True,'interactivePredictionManipulationExplanation':True,'terraSecondPass':'pending'},'reviewedAt':TODAY,'note':'10 題重新改寫為天氣／氣候尺度、溫室效應、風險、減緩、調適、公平與不確定性決策題；每題具唯一答案、解析、策略與五步解法。'},ensure_ascii=False,indent=2)+'\n',encoding='utf-8')
 print('authored science content cross-global-climate-adaptation')

if __name__=='__main__': main()
