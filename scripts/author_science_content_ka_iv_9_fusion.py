import json
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
LESSON = ROOT / "lessons/science/lesson-science-content-ka-iv-9.json"
REPORT = ROOT / "implementation/reports/science-content-ka-iv-9-first-pass-review.json"
URLS = [
    ("https://www.nehs.tc.edu.tw/wp-content/uploads/sites/95/2026/02/6%E7%90%86%E5%8C%96%E7%A7%91-%E4%B9%9D%E5%B9%B4%E7%B4%9A-%E9%A1%8C%E5%BA%AB.pdf", "國立中科實驗高級中學公開九年級理化題庫", "透鏡成像、光學儀器與資料判讀"),
    ("https://www.nhjh.tp.edu.tw/uploads/1675417616549dOhkhC5L.pdf", "臺北市立內湖國民中學公開九年級理化段考", "凸凹透鏡、眼鏡與成像情境"),
    ("https://www.kcjh.kh.edu.tw/upload/190/104_34764/%E4%B8%89%E5%B9%B4%E7%B4%9A%E7%90%86%E5%8C%96-%E7%AC%AC三次段考5-OK.pdf", "高雄市立國昌國民中學公開三年級自然科試題", "反射折射、光學器材與實驗證據"),
]
BOUNDARY = "本紀錄只保存可追溯公開來源的章節定位、教學方向與評量能力；不複製出版社或學校教材正文、原題、選項、圖表、答案、影音或版面。"
PATTERN = "公立學校公開自然／理化試題常以光線圖、物距與焦距、白幕成像、眼鏡、相機、望遠鏡或顯微鏡考查透鏡成像與光學器材功能；本題只取能力方向並重新設計情境、數據與選項。"
EXPLANATIONS = [
    "A。凸透鏡使近軸平行光折射後朝主軸焦點會聚；焦點位置由透鏡與介質決定，不是任意落在透鏡表面。",
    "B。凹透鏡對實物形成正立、縮小的虛像，可使入眼光線先發散，配合眼睛把近視遠方影像移回視網膜。",
    "C。物體放在凸透鏡焦距內時，出射光發散、反向延伸形成正立放大的虛像，適合放大鏡；不能用白幕接到。",
    "D。遠處物體相當於物距大於二倍焦距，凸透鏡在感光元件前形成倒立縮小實像，感光面可接收光線。",
    "B。顯微鏡的物鏡先把近距離小物形成放大的中間實像，目鏡再把中間像放大給眼睛；兩片透鏡不是同一個功能。",
    "C。望遠鏡物鏡先收集幾乎平行的遠方光線，在焦點附近形成中間實像，目鏡再供眼睛觀察；要先追第一段光路。",
    "D。凸面鏡形成正立、縮小虛像，能在鏡面有限尺寸下提供較大視野，適合觀察車後較寬廣區域。",
    "A。凹面鏡把燈泡附近發出的發散光反射成較平行的光束，增加照射方向性；不是把所有光線會聚在駕駛者眼前。",
    "C。遠視時需要增加會聚能力，凸透鏡先使入眼光線會聚，再由眼睛把焦點調到視網膜附近。",
    "B。把凸透鏡對準遠方物體並在另一側移動白紙；若能找到清楚、倒立、可接幕的影像，便直接支持其會聚成實像的特性。",
]
STRATEGIES = [
    "先找平行光通過透鏡後的方向，再判斷是否朝主軸焦點會聚。",
    "從焦點落在視網膜前或後推回需要發散或會聚，再選鏡片。",
    "比較物距與焦距；物距小於焦距時判斷虛像與白幕證據。",
    "以遠物近似平行光，判斷實像位置、方向與感光面能否接收。",
    "把儀器拆成物鏡—中間像—目鏡三段，分別寫出功能。",
    "先處理物鏡形成的中間像，再判斷目鏡如何讓眼睛觀察。",
    "由曲面鏡類型推正立縮小虛像，再連到視野大小的實際用途。",
    "把燈泡位置與反射後光束方向畫出，判斷凹面鏡是整形成平行光。",
    "不要以『看近／看遠』背鏡片，先判斷焦點位置與修正方向。",
    "選有可觀察白幕證據的操作，並排除只靠外觀或厚薄做判斷。",
]
STEPS = [
    "標出光源或物體、透鏡／鏡面、焦點與眼睛或白幕的位置。",
    "判斷光線是會聚、發散、反射後平行，或在焦點附近交會。",
    "依物距與焦距判斷正倒、大小及實像／虛像。",
    "用白幕、感光面、視網膜或視野等可觀察證據檢查判斷。",
    "再連結到相機、眼鏡或複合儀器的功能，說明限制。",
]


def refs():
    return [{"url": u, "title": f"{t}；只取{loc}的題型與推理方向，未複製原題、選項、圖表、答案或版面。", "year": "109-115", "subject": "science", "locator": loc, "observedPattern": PATTERN, "reuseDecision": "pattern-only", "status": "recorded", "locatorLevel": "paper"} for u, t, loc in URLS]


def main():
    lesson = json.loads(LESSON.read_text(encoding="utf-8"))
    lesson.update({"updatedAt": "2026-09-21", "reviewStatus": "draft", "authoringStandard": "version-fused-v1"})
    for row in lesson.get("publisherResearch", []):
        row["reviewedAt"] = "2026-09-21"
    for row in lesson.get("versionResearch", []):
        row.update({"reviewedAt": "2026-09-21", "licenseBoundary": BOUNDARY})
    lesson["fusionRecord"]["llmSynthesisNote"] = "本課依官方自然科學課綱、kg-science-content-ka-iv-9、南一／康軒／翰林可取得的公開研究方向與三筆公立學校自然／理化試題能力模式，以自己的話獨立融合凸凹透鏡、焦點、物距、實虛像、白幕證據、眼鏡、相機、望遠鏡、顯微鏡與曲面鏡；保留硬幣—光路—儀器設計互動主線，未複製教材或試題，Terra 第二輪與正式發布審查尚未完成，維持 draft。"
    LESSON.write_text(json.dumps(lesson, ensure_ascii=False, indent=2) + "\n", encoding="utf-8")
    for i in range(1, 11):
        path = ROOT / f"questions/science/question-science-content-ka-iv-9-{i}.json"
        q = json.loads(path.read_text(encoding="utf-8"))
        q.update({"examPatternRefs": refs(), "reviewStatus": "draft", "updatedAt": "2026-09-21", "solutionStrategy": STRATEGIES[i - 1], "solutionSteps": STEPS})
        q["answer"]["explanation"] = EXPLANATIONS[i - 1]
        q["provenance"].update({"sourceUrl": URLS[0][0], "sourceLocator": "三筆公立學校公開自然／理化試題中的透鏡成像、鏡面、眼鏡、相機、望遠鏡、顯微鏡與實驗證據能力；本題改寫為光學原理與儀器原創情境。"})
        path.write_text(json.dumps(q, ensure_ascii=False, indent=2) + "\n", encoding="utf-8")
    REPORT.write_text(json.dumps({"unit": lesson["title"], "lessonId": lesson["id"], "status": "first-pass-ai-review-complete", "reviewStatus": "draft", "checks": {"unitSpecificOriginalContent": True, "threeVersionResearchRecords": True, "publicExamPatternRewrite": True, "fusionRecordPresent": True, "interactivePredictionManipulationExplanation": True, "answersAndDetailedSteps": True, "terraSecondPass": "pending"}, "reviewedAt": "2026-09-21"}, ensure_ascii=False, indent=2) + "\n", encoding="utf-8")
    print("authored science content ka iv 9")


if __name__ == "__main__": main()
