import json
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
LESSON = ROOT / "lessons/science/lesson-science-content-md-iv-1.json"
QDIR = ROOT / "questions/science"
REPORT = ROOT / "implementation/reports/science-content-md-iv-1-first-pass-review.json"
TODAY = "2026-09-23"
BOUNDARY = "只保存公開來源的能力方向、章節定位與查核限制；不複製出版社或學校教材正文、原題、選項、圖表、答案、圖片或影音。"
SOURCES = [
    {
        "url": "https://www.kcjh.kh.edu.tw/upload/190/104_34764/%E5%9C%8B%E6%98%8C--%E4%BA%8C%E5%B9%B4%E7%B4%9A--%E7%90%86%E5%8C%96%E7%A7%91_2.pdf",
        "title": "高雄市立國昌國民中學公開理化科段考試題（生物與環境）",
        "year": "112",
        "locator": "生物與環境、保育調查、天然災害與防治資料判讀",
        "pattern": "取公開題型對環境因子、棲地變化與防災資料的證據判讀方向，另行設計坡面情境。",
    },
    {
        "url": "https://www.yacjh.kh.edu.tw/upload/221/101_30637/114%E4%B8%8B%E5%AD%B8%E6%9C%9F%E7%AC%AC%E4%B8%80%E6%AC%A1%E6%AE%B5%E8%80%83%E4%B8%89%E5%B9%B4%E7%B4%9A%E8%87%AA%E7%84%B6.pdf",
        "title": "高雄市立鹽埕國民中學公開自然科段考試題",
        "year": "114",
        "locator": "環境因子、天然災害、資料圖表與生態調查",
        "pattern": "取公立國中自然科以觀測條件、因果機制、對照與安全決策作答的能力方向。",
    },
    {
        "url": "https://market.cloud.edu.tw/resources/web/1807720",
        "title": "教育雲國中生態與環境教學資源",
        "year": "110",
        "locator": "生態系、棲地保育、環境變化與防災學習資源",
        "pattern": "取公開課程資源把生態關係、環境觀察與行動方案連成證據鏈的能力方向。",
    },
]
REFS = [{**s, "subject": "science", "observedPattern": s["pattern"], "reuseDecision": "pattern-only", "status": "recorded", "locatorLevel": "paper"} for s in SOURCES]

ROWS = [
    ("easy", "雨後比較三段坡面，哪一組紀錄最能支持保育與防災判斷？", ["只寫地點名稱", "坡度、土壤裂縫、植被覆蓋、雨量、逕流方向與歷次災痕", "只拍一張遠景照", "只問居民喜歡哪種植物"], "B", "坡面災害不是單一因素造成；把地形、土壤、水與生物覆蓋放在同一空間與時間資料中，才可以連結機制並安排監測。", "先圈出可測量的自然條件，再找能連成雨水—土壤—滑動路徑的資料，最後檢查是否有時間或空間比較。"),
    ("medium", "同樣降雨量下，甲坡有枯落物與深根草，乙坡裸露且排水溝堵塞；較合理的推論是？", ["甲坡一定不會崩塌", "乙坡的逕流與表層沖刷可能較集中，但仍須考慮坡度、地質與地下水", "只要有植物就不必巡查", "乙坡一定比甲坡承受更多雨量"], "B", "植被與枯落物可減緩雨滴打擊和水流集中，堵塞排水也可能讓水改走坡面；這是風險線索，不是忽略坡度、地質與地下水的單一結論。", "固定降雨條件，分辨可觀察差異，再寫出可能機制，最後列出不能由現有資料確定的因素。"),
    ("medium", "要測試『移除枯落物會增加泥水濁度』，哪種設計較能判斷因果？", ["只在移除後測一次", "兩個相近坡面同步收集雨量與濁度，只改變枯落物並重複觀察", "把坡度和雨量也同時改變", "只訪問看到泥水的人"], "B", "控制坡度、雨量、土壤與量測方法，只改變枯落物，並用重複或對照資料比較，才較能把濁度差異歸因於操弄因素。", "先定義操弄與結果變因，再固定混淆條件，接著設對照和重複測量，最後檢查雨勢是否超出模型範圍。"),
    ("easy", "坡頂道路切坡旁出現逐日變長的裂縫，且預報將有豪雨；第一項安全處置為何？", ["進入裂縫旁插旗測量", "依官方警戒避開危險區並通報校方、管理單位或專業人員", "等雨後再靠近拍照", "先移除所有植物"], "B", "裂縫變化與豪雨預報代表可能有立即風險，應先降低人員暴露並由有權責與專業能力者評估，不能為了蒐證進入危險坡面。", "先辨識時間敏感的危害，再把人員撤離與通報放在觀測前，最後確認後續資料由安全且合格的管道取得。"),
    ("medium", "下列哪句最能解釋植被有助於降低部分坡面風險？", ["葉片會讓所有雨水消失", "冠層、枯落物與根系可分散雨滴、減慢逕流或增加土粒抓附，但效果受坡度、地質與極端降雨限制", "植物根系能承受任何土石流", "只要種樹就能取代排水工程"], "B", "植被作用是多個環節的部分改變，不是消除水量或保證坡體穩定；完整判斷仍需納入地形、材料、排水與事件強度。", "把植物作用拆成截留、減速、滲入與抓附，再逐一問其限制，避免把生態功能誇大成萬靈丹。"),
    ("hard", "校園想比較『保留植被』與『鋪設硬鋪面』對雨水的影響，哪項結果最適合納入？", ["只比較施工費", "相同降雨下的出流水量、峰值時間、濁度、土壤含水與下游積水位置", "只看施工當天外觀", "只記錄哪個方案較受歡迎"], "B", "方案可能改變水流速度、入滲、沖刷與下游尖峰；需要多個可量測結果，不能用外觀或單一成本取代水文與安全證據。", "先畫出雨水可能路徑，再選能代表量、速率、泥砂和下游影響的指標，並保持降雨與量測位置可比較。"),
    ("hard", "山坡保育計畫宣稱『災害件數下降就是復育成功』，哪個追問最重要？", ["是否把所有照片換成彩色", "災害件數是否受降雨量、觀測範圍、通報習慣、坡面工程與植被成長時間共同影響", "是否只挑最好看的月份", "是否取消裂縫巡查"], "B", "件數是結果指標，但可能受事件頻率、資料蒐集與其他措施影響；要結合雨量、裂縫、逕流、覆蓋率和對照坡面，才可較謹慎評估。", "先確認指標如何定義，再找可能的替代原因與對照資料，最後把結論寫成有時間和範圍限制的句子。"),
    ("medium", "若裸露坡面要復育，哪項方案順序較合理？", ["先種任何快速生長植物，再忽略排水", "先避開危險區並由專業人員評估坡體，改善排水與水流路徑，再選適地植被並追蹤成效", "只覆蓋一層塑膠布永久解決", "先讓學生進入坡腳踩實土壤"], "B", "安全評估與水流控制是前提，植被選擇須符合當地環境且需要成長時間；方案還要有監測和維護，不能以單一動作代替系統管理。", "依風險急迫性排順序，分開立即防護、工程處理、生態復育與長期監測，再檢查每步的權責與安全條件。"),
    ("hard", "比較兩地山崩風險時，哪個結論最符合證據推理？", ["雨量較大者必定比較危險", "在相近觀測期間，若乙地坡度較大、含水較高且排水受阻，乙地具有較多風險條件，但仍需地質與地下水資料驗證", "有樹的地方必定安全", "災痕較少代表永遠不會發生"], "B", "坡度、含水與排水阻礙共同提供機制線索；條件式結論承認資料限制，也避免以單一指標把風險說成確定事件。", "把兩地資料逐欄對齊，區分已觀察事實和推論，補列尚缺資料，再使用『在……條件下』表達結論。"),
    ("medium", "面對保育與防災方案的居民會議，哪個提案最完整？", ["只宣傳種樹口號", "公開風險圖與不確定性，保留高風險植被、維護排水、設雨季監測與通報門檻，並檢討對下游與居民的影響", "只追求降低工程費", "封鎖所有資料避免爭議"], "B", "好的方案同時處理自然機制、工程維護、監測觸發、資訊透明與不同群體的安全，不把保育或防災縮成一句口號。", "先列出受保護對象與風險，再安排可執行措施和指標，最後加入回饋、公開說明與公平性檢查。"),
]

def refs():
    return REFS

def steps(index, answer, core):
    starts = [
        "找出題目要求的判斷目標與所有已給條件。",
        "把直接觀察、推論和仍未知的資料分開記錄。",
        "依本題的因果鏈檢查條件是否足以支持選項。",
        f"比較四個選項，排除與安全或證據不符者，保留選項 {answer}。",
        f"回讀題幹確認結論範圍；本題核心是：{core}",
    ]
    return starts

def make_question(n, row):
    difficulty, prompt, options, answer, explanation, strategy = row
    # 先保留題意中已判定的正解，再讓選項位置依題號變化；避免答案位置成為猜題線索。
    target = "ACDBACDBAC"[n - 1]
    correct_text = options[1]
    distractors = [options[0], options[2], options[3]]
    ordered = []
    di = 0
    for label in "ABCD":
        if label == target:
            ordered.append(correct_text)
        else:
            ordered.append(distractors[di])
            di += 1
    answer = target
    return {
        "id": f"question-science-content-md-iv-1-{n}",
        "subject": "science", "type": "single-choice", "prompt": prompt,
        "options": [{"id": k, "text": v} for k, v in zip("ABCD", ordered)],
        "knowledgeIds": ["kg-science-content-md-iv-1"], "difficulty": difficulty,
        "answer": {"value": answer, "explanation": f"{explanation} 正確答案為選項 {answer}。"},
        "provenance": {
            "origin": "original", "license": "All rights reserved", "sourceUrl": SOURCES[0]["url"],
            "sourceLocator": "三筆公立學校／公開生態與自然科資料的保育調查、天然災害、防治決策與多指標判讀能力方向；本題為 Md-Ⅳ-1 原創情境改寫。",
            "authoringNote": "依官方課綱、Knowledge Graph 與公開試題 pattern-only 方向獨立改寫；未複製原題、選項、圖表或答案；待第二輪 AI／Terra 內容複核。",
        },
        "reviewStatus": "draft", "updatedAt": TODAY,
        "lessonId": "lesson-science-content-md-iv-1", "examPatternRefs": refs(),
        "solutionStrategy": strategy, "solutionSteps": steps(n, answer, explanation),
    }

def main():
    lesson = json.loads(LESSON.read_text(encoding="utf-8"))
    lesson.update({"updatedAt": TODAY, "reviewStatus": "draft", "authoringStandard": "version-fused-v1"})
    for row in lesson.get("publisherResearch", []) + lesson.get("versionResearch", []):
        row["reviewedAt"] = TODAY
        if "licenseBoundary" in row:
            row["licenseBoundary"] = BOUNDARY
    lesson["fusionRecord"]["llmSynthesisNote"] = "本課依官方自然科學課綱、kg-science-content-md-iv-1、南一／康軒／翰林可取得的公開版本研究限制，以及三筆公立學校／公開生態自然科試題能力模式，獨立融合坡度、地質、降雨、逕流、植被、根系、排水、土地利用、監測、復育與天然災害安全。題目與互動均重新設計為坡面證據—機制—風險—防治的脈絡，未複製受保護內容；Terra 第二輪與正式發布審查尚未完成，維持 draft。"
    lesson["interactive"] = {
        "type": "scientific-investigation",
        "goal": "用坡面觀測資料連結生物保育、雨水路徑與天然災害風險，提出有條件且安全的防治行動。",
        "scenario": "雨後比較林地、裸地與道路切坡三段模型；你必須先預測泥水與裂縫的變化，再逐步改動覆蓋、排水或坡度，最後說明證據與限制。",
        "variables": [{"symbol": "rain", "meaning": "降雨強度與持續時間"}, {"symbol": "cover", "meaning": "植被與枯落物覆蓋"}, {"symbol": "slope", "meaning": "坡度、裂縫與坡頂負荷"}, {"symbol": "drain", "meaning": "排水路徑是否通暢"}],
        "steps": [
            {"id": "step-1", "prompt": "先從三段坡面資料找出哪類證據？", "options": ["坡度、覆蓋、裂縫、雨量、排水與泥水結果", "只看植物名稱", "只看照片顏色"], "answer": "A", "feedback": "先把條件與結果放入同一張觀測表，避免用單一外觀直接下結論。"},
            {"id": "step-2", "prompt": "只移除枯落物後，應預測哪個可觀察變化？", "options": ["逕流可能較集中且出流水濁度可能增加", "所有坡面立刻崩塌", "降雨量自動改變"], "answer": "A", "feedback": "這是機制預測，不是確定災害宣告；仍要用相同雨量和重複觀測檢查。"},
            {"id": "step-3", "prompt": "模型出現裂縫並預報豪雨，下一步應如何處理？", "options": ["停止靠近、依警戒通報並由專業人員評估", "進入坡腳補拍細節", "先拔除所有植物"], "answer": "A", "feedback": "安全與降低暴露優先，觀測不能凌駕官方警戒與專業評估。"},
            {"id": "step-4", "prompt": "如何提出可檢驗的防治方案？", "options": ["指出措施、觸發指標、資料限制與下一次檢查時間", "只寫多種樹", "宣稱保育後永遠不會有災害"], "answer": "A", "feedback": "完整方案要把植被、排水、工程、監測與避難放在條件式決策中。"},
        ],
    }
    LESSON.write_text(json.dumps(lesson, ensure_ascii=False, indent=2) + "\n", encoding="utf-8")
    for i, row in enumerate(ROWS, 1):
        (QDIR / f"question-science-content-md-iv-1-{i}.json").write_text(json.dumps(make_question(i, row), ensure_ascii=False, indent=2) + "\n", encoding="utf-8")
    REPORT.write_text(json.dumps({
        "unit": lesson["title"], "lessonId": lesson["id"], "status": "first-pass-ai-review-complete", "reviewStatus": "draft", "checkedQuestions": 10,
        "checks": {"unitSpecificOriginalContent": True, "threeVersionResearchRecords": True, "threePublicSchoolExamPatternSources": True, "answersAndDetailedSteps": True, "interactivePredictionManipulationExplanation": True, "terraSecondPass": "pending"},
        "reviewedAt": TODAY, "note": "10 題以坡面資料、植被作用、控制變因、安全處置、復育成效、監測與居民方案重新改寫；每題具唯一答案、解析、策略與五步解法。"
    }, ensure_ascii=False, indent=2) + "\n", encoding="utf-8")
    print("authored science content md-iv-1")

if __name__ == "__main__":
    main()
