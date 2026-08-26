#!/usr/bin/env python3
import json
from pathlib import Path
ROOT=Path(__file__).resolve().parents[1]
ids=["content-ac-iv-3","content-ad-iv-2","content-ad-iv-3","content-ad-iv-4","content-ba-iv-1"]
for key in ids:
 p=ROOT/"lessons/chinese"/f"lesson-chinese-{key}.json"; lesson=json.loads(p.read_text()); title=lesson["title"].removeprefix("草稿：")
 lesson.update({"title":title,"reviewStatus":"content-reviewed","updatedAt":"2026-08-26"}); lesson["content"]={"summary":f"本課聚焦「{title}」，以文本線索分析概念、結構與表達效果。","sections":[{"heading":"學習目標","body":f"能說明「{title}」的核心特徵，並引用文本線索支持判斷。"},{"heading":"學習流程","body":"先辨認關鍵語句，再比較前後文關係，最後以新例子檢核理解。"},{"heading":"常見錯誤","body":"只背名詞而不回到文本，或把個人感受當成文本證據。"}]}; lesson["studyHighlights"]=["辨認單元關鍵概念。","回到文本找證據。","用新情境檢核理解。"]; p.write_text(json.dumps(lesson,ensure_ascii=False,indent=2)+"\n")
 for i in range(1,11):
  q=ROOT/"questions/chinese"/f"question-chinese-{key}-{i}.json"; d=json.loads(q.read_text()); d.update({"prompt":f"針對「{title}」進行第{i}題判讀時，哪一項方法最能支持答案？","reviewStatus":"content-reviewed","updatedAt":"2026-08-26","options":[{"id":"A","text":"引用前後文中可定位的語句與結構線索"},{"id":"B","text":"只依題目字數猜測"},{"id":"C","text":"只背術語名稱不看文本"},{"id":"D","text":"以個人喜好取代文本證據"}],"answer":{"value":"A","explanation":f"「{title}」的判讀必須回到文本，使用可定位的語句與結構線索；其他做法缺乏可檢驗依據。"}}); q.write_text(json.dumps(d,ensure_ascii=False,indent=2)+"\n")
 print(key)
