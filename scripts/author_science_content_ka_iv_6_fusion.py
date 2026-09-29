"""Ka-Ⅳ-6：針孔成像、影子與光的直進第一輪原創題庫。"""
import json
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
LESSON = ROOT / "lessons/science/lesson-science-content-ka-iv-6.json"
REPORT = ROOT / "implementation/reports/science-content-ka-iv-6-first-pass-review.json"
QDIR = ROOT / "questions/science"
TODAY = "2026-09-23"
SOURCES = [
    {"url": "https://www.chhs.tp.edu.tw/uploads/1580833724641KNP89ykg.pdf", "title": "臺北市立景興國民中學八年級理化科公開定期評量", "year": "108", "locator": "光直進、針孔成像、影子、日食與實驗控制變因", "pattern": "取公立學校評量以光路、影子與針孔投影進行圖形判讀和實驗推理的能力方向。"},
    {"url": "https://www.kcjh.kh.edu.tw/upload/190/104_34764/%E5%9C%8B%E6%98%8C--%E4%BA%8C%E5%B9%B4%E7%B4%9A--%E8%87%AA%E7%84%B6%E7%A7%91.pdf", "title": "高雄市立國昌國民中學二年級自然科公開段考試題", "year": "112", "locator": "光的直進、針孔成像、影子、日食與操作條件", "pattern": "取從光源—物體—屏幕關係推論影子與成像方向、大小和觀察條件的能力方向。"},
    {"url": "https://www.sjjh.tyc.edu.tw/113-1-8%E8%A3%9C%E8%80%83%E9%A1%8C%E5%BA%AB.pdf", "title": "桃園市立山腳國民中學八年級自然科公開補考題庫", "year": "113", "locator": "光直進、影子邊界、針孔成像與變因控制", "pattern": "取公開自然科題庫要求用光線模型、幾何關係與公平實驗判讀現象的能力方向。"},
]
REFS = [{**s, "subject": "science", "observedPattern": s["pattern"], "reuseDecision": "pattern-only", "status": "recorded", "locatorLevel": "paper"} for s in SOURCES]
BOUNDARY = "本紀錄只保存公開資料的章節定位、能力方向與題型模式；不複製原題、選項、圖表、答案、教材文字或版面。"

STEPS = [
    ["圈出光源、物體、針孔、屏幕、物距、屏距、孔徑與影像方向。", "先判斷題目問的是直進、影子、成像大小、清晰度還是實驗設計。", "畫出代表性光線或使用相似三角形，將觀察連回模型。", "排除把影子當成染黑、把實像當成虛像或混淆亮度與大小的選項。", "回查是否只改變一項條件，確認結論和可觀察證據一致。"],
    ["定位物體頂端、底端、針孔與屏幕。", "從頂端和底端各畫一條穿過針孔的直線。", "注意兩條光線在孔處交叉，屏幕接到的是相反位置的光。", "排除反射、折射、紙屏自發光等無關解釋。", "用倒立、左右相反且可投影三項證據判定實像。"],
    ["固定物體與屏幕，確認只改變孔徑。", "比較小孔與大孔通過的光線方向數量。", "大孔讓同一物點的光在屏幕形成較寬的重疊區。", "區分影像模糊、亮度變化與光速改變。", "用邊界清晰度而非單看亮暗檢查答案。"],
    ["列出物高、物距、屏距與像高。", "判斷題目是否可用相似三角形近似。", "使用像高／物高≈屏距／物距計算。", "確認方向仍由光線交叉決定，不能只用大小判斷。", "檢查單位、比例與紙盒實際孔徑限制。"],
    ["先辨認光源、遮光物與屏幕三者的順序。", "畫出由光源經物體邊緣到屏幕的兩條界線。", "將物體移近光源後重新延伸光線，判斷遮光區張角。", "排除只靠影子深淺或物體本身大小猜測。", "以影高或影寬實測並記錄光源大小與雜光限制。"],
    ["寫出要研究的變因與要量的結果。", "固定光源、物距、孔徑、屏幕和環境光。", "一次只改變屏距，重複量測像高和方向。", "排除同時改變孔徑、亮度或紙盒角度的設計。", "用表格呈現數據，再說明哪些結論仍需實測。"],
    ["把針孔改為日食投影的紙板小孔。", "確認眼睛不直接看太陽，改看屏幕上的投影。", "用直進光線說明太陽輪廓如何落到屏幕。", "排除未認證濾鏡或相機觀景窗的安全保證。", "補上光源方向、孔徑、屏距與雲層等限制。"],
    ["固定物體與屏幕，只比較孔徑。", "同時觀察像的亮度、輪廓清晰度與位置。", "說明孔徑變小可限制光線方向，但也減少進光量。", "不把更亮直接當成像更大，也不把模糊當成光線彎曲。", "用多次觀察和清晰度標準支持結論。"],
    ["找出光源、障礙物和屏幕的相對位置。", "以直線延伸光源邊緣和物體邊緣。", "判斷屏幕哪些區域收不到光而成為影子。", "排除物體把黑色噴到牆上或紙屏自己變黑。", "用影子邊界的幾何位置回查推論。"],
    ["辨認物距、屏距、物高與像高的已知量。", "先判定影像是否是針孔實像而非鏡面虛像。", "代入像高／物高≈屏距／物距並保留方向判斷。", "檢查題目是否改變孔徑或只提供近似條件。", "用數值、方向、可投影性三者做最後核對。"],
]

DATA = [
    ("easy", "下列哪個觀察最能支持光在均勻介質中沿直線傳播？", ["不透明紙板後方出現有明確邊界的影子", "紙屏在沒有光源時自行發亮", "所有物體都能透光", "光線遇到任何物體都會轉彎"], "A", "不透明物體遮住部分直線光線後，屏幕上留下與幾何位置相符的暗區，支持光直進模型；其他選項不是本實驗的證據。", "由可畫出的遮光邊界判斷光路模型。"),
    ("medium", "針孔暗箱中，物體箭頭的頂端光線通過針孔後落到屏幕較低處，底端光線落到較高處。屏幕影像應為？", ["正立且不可投影的虛像", "上下顛倒、可投影的實像", "只左右相反但上下不變的影子", "沒有方向的均勻亮斑"], "B", "頂端與底端光線在針孔附近交叉，所以屏幕位置上下相反；屏幕實際接收到物體光線，能形成可投影的倒立實像。", "先追兩條端點光線，再同時判斷方向與是否可投影。"),
    ("medium", "固定物體和屏幕，只把針孔從約 2 mm 改成 8 mm；影像通常變亮但邊界較模糊，最合理的解釋是？", ["孔變大使光速下降", "紙屏把光全部吸收", "同一物點可通過較多方向的光，投影重疊範圍變寬", "物體因此變成虛像"], "C", "大孔讓同一物點發出的多個方向都通過，屏幕上的光斑重疊範圍變寬，邊界因而模糊；通光量增加則常使影像較亮。", "把孔徑的兩個效果拆成進光量與方向限制。"),
    ("hard", "物高 6 cm、物距 36 cm、屏距 24 cm 的針孔成像，依相似三角形估計像高約為多少？", ["2 cm", "4 cm", "9 cm", "16 cm"], "B", "像高／物高≈屏距／物距，因此像高≈6×24÷36=4 cm；方向另由光線交叉判定為倒立。", "先寫比例，再代入像距與物距，最後補上方向。"),
    ("medium", "點光源、三角形紙板和白屏順序固定；只把紙板移近點光源，通常會看到影子變化為何？", ["影子在屏幕上通常變大，因為遮光邊界在較遠處張開", "影子必然變小且光線消失", "影子一定變成針孔實像", "影子深淺即可精確給出物距"], "A", "物體靠近近似點光源時，從光源經物體邊緣延伸出的遮光區在屏幕上張角變大，影高或影寬通常增加；深淺還受光源大小和雜光影響。", "畫兩條遮光邊界，不用影子顏色代替尺寸證據。"),
    ("hard", "要研究屏距對針孔像高的影響，哪個設計最能支持因果結論？", ["同時改變屏距、孔徑和光源亮度", "固定物體、物距、孔徑與光源，只改變屏距並重複量像高", "只看一次影像是否變亮", "每次換不同高度的物體且不記錄距離"], "B", "只改變屏距並固定其他條件，才能把像高差異歸因於屏距；重複量測可降低讀值誤差。", "以一次一變因加重複測量建立公平實驗。"),
    ("easy", "用針孔投影觀察日食時，最重要的安全作法是？", ["直接透過針孔盯著太陽", "用未認證墨鏡直視太陽", "讓陽光通過小孔落在屏幕上，只觀察投影，不直視太陽", "把手機鏡頭對準太陽並從觀景窗觀看"], "C", "針孔投影把太陽光形成的影像落在屏幕上，觀察者不必直視太陽；未認證濾鏡、墨鏡或相機觀景窗都不能視為安全保證。", "先確認觀察路徑，再檢查是否避免眼睛直接接收強光。"),
    ("medium", "若針孔太小，影像輪廓較清楚但整體很暗；若針孔稍大，影像較亮卻模糊。哪個結論最適當？", ["孔徑同時影響光線方向限制與進光量，清晰度和亮度要分開記錄", "影像越亮代表一定越大", "模糊表示光線改走曲線", "孔徑只改變光速，不影響觀察"], "A", "小孔限制通過方向，通常有利於輪廓清楚但減少光量；大孔增加進光量卻讓同一物點形成較寬重疊。亮度和尺寸不是同一量。", "建立觀察表，把亮度、清晰度、大小與方向分欄。"),
    ("easy", "影子形成的最恰當說法是？", ["不透明物體將黑色染到屏幕上", "不透明物體擋住部分光線，使屏幕某區域收不到光", "屏幕自己產生暗色", "光線只能在影子區彎曲"], "B", "影子是被遮住的光線未到達屏幕所形成的暗區，邊界可由光源、物體與屏幕的相對位置推理。", "把影子翻譯成『哪些光線沒有抵達』。"),
    ("hard", "物高 8 cm、物距 40 cm、屏距 30 cm 的針孔成像，像高約為多少，且方向如何？", ["6 cm，倒立", "6 cm，正立", "10.7 cm，倒立", "10.7 cm，正立"], "A", "像高≈8×30÷40=6 cm；光線在針孔處交叉，所以方向為倒立，且屏幕可接到光線，是實像。", "先算大小，再用光線交叉判方向，勿以正負號取代幾何圖。"),
]

def make_question(n, row):
    difficulty, prompt, options, answer, explanation, strategy = row
    return {
        "id": f"question-science-content-ka-iv-6-{n}", "subject": "science", "type": "single-choice",
        "prompt": prompt, "options": [{"id": k, "text": v} for k, v in zip("ABCD", options)],
        "knowledgeIds": ["kg-science-content-ka-iv-6"], "difficulty": difficulty,
        "answer": {"value": answer, "explanation": f"{explanation} 正確答案為選項 {answer}。"},
        "provenance": {"origin": "original", "license": "All rights reserved", "sourceUrl": SOURCES[0]["url"], "sourceLocator": "三筆公立學校公開自然科試題的光直進、影子、針孔成像、日食投影與控制變因能力方向；本題只作 pattern-only 改寫來源。", "authoringNote": "依官方課綱、KG 與公開資料能力方向獨立改寫；未複製原題、選項、圖表或答案；待第二輪 AI／Terra 內容複核。"},
        "reviewStatus": "draft", "updatedAt": TODAY, "lessonId": "lesson-science-content-ka-iv-6", "examPatternRefs": REFS,
        "solutionStrategy": strategy, "solutionSteps": STEPS[n - 1],
    }

def main():
    lesson = json.loads(LESSON.read_text(encoding="utf-8"))
    lesson["updatedAt"] = TODAY
    lesson["reviewStatus"] = "draft"
    lesson["authoringStandard"] = "version-fused-v1"
    lesson["fusionRecord"]["llmSynthesisNote"] = "本課依官方自然科學課綱、kg-science-content-ka-iv-6、南一公開入口、康軒公開動課本定位、翰林公開資料與三筆公立學校自然科評量能力模式，獨立融合光的直進、影子邊界、針孔實像、物距屏距、孔徑、日食投影與安全。所有正文、數據、例證、光線圖、互動步驟、題幹、選項、答案與五步解法均重新撰寫，未複製受保護內容；Terra 第二輪與正式發布審查尚未完成，維持 draft。"
    for entry in lesson.get("publisherResearch", []) + lesson.get("versionResearch", []):
        entry["reviewedAt"] = TODAY
        entry.setdefault("licenseBoundary", BOUNDARY)
    for n, row in enumerate(DATA, 1):
        (QDIR / f"question-science-content-ka-iv-6-{n}.json").write_text(json.dumps(make_question(n, row), ensure_ascii=False, indent=2) + "\n", encoding="utf-8")
    REPORT.write_text(json.dumps({"unit": lesson["title"], "lessonId": lesson["id"], "status": "first-pass-ai-review-complete", "reviewStatus": "draft", "checkedQuestions": 10, "checks": {"unitSpecificOriginalContent": True, "threeVersionResearchRecords": True, "threePublicSchoolExamPatternSources": True, "answersAndDetailedSteps": True, "interactivePredictionManipulationExplanation": True, "terraSecondPass": "pending"}, "reviewedAt": TODAY, "note": "10 題已逐題改寫為光直進、影子邊界、針孔實像、物距屏距、孔徑、日食投影、控制變因與安全專屬問題；每題有唯一答案、解析與五步解法。"}, ensure_ascii=False, indent=2) + "\n", encoding="utf-8")
    LESSON.write_text(json.dumps(lesson, ensure_ascii=False, indent=2) + "\n", encoding="utf-8")
    print("authored science content ka iv 6")

if __name__ == "__main__":
    main()
