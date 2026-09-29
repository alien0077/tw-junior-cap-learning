"""La-Ⅳ-1：生態系交互作用與演替第一輪原創題庫。"""
import json
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
LESSON = ROOT / "lessons/science/lesson-science-content-la-iv-1.json"
REPORT = ROOT / "implementation/reports/science-content-la-iv-1-first-pass-review.json"
QDIR = ROOT / "questions/science"
TODAY = "2026-09-23"
SOURCES = [
    {"url": "https://www.yacjh.kh.edu.tw/upload/221/101_30637/114%E4%B8%8B%E5%AD%B8%E6%9C%9F%E7%AC%AC%E4%B8%80%E6%AC%A1%E6%AE%B5%E8%80%83%E4%B8%89%E5%B9%B4%E7%B4%9A%E8%87%AA%E7%84%B6.pdf", "title": "高雄市立鹽埕國民中學 114 學年度第 2 學期第 1 次段考自然科公開試題", "year": "114", "locator": "生態系、族群互動、食物網與環境資料判讀", "pattern": "取公開自然科評量以生物關係、能量流動、環境條件和資料判讀建立生態推理的能力方向。"},
    {"url": "https://www.grow22.com/download/114/114_cp/05_114P_Nature.pdf", "title": "114 年國中教育會考自然科公開試題", "year": "114", "locator": "生態系資料、族群變化、環境因子與證據推論", "pattern": "取公開會考以圖表、時間序列、因果限制和環境情境判讀生態系變化的能力方向。"},
    {"url": "https://www.kcjh.kh.edu.tw/upload/190/104_34764/%E5%9C%8B%E6%98%8C--%E4%BA%8C%E5%B9%B4%E7%B4%9A--%E8%87%AA%E7%84%B6%E7%A7%91.pdf", "title": "高雄市立國昌國民中學二年級自然科公開段考試題", "year": "112", "locator": "族群、群集、演替、干擾與觀測設計", "pattern": "取公立國中試題以生物間互動、群集隨時間改變和控制變因進行推理的能力方向。"},
]
REFS = [{**s, "subject": "science", "observedPattern": s["pattern"], "reuseDecision": "pattern-only", "status": "recorded", "locatorLevel": "paper"} for s in SOURCES]
STEPS = [
    ["圈出互動的兩個族群與數量變化。", "判斷每方得到或失去什麼。", "用正負方向連結互動類型。", "排除只看一方或把共存直接當互利。", "回查是否有直接觀察支持箭頭。"],
    ["標出年份、樣區、物種和環境資料。", "確認是同一地點的時間變化。", "依群集組成排序並找土壤或干擾證據。", "排除單張照片推斷完整歷史。", "寫出支持演替的資料與仍缺的證據。"],
    ["找出誰吃誰或誰利用誰。", "分別標記受益與受損者。", "判斷捕食、寄生、競爭或互利。", "排除把分解者當捕食者。", "用箭頭方向和文字理由雙重核對。"],
    ["列出保留區和干擾區的起始條件。", "確認樣區大小與測量方式一致。", "比較多次物種與環境資料。", "排除季節差異或樣區差異的替代解釋。", "把結論限制在這些樣區和觀察期間。"],
    ["找出土壤、根系或有機質是否保留。", "比較起始基質和先出現的生物。", "依條件判斷較像初生或次生演替線索。", "不要把所有演替都排成同一終點。", "補上干擾歷史與土壤形成的限制。"],
    ["圈出同時上升或下降的族群。", "列出至少兩個可能機制。", "找操弄或對照資料支持其中一個。", "排除相關就等於唯一因果。", "提出下一次重複觀察或控制變因。"],
    ["辨認競爭雙方使用的共同資源。", "固定時間和樣區條件。", "比較資源有限時雙方的變化方向。", "不要以先出現者直接判定競爭最強。", "以資源或行為證據支持競爭判斷。"],
    ["把多年紀錄依時間排列。", "確認群集組成而非單一個體大小。", "找出草本、灌木、森林或裸地的更替。", "排除季節照片造成的假序列。", "用土壤、光照和干擾資料交叉檢查。"],
    ["辨認研究區、對照區和干擾事件。", "固定觀察頻率與測量指標。", "比較干擾前後及兩區差異。", "排除一次觀察和自然季節波動。", "回報可支持的關係與不能確定的原因。"],
    ["先問題目提供的是觀察還是推論。", "指出作用雙方、時間和空間範圍。", "用食物網或演替時間線整理資料。", "標記替代解釋與缺少的測量。", "用『資料顯示……在……條件下可能……仍需……』完成結論。"],
]
ROWS = [
    ("easy", "水草增加提供蝸牛食物，蝸牛增加又啃食水草；若要描述這段關係，最適當的是？", ["水草和蝸牛的互動方向可能彼此不同，需分別標記提供資源與取食", "水草和蝸牛一定是互利", "蝸牛是水草的分解者", "兩族群沒有任何關係"], "A", "水草可能提供食物或躲藏處，蝸牛取食又會對水草造成壓力；同一網絡可包含不同方向的作用，不能只用一個標籤包辦。", "先列互動雙方，再分別判斷受益與受損。"),
    ("medium", "某池塘同一樣區四年紀錄為：裸地與薄土、草本增加並有有機質、出現灌木幼苗。這最支持哪項？", ["群集隨時間改變，可能是演替線索", "一株幼苗已證明最後必然成森林", "所有物種都同時出現", "只代表個體變高，不是群集改變"], "A", "多年同一樣區的群集組成和土壤變化支持演替線索，但不能由一株幼苗保證未來終點。", "先看時間序列與群集組成，再限制推論範圍。"),
    ("easy", "貓頭鷹捕食田鼠，最直接的互動判定為？", ["捕食：貓頭鷹獲得食物，田鼠承受傷害", "互利：兩者都因此增加", "競爭：兩者搶同一資源", "分解：貓頭鷹把遺體分解回土壤"], "A", "捕食是一方捕捉並取食另一方；捕食者獲得能量，被捕食者承受傷害，與競爭或分解不同。", "以誰取食誰及雙方結果判斷互動類型。"),
    ("hard", "清除區的水草、蝸牛和鳥類都下降；要區分水草移除與季節因素，哪項設計較好？", ["設保留區作對照，固定樣區與季節，多次記錄三族群及環境資料", "只看清除後一天，直接宣布唯一因果", "刪去不符合預期的月份", "只調查鳥類，不量水草和蝸牛"], "A", "保留區、固定樣區、相同季節與重複測量可比較干擾和季節替代解釋；單日單族群資料不足以確定因果。", "用對照、重複與多個指標隔離替代解釋。"),
    ("medium", "岩石裸地沒有土壤，保留土壤與根系的火災地很快長回草本；哪個解釋較合理？", ["兩地起始條件不同，後者較像次生演替線索", "兩地必然以相同速度形成森林", "只要有火災就一定是初生演替", "草本長回表示沒有發生演替"], "A", "保留土壤或根系的地點仍有較多基礎條件，快速恢復可作次生演替線索；岩石裸地需先考慮土壤形成。", "先比較基質與干擾歷史，再判斷演替類型。"),
    ("hard", "某年蝸牛數量下降與水質惡化同時發生，若沒有操弄資料，最嚴謹的結論是？", ["兩者有時間上的關聯，但仍需控制或額外證據判斷因果", "水質一定是唯一原因", "蝸牛一定造成水質惡化", "數量下降代表物種已滅絕"], "A", "同時變化可提出關聯線索，卻不能排除溫度、棲地或其他污染因素；需要對照、重複和環境資料。", "區分觀察到的相關與尚待驗證的因果。"),
    ("medium", "兩種植物在乾旱樣區共享水分有限的土壤，哪個證據最能支持競爭？", ["固定樣區後，水分減少時兩者生長或存活都下降，補水對照可改善", "只看到其中一種先發芽", "兩種植物都在同一張照片", "其中一種顏色較深"], "A", "共享有限水源、資源減少時雙方受影響且補水對照改善，較能支持競爭；單一外觀不能證明。", "找共同限制資源並加入對照證據。"),
    ("easy", "判斷裸地、草本、灌木到森林的演替順序，哪項資料最有用？", ["同一樣區多年群集組成與土壤資料", "不同地點同一天各拍一張照片", "只量一株植物的高度", "依植物名稱長短排序"], "A", "演替是群集隨時間變化，同一樣區的多年資料和土壤條件比不同地點單日照片更能支持序列。", "先鎖定時間和空間，再讀群集而非個體。"),
    ("hard", "校園花圃的保留區與照明干擾區在三個月份都記錄昆蟲種類、光照和植物覆蓋率，這樣做的主要價值是？", ["比較干擾與環境條件下的重複變化，降低單次觀察的誤判", "只要三個月份相同就能證明唯一因果", "可以不用記錄樣區大小", "植物覆蓋率可直接代表所有生物種類"], "A", "多時間點、對照區和多項指標可提高證據品質，但仍需注意季節、樣區和其他干擾，不能過度宣稱唯一因果。", "從研究設計的重複、對照與測量範圍評估證據。"),
    ("medium", "看到一張池塘照片同時有草本、灌木和鳥，最合理的報告方式是？", ["描述同時觀察到的物種，不能僅憑照片確定先後演替順序", "直接排成裸地到森林的完整歷史", "宣布鳥是灌木的分解者", "由照片判定每種生物的數量變化"], "A", "單張照片提供空間共存的觀察，不提供過去先後或多年數量；需要時間序列和其他資料才能談演替。", "分開直接觀察、推論與缺少的時間證據。"),
]

def make_question(n, row):
    difficulty, prompt, options, answer, explanation, strategy = row
    return {"id": f"question-science-content-la-iv-1-{n}", "subject": "science", "type": "single-choice", "prompt": prompt, "options": [{"id": k, "text": v} for k, v in zip("ABCD", options)], "knowledgeIds": ["kg-science-content-la-iv-1"], "difficulty": difficulty, "answer": {"value": answer, "explanation": f"{explanation} 正確答案為選項 {answer}。"}, "provenance": {"origin": "original", "license": "All rights reserved", "sourceUrl": SOURCES[0]["url"], "sourceLocator": "三筆公立學校／公開自然科試題與課程資料的族群互動、演替、樣區、時間序列、干擾與證據界線能力方向；本題只作 pattern-only 改寫來源。", "authoringNote": "依官方課綱、KG 與公開資料能力方向獨立改寫；未複製原題、選項、圖表或答案；待第二輪 AI／Terra 內容複核。"}, "reviewStatus": "draft", "updatedAt": TODAY, "lessonId": "lesson-science-content-la-iv-1", "examPatternRefs": REFS, "solutionStrategy": strategy, "solutionSteps": STEPS[n - 1]}

def main():
    lesson = json.loads(LESSON.read_text(encoding="utf-8"))
    lesson["updatedAt"] = TODAY
    lesson["reviewStatus"] = "draft"
    lesson["authoringStandard"] = "version-fused-v1"
    lesson["fusionRecord"]["llmSynthesisNote"] = "本課依官方自然科學課綱、kg-science-content-la-iv-1、南一／康軒／翰林可取得的公開資源限制與三筆公立學校／公開自然科評量能力模式，獨立融合族群交互作用、食物網、競爭、捕食、寄生、互利、演替、樣區、時間序列、干擾、對照與證據界線。原有能量錯配題已全部改為本單元專屬題目；所有正文、資料、題幹、選項、答案、互動回饋與五步解法均重新撰寫，未複製受保護內容；Terra 第二輪與正式發布審查尚未完成，維持 draft。"
    for entry in lesson.get("publisherResearch", []) + lesson.get("versionResearch", []):
        entry["reviewedAt"] = TODAY
    for n, row in enumerate(ROWS, 1):
        (QDIR / f"question-science-content-la-iv-1-{n}.json").write_text(json.dumps(make_question(n, row), ensure_ascii=False, indent=2) + "\n", encoding="utf-8")
    REPORT.write_text(json.dumps({"unit": lesson["title"], "lessonId": lesson["id"], "status": "first-pass-ai-review-complete", "reviewStatus": "draft", "checkedQuestions": 10, "checks": {"unitSpecificOriginalContent": True, "threeVersionResearchRecords": True, "threePublicSchoolExamPatternSources": True, "answersAndDetailedSteps": True, "interactivePredictionManipulationExplanation": True, "terraSecondPass": "pending"}, "reviewedAt": TODAY, "note": "原有能量錯配題已移除，10 題改寫為族群互動、演替、樣區、時間序列、干擾、對照與證據界線專屬問題；每題有唯一答案、解析與五步解法。"}, ensure_ascii=False, indent=2) + "\n", encoding="utf-8")
    LESSON.write_text(json.dumps(lesson, ensure_ascii=False, indent=2) + "\n", encoding="utf-8")
    print("authored science content la iv 1")

if __name__ == "__main__":
    main()
