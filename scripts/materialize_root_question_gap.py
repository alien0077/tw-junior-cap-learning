#!/usr/bin/env python3
"""Materialize the seven audited root-KG question gaps.

These are original draft questions grounded only in the repository's official
curriculum records. They are intentionally left draft until AI content QA.
"""
from __future__ import annotations

import json
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]

URLS = {
    "chinese": "https://www.naer.edu.tw/upload/1/16/doc/806/%E5%8D%81%E4%BA%8C%E5%B9%B4%E5%9C%8B%E6%B0%91%E5%9F%BA%E6%9C%AC%E6%95%99%E8%82%B2%E8%AA%B2%E7%A8%8B%E7%B6%B1%E8%A6%81%E5%9C%8B%E6%B0%91%E4%B8%AD%E5%B0%8F%E5%AD%B8%E6%9A%A8%E6%99%AE%E9%80%9A%E5%9E%8B%E9%AB%98%E7%B4%9A%E4%B8%AD%E7%AD%89%E5%AD%B8%E6%A0%A1(%E8%AA%9E%E6%96%87%E9%A0%98%E5%9F%9F%E2%94%80%E5%9C%8B%E8%AA%9E%E6%96%87).pdf",
    "english": "https://www.naer.edu.tw/upload/1/16/doc/812/(%E7%99%BC%E5%B8%83%E7%89%88)%E5%9C%8B%E6%B0%91%E4%B8%AD%E5%B0%8F%E5%AD%B8%E6%9A%A8%E6%99%AE%E9%80%9A%E5%9E%8B%E9%AB%98%E7%B4%9A%E4%B8%AD%E7%AD%89%E5%AD%B8%E6%A0%A1-%E8%AA%9E%E6%96%87%E9%A0%98%E5%9F%9F-%E8%8B%B1%E8%AA%9E%E6%96%87%E8%AA%B2%E7%A8%8B%E7%B6%B1%E8%A6%81.pdf",
    "math": "https://www.naer.edu.tw/upload/1/16/doc/815/%E5%8D%81%E4%BA%8C%E5%B9%B4%E5%9C%8B%E6%B0%91%E5%9F%BA%E6%9C%AC%E6%95%99%E8%82%B2%E8%AA%B2%E7%A8%8B%E7%B6%B1%E8%A6%81%E5%9C%8B%E6%B0%91%E4%B8%AD%E5%B0%8F%E5%AD%B8%E6%9A%A8%E6%99%AE%E9%80%9A%E5%9E%8B%E9%AB%98%E7%B4%9A%E4%B8%AD%E7%AD%89%E5%AD%B8%E6%A0%A1-%E6%95%B8%E5%AD%B8%E9%A0%98%E5%9F%9F.pdf",
    "science": "https://www.naer.edu.tw/upload/1/16/doc/820/%E5%8D%81%E4%BA%8C%E5%B9%B4%E5%9C%8B%E6%B0%91%E5%9F%BA%E6%9C%AC%E6%95%99%E8%82%B2%E8%AA%B2%E7%B6%B1%E8%A6%81%E5%9C%8B%E6%B0%91%E4%B8%AD%E5%B0%8F%E5%AD%B8%E6%9A%A8%E6%99%AE%E9%80%9A%E5%9E%8B%E9%AB%98%E7%B4%9A%E4%B8%AD%E7%AD%89%E5%AD%B8%E6%A0%A1-%E8%87%AA%E7%84%B6%E7%A7%91%E5%AD%B8%E9%A0%98%E5%9F%9F.pdf",
}

REPRESENTATIVE_LESSONS = {
    ("chinese", "a"): ("lesson-chinese-content-ac-iv-3", "kg-chinese-content-ac-iv-3"),
    ("chinese", "b"): ("lesson-chinese-content-ba", "kg-chinese-content-ba"),
    ("english", "a"): ("lesson-english-content-ab-iv-2", "kg-english-content-ab-iv-2"),
    ("english", "b"): ("lesson-english-content-b-iv-7", "kg-english-content-b-iv-7"),
    ("math", "a"): ("lesson-math-content-a-8-2", "kg-math-content-a-8-2"),
    ("science", "a"): ("lesson-science-content-ab-iv-2", "kg-science-content-ab-iv-2"),
    ("science", "b"): ("lesson-science-content-ba-iv-3", "kg-science-content-ba-iv-3"),
}

QUESTIONS = [
  ("chinese", "a", "文字篇章", "正文先提出問題，接著依時間順序記錄觀察，最後回到問題作結。這段安排最需要讀者掌握哪種關係？", [("A", "事件或資訊的先後與轉折"), ("B", "每句字數必須相同"), ("C", "所有句子都要押韻"), ("D", "作者姓名的筆畫" )], "A", "依時間順序整理材料時，先後與轉折是理解篇章發展的關鍵；其他選項不是篇章關係。"),
  ("chinese", "a", "文字篇章", "讀者先找出文章反覆回答的問題，再比較開頭與結尾的說法。這樣做最能協助判斷什麼？", [("A", "篇章主旨如何由材料逐步收束"), ("B", "每個字的部首數量"), ("C", "印刷頁面的紙張大小"), ("D", "作者是否使用同一個標點" )], "A", "比較問題、材料與收束能連結篇章整體意思，不能只靠字形或版面判定主旨。"),
  ("chinese", "a", "文字篇章", "一段文字先描述現象，再提出兩個可能原因，最後說明還需要哪些資料才能判斷。讀者最適合把它看成哪種閱讀任務？", [("A", "辨認說明、推論與證據限制"), ("B", "只背誦最後一句"), ("C", "只計算段落行數"), ("D", "只挑最長的句子" )], "A", "文字同時呈現現象、可能原因與資料限制，應區分文本明示內容與需要證據支持的推論。"),
  ("chinese", "b", "文本表述", "同一項校園提案要向校長說明，也要向同學宣傳。下列哪個做法最符合文本表述的調整？", [("A", "依受眾改變用詞、證據與說明重點"), ("B", "兩種場合完全複製同一段話"), ("C", "只增加感嘆號就算完成"), ("D", "刪去所有具體資料" )], "A", "文本表述需配合目的與受眾，調整語氣、資訊與證據；只改標點或刪資料不足以完成溝通。"),
  ("chinese", "b", "文本表述", "要把一則觀察寫成可查證的說明，下列哪個句子最適合作為初稿？", [("A", "本次記錄在三天內於同一時段完成，觀察到兩種結果"), ("B", "這一定是全校最好的方法"), ("C", "大家都知道它絕對有效"), ("D", "我覺得不用再看資料" )], "A", "A保留觀察範圍與結果，較能讓讀者理解資料界線；其餘句子過度斷言或缺乏可查證內容。"),
  ("chinese", "b", "文本表述", "小組要寫一段議論文字支持增加遮蔭座位，哪一組材料最能形成主張與論據的對應？", [("A", "主張需求增加；附上不同時段的座位使用紀錄"), ("B", "主張需求增加；附上最喜歡的顏色"), ("C", "主張需求增加；附上與座位無關的校徽介紹"), ("D", "主張需求增加；只重複主張三次" )], "A", "使用紀錄直接回應座位需求，能作為論據；偏好、無關資訊或重複主張不能取代證據。"),
  ("english", "a", "語言知識", "Which sentence uses a verb form that matches a repeated action happening every Saturday?", [("A", "Mia practices the piano every Saturday."), ("B", "Mia practiced the piano every Saturday now."), ("C", "Mia practicing the piano every Saturday."), ("D", "Mia practice the piano every Saturday yesterday." )], "A", "The present simple fits a repeated weekly action, and the third-person singular subject takes practices."),
  ("english", "a", "語言知識", "In the sentence 'The bottle is reusable, so we can use it again,' what does 'reusable' tell the reader?", [("A", "It can be used again."), ("B", "It must be thrown away."), ("C", "It is already empty."), ("D", "It is made only of paper." )], "A", "The prefix and context indicate that reusable means able to be used again."),
  ("english", "a", "語言知識", "Which choice keeps the meaning of 'Although it was raining, the team continued the game'?", [("A", "The team continued the game even though it was raining."), ("B", "The team stopped before it rained."), ("C", "The team played only because there was no rain."), ("D", "The team caused the rain to stop." )], "A", "Although introduces a contrast: rain happened, but the team continued."),
  ("english", "b", "溝通功能", "A classmate says, 'I cannot find the science room.' Which reply best asks for clarification before giving directions?", [("A", "Which building are you standing near?"), ("B", "Science is always easy."), ("C", "I finished my homework."), ("D", "The room was bright yesterday." )], "A", "The question requests the location information needed to give useful directions."),
  ("english", "b", "溝通功能", "You disagree with a partner's plan but want to keep the discussion constructive. Which sentence is most appropriate?", [("A", "I see your idea; could we compare it with another option?"), ("B", "Your idea is stupid."), ("C", "I will ignore everyone."), ("D", "There is no reason to explain." )], "A", "A acknowledges the partner and invites comparison, which supports respectful discussion."),
  ("english", "b", "溝通功能", "A notice says a library workshop starts at 3:30 p.m. and registration closes Friday. Which response shows the reader understood both functions?", [("A", "I should register before Friday and arrive by 3:30 p.m."), ("B", "I should arrive Friday at midnight."), ("C", "I should register after the workshop."), ("D", "I should ignore the time and date." )], "A", "The response combines the deadline for registration with the event start time."),
  ("math", "a", "代數", "若用 x 表示一本筆記本的單價，買 4 本再加 15 元運費，哪個式子表示總費用？", [("A", "4x+15"), ("B", "x+4+15"), ("C", "4(x+15)"), ("D", "x/(4+15)" )], "A", "四本的費用是4x，運費只加一次，因此總費用為4x+15。"),
  ("math", "a", "代數", "方程式 3x+2=14 中，若先從等號兩邊同時減去 2，下一步得到什麼？", [("A", "3x=12"), ("B", "3x=16"), ("C", "x=12"), ("D", "3x+4=14" )], "A", "等式兩邊同時減2可保持相等，左邊剩3x，右邊為12。"),
  ("math", "a", "代數", "某數的兩倍比 5 多 7。若以 x 表示該數，哪個方程式正確表達題意？", [("A", "2x=5+7"), ("B", "x+2=5+7"), ("C", "2(x+5)=7"), ("D", "5x=2+7" )], "A", "兩倍是2x，比5多7表示2x=5+7；其他式子的運算關係與文字不符。"),
  ("science", "a", "物質的組成與特性", "下列哪項觀察最能支持『樣品是混合物』而不是單一純物質？", [("A", "同一樣品分出兩部分後可觀察到不同成分特徵"), ("B", "樣品只有一種顏色"), ("C", "樣品放在透明容器中"), ("D", "樣品的名稱只有兩個字" )], "A", "可分出具有不同成分特徵的部分，才直接支持含有多種物質；顏色、容器或名稱不能單獨判定。"),
  ("science", "a", "物質的組成與特性", "把冰塊融化成水，若沒有產生新物質，這個例子主要呈現哪一種變化？", [("A", "物理變化"), ("B", "化學變化"), ("C", "元素變成另一元素"), ("D", "化合物分解成不同元素" )], "A", "固態水變成液態水，物質本身仍是水，屬於狀態改變的物理變化。"),
  ("science", "a", "物質的組成與特性", "要比較兩種粉末是否由相同物質組成，哪項策略最符合證據導向的判斷？", [("A", "在相同條件下比較可測量的性質並記錄結果"), ("B", "只看包裝顏色"), ("C", "只聞一次就下結論"), ("D", "依粉末名稱長短判斷" )], "A", "相同條件下的可測量性質能提供可比較證據；外觀或單次主觀感受不足以確定組成。"),
  ("science", "b", "能量的形式、轉換及流動", "電池驅動小馬達時，能量轉換的合理描述是哪一項？", [("A", "化學能轉換成電能，再帶動機械運動"), ("B", "機械能消失且沒有任何轉換"), ("C", "光能必定直接變成聲能"), ("D", "溫度單位變成電流" )], "A", "電池的化學能經由電路供應電能，馬達再把部分能量轉成機械運動。"),
  ("science", "b", "能量的形式、轉換及流動", "兩杯水溫度不同放在一起，若最後趨於相同溫度，最合理的解釋是什麼？", [("A", "熱能由高溫處傳向低溫處，直到達到熱平衡"), ("B", "低溫水把溫度單位傳給高溫水"), ("C", "兩杯水都沒有能量改變"), ("D", "熱只能由低溫流向高溫" )], "A", "在一般接觸情況下，能量由高溫處傳向低溫處，溫差減小後達到熱平衡。"),
  ("science", "b", "能量的形式、轉換及流動", "同一盞燈在不同電壓下亮度不同。若要探究原因，哪個設計最能保留因果判斷？", [("A", "只改變電壓，其他條件相同並記錄亮度"), ("B", "同時更換燈泡、電池與測量時間"), ("C", "只問同學覺得哪盞較亮"), ("D", "先決定答案再挑選資料" )], "A", "一次只改變一個主要變因並控制其他條件，才能把亮度差異與電壓變化連結。"),
]

def main() -> int:
    out_dir = ROOT / "questions/generated"
    out_dir.mkdir(parents=True, exist_ok=True)
    written = []
    for index, (subject, root, topic, prompt, options, answer, explanation) in enumerate(QUESTIONS, 1):
        kg = f"kg-{subject}-content-{root}"
        lesson, representative_kg = REPRESENTATIVE_LESSONS[(subject, root)]
        locator = {"chinese": f"國民中學教育階段學習內容；主題 {root.upper()}：{topic}", "english": f"國民中學教育階段學習內容；主題 {root.upper()}：{topic}", "math": "國民中學教育階段學習內容；主題 A：代數", "science": f"國民中學教育階段學習內容；主題 {root.upper()}：{topic}"}[subject]
        qid = f"question-{subject}-root-{root}-{index:02d}"
        question = {"id": qid, "subject": subject, "type": "single-choice", "prompt": prompt, "options": [{"id": key, "text": value} for key, value in options], "knowledgeIds": [kg, representative_kg], "difficulty": "medium", "answer": {"value": answer, "explanation": explanation}, "provenance": {"origin": "original", "license": "All rights reserved", "sourceUrl": URLS[subject], "sourceLocator": locator, "authoringNote": "依官方課綱與 KG 範圍原創命題，非公開試題或教材重製。"}, "reviewStatus": "draft", "updatedAt": "2026-09-06", "lessonId": lesson}
        path = out_dir / f"{qid}.json"
        path.write_text(json.dumps(question, ensure_ascii=False, indent=2) + "\n", encoding="utf-8")
        written.append(str(path))
    print(json.dumps({"written": len(written), "files": written}, ensure_ascii=False))
    return 0

if __name__ == "__main__":
    raise SystemExit(main())
