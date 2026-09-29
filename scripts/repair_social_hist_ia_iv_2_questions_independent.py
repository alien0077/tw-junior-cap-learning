#!/usr/bin/env python3
"""Independently normalize the Hist Ia-IV-2 question bank."""
import json
from pathlib import Path
ROOT = Path(__file__).resolve().parents[1]
OUT = ROOT / "questions/social"
LESSON = "lesson-social-content-hist-ia-iv-2"
KG = "kg-social-content-hist-ia-iv-2"
TARGETS = ["A", "B", "C", "D", "A", "B", "C", "D", "B", "C"]
FOCI = [
    ("白銀流入與不均等影響", "總量增加不等於所有地區或群體同樣受益，還要比較稅負、物價與交易位置。"),
    ("貨物、內陸路徑與節點", "倉庫、渡口和稅卡提示商品流動需要中介與制度，不代表每個居民都參與同樣交易。"),
    ("商業憑證、關稅與風險", "政府規則與商人組織可能同時促進交易並分配成本，不能把市場寫成完全自由。"),
    ("同一商品的多重用途", "商品進入不同社會位置後會被重新選擇，用途差異可反映身分、需求與取得條件。"),
    ("雙語契約與中介", "契約的語詞、重量與責任需要放在通事、法律與交易關係中讀，不能只看語言表面。"),
    ("外商聚居與治理", "聚居區兼有社群自主和政府管理，會館、墓地與稅務可共同呈現互動與界線。"),
    ("宗教場所與商路服務", "捐助與宗教場所功能提示商路上的信仰、住宿、翻譯和慈善交織，但各地功能必須分別查證。"),
    ("技術流通與地方差異", "技術交流不會抹平地方船型與操作規則，應區分共同原理、在地改造與制度條件。"),
    ("飲食交流與在地改造", "食物被採用後可能改變名稱、材料與儀式功能，交流是地方選擇和重組而非原封搬移。"),
    ("三類商貿資料的互證", "帳冊、家書與器物各自記錄數量、經驗或使用線索，差異應轉成研究問題而非任意裁決。"),
]
SOURCES = [
    {"url": "https://www.yacjh.kh.edu.tw/upload/221/101_30637/114%E4%B8%8B%E5%AD%B8%E6%9C%9F%E7%AC%AC%E4%B8%80%E6%AC%A1%E6%AE%B5%E8%80%83%E4%B8%89%E5%B9%B4%E7%B4%9A%E7%9A%84%E7%A4%BE%E6%9C%83.pdf", "title": "高雄市立鹽埕國民中學公開段考社會科；僅研究資料判讀與歷史推理題型，未複製原題。", "year": "114", "locator": "公開段考社會科 PDF；第 1 題至第 10 題型範圍：資料判讀、流通與因果界線", "observedPattern": "以貨物、制度與角色材料要求學生判斷證據所能支持的商貿解釋。"},
    {"url": "https://affairs.kh.edu.tw/1126/upload/file_list/149", "title": "高雄市立文府國民中學公開社會科試題入口；僅研究多資料互證題型，未複製原題。", "year": "113-114", "locator": "公開試題與解答入口；第 1 題至第 10 題型範圍：跨區交流、制度與多重證據", "observedPattern": "比較文字、路徑與物質資料，區分直接記錄、合理推論與待補證主張。"},
    {"url": "https://www.dwm.kh.edu.tw/view/index.php?MainMenuId=64182&MainType=0&SubMenuId=64184&SubType=104&WebID=344", "title": "高雄市立大灣國民中學公開段考試題入口；僅研究區域互動與多方觀點題型，未複製原題。", "year": "113-114", "locator": "公開段考試題入口；第 1 題至第 10 題型範圍：區域互動、文化變遷與多方角色", "observedPattern": "從交流材料分析不同角色、利益與文化變化，不以單一來源包辦結論。"},
]
def refs(): return [{**s, "subject": "social", "reuseDecision": "pattern-only", "status": "recorded", "locatorLevel": "paper"} for s in SOURCES]
for i, target in enumerate(TARGETS, 1):
    p = OUT / f"question-social-content-hist-ia-iv-2-{i}.json"
    d = json.loads(p.read_text(encoding="utf-8"))
    assert d["lessonId"] == LESSON and d["knowledgeIds"] == [KG]
    old = d["answer"]["value"]; oi = ord(old) - 65; ti = ord(target) - 65
    correct = d["options"][oi]["text"]; rest = [x["text"] for j, x in enumerate(d["options"]) if j != oi]
    ordered = rest[:ti] + [correct] + rest[ti:]
    d["options"] = [{"id": chr(65 + j), "text": x} for j, x in enumerate(ordered)]
    focus, reason = FOCI[i - 1]
    d["answer"] = {"value": target, "explanation": f"本題聚焦「{focus}」。{reason} 正確答案為選項 {target}：「{correct}」。"}
    d["solutionStrategy"] = f"先定位{focus}的時間、角色、貨物與制度，再分開直接證據和推論；{reason}"
    d["solutionSteps"] = [
        f"讀題定位：圈出材料中的貨物、制度、地點和角色，確認題目正在考「{focus}」。",
        "建立判準：把流通路徑、交易規則、使用者與文化意義分層，並記錄每層的資料來源。",
        f"核對正解：選項 {target}「{correct}」符合題幹，因為{reason}",
        "逐項排除：檢查其餘選項是否把總量當成人人受益、把商品當成單一路徑，或忽略中介、地方改造與資料盲點。",
        "結論回查：重新核對時間、地點、角色與證據強度；若新增帳冊、器物或地方資料，必須重新檢查結論。",
    ]
    d["examPatternRefs"] = refs(); d["updatedAt"] = "2026-09-13"; d["reviewStatus"] = "draft"
    d["provenance"]["authoringNote"] = "依官方課綱、歷 Ia-Ⅳ-2 知識圖譜及三所公立學校公開社會科試題的資料判讀、商貿流通與多方觀點能力方向獨立改寫；未複製原題文字、選項、圖片或答案，待逐題學科與 Terra 複核。"
    p.write_text(json.dumps(d, ensure_ascii=False, indent=2) + "\n", encoding="utf-8")
print(f"rewrote {len(TARGETS)} independent questions for {LESSON}")
