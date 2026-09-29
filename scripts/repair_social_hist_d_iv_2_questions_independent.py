#!/usr/bin/env python3
"""Normalize the Hist D-IV-2 inquiry and exhibition bank."""
import json
from pathlib import Path
ROOT=Path(__file__).resolve().parents[1]; OUT=ROOT/"questions/social"; LESSON="lesson-social-content-hist-d-iv-2"; KG="kg-social-content-hist-d-iv-2"; TARGETS=["A","B","C","D","B","C","D","A","B","C"]
for i,target in enumerate(TARGETS,1):
 path=OUT/f"question-social-content-hist-d-iv-2-{i}.json"; item=json.loads(path.read_text(encoding="utf-8")); assert item["lessonId"]==LESSON and item["knowledgeIds"]==[KG]
 old=item["answer"]["value"]; ci=ord(old)-65; ti=ord(target)-65; correct=item["options"][ci]["text"]; rest=[x["text"] for j,x in enumerate(item["options"]) if j!=ci]; ordered=rest[:ti]+[correct]+rest[ti:]
 item["options"]=[{"id":chr(65+j),"text":x} for j,x in enumerate(ordered)]; item["answer"]["value"]=target; item["updatedAt"]="2026-09-13"; item["reviewStatus"]="draft"
 item["solutionSteps"]=["讀題定位：圈出研究範圍、問題、樣本、戶籍、地圖、族譜、口述、踏查、展演或授權等條件。","設計探究：先界定時間、地點與可回答的問題，再安排不同資料和角色的交叉檢查。",f"核對正解：選項 {target}「{correct}」能把資料、研究設計與展演主張連起來，並保留樣本與尺度限制。","排除誘答：檢查是否範圍過大、只用單一家族或單張照片、圖層未校準，或未取得私人影像與錄音的同意。","成果回查：確認每項展演說法都有來源、定位、樣本與倫理說明，觀眾提出新證據時能追溯並修正。"]
 for ref in item.get("examPatternRefs",[]): ref["reuseDecision"]="pattern-only"; ref["status"]="recorded"
 path.write_text(json.dumps(item,ensure_ascii=False,indent=2)+"\n",encoding="utf-8")
print(f"rewrote {len(TARGETS)} independent questions for {LESSON}")
