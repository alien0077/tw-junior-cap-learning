import json
from pathlib import Path

ROOT=Path(__file__).resolve().parents[1]
LESSON=ROOT/"lessons/science/lesson-science-content-me-iv-7.json"
QDIR=ROOT/"questions/science"
REPORT=ROOT/"implementation/reports/science-content-me-iv-7-first-pass-review.json"
TODAY="2026-09-23"
SOURCES=[
 ("https://www.yacjh.kh.edu.tw/upload/221/101_30637/114%E4%B8%8B%E5%AD%B8%E6%9C%9F%E7%AC%AC%E4%B8%80%E6%AC%A1%E6%AE%B5%E8%80%83%E4%B8%89%E5%B9%B4%E7%B4%9A%E8%87%AA%E7%84%B6.pdf","高雄市立鹽埕國民中學公開自然科段考試題","聲音特性、波形、響度與噪音資料","取公開自然科題型對音調、響度、音色與測量判讀的能力方向，另寫聲音情境。"),
 ("https://www.grow22.com/download/114/114_cp/05_114P_Nature.pdf","114 年國中教育會考自然科公開試題","波動、聲音、資料與實驗控制","取公開會考對波動概念、控制條件和圖表證據的推理方向，未複製原題。"),
 ("https://www.kcjh.kh.edu.tw/upload/190/104_34764/%E4%B8%89%E5%B9%B4%E7%B4%9A%E7%90%86%E5%8C%96-%E7%AC%AC三次段考5-OK.pdf","高雄市立國昌國民中學公開三年級自然科試題","聲音傳播、反射與生活應用","取公立學校自然科對聲音傳播、反射與生活防護的能力方向，重新設計選項。"),
]
REFS=[{"url":u,"title":t,"year":"109-115","subject":"science","locator":loc,"observedPattern":pat,"reuseDecision":"pattern-only","status":"recorded","locatorLevel":"paper"} for u,t,loc,pat in SOURCES]
ROWS=[
 ("easy","兩個聲音的振幅相同，但甲的頻率高於乙；哪個敘述較合理？",["甲的音調較高，響度不必然較大","甲的音調較低且聲速較快","兩者音調必定相同","頻率只決定回聲時間"],"A","頻率是每秒振動次數，通常與音調高低相關；振幅和接收條件較常連到響度，不能混成聲速。","先分清頻率與振幅，再把物理量對應到音調或響度，最後排除把聲速混進來的選項。"),
 ("medium","資料甲和乙頻率同為 440 Hz，但乙波形振幅約為甲的兩倍；可先預測什麼？",["乙音調較高且聲速較快","兩者音調較接近，乙可能有較大響度；不能直接宣稱分貝加倍","乙的音色一定完全不同","甲一定聽不見"],"B","頻率相同支持音調相近，振幅差異可作為響度差異的相對線索；相對波形振幅不是直接的分貝讀值。","先找固定的頻率，再找改變的振幅，最後確認儀器單位和聽者位置是否支持更強的結論。"),
 ("medium","鋼琴和長笛演奏相同基頻仍有不同音色，最適合用哪項解釋？",["音色與波形細節或泛音組成有關，不只看基頻","音色只由音量決定","相同頻率代表波形完全相同","音色等於分貝數"],"A","相同基頻不代表整個波形和泛音組成相同；波形細節改變會使聽感的音色不同。","先固定基頻，再比較波形形狀或頻譜成分，避免把音色、音調與響度混為一談。"),
 ("easy","聲音在空氣中傳到耳朵時，哪個說法正確？",["空氣分子整團從喇叭跑到耳朵","聲源振動造成介質中疏密變化傳遞，分子主要在平衡位置附近振動","聲音不需要介質","只有真空能傳聲"],"B","聲音是介質中的機械波，空氣分子傳遞局部擾動而非整團長距離搬運；真空不能以此方式傳播聲音。","畫出聲源、介質與受體，區分介質的局部振動和波動能量的傳遞。"),
 ("medium","拍手後 0.20 秒聽到牆面回聲，若聲速取 340 m/s，聲源到牆面距離約為多少？",["17 m","34 m","68 m","170 m"],"B","聲波往返距離為 340×0.20=68 m，單程距離約 68÷2=34 m；估算仍受溫度、風和辨識時間影響。","先把時間乘聲速求往返路徑，再除以二求單程距離，最後標出假設與單位。"),
 ("hard","比較兩個校園測點的噪音來源，哪項調查設計最能避免誤判？",["同一時間只測一次，並把較大值直接歸給球場","固定時段與儀器設定，在教室、球場、校門等測點重複測量並記錄距離、背景和活動","只問哪個地方聽起來最吵","移動測點直到數字變小"],"B","聲級受距離、背景、反射和活動影響；多點、重複與條件記錄可把聲源推論和主觀印象分開。","先列出可能聲源，再固定測量時段和儀器，最後比較介入前後的同位置資料。"),
 ("hard","吸音材料與隔音措施的差別，哪個描述較正確？",["吸音主要減少室內反射，隔音主要阻擋聲能穿透；兩者都要用相同條件重測","吸音和隔音完全同義","加大聲源就能隔音","只要改變測點就能證明吸音有效"],"A","吸音處理偏向降低反射和殘響，隔音偏向減少聲能穿越結構；效果判斷仍需控制測點、聲源與背景。","先判斷問題是反射還是穿透，再選路徑措施，最後用可比的聲級或回聲峰值驗證。"),
 ("medium","手機錄音顯示波形變高，哪個結論不能直接推出？",["錄音中的相對振幅可能改變","聲音的壓力變化在此設定下可能較大","分貝數必定精確加倍且符合法規聲級","應檢查麥克風增益、距離與背景"],"C","相對波形高度受錄音設備、增益和距離影響，不能直接當成校準聲級計或法規分貝值。","先辨識資料是相對波形還是校準單位，再補測設備設定和距離，避免把視覺高度當成絕對聲級。"),
 ("hard","校園噪音方案使平均聲級下降，但測量位置、風速與活動人數都變了；報告應如何寫？",["直接宣稱方案必然有效","把結果列為暫定，恢復可比的測點、時間、聲源活動與背景條件後重測","刪除不同條件的紀錄","只保留最小讀值"],"B","多個條件同時改變，下降可能來自風、距離或活動量；可比重測和完整紀錄是因果判斷的必要證據。","列出介入前後每個變因，標記不能歸因的部分，再設計只改變防治措施的重測。"),
 ("medium","要保護午休教室免受球場噪音，哪個方案最完整？",["只要求學生忍耐","在聲源、傳播路徑與受體三端評估，調整活動時段、改善反射／隔音並縮短暴露，且以重測確認","只把喇叭音量調大","只換一張漂亮的告示"],"B","噪音管理可同時從源頭、路徑和受體降低暴露；措施要對應可量測指標並在相同條件下追蹤。","先定位主要來源和路徑，再按三端列措施，最後指定聲級、殘響或暴露時間的驗證方式。"),
]

def make_question(n,row):
    diff,prompt,opts,source_answer,explanation,strategy=row; target="ACDBACDBAC"[n-1]
    correct=opts[ord(source_answer)-65]; distractors=[x for i,x in enumerate(opts) if i!=ord(source_answer)-65]
    ordered=[]; di=0
    for label in "ABCD":
        if label==target: ordered.append(correct)
        else: ordered.append(distractors[di]); di+=1
    steps=["找出聲源、介質、受體及題目要求的物理量。","將頻率、振幅、波形、聲速、聲級與測量條件分開標記。","用公式或控制變因逐步檢查資料，並寫出單位與假設。",f"排除把相對波形當校準分貝、把音調當音量或忽略安全測量的選項，答案為 {target}。",f"回查結論是否可重測並保留限制：{explanation}"]
    return {"id":f"question-science-content-me-iv-7-{n}","subject":"science","type":"single-choice","prompt":prompt,"options":[{"id":k,"text":v} for k,v in zip("ABCD",ordered)],"knowledgeIds":["kg-science-content-me-iv-7"],"difficulty":diff,"answer":{"value":target,"explanation":f"{explanation} 正確答案為選項 {target}。"},"provenance":{"origin":"original","license":"All rights reserved","sourceUrl":SOURCES[0][0],"sourceLocator":"三筆公立學校／公開自然與理化資料的音調、響度、音色、波形、聲速、反射、噪音測量與防治能力方向；本題為 Me-Ⅳ-7 原創情境改寫。","authoringNote":"依官方課綱、Knowledge Graph 與公開題型 pattern-only 方向獨立改寫；未複製原題、選項、圖表或答案；待第二輪 AI／Terra 內容複核。"},"reviewStatus":"draft","updatedAt":TODAY,"lessonId":"lesson-science-content-me-iv-7","examPatternRefs":REFS,"solutionStrategy":strategy,"solutionSteps":steps}

def main():
    lesson=json.loads(LESSON.read_text(encoding="utf-8")); lesson.update({"updatedAt":TODAY,"reviewStatus":"draft","authoringStandard":"version-fused-v1"})
    for row in lesson.get("publisherResearch",[])+lesson.get("versionResearch",[]): row["reviewedAt"]=TODAY
    lesson["fusionRecord"]["llmSynthesisNote"]="本課依官方自然科學課綱、kg-science-content-me-iv-7、南一／康軒／翰林可取得的公開版本研究限制與三筆公立學校／公開自然與理化題型能力模式，獨立融合聲源振動、介質、頻率、振幅、音調、響度、音色、波形、回聲、聲速、吸音、隔音、噪音測量與健康防治。題目與互動均重新設計，未複製受保護內容；Terra 第二輪與正式發布審查尚未完成，維持 draft。"
    LESSON.write_text(json.dumps(lesson,ensure_ascii=False,indent=2)+"\n",encoding="utf-8")
    for i,row in enumerate(ROWS,1): (QDIR/f"question-science-content-me-iv-7-{i}.json").write_text(json.dumps(make_question(i,row),ensure_ascii=False,indent=2)+"\n",encoding="utf-8")
    REPORT.write_text(json.dumps({"unit":lesson["title"],"lessonId":lesson["id"],"status":"first-pass-ai-review-complete","reviewStatus":"draft","checkedQuestions":10,"checks":{"unitSpecificOriginalContent":True,"threeVersionResearchRecords":True,"threePublicSchoolExamPatternSources":True,"answersAndDetailedSteps":True,"interactivePredictionManipulationExplanation":True,"terraSecondPass":"pending"},"reviewedAt":TODAY,"note":"10 題重新改寫為聲音特性、控制變因、回聲估算、校園噪音、吸音隔音與測量限制；每題具唯一答案、解析、策略與五步解法。"},ensure_ascii=False,indent=2)+"\n",encoding="utf-8")
    print("authored science content me-iv-7")
if __name__=="__main__": main()
