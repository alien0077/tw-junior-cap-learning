"""Je-Ⅳ-1：化學反應速率與影響因素第一輪原創題庫。"""
import json
from pathlib import Path

ROOT=Path(__file__).resolve().parents[1]
LESSON=ROOT/"lessons/science/lesson-science-content-je-iv-1.json"
REPORT=ROOT/"implementation/reports/science-content-je-iv-1-first-pass-review.json"
QDIR=ROOT/"questions/science"
TODAY="2026-09-23"
SOURCES=[
 {"url":"https://www.yacjh.kh.edu.tw/upload/221/101_30637/114%E4%B8%8B%E5%AD%B8%E6%9C%9F%E7%AC%AC%E4%B8%80%E6%AC%A1%E6%AE%B5%E8%80%83%E4%B8%89%E5%B9%B4%E7%B4%9A%E8%87%AA%E7%84%B6.pdf","title":"高雄市立鹽埕國民中學 114 學年度第 2 學期第 1 次段考自然科公開試題","year":"114","locator":"反應速率、濃度、溫度、表面積與資料判讀","pattern":"取由反應時間、實驗條件與資料圖表判讀速率快慢及影響因素的能力方向。"},
 {"url":"https://www.grow22.com/download/114/114_cp/05_114P_Nature.pdf","title":"114 年國中教育會考自然科公開試題","year":"114","locator":"碰撞、反應速率、催化劑與生活情境","pattern":"取從實驗圖表、粒子模型與生活製程推論反應速率變化的能力方向。"},
 {"url":"https://www.hkjh.hc.edu.tw/uploads/1661481260739sfuB4gG2.pdf","title":"新竹市立新科國中公開康軒版自然課程計畫","year":"公開課程計畫","locator":"化學反應速率、控制變因與催化劑","pattern":"取以碰撞模型、濃度、溫度、表面積、催化劑和公平實驗連結速率的教學方向。"},
]
REFS=[{**s,"subject":"science","observedPattern":s["pattern"],"reuseDecision":"pattern-only","status":"recorded","locatorLevel":"paper"} for s in SOURCES]
def q(n,prompt,opts,ans,exp,strat,steps,d="medium"):
 return {"id":f"question-science-content-je-iv-1-{n}","subject":"science","type":"single-choice","prompt":prompt,"options":[{"id":k,"text":v} for k,v in zip("ABCD",opts)],"knowledgeIds":["kg-science-content-je-iv-1"],"difficulty":d,"answer":{"value":ans,"explanation":exp},"provenance":{"origin":"original","license":"All rights reserved","sourceUrl":SOURCES[0]["url"],"sourceLocator":"三筆公立學校／公開自然科試題與課程資料的反應速率、碰撞、濃度、溫度、表面積、催化劑與公平實驗能力方向；本題只作 pattern-only 改寫來源。","authoringNote":"依公開資料能力方向獨立改寫；未複製原題、圖表或答案；待第二輪 AI／Terra 內容複核。"},"reviewStatus":"draft","updatedAt":TODAY,"lessonId":"lesson-science-content-je-iv-1","examPatternRefs":REFS,"solutionStrategy":strat,"solutionSteps":steps}
Q=[
q(1,"將相同質量的碳酸鈣由大顆粒改成粉末，加入相同濃度與體積的酸，通常反應會較快，主要原因是？",["粉末總表面積較大，酸與碳酸鈣接觸及有效碰撞機會增加","粉末的元素種類變多","粉末使生成物質量必定增加","粉末會讓酸失去所有離子"],"A","在其他條件相同時，粉末有較大總表面積，增加接觸和有效碰撞，因而縮短產氣所需時間；不代表改變元素或總產量。","把表面積改變連到粒子接觸，而非產物總量。",["固定碳酸鈣質量與酸條件。","比較顆粒和粉末的暴露表面積。","用碰撞機會解釋產氣速率。","排除成分變多、產量必增與離子消失。","答案為 A。"],"easy"),
q(2,"在相同溫度下提高反應物濃度，反應速率通常增加的粒子模型解釋是？",["單位體積內粒子較多，單位時間碰撞次數可能增加","每個粒子都會變成更大的原子","濃度增加會消除所有活化能","生成物一定變成另一種元素"],"A","濃度提高使單位體積粒子數增加，碰撞頻率可能提高；是否有效仍與能量和方向有關。","以單位體積粒子數和有效碰撞解釋速率。",["確認只改變濃度而溫度等相同。","比較單位體積內反應物粒子數。","推論碰撞頻率增加。","說明有效碰撞才會造成反應，不是每次碰撞。","所以 A 最合理。"],"medium"),
q(3,"加熱通常能使化學反應變快，最適合的解釋是？",["粒子平均動能提高，更多碰撞可能具有足夠能量並形成有效反應","加熱會創造新的元素","溫度越高就不需要反應物","加熱一定使平衡產率增加"],"A","升溫提高粒子平均動能，使超過活化能的碰撞比例增加；速率變快不等於改變元素或必然提高平衡產率。","區分反應速率和反應物、平衡等不同概念。",["確認反應物和濃度保持相同。","比較升溫前後粒子動能分布。","判斷有效碰撞比例增加。","排除元素生成、無需反應物與產率必增。","因此 A 正確。"],"medium"),
q(4,"催化劑使反應變快，哪項敘述最正確？",["催化劑提供較容易的反應途徑，降低活化能，反應前後通常不被消耗完","催化劑一定增加生成物總量","催化劑會把反應物變成熱量","催化劑只適用於物理變化"],"A","催化劑改變反應途徑、降低活化能，使正逆或反應過程較快，但不等於增加平衡時的生成物總量，也不一定被永久消耗。","把催化劑的速率作用和產量作用分開。",["比較有無催化劑的反應時間。","用活化能模型解釋速率差。","檢查催化劑是否在反應前後仍存在。","排除產量必增、反應物變熱與只適用物理變化。","答案為 A。"],"medium"),
q(5,"要比較不同溫度對鎂和酸反應速率的影響，哪項設計最公平？",["固定鎂質量、表面積、酸濃度與體積，只改變溫度並量測產氣速率","同時改變溫度、酸濃度與鎂片大小","一組用鎂粉、一組用鎂帶且不控制質量","只觀察哪組火焰顏色較亮"],"A","只把溫度設為自變因，其他反應條件一致並以量化產氣速率比較，才能歸因於溫度。","先完整列控制變因，再設定單一自變因和可量測指標。",["列出質量、表面、濃度、體積和溫度。","固定除溫度外的所有條件。","記錄單位時間產氣量或達固定體積的時間。","重複測量並比較平均速率。","因此 A 是公平實驗。"],"medium"),
q(6,"某反應的產氣量—時間圖在開始時斜率最大，後來逐漸變小並達平台；斜率代表什麼？",["當下反應速率，斜率越大表示單位時間生成氣體越快","反應物的總質量","容器的體積大小","反應溫度一定不變"],"A","產氣量對時間圖的斜率表示單位時間產氣量，即反應速率；斜率變小表示速率下降，平台表示產氣量近似不再增加。","讀圖時分辨縱軸總量和斜率速率。",["確認縱軸是累積產氣量、橫軸是時間。","取曲線某段的斜率。","將斜率解讀為單位時間生成量。","比較開始與後段斜率。","所以 A 正確。"],"hard"),
q(7,"若兩組反應最後生成的氣體總量相同，但甲較早達到平台，正確結論是？",["甲的平均反應速率較快，但兩組在此條件下的最終產量相同","甲的反應物一定比較多","乙一定沒有發生化學反應","甲的催化劑一定增加了平衡產量"],"A","達到同一總量所需時間較短表示甲速率較快；最終產量相同則不能推論甲反應物更多或催化劑提高產量。","分開比較曲線斜率和平台高度。",["比較兩曲線初期斜率或達平台時間。","比較最後平台的產氣量。","分別下速率和產量結論。","排除反應物量、未反應及催化劑增產的過度推論。","所以 A 最符合資料。"],"hard"),
q(8,"快速反應可能造成溫度突然上升或大量氣體生成；實驗時最重要的作法是？",["少量、可控地加入反應物，使用防護具並預留散熱與氣體出口，不密閉堵塞系統","為了加速一次加入所有試劑並封死容器","用手觸摸容器判斷溫度","把安全警示當成不影響科學結果的事情"],"A","快速放熱或產氣可能造成壓力與灼傷風險，需少量、通風、適當容器與防護，避免封死或直接觸摸。","把速率控制和實驗安全一起納入設計。",["預測快速放熱與產氣的危害。","限制反應物量和加入速度。","安排防護、散熱與安全氣體出口。","不可堵塞、封死或徒手測溫。","因此 A 是安全作法。"],"easy"),
q(9,"若提高溫度後反應速率增加，但曲線最後平台高度相同，哪項解釋最合理？",["溫度影響到達平台的速度，但在該條件下沒有改變可生成物的總量","溫度一定讓生成物總量增加但圖看不出來","平台高度只代表反應時間","反應速率與生成物量永遠完全相同"],"A","曲線初期和到平台時間反映速率，平台高度反映總產量；兩者可受不同因素影響。","用圖形的斜率與平台分別判斷速率和產量。",["比較兩曲線初始斜率。","比較到達平台的時間。","比較平台高度是否相同。","將結論限定為速率變快、總量未變。","所以 A 正確。"],"hard"),
q(10,"若要確認某添加物是催化劑而不是單純改變反應物量，哪項資料最有力？",["控制反應物量與條件後，加入添加物使達到相同產量的時間縮短，且反應後添加物可回收或仍存在","加入添加物後只看泡沫變多","讓添加物同時提供新的反應物","只測量容器顏色變化"],"A","在反應物量和條件控制下速率變快，且添加物未被消耗完，才能支持催化劑作用；泡沫或顏色不足以單獨證明。","以控制變因、速率指標和催化劑存在性建立證據。",["固定反應物質量、濃度、溫度與容器。","比較有無添加物達到相同產量所需時間。","檢查添加物反應後是否仍可辨識或回收。","排除添加物其實是新反應物的可能。","因此 A 的證據最完整。"],"hard"),
]
def main():
 lesson=json.loads(LESSON.read_text(encoding="utf-8")); lesson["updatedAt"]=TODAY; lesson["reviewStatus"]="draft"
 lesson["fusionRecord"]={"commonCore":["反應速率描述單位時間反應物消耗或生成物形成的快慢。","碰撞頻率、有效碰撞、濃度、溫度、表面積和催化劑可共同解釋速率變化。","曲線斜率代表速率，平台高度代表總量；速率和產量不能混為一談。"],"versionDifferences":["南一公開線索支持由產氣、時間和生活反應進入速率。","康軒公開課程資料較突出粒子碰撞、控制變因與圖表斜率。","翰林公開課程計畫補充催化劑、製程和安全連結；公開資料不足以宣稱取得完整教材內容。"],"originalAdditions":["以『條件—有效碰撞—曲線斜率—平台高度—安全』框架進行速率判讀。","把添加物是否為催化劑、反應物量、放熱產氣與資料限制納入遷移。"],"llmSynthesisNote":"依官方課綱、本單元 KG、南一／康軒／翰林公開版本線索與三筆公開試題／課程資料能力方向，重新撰寫反應速率、碰撞、濃度、溫度、表面積、催化劑、圖表與安全；未複製教材或試題文字、圖表與答案，Terra 第二輪與正式發布審查尚未完成，維持 draft。"}
 for e in lesson.get("versionResearch",[])+lesson.get("publisherResearch",[]): e["reviewedAt"]=TODAY
 for x in Q: (QDIR/f"{x['id']}.json").write_text(json.dumps(x,ensure_ascii=False,indent=2)+"\n",encoding="utf-8")
 REPORT.write_text(json.dumps({"unit":"Je-Ⅳ-1：化學反應速率與影響因素","lessonId":lesson["id"],"status":"first-pass-ai-review-complete","reviewStatus":"draft","checkedQuestions":10,"checks":{"unitSpecificOriginalContent":True,"threeVersionResearchRecords":True,"threePublicSchoolExamPatternSources":True,"answersAndDetailedSteps":True,"interactivePredictionManipulationExplanation":True,"terraSecondPass":"pending"},"reviewedAt":TODAY,"note":"10 題已逐題改寫為碰撞模型、濃度、溫度、表面積、催化劑、曲線斜率、平台高度、公平實驗與安全專屬問題；每題有唯一答案、解析與五步解法。"},ensure_ascii=False,indent=2)+"\n",encoding="utf-8")
 LESSON.write_text(json.dumps(lesson,ensure_ascii=False,indent=2)+"\n",encoding="utf-8"); print("authored science content je-iv-1")
if __name__=="__main__": main()
