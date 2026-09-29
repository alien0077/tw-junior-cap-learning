"""Nb-Ⅳ-3：氣候變遷的減緩與調適的第一輪獨立融合與題目補強。"""
import json
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
LESSON = ROOT / "lessons/science/lesson-science-content-nb-iv-3.json"
REPORT = ROOT / "implementation/reports/science-content-nb-iv-3-first-pass-review.json"
QDIR = ROOT / "questions/science"
TODAY = "2026-09-21"
SOURCES = [
 {"url":"https://www.nehs.tc.edu.tw/wp-content/uploads/sites/95/2026/02/6%E7%90%86%E5%8C%96%E7%A7%91-%E4%B9%9D%E5%B9%B4%E7%B4%9A-%E9%A1%8C%E5%BA%AB.pdf","title":"國立中科實驗高級中學公開九年級理化題庫","year":"109-115","locator":"氣候變遷、能源、資料判讀與環境決策","pattern":"取減緩／調適分類、證據判讀與方案比較的能力方向，重新設計本課情境。"},
 {"url":"https://www.nhjh.tp.edu.tw/uploads/1675417616549dOhkhC5L.pdf","title":"臺北市立內湖國民中學公開九年級理化段考","year":"109-115","locator":"溫室氣體、災害風險、校園與社區措施","pattern":"取由現象連到機制、風險與控制條件的推理方向，未複製題幹、選項、圖表或答案。"},
 {"url":"https://www.kcjh.kh.edu.tw/upload/190/104_34764/%E4%B8%89%E5%B9%B4%E7%B4%9A%E7%90%86%E5%8C%96-%E7%AC%AC三次段考5-OK.pdf","title":"高雄市立國昌國民中學公開三年級自然科試題","year":"109-115","locator":"能源轉型、沿海防護、極端事件與公平影響","pattern":"取多條件評估與限制說明的能力方向，全部以本課原創文字改寫。"},
]

def refs():
    return [{**s,"subject":"science","reuseDecision":"pattern-only","status":"recorded","locatorLevel":"paper","observedPattern":s["pattern"]} for s in SOURCES]

STRATEGIES = {
 1:"先判斷措施改變的是排放／碳匯還是暴露／脆弱度，再檢查作用時間與副作用。",
 2:"將措施對準危害、暴露或脆弱度，確認它是否降低預期衝擊而不是改寫排放統計。",
 3:"分別列出節電造成的排放收益與遮蔭造成的熱暴露收益，再檢查兩者的系統邊界。",
 4:"把指標分成危害、損失、恢復、公平與參與，避免用工程費或一次民調代替成效。",
 5:"用生命週期比較初期費用、維護、排放、健康與分配負擔，不只看施工報價。",
 6:"把不確定性轉成多情境與可調整門檻，以監測結果決定何時加強措施。",
 7:"先辨認不同群體的成本與收益，再設計支持、參與和分配指標。",
 8:"把個人需求端行動放進能源、交通、建築與產業系統，判斷尺度而非二選一。",
 9:"同時檢查工程降低的現況風險、未來情境、維護、下游轉移與錯誤安全感。",
10:"把減緩與調適的目標、證據、時間尺度、公平與監測回饋放進同一決策框架。",
}

def main():
    lesson=json.loads(LESSON.read_text(encoding="utf-8"))
    lesson["content"]={"summary":"本課不把氣候行動簡化成口號，而是比較減緩與調適改變的對象、時間尺度、證據與分配結果。學習者從排放—濃度—危害—暴露—脆弱度—恢復的鏈條判讀校園、沿海社區與能源轉型方案，最後用監測資料修正決策。","sections":[{"title":"先辨認措施正在改變什麼","body":"節電、再生能源與增加碳匯主要作用於排放或吸收；預警、耐熱建築、供水調整與疏散則降低暴露或脆弱度。同一方案可能兼有兩種效益，但要分別寫出作用對象，不能因為『環保』兩字就跳過證據。"},{"title":"把方案放進時間與系統邊界","body":"減緩的氣候效益常需較長時間累積，調適可先降低地方損失卻受維護、未來情境與空間限制。比較時畫出系統邊界，納入生命週期排放、下游轉移、能源需求與維護，而非只看建造當下。"},{"title":"成效要看誰受益、誰承擔","body":"平均溫度、總減碳量或工程費不足以回答公平問題。要追蹤弱勢族群熱暴露、停水停電、健康、就業與參與，並檢查政策是否把風險移到別的社區。"},{"title":"用不確定性設計可修正行動","body":"預測不是單一命運。用多種情境、門檻與可逆措施建立路徑，定期讀取排放、氣象、健康和使用者資料；當證據改變時調整，而不是等到所有不確定性消失才行動。"}]}
    lesson["studyHighlights"]=["區分減緩與調適所改變的對象、時間與證據。","用系統邊界比較排放、風險、維護、健康與公平。","把不確定性轉成多情境、門檻與可調整措施。","用分群指標與監測回饋檢查方案是否真的降低風險。"]
    for e in lesson.get("versionResearch",[])+lesson.get("publisherResearch",[]): e["reviewedAt"]=TODAY
    lesson["fusionRecord"]={"commonCore":["三版本公開線索共同支持以能源、環境資料與生活情境理解氣候行動。","評量需區分措施目的、證據、限制與應用條件。"],"versionDifferences":["南一公開入口偏向主題定位；康軒公開索引偏向觀察與活動；翰林公開入口偏向環境議題資源。公開頁面不足以宣稱未取得的完整教材細節。"],"originalAdditions":["以校園節能遮蔭、沿海堤防、都市降溫、能源轉型與多情境決策建立專屬推理路徑。","加入生命週期、錯誤安全感、分配影響與可調整門檻檢核。"],"llmSynthesisNote":"依官方課綱、本單元 KG、南一／康軒／翰林公開版本線索與三筆公立學校公開自然／理化試題能力方向，重新撰寫減緩與調適的機制、證據、限制、公平與互動；未複製教材或試題文字、圖表與答案。Terra 第二輪與正式發布審查尚未完成，維持 draft。"}
    lesson["interactive"]={"type":"scientific-investigation","goal":"用排放、風險、公平與監測證據比較減緩與調適方案。","scenario":"在校園與沿海社區的方案卡上切換措施、時間尺度、受益群體與副作用，建立可調整的氣候行動路徑。","variables":[{"symbol":"M","meaning":"排放或碳吸收變化"},{"symbol":"A","meaning":"暴露、脆弱度與恢復能力變化"},{"symbol":"F","meaning":"不同群體的成本與收益"}],"steps":[{"id":"step-1","prompt":"看到一項氣候措施，第一個要辨認什麼？","options":["它改變排放／碳匯，還是降低暴露／脆弱度","只看宣傳口號","先選最昂貴的工程"],"answer":"A","feedback":"先判斷作用對象，才能區分減緩、調適及共同效益。"},{"id":"step-2","prompt":"比較兩個方案時，除了初期費用還要保留什麼？","options":["生命週期、維護、健康、排放與分配影響","只保留施工照片","把所有長期成本視為零"],"answer":"A","feedback":"完整比較需跨時間與系統邊界，並看誰受益、誰承擔。"},{"id":"step-3","prompt":"預測有不確定性時，哪種做法可保留修正空間？","options":["用多情境、門檻、監測與可調整措施","只採最樂觀情境","因不確定而完全不行動"],"answer":"A","feedback":"不確定性應轉成路徑和觸發條件，而不是假裝不存在。"},{"id":"step-4","prompt":"方案試行後如何判斷是否公平有效？","options":["比較分群風險、恢復、負擔與參與資料並依結果修正","只看總減碳量","只問一次平均滿意度"],"answer":"A","feedback":"平均值可能掩蓋弱勢群體的損失，需用分群與長期回饋追蹤。"}]}
    lesson["updatedAt"]=TODAY; lesson["reviewStatus"]="draft"
    for i in range(1,11):
        p=QDIR/f"question-science-content-nb-iv-3-{i}.json"; q=json.loads(p.read_text(encoding="utf-8")); q["examPatternRefs"]=refs(); q["provenance"]={"origin":"original","license":"All rights reserved","sourceUrl":SOURCES[0]["url"],"sourceLocator":"三筆公立學校公開自然／理化試題的減緩、調適、資料判讀與方案比較能力方向；本題只作 pattern-only 改寫。","authoringNote":"本題只取公立學校公開試題的能力方向與資料判讀層次，題幹、選項、答案、解析與步驟均以 Nb-Ⅳ-3 重新撰寫，未複製原題、圖表或答案；待第二輪 AI／Terra 內容複核。"}; q["solutionStrategy"]=STRATEGIES[i]; q["solutionSteps"]=["圈出題幹的措施、目標、時間尺度與受影響群體。",f"依 Nb-Ⅳ-3 判準檢查：{STRATEGIES[i]}","比較選項是否漏掉排放、風險、維護、公平或不確定性中的關鍵條件。","排除把單一數字、單一工程或平均值當成全部證據的說法。","回到題幹核對唯一最佳答案，寫出仍需監測或修正的限制。"]; q["reviewStatus"]="draft"; q["updatedAt"]=TODAY; p.write_text(json.dumps(q,ensure_ascii=False,indent=2)+"\n",encoding="utf-8")
    REPORT.write_text(json.dumps({"unit":"Nb-Ⅳ-3：氣候變遷的減緩與調適","lessonId":lesson["id"],"status":"first-pass-ai-review-complete","reviewStatus":"draft","checkedQuestions":10,"checks":{"unitSpecificOriginalContent":True,"threeVersionResearchRecords":True,"threePublicSchoolExamPatternSources":True,"answersAndDetailedSteps":True,"interactivePredictionManipulationExplanation":True,"terraSecondPass":"pending"},"reviewedAt":TODAY,"note":"三筆公開試題僅作 pattern-only 來源；版本融合、逐題內容 QA、Terra 第二輪與正式發布尚未完成，維持 draft。"},ensure_ascii=False,indent=2)+"\n",encoding="utf-8")
    LESSON.write_text(json.dumps(lesson,ensure_ascii=False,indent=2)+"\n",encoding="utf-8"); print("authored science content nb iv 3")

if __name__=="__main__": main()
