#!/usr/bin/env python3
"""Replace one Social Studies history lesson with independently adapted public-exam-style items."""
from __future__ import annotations

import json
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
LESSON = "lesson-social-content-hist-qa-iv-3"
KID = "kg-social-content-hist-qa-iv-3"
SOURCE = "https://www.yacjh.kh.edu.tw/upload/221/101_30637/114%E4%B8%8B%E5%AD%B8%E6%9C%9F%E7%AC%AC%E4%B8%80%E6%AC%A1%E6%AE%B5%E8%80%83%E4%B8%89%E5%B9%B4%E7%B4%9A%E7%A4%BE%E6%9C%83.pdf"

rows = [
    ("十八世紀北美殖民地居民反對英國課稅，最直接反映哪一項政治訴求？", ["殖民地應有代表參與決策", "君主應擴大特權", "殖民地應停止貿易", "殖民地應恢復封建制度"], "A", "反對無代表的課稅，核心是要求政治代表與參與決策的權利。", "第21題題型改編"),
    ("法國第三身分代表宣誓制定憲法，主要展現哪一項啟蒙政治理念？", ["主權在民", "神權政治", "殖民擴張", "君權神授"], "A", "代表以人民代表身分要求制定憲法，展現主權在民的理念。", "第22至23題題型改編"),
    ("拿破崙遠征哪個國家時遭遇嚴重失敗，成為其勢力衰退的關鍵？", ["俄國", "西班牙", "奧地利", "葡萄牙"], "A", "1812 年遠征俄國受到嚴寒、補給與軍事抵抗影響而失敗。", "第24題題型改編"),
    ("普魯士推動德意志統一時，俾斯麥採取的主要政策是什麼？", ["鐵血政策", "閉關鎖國", "平均地權", "民族自決公投"], "A", "俾斯麥以軍事與外交手段推動統一，通常概括為鐵血政策。", "第26題題型改編"),
    ("十九世紀後期列強以原料、市場與投資為目標向外擴張，這種現象最符合哪個概念？", ["帝國主義", "文藝復興", "宗教改革", "封建制度"], "A", "工業化列強為取得原料與市場而擴張，屬於近代帝國主義。", "第27至28題題型改編"),
    ("下列哪一項最能說明社會達爾文主義如何助長帝國主義？", ["以強者競爭淘汰的觀念合理化征服弱國", "主張各國放棄軍備", "要求殖民地完全自治", "鼓勵取消海外貿易"], "A", "社會達爾文主義把生物競爭觀念套用於國際關係，常被用來合理化強國支配弱國。", "第28題題型改編"),
    ("第一次世界大戰爆發後，哪個國家由原本的同盟關係轉而加入協約國？", ["義大利", "俄國", "美國", "中國"], "A", "義大利原屬三國同盟，戰爭期間改加入協約國。", "第29題題型改編"),
    ("德國在第一次世界大戰前擴張海軍，最可能造成哪項影響？", ["加劇英德競爭並動搖歐洲均勢", "促成歐洲永久和平", "使殖民地立即獨立", "終止軍備競賽"], "A", "海軍擴張提高英德間的戰略競爭，增加歐洲均勢的不穩定。", "第30題題型改編"),
    ("第一次世界大戰期間，德軍在法國境內作戰，最可能對應哪個年份？", ["1915 年", "1815 年", "1870 年", "1945 年"], "A", "第一次世界大戰發生於 1914 至 1918 年，1915 年符合題幹時代。", "第31題題型改編"),
    ("第一次世界大戰後的巴黎和會，哪個國家以戰敗國身分不能作為主要勝方參與決策？", ["德國", "中國", "日本", "義大利"], "A", "德國是戰敗國，巴黎和會的主要決策由戰勝國主導。", "第32題題型改編"),
]

answer_positions = ["B", "C", "D", "B", "C", "D", "B", "C", "D", "A"]
for index, (prompt, options, answer, explanation, locator) in enumerate(rows, 1):
    path = ROOT / "questions" / "social" / f"question-social-content-hist-qa-iv-3-{index}.json"
    data = json.loads(path.read_text(encoding="utf-8"))
    target = ord(answer_positions[index - 1]) - ord("A")
    options = options[1:target + 1] + options[:1] + options[target + 1:]
    answer = answer_positions[index - 1]
    data.update({
        "prompt": prompt,
        "options": [{"id": chr(65 + i), "text": text} for i, text in enumerate(options)],
        "answer": {"value": answer, "explanation": explanation},
        "difficulty": "medium",
        "knowledgeIds": [KID],
        "lessonId": LESSON,
        "provenance": {"origin": "original", "license": "All rights reserved", "sourceUrl": SOURCE, "sourceLocator": f"高雄市立鹽埕國中 114 學年度第 2 學期三年級第 1 次段考社會科歷史科；{locator}；獨立改編，非原題重製。"},
        "reviewStatus": "draft",
        "updatedAt": "2026-08-28",
    })
    path.write_text(json.dumps(data, ensure_ascii=False, indent=2) + "\n", encoding="utf-8")
print(f"replaced {len(rows)} Social Studies questions")
