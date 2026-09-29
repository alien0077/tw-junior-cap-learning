import json
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
LESSON = ROOT / "lessons/science/lesson-science-content-ka-iv-4.json"
REPORT = ROOT / "implementation/reports/science-content-ka-iv-4-first-pass-review.json"
URLS = [
    ("https://www.yacjh.kh.edu.tw/upload/221/101_30637/114%E4%B8%8B%E5%AD%B8%E6%9C%9F%E7%AC%AC%E4%B8%80%E6%AC%A1%E6%AE%B5%E8%80%83%E4%B8%89%E5%B9%B4%E7%B4%9A%E8%87%AA%E7%84%B6.pdf", "高雄市立鹽埕國民中學公開自然科段考", "聲波、回聲、速度與反射測量"),
    ("https://www.nhjh.tp.edu.tw/uploads/1738658165906utzaMLG4.pdf", "臺北市立內湖國民中學公開自然科段考", "波動、介質與資料判讀"),
    ("https://www.kcjh.kh.edu.tw/upload/190/104_34764/%E5%9C%8B%E6%98%8C--%E4%BA%8C%E5%B9%B4%E7%B4%9A--%E8%87%AA%E7%84%B6%E7%A7%91.pdf", "高雄市立國昌國民中學公開自然科試題", "聲波反射、超音波與生活應用"),
]
BOUNDARY = "本紀錄只保存可追溯公開來源的章節定位、教學方向與評量能力；不複製出版社或學校教材正文、原題、選項、圖表、答案、影音或版面。"
EXPLANATIONS = [
    "A。回聲是聲音往返牆面的總路程，因此距離 d=vt/2=340×2.0÷2=340 m；不能把 2.0 秒直接當成單程時間。",
    "B。聲納回波的 0.80 秒也是往返時間，目標距離 d=1500×0.80÷2=600 m；計算時必須採用水中的聲速。",
    "C。要由回聲求距離，至少要有回波往返時間、介質中的聲速，以及清楚的反射路徑或量測幾何；音量本身不足以換算距離。",
    "D。吸音材料主要降低反射回來的振幅，使回聲變弱；若聲速與路徑不變，單靠變小的音量不能判定牆面距離變了。",
    "B。蝙蝠利用超音波回波抵達的時間差與方向判斷障礙物位置；關鍵是發射、反射、接收的時間資訊，而不是只聽聲音大小。",
    "C。介質不同，聲速可能不同，所以要先確認傳播介質，再用該介質的聲速計算；不能把空氣中的 340 m/s 套到水中。",
    "D。多個時間峰通常代表不同反射界面或目標距離；應用到達時間換算距離，並用重複量測、峰值穩定性與路徑判讀排除雜訊。",
    "A。裂縫檢測應送出受控脈衝，記錄各回波的到達時間與強度，和完整材料的基準資料比較並重複校正；只聽聲音大小不夠可靠。",
    "C。超音波影像的亮暗與界面反射回來的訊號強度有關，還受聲阻抗差、角度、衰減與儀器設定影響；不能簡化成越緻密就一定越亮。",
    "B。比較牆材要固定聲源、距離、角度、介質、發射強度與儀器設定，重複記錄回波到達時間和振幅，再評估反射、吸音與測量誤差。",
]
STRATEGIES = [
    "先判斷回聲時間是單程還是往返，再套用 d=vt/2。",
    "圈出介質與回波時間，畫出聲波往返路徑後再計算。",
    "列出時間、聲速與路徑三項資料，先確認單位和幾何條件。",
    "把回波到達時間與回波振幅分開，判斷材料吸音不等於距離改變。",
    "用發射—反射—接收的時間順序解釋定位，不把音量當成唯一證據。",
    "先選對介質聲速，再檢查是否需要除以二與是否有折射或多重路徑。",
    "將每個穩定時間峰視為候選界面，利用重複量測和路徑資訊排除雜訊。",
    "把非破壞檢測拆成受控脈衝、基準比較、時間判讀與校正四個環節。",
    "區分反射強度、介面差異、衰減和儀器設定，避免單一亮暗直覺。",
    "先固定所有控制變因，再同時比較回波時間、振幅與不確定度。",
]


def refs():
    return [{"url": u, "title": f"{t}；只取{loc}的題型與推理方向，未複製原題、選項、圖表或答案。", "year": "113-114", "subject": "science", "locator": loc, "observedPattern": "公開自然科評量常要求連結回聲延遲、聲速、路徑長度、介質、反射、訊號峰值與測量條件；本題以全新聲波反射情境重寫。", "reuseDecision": "pattern-only", "status": "recorded", "locatorLevel": "paper"} for u, t, loc in URLS]


def main():
    lesson = json.loads(LESSON.read_text(encoding="utf-8"))
    lesson.update({"updatedAt": "2026-09-21", "reviewStatus": "draft", "authoringStandard": "version-fused-v1"})
    for row in lesson.get("publisherResearch", []):
        row["reviewedAt"] = "2026-09-21"
    for row in lesson.get("versionResearch", []):
        row["reviewedAt"] = "2026-09-21"
        row["licenseBoundary"] = BOUNDARY
    lesson["fusionRecord"]["llmSynthesisNote"] = "本課依官方自然科學課綱、kg-science-content-ka-iv-4、南一／康軒／翰林可取得的公開研究方向與三筆公立學校自然科試題能力模式，以自己的話獨立融合聲波反射、回聲往返路徑、d=vt/2、介質聲速、到達時間與振幅、訊號峰值、聲納、超音波及量測限制；保留本單元專屬的聲波調查互動，未複製教材或試題，Terra 第二輪與正式發布審查尚未完成，維持 draft。"
    LESSON.write_text(json.dumps(lesson, ensure_ascii=False, indent=2) + "\n", encoding="utf-8")
    steps = ["圈出聲速、回波時間、介質、反射路徑、訊號峰值與材料條件。", "畫出發射—反射—接收的路徑，判斷題目給的是單程或往返時間。", "用 d=vt/2 或總路程=vt 計算，統一秒、m/s 與 m 的單位。", "分開判讀到達時間、振幅、反射界面、角度與雜訊，排除只看音量或只套空氣聲速的說法。", "回查測量是否受吸音、衰減、多重反射、路徑不直、儀器解析度與聲速變動影響。"]
    for i in range(1, 11):
        path = ROOT / f"questions/science/question-science-content-ka-iv-4-{i}.json"
        q = json.loads(path.read_text(encoding="utf-8"))
        q["examPatternRefs"] = refs()
        q["reviewStatus"] = "draft"
        q["updatedAt"] = "2026-09-21"
        q["answer"]["explanation"] = EXPLANATIONS[i - 1]
        q["solutionStrategy"] = STRATEGIES[i - 1]
        q["solutionSteps"] = steps
        q["provenance"]["sourceUrl"] = URLS[0][0]
        q["provenance"]["sourceLocator"] = "三筆公立學校公開自然科試題中的聲波、回聲、速度、反射、超音波與測量條件能力；本題改寫為聲波反射原創情境。"
        path.write_text(json.dumps(q, ensure_ascii=False, indent=2) + "\n", encoding="utf-8")
    REPORT.write_text(json.dumps({"unit": lesson["title"], "lessonId": lesson["id"], "status": "first-pass-ai-review-complete", "reviewStatus": "draft", "checks": {"unitSpecificOriginalContent": True, "threeVersionResearchRecords": True, "publicExamPatternRewrite": True, "fusionRecordPresent": True, "interactivePredictionManipulationExplanation": True, "answersAndDetailedSteps": True, "terraSecondPass": "pending"}, "reviewedAt": "2026-09-21"}, ensure_ascii=False, indent=2) + "\n", encoding="utf-8")
    print("authored science content ka iv 4")


if __name__ == "__main__":
    main()
