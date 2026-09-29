#!/usr/bin/env python3
"""Normalize the Hist Ha-IV-1 early-state and society bank."""
import json
from pathlib import Path
ROOT=Path(__file__).resolve().parents[1]; OUT=ROOT/"questions/social"; LESSON="lesson-social-content-hist-ha-iv-1"; KG="kg-social-content-hist-ha-iv-1"; TARGETS=["A","B","C","D","B","C","D","A","B","C"]
for i,target in enumerate(TARGETS,1):
 path=OUT/f"question-social-content-hist-ha-iv-1-{i}.json"; item=json.loads(path.read_text(encoding="utf-8")); assert item["lessonId"]==LESSON and item["knowledgeIds"]==[KG]
 old=item["answer"]["value"]; ci=ord(old)-65; ti=ord(target)-65; correct=item["options"][ci]["text"]; rest=[x["text"] for j,x in enumerate(item["options"]) if j!=ci]; ordered=rest[:ti]+[correct]+rest[ti:]
 item["options"]=[{"id":chr(65+j),"text":x} for j,x in enumerate(ordered)]; item["answer"]["value"]=target; item["updatedAt"]="2026-09-13"; item["reviewStatus"]="draft"
 item["solutionSteps"]=["讀題定位：圈出青銅器、銘文、祭祀、軍事、王室賞賜、分封、官僚、交通、地方社會、家族或思想制度等線索。","跨時期比較：先分辨商周、秦漢、魏晉南北朝與隋唐的制度變化，再檢查國家組織和地方網絡如何並存。",f"核對正解：選項 {target}「{correct}」能以器物、制度或社會資料支持國家與社會變遷的有界結論。","排除誘答：檢查是否把青銅器直接當成全民生活、把行政集中推成地方網絡消失，或用後世制度倒套早期情境。","結論回查：確認年代、資料類型、制度尺度與地方差異相稱；補入不同群體與地區資料後重新檢查。"]
 for ref in item.get("examPatternRefs",[]): ref["reuseDecision"]="pattern-only"; ref["status"]="recorded"
 path.write_text(json.dumps(item,ensure_ascii=False,indent=2)+"\n",encoding="utf-8")
print(f"rewrote {len(TARGETS)} independent questions for {LESSON}")
