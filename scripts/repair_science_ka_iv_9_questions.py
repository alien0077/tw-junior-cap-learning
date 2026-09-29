import json
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
DATA = [
    ("凸透鏡對近軸平行光的主要作用是什麼？", ["使光線折射後會聚於焦點附近", "使光線必定向外發散", "使光線完全不改變方向", "使光線變成聲波"], "A", "凸透鏡具有會聚作用，平行主軸的光線折射後可在焦點附近會聚。", "先辨認透鏡形狀，再判斷它對光線的會聚或發散作用。"),
    ("凹透鏡形成的正立、縮小虛像，最適合用在哪種視力矯正？", ["近視眼鏡", "遠視眼鏡", "老花眼鏡一定只能用凹透鏡", "顯微鏡物鏡"], "A", "凹透鏡使入眼光線發散，可協助近視眼將焦點後移到視網膜上。", "先判斷眼睛焦點位置，再選擇使光線會聚或發散的透鏡。"),
    ("用凸透鏡當放大鏡時，物體應放在什麼位置？", ["焦點內，且靠近透鏡的一側", "焦點外很遠處才能形成正立放大虛像", "剛好在焦點上且一定成清晰像", "透鏡另一側的焦點外"], "A", "物體位於凸透鏡焦點內時，可形成正立、放大的虛像，這是放大鏡的基本原理。", "先確認所需像的正倒、大小與虛實，再對照凸透鏡成像條件。"),
    ("照相機用凸透鏡把遠處景物成像在感光元件上，通常形成哪種像？", ["倒立、縮小、實像", "正立、放大、虛像", "正立、縮小、虛像", "倒立、放大、虛像"], "A", "遠處物體經凸透鏡通常在焦點附近形成倒立、縮小的實像，感光元件可接收實像。", "先判斷物距相對焦距，再依是否能投影到感光元件判斷實虛像。"),
    ("複式顯微鏡通常使用兩個凸透鏡，最合理的功能分工是？", ["物鏡先形成放大的中間像，目鏡再把中間像放大供眼睛觀察", "兩片都使光線發散", "只有鏡架負責放大", "物鏡把所有光吸收"], "A", "複式顯微鏡以物鏡與目鏡連續成像，先形成中間像，再由目鏡放大觀察。", "沿光路逐片分析透鏡的物、像關係，不把總倍率當成單片作用。"),
    ("望遠鏡需要觀察遠方物體，物鏡通常先形成什麼？", ["位於目鏡前方的倒立縮小實像或中間像", "永遠是物鏡焦點內的正立放大虛像", "只形成聲音", "沒有任何像，只改變顏色"], "A", "遠方物體經物鏡可在焦平面附近形成中間實像，再由目鏡觀察與放大視角。", "先分析遠物經物鏡的成像，再判斷目鏡如何接續。"),
    ("汽車後視鏡常使用凸面鏡，主要優點是什麼？", ["視野較廣，可看到較大範圍但影像縮小", "形成倒立放大的實像", "把所有光線會聚在焦點", "使後方物體看起來更近且更大"], "A", "凸面鏡形成正立、縮小虛像，但能提供較廣視野，適合觀察較大範圍。", "把鏡面形狀與成像特性分開，再連結交通安全用途。"),
    ("凹面鏡可用於手電筒反射罩，最主要的光學目的為何？", ["將接近焦點的光源發出的光反射成較集中的光束", "使光線全部向四周發散", "形成正立縮小虛像供眼睛看", "消除光的反射"], "A", "光源若置於凹面鏡焦點附近，反射光可較接近平行方向而集中照向前方。", "先判斷光源與焦點的相對位置，再推論反射後光束。"),
    ("若一副遠視眼鏡需要協助眼睛把光線會聚，應選用哪種鏡片？", ["凸透鏡", "凹透鏡", "平面玻璃一定可以", "凸面鏡"], "A", "遠視眼可能使焦點落在視網膜後方，凸透鏡增加會聚作用可協助焦點前移。", "先判斷焦點在視網膜前或後，再選擇會聚或發散透鏡。"),
    ("要驗證某透鏡是凸透鏡，哪項實驗最直接？", ["讓遠處平行光通過，觀察是否能在屏幕上形成明亮集中的實像並量焦距", "只摸透鏡重量", "只比較鏡框顏色", "只把透鏡放在黑暗處不入光"], "A", "凸透鏡可使平行光會聚，在屏幕上形成亮斑或實像；量測焦距可進一步確認光學特性。", "設計可觀察會聚或發散結果的測試，再控制光源與屏幕位置。"),
]

TARGET_ANSWERS = 'ABCDBCDACB'

PUBLIC_REFERENCES = [
    {"url": "https://www.kcjh.kh.edu.tw/upload/190/104_34764/%E5%9C%8B%E6%98%8C--%E4%BA%8C%E5%B9%B4%E7%B4%9A--%E8%87%AA%E7%84%B6%E7%A7%91.pdf", "title": "高雄市立國昌國中 112 學年度第一學期第二次段考二年級自然科試題", "year": "112"},
    {"url": "https://www.dwm.kh.edu.tw/upload/344/104_64184/114%E5%AD%B8%E5%B9%B4%E5%BA%A6%E7%AC%AC%E4%B8%80%E5%AD%B8%E6%9C%9F%E7%AC%AC%E4%BA%8C%E6%AC%A1%E6%AE%B5%E8%80%83%E8%87%AA%E7%84%B6%E7%A7%91%E8%87%AA%E7%84%B6%E4%BA%8C%E5%B9%B4%E7%B4%9A%E8%A9%A6%E9%A1%8C.pdf", "title": "高雄市立大灣國中 114 學年度第一學期第二次段考二年級自然科", "year": "114"},
    {"url": "https://www.nhjh.tp.edu.tw/uploads/1675416610965nINWfUhq.pdf", "title": "臺北市立內湖國民中學 111 學年度第一學期第二次定期考查八年級理化科試題", "year": "111"},
]
for ref in PUBLIC_REFERENCES:
    ref.update({"subject": "science", "locator": ref["title"], "observedPattern": "僅研究公立學校公開試題的透鏡成像、面鏡、眼鏡、照相機與顯微鏡判讀能力方向；未複製原題文字、選項、圖表或答案。", "reuseDecision": "pattern-only", "status": "recorded", "locatorLevel": "paper"})

for i, (prompt, options, answer, explanation, strategy) in enumerate(DATA, 1):
    path = ROOT / "questions/science" / f"question-science-content-ka-iv-9-{i}.json"
    item = json.loads(path.read_text())
    correct = options[ord(answer) - 65]
    target = TARGET_ANSWERS[i - 1]
    distractors = [text for option_index, text in enumerate(options) if option_index != ord(answer) - 65]
    position = ord(target) - 65
    arranged = distractors[:position] + [correct] + distractors[position:]
    item.update({
        "prompt": prompt,
        "options": [{"id": chr(65 + j), "text": text} for j, text in enumerate(arranged)],
        "answer": {"value": target, "explanation": f"{explanation} 正確答案為選項 {target}：「{correct}」。"},
        "solutionStrategy": strategy,
        "solutionSteps": [
            "圈出題目中的透鏡、面鏡、焦點、物距、像的正倒大小與實虛。",
            "先沿光路判斷會聚／發散，再確認物距與焦距關係。",
            f"套用原理：{explanation}",
            f"排除把凹凸透鏡、凹凸面鏡或眼鏡用途混淆的選項，答案為「{correct}」（選項 {target}）。",
            "回查是否符合儀器實際功能與可觀察的成像條件。",
        ],
        "examPatternRefs": PUBLIC_REFERENCES,
        "reviewStatus": "draft",
    })
    path.write_text(json.dumps(item, ensure_ascii=False, indent=2) + "\n")
print(f"rewrote {len(DATA)} questions")
