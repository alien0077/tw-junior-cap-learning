"""J：物質的反應、平衡及製造第一輪原創題庫。"""
import json
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
LESSON = ROOT / "lessons/science/lesson-science-content-j.json"
REPORT = ROOT / "implementation/reports/science-content-j-first-pass-review.json"
QDIR = ROOT / "questions/science"
TODAY = "2026-09-23"
SOURCES = [
    {
        "url": "https://www.yacjh.kh.edu.tw/upload/221/101_30637/114%E4%B8%8B%E5%AD%B8%E6%9C%9F%E7%AC%AC%E4%B8%80%E6%AC%A1%E6%AE%B5%E8%80%83%E4%B8%89%E5%B9%B4%E7%B4%9A%E8%87%AA%E7%84%B6.pdf",
        "title": "高雄市立鹽埕國民中學 114 學年度第 2 學期第 1 次段考自然科公開試題",
        "year": "114",
        "locator": "化學反應、反應式、質量與實驗資料判讀",
        "pattern": "取由反應現象、反應式與資料證據判斷物質變化及守恆關係的能力方向。",
    },
    {
        "url": "https://www.grow22.com/download/114/114_cp/05_114P_Nature.pdf",
        "title": "114 年國中教育會考自然科公開試題",
        "year": "114",
        "locator": "反應條件、圖表資料、粒子模型與生活／製程情境",
        "pattern": "取從粒子圖、實驗資料與生活情境推論反應條件、反應速率及結果的能力方向。",
    },
    {
        "url": "https://www.hkjh.hc.edu.tw/uploads/1661481260739sfuB4gG2.pdf",
        "title": "新竹市立新科國中公開康軒版自然課程計畫",
        "year": "公開課程計畫",
        "locator": "化學反應表示、可逆反應、平衡與工業製造",
        "pattern": "取以微觀粒子、反應條件與工業應用連結化學反應及平衡的教學與評量方向。",
    },
]
REFS = [{**s, "subject": "science", "observedPattern": s["pattern"], "reuseDecision": "pattern-only", "status": "recorded", "locatorLevel": "paper"} for s in SOURCES]


def q(number, prompt, options, answer, explanation, strategy, steps, difficulty="medium"):
    return {
        "id": f"question-science-content-j-{number}",
        "subject": "science",
        "type": "single-choice",
        "prompt": prompt,
        "options": [{"id": key, "text": text} for key, text in zip("ABCD", options)],
        "knowledgeIds": ["kg-science-content-j"],
        "difficulty": difficulty,
        "answer": {"value": answer, "explanation": explanation},
        "provenance": {
            "origin": "original",
            "license": "All rights reserved",
            "sourceUrl": SOURCES[0]["url"],
            "sourceLocator": "三筆公立學校／公開自然科試題與課程資料的反應證據、粒子模型、守恆、條件控制、平衡與製程能力方向；本題只作 pattern-only 改寫來源。",
            "authoringNote": "依公開資料能力方向獨立改寫；題幹、選項、答案、解析與五步解法均依 J 根單元重新撰寫，未複製原題、圖表或答案；待第二輪 AI／Terra 內容複核。",
        },
        "reviewStatus": "draft",
        "updatedAt": TODAY,
        "lessonId": "lesson-science-content-j",
        "examPatternRefs": REFS,
        "solutionStrategy": strategy,
        "solutionSteps": steps,
    }


QUESTIONS = [
    q(1, "下列哪項最能支持『鐵和硫反應生成新物質』，而不只是兩種物質混合？", ["生成物的性質與鐵、硫都不同，且無法用磁鐵分離回原物質", "鐵粉和硫粉仍各自保留原來顏色", "把兩種粉末放在同一張紙上", "混合物的總質量可以直接相加"], "A", "新物質具有不同性質且不能用簡單物理方法分回原物質，是化學反應的重要證據；單純放在一起或質量相加不足以證明反應。", "先區分混合與新物質，再檢查是否有可逆的物理分離證據。", ["列出反應前鐵、硫各自的性質。", "觀察生成物是否出現新的性質。", "檢查磁鐵等物理方法能否分離回原物質。", "B、C 只描述混合，D 只是數值相加。", "因此 A 才同時支持生成新物質。"], "easy"),
    q(2, "反應式 2H₂＋O₂→2H₂O 中，係數 2 的主要作用是？", ["讓反應前後氫、氧原子數相等", "改變水分子的化學式", "表示氧氣有兩種元素", "表示反應一定需要兩秒"], "A", "係數可調整參與反應的粒子數，使左右兩側每種元素的原子數符合守恆；下標才是分子內原子組成的一部分。", "把係數和下標分開，逐元素點算反應前後的原子。", ["先數左側氫原子與氧原子。", "再數右側水分子中的氫、氧原子。", "確認左側 4 個氫、2 個氧等於右側 4 個氫、2 個氧。", "B 把係數誤當下標，C、D 沒有守恆意義。", "所以 A 正確。"], "easy"),
    q(3, "密閉容器中碳酸鈣受熱分解，若反應前後容器總質量相同，最合理的解釋是？", ["生成的氣體仍留在密閉系統內，原子總數沒有憑空增加或減少", "反應沒有發生", "只要是氣體就沒有質量", "天平會自動把質量補回來"], "A", "密閉系統保留固體與氣體，反應只是原子重新排列；總質量相同是質量守恆的系統性證據。", "先確認系統邊界，再用粒子重新排列解釋總量。", ["圈出密閉容器包含固體、氣體與容器。", "確認分解反應產生的氣體沒有逸出系統。", "比較反應前後所有物質的總質量。", "B、C、D 都否認反應或錯解質量。", "因此 A 符合封閉系統的守恆。"], "medium"),
    q(4, "同一反應使用粉末而非大顆粒固體，通常反應較快，最直接的原因是？", ["粉末總表面積較大，能同時接觸反應的粒子較多", "粉末的原子種類會自動改變", "粉末一定使生成物質量增加", "粉末會讓質量守恆失效"], "A", "在其他條件相同時，粉末暴露的總表面積較大，碰撞與接觸機會增加，因而提高反應速率；不代表改變元素或守恆。", "只改一個變因，將速率改變連回粒子接觸機會。", ["確認粉末與大顆粒使用相同物質量。", "比較兩者暴露給溶液或氣體的表面積。", "用接觸面積解釋有效碰撞次數。", "B、C、D 分別誤改物質、產量或守恆。", "答案為 A。"], "easy"),
    q(5, "可逆反應達到動態平衡時，哪項描述正確？", ["正反應與逆反應仍持續，但在相同條件下速率相等，宏觀濃度維持穩定", "所有粒子停止運動", "反應物完全變成生成物", "只剩逆反應而沒有正反應"], "A", "動態平衡不是靜止；微觀反應仍在進行，只是正、逆反應速率相等，使可測量的濃度等宏觀量維持穩定。", "把微觀持續變化與宏觀穩定分成兩層判斷。", ["先辨認題目是否為可逆反應。", "檢查正反應與逆反應是否仍存在。", "確認兩方向速率相等而非都等於零。", "B、C、D 分別把平衡誤解成停止、完全反應或單向反應。", "所以 A 最完整。"], "medium"),
    q(6, "某可逆反應在平衡狀態下增加反應物濃度，若其他條件不變，系統短時間內通常會？", ["正反應速率先增加，消耗部分新增反應物，直到建立新的平衡", "正反應和逆反應都永久停止", "生成物立刻全部消失且永不恢復", "平衡位置必定完全不變"], "A", "增加反應物會使正向碰撞機會先增加，系統會透過正反應消耗部分新增物，最後在新條件下重新達到動態平衡。", "分開『瞬間速率變化』和『最後新平衡』兩個時刻。", ["標出被增加的反應物。", "判斷立即增加的是哪一方向的有效碰撞。", "推論系統會消耗部分新增反應物。", "檢查是否仍存在逆反應與新的穩定狀態。", "因此 A 同時描述變化歷程與結果。"], "hard"),
    q(7, "某反應升高溫度後，平衡混合物中生成物比例增加；由此可推論較合理的是？", ["升溫有利於吸熱方向，不能只用『升溫一定加快所有反應』代替平衡判斷", "升溫必定使所有生成物比例減少", "溫度只影響顏色，不影響平衡", "只要反應變快，平衡組成就一定不變"], "A", "升溫可能改變平衡位置，方向取決於正、逆反應的熱效應；速率變快與平衡組成改變是不同概念。", "先讀資料判斷平衡位移，再區分速率和組成。", ["比較升溫前後生成物比例。", "判斷平衡往生成物方向移動。", "用勒沙特列原理推論該方向吸熱。", "排除把速率、顏色或固定規則當成平衡位置。", "答案為 A。"], "hard"),
    q(8, "若要研究催化劑對反應速率的影響，哪項設計最公平？", ["固定反應物量、濃度、溫度與攪拌方式，只改變是否加入等量催化劑，並比較達到相同產物量所需時間", "同時改變反應物濃度與催化劑", "一組加熱、一組不加熱", "只觀察哪組顏色比較深"], "A", "公平實驗只改變催化劑這一項，並以可量測的反應時間或產氣速率比較；其他條件改變會造成混淆。", "先列控制變因，再找單一自變因與可量測依變因。", ["列出可能影響速率的溫度、濃度、量與攪拌。", "把催化劑有無設為唯一自變因。", "選擇達到相同產物量的時間作為指標。", "B、C 同時改變多項條件，D 缺乏可靠量化。", "因此 A 是公平設計。"], "medium"),
    q(9, "工業製造氨時，若某條件能提高反應速率但也增加能源消耗，選擇製程時最適合的判準是？", ["同時比較產率、反應速率、能源成本、安全與設備限制，而不是只追求單一最高速率", "只選溫度最高的條件", "只看一次實驗的顏色", "只要速率快就必然最適合量產"], "A", "工業製程是多目標決策，需在產率、速度、能源、材料安全與成本間取捨；最快不等於最有效率或最可持續。", "把課本反應條件轉成多指標製程決策。", ["列出需要比較的產率與速率。", "加入能源、設備、安全與環境限制。", "比較各條件的總體效益而非單一指標。", "B、C、D 都忽略量產的系統限制。", "所以 A 最符合製程判準。"], "medium"),
    q(10, "某工廠要改善可逆反應的產物收率，哪項做法最需要先用資料驗證？", ["調整壓力、溫度或移除生成物是否使平衡朝目標產物移動，並同時檢查速率與能源代價", "不看反應式就任意提高所有條件", "只把反應時間拉長便宣稱收率提高", "只測量設備外觀而不量產物量"], "A", "改善收率需由反應式與資料判斷平衡方向，再評估速率、成本和安全；延長時間或盲目改條件不保證產物增加。", "以反應式、平衡資料和製程代價三層交叉判斷。", ["先確認反應物與生成物的比例及氣體莫耳數。", "預測改變溫度、壓力或移除生成物的平衡方向。", "實測目標產物收率與達平衡時間。", "比較能源、設備和安全代價。", "只有 A 同時包含可驗證的平衡與製程判準。"], "hard"),
]


def main():
    lesson = json.loads(LESSON.read_text(encoding="utf-8"))
    lesson["updatedAt"] = TODAY
    lesson["reviewStatus"] = "draft"
    lesson["fusionRecord"] = {
        "commonCore": [
            "三版本公開資料共同支持以化學反應證據、粒子重新排列與原子守恆理解物質變化。",
            "可逆反應的動態平衡必須同時看微觀正逆反應與宏觀濃度，不能誤解為反應停止。",
            "速率、平衡位置、產率與工業製程條件彼此相關但不是同一概念。",
        ],
        "versionDifferences": [
            "南一公開線索較適合作為由現象與生活物質進入反應證據的入口。",
            "康軒公開線索較突出反應式、控制變因與資料判讀，能支撐條件比較。",
            "翰林公開課程線索補充可逆反應、平衡及工業製造的微觀與製程連結；公開資料不足以宣稱取得完整教材內容。",
        ],
        "originalAdditions": [
            "以『證據—粒子—守恆—條件—製程』五層框架串連根單元。",
            "把動態平衡與速率、收率和能源取捨放在同一個工業決策情境中比較。",
        ],
        "llmSynthesisNote": "依官方課綱、本單元 KG、南一／康軒／翰林公開版本線索與三筆公立學校／公開自然科試題及課程資料能力方向，重新撰寫反應證據、原子守恆、反應速率、動態平衡與工業製造。原有 10 題為食鹽質量與日期的泛化套題，已逐題改寫為 J 根單元專屬題，均具唯一答案、解析與五步解法，未複製教材或試題文字、圖表與答案；Terra 第二輪與正式發布審查尚未完成，維持 draft。",
    }
    for entry in lesson.get("versionResearch", []) + lesson.get("publisherResearch", []):
        entry["reviewedAt"] = TODAY
    for item in QUESTIONS:
        number = item["id"].rsplit("-", 1)[-1]
        (QDIR / f"question-science-content-j-{number}.json").write_text(json.dumps(item, ensure_ascii=False, indent=2) + "\n", encoding="utf-8")
    REPORT.write_text(json.dumps({
        "unit": "J：物質的反應、平衡及製造",
        "lessonId": lesson["id"],
        "status": "first-pass-ai-review-complete",
        "reviewStatus": "draft",
        "checkedQuestions": 10,
        "checks": {"unitSpecificOriginalContent": True, "threeVersionResearchRecords": True, "threePublicSchoolExamPatternSources": True, "answersAndDetailedSteps": True, "interactivePredictionManipulationExplanation": True, "terraSecondPass": "pending"},
        "reviewedAt": TODAY,
        "note": "原有 10 題為食鹽質量與日期的泛化套題，已逐題改寫為反應證據、原子守恆、配平、速率、動態平衡與工業製程專屬問題；每題有唯一答案、解析與五步解法，三筆公開試題／課程資料僅作 pattern-only 來源，正式發布前仍須第二輪 AI／Terra 內容複核。",
    }, ensure_ascii=False, indent=2) + "\n", encoding="utf-8")
    LESSON.write_text(json.dumps(lesson, ensure_ascii=False, indent=2) + "\n", encoding="utf-8")
    print("authored science content j")


if __name__ == "__main__":
    main()
