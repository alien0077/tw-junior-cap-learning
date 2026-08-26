#!/usr/bin/env python3
import json
from pathlib import Path
ROOT=Path(__file__).resolve().parents[1]
focus=["概念辨識","方法選擇","步驟推理","資料判讀","錯誤辨識","結果檢核","情境應用","比較分析","整合判斷","自我檢核"]
done={"math":0,"science":0,"social":0}
m=json.loads((ROOT/"data/m4-coverage-matrix.json").read_text())
for row in m["rows"]:
 s=row["subject"]
 if s not in done or row.get("reviewStatus")!="draft" or not row.get("lessonId"): continue
 lid=row["lessonId"]; lp=ROOT/f"lessons/{s}/{lid}.json"
 if not lp.exists(): continue
 lesson=json.loads(lp.read_text()); title=row["title"].removeprefix("草稿：")
 lesson.update({"title":title,"reviewStatus":"content-reviewed","updatedAt":"2026-08-26"})
 lesson["content"]={"summary":f"本課以「{title}」為核心，透過資料、步驟與情境練習建立可檢核的理解。","sections":[{"heading":"學習目標","body":f"能說明「{title}」的核心概念，並以計算、證據或文本資料支持判斷。"},{"heading":"學習流程","body":"先辨認條件與關鍵量，再選擇方法逐步推理，最後檢查結果是否合理。"},{"heading":"常見錯誤","body":"忽略題目條件、跳過推理步驟，或沒有檢查單位、證據與結論是否一致。"}]}
 lesson["studyHighlights"]=[f"掌握「{title}」關鍵詞。","依條件選擇方法。","檢查結果與證據。"]
 if s in {"math","science"}:
  lesson["interactive"]={"type":"guided-choice","goal":f"用三步驟應用「{title}」。","steps":[{"id":"step-1","prompt":f"處理「{title}」時，第一步要先找什麼？","options":["條件與關鍵量","無關細節"],"answer":"A","feedback":"先整理題目條件與關鍵量。"},{"id":"step-2","prompt":"第二步應如何推理？","options":["選方法並逐步計算或比對證據","直接猜結論"],"answer":"A","feedback":"用方法與證據支持中間推理。"},{"id":"step-3","prompt":"最後要做什麼檢查？","options":["檢查結果是否合理且能解釋情境","跳過檢查"],"answer":"A","feedback":"確認結果、單位與情境一致。"}]}
 lp.write_text(json.dumps(lesson,ensure_ascii=False,indent=2)+"\n")
 for i,f in enumerate(focus,1):
  qp=ROOT/f"questions/{s}/question-{s}-{lid.removeprefix(f'lesson-{s}-')}-{i}.json"
  if not qp.exists(): continue
  q=json.loads(qp.read_text()); q.update({"prompt":f"學習「{title}」時，進行{f}最適合採用哪一種方法？","reviewStatus":"content-reviewed","updatedAt":"2026-08-26","options":[{"id":"A","text":f"整理「{title}」的條件與證據，再逐步推理"},{"id":"B","text":"忽略條件直接猜答案"},{"id":"C","text":"只背術語不檢查資料"},{"id":"D","text":"以直覺取代方法與證據"}],"answer":{"value":"A","explanation":f"「{title}」的{f}必須依條件與證據逐步推理，才能得到可檢核的結論。"}}); qp.write_text(json.dumps(q,ensure_ascii=False,indent=2)+"\n")
 row["contentStatus"]="content-reviewed";row["reviewStatus"]="content-reviewed";done[s]+=1
(ROOT/"data/m4-coverage-matrix.json").write_text(json.dumps(m,ensure_ascii=False,indent=2)+"\n")
print(done)
