#!/usr/bin/env python3
"""Normalize the Hist Eb-IV-1 modern-education bank."""
import json
from pathlib import Path
ROOT=Path(__file__).resolve().parents[1]; OUT=ROOT/"questions/social"; LESSON="lesson-social-content-hist-eb-iv-1"; KG="kg-social-content-hist-eb-iv-1"; TARGETS=["A","B","C","D","B","C","D","A","B","C"]
for i,target in enumerate(TARGETS,1):
 path=OUT/f"question-social-content-hist-eb-iv-1-{i}.json"; item=json.loads(path.read_text(encoding="utf-8")); assert item["lessonId"]==LESSON and item["knowledgeIds"]==[KG]
 old=item["answer"]["value"]; ci=ord(old)-65; ti=ord(target)-65; correct=item["options"][ci]["text"]; rest=[x["text"] for j,x in enumerate(item["options"]) if j!=ci]; ordered=rest[:ti]+[correct]+rest[ti:]
 item["options"]=[{"id":chr(65+j),"text":x} for j,x in enumerate(ordered)]; item["answer"]["value"]=target; item["updatedAt"]="2026-09-13"; item["reviewStatus"]="draft"
 item["solutionSteps"]=["讀題定位：圈出公學校、入學身分、地區、性別、留學、報紙、公文、帳冊、語言或啟蒙思想等線索。","分辨教育效果：先比較政策設計與實際入學機會，再檢查識字、媒介、職業、性別與階層差異。",f"核對正解：選項 {target}「{correct}」能說明教育與文化變化的可能效果，且不把少數受教育者經驗推成全臺共同經驗。","排除誘答：檢查是否把設立學校等同人人受益、把留學者回憶當全民資料，或忽略課程、語言與殖民權力背景。","結論回查：確認資料的身分、地區、時期與代表性相稱；補入未入學者或地方資料後重新檢查結論。"]
 for ref in item.get("examPatternRefs",[]): ref["reuseDecision"]="pattern-only"; ref["status"]="recorded"
 path.write_text(json.dumps(item,ensure_ascii=False,indent=2)+"\n",encoding="utf-8")
print(f"rewrote {len(TARGETS)} independent questions for {LESSON}")
