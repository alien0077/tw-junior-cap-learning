#!/usr/bin/env python3
"""Materialize a bounded batch of M4 draft lessons and questions."""
from __future__ import annotations
import argparse, json
from pathlib import Path
ROOT=Path(__file__).resolve().parents[1]
def main()->int:
 ap=argparse.ArgumentParser();ap.add_argument("--subject",required=True,choices=["chinese","english","math","science","social"]);ap.add_argument("--limit",type=int,default=5);a=ap.parse_args()
 mp=ROOT/"data/m4-coverage-matrix.json";m=json.loads(mp.read_text())
 kg_by_curriculum={}
 for graph_path in (ROOT/"knowledge").glob("*/foundational-graph.json"):
  graph=json.loads(graph_path.read_text())
  for node in graph.get("nodes",[]):
   for curriculum_id in node.get("curriculumIds",[]): kg_by_curriculum[curriculum_id]=node["id"]
 rows=[r for r in m["rows"] if r["subject"]==a.subject and not r.get("lessonId")][:a.limit]
 for r in rows:
  key=r["curriculumId"].removeprefix("cur-");lid=f"lesson-{a.subject}-{key[len(a.subject)+1:] if key.startswith(a.subject+'-') else key}";kg=kg_by_curriculum.get(r["curriculumId"]);ld=ROOT/"lessons"/a.subject;qd=ROOT/"questions"/a.subject;ld.mkdir(parents=True,exist_ok=True);qd.mkdir(parents=True,exist_ok=True)
  if not kg: raise ValueError(f"missing KG endpoint for {r['curriculumId']}")
  lesson={"id":lid,"subject":a.subject,"title":f"草稿：{r['title']}","knowledgeIds":[kg],"gradeRange":r.get("gradeRange",["7","8","9"]),"content":{"summary":f"依課綱「{r['title']}」建立的 M4 草稿，待學科 QA。","sections":[{"heading":"學習目標（草稿）","body":f"能說明「{r['title']}」的核心概念。"},{"heading":"學習步驟（草稿）","body":"整理關鍵詞，閱讀例子，再用新情境檢查理解。"}]},"studyHighlights":["先抓課綱關鍵詞。","用例子驗證理解。","回看常見錯誤。"],"studyReferences":["https://www.naer.edu.tw/"],"provenance":{"origin":"original","license":"All rights reserved","authoringNote":"Batch-generated draft; subject QA required."},"reviewStatus":"draft","updatedAt":"2026-08-26"}
  if a.subject in {"math","science"}: lesson["interactive"]={"type":"guided-choice","goal":f"用步驟檢查「{r['title']}」的理解。","steps":[{"id":"step-1","prompt":"先找出題目的核心概念？","options":["核心概念","無關細節"],"answer":"A","feedback":"先定位課綱關鍵詞。"},{"id":"step-2","prompt":"接著應採取哪種方法？","options":["依概念整理證據","只猜答案"],"answer":"A","feedback":"以證據或計算支持判斷。"},{"id":"step-3","prompt":"最後如何檢查？","options":["套用新情境驗證","跳過檢查"],"answer":"A","feedback":"用新情境確認能遷移應用。"}]}
  (ld/f"{lid}.json").write_text(json.dumps(lesson,ensure_ascii=False,indent=2)+"\n")
  for i in range(1,11):
   q={"id":f"question-{a.subject}-{key[len(a.subject)+1:] if key.startswith(a.subject+'-') else key}-{i}","subject":a.subject,"type":"single-choice","prompt":f"【草稿】學習「{r['title']}」時，哪一項最符合課綱學習方向？","options":[{"id":"A","text":f"理解「{r['title']}」並能應用"},{"id":"B","text":"只記頁碼"},{"id":"C","text":"只背選項順序"},{"id":"D","text":"跳過學習目標"}],"knowledgeIds":[kg],"difficulty":"easy" if i<=3 else "medium","answer":{"value":"A","explanation":f"本題檢查「{r['title']}」的核心理解與應用。"},"provenance":{"origin":"original","license":"All rights reserved"},"reviewStatus":"draft","updatedAt":"2026-08-26","lessonId":lid};(qd/f"{q['id']}.json").write_text(json.dumps(q,ensure_ascii=False,indent=2)+"\n")
  r.update({"lessonId":lid,"questionCount":10,"contentStatus":"draft","reviewStatus":"draft"})
 m["summary"]["questionsCovered"]=sum(r.get("questionCount",0)>=10 for r in m["rows"]);mp.write_text(json.dumps(m,ensure_ascii=False,indent=2)+"\n");print(f"materialized {len(rows)} {a.subject} draft lessons and {len(rows)*10} draft questions");return 0
if __name__=="__main__":raise SystemExit(main())
