#!/usr/bin/env python3
"""Independently normalize the Hist Ia-IV-1 question bank."""
import json
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
OUT = ROOT / "questions/social"
LESSON = "lesson-social-content-hist-ia-iv-1"
KG = "kg-social-content-hist-ia-iv-1"
TARGETS = ["A", "B", "C", "D", "A", "B", "C", "D", "B", "C"]
FOCI = [
    ("海禁、轉運與地方貿易", "政策文字與地方行動可能有落差，應同時查制度、路徑與實際參與者。"),
    ("朝貢文書與市場協商", "禮儀語言不會涵蓋往來的全部功能，還要辨認物品、資訊與邊境協商。"),
    ("白銀流動與稅制變化", "白銀流動可連結稅制與港口，但不同地區的利益與成本不能被平均化。"),
    ("沿海暴力與治理回應", "武裝活動涉及多種角色，必須把暴力、地方利益與政策回應分開分析。"),
    ("港口的多重節點", "同一港口可同時承載官方、民間、宗教與語言網絡，不能化約成單一政權往來。"),
    ("旅行記錄與接待展示", "旅行者所見和接待方展示都有形成目的，應區分觀察、選擇性呈現與未見部分。"),
    ("思想流通與地方改寫", "書籍流通提示接觸，但不同註解與使用方式顯示地方社會會選擇和重組思想。"),
    ("海圖的比例與空白", "海圖的製圖目的、比例、地名和空白會影響可見範圍，不能直接比較空白等於未知。"),
    ("人口移動與地方痕跡", "地名、婚姻與產業可作為移動線索，但仍要查時間、來源與其他可能原因。"),
    ("中央命令與多重證據", "單一中央禁令不能代表所有時段與地區，應以不同來源建立可檢驗的時間序列。"),
]
SOURCES = [
    {
        "url": "https://www.yacjh.kh.edu.tw/upload/221/101_30637/114%E4%B8%8B%E5%AD%B8%E6%9C%9F%E7%AC%AC%E4%B8%80%E6%AC%A1%E6%AE%B5%E8%80%83%E4%B8%89%E5%B9%B4%E7%B4%9A%E7%9A%84%E7%A4%BE%E6%9C%83.pdf",
        "title": "高雄市立鹽埕國民中學公開段考社會科；僅研究資料判讀與歷史推理題型，未複製原題。",
        "year": "114",
        "locator": "公開段考社會科 PDF；第 1 題至第 10 題型範圍：時序、資料判讀與因果界線",
        "observedPattern": "由材料中的制度、時間與多方角色要求學生提出證據範圍相稱的歷史解釋。",
    },
    {
        "url": "https://affairs.kh.edu.tw/1126/upload/file_list/149",
        "title": "高雄市立文府國民中學公開社會科試題入口；僅研究多資料互證題型，未複製原題。",
        "year": "113-114",
        "locator": "公開試題與解答入口；第 1 題至第 10 題型範圍：跨區交流、制度與多重證據",
        "observedPattern": "要求比較文字、地圖與角色材料，區分直接記錄、合理推論及待補證的主張。",
    },
    {
        "url": "https://www.dwm.kh.edu.tw/view/index.php?MainMenuId=64182&MainType=0&SubMenuId=64184&SubType=104&WebID=344",
        "title": "高雄市立大灣國民中學公開段考試題入口；僅研究區域互動與多方觀點題型，未複製原題。",
        "year": "113-114",
        "locator": "公開段考試題入口；第 1 題至第 10 題型範圍：區域互動、文化變遷與多方角色",
        "observedPattern": "從區域往來的材料情境判斷不同角色、利益與社會變化，避免單一來源包辦結論。",
    },
]

def refs():
    return [{**s, "subject": "social", "reuseDecision": "pattern-only", "status": "recorded", "locatorLevel": "paper"} for s in SOURCES]

for index, target in enumerate(TARGETS, 1):
    path = OUT / f"question-social-content-hist-ia-iv-1-{index}.json"
    data = json.loads(path.read_text(encoding="utf-8"))
    assert data["lessonId"] == LESSON and data["knowledgeIds"] == [KG]
    old = data["answer"]["value"]
    correct = data["options"][ord(old) - 65]["text"]
    remaining = [x["text"] for i, x in enumerate(data["options"]) if i != ord(old) - 65]
    ordered = remaining[:ord(target) - 65] + [correct] + remaining[ord(target) - 65:]
    data["options"] = [{"id": chr(65 + i), "text": text} for i, text in enumerate(ordered)]
    data["answer"] = {"value": target, "explanation": f"本題聚焦「{FOCI[index - 1][0]}」。{FOCI[index - 1][1]} 正確答案為選項 {target}：「{correct}」。"}
    data["solutionStrategy"] = f"先定位{FOCI[index - 1][0]}的時間、角色與資料類型，再區分直接證據、推論和資料缺口；{FOCI[index - 1][1]}"
    data["solutionSteps"] = [
        f"讀題定位：圈出本題的材料、時段、角色與任務，確認題目正在考「{FOCI[index - 1][0]}」，不要只看答案字母。",
        "建立判準：把政策、行動、物質流動、人口移動與地方經驗分開，並標記每個結論的資料來源。",
        f"核對正解：選項 {target}「{correct}」符合題幹，因為{FOCI[index - 1][1]}",
        "逐項排除：檢查其餘選項是否把官方規定當成全部實況、把單一來源放大成全區結論，或忽略時代與角色差異。",
        "結論回查：將答案放回材料，重新核對年代、地點、角色與證據強度；若新增來源或改變尺度，必須重新判斷。",
    ]
    data["examPatternRefs"] = refs()
    data["updatedAt"] = "2026-09-13"
    data["reviewStatus"] = "draft"
    data["provenance"]["authoringNote"] = "依官方課綱、歷 Ia-Ⅳ-1 知識圖譜及三所公立學校公開社會科試題的時序、資料判讀與多方觀點能力方向獨立改寫；未複製原題文字、選項、圖片或答案，待逐題學科與 Terra 複核。"
    path.write_text(json.dumps(data, ensure_ascii=False, indent=2) + "\n", encoding="utf-8")
print(f"rewrote {len(TARGETS)} independent questions for {LESSON}")
