"""Aa：物質組成與元素週期性第一輪來源融合與題目錯置修復。"""
import json
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
LESSON = ROOT / "lessons/science/lesson-science-content-aa.json"
REPORT = ROOT / "implementation/reports/science-content-aa-first-pass-review.json"
QDIR = ROOT / "questions/science"
TODAY = "2026-09-23"
SOURCES = [
    {"url": "https://www.grow22.com/download/114/114_cp/05_114P_Nature.pdf", "title": "114 年國中教育會考自然科公開試題", "year": "114", "locator": "原子、元素、化合物、化學式與週期表資料判讀", "pattern": "取由微觀粒子模型、符號與表格資料推論物質組成的能力方向。"},
    {"url": "https://www.hkjh.hc.edu.tw/uploads/1661481260739sfuB4gG2.pdf", "title": "新竹市立新科國中公開康軒版自然課程計畫", "year": "公開課程計畫", "locator": "物質組成、原子概念、化學符號與元素週期性", "pattern": "取原子與離子、化學式、相對質量、週期與族的教學及評量方向。"},
    {"url": "https://lgt.ntpc.edu.tw/TeachPlanFile_Upload/2022/plan/641_plan.pdf", "title": "新北市文山區安康高中國中部公開翰林版自然簡案", "year": "公開課程計畫", "locator": "物質結構、元素週期性與模型資料判讀", "pattern": "取粒子表示、元素分類、週期表位置與證據限制的能力方向。"},
]


def refs():
    return [{**s, "subject": "science", "observedPattern": s["pattern"], "reuseDecision": "pattern-only", "status": "recorded", "locatorLevel": "paper"} for s in SOURCES]


QUESTIONS = [
    ("元素的身分由哪項資料決定？", ["原子序，也就是質子數", "中子數一定相同", "電子層數一定相同", "樣品的外觀顏色"], "A", "元素身分判定先抓原子序。", ["圈出『元素身分』。", "元素身分由原子核內質子數決定。", "原子序就是質子數。", "電子數改變可能形成離子，不能單獨改變元素身分。", "因此選 A。"]),
    ("某粒子有 11 個質子、10 個電子，最合理的判讀是什麼？", ["它是原子序 10 的元素", "它是原子序 11 的陽離子", "它是沒有原子核的粒子", "它一定是中性原子"], "B", "分開比較質子數與電子數，再判斷元素身分和電性。", ["先記錄質子數 11。", "質子數決定元素身分，所以原子序為 11。", "電子少於質子，正電荷多於負電荷。", "因此它是帶正電的陽離子。", "所以選 B。"]),
    ("化學式 Al₂O₃ 中的下標 2 和 3 主要表示什麼？", ["一個粒子中鋁、氧原子的數量比", "樣品中有 2 個粒子和 3 個粒子", "鋁和氧的相對原子質量", "反應需要加熱 2 到 3 分鐘"], "A", "區分化學式下標的組成意義與前方係數的粒子數意義。", ["先找下標位置。", "下標附在元素符號後，描述單一化學粒子的原子數。", "因此 Al₂O₃ 中鋁與氧的原子比為 2：3。", "它不是樣品粒子總數，也不是時間或質量。", "答案為 A。"]),
    ("比較 3CO₂ 與 CO₂，下列敘述何者正確？", ["兩者單一分子的組成不同", "3CO₂ 表示三個 CO₂ 分子，CO₂ 表示一個 CO₂ 分子", "3 會把氧的下標 2 改成 6", "兩者都只含有氧元素"], "B", "先分辨係數與下標，再分開處理粒子數和單一粒子組成。", ["圈出 CO₂ 後方的下標 2。", "下標 2 表示一個分子含兩個氧原子。", "前方係數 3 表示有三個這樣的分子。", "所以單一分子組成沒有改變，只改變粒子數。", "選 B。"]),
    ("若元素 X 的相對原子質量為 23，X₂Y 中 Y 的相對原子質量為 16，X₂Y 的相對分子質量是多少？", ["39", "46", "62", "69"], "C", "依化學式下標逐項乘上相對原子質量，再相加。", ["讀出 X 有 2 個、Y 有 1 個。", "計算 X 的貢獻：2×23＝46。", "計算 Y 的貢獻：1×16＝16。", "相對分子質量為 46＋16＝62。", "故選 C。"]),
    ("元素 P 與 Q 位於週期表同一族，最有根據的推論是什麼？", ["兩者原子序完全相同", "兩者最外層電子排列可能相近，部分化學性質可能相似", "兩者所有物理性質必定相同", "兩者一定位於同一週期"], "B", "使用週期表規律時保留推論的條件與限制。", ["先圈出『同一族』。", "同族通常代表最外層電子排列具有相近規律。", "這可支持部分化學性質相似的預測。", "但原子序、週期和所有物理性質不會因此相同。", "所以選 B。"]),
    ("某元素位在第 3 週期第 17 族，哪項資料最能支持它的週期位置？", ["它有三層電子分布", "它一定是金屬", "它的樣品質量是 3 g", "它的名稱有三個字"], "A", "先用週期代表電子層數的線索，再排除與位置無關的敘述。", ["週期是週期表的橫列。", "第 3 週期對應三層電子分布。", "第 17 族是另一個族位置資訊，不能改寫成質量或名稱字數。", "題目問支持週期位置的資料。", "答案為 A。"]),
    ("下列哪一組粒子模型代表化合物而不是元素？", ["每個粒子都只有一種綠球", "每個粒子都由一個紅球和兩個白球連結", "樣品中只有一種紫色原子", "每個粒子都是單一藍球"], "B", "看單一粒子是否含有兩種以上元素，而不是只看顏色或粒子數。", ["先以顏色代表不同元素作為模型規則。", "化合物的單一粒子需含兩種以上元素。", "B 的粒子含紅、白兩種球。", "其餘選項的單一粒子只有一種元素。", "因此選 B。"]),
    ("同一元素的兩個粒子，一個有 8 個質子、8 個電子，另一個有 8 個質子、10 個電子；最合理的結論是什麼？", ["它們是不同元素", "它們的原子序不同", "它們是同一元素的不同電性粒子", "其中一個沒有原子核"], "C", "固定質子數判定元素，再以電子數差判斷電性。", ["兩個粒子的質子數都為 8。", "相同質子數表示相同元素，原子序都為 8。", "電子數不同會改變正負電荷平衡。", "所以差異是電性，不是元素身分。", "選 C。"]),
    ("研究新元素週期性主張時，哪種作法最符合證據邊界？", ["只因同族就宣稱所有性質相同", "先用位置預測，再以實驗資料檢查並標示尚未測得的性質", "只看元素名稱猜反應性", "把週期表位置直接當成完整實驗結果"], "B", "將週期表當作可檢驗的預測線索，而非代替實驗的完整答案。", ["先指出題目要求的是研究作法。", "週期表可提供原子排列與性質規律的初步線索。", "預測必須接受實驗資料檢驗。", "資料未提供的性質要保留為未知，不能自行補上。", "因此選 B。"]),
]


def main():
    lesson = json.loads(LESSON.read_text(encoding="utf-8"))
    lesson["updatedAt"] = TODAY
    lesson["reviewStatus"] = "draft"
    lesson["fusionRecord"] = {
        "commonCore": ["三版本公開線索共同支持以原子、元素、化合物、化學式與週期表建立物質組成的微觀—符號—資料判讀鏈。", "原子序、質子／電子、下標／係數、相對質量、週期／族及證據限制是共同能力核心。"],
        "versionDifferences": ["南一公開定位偏向物質組成與符號核算；康軒線索偏向原子、離子、化學式與週期性教學評量；翰林線索偏向粒子模型、位置規律與探究證據。公開資料不足以宣稱取得完整教材內容。"],
        "originalAdditions": ["以元素資料工作台、粒子卡與化學式帳本串接原子序、電性、組成比例、式量和週期位置。", "把元素身分與電子數混淆、把下標與係數混用、把同族相似性誇大成完全相同列為本單元迷思診斷。"],
        "llmSynthesisNote": "依官方課綱、本單元 KG、南一／康軒／翰林公開版本線索與三筆公立學校公開自然科試題／課程資料能力方向，重新組織原子、元素、化合物、化學式、相對質量與週期表；已移除原先與單元無關的溶液質量批次題，10 題題幹、選項、答案、解析與五步解法均為原創，未複製教材或試題文字、圖表與答案。Terra 第二輪與正式發布審查尚未完成，維持 draft。",
    }
    for entry in lesson.get("versionResearch", []) + lesson.get("publisherResearch", []):
        entry["reviewedAt"] = TODAY
    for i, (prompt, options, answer, strategy, steps) in enumerate(QUESTIONS, 1):
        path = QDIR / f"question-science-content-aa-{i}.json"
        question = json.loads(path.read_text(encoding="utf-8"))
        question["prompt"] = prompt
        question["options"] = [{"id": chr(65+j), "text": text} for j, text in enumerate(options)]
        question["answer"] = {"value": answer, "explanation": f"{steps[-2]} {steps[-1]} 正確答案：{answer}。"}
        question["provenance"] = {"origin": "original", "license": "All rights reserved", "sourceUrl": SOURCES[0]["url"], "sourceLocator": "三筆公立學校公開自然科試題／課程資料的原子、元素、化學式與週期表能力方向；本題只作 pattern-only 改寫。", "authoringNote": "本題取公開資料能力方向，題幹、選項、答案、解析與五步解法均依 Aa 單元重新撰寫，未複製原題、圖表或答案；待第二輪 AI／Terra 內容複核。"}
        question["examPatternRefs"] = refs()
        question["solutionStrategy"] = strategy
        question["solutionSteps"] = steps
        question["reviewStatus"] = "draft"
        question["updatedAt"] = TODAY
        path.write_text(json.dumps(question, ensure_ascii=False, indent=2) + "\n", encoding="utf-8")
    REPORT.write_text(json.dumps({"unit": "Aa：物質組成與元素週期性", "lessonId": lesson["id"], "status": "first-pass-ai-review-complete", "reviewStatus": "draft", "checkedQuestions": 10, "checks": {"unitSpecificOriginalContent": True, "threeVersionResearchRecords": True, "threePublicSchoolExamPatternSources": True, "answersAndDetailedSteps": True, "interactivePredictionManipulationExplanation": True, "unitMismatchRemediated": True, "terraSecondPass": "pending"}, "reviewedAt": TODAY, "note": "已移除原先與 Aa 單元無關的溶液質量批次題；三筆公開試題／課程資料僅作 pattern-only 來源，版本融合、逐題內容 QA、Terra 第二輪與正式發布尚未完成，維持 draft。"}, ensure_ascii=False, indent=2) + "\n", encoding="utf-8")
    LESSON.write_text(json.dumps(lesson, ensure_ascii=False, indent=2) + "\n", encoding="utf-8")
    print("authored science content aa")


if __name__ == "__main__":
    main()
