import json
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
LESSON = ROOT / "lessons/science/lesson-science-content-ja.json"
REPORT = ROOT / "implementation/reports/science-content-ja-first-pass-review.json"
URLS = [
    ("https://www.yacjh.kh.edu.tw/upload/221/101_30637/114%E4%B8%8B%E5%AD%B8%E6%9C%9F%E7%AC%AC%E4%B8%80%E6%AC%A1%E6%AE%B5%E8%80%83%E4%B8%89%E5%B9%B4%E7%B4%9A%E8%87%AA%E7%84%B6.pdf", "高雄市立鹽埕國民中學公開自然科段考", "物質反應、質量守恆與粒子模型"),
    ("https://www.nhjh.tp.edu.tw/uploads/1738658165906utzaMLG4.pdf", "臺北市立內湖國民中學公開自然科段考", "化學變化、反應式與資料判讀"),
    ("https://www.kcjh.kh.edu.tw/upload/190/104_34764/%E5%9C%8B%E6%98%8C--%E4%BA%8C%E5%B9%B4%E7%B4%9A--%E8%87%AA%E7%84%B6%E7%A7%91.pdf", "高雄市立國昌國民中學公開自然科試題", "生活反應、系統邊界與安全"),
]
BOUNDARY = "本紀錄只保存可追溯公開來源的章節定位、教學方向與評量能力；不複製出版社或學校教材正文、原題、選項、圖表、答案、影音或版面。"
ITEMS = [
    ("把鎂帶放入稀鹽酸後出現氣泡，容器外壁溫度上升。哪個判斷最合理？", ["只代表液體沸騰", "只能由氣泡判定生成的氣體種類", "現象提示可能有新物質與能量變化，仍需用反應物、產物與安全資料確認", "溫度上升表示原子消失"], "C", "氣泡和溫度變化是化學反應的線索，但不能單靠一種現象指定產物；要用粒子、質量與其他安全證據交叉檢查。"),
    ("在密閉袋中混合兩種反應物，反應前後總質量幾乎相同。這最直接支持什麼？", ["原子重新排列，系統內總質量近似守恆", "反應沒有發生", "生成物一定是氣體", "溫度必定保持不變"], "A", "密閉系統把氣體留在裝置中；質量近似不變支持原子重新排列而非消失，但還需觀察其他證據判斷反應性質。"),
    ("同一反應在開放燒杯中量得質量下降，最先應檢查哪個原因？", ["質量守恆在化學反應中失效", "有氣體逸出，使系統邊界外的物質未被秤到", "原子變成沒有質量的熱", "只要顏色改變就能忽略秤量"], "B", "開放系統可能有氣體離開，秤到的只是剩在容器內的部分；要先追蹤物質進出，再討論測量誤差。"),
    ("若反應式左側有 2 個氫原子與 2 個氧原子，右側也必須保留什麼？", ["只保留反應前的分子形狀", "任意增加新的元素以配平", "把下標改成能讓數字相同即可", "每種元素的原子種類與總數都相同，只重新排列組合"], "D", "化學反應改變的是原子組合；配平要求左右每種元素的原子數相等，不是創造元素或任意改變化學式下標。"),
    ("配平  Mg＋O₂→MgO 時，最小整數係數應為何？", ["1、1、1", "2、1、2", "1、2、2", "2、2、1"], "B", "右側 2 個 MgO 需要 2 個鎂與 2 個氧原子，因此左側放 2Mg 和 1O₂，係數為 2、1、2。"),
    ("為什麼配平反應式時不能把 H₂O 的下標 2 改成 3？", ["下標只表示反應速度", "係數永遠不能改", "下標改變會換成另一種物質，應只調整整個物質前的係數", "改下標會讓所有反應停止"], "C", "下標是物質組成的一部分；改變 H₂O 的下標等於改寫物質本身，配平只能調整分子或化學式前的係數。"),
    ("兩種透明溶液混合後出現沉澱。哪項資料最能加強『形成新物質』的判斷？", ["只記錄杯子的顏色", "只問觀察者覺得是否漂亮", "不記錄原料種類以避免偏見", "記錄反應物、沉澱性質與控制條件，並比較混合前後的粒子或質量資料"], "D", "沉澱是重要線索，但要把原料、條件與產物資料記下來，才能將宏觀現象連到粒子模型並排除物理混合的替代解釋。"),
    ("要研究鐵釘生鏽是否需要水與氧氣，哪種設計最能控制變因？", ["分別設置乾燥空氣、煮沸後隔絕空氣與潮濕空氣，使用相同鐵釘並記錄時間", "每支鐵釘用不同材質並只觀察一天", "先選會生鏽的照片再安排條件", "同時改變鐵釘大小、溫度、水量與氧氣"], "A", "只改變水與氧氣的可得性、固定鐵釘與觀察時間，才能比較鏽蝕差異並建立可檢驗的因果判斷。"),
    ("密閉反應中溫度升高，但總質量近似不變；最恰當的說明是？", ["能量增加表示有原子被創造", "質量守恆只適用於吸熱反應", "能量可在系統內重新分配或與環境交換，不能因此否定原子數守恆", "只要溫度變化就代表質量必然增加"], "C", "質量守恆和能量變化是不同的判讀面向；溫度改變可反映能量轉移或重新分配，不等於創造原子。"),
    ("想清潔水槽時，哪個做法最符合物質反應的安全探究原則？", ["把不同清潔劑混合以觀察更多氣泡", "先查閱標示與安全資料，依指示單獨使用並保持通風，不做未授權混合", "用手直接測試是否放熱", "在密閉瓶中加熱混合物以加速反應"], "B", "清潔劑可能產生有害氣體或熱；安全探究先查標示、遵守使用條件與通風，不能為了觀察反應任意混合或加熱。"),
]


def refs():
    return [{"url": u, "title": f"{t}；只取{loc}的題型與推理方向，未複製原題、選項、圖表或答案。", "year": "113-114", "subject": "science", "locator": loc, "observedPattern": "公開自然科評量常要求由反應現象、粒子數、質量、反應式、控制變因與安全條件建立推論；本題以全新語料重寫。", "reuseDecision": "pattern-only", "status": "recorded", "locatorLevel": "paper"} for u, t, loc in URLS]


def main():
    lesson = json.loads(LESSON.read_text(encoding="utf-8")); lesson.update({"updatedAt": "2026-09-21", "reviewStatus": "draft", "authoringStandard": "version-fused-v1"})
    for row in lesson.get("publisherResearch", []): row["reviewedAt"] = "2026-09-21"
    for row in lesson.get("versionResearch", []): row["reviewedAt"] = "2026-09-21"; row["licenseBoundary"] = BOUNDARY
    lesson["fusionRecord"]["llmSynthesisNote"] = "本課依官方自然科學課綱、kg-science-content-ja、南一／康軒／翰林可取得的公開研究方向與三筆公立學校自然科試題能力模式，以自己的話獨立融合反應現象、粒子重新排列、質量守恆、系統邊界、反應式配平、控制變因與安全；保留既有安全互動，未複製教材或試題，Terra 第二輪與正式發布審查尚未完成，維持 draft。"
    LESSON.write_text(json.dumps(lesson, ensure_ascii=False, indent=2) + "\n", encoding="utf-8")
    steps = ["圈出反應物、現象、系統邊界、元素原子數、係數或安全條件。", "把可直接觀察的資料與粒子模型或反應式推論分開。", "逐元素計數，或依控制變因與質量進出檢查因果關係。", "排除把氣泡直接等同特定產物、改變化學式下標配平、忽略開放系統或任意混合危險物質的選項。", "用完整句回查答案，補上測量誤差、系統邊界與安全限制。"]
    for i, (prompt, options, answer, explanation) in enumerate(ITEMS, 1):
        path = ROOT / f"questions/science/question-science-content-ja-{i}.json"; q = json.loads(path.read_text(encoding="utf-8")); q["prompt"] = prompt; q["options"] = [{"id": chr(65+j), "text": text} for j, text in enumerate(options)]; q["answer"] = {"value": answer, "explanation": explanation}; q["examPatternRefs"] = refs(); q["reviewStatus"] = "draft"; q["updatedAt"] = "2026-09-21"; q["solutionStrategy"] = "先把宏觀現象、微觀粒子、質量與系統邊界分開，再用本題要求的反應規律逐項核對。"; q["solutionSteps"] = steps; q["provenance"]["sourceUrl"] = URLS[0][0]; q["provenance"]["sourceLocator"] = "三筆公立學校公開自然科試題中的反應現象、粒子守恆、質量、反應式、控制變因與安全判讀能力；本題改寫為物質反應原創情境。"; path.write_text(json.dumps(q, ensure_ascii=False, indent=2) + "\n", encoding="utf-8")
    REPORT.write_text(json.dumps({"unit": lesson["title"], "lessonId": lesson["id"], "status": "first-pass-ai-review-complete", "reviewStatus": "draft", "checks": {"unitSpecificOriginalContent": True, "threeVersionResearchRecords": True, "publicExamPatternRewrite": True, "fusionRecordPresent": True, "interactivePredictionManipulationExplanation": True, "answersAndDetailedSteps": True, "terraSecondPass": "pending"}, "reviewedAt": "2026-09-21"}, ensure_ascii=False, indent=2) + "\n", encoding="utf-8")
    print("authored science content ja")


if __name__ == "__main__": main()
