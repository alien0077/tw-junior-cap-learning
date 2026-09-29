#!/usr/bin/env python3
"""Normalize the Hist Fa-IV-4 cross-strait and international-context bank."""
import json
from pathlib import Path
ROOT=Path(__file__).resolve().parents[1]; OUT=ROOT/"questions/social"; LESSON="lesson-social-content-hist-fa-iv-4"; KG="kg-social-content-hist-fa-iv-4"; TARGETS=["A","B","C","D","B","C","D","A","B","C"]
for i,target in enumerate(TARGETS,1):
 path=OUT/f"question-social-content-hist-fa-iv-4-{i}.json"; item=json.loads(path.read_text(encoding="utf-8")); assert item["lessonId"]==LESSON and item["knowledgeIds"]==[KG]
 old=item["answer"]["value"]; ci=ord(old)-65; ti=ord(target)-65; correct=item["options"][ci]["text"]; rest=[x["text"] for j,x in enumerate(item["options"]) if j!=ci]; ordered=rest[:ti]+[correct]+rest[ti:]
 item["options"]=[{"id":chr(65+j),"text":x} for j,x in enumerate(ordered)]; item["answer"]["value"]=target; item["updatedAt"]="2026-09-13"; item["reviewStatus"]="draft"
 item["solutionSteps"]=["讀題定位：圈出分治、政府制度、軍事控制、國際局勢、家庭分隔、探親、書信、遷移、外交或身分等線索。","分層分析：先區分兩岸制度與軍事條件，再比較國際環境、家庭經驗、地方政策與不同居民的觀點。",f"核對正解：選項 {target}「{correct}」能連結分治背景、國際脈絡與個人生活，不把政府聲明當成所有居民的共同看法。","排除誘答：檢查是否把單一政府立場推成全民意見、把國際承認當成居民生活的唯一因素，或忽略跨境家庭的多樣經驗。","結論回查：確認時間、制度、國際事件、家庭資料與群體範圍相稱；補入多方聲音後重新檢查結論。"]
 for ref in item.get("examPatternRefs",[]): ref["reuseDecision"]="pattern-only"; ref["status"]="recorded"
 path.write_text(json.dumps(item,ensure_ascii=False,indent=2)+"\n",encoding="utf-8")
print(f"rewrote {len(TARGETS)} independent questions for {LESSON}")
