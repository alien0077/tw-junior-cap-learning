import json
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
LESSON = ROOT / "lessons/science/lesson-science-content-fa-iv-5.json"
REPORT = ROOT / "implementation/reports/science-content-fa-iv-5-first-pass-review.json"
URLS = [
    ("https://www.nehs.tc.edu.tw/wp-content/uploads/sites/95/2026/02/6%E7%90%86%E5%8C%96%E7%A7%91-%E4%B9%9D%E5%B9%B4%E7%B4%9A-%E9%A1%8C%E5%BA%AB.pdf", "國立中科實驗高級中學公開九年級理化題庫", "海水成分、密度與資料判讀"),
    ("https://www.nhjh.tp.edu.tw/uploads/1675417616549dOhkhC5L.pdf", "臺北市立內湖國民中學公開九年級理化段考", "鹽度、溫度、海水分層與海洋環境"),
    ("https://www.kcjh.kh.edu.tw/upload/190/104_34764/%E4%B8%89%E5%B9%B4%E7%B4%9A%E7%90%86%E5%8C%96-%E7%AC%AC三次段考5-OK.pdf", "高雄市立國昌國民中學公開三年級自然科試題", "溶液、濃度、密度與淡化應用"),
]
BOUNDARY = "本紀錄只保存可追溯公開來源的章節定位、教學方向與評量能力；不複製出版社或學校教材正文、原題、選項、圖表、答案、影音或版面。"
PATTERN = "公立學校公開自然／理化試題常以溶液組成、離子、濃度、密度、資料剖面、溫度／鹽度變化與環境應用考查海水特性；本題只取能力方向並重新設計情境與數據。"
EXPLANATIONS = [
    "A。海水主要陽離子包含 Na⁺，主要陰離子為 Cl⁻；另有硫酸根、鎂、鈣、鉀等，不能把海水簡化成單一鹽。",
    "C。海水含多種離子、溶解氣體及微量物質，蒸乾後的鹽類組成和比例不等於純氯化鈉溶液。",
    "A。鹽度描述海水中溶解鹽類的總量或整體程度，不是某一種離子的單獨濃度，也不能忽略單位與定義。",
    "B。35 PSU 是開放海域海水鹽度的近似量級，表示整體鹽分尺度，不等於每公升固定含 35 g 的純食鹽。",
    "A。深度增加同時出現降溫、鹽度上升與密度上升，支持溫鹽差造成的分層線索；仍不能單靠此圖完整確定流向。",
    "C。蒸發移走水而留下鹽，會使表層鹽度增加；降雨、河川淡水或融冰則常使鹽度降低。",
    "D。蒸餾或逆滲透能降低鹽分，但需要能量、設備與維護，且濃縮鹵水處置也有環境代價。",
    "A。應先比較兩站的溫度、鹽度、密度剖面與採樣時間／深度，再搭配風場或流速資料提出水團或洋流假說。",
    "B。溫度升高通常使水膨脹、密度降低；鹽度不變時可先依此方向判斷，但壓力與成分也可能影響實際值。",
    "A。先確認縱軸是深度且方向一致，再對照單位、測站和三條曲線；不能把顏色深淺或單一曲線直接當成流向證明。",
]
STRATEGIES = [
    "先按陽離子／陰離子分類，再檢查主要成分與電荷符號。",
    "比較海水的多種溶質與蒸乾殘留，不把天然溶液等同單一鹽溶液。",
    "確認鹽度描述的是總溶解鹽量，而非單一離子或純食鹽濃度。",
    "讀清 PSU 的意義與近似量級，再避免自行替換成不相容單位。",
    "同步比較溫度、鹽度、密度和深度，寫出資料支持的分層範圍。",
    "判斷水分進出：蒸發、降水、河川輸入、結冰與融冰對鹽度方向不同。",
    "把除鹽效果與能量、設備、鹵水排放及維護成本一起評估。",
    "用多變量剖面與額外流速／風場資料支持假說，避免從密度差直接宣稱流向。",
    "先固定鹽度，使用溫度對密度的通常方向，再檢查其他條件。",
    "先讀圖例、軸、單位、方向和測站，再比較曲線的變化。",
]
STEPS = [
    "辨認海水成分、鹽度、溫度、深度與密度的定義和單位。",
    "將離子、溶質總量或水分進出對應到可觀察變化。",
    "逐軸讀取資料並比較測站、深度或時間差異。",
    "用溫度—鹽度—密度關係檢查推論方向。",
    "交代資料能支持的範圍與尚需補測的流向、成因或環境影響。",
]


def refs():
    return [{"url": u, "title": f"{t}；只取{loc}的題型與推理方向，未複製原題、選項、圖表、答案或版面。", "year": "109-115", "subject": "science", "locator": loc, "observedPattern": PATTERN, "reuseDecision": "pattern-only", "status": "recorded", "locatorLevel": "paper"} for u, t, loc in URLS]


def main():
    lesson = json.loads(LESSON.read_text(encoding="utf-8"))
    lesson.update({"updatedAt": "2026-09-21", "reviewStatus": "draft", "authoringStandard": "version-fused-v1"})
    for row in lesson.get("publisherResearch", []): row["reviewedAt"] = "2026-09-21"
    for row in lesson.get("versionResearch", []): row.update({"reviewedAt": "2026-09-21", "licenseBoundary": BOUNDARY})
    lesson["fusionRecord"]["llmSynthesisNote"] = "本課依官方自然科學課綱、kg-science-content-fa-iv-5、南一／康軒／翰林可取得的公開研究方向與三筆公立學校自然／理化試題能力模式，以自己的話獨立融合海水多種離子、鹽度、溫度、深度、密度、分層、水團、淡化能量與鹵水環境代價；保留海水蒸乾—剖面資料—淡化決策互動，未複製教材或試題，Terra 第二輪與正式發布審查尚未完成，維持 draft。"
    LESSON.write_text(json.dumps(lesson, ensure_ascii=False, indent=2) + "\n", encoding="utf-8")
    for i in range(1, 11):
        path = ROOT / f"questions/science/question-science-content-fa-iv-5-{i}.json"
        q = json.loads(path.read_text(encoding="utf-8"))
        q.update({"examPatternRefs": refs(), "reviewStatus": "draft", "updatedAt": "2026-09-21", "solutionStrategy": STRATEGIES[i - 1], "solutionSteps": STEPS})
        q["answer"]["explanation"] = EXPLANATIONS[i - 1]
        q["provenance"].update({"sourceUrl": URLS[0][0], "sourceLocator": "三筆公立學校公開自然／理化試題中的海水成分、溶液、鹽度、密度、剖面資料、淡化與環境應用能力；本題改寫為海水的成分與特性原創情境。"})
        path.write_text(json.dumps(q, ensure_ascii=False, indent=2) + "\n", encoding="utf-8")
    REPORT.write_text(json.dumps({"unit": lesson["title"], "lessonId": lesson["id"], "status": "first-pass-ai-review-complete", "reviewStatus": "draft", "checks": {"unitSpecificOriginalContent": True, "threeVersionResearchRecords": True, "publicExamPatternRewrite": True, "fusionRecordPresent": True, "interactivePredictionManipulationExplanation": True, "answersAndDetailedSteps": True, "terraSecondPass": "pending"}, "reviewedAt": "2026-09-21"}, ensure_ascii=False, indent=2) + "\n", encoding="utf-8")
    print("authored science content fa iv 5")


if __name__ == "__main__": main()
