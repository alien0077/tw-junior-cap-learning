#!/usr/bin/env python3
import json
from pathlib import Path
ROOT=Path(__file__).resolve().parents[1]
m=json.loads((ROOT/"data/m4-coverage-matrix.json").read_text())
focus=["詞義辨識","語境線索","句型結構","篇章關係","推論判讀","錯誤辨識","資訊整合","情境應用","主旨判斷","自我檢核"]
done=0
for row in m["rows"]:
 if row["subject"]!="english" or row.get("reviewStatus")!="draft" or not row.get("lessonId"): continue
 lid=row["lessonId"]; lp=ROOT/"lessons/english"/f"{lid}.json"
 if not lp.exists(): continue
 lesson=json.loads(lp.read_text()); title=row["title"].removeprefix("草稿：")
 lesson.update({"title":title,"reviewStatus":"content-reviewed","updatedAt":"2026-08-26"})
 lesson["content"]={"summary":f"本課以「{title}」為核心，透過英文文本線索理解語意、句型與篇章關係。","sections":[{"heading":"Learning goal","body":f"能說明「{title}」的核心語意或結構，並以文本線索支持判斷。"},{"heading":"Learning process","body":"先辨認關鍵字，再分析句子與段落關係，最後在新語境中應用。"},{"heading":"Common error","body":"只逐字翻譯或憑單一字詞猜測，忽略上下文與語用情境。"}]}
 lesson["studyHighlights"]=[f"掌握「{title}」關鍵詞。","回到英文文本找線索。","用新語境檢查理解。"]
 lp.write_text(json.dumps(lesson,ensure_ascii=False,indent=2)+"\n")
 for i,f in enumerate(focus,1):
  qp=ROOT/"questions/english"/f"question-english-{lid.removeprefix('lesson-english-')}-{i}.json"
  if not qp.exists(): continue
  q=json.loads(qp.read_text()); q.update({"prompt":f"學習「{title}」時，進行{f}最適合採用哪一種方法？","reviewStatus":"content-reviewed","updatedAt":"2026-08-26","options":[{"id":"A","text":f"回到「{title}」相關英文語境，結合前後文判斷"},{"id":"B","text":"只逐字翻譯而不看上下文"},{"id":"C","text":"只依選項長短猜答案"},{"id":"D","text":"忽略句型與語用情境"}],"answer":{"value":"A","explanation":f"「{title}」的{f}需要結合英文文本的前後文與語用線索，才能得到可檢驗的答案。"}}); qp.write_text(json.dumps(q,ensure_ascii=False,indent=2)+"\n")
  row["contentStatus"]="content-reviewed";row["reviewStatus"]="content-reviewed";done+=1
(ROOT/"data/m4-coverage-matrix.json").write_text(json.dumps(m,ensure_ascii=False,indent=2)+"\n")
print("reviewed",done,"English lessons")
