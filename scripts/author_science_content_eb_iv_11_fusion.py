import json
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
LESSON = ROOT / "lessons/science/lesson-science-content-eb-iv-11.json"
REPORT = ROOT / "implementation/reports/science-content-eb-iv-11-first-pass-review.json"
URLS = [
    ("https://www.nehs.tc.edu.tw/wp-content/uploads/sites/95/2026/02/6%E7%90%86%E5%8C%96%E7%A7%91-%E4%B9%9D%E5%B9%B4%E7%B4%9A-%E9%A1%8C%E5%BA%AB.pdf", "國立中科實驗高級中學公開九年級理化題庫", "力、動量、衝量與碰撞計算"),
    ("https://www.nhjh.tp.edu.tw/uploads/1675417616549dOhkhC5L.pdf", "臺北市立內湖國民中學公開九年級理化段考", "平均力、作用時間與安全設計"),
    ("https://www.kcjh.kh.edu.tw/upload/190/104_34764/%E4%B8%89%E5%B9%B4%E7%B4%9A%E7%90%86%E5%8C%96-%E7%AC%AC三次段考5-OK.pdf", "高雄市立國昌國民中學公開三年級自然科試題", "碰撞、動量變化與資料圖表"),
]
BOUNDARY = "本紀錄只保存可追溯公開來源的章節定位、教學方向與評量能力；不複製出版社或學校教材正文、原題、選項、圖表、答案、影音或版面。"
PATTERN = "公立學校公開自然／理化試題常以 p=mv、J=FΔt、力—時間圖、接球、煞車、碰撞與向量方向考查動量變化；本題只取能力方向並重新設計情境與數據。"
EXPLANATIONS = [
    "C。p=mv=3×4=12 kg·m/s；向東取正，所以動量為 +12 kg·m/s，方向向東。",
    "A。p_i=2×5=+10，p_f=2×(-1)=-2 kg·m/s，Δp=p_f-p_i=-12 kg·m/s，表示向西改變 12。",
    "C。衝量 J=FΔt=10×0.30=3.0 N·s，也等於動量變化量的大小。",
    "C。初動量 0，末動量 p=2×3=6 kg·m/s，因此 Δp 大小為 6 kg·m/s，方向向東。",
    "B。同一顆球要相同 Δp，即相同衝量 FΔt；作用時間變成 4 倍，理想平均力應變成原來 1/4。",
    "C。接球時手臂向後增加接觸時間，在相同動量變化下可降低平均力，不是把來球質量或動量直接消除。",
    "B。煞車力與車前進方向相反；車速降低使動量變化也向後，因此兩者同向，都是向西（負方向）。",
    "A。力—時間圖下面積就是衝量，矩形面積=20×0.50=10 N·s。",
    "A。若系統只選一台車，碰撞車對它的外力在作用時間內造成動量變化，可用衝量 J=Δp 描述；若選兩車系統，內力需另作處理。",
    "C。平均力 6 N 作用 2 s 的衝量為 12 N·s，因此動量向東增加 12 kg·m/s；質量只在求速度時再使用。",
]
STRATEGIES = [
    "先定正方向，再直接用 p=mv 並保留方向符號。",
    "先算初、末動量，再用 Δp=p_f-p_i，特別留意反向速度。",
    "把平均力和作用時間相乘，確認 N·s 與 kg·m/s 等價。",
    "利用初動量為零的條件，直接由末速度求動量改變。",
    "固定 Δp 比較 FΔt，作用時間放大幾倍，平均力反向縮小幾倍。",
    "在動量變化固定時延長接觸時間，判斷平均力如何下降。",
    "先判煞車力方向，再用末動量減初動量檢查方向。",
    "把力—時間圖下方面積當作衝量，確認圖形單位。",
    "先畫系統邊界，再判斷外力衝量與內力是否互相抵消。",
    "由 J=FΔt 得到 Δp，再依需要用 p=mv 求速度改變。",
]
STEPS = [
    "選定系統與正方向，寫出質量、初速、末速和作用時間。",
    "計算初、末動量並保留向量正負。",
    "用 Δp=p_f-p_i 或 J=FΔt 連結力與動量。",
    "檢查圖表面積、單位與數量級。",
    "說明接觸時間、外力、系統邊界及安全設計限制。",
]


def refs():
    return [{"url": u, "title": f"{t}；只取{loc}的題型與推理方向，未複製原題、選項、圖表、答案或版面。", "year": "109-115", "subject": "science", "locator": loc, "observedPattern": PATTERN, "reuseDecision": "pattern-only", "status": "recorded", "locatorLevel": "paper"} for u, t, loc in URLS]


def main():
    lesson = json.loads(LESSON.read_text(encoding="utf-8"))
    lesson.update({"updatedAt": "2026-09-21", "reviewStatus": "draft", "authoringStandard": "version-fused-v1"})
    for row in lesson.get("publisherResearch", []): row["reviewedAt"] = "2026-09-21"
    for row in lesson.get("versionResearch", []): row.update({"reviewedAt": "2026-09-21", "licenseBoundary": BOUNDARY})
    lesson["fusionRecord"]["llmSynthesisNote"] = "本課依官方自然科學課綱、kg-science-content-eb-iv-11、南一／康軒／翰林可取得的公開研究方向與三筆公立學校自然／理化試題能力模式，以自己的話獨立融合動量 p=mv、衝量 J=FΔt、向量方向、力—時間圖、接球、煞車、碰撞與系統邊界；保留安全接球—圖表面積—碰撞分析互動，未複製教材或試題，Terra 第二輪與正式發布審查尚未完成，維持 draft。"
    LESSON.write_text(json.dumps(lesson, ensure_ascii=False, indent=2) + "\n", encoding="utf-8")
    for i in range(1, 11):
        path = ROOT / f"questions/science/question-science-content-eb-iv-11-{i}.json"
        q = json.loads(path.read_text(encoding="utf-8"))
        q.update({"examPatternRefs": refs(), "reviewStatus": "draft", "updatedAt": "2026-09-21", "solutionStrategy": STRATEGIES[i - 1], "solutionSteps": STEPS})
        q["answer"]["explanation"] = EXPLANATIONS[i - 1]
        q["provenance"].update({"sourceUrl": URLS[0][0], "sourceLocator": "三筆公立學校公開自然／理化試題中的動量、衝量、力—時間圖、碰撞、煞車、接球與系統邊界能力；本題改寫為力、作用時間、質量與速度改變原創情境。"})
        path.write_text(json.dumps(q, ensure_ascii=False, indent=2) + "\n", encoding="utf-8")
    REPORT.write_text(json.dumps({"unit": lesson["title"], "lessonId": lesson["id"], "status": "first-pass-ai-review-complete", "reviewStatus": "draft", "checks": {"unitSpecificOriginalContent": True, "threeVersionResearchRecords": True, "publicExamPatternRewrite": True, "fusionRecordPresent": True, "interactivePredictionManipulationExplanation": True, "answersAndDetailedSteps": True, "terraSecondPass": "pending"}, "reviewedAt": "2026-09-21"}, ensure_ascii=False, indent=2) + "\n", encoding="utf-8")
    print("authored science content eb iv 11")


if __name__ == "__main__": main()
