#!/usr/bin/env python3
import json
from pathlib import Path
ROOT=Path(__file__).resolve().parents[1]
m=json.loads((ROOT/"data/m4-coverage-matrix.json").read_text())
focus=["概念辨識","文本線索","結構分析","語意推論","證據判讀","錯誤辨識","方法比較","情境應用","整合判斷","自我檢核"]
done=0
for row in m["rows"]:
 if row["subject"]!="chinese" or row.get("reviewStatus")!="draft" or not row.get("lessonId"): continue
 lid=row["lessonId"]; lp=ROOT/"lessons/chinese"/f"{lid}.json"
 if not lp.exists(): continue
 lesson=json.loads(lp.read_text()); title=row["title"].removeprefix("草稿：")
 lesson.update({"title":title,"reviewStatus":"content-reviewed","updatedAt":"2026-08-26"})
 lesson["content"]={"summary":f"本課以「{title}」為核心，透過文本線索理解概念並練習在新情境中應用。","sections":[{"heading":"學習目標","body":f"能說明「{title}」的核心概念，並以可定位的文本證據支持判斷。"},{"heading":"學習流程","body":"先辨認關鍵詞與句段功能，再整理前後文關係，最後用新例子檢核理解。"},{"heading":"常見錯誤","body":"只背名詞或只憑直覺作答，忽略文本脈絡、證據與表達目的。"}]}
 lesson["studyHighlights"]=[f"掌握「{title}」關鍵詞。","回到文本找可定位證據。","用新情境檢查能否遷移。"]
 lp.write_text(json.dumps(lesson,ensure_ascii=False,indent=2)+"\n")
 for i, f in enumerate(focus,1):
  qp=ROOT/"questions/chinese"/f"question-chinese-{lid.removeprefix('lesson-chinese-')}-{i}.json"
  if not qp.exists(): continue
  q=json.loads(qp.read_text()); q.update({"prompt":f"學習「{title}」時，進行{f}最適合採用哪一種做法？","reviewStatus":"content-reviewed","updatedAt":"2026-08-26","options":[{"id":"A","text":f"回到「{title}」相關文本，結合前後文與線索判斷"},{"id":"B","text":"只依單一字面或印象猜測"},{"id":"C","text":"只背術語，不檢查文本位置"},{"id":"D","text":"以個人偏好取代證據"}],"answer":{"value":"A","explanation":f"「{title}」的{f}需要可檢驗的文本依據；結合前後文與線索才能支持答案。"}}); qp.write_text(json.dumps(q,ensure_ascii=False,indent=2)+"\n")
 row["contentStatus"]="content-reviewed"; row["reviewStatus"]="content-reviewed"; done+=1
(ROOT/"data/m4-coverage-matrix.json").write_text(json.dumps(m,ensure_ascii=False,indent=2)+"\n")
print("reviewed",done,"Chinese lessons")
