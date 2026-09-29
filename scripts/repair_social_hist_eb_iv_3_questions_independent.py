#!/usr/bin/env python3
"""Normalize the Hist Eb-IV-3 cultural adaptation bank."""
import json
from pathlib import Path
ROOT=Path(__file__).resolve().parents[1]; OUT=ROOT/"questions/social"; LESSON="lesson-social-content-hist-eb-iv-3"; KG="kg-social-content-hist-eb-iv-3"; TARGETS=["A","B","C","D","B","C","D","A","B","C"]
for i,target in enumerate(TARGETS,1):
 path=OUT/f"question-social-content-hist-eb-iv-3-{i}.json"; item=json.loads(path.read_text(encoding="utf-8")); assert item["lessonId"]==LESSON and item["knowledgeIds"]==[KG]
 old=item["answer"]["value"]; ci=ord(old)-65; ti=ord(target)-65; correct=item["options"][ci]["text"]; rest=[x["text"] for j,x in enumerate(item["options"]) if j!=ci]; ordered=rest[:ti]+[correct]+rest[ti:]
 item["options"]=[{"id":chr(65+j),"text":x} for j,x in enumerate(ordered)]; item["answer"]["value"]=target; item["updatedAt"]="2026-09-13"; item["reviewStatus"]="draft"
 item["solutionSteps"]=["讀題定位：圈出曆法、鐘表、作息、祭典、農事、制服、服飾、飲食、語言、家庭或官方報刊等線索。","比較調適方式：分開辨認制度要求、日常實踐、家庭選擇與群體差異，避免把文化變化簡化成接受或拒絕。",f"核對正解：選項 {target}「{correct}」能說明新舊文化在不同場域並存、協商或轉化的具體方式。","排除誘答：檢查是否只用官方報刊代表居民、把保留傳統當成完全抗拒，或把新式制度當成所有生活立即改變。","結論回查：確認資料的場域、時間、群體與文化實踐相稱；補入家庭、女性、勞工或地方資料後重新檢查。"]
 for ref in item.get("examPatternRefs",[]): ref["reuseDecision"]="pattern-only"; ref["status"]="recorded"
 path.write_text(json.dumps(item,ensure_ascii=False,indent=2)+"\n",encoding="utf-8")
print(f"rewrote {len(TARGETS)} independent questions for {LESSON}")
