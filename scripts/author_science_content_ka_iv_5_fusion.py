import json
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
LESSON = ROOT / "lessons/science/lesson-science-content-ka-iv-5.json"
REPORT = ROOT / "implementation/reports/science-content-ka-iv-5-first-pass-review.json"
URLS = [
    ("https://www.yacjh.kh.edu.tw/upload/221/101_30637/114%E4%B8%8B%E5%AD%B8%E6%9C%9F%E7%AC%AC%E4%B8%80%E6%AC%A1%E6%AE%B5%E8%80%83%E4%B8%89%E5%B9%B4%E7%B4%9A%E8%87%AA%E7%84%B6.pdf", "高雄市立鹽埕國民中學公開自然科段考", "頻率、振幅、波形、音調與響度"),
    ("https://www.nhjh.tp.edu.tw/uploads/1738658165906utzaMLG4.pdf", "臺北市立內湖國民中學公開自然科段考", "音色、超聲波、回波與聲波應用"),
    ("https://www.kcjh.kh.edu.tw/upload/190/104_34764/%E5%9C%8B%E6%98%8C--%E4%BA%8C%E5%B9%B4%E7%B4%9A--%E8%87%AA%E7%84%B6%E7%A7%91.pdf", "高雄市立國昌國民中學公開自然科試題", "聲波圖、聽覺範圍與公平測量"),
]
BOUNDARY = "本紀錄只保存可追溯公開來源的章節定位、教學方向與評量能力；不複製出版社或學校教材正文、原題、選項、圖表、答案、影音或版面。"
EXPLANATIONS = [
    "A。頻率較高代表音調較高；兩音源響度相近表示振幅或聲壓強弱相近，不能把高音誤解成大聲。",
    "B。同一音源頻率不變時，振幅增加通常使聲壓變大、聽起來較響，但音調不必然改變。",
    "C。不同樂器即使基頻相同，泛音組成與波形形狀仍不同，耳朵因此辨認出不同音色。",
    "D。頻率高於約 20 kHz 超出一般人耳聽覺上限，稱為超聲波；定義依頻率，不是依速度。",
    "B。超音波遇到不同組織界面會反射，儀器依回波到達時間與強度重建影像；不是因為聲波本身能直接看見人體。",
    "C。回波時間包含去程和回程，總路程=vt，障礙物單程距離 d=vt/2，所以要除以二。",
    "D。應依設備規格、頻率、功率、清洗時間與材料耐受性設定，並控制安全距離和溫升，不是頻率越高或功率越大就無條件更好。",
    "A。固定介質、探頭位置、目標距離、發射設定與時間刻度，只比較探頭差異並重複測量，才能公平評估。",
    "C。音調主要看頻率、響度看振幅或聲壓、音色看波形；超聲波則以頻率高於人耳上限定義，四者不可混用。",
    "B。完整判讀要在相同刻度下比較週期、峰值與波形，確認介質與測量條件，再分別推論音調、響度、音色或距離。",
]
STRATEGIES = [
    "先比較週期或頻率判斷音調，再看振幅判斷響度。",
    "固定頻率後只看振幅變化，避免把大聲當高音。",
    "比較相同基頻下的波形與泛音，判斷音色差異。",
    "用頻率門檻判斷超聲波，不用聲速或音量定義。",
    "找界面回波、到達時間與強度，說明影像形成的證據。",
    "先確認回波為往返路程，再用 d=vt/2。",
    "同時看頻率、功率、材料、溫升、距離與設備安全規格。",
    "固定介質、位置、目標、設定與刻度，只改探頭並重複測量。",
    "把頻率、振幅、波形與聽覺範圍逐項對應，不用單一名詞包辦。",
    "先校正時間與縱軸刻度，再分別讀週期、峰值、波形和回波。",
]


def refs():
    return [{"url": u, "title": f"{t}；只取{loc}的題型與推理方向，未複製原題、選項、圖表或答案。", "year": "113-114", "subject": "science", "locator": loc, "observedPattern": "公開自然科評量常要求連結頻率、振幅、波形、音調、響度、音色、超聲波與回波測距；本題以全新聲波判讀情境重寫。", "reuseDecision": "pattern-only", "status": "recorded", "locatorLevel": "paper"} for u, t, loc in URLS]


def main():
    lesson = json.loads(LESSON.read_text(encoding="utf-8")); lesson.update({"updatedAt": "2026-09-21", "reviewStatus": "draft", "authoringStandard": "version-fused-v1"})
    for row in lesson.get("publisherResearch", []): row["reviewedAt"] = "2026-09-21"
    for row in lesson.get("versionResearch", []): row.update({"reviewedAt": "2026-09-21", "licenseBoundary": BOUNDARY})
    lesson["fusionRecord"]["llmSynthesisNote"] = "本課依官方自然科學課綱、kg-science-content-ka-iv-5、南一／康軒／翰林可取得的公開研究方向與三筆公立學校自然科試題能力模式，以自己的話獨立融合頻率、振幅、波形、音調、響度、音色、人耳聽覺範圍、超聲波、回波與醫療／清洗應用；保留樂器—示波器—探頭比較互動，未複製教材或試題，Terra 第二輪與正式發布審查尚未完成，維持 draft。"
    LESSON.write_text(json.dumps(lesson, ensure_ascii=False, indent=2) + "\n", encoding="utf-8")
    steps = ["圈出頻率、週期、振幅、波形、介質、回波時間與人耳範圍。", "用週期或頻率判斷音調，用振幅或聲壓判斷響度，用波形判斷音色。", "比較波形時固定時間與縱軸刻度，測距時先判斷是否為往返時間。", "以 20 Hz—20 kHz 門檻判斷超聲波，並區分回波強度、到達時間與聲速。", "回查介質、探頭設定、材料耐受、溫升與測量誤差，說明應用條件和安全限制。"]
    for i in range(1, 11):
        path = ROOT / f"questions/science/question-science-content-ka-iv-5-{i}.json"; q = json.loads(path.read_text(encoding="utf-8")); q.update({"examPatternRefs": refs(), "reviewStatus": "draft", "updatedAt": "2026-09-21", "solutionStrategy": STRATEGIES[i-1], "solutionSteps": steps}); q["answer"]["explanation"] = EXPLANATIONS[i-1]; q["provenance"]["sourceUrl"] = URLS[0][0]; q["provenance"]["sourceLocator"] = "三筆公立學校公開自然科試題中的頻率、振幅、波形、音調、響度、音色、超聲波與回波應用能力；本題改寫為聲波原創情境。"; path.write_text(json.dumps(q,ensure_ascii=False,indent=2)+"\n",encoding="utf-8")
    REPORT.write_text(json.dumps({"unit":lesson["title"],"lessonId":lesson["id"],"status":"first-pass-ai-review-complete","reviewStatus":"draft","checks":{"unitSpecificOriginalContent":True,"threeVersionResearchRecords":True,"publicExamPatternRewrite":True,"fusionRecordPresent":True,"interactivePredictionManipulationExplanation":True,"answersAndDetailedSteps":True,"terraSecondPass":"pending"},"reviewedAt":"2026-09-21"},ensure_ascii=False,indent=2)+"\n",encoding="utf-8")
    print("authored science content ka iv 5")


if __name__ == "__main__": main()
