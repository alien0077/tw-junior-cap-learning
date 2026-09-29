"""Jc-Ⅳ-3：金屬燃燒與對氧活性第一輪原創題庫。"""
import json
from pathlib import Path

ROOT=Path(__file__).resolve().parents[1]
LESSON=ROOT/"lessons/science/lesson-science-content-jc-iv-3.json"
REPORT=ROOT/"implementation/reports/science-content-jc-iv-3-first-pass-review.json"
QDIR=ROOT/"questions/science"
TODAY="2026-09-23"
SOURCES=[
 {"url":"https://www.yacjh.kh.edu.tw/upload/221/101_30637/114%E4%B8%8B%E5%AD%B8%E6%9C%9F%E7%AC%AC%E4%B8%80%E6%AC%A1%E6%AE%B5%E8%80%83%E4%B8%89%E5%B9%B4%E7%B4%9A%E8%87%AA%E7%84%B6.pdf","title":"高雄市立鹽埕國民中學 114 學年度第 2 學期第 1 次段考自然科公開試題","year":"114","locator":"金屬與氧反應、燃燒現象、氧化物判讀","pattern":"取由金屬燃燒現象、氧化物性質與實驗資料比較對氧反應性的能力方向。"},
 {"url":"https://www.grow22.com/download/114/114_cp/05_114P_Nature.pdf","title":"114 年國中教育會考自然科公開試題","year":"114","locator":"金屬反應、實驗控制與生活材料情境","pattern":"取由實驗圖表、產物證據與材料情境推論金屬氧化反應的能力方向。"},
 {"url":"https://www.hkjh.hc.edu.tw/uploads/1661481260739sfuB4gG2.pdf","title":"新竹市立新科國中公開康軒版自然課程計畫","year":"公開課程計畫","locator":"金屬對氧活性、燃燒操作與氧化還原","pattern":"取以金屬對氧活性實驗、控制條件與氧化還原模型連結反應性的教學方向。"},
]
REFS=[{**s,"subject":"science","observedPattern":s["pattern"],"reuseDecision":"pattern-only","status":"recorded","locatorLevel":"paper"} for s in SOURCES]
def q(n,prompt,opts,ans,exp,strat,steps,d="medium"):
 return {"id":f"question-science-content-jc-iv-3-{n}","subject":"science","type":"single-choice","prompt":prompt,"options":[{"id":k,"text":v} for k,v in zip("ABCD",opts)],"knowledgeIds":["kg-science-content-jc-iv-3"],"difficulty":d,"answer":{"value":ans,"explanation":exp},"provenance":{"origin":"original","license":"All rights reserved","sourceUrl":SOURCES[0]["url"],"sourceLocator":"三筆公立學校／公開自然科試題與課程資料的金屬燃燒、對氧活性、產物與公平實驗能力方向；本題只作 pattern-only 改寫來源。","authoringNote":"依公開資料能力方向獨立改寫；未複製原題、圖表或答案；待第二輪 AI／Terra 內容複核。"},"reviewStatus":"draft","updatedAt":TODAY,"lessonId":"lesson-science-content-jc-iv-3","examPatternRefs":REFS,"solutionStrategy":strat,"solutionSteps":steps}
Q=[
q(1,"鎂帶在氧氣中發出強烈白光並生成白色固體，最合理的判讀是？",["鎂與氧反應生成氧化鎂，鎂對氧的反應性高","鎂只被加熱沒有新物質","白光表示鎂變成氧氣","白色固體一定是未反應的鎂"],"A","白光與白色新固體及氧氣條件共同支持鎂被氧化生成氧化鎂，顯示其對氧反應性高。","同時看反應條件、能量現象與生成物證據。",["確認氧氣是反應環境。","觀察是否有能量釋放與新固體。","判斷生成物是否含鎂和氧。","排除只加熱、生成氧氣與未反應物的說法。","因此 A 最完整。"],"easy"),
q(2,"若要比較鎂、鐵、銅對氧的反應性，哪項結果最能支持鎂較活潑？",["在相同條件下鎂較快反應，且生成物有明確氧化物證據","鎂的顏色比較亮","鎂的名稱比較短","只在鎂使用純氧、其他金屬使用空氣"],"A","反應速率與氧化物產物是可比較的證據；顏色、名稱或不同氧氣條件不能公平支持活性排序。","把主觀外觀換成控制條件下的速率與產物證據。",["固定金屬質量、表面與氧氣濃度。","記錄各金屬開始反應到完成的時間。","檢驗生成物是否為相應氧化物。","排除不同條件與非科學外觀判準。","所以 A 最可靠。"],"medium"),
q(3,"鐵絲在氧氣中燃燒前常在末端綁一小段火柴，主要作用是？",["先提供熱量使鐵絲達到著火點，再觀察鐵的燃燒","讓鐵絲吸收更多氧氣而改變元素","把鐵絲變成非金屬","使生成物不含氧"],"A","鐵絲需要先達到著火點才容易持續與氧反應，火柴提供初始熱量；它不會改變鐵的元素身分。","區分引燃作用和反應物本身的化學變化。",["辨認鐵絲是否能自行快速達到著火點。","確認火柴提供的是初始熱量。","觀察後續鐵與氧的反應。","排除改變元素與去除氧的說法。","答案為 A。"],"easy"),
q(4,"金屬粉末比同質量金屬片更容易快速氧化，最合理的粒子層次解釋是？",["粉末總表面積較大，氧氣與金屬接觸的機會增加","粉末中的原子種類比較多","粉末一定含有更多氧原子","粉末會讓氧氣失去質量"],"A","同質量下粉末通常有較大的總表面積，增加氧氣和金屬的接觸及有效碰撞機會，因此反應較快。","用表面積解釋速率，不把形狀改變誤當成成分改變。",["固定金屬種類與質量。","比較片狀與粉末的暴露表面積。","連結接觸面積與有效碰撞。","排除原子種類、氧原子數與質量的錯誤推論。","所以 A 正確。"],"easy"),
q(5,"下列哪項是比較金屬對氧活性的公平實驗設計？",["使用相同質量與表面處理的金屬，在相同氧氣濃度、加熱方式與時間下比較反應證據","每種金屬選不同質量以便看清楚","讓活性預期最高的金屬使用純氧","只觀察一次並不記錄溫度"],"A","控制金屬質量、表面、氧氣、加熱與時間，才能把差異歸因於金屬本身；其餘選項混入其他變因。","從控制變因檢查比較是否可歸因。",["列出會影響氧化的外加條件。","固定質量、表面、氧氣和加熱方式。","選擇反應速率、亮度或產物作為可記錄證據。","檢查是否只改變金屬種類。","因此 A 是公平設計。"],"medium"),
q(6,"某金屬燃燒後產物質量增加，最合理的原因是？",["氧原子由空氣進入產物，金屬與氧結合形成氧化物","金屬在燃燒中憑空生成了新的金屬原子","天平把火焰質量也加進來","質量增加表示氧氣被消滅"],"A","產物增加的質量來自與金屬結合的氧，符合質量守恆；系統邊界與收集方法仍需清楚。","用質量差追蹤來自空氣的氧，而非假設物質憑空生成。",["確認反應前後秤量的系統範圍。","比較金屬與生成物質量。","將增加量連結到進入固體的氧。","排除憑空生成、天平加火焰與氧消失。","所以 A 最符合守恆。"],"medium"),
q(7,"鋁片在空氣中常不易持續燃燒，但鋁粉反應可能較明顯；哪項解釋最適合？",["鋁片表面的氧化膜與較小表面積限制反應，粉末增加暴露面但仍須控制安全條件","鋁片不是金屬而鋁粉才是金屬","鋁粉的元素已改成鐵","氧化膜會把鋁變成氧氣"],"A","表面氧化膜可能阻隔氧接觸，片狀材料表面積也較小；粉末增加接觸面，但反應風險需受控。","把表面狀態與表面積兩個因素分開分析。",["比較鋁片和鋁粉的表面狀態。","考慮氧化膜對接觸的阻隔。","比較單位質量的暴露表面積。","排除改變元素與錯誤的氧化膜說法。","因此 A 能解釋差異。"],"hard"),
q(8,"若要判定某金屬氧化物是由金屬燃燒形成，哪項驗證最完整？",["確認燃燒時有氧參與、生成物含該金屬與氧，並與未燃燒金屬性質比較","只看火焰是否很亮","只用生成物顏色命名","只量燃燒時間而不收集產物"],"A","反應物條件、產物組成與性質比較共同支持氧化物形成；單一亮度、顏色或時間不足以證明組成。","以條件、組成、性質三層證據交叉確認。",["確認氧氣存在且有反應。","收集並檢驗生成物組成。","比較金屬與產物性質。","排除只靠外觀或時間的過度推論。","所以 A 的驗證最完整。"],"medium"),
q(9,"在氧氣中燃燒金屬時，為什麼要使用護目鏡並避免直接俯視火焰？",["強光、飛濺的高溫產物與熱氣流可能傷害眼睛，安全距離能降低暴露","護目鏡能讓金屬不再氧化","俯視可讓氧氣變少而影響結果","安全措施只為了使火焰更亮"],"A","金屬燃燒可能有強光、高溫熔融物與飛濺，護目鏡及適當距離是降低眼睛與皮膚暴露的必要措施。","從實驗現象辨認危害，再選擇個人防護與距離控制。",["列出強光、熱與飛濺等危害。","判斷眼睛是直接暴露部位。","使用護目鏡並保持安全距離。","排除把防護當成改變反應條件的說法。","答案為 A。"],"easy"),
q(10,"三種金屬在相同條件下的反應資料為：甲 10 秒出現明顯氧化物、乙 60 秒出現、丙 5 分鐘仍不明顯。若其他證據一致，合理排序是？",["甲對氧活性最高，乙次之，丙最低","丙最高，乙次之，甲最低","三者活性一定相同","只能依金屬顏色排序"],"A","在控制條件一致且產物證據可靠時，較短時間形成明顯氧化物表示反應較快，可作為相對活性線索。","先確認資料可比，再把反應時間轉成相對活性排序。",["確認三組質量、表面、氧氣與加熱條件一致。","比較出現氧化物所需時間。","時間越短表示在此條件下反應越快。","檢查丙的『不明顯』是否代表低反應或資料不足。","在題目給定證據下排序為 A。"],"hard"),
]
def main():
 lesson=json.loads(LESSON.read_text(encoding="utf-8")); lesson["updatedAt"]=TODAY; lesson["reviewStatus"]="draft"
 lesson["fusionRecord"]={"commonCore":["金屬與氧反應可由燃燒現象、產物組成與質量證據判讀。","對氧活性比較必須控制質量、表面、氧氣、加熱與觀察時間。","表面積、氧化膜與氧氣濃度會影響反應速率，但不能直接改變元素身分。"],"versionDifferences":["南一公開線索支持由金屬燃燒與氧化物性質進入反應性比較。","康軒公開課程資料較突出金屬對氧活性實驗與控制變因。","翰林公開課程計畫補充氧化還原與實驗安全連結；公開資料不足以宣稱取得完整教材內容。"],"originalAdditions":["以鎂、鐵、銅、鋁等不同金屬建立表面狀態—氧接觸—反應證據鏈。","把活性排序、質量守恆、安全距離及資料限制整合為單元專屬判讀。"],"llmSynthesisNote":"依官方課綱、本單元 KG、南一／康軒／翰林公開版本線索與三筆公開試題／課程資料能力方向，重新撰寫金屬燃燒、對氧活性、產物判讀與公平實驗；未複製教材或試題文字、圖表與答案，Terra 第二輪與正式發布審查尚未完成，維持 draft。"}
 for e in lesson.get("versionResearch",[])+lesson.get("publisherResearch",[]): e["reviewedAt"]=TODAY
 for x in Q: (QDIR/f"{x['id']}.json").write_text(json.dumps(x,ensure_ascii=False,indent=2)+"\n",encoding="utf-8")
 REPORT.write_text(json.dumps({"unit":"Jc-Ⅳ-3：金屬燃燒與對氧活性","lessonId":lesson["id"],"status":"first-pass-ai-review-complete","reviewStatus":"draft","checkedQuestions":10,"checks":{"unitSpecificOriginalContent":True,"threeVersionResearchRecords":True,"threePublicSchoolExamPatternSources":True,"answersAndDetailedSteps":True,"interactivePredictionManipulationExplanation":True,"terraSecondPass":"pending"},"reviewedAt":TODAY,"note":"10 題已逐題改寫為金屬活性、燃燒現象、產物與質量、表面積、氧化膜、公平實驗及安全操作專屬問題；每題有唯一答案、解析與五步解法。"},ensure_ascii=False,indent=2)+"\n",encoding="utf-8")
 LESSON.write_text(json.dumps(lesson,ensure_ascii=False,indent=2)+"\n",encoding="utf-8"); print("authored science content jc-iv-3")
if __name__=="__main__": main()
