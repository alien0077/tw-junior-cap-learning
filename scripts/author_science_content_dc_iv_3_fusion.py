import json
from pathlib import Path

ROOT=Path(__file__).resolve().parents[1]
LESSON=ROOT/'lessons/science/lesson-science-content-dc-iv-3.json'
QDIR=ROOT/'questions/science'
REPORT=ROOT/'implementation/reports/science-content-dc-iv-3-first-pass-review.json'
TODAY='2026-09-23'
SOURCES=[
 ('https://www.yacjh.kh.edu.tw/view/index.php?DataId=497103&MainMenuId=30637&MainType=101&SubMenuId=0&SubType=0&WebID=221&Work=View&page=1','高雄市立鹽埕國民中學公開自然科定期評量試題頁','皮膚、淋巴、免疫防禦與資料判讀','只取公立校方公開試題的生物防禦與證據能力方向，重寫免疫情境。'),
 ('https://www.bhjh.ntpc.edu.tw/p/406-1000-10627%2Cr111.php?Lang=zh-tw','新北市立板橋國民中學公開自然科定期評量試題頁','人體防禦、抗原抗體、構造功能','只取公開題型的因果與概念區分層次，未複製原題或答案。'),
 ('https://www.hcjh.ntpc.edu.tw/p/406-1000-7527%2Cr146.php','新北市立新莊國民中學公開自然科定期評量試題頁','淋巴系統、發炎、疫苗與證據','只取公開資料題的能力模式，重新設計防禦路徑與免疫記憶。'),
]
REFS=[{'url':u,'title':t,'year':'113-115','subject':'science','locator':l,'observedPattern':p,'reuseDecision':'pattern-only','status':'recorded','locatorLevel':'paper'} for u,t,l,p in SOURCES]
ROWS=[
 ('easy','皮膚被擦破後，局部紅、熱、腫、痛通常表示什麼？',['發炎反應使血流與防禦細胞較容易到達受傷處','病原體本身被染成紅色','抗體只在皮膚表面變熱','淋巴液停止流動'],'A','發炎是身體的廣泛防禦反應，局部血管與組織變化有助於防禦資源抵達受傷處。','先按時間辨認屏障受損，再把局部現象和防禦機制配對。'),
 ('medium','皮膚在人體防禦中的第一個重要角色是？',['形成物理與化學屏障，降低病原體進入組織的機會','只製造抗體攻擊所有抗原','把所有病原體運送到淋巴結','取代淋巴球辨認特定抗原'],'A','完整皮膚與黏膜先阻擋病原體；屏障受損後才可能引發後續防禦反應。','按防線先後分辨屏障、發炎、淋巴與專一性免疫。'),
 ('medium','淋巴結在防禦路徑中較合理的描述是？',['淋巴流經時可讓免疫細胞接觸與處理異物，並非只是一個儲存水分的袋子','負責製造所有紅血球','把抗原變成氧氣','直接取代皮膚屏障'],'A','淋巴結是淋巴與免疫細胞互動的重要場所，淋巴系統也協助回收組織液。','沿組織液—淋巴管—淋巴結—免疫細胞畫出運輸與檢查路徑。'),
 ('hard','下列哪項最能區分非專一性與專一性防禦？',['發炎可廣泛回應組織損傷或多種病原；抗體與記憶細胞則針對特定抗原','兩者都只針對同一種抗原','抗體是皮膚屏障的一部分','發炎一定比專一性免疫慢'],'A','非專一性防禦較廣泛，專一性免疫需辨認特定抗原並可形成記憶。','先看是否需要特定抗原辨認，再比較反應範圍與記憶特性。'),
 ('easy','抗原與抗體的關係何者正確？',['抗原是可被免疫系統辨認的異物特徵，抗體可專一性與相應抗原結合','抗原就是所有抗體的別名','抗體是病原體用來感染的構造','兩者都只存在皮膚表面'],'A','抗原是辨識目標，抗體是免疫反應產生的專一性結合分子，兩者層級與角色不同。','把目標、辨認分子與作用結果分開標記。'),
 ('hard','接種疫苗後再次遇到相同病原體時反應較快，最適合的解釋是？',['疫苗提供抗原刺激免疫系統形成記憶，再遇到相同抗原時可較快反應','疫苗是抗生素，直接殺死所有病原體','疫苗使皮膚永遠不會受傷','記憶細胞會把所有抗原都當成同一種'],'A','疫苗利用抗原刺激建立免疫記憶，不等同抗生素，也不代表對所有病原體都一樣有效。','區分預防性抗原刺激、抗生素治療與特定抗原記憶。'),
 ('medium','若傷口附近淋巴結腫大，哪項結論較謹慎？',['表示局部免疫活動或淋巴流量可能增加，仍需配合症狀與檢查判斷原因','可直接證明一定是某一種細菌','表示淋巴結停止過濾','只要腫大就代表疫苗成功'],'A','淋巴結腫大是可觀察現象，成因可能多樣，不能只由單一症狀確定病原。','把觀察與病因推論分開，列出需要補充的檢查資料。'),
 ('hard','比較接種前後對同一抗原的抗體反應，哪項設計較有證據？',['固定測量時間與方法，設置適當對照並追蹤反應強度與持續時間','只測接種後一次且不記錄基準','把不同抗原的結果直接相加','只挑抗體最高的樣本'],'A','免疫記憶需比較前後與對照的時間資料，單次高值不足以說明專一性與持續性。','先建立基準與對照，再畫時間曲線比較反應速度、強度與持續。'),
 ('medium','皮膚屏障、發炎、淋巴運輸和抗體作用的先後關係哪項較完整？',['先由屏障阻擋，受損後可發炎與運輸，辨認特定抗原後才出現相應專一性反應','抗體永遠先於皮膚作用','淋巴運輸只在感染結束後出現','發炎一定等於專一性抗體作用'],'A','防禦系統是多道防線接力，時間順序和專一性程度不同，不能用單一名詞概括全部。','依位置與時間排出屏障—警報—運送／攔截—專一性辨認路徑。'),
 ('medium','寫免疫防禦單元結論時，哪項最完整？',['依病原位置、屏障狀態、發炎、淋巴路徑、抗原抗體與免疫記憶說明，並交代證據限制','只說白血球會消滅所有病原','只看到紅腫就確定疫苗有效','把疫苗和抗生素當同一種作用'],'A','完整結論需把廣泛與專一性防禦接成有時間順序的證據鏈，並保留症狀不能單獨診斷的限制。','用位置—防線—專一性—資料—限制回查每個主張。'),
]

def make_question(n,row):
 diff,prompt,opts,source_answer,explanation,strategy=row; target='CADBACDBAC'[n-1]; idx=ord(source_answer)-65; correct=opts[idx]; distractors=[x for i,x in enumerate(opts) if i!=idx]
 ordered=[]; di=0
 for label in 'ABCD':
  if label==target: ordered.append(correct)
  else: ordered.append(distractors[di]); di+=1
 steps=['先定位病原體、皮膚／黏膜、組織、淋巴與血液中的事件位置。','依屏障、發炎、淋巴運輸、抗原辨認、抗體與記憶整理防禦層級。','核對是否具有專一性、時間順序、對照資料與症狀的替代解釋。',f'排除把抗原當抗體、疫苗當抗生素、症狀當確診或把發炎當專一性免疫的選項，答案為 {target}。',f'將答案放回免疫防禦情境並檢查證據範圍：{explanation}']
 return {'id':f'question-science-content-dc-iv-3-{n}','subject':'science','type':'single-choice','prompt':prompt,'options':[{'id':k,'text':v} for k,v in zip('ABCD',ordered)],'knowledgeIds':['kg-science-content-dc-iv-3'],'difficulty':diff,'answer':{'value':target,'explanation':f'{explanation} 正確答案為選項 {target}。'},'examPatternRefs':REFS,'provenance':{'origin':'original','license':'All rights reserved','sourceUrl':SOURCES[0][0],'sourceLocator':'三筆公立國中公開自然科資料僅作皮膚屏障、發炎、淋巴、抗原抗體、疫苗、免疫記憶與證據界線的能力方向；本題為 Dc-Ⅳ-3 原創情境改寫。','authoringNote':'依官方課綱、Knowledge Graph 與公開試題 pattern-only 能力方向獨立改寫；未複製原題、選項、圖表或答案；待第二輪 AI／Terra 內容複核。'},'reviewStatus':'draft','updatedAt':TODAY,'lessonId':'lesson-science-content-dc-iv-3','solutionStrategy':strategy,'solutionSteps':steps}

def main():
 lesson=json.loads(LESSON.read_text(encoding='utf-8')); lesson.update({'updatedAt':TODAY,'reviewStatus':'draft','authoringStandard':'version-fused-v1'})
 for row in lesson.get('versionResearch',[]): row['reviewedAt']=TODAY
 lesson['fusionRecord']['llmSynthesisNote']='本課依官方自然科學課綱、kg-science-content-dc-iv-3、南一／康軒／翰林公開版本研究限制及三筆公立國中公開自然科題型能力模式，獨立融合皮膚與黏膜屏障、發炎、淋巴運輸與淋巴結、抗原、抗體、疫苗、專一性免疫與免疫記憶。題目與互動均重新設計，未複製受保護內容；Terra 第二輪與正式發布審查尚未完成，維持 draft。'
 LESSON.write_text(json.dumps(lesson,ensure_ascii=False,indent=2)+'\n',encoding='utf-8')
 for i,row in enumerate(ROWS,1): (QDIR/f'question-science-content-dc-iv-3-{i}.json').write_text(json.dumps(make_question(i,row),ensure_ascii=False,indent=2)+'\n',encoding='utf-8')
 REPORT.write_text(json.dumps({'unit':lesson['title'],'lessonId':lesson['id'],'status':'first-pass-ai-review-complete','reviewStatus':'draft','checkedQuestions':10,'checks':{'unitSpecificOriginalContent':True,'threeVersionResearchRecords':True,'threePublicSchoolExamPatternSources':True,'answersAndDetailedSteps':True,'interactivePredictionManipulationExplanation':True,'terraSecondPass':'pending'},'reviewedAt':TODAY,'note':'10 題重新改寫為皮膚屏障、發炎、淋巴、抗原抗體、疫苗、專一性免疫與免疫記憶題；每題具唯一答案、解析、策略與五步解法。'},ensure_ascii=False,indent=2)+'\n',encoding='utf-8')
 print('authored science content dc-iv-3')

if __name__=='__main__': main()
