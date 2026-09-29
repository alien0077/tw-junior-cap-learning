#!/usr/bin/env python3
"""Normalize the Hist Ea-IV-1 colonial-governance bank."""
import json
from pathlib import Path
ROOT=Path(__file__).resolve().parents[1]; OUT=ROOT/"questions/social"; LESSON="lesson-social-content-hist-ea-iv-1"; KG="kg-social-content-hist-ea-iv-1"; TARGETS=["A","B","C","D","B","C","D","A","B","C"]
for i,target in enumerate(TARGETS,1):
 path=OUT/f"question-social-content-hist-ea-iv-1-{i}.json"; item=json.loads(path.read_text(encoding="utf-8")); assert item["lessonId"]==LESSON and item["knowledgeIds"]==[KG]
 old=item["answer"]["value"]; ci=ord(old)-65; ti=ord(target)-65; correct=item["options"][ci]["text"]; rest=[x["text"] for j,x in enumerate(item["options"]) if j!=ci]; ordered=rest[:ti]+[correct]+rest[ti:]
 item["options"]=[{"id":chr(65+j),"text":x} for j,x in enumerate(ordered)]; item["answer"]["value"]=target; item["updatedAt"]="2026-09-13"; item["reviewStatus"]="draft"
 item["solutionSteps"]=["讀題定位：圈出總督、警察、行政、軍事、戶口、教育、地方參與、年度報告或制度差異等線索。","拆分制度與經驗：先辨認法規與行政機構，再比較執行範圍、居民回應、不同群體經驗與資料來源立場。",f"核對正解：選項 {target}「{correct}」能說明殖民體制的權力配置與資料限制，不把官方報告等同所有居民的意見。","排除誘答：檢查是否把制度設置直接當成完全控制、把單一官方記錄推成普遍支持，或忽略地方與被統治者聲音。","結論回查：確認制度、時間、地區、群體與證據來源相稱；補入民間資料後重新檢查統治效果的推論。"]
 for ref in item.get("examPatternRefs",[]): ref["reuseDecision"]="pattern-only"; ref["status"]="recorded"
 path.write_text(json.dumps(item,ensure_ascii=False,indent=2)+"\n",encoding="utf-8")
print(f"rewrote {len(TARGETS)} independent questions for {LESSON}")
