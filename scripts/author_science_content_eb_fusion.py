"""Eb：力與運動第一輪來源融合與題目錯置修復。"""
import json
from pathlib import Path
ROOT=Path(__file__).resolve().parents[1]; LESSON=ROOT/"lessons/science/lesson-science-content-eb.json"; REPORT=ROOT/"implementation/reports/science-content-eb-first-pass-review.json"; QDIR=ROOT/"questions/science"; TODAY="2026-09-23"
SOURCES=[
 {"url":"https://www.grow22.com/download/114/114_cp/05_114P_Nature.pdf","title":"114 年國中教育會考自然科公開試題","year":"114","locator":"受力、運動、慣性、加速度與資料判讀","pattern":"取由力的大小方向、合力、速度變化與運動資料推論物體運動的能力方向。"},
 {"url":"https://www.hkjh.hc.edu.tw/uploads/1661481260739sfuB4gG2.pdf","title":"新竹市立新科國中公開康軒版自然課程計畫","year":"公開課程計畫","locator":"力與運動、牛頓定律、摩擦與受力圖","pattern":"取受力圖、合力、慣性、加速度、摩擦與實驗評量方向。"},
 {"url":"https://lgt.ntpc.edu.tw/TeachPlanFile_Upload/2022/plan/641_plan.pdf","title":"新北市文山區安康高中國中部公開翰林版自然簡案","year":"公開課程計畫","locator":"力學運動、質量、力與資料探究","pattern":"取力—質量—加速度關係、運動圖表、控制變因與模型限制的能力方向。"},
]
def refs(): return [{**s,"subject":"science","observedPattern":s["pattern"],"reuseDecision":"pattern-only","status":"recorded","locatorLevel":"paper"} for s in SOURCES]
QUESTIONS=[
 ("小車受到向東 8 N 與向西 3 N 的水平力，合力為何？",["向東 5 N","向西 5 N","向東 11 N","零"],"A","先選正方向，再以相反方向力相減。",["取向東為正。","向東力為 +8 N，向西力為 −3 N。","合力為 8−3＝+5 N。","正號表示向東。","答案為 A。"]),
 ("物體受到合力為零，但原本正向東等速運動，之後最合理的狀態是？",["維持向東等速運動","立即停止","必定向西加速","速度一定變成兩倍"],"A","用牛頓第一定律區分合力零與靜止。",["題目給出合力為零。","合力零表示加速度為零。","若原本已有向東速度，速度會維持。","只有原本靜止才維持靜止。","所以選 A。"]),
 ("質量 2 kg 的小車受到向東 10 N 合力，加速度大小為何？",["5 m/s² 向東","20 m/s² 向東","0.2 m/s² 向西","12 m/s² 向東"],"A","代入 F＝ma，並保留力的方向。",["寫出 a＝F/m。","代入 F＝10 N、m＝2 kg。","a＝10÷2＝5 m/s²。","合力向東，所以加速度也向東。","選 A。"]),
 ("公車突然向前起步時，乘客上半身相對車內向後傾，主要原因是？",["身體具有維持原運動狀態的慣性","重力突然變成向後","乘客受到向後的磁力","車內沒有任何力"],"A","比較車輛和乘客原本的運動狀態。",["起步前乘客與公車近似靜止。","公車向前加速，身體傾向維持原本狀態。","這種抗拒運動狀態改變的性質稱為慣性。","不是重力方向改變或磁力作用。","故選 A。"]),
 ("水平桌面上的箱子向右等速滑動，忽略空氣阻力時，水平方向受力應如何描述？",["向右拉力與向左摩擦力大小相等","只有向右拉力沒有反作用","只有向左摩擦力且合力向左","摩擦力一定為零"],"A","由等速判斷水平方向合力，再配對受力。",["等速表示水平方向加速度為零。","因此水平合力為零。","若有向右拉力，必有等大的向左摩擦力。","摩擦力方向與相對滑動方向相反。","答案為 A。"]),
 ("同樣合力作用在 2 kg 與 6 kg 的推車上，哪台加速度較大？",["2 kg 推車","6 kg 推車","兩者一定相同","無法由質量判斷"],"A","固定合力時用 a＝F/m 比較質量與加速度。",["兩台車受到相同合力。","加速度與質量成反比。","質量較小的 2 kg 車加速度較大。","不需要知道力的具體數值也可作比例判斷。","所以選 A。"]),
 ("研究推力大小對小車加速度的影響時，哪項設計最公平？",["固定小車質量與路面，只改變水平推力並量測加速度","同時改變質量、推力和路面","只記錄車子顏色","每次使用不同量具且不重複"],"A","只改變自變因，固定會影響結果的條件。",["自變因是推力大小。","小車質量和路面摩擦會影響加速度，需固定。","重複測量並記錄加速度。","同時改變多項條件無法歸因。","答案為 A。"]),
 ("書本靜止在水平桌面上，哪項受力描述正確？",["重力向下與桌面支持力向上，大小相等","書本完全沒有受到力","只有重力沒有支持力","支持力方向向下且大於重力"],"A","畫自由體圖，分清合力零和沒有受力。",["書本受到地球重力向下。","桌面提供垂直向上的支持力。","靜止表示兩力大小相等、方向相反。","合力為零不代表每個力都不存在。","選 A。"]),
 ("滑板車停止踩踏後在粗糙地面上逐漸減速，造成速度改變的主要原因是？",["摩擦力與速度方向相反，造成反向合力","慣性主動把速度降低","重力一定水平向後","空氣顏色改變"],"A","找出與速度方向相反的實際力，再判斷加速度方向。",["滑行方向是前進方向。","粗糙地面提供反向摩擦力。","反向合力造成減速。","慣性不是一種主動施力。","因此選 A。"]),
 ("若受力圖顯示水平合力由 4 N 增為 8 N，而質量固定，依 F＝ma 加速度如何變化？",["加倍","減半","不變","變成零"],"A","固定質量時比較合力與加速度的正比關係。",["由 F＝ma 得 a＝F/m。","質量固定，分母不變。","合力從 4 N 變 8 N 是兩倍。","加速度也變為兩倍。","答案為 A。"]),
]
def main():
 lesson=json.loads(LESSON.read_text(encoding="utf-8")); lesson["updatedAt"]=TODAY; lesson["reviewStatus"]="draft"; lesson["fusionRecord"]={"commonCore":["三版本公開線索共同支持由受力圖、合力、慣性與加速度連結力和運動變化。","牛頓定律、F＝ma、摩擦、控制變因與運動資料判讀是共同能力核心。"],"versionDifferences":["南一公開定位偏向力與運動現象；康軒線索偏向受力圖、慣性、摩擦與定律；翰林線索偏向質量—力—加速度資料與探究設計。公開資料不足以宣稱取得完整教材內容。"],"originalAdditions":["以推車、煞車與受力卡工作台建立方向、合力、加速度和系統邊界的可操作證據鏈。","把合力零等於沒有受力、慣性是力、速度變化只看單一力列為單元迷思診斷。"],"llmSynthesisNote":"依官方課綱、本單元 KG、南一／康軒／翰林公開版本線索與三筆公立學校公開自然科試題／課程資料能力方向，重新組織受力、運動、慣性、加速度、F＝ma與實驗資料；已移除原先只重複平均速率且未涵蓋課程核心的批次題，10 題題幹、選項、答案、解析與五步解法均為原創，未複製教材或試題文字、圖表與答案。Terra 第二輪與正式發布審查尚未完成，維持 draft。"}
 for e in lesson.get("versionResearch",[])+lesson.get("publisherResearch",[]): e["reviewedAt"]=TODAY
 for i,(prompt,opts,ans,strategy,steps) in enumerate(QUESTIONS,1):
  p=QDIR/f"question-science-content-eb-{i}.json"; q=json.loads(p.read_text(encoding="utf-8")); q["prompt"]=prompt; q["options"]=[{"id":chr(65+j),"text":t} for j,t in enumerate(opts)]; q["answer"]={"value":ans,"explanation":f"{steps[-2]} {steps[-1]} 正確答案：{ans}。"}; q["provenance"]={"origin":"original","license":"All rights reserved","sourceUrl":SOURCES[0]["url"],"sourceLocator":"三筆公立學校公開自然科試題／課程資料的力與運動、受力圖、牛頓定律與資料判讀能力方向；本題只作 pattern-only 改寫。","authoringNote":"本題取公開資料能力方向，題幹、選項、答案、解析與五步解法均依 Eb 單元重新撰寫，未複製原題、圖表或答案；待第二輪 AI／Terra 內容複核。"}; q["examPatternRefs"]=refs(); q["solutionStrategy"]=strategy; q["solutionSteps"]=steps; q["reviewStatus"]="draft"; q["updatedAt"]=TODAY; p.write_text(json.dumps(q,ensure_ascii=False,indent=2)+"\n",encoding="utf-8")
 REPORT.write_text(json.dumps({"unit":"Eb：力與運動","lessonId":lesson["id"],"status":"first-pass-ai-review-complete","reviewStatus":"draft","checkedQuestions":10,"checks":{"unitSpecificOriginalContent":True,"threeVersionResearchRecords":True,"threePublicSchoolExamPatternSources":True,"answersAndDetailedSteps":True,"interactivePredictionManipulationExplanation":True,"unitMismatchRemediated":True,"terraSecondPass":"pending"},"reviewedAt":TODAY,"note":"已移除原先只重複平均速率且未涵蓋 Eb 核心的批次題；三筆公開試題／課程資料僅作 pattern-only 來源，版本融合、逐題內容 QA、Terra 第二輪與正式發布尚未完成，維持 draft。"},ensure_ascii=False,indent=2)+"\n",encoding="utf-8")
 LESSON.write_text(json.dumps(lesson,ensure_ascii=False,indent=2)+"\n",encoding="utf-8"); print("authored science content eb")
if __name__=="__main__": main()
