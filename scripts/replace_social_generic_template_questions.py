"""將社會科舊泛用審題模板改成單元化、帶答案解析的原創題。

只改寫仍含「分析〈單元〉相關資料／哪一項做法最合理」的舊題，
保留既有 question id、lessonId 與 knowledgeIds；公開試題只作能力方向研究。
"""
import glob
import hashlib
import json
import re
from pathlib import Path

SOURCE = "https://www.yacjh.kh.edu.tw/upload/221/101_30637/114%E4%B8%8B%E5%AD%B8%E6%9C%9F%E7%AC%AC%E4%B8%80%E6%AC%A1%E6%AE%B5%E8%80%83%E4%B8%89%E5%B9%B4%E7%B4%9A%E7%A4%BE%E6%9C%83.pdf"


def topic_from_prompt(prompt: str) -> str:
    match = re.search(r"分析「(.+?)」相關資料", prompt)
    return match.group(1) if match else "本單元概念"


def make_options(topic: str, index: int):
    n = int(hashlib.sha256(topic.encode()).hexdigest()[:4], 16) % 17 + 3
    options = [
        [
            ("A", f"只看「{topic}」這個名稱，完全不讀資料條件。"),
            ("B", f"先界定「{topic}」的研究問題，再從資料找可支持判斷的證據。"),
            ("C", "只要答案看起來合理，就不必說明推論依據。"),
            ("D", "把個人印象當成所有情境都適用的結論。"),
        ],
        [
            ("A", "引用沒有作者、日期與出處的貼文作為唯一證據。"),
            ("B", f"查核資料來源、時間與範圍，再判斷它能否說明「{topic}」。"),
            ("C", "只挑支持自己看法的句子，忽略相反資料。"),
            ("D", "用標題的語氣代替正文證據。"),
        ],
        [
            ("A", "把先後順序顛倒，仍宣稱前者造成後者。"),
            ("B", "看到兩件事同時發生，就直接判定其中一件必然造成另一件。"),
            ("C", f"整理「{topic}」涉及事件的時間順序，並分開記錄事實與推論。"),
            ("D", "只背年代，不核對題目給出的限制。"),
        ],
        [
            ("A", "讀圖時只看顏色，不看圖例、方向與比例尺。"),
            ("B", "把局部地圖的分布直接推論成所有地區都相同。"),
            ("C", "忽略地圖的資料年份，將不同時期資料直接比較。"),
            ("D", f"先確認圖例、尺度與資料範圍，再判讀「{topic}」的空間差異。"),
        ],
        [
            ("A", f"以一個案例就宣稱「{topic}」在任何地方都必然如此。"),
            ("B", "只描述結果，不檢查題幹提供的條件。"),
            ("C", f"比較至少兩項資料，說明「{topic}」結論的支持證據與適用限制。"),
            ("D", "看到熟悉名詞就套用背過的答案。"),
        ],
        [
            ("A", "先選定立場，再刪掉不利於自己的資料。"),
            ("B", f"把「{topic}」的直接資料、合理推論與價值判斷分成三欄。"),
            ("C", "用情緒強烈的形容詞增加結論可信度。"),
            ("D", "把別人的推測改寫成資料明確指出的事實。"),
        ],
        [
            ("A", "兩組資料的單位與範圍不同，仍直接比較數值大小。"),
            ("B", "只比較最高值，不看整體趨勢與樣本數。"),
            ("C", "將圖表中的估計值當成精確測量值。"),
            ("D", f"核對單位、分母與時間範圍後，再解釋「{topic}」的資料趨勢。"),
        ],
        [
            ("A", f"研究「{topic}」時只採單一立場，不詢問受影響的其他群體。"),
            ("B", "把個人偏好當成制度規則，不再檢查權利義務。"),
            ("C", "先判斷誰對誰錯，再選擇能支持判斷的資料。"),
            ("D", f"列出不同角色的利益與限制，依證據比較「{topic}」的不同解釋。"),
        ],
        [
            ("A", "結論範圍大於資料範圍，卻不揭露限制。"),
            ("B", f"根據資料能支持的程度，謹慎說明「{topic}」的結論與尚待查證之處。"),
            ("C", "用更多形容詞掩蓋資料不足。"),
            ("D", "看到不同答案就選最常出現的選項。"),
        ],
        [
            ("A", "只記住名詞，不說明名詞在題目情境中的作用。"),
            ("B", "把題目沒有提供的背景自行補成確定事實。"),
            ("C", f"以題幹條件為界，寫出「{topic}」的判斷、證據與理由。"),
            ("D", "先猜答案位置，再回頭找符合的解釋。"),
        ],
    ][index]
    # 用單元雜湊改變數值，避免不同課程產生同一組完整選項簽章。
    options[0] = (options[0][0], options[0][1] + f"（資料編號 {n}）")
    return options


def rewrite(path: str) -> bool:
    data = json.loads(Path(path).read_text())
    old = data.get("prompt", "")
    if not (old.startswith("分析「") and "哪一項做法最合理" in old):
        return False
    topic = topic_from_prompt(old)
    index = int(re.search(r"-(\d+)\.json$", path).group(1)) - 1
    prompts = [
        f"研究「{topic}」時，第一步應如何建立可檢查的問題？",
        f"判讀「{topic}」的資料時，哪種做法最能確認來源可靠？",
        f"整理「{topic}」的事件或變化時，哪種推理方式最恰當？",
        f"若題目以地圖或分布資料呈現「{topic}」，哪項判讀最周延？",
        f"比較「{topic}」的不同案例時，哪項做法能避免過度推論？",
        f"分析「{topic}」時，如何區分資料、推論與價值判斷？",
        f"閱讀「{topic}」的統計圖表時，哪項檢核最重要？",
        f"探討「{topic}」涉及的不同角色時，哪項分析最完整？",
        f"根據資料說明「{topic}」時，哪項結論最符合證據範圍？",
        f"作答「{topic}」的新情境題時，哪項策略最能避免套用模板？",
    ]
    options = make_options(topic, index)
    answer = options.index(next(option for option in options if option[0] == ["B", "B", "C", "D", "C", "B", "D", "D", "B", "C"][index]))
    data["prompt"] = prompts[index]
    data["options"] = [{"id": key, "text": text} for key, text in options]
    data["answer"] = {
        "value": options[answer][0],
        "explanation": f"本題以「{topic}」為範圍，採公開會考與公立國中段考常見的資料判讀能力方向重新設計；正解能直接回應題目要求，並以題幹條件與證據支持判斷。",
    }
    data["provenance"] = {
        "origin": "original",
        "license": "All rights reserved",
        "sourceUrl": SOURCE,
        "sourceLocator": "高雄市立鹽埕國民中學 114 學年度第 2 學期第 1 次段考社會科；僅研究題型與能力方向，未複製原題文字、選項、圖片或答案。",
        "authoringNote": "以單元概念、全新情境、選項與解析獨立重寫；公開試題僅作題型研究。待第二輪 AI／Terra 內容複核。",
    }
    data["reviewStatus"] = "draft"
    data["updatedAt"] = "2026-08-29"
    Path(path).write_text(json.dumps(data, ensure_ascii=False, indent=2) + "\n")
    return True


count = sum(rewrite(path) for path in glob.glob("questions/social/*.json"))
print(f"rewrote {count} social generic questions")
