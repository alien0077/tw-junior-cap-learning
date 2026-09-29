#!/usr/bin/env python3
"""Normalize the Hist Ca-IV-1 governance-policy bank."""
import json
from pathlib import Path
ROOT=Path(__file__).resolve().parents[1]; OUT=ROOT/"questions/social"; LESSON="lesson-social-content-hist-ca-iv-1"; KG="kg-social-content-hist-ca-iv-1"; TARGETS=["A","B","C","D","B","C","D","A","B","C"]
for i,target in enumerate(TARGETS,1):
 path=OUT/f"question-social-content-hist-ca-iv-1-{i}.json"; item=json.loads(path.read_text(encoding="utf-8")); assert item["lessonId"]==LESSON and item["knowledgeIds"]==[KG]
 old=item["answer"]["value"]; ci=ord(old)-65; ti=ord(target)-65; correct=item["options"][ci]["text"]; rest=[x["text"] for j,x in enumerate(item["options"]) if j!=ci]; ordered=rest[:ti]+[correct]+rest[ti:]
 item["options"]=[{"id":chr(65+j),"text":x} for j,x in enumerate(ordered)]; item["answer"]["value"]=target; item["updatedAt"]="2026-09-13"; item["reviewStatus"]="draft"
 item["solutionSteps"]=["讀題定位：圈出行政區劃、移民限制、官署、地方治理、官方文書、民間行動或統治範圍等線索。","拆分政策與效果：先區分制度設計、執行方式與地方實際反應，再比較不同資料來源。",f"核對正解：選項 {target}「{correct}」能回應統治政策資料，且不把官方意圖直接等同於全島實際控制。","排除誘答：檢查是否只引用單一官府資料、把設置官署當成完全統治，或忽略地方差異與民間協商。","結論回查：確認政策、時間、地區、執行與受影響群體的範圍相符；補充地方資料後重新檢查結論。"]
 for ref in item.get("examPatternRefs",[]): ref["reuseDecision"]="pattern-only"; ref["status"]="recorded"
 path.write_text(json.dumps(item,ensure_ascii=False,indent=2)+"\n",encoding="utf-8")
print(f"rewrote {len(TARGETS)} independent questions for {LESSON}")
