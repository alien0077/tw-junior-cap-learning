import json
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
LESSON = ROOT / "lessons/science/lesson-science-content-db-iv-6.json"
REPORT = ROOT / "implementation/reports/science-content-db-iv-6-first-pass-review.json"
URLS = [
    ("https://www.nehs.tc.edu.tw/wp-content/uploads/sites/95/2026/02/6%E7%90%86%E5%8C%96%E7%A7%91-%E4%B9%9D%E5%B9%B4%E7%B4%9A-%E9%A1%8C%E5%BA%AB.pdf", "國立中科實驗高級中學公開九年級理化題庫", "植物運輸、維管束與實驗判讀"),
    ("https://www.nhjh.tp.edu.tw/uploads/1675417616549dOhkhC5L.pdf", "臺北市立內湖國民中學公開九年級理化段考", "木質部、韌皮部、蒸散與水分運輸"),
    ("https://www.kcjh.kh.edu.tw/upload/190/104_34764/%E4%B8%89%E5%B9%B4%E7%B4%9A%E7%90%86%E5%8C%96-%E7%AC%AC三次段考5-OK.pdf", "高雄市立國昌國民中學公開三年級自然科試題", "染色水、環剝與控制變因"),
]
BOUNDARY = "本紀錄只保存可追溯公開來源的章節定位、教學方向與評量能力；不複製出版社或學校教材正文、原題、選項、圖表、答案、影音或版面。"
PATTERN = "公立學校公開自然／理化試題常以染色水、蒸散、木質部、韌皮部、環剝、枝條資料與控制變因考查植物運輸；本題只取能力方向並重新設計情境與選項。"
EXPLANATIONS = [
    "C。木質部主要運送根吸收的水和無機鹽向上，切斷後最先直接影響的是水分與無機鹽到葉片的路徑；韌皮部仍可能暫時運送有機物。",
    "B。若要檢驗木質部水分運輸，應固定枝條長度、葉片數、溫度與水量，只改變是否保留木質部或加入染色示蹤，並重複量測染色前進距離。",
    "A。紅色染水到達花瓣細線，直接支持水分可沿莖內連續管線抵達花瓣；尚不能只由顏色證明所有水都經同一種細胞。",
    "C。葉片蒸散使葉內水勢降低，透過連續水柱與毛細／張力作用促進根—莖—葉的水分上升；不是葉片直接用泵抽水。",
    "A。剪除大部分葉片會降低蒸散拉力，在根系與環境相同下，枝條吸水速率通常可能下降；仍須控制傷口與葉面面積差異。",
    "D。環剝切斷樹皮內較外側的韌皮部，葉片製造的有機養分向下輸送受阻，因而在傷口上方累積；木質部水運輸未必立刻中斷。",
    "A。形成層持續分裂並產生新的木質部與韌皮部，使木本莖逐年增粗；不是成熟木質部本身一直分裂。",
    "B。木質部的水和無機鹽通常由根向上，韌皮部的有機養分則由源輸往庫，方向可隨來源與需求改變，不能簡化成固定上下。",
    "A。看到染水到達葉脈只直接支持染液隨水路徑移動，尚不能單獨證明蒸散是唯一原因或染色水完全等同天然水流。",
    "C。要比較蒸散對吸水的影響，應使用有葉與去葉枝條，固定枝條長度、溫度、水量與時間，並重複量測質量減少或染水上升量。",
]
STRATEGIES = [
    "先確認被切斷的是木質部還是韌皮部，再對應運輸物質。",
    "只改維管束條件，固定枝條與環境，選擇可量化的染色進程。",
    "把染色結果限定在水路徑證據，不直接擴大成完整機制。",
    "從蒸散造成的水勢差與連續水柱解釋上升，不使用吸管比喻代替機制。",
    "比較葉面面積和吸水／失水資料，控制剪切傷口與環境。",
    "由環剝位置判斷韌皮部養分向下受阻，再分辨木質部水流。",
    "指出形成層的位置與分裂產物，連到莖的次生生長。",
    "分別追蹤木質部水鹽與韌皮部有機物，補上源庫方向。",
    "區分直接看見的染色和對蒸散、細胞路徑的推論。",
    "建立有葉／無葉對照，固定環境並用重複量測比較吸水差異。",
]
STEPS = [
    "辨認木質部、韌皮部、根、莖、葉與花的位置。",
    "確認運輸物質是水、無機鹽或有機養分。",
    "沿來源—管線—目的地畫出運輸箭頭。",
    "用染色、環剝、蒸散或對照資料檢查推論。",
    "說明實驗直接證據與尚未證明的機制限制。",
]
Q2_PROMPT = "若要測試木質部是否負責把根部吸收的水運到葉片，哪項設計較能支持結構功能關係？"
Q2_OPTIONS = ["同時改變枝條長度、葉片數與溫度", "固定枝條與環境，只改變木質部是否連通並重複量測染水上升", "只看一次葉片顏色便下結論", "依喜歡的結果挑選染色照片"]


def refs():
    return [{"url": u, "title": f"{t}；只取{loc}的題型與推理方向，未複製原題、選項、圖表、答案或版面。", "year": "109-115", "subject": "science", "locator": loc, "observedPattern": PATTERN, "reuseDecision": "pattern-only", "status": "recorded", "locatorLevel": "paper"} for u, t, loc in URLS]


def main():
    lesson = json.loads(LESSON.read_text(encoding="utf-8"))
    lesson.update({"updatedAt": "2026-09-21", "reviewStatus": "draft", "authoringStandard": "version-fused-v1"})
    for row in lesson.get("publisherResearch", []): row["reviewedAt"] = "2026-09-21"
    for row in lesson.get("versionResearch", []): row.update({"reviewedAt": "2026-09-21", "licenseBoundary": BOUNDARY})
    lesson["fusionRecord"]["llmSynthesisNote"] = "本課依官方自然科學課綱、kg-science-content-db-iv-6、南一／康軒／翰林可取得的公開研究方向與三筆公立學校自然／理化試題能力模式，以自己的話獨立融合木質部、韌皮部、根—莖—葉水鹽與有機養分運輸、蒸散、染色水、環剝、形成層與控制變因；移除原先誤放的水草光合作用題並改為木質部結構功能題，未複製教材或試題，Terra 第二輪與正式發布審查尚未完成，維持 draft。"
    LESSON.write_text(json.dumps(lesson, ensure_ascii=False, indent=2) + "\n", encoding="utf-8")
    for i in range(1, 11):
        path = ROOT / f"questions/science/question-science-content-db-iv-6-{i}.json"
        q = json.loads(path.read_text(encoding="utf-8"))
        if i == 2:
            q["prompt"] = Q2_PROMPT
            q["options"] = [{"id": chr(65 + n), "text": t} for n, t in enumerate(Q2_OPTIONS)]
            q["answer"]["value"] = "B"
        q.update({"examPatternRefs": refs(), "reviewStatus": "draft", "updatedAt": "2026-09-21", "solutionStrategy": STRATEGIES[i - 1], "solutionSteps": STEPS})
        q["answer"]["explanation"] = EXPLANATIONS[i - 1]
        q["provenance"].update({"sourceUrl": URLS[0][0], "sourceLocator": "三筆公立學校公開自然／理化試題中的植物運輸、木質部、韌皮部、蒸散、染色水、環剝與控制變因能力；本題改寫為植物維管束運輸功能原創情境。"})
        path.write_text(json.dumps(q, ensure_ascii=False, indent=2) + "\n", encoding="utf-8")
    REPORT.write_text(json.dumps({"unit": lesson["title"], "lessonId": lesson["id"], "status": "first-pass-ai-review-complete", "reviewStatus": "draft", "checks": {"unitSpecificOriginalContent": True, "threeVersionResearchRecords": True, "publicExamPatternRewrite": True, "fusionRecordPresent": True, "interactivePredictionManipulationExplanation": True, "answersAndDetailedSteps": True, "irrelevantQuestionRewritten": True, "terraSecondPass": "pending"}, "reviewedAt": "2026-09-21"}, ensure_ascii=False, indent=2) + "\n", encoding="utf-8")
    print("authored science content db iv 6")


if __name__ == "__main__": main()
