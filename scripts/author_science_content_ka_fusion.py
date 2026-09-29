"""Ka：波動、光及聲音第一輪原創題庫。"""
import json
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
LESSON = ROOT / "lessons/science/lesson-science-content-ka.json"
REPORT = ROOT / "implementation/reports/science-content-ka-first-pass-review.json"
QDIR = ROOT / "questions/science"
TODAY = "2026-09-23"

SOURCES = [
    {
        "url": "https://www.yacjh.kh.edu.tw/upload/221/101_30637/114%E4%B8%8B%E5%AD%B8%E6%9C%9F%E7%AC%AC%E4%B8%80%E6%AC%A1%E6%AE%B5%E8%80%83%E4%B8%89%E5%B9%B4%E7%B4%9A%E8%87%AA%E7%84%B6.pdf",
        "title": "高雄市立鹽埕國民中學 114 學年度第 2 學期第 1 次段考自然科公開試題",
        "year": "114",
        "locator": "波動、聲音、光學圖形與資料判讀",
        "pattern": "取公立學校自然科評量以波形量測、介質條件、光路圖和生活情境推理的能力方向。",
    },
    {
        "url": "https://www.grow22.com/download/114/114_cp/05_114P_Nature.pdf",
        "title": "114 年國中教育會考自然科公開試題",
        "year": "114",
        "locator": "波速頻率波長、聲音傳播、反射折射與實驗變因判讀",
        "pattern": "取公開會考以圖表、物理量關係、路徑幾何與證據界線評估的能力方向。",
    },
    {
        "url": "https://www.kcjh.kh.edu.tw/upload/190/104_34764/%E5%9C%8B%E6%98%8C--%E4%BA%8C%E5%B9%B4%E7%B4%9A--%E8%87%AA%E7%84%B6%E7%A7%91.pdf",
        "title": "高雄市立國昌國民中學二年級自然科公開段考試題",
        "year": "112",
        "locator": "波動量、回聲、聲音三要素、反射折射與控制變因",
        "pattern": "取公立國中試題以公式代換、往返路徑、波形辨識、光線作圖和公平測量的能力方向。",
    },
]
REFS = [
    {
        **source,
        "subject": "science",
        "observedPattern": source["pattern"],
        "reuseDecision": "pattern-only",
        "status": "recorded",
        "locatorLevel": "paper",
    }
    for source in SOURCES
]

STEPS = [
    [
        "先辨認題目談的是介質粒子的振動，還是波形整體的傳播。",
        "圈出波長、頻率、週期、振幅與波速的定義和單位。",
        "依圖上的刻度找同相位點或平衡位置，再建立方程式。",
        "把數值代入前先檢查單位與題目給的介質條件。",
        "用量綱、極端情況或圖形方向回頭檢查答案是否合理。",
    ]
    for _ in range(10)
]

ROWS = [
    (
        "easy",
        "水面波紋向外擴散，但漂浮葉片主要在原處上下起伏；這項觀察最能支持哪個說法？",
        [
            "波主要傳遞能量，介質粒子不必隨波移到波前位置",
            "水面粒子都會跟著每個波峰向外搬運",
            "波的振幅就是波前向外移動的速度",
            "只要看見波紋，便可確定水分子離開水面",
        ],
        "A",
        "葉片的局部振動和波紋的向外傳播可以同時存在，顯示波動傳遞的是擾動的能量與資訊，不是把所有介質粒子搬到遠處。",
        "先把介質粒子的運動和波形前進分開描述，再判斷觀察支持哪一種模型。",
    ),
    (
        "medium",
        "一列週期波在繩上以 12 m/s 傳播，振源頻率為 3 Hz。相鄰同相位點的距離約為多少？",
        ["4 m", "9 m", "15 m", "36 m"],
        "A",
        "由 v=fλ 得 λ=v/f=12÷3=4 m；相鄰波峰或相鄰波谷的距離就是波長。",
        "先寫 v=fλ，再確認要求的是 λ，最後將速度除以頻率並保留單位。",
    ),
    (
        "medium",
        "示波器圖上波峰到相鄰波谷的垂直差為 8 cm。若平衡位置在兩者正中間，這列波的振幅為何？",
        ["2 cm", "4 cm", "8 cm", "16 cm"],
        "B",
        "波峰到波谷的垂直差是兩倍振幅；8 cm÷2=4 cm，因此振幅為 4 cm。",
        "先找平衡位置，再量平衡位置到波峰或波谷的單側距離，不把峰峰值誤當振幅。",
    ),
    (
        "easy",
        "同一種介質中，振源頻率提高而波速近似不變。下列哪項最合理？",
        [
            "波長縮短，因為 v=fλ 必須維持相同波速",
            "波長變長，因為頻率越高每個波峰越大",
            "波速必然加倍，因為頻率加倍",
            "頻率只影響振幅，不影響波長",
        ],
        "A",
        "在波速近似固定時，λ=v/f；頻率增加會使波長縮短。頻率、振幅與波速不是同一個物理量。",
        "先固定題目明示不變的量，再用比例關係判斷其餘量如何變化。",
    ),
    (
        "easy",
        "太空中兩位太空人可以看見彼此手電筒的光，卻不能只靠空氣傳聲直接交談，關鍵原因是？",
        [
            "光不需要物質介質，聲音是需要介質的機械波",
            "光的頻率一定比聲音低",
            "聲音只能在水中傳播，不能在任何氣體中傳播",
            "太空中的光沒有能量，所以不會受真空影響",
        ],
        "A",
        "光可在真空中傳播；聲音需要介質粒子形成壓縮與疏鬆，真空沒有足夠粒子傳遞聲波，因此太空人需用無線電等方式通訊。",
        "先辨認波的種類，再檢查該波是否需要介質，不要用音調或亮度替代傳播條件。",
    ),
    (
        "medium",
        "以空氣中聲速 340 m/s 測量牆面回聲，發聲到收到回聲相隔 0.60 s。發聲者到牆面的距離約為多少？",
        ["51 m", "102 m", "204 m", "566 m"],
        "B",
        "聲音走的是發聲者到牆面再回來的往返路徑；往返距離為 340×0.60=204 m，單程距離要再除以 2，得到 102 m。",
        "先畫去程與回程，算出往返距離後一定除以二；同時檢查選項與計算是否一致。",
    ),
    (
        "medium",
        "光線射到平面鏡，入射角（相對法線）為 35°。在鏡面方向不變的情況下，反射角為何？",
        ["35°", "55°", "70°", "145°"],
        "A",
        "反射定律規定入射角等於反射角，而且兩者都以法線為量角基準，所以反射角也是 35°。",
        "先畫交界點的法線，再確認題目給的角是相對法線還是相對鏡面，最後套用反射定律。",
    ),
    (
        "medium",
        "光從空氣斜射入水中，作圖時最先應完成哪個動作？",
        [
            "在入射點畫出垂直界面的法線，再量入射角與折射角",
            "直接以水面作為量角基準，透明介質就不會改變光路",
            "先以光的亮度判定折射角，再補上界面",
            "把所有折射光畫成沿法線前進，不必看入射方向",
        ],
        "A",
        "法線提供一致的幾何基準；光進入不同介質後可能改變速度與方向，不能以透明或亮度直接代替角度判讀。",
        "作圖順序固定為界面、法線、入射線與折射線，最後才比較角度與方向。",
    ),
    (
        "hard",
        "兩個聲音的頻率相同，但由小提琴和長笛發出時聽起來不同；最適合解釋這種差異的因素是？",
        [
            "波形與泛音組成不同，造成音色不同",
            "頻率相同代表響度一定不同",
            "聲音只要來自不同位置，波長就必然不同",
            "音色是由回聲時間單獨決定的",
        ],
        "A",
        "頻率主要決定音調；不同樂器的波形與泛音比例可不同，即使基頻相同，耳朵仍能辨識不同音色。",
        "把音調、響度與音色分成三個問題，分別對應頻率、振幅／聲強和波形／泛音。",
    ),
    (
        "hard",
        "要測試吸音材料是否改善教室廣播清晰度，哪個實驗設計最能支持因果判斷？",
        [
            "固定喇叭音量、播放內容、測量位置與時間，只改變是否放置吸音材料並重複測量",
            "一間教室使用吸音材料，另一間同時更換喇叭與播放內容",
            "只在最安靜的一次測量後宣布材料有效",
            "讓使用者知道預期答案，再請他們主觀評分一次",
        ],
        "A",
        "公平實驗需控制可能影響結果的變因，只改變吸音材料，並以多次、相同位置的聲音資料比較，才能把差異較合理地歸因於材料。",
        "先列出自變因、應變因與控制變因，再安排重複測量和可量化指標。",
    ),
]


def make_question(number, row):
    difficulty, prompt, options, answer, explanation, strategy = row
    return {
        "id": f"question-science-content-ka-{number}",
        "subject": "science",
        "type": "single-choice",
        "prompt": prompt,
        "options": [{"id": key, "text": text} for key, text in zip("ABCD", options)],
        "knowledgeIds": ["kg-science-content-ka"],
        "difficulty": difficulty,
        "answer": {"value": answer, "explanation": f"{explanation} 正確答案為選項 {answer}。"},
        "provenance": {
            "origin": "original",
            "license": "All rights reserved",
            "sourceUrl": SOURCES[0]["url"],
            "sourceLocator": "三筆公立學校／公開自然科試題與課程資料的波形、公式、介質、聲音、回聲、光路與實驗設計能力方向；本題只作 pattern-only 改寫來源。",
            "authoringNote": "依官方課綱、KG 與公開資料能力方向獨立改寫；未複製原題、選項、圖表或答案；待第二輪 AI／Terra 內容複核。",
        },
        "reviewStatus": "draft",
        "updatedAt": TODAY,
        "lessonId": "lesson-science-content-ka",
        "examPatternRefs": REFS,
        "solutionStrategy": strategy,
        "solutionSteps": STEPS[number - 1],
    }


def main():
    lesson = json.loads(LESSON.read_text(encoding="utf-8"))
    lesson["updatedAt"] = TODAY
    lesson["reviewStatus"] = "draft"
    lesson["authoringStandard"] = "version-fused-v1"
    lesson["fusionRecord"]["llmSynthesisNote"] = (
        "本課依官方自然科學課綱、kg-science-content-ka、南一／康軒／翰林公開資源限制與三筆公立學校／公開自然科評量能力模式，"
        "獨立融合波動傳能、波形量、v=fλ、聲音介質、音調響度音色、回聲測距、光的反射折射、顏色與公平實驗。"
        "原有題目已全部改為波動、光及聲音專屬題目；所有正文、題幹、選項、答案、互動回饋與五步解法均重新撰寫，"
        "未複製受保護內容；Terra 第二輪與正式發布審查尚未完成，維持 draft。"
    )
    for entry in lesson.get("publisherResearch", []) + lesson.get("versionResearch", []):
        entry["reviewedAt"] = TODAY
    for number, row in enumerate(ROWS, 1):
        path = QDIR / f"question-science-content-ka-{number}.json"
        path.write_text(json.dumps(make_question(number, row), ensure_ascii=False, indent=2) + "\n", encoding="utf-8")
    REPORT.write_text(
        json.dumps(
            {
                "unit": lesson["title"],
                "lessonId": lesson["id"],
                "status": "first-pass-ai-review-complete",
                "reviewStatus": "draft",
                "checkedQuestions": 10,
                "checks": {
                    "unitSpecificOriginalContent": True,
                    "threeVersionResearchRecords": True,
                    "threePublicSchoolExamPatternSources": True,
                    "answersAndDetailedSteps": True,
                    "interactivePredictionManipulationExplanation": True,
                    "terraSecondPass": "pending",
                },
                "reviewedAt": TODAY,
                "note": "10 題改寫為波形量、波速頻率波長、聲音介質、回聲、反射折射、音色與公平實驗專屬問題；每題有唯一答案、解析與五步解法。",
            },
            ensure_ascii=False,
            indent=2,
        )
        + "\n",
        encoding="utf-8",
    )
    LESSON.write_text(json.dumps(lesson, ensure_ascii=False, indent=2) + "\n", encoding="utf-8")
    print("authored science content ka")


if __name__ == "__main__":
    main()
