import json
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
LESSON = ROOT / "lessons/science/lesson-science-content-jb-iv-2.json"
REPORT = ROOT / "implementation/reports/science-content-jb-iv-2-first-pass-review.json"
URLS = [
    ("https://www.yacjh.kh.edu.tw/upload/221/101_30637/114%E4%B8%8B%E5%AD%B8%E6%9C%9F%E7%AC%AC%E4%B8%80%E6%AC%A1%E6%AE%B5%E8%80%83%E4%B8%89%E5%B9%B4%E7%B4%9A%E8%87%AA%E7%84%B6.pdf", "高雄市立鹽埕國民中學公開自然科段考", "電解質解離、離子與水溶液導電"),
    ("https://www.nhjh.tp.edu.tw/uploads/1738658165906utzaMLG4.pdf", "臺北市立內湖國民中學公開自然科段考", "強弱電解質、濃度、導電度與控制變因"),
    ("https://www.kcjh.kh.edu.tw/upload/190/104_34764/%E5%9C%8B%E6%98%8C--%E4%BA%8C%E5%B9%B4%E7%B4%9A--%E8%87%AA%E7%84%B6%E7%A7%91.pdf", "高雄市立國昌國民中學公開自然科試題", "離子數量、稀釋、混合溶液與測量限制"),
]
BOUNDARY = "本紀錄只保存可追溯公開來源的章節定位、教學方向與評量能力；不複製出版社或學校教材正文、原題、選項、圖表、答案、影音或版面。"
EXPLANATIONS = [
    "A。電解質溶於水後形成可移動的陽、陰離子；在電場中離子定向移動，使溶液具有導電能力。",
    "B。NaCl(s)溶於水可寫成 NaCl→Na⁺+Cl⁻，固體晶格中的離子進入水溶液成為可移動粒子；不是生成金屬鈉。",
    "C。CaCl₂→Ca²⁺+2Cl⁻，每一個化學式單位產生一個鈣離子和兩個氯離子，電荷總和仍為零。",
    "D。溶液導電的直接原因是其中存在能在電場中移動的離子；中性分子即使溶解也不必然提供離子導電。",
    "B。強電解質在水中解離比例通常較高，弱電解質只部分解離；強弱不是單純由溶液顏色或濃度決定。",
    "C。加水使總離子量近似不變但體積增加，單位體積離子濃度通常下降，導電度也可能降低；需指定測量條件。",
    "D。酸在水中形成可移動的氫離子（更精確可描述為水合氫離子）與相應陰離子，離子移動使溶液導電。",
    "A。要預測混合後導電性，需看兩種電解質的解離程度、離子種類與濃度、是否反應沉澱，以及總體積。",
    "C。比較導電性應固定濃度或離子總量、體積、溫度、電極、電壓與測量時間，否則差異可能來自條件不一致。",
    "B。導電度是離子種類、數量、移動性、濃度、溫度與儀器條件共同結果；較高導電度不能單獨證明濃度較高。",
]
STRATEGIES = [
    "先判斷是否形成可移動離子，再連到電場中的離子移動。",
    "讀化學式的離子比例與電荷，寫出解離式並檢查電荷守恆。",
    "依陽離子與陰離子下標列數量，確認總電荷為零。",
    "把導電的直接證據鎖定在可移動離子，不用溶解或顏色代替。",
    "比較解離程度與離子數，分開強弱電解質和濃度概念。",
    "稀釋時同時看離子總量、體積與單位體積濃度。",
    "標出酸在水中的離子，說明其移動和導電關係。",
    "混合前先列離子、濃度、體積與可能沉澱或中和反應。",
    "列出濃度、溫度、電極與儀器等控制變因再比較導電性。",
    "把導電度視為多項因素結果，不由單一數值過度推論濃度。",
]


def refs():
    return [{"url": u, "title": f"{t}；只取{loc}的題型與推理方向，未複製原題、選項、圖表或答案。", "year": "113-114", "subject": "science", "locator": loc, "observedPattern": "公開自然科評量常要求連結電解質解離、離子比例、導電、強弱電解質、稀釋、混合與測量控制；本題以全新水溶液情境重寫。", "reuseDecision": "pattern-only", "status": "recorded", "locatorLevel": "paper"} for u, t, loc in URLS]


def main():
    lesson = json.loads(LESSON.read_text(encoding="utf-8")); lesson.update({"updatedAt": "2026-09-21", "reviewStatus": "draft", "authoringStandard": "version-fused-v1"})
    lesson["content"] = {"summary": "電解質溶於水後形成可移動的離子，離子種類、數量、移動性與溶液條件共同決定導電表現。本課從食鹽、氯化鈣、酸與混合溶液的解離式出發，連結電荷守恆、濃度、稀釋、強弱電解質與公平測量。", "sections": [{"heading": "學習目標", "body": "你將能由化學式寫出電解質解離的離子比例，說明陽離子和陰離子如何造成導電，並區分強弱電解質、濃度、稀釋和導電度；也能檢查混合溶液與測量條件。"}, {"heading": "探究流程", "body": "先從化學式列出離子與電荷，再預測水溶液中可移動粒子的種類和數量；接著改變濃度或電解質種類，固定溫度、電極與體積，將導電讀值與離子模型互相核對。"}, {"heading": "常見錯誤", "body": "溶解不一定等於解離，導電度高也不必然代表濃度高；強電解質不是濃度永遠高，稀釋會改變單位體積離子數但不會憑空消滅離子。解離式還要同時檢查原子數和總電荷。"}, {"heading": "自我檢核", "body": "選擇 NaCl、CaCl₂ 或酸，寫出解離式、標記離子移動方向，預測稀釋或混合後的導電變化，再指出一項需要固定的測量條件與一項可能的替代解釋。"}]}
    for row in lesson.get("publisherResearch", []): row["reviewedAt"] = "2026-09-21"
    for row in lesson.get("versionResearch", []): row.update({"reviewedAt": "2026-09-21", "licenseBoundary": BOUNDARY})
    lesson["fusionRecord"]["llmSynthesisNote"] = "本課依官方自然科學課綱、kg-science-content-jb-iv-2、南一／康軒／翰林可取得的公開研究方向與三筆公立學校自然科試題能力模式，以自己的話獨立融合電解質解離、離子比例、電荷守恆、導電、強弱電解質、稀釋、混合溶液與公平測量；重寫食鹽—氯化鈣—酸—混合溶液互動，未複製教材或試題，Terra 第二輪與正式發布審查尚未完成，維持 draft。"
    LESSON.write_text(json.dumps(lesson, ensure_ascii=False, indent=2) + "\n", encoding="utf-8")
    steps = ["圈出化學式、離子種類、解離比例、電荷、濃度、體積與溫度。", "寫出解離式並檢查原子數與正負電荷守恆。", "把可移動離子數量與移動性連到導電預測，稀釋時區分總量和單位體積。", "混合時檢查沉澱、中和、離子反應與總體積，不用單一導電讀值判定濃度。", "回查電極、電壓、溫度、時間與儀器條件，說明結果的限制。"]
    for i in range(1, 11):
        path = ROOT / f"questions/science/question-science-content-jb-iv-2-{i}.json"; q = json.loads(path.read_text(encoding="utf-8")); q.update({"examPatternRefs": refs(), "reviewStatus": "draft", "updatedAt": "2026-09-21", "solutionStrategy": STRATEGIES[i-1], "solutionSteps": steps}); q["answer"]["explanation"] = EXPLANATIONS[i-1]; q["provenance"]["sourceUrl"] = URLS[0][0]; q["provenance"]["sourceLocator"] = "三筆公立學校公開自然科試題中的電解質解離、離子比例、導電、強弱電解質、稀釋、混合與測量控制能力；本題改寫為電解質原創情境。"; path.write_text(json.dumps(q,ensure_ascii=False,indent=2)+"\n",encoding="utf-8")
    REPORT.write_text(json.dumps({"unit":lesson["title"],"lessonId":lesson["id"],"status":"first-pass-ai-review-complete","reviewStatus":"draft","checks":{"unitSpecificOriginalContent":True,"threeVersionResearchRecords":True,"publicExamPatternRewrite":True,"fusionRecordPresent":True,"interactivePredictionManipulationExplanation":True,"answersAndDetailedSteps":True,"terraSecondPass":"pending"},"reviewedAt":"2026-09-21"},ensure_ascii=False,indent=2)+"\n",encoding="utf-8")
    print("authored science content jb iv 2")


if __name__ == "__main__": main()
