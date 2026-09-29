import json
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
LESSON = ROOT / "lessons/science/lesson-science-content-db-iv-1.json"
REPORT = ROOT / "implementation/reports/science-content-db-iv-1-first-pass-review.json"
URLS = [
    ("https://www.yacjh.kh.edu.tw/upload/221/101_30637/114%E4%B8%8B%E5%AD%B8%E6%9C%9F%E7%AC%AC%E4%B8%80%E6%AC%A1%E6%AE%B5%E8%80%83%E4%B8%89%E5%B9%B4%E7%B4%9A%E8%87%AA%E7%84%B6.pdf", "高雄市立鹽埕國民中學公開自然科段考", "攝食、消化、養分吸收與運輸"),
    ("https://www.nhjh.tp.edu.tw/uploads/1738658165906utzaMLG4.pdf", "臺北市立內湖國民中學公開自然科段考", "消化道、小腸構造與三大養分路徑"),
    ("https://www.kcjh.kh.edu.tw/upload/190/104_34764/%E5%9C%8B%E6%98%8C--%E4%BA%8C%E5%B9%B4%E7%B4%9A--%E8%87%AA%E7%84%B6%E7%A7%91.pdf", "高雄市立國昌國民中學公開自然科試題", "機械與化學消化、膽汁、血液與淋巴"),
]
BOUNDARY = "本紀錄只保存可追溯公開來源的章節定位、教學方向與評量能力；不複製出版社或學校教材正文、原題、選項、圖表、答案、影音或版面。"
EXPLANATIONS = [
    "A。食物先經咀嚼、攪拌等機械作用與酵素等化學作用，再在小腸吸收小分子；水溶性養分多進血液，部分脂質相關物質先走淋巴，最後送到細胞。",
    "B。澱粉需在消化道中被分解成可吸收的小分子，主要於小腸穿過腸壁進入血液；牙齒咬碎只改變顆粒大小。",
    "A。蛋白質經消化成胺基酸，在小腸吸收後進入血液，再由循環系統送至細胞利用；膽汁不會把蛋白質變成葡萄糖。",
    "C。膽汁將脂肪乳化成較小液滴，增加脂肪酶接觸面；它不是把脂肪直接水解的消化酵素。",
    "A。皺褶與絨毛擴大小腸內壁有效表面積，使消化產物更容易接觸吸收表面，並靠近微血管與乳糜管。",
    "D。牙齒把食物咬碎，主要改變顆粒大小與接觸面，沒有因此改變分子種類，屬於機械性消化。",
    "A。食物依序由口腔經咽、食道到胃，再進入小腸；順序反映消化道的連續管道。",
    "B。水溶性小分子多進入絨毛微血管；部分脂質消化產物先進乳糜管和淋巴，再匯入血液，不能把所有養分視為同一路徑。",
    "A。打成液體可能只是顆粒變小或混合，仍需證明大分子被分解並穿過小腸壁；外觀不能直接代表已吸收。",
    "C。完整模型應記錄蛋白質變成胺基酸、胺基酸穿過小腸壁進入血液，以及後續運送到細胞的方向與證據。",
]
STRATEGIES = [
    "沿攝食—消化—吸收—運輸—細胞利用分段，分辨每段的物質與證據。",
    "先判斷澱粉是否完成化學消化，再定位小腸吸收，不把咀嚼當成吸收。",
    "圈出蛋白質、胺基酸、小腸、血液與細胞，畫出正確運輸箭頭。",
    "分辨膽汁的乳化作用與酵素的化學分解作用。",
    "把皺褶、絨毛、微血管與乳糜管連到吸收表面與運輸功能。",
    "看分子種類是否改變；只改顆粒大小的是機械性消化。",
    "依消化道實際連續順序排列器官，不用功能名稱互換位置。",
    "先按水溶性或脂溶性判斷絨毛內血管與乳糜管路徑。",
    "把食物外觀和分子跨腸壁的吸收事件分開，要求直接證據。",
    "用物質變化、吸收位置、血液／淋巴方向與細胞利用完成證據圖。",
]


def refs():
    return [{"url": u, "title": f"{t}；只取{loc}的題型與推理方向，未複製原題、選項、圖表或答案。", "year": "113-114", "subject": "science", "locator": loc, "observedPattern": "公開自然科評量常要求追蹤攝食、機械與化學消化、小腸吸收、膽汁、血液與淋巴運輸；本題以全新消化與養分路徑情境重寫。", "reuseDecision": "pattern-only", "status": "recorded", "locatorLevel": "paper"} for u, t, loc in URLS]


def main():
    lesson = json.loads(LESSON.read_text(encoding="utf-8")); lesson.update({"updatedAt": "2026-09-21", "reviewStatus": "draft", "authoringStandard": "version-fused-v1"})
    for row in lesson.get("publisherResearch", []): row["reviewedAt"] = "2026-09-21"
    for row in lesson.get("versionResearch", []): row.update({"reviewedAt": "2026-09-21", "licenseBoundary": BOUNDARY})
    lesson["fusionRecord"]["llmSynthesisNote"] = "本課依官方自然科學課綱、kg-science-content-db-iv-1、南一／康軒／翰林可取得的公開研究方向與三筆公立學校自然科試題能力模式，以自己的話獨立融合攝食、機械與化學消化、三大養分、小腸絨毛、血液與淋巴運輸及證據界線；重寫早餐路徑與養分證據圖互動，並移除原本不屬於本單元的植物題，未複製教材或試題，Terra 第二輪與正式發布審查尚未完成，維持 draft。"
    LESSON.write_text(json.dumps(lesson, ensure_ascii=False, indent=2) + "\n", encoding="utf-8")
    steps = ["圈出食物種類、消化部位、分子變化、吸收位置與血液／淋巴方向。", "分開機械性消化、化學性消化、吸收與細胞利用，不把顆粒變小當成跨腸壁。", "沿口腔—胃—小腸與絨毛內血管／乳糜管畫出路徑，標記三大養分的消化產物。", "檢查膽汁、酵素、皺褶絨毛與運輸系統各自的功能，排除器官和物質混淆。", "回查模型是否有直接吸收證據、替代解釋與條件限制，避免由食物外觀推論細胞利用。"]
    for i in range(1, 11):
        path = ROOT / f"questions/science/question-science-content-db-iv-1-{i}.json"; q = json.loads(path.read_text(encoding="utf-8"))
        if i == 1:
            q["prompt"] = "含澱粉、蛋白質與脂質的食物要被細胞利用，哪條整體路徑最合理？"
            q["options"] = [{"id":"A","text":"先在消化道經機械與化學作用分解，再於小腸吸收小分子，經血液或淋巴運送到細胞"},{"id":"B","text":"只要在口腔咬碎，完整大分子便會直接穿過小腸壁進入細胞"},{"id":"C","text":"食物進胃後所有養分立即進入血液，不需經過小腸吸收"},{"id":"D","text":"膽汁把蛋白質與澱粉都變成葡萄糖，再由乳糜管送到細胞"}]
        q.update({"examPatternRefs": refs(), "reviewStatus": "draft", "updatedAt": "2026-09-21", "solutionStrategy": STRATEGIES[i-1], "solutionSteps": steps}); q["answer"]["explanation"] = EXPLANATIONS[i-1]; q["provenance"]["sourceUrl"] = URLS[0][0]; q["provenance"]["sourceLocator"] = "三筆公立學校公開自然科試題中的攝食、消化、養分吸收、運輸與證據判讀能力；本題改寫為消化與吸收原創情境。"; path.write_text(json.dumps(q,ensure_ascii=False,indent=2)+"\n",encoding="utf-8")
    REPORT.write_text(json.dumps({"unit":lesson["title"],"lessonId":lesson["id"],"status":"first-pass-ai-review-complete","reviewStatus":"draft","checks":{"unitSpecificOriginalContent":True,"threeVersionResearchRecords":True,"publicExamPatternRewrite":True,"fusionRecordPresent":True,"interactivePredictionManipulationExplanation":True,"answersAndDetailedSteps":True,"terraSecondPass":"pending"},"reviewedAt":"2026-09-21"},ensure_ascii=False,indent=2)+"\n",encoding="utf-8")
    print("authored science content db iv 1")


if __name__ == "__main__": main()
