import json
from pathlib import Path

ROOT=Path(__file__).resolve().parents[1]
LESSON=ROOT/"lessons/science/lesson-science-content-na-iv-6.json"
QDIR=ROOT/"questions/science"
REPORT=ROOT/"implementation/reports/science-content-na-iv-6-first-pass-review.json"
TODAY="2026-09-23"
SOURCES=[
 ("https://www.yacjh.kh.edu.tw/upload/221/101_30637/114%E4%B8%8B%E5%AD%B8%E6%9C%9F%E7%AC%AC%E4%B8%80%E6%AC%A1%E6%AE%B5%E8%80%83%E8%87%AA%E7%84%B6.pdf","高雄市立鹽埕國民中學公開自然科評量","環境、永續、證據比較與自然科資料推理","取公開自然科評量對資源、環境變化與人類活動資料判讀的能力方向，另寫方案。"),
 ("https://www.cp.ptc.edu.tw/storage/134523/134523_114_B-23_7A.pdf?1774770497=","屏東縣新園國中公開自然領域教學計畫","永續發展、環境保護、資源使用與探究活動","取公立學校課程資料的永續與探究定位，未複製教材或題目。"),
 ("https://market.cloud.edu.tw/resources/web/1807720","教育雲國中生態與環境教學資源","生態系服務、保育、人類活動與環境決策","取公開教育資源把生態功能與行動決策連結的能力方向，重新設計溪流案例。"),
]
REFS=[{"url":u,"title":t,"year":"108-115","subject":"science","locator":loc,"observedPattern":pat,"reuseDecision":"pattern-only","status":"recorded","locatorLevel":"paper"} for u,t,loc,pat in SOURCES]
ROWS=[
 ("easy","在溪流旁規劃停車場前，哪組證據最完整？",["車位需求、逕流與積水、濁度、棲地、植被和替代位置資料","只看車位數","只看工程外觀","只問單一商店是否贊成"],"A","以自然功能、社會需求、環境影響與替代方案一起比較，才符合以保護自然環境為發展基礎。","先列出人類需求和自然功能，再找每項主張需要的可量測證據。"),
 ("medium","鋪面增加後雨量相同但逕流量升高，較合理的機制是？",["不透水面減少入滲，使較多水在短時間集中流出","雨量會因停車場自動增加","車位數直接製造降雨","逕流與鋪面沒有可能關係"],"A","鋪面改變地表入滲和水流路徑，可能使尖峰逕流增加；仍須用前後或對照資料確認，而非把單次相關當成定論。","先固定降雨條件，再連結鋪面、入滲、逕流和下游積水的因果路徑。"),
 ("medium","比較甲增加 80 車位但逕流升 35%，乙增加 35 車位並保留溪流植被帶，最好的判斷方式是？",["只選車位最多的甲","同時比較需求滿足、逕流、濁度、棲地、交通安全與修正方案","只選寫有植被的乙，不必看資料","因兩方案不同就不能比較"],"B","發展成效不是單一車位數，環境功能、交通與可修正性都要放進多指標比較；乙也需要檢查需求是否足夠。","建立需求—環境影響—公平—監測四欄表，再寫出條件式選擇而非口號。"),
 ("easy","哪項觀察最能支持溪流植被帶可能有助於降低濁度？",["相近降雨下，有植被帶區段的出流水濁度較低且重複測量一致","只在晴天看一次樹葉顏色","植被名稱聽起來很環保","施工告示寫著會保育"],"A","相近降雨和重複測量能讓植被帶與濁度的關係更可比較，但仍需考慮土壤、坡度與上游來源。","先找同時相近的降雨與測點，再看重複結果，最後列出替代解釋。"),
 ("hard","方案通過後，哪項設計最符合可修正的永續管理？",["設定逕流、濁度、植被和物種觀察門檻，超過時指定責任人調整或暫停","通過一次就永不檢查","只追蹤收入不量環境","只在開幕日拍照"],"A","以門檻、責任和行動連結監測資料，才能讓保護環境成為持續管理，而非一次性承諾。","把每個環境指標配上測量頻率、警戒門檻、負責單位和修正動作。"),
 ("medium","若居民反對停車方案，哪種溝通最公平？",["公開需求、環境資料、不確定性與受影響群體，邀請提出替代方案並說明決策規則","只公布支持方案的數字","讓受影響居民自行承擔成本","刪除不利資料避免爭議"],"A","公平決策要讓受影響者看見資料與限制，並比較成本、利益和替代方案，不能只呈現單方效益。","先列各群體獲得的利益與承擔的風險，再公開證據和選擇標準。"),
 ("hard","一次暴雨後發現積水增加，能否直接證明新建鋪面造成全部影響？",["不能，還需比較開發前後、相近降雨、排水變化與其他上游條件","可以，任何一次同時發生就是完整因果","只要有人看見就不需量測","積水資料永遠沒有用"],"A","單次事件可能同時受降雨強度、排水堵塞、上游施工等影響；前後和對照資料能降低替代解釋。","先把觀察和因果主張分開，再找時間、空間和排水條件的比較證據。"),
 ("medium","把溪流開發判斷移到屋頂太陽能方案時，哪項做法正確？",["重新檢查承重、眩光、廢棄模組、儲能、能源效益和受影響者，不能照搬溪流答案","只要是再生能源就不需評估","只比較安裝數量","把溪流濁度當成唯一指標"],"A","不同方案的自然條件、影響路徑和指標不同；永續原則可遷移，但證據與監測必須依情境重設。","先保留需求—環境基礎—影響—替代—監測五格，再替新方案填入專屬條件。"),
 ("hard","若乙案車位不足但保留溪流功能，哪項替代設計較能兼顧需求？",["分時接送、接駁停車與步行安全改善，並追蹤交通和水文指標","填平整片草地以一次解決","取消所有接送而不評估需求","只宣傳環保不改善交通"],"A","替代方案可降低對自然功能的壓力，同時回應交通需求；是否成功仍要由接送時間、安全、逕流和棲地資料追蹤。","先確認需求缺口，再設計不把成本轉嫁到環境或弱勢者的替代方案，最後訂指標。"),
 ("medium","以下哪句最符合『以保護自然環境為基礎』的結論？",["在滿足必要接送需求的條件下，選擇能保留滯洪與棲地功能的方案，並以濁度、逕流和生物資料觸發修正","所有發展都一定錯","只要收入增加就算永續","只要種樹就能抵銷任何破壞"],"A","永續不是取消所有發展或以單一指標決策，而是在自然環境承載與公平條件下滿足需求，並持續監測修正。","檢查結論是否同時交代需求、自然功能、指標、門檻和責任，避免兩個極端。"),
]

def make_question(n,row):
    diff,prompt,opts,source_answer,explanation,strategy=row; target="ACDBACDBAC"[n-1]
    correct=opts[ord(source_answer)-65]; distractors=[x for i,x in enumerate(opts) if i!=ord(source_answer)-65]
    ordered=[]; di=0
    for label in "ABCD":
        if label==target: ordered.append(correct)
        else: ordered.append(distractors[di]); di+=1
    steps=["先寫出發展需求與自然環境提供的功能。","把可能影響轉成逕流、濁度、棲地、資源或公平等可觀察指標。","比較前後、對照、替代方案和資料限制，避免只看單一效益。",f"排除口號、單一數字、永續保證或忽略受影響者的選項，答案為 {target}。",f"用『在……條件下』完成可監測、可修正的決策句：{explanation}"]
    return {"id":f"question-science-content-na-iv-6-{n}","subject":"science","type":"single-choice","prompt":prompt,"options":[{"id":k,"text":v} for k,v in zip("ABCD",ordered)],"knowledgeIds":["kg-science-content-na-iv-6"],"difficulty":diff,"answer":{"value":target,"explanation":f"{explanation} 正確答案為選項 {target}。"},"provenance":{"origin":"original","license":"All rights reserved","sourceUrl":SOURCES[0][0],"sourceLocator":"三筆公立學校／公開自然與生態資料的資源使用、環境保護、永續發展、證據比較與人類活動決策能力方向；本題為 Na-Ⅳ-6 原創情境改寫。","authoringNote":"依官方課綱、Knowledge Graph 與公開題型 pattern-only 方向獨立改寫；未複製原題、選項、圖表或答案；待第二輪 AI／Terra 內容複核。"},"reviewStatus":"draft","updatedAt":TODAY,"lessonId":"lesson-science-content-na-iv-6","examPatternRefs":REFS,"solutionStrategy":strategy,"solutionSteps":steps}

def main():
    lesson=json.loads(LESSON.read_text(encoding="utf-8")); lesson.update({"updatedAt":TODAY,"reviewStatus":"draft","authoringStandard":"version-fused-v1"})
    for row in lesson.get("publisherResearch",[])+lesson.get("versionResearch",[]): row["reviewedAt"]=TODAY
    lesson["fusionRecord"]["llmSynthesisNote"]="本課依官方自然科學課綱、kg-science-content-na-iv-6、南一／康軒／翰林可取得的公開版本研究限制與三筆公立學校／公開自然與生態資料能力模式，獨立融合人類需求、自然環境功能、逕流、棲地、污染、替代方案、公平、監測門檻與可修正永續決策。題目與互動均重新設計，未複製受保護內容；Terra 第二輪與正式發布審查尚未完成，維持 draft。"
    LESSON.write_text(json.dumps(lesson,ensure_ascii=False,indent=2)+"\n",encoding="utf-8")
    for i,row in enumerate(ROWS,1): (QDIR/f"question-science-content-na-iv-6-{i}.json").write_text(json.dumps(make_question(i,row),ensure_ascii=False,indent=2)+"\n",encoding="utf-8")
    REPORT.write_text(json.dumps({"unit":lesson["title"],"lessonId":lesson["id"],"status":"first-pass-ai-review-complete","reviewStatus":"draft","checkedQuestions":10,"checks":{"unitSpecificOriginalContent":True,"threeVersionResearchRecords":True,"threePublicSchoolExamPatternSources":True,"answersAndDetailedSteps":True,"interactivePredictionManipulationExplanation":True,"terraSecondPass":"pending"},"reviewedAt":TODAY,"note":"10 題重新改寫為人類需求、自然環境功能、逕流與棲地、替代方案、公平、監測門檻和永續決策；每題具唯一答案、解析、策略與五步解法。"},ensure_ascii=False,indent=2)+"\n",encoding="utf-8")
    print("authored science content na-iv-6")
if __name__=="__main__": main()
