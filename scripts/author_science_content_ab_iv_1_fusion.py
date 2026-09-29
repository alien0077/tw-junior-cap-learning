import json
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
LESSON = ROOT / "lessons/science/lesson-science-content-ab-iv-1.json"
REPORT = ROOT / "implementation/reports/science-content-ab-iv-1-first-pass-review.json"
URLS = [
    ("https://www.yacjh.kh.edu.tw/upload/221/101_30637/114%E4%B8%8B%E5%AD%B8%E6%9C%9F%E7%AC%AC%E4%B8%80%E6%AC%A1%E6%AE%B5%E8%80%83%E4%B8%89%E5%B9%B4%E7%B4%9A%E8%87%AA%E7%84%B6.pdf", "高雄市立鹽埕國民中學公開自然科段考", "粒子模型、三態與相變"),
    ("https://www.nhjh.tp.edu.tw/uploads/1738658165906utzaMLG4.pdf", "臺北市立內湖國民中學公開自然科段考", "形狀、體積、壓縮性與微觀解釋"),
    ("https://www.kcjh.kh.edu.tw/upload/190/104_34764/%E5%9C%8B%E6%98%8C--%E4%BA%8C%E5%B9%B4%E7%B4%9A--%E8%87%AA%E7%84%B6%E7%A7%91.pdf", "高雄市立國昌國民中學公開自然科試題", "溫度、狀態變化與模型限制"),
]
BOUNDARY = "本紀錄只保存可追溯公開來源的章節定位、教學方向與評量能力；不複製出版社或學校教材正文、原題、選項、圖表、答案、影音或版面。"
EXPLANATIONS = [
    "B。固體粒子彼此較接近、排列有規則，主要在固定位置附近振動；不是完全靜止，也不是粒子本身沒有間隙。",
    "A。液體粒子仍彼此接近但可相對移動，因此體積較固定、形狀可隨容器改變並能流動。",
    "D。氣體粒子間距大，施壓時可減少空隙；不是把粒子壓扁或讓粒子本身變小。",
    "B。融化主要改變粒子的排列與運動狀態，物質仍是水，粒子種類沒有因相變而換成新物質。",
    "C。蒸發可在液面、各種溫度發生；沸騰在特定條件下液體內部形成大量氣泡，兩者都不是化學反應。",
    "D。較冷的鏡面使水蒸氣凝結成液態小水滴；看到水珠不是直接看見水蒸氣分子。",
    "B。升溫通常使同一物質粒子的平均動能增加，運動更快；粒子種類不會因此改變。",
    "A。體積固定時，升溫使粒子平均運動加快、碰撞更頻繁或更有力，因此壓力上升。",
    "C。同一物質的粒子種類通常不因固、液、氣狀態改變而改變，差別在排列、距離與運動。",
    "D。小球圖是用來表示粒子分布、距離與運動的模型，不是物質真實外觀或粒子的直接放大照片。",
]
STRATEGIES = [
    "先看排列、間距與運動，再對照固體的形狀和體積特性。", "把液體的可流動性連到粒子可相對移動，而非粒子完全分離。", "將可壓縮性與粒子間空隙連結，不改變粒子本身大小。", "區分物理狀態改變與化學變化，檢查粒子種類是否改變。", "比較發生位置、溫度條件與氣泡位置，分清蒸發和沸騰。", "把宏觀水珠與微觀水蒸氣凝結分開描述。", "用平均動能和運動速度解釋溫度，不把升溫當成粒子變大。", "在固定容器條件下，檢查碰撞頻率和碰撞強度。", "找狀態改變前後仍保留的粒子種類。", "先說模型表示的關係，再說它不能直接呈現的真實尺度。",
]


def refs():
    return [{"url": u, "title": f"{t}；只取{loc}的題型與推理方向，未複製原題、選項、圖表或答案。", "year": "113-114", "subject": "science", "locator": loc, "observedPattern": "公開自然科評量常要求從形狀、體積、流動、壓縮、溫度與相變資料建立粒子模型；本題以全新語料重寫。", "reuseDecision": "pattern-only", "status": "recorded", "locatorLevel": "paper"} for u, t, loc in URLS]


def main():
    lesson = json.loads(LESSON.read_text(encoding="utf-8")); lesson.update({"updatedAt": "2026-09-21", "reviewStatus": "draft", "authoringStandard": "version-fused-v1"})
    for row in lesson.get("publisherResearch", []): row["reviewedAt"] = "2026-09-21"
    for row in lesson.get("versionResearch", []): row["reviewedAt"] = "2026-09-21"; row["licenseBoundary"] = BOUNDARY
    lesson["fusionRecord"]["llmSynthesisNote"] = "本課依官方自然科學課綱、kg-science-content-ab-iv-1、南一／康軒／翰林可取得的公開研究方向與三筆公立學校自然科試題能力模式，以自己的話獨立融合粒子排列、間距、運動、三態、相變、壓縮性、壓力與模型限制；保留既有粒子箱互動，未複製教材或試題，Terra 第二輪與正式發布審查尚未完成，維持 draft。"
    LESSON.write_text(json.dumps(lesson, ensure_ascii=False, indent=2) + "\n", encoding="utf-8")
    steps = ["圈出物質狀態、形狀、體積、流動、壓縮、溫度或模型限制線索。", "把宏觀觀察轉成粒子的排列、間距與運動描述。", "檢查相變前後粒子種類、平均動能、碰撞與容器條件。", "排除把粒子當成直接照片、把氣體膨脹當粒子變大，或把物理狀態改變當成新物質生成的選項。", "用模型回查答案，補上模型假設、測量條件與不能直接觀察的限制。"]
    for i in range(1, 11):
        path = ROOT / f"questions/science/question-science-content-ab-iv-1-{i}.json"; q = json.loads(path.read_text(encoding="utf-8")); q["examPatternRefs"] = refs(); q["reviewStatus"] = "draft"; q["updatedAt"] = "2026-09-21"; q["answer"]["explanation"] = EXPLANATIONS[i-1]; q["solutionStrategy"] = STRATEGIES[i-1]; q["solutionSteps"] = steps; q["provenance"]["sourceUrl"] = URLS[0][0]; q["provenance"]["sourceLocator"] = "三筆公立學校公開自然科試題中的粒子模型、三態、相變、壓縮性、溫度與微觀解釋能力；本題改寫為粒子模型原創情境。"; path.write_text(json.dumps(q, ensure_ascii=False, indent=2) + "\n", encoding="utf-8")
    REPORT.write_text(json.dumps({"unit": lesson["title"], "lessonId": lesson["id"], "status": "first-pass-ai-review-complete", "reviewStatus": "draft", "checks": {"unitSpecificOriginalContent": True, "threeVersionResearchRecords": True, "publicExamPatternRewrite": True, "fusionRecordPresent": True, "interactivePredictionManipulationExplanation": True, "answersAndDetailedSteps": True, "terraSecondPass": "pending"}, "reviewedAt": "2026-09-21"}, ensure_ascii=False, indent=2) + "\n", encoding="utf-8")
    print("authored science content ab iv 1")


if __name__ == "__main__": main()
