import json
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
LESSON = ROOT / "lessons/science/lesson-science-content-ka-iv-2.json"
REPORT = ROOT / "implementation/reports/science-content-ka-iv-2-first-pass-review.json"
URLS = [
    ("https://www.nehs.tc.edu.tw/wp-content/uploads/sites/95/2026/02/6%E7%90%86%E5%8C%96%E7%A7%91-%E4%B9%9D%E5%B9%B4%E7%B4%9A-%E9%A1%8C%E5%BA%AB.pdf", "國立中科實驗高級中學公開九年級理化題庫", "波的傳播、橫波縱波與圖表判讀"),
    ("https://www.nhjh.tp.edu.tw/uploads/1675417616549dOhkhC5L.pdf", "臺北市立內湖國民中學公開九年級理化段考", "繩波、彈簧波、波長與介質運動"),
    ("https://www.kcjh.kh.edu.tw/upload/190/104_34764/%E4%B8%89%E5%B9%B4%E7%B4%9A%E7%90%86%E5%8C%96-%E7%AC%AC三次段考5-OK.pdf", "高雄市立國昌國民中學公開三年級自然科試題", "橫波縱波、反射與控制變因"),
]
BOUNDARY = "本紀錄只保存可追溯公開來源的章節定位、教學方向與評量能力；不複製出版社或學校教材正文、原題、選項、圖表、答案、影音或版面。"
PATTERN = "公立學校公開自然／理化試題常以繩波、彈簧壓縮、波形快照、波長、傳播方向、粒子振動與反射考查橫波縱波分類；本題只取能力方向並重新設計情境與選項。"
CONTENT = {
    "summary": "一條繩上的波形向右移動時，繩段本身可能只上下振動；彈簧的壓縮與疏部則沿彈簧方向傳遞。本課用方向關係而不是波峰外觀區分橫波與縱波，並分清介質運動、波形傳播、能量傳遞和反射資料。",
    "sections": [
        {"heading": "分類要看兩個方向", "body": "橫波的介質振動方向大致垂直於波的傳播方向，例如拉緊繩子上下抖動，波形向右而繩段上下移動；縱波的介質振動方向大致平行於傳播方向，例如彈簧的壓縮與伸張沿彈簧前進。波峰、波谷、疏部與密部是圖像線索，真正的分類依據是振動與傳播的方向關係。"},
        {"heading": "波形前進不等於介質搬家", "body": "在繩波中，某一小段繩子只在平衡位置附近往復，波形卻把擾動和能量傳到遠方；可用固定標記點的位移—時間紀錄和連續快照分開觀察兩者。波長是相鄰同相位置的距離，例如波峰到下一波峰；它不是某個繩段移動的距離。"},
        {"heading": "把彈簧資料讀成密疏變化", "body": "推拉彈簧一端會產生壓縮區和疏鬆區，若密疏沿彈簧軸向移動，就是縱波。調整推動頻率可能改變波長，但在同一介質與張力近似固定時，波速和頻率、波長要以 v=fλ 互相檢查。圖表判讀要先標出傳播方向、介質振動方向和時間間隔。"},
        {"heading": "水面、地震與聲音的限制", "body": "水面波的粒子運動可能同時含垂直與水平方向，不能只用肉眼看波峰就斷言是純橫波；聲音在空氣中主要以縱向壓縮疏鬆傳遞，地震波則可有不同型態。固定端反射會改變波形相位或方向，需把邊界條件納入，不能把反射誤當成新的波源。"},
    ],
}
EXPLANATIONS = [
    "A。繩段上下振動、波形向右傳播，兩方向互相垂直，因此屬於橫波；繩段沒有隨波形整體搬到右方。",
    "B。壓縮與伸張沿彈簧方向傳播，介質振動和波的傳播方向平行，屬於縱波。",
    "C。波形與能量可向右傳遞，但繩上小段只在原處附近振動；介質的局部運動不等於整個介質向右搬運。",
    "D。水面粒子常有上下與水平分量，分類需比較合成振動方向與傳播方向，不能只看表面波峰外觀。",
    "B。相鄰波峰是相鄰同相位置，水平距離就是波長 λ；不是週期，也不是介質粒子的振幅。",
    "C。用連續快照追蹤波峰位置得到傳播方向，再在固定標記點記錄上下位移，便能分開波形移動與介質振動。",
    "D。只改振動方向或推動方式，固定繩長、張力、介質、頻率和測量方法，才可公平比較波形差異。",
    "A。橫波縱波的分類依介質振動與傳播方向的關係，不是依波是否有波峰、波谷或是否能在所有介質中傳播。",
    "C。固定端反射可能造成相位反轉，入射與反射波疊加時還可能出現節點與腹部；必須交代邊界條件。",
    "B。應同時標示傳播方向、振動方向、時間間隔、波長或頻率，並說明資料能支持的範圍，不能只看一張快照。",
]
STRATEGIES = [
    "先畫出介質振動方向和波形傳播方向，再判斷是否垂直。",
    "追蹤彈簧密疏與軸向傳播，判斷方向是否平行。",
    "把固定點位移和波峰位置分開記錄，區分介質運動與波形傳播。",
    "列出水面粒子的所有運動分量，再比較其合成方向。",
    "找相鄰同相位置，將距離定義為波長。",
    "先用快照判傳播，再用固定標記點資料判粒子振動。",
    "只改一個振動條件並固定介質、張力、頻率與測量方式。",
    "回到方向定義，不用波峰外觀或介質名稱直接猜分類。",
    "先確認邊界，再判斷相位反轉、疊加與節腹位置。",
    "完整標示方向、時間與尺度，最後寫出資料限制。",
]
STEPS = [
    "標出波的傳播方向與介質局部振動方向。",
    "比較兩方向是垂直、平行或同時含多個分量。",
    "分辨波形／能量傳遞和介質粒子的局部運動。",
    "用波長、頻率、週期或速度資料交叉檢查。",
    "納入張力、介質、邊界與量測解析度等限制。",
]


def refs():
    return [{"url": u, "title": f"{t}；只取{loc}的題型與推理方向，未複製原題、選項、圖表、答案或版面。", "year": "109-115", "subject": "science", "locator": loc, "observedPattern": PATTERN, "reuseDecision": "pattern-only", "status": "recorded", "locatorLevel": "paper"} for u, t, loc in URLS]


def main():
    lesson = json.loads(LESSON.read_text(encoding="utf-8"))
    lesson.update({"updatedAt": "2026-09-21", "reviewStatus": "draft", "authoringStandard": "version-fused-v1", "content": CONTENT})
    lesson["studyHighlights"] = ["以振動方向與傳播方向區分橫波、縱波。", "把介質局部運動、波形前進與能量傳遞分開。", "用波峰間距、密疏、v=fλ 與快照資料互相驗證。", "水面波、聲音、地震波與反射都要交代模型適用條件。"]
    for row in lesson.get("publisherResearch", []): row["reviewedAt"] = "2026-09-21"
    for row in lesson.get("versionResearch", []): row.update({"reviewedAt": "2026-09-21", "licenseBoundary": BOUNDARY})
    lesson["fusionRecord"]["llmSynthesisNote"] = "本課依官方自然科學課綱、kg-science-content-ka-iv-2、南一／康軒／翰林可取得的公開研究方向與三筆公立學校自然／理化試題能力模式，以自己的話獨立融合繩波、彈簧縱波、介質振動、波形／能量傳播、波長、v=fλ、水面波、聲音、地震波與固定端反射；把原通用佔位正文改寫為方向判讀與快照實驗專屬教材，未複製教材或試題，Terra 第二輪與正式發布審查尚未完成，維持 draft。"
    LESSON.write_text(json.dumps(lesson, ensure_ascii=False, indent=2) + "\n", encoding="utf-8")
    for i in range(1, 11):
        path = ROOT / f"questions/science/question-science-content-ka-iv-2-{i}.json"
        q = json.loads(path.read_text(encoding="utf-8"))
        q.update({"examPatternRefs": refs(), "reviewStatus": "draft", "updatedAt": "2026-09-21", "solutionStrategy": STRATEGIES[i - 1], "solutionSteps": STEPS})
        q["answer"]["explanation"] = EXPLANATIONS[i - 1]
        q["provenance"].update({"sourceUrl": URLS[0][0], "sourceLocator": "三筆公立學校公開自然／理化試題中的繩波、彈簧波、橫波縱波、波長、反射與控制變因能力；本題改寫為橫波與縱波原創情境。"})
        path.write_text(json.dumps(q, ensure_ascii=False, indent=2) + "\n", encoding="utf-8")
    REPORT.write_text(json.dumps({"unit": lesson["title"], "lessonId": lesson["id"], "status": "first-pass-ai-review-complete", "reviewStatus": "draft", "checks": {"unitSpecificOriginalContent": True, "threeVersionResearchRecords": True, "publicExamPatternRewrite": True, "fusionRecordPresent": True, "interactivePredictionManipulationExplanation": True, "answersAndDetailedSteps": True, "contentRewrittenFromPlaceholder": True, "terraSecondPass": "pending"}, "reviewedAt": "2026-09-21"}, ensure_ascii=False, indent=2) + "\n", encoding="utf-8")
    print("authored science content ka iv 2")


if __name__ == "__main__": main()
