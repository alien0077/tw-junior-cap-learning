#!/usr/bin/env python3
"""Normalize the Hist Bb-IV-1 East Asian maritime-world bank."""
import json
from pathlib import Path

ROOT=Path(__file__).resolve().parents[1]; OUT=ROOT/"questions/social"; LESSON="lesson-social-content-hist-bb-iv-1"; KG="kg-social-content-hist-bb-iv-1"
TARGETS=["A","B","C","D","B","C","D","A","B","C"]
for i,target in enumerate(TARGETS,1):
 path=OUT/f"question-social-content-hist-bb-iv-1-{i}.json"; item=json.loads(path.read_text(encoding="utf-8")); assert item["lessonId"]==LESSON and item["knowledgeIds"]==[KG]
 old=item["answer"]["value"]; ci=ord(old)-65; ti=ord(target)-65; correct=item["options"][ci]["text"]; rest=[x["text"] for j,x in enumerate(item["options"]) if j!=ci]; ordered=rest[:ti]+[correct]+rest[ti:]
 item["options"]=[{"id":chr(65+j),"text":x} for j,x in enumerate(ordered)]; item["answer"]["value"]=target; item["updatedAt"]="2026-09-13"; item["reviewStatus"]="draft"
 item["solutionSteps"]=["讀題定位：圈出海域、商人、港口、官方政策、民間交易、航線、貨物或權力關係等線索。","整理網絡：把不同群體與制度放在同一時間、空間與往來網絡中，比較合作、競爭與限制。",f"核對正解：選項 {target}「{correct}」能回應題幹資料，且不把單一港口或歐洲勢力推成整個海域的唯一解釋。","排除誘答：檢查是否把官方規定當成實際全部、把控制港口當成全面支配，或忽略地方商人與多方中介。","結論回查：確認主張的時間、地區、參與者與證據範圍一致；加入新港口或史料時重新比較。"]
 for ref in item.get("examPatternRefs",[]): ref["reuseDecision"]="pattern-only"; ref["status"]="recorded"
 path.write_text(json.dumps(item,ensure_ascii=False,indent=2)+"\n",encoding="utf-8")
print(f"rewrote {len(TARGETS)} independent questions for {LESSON}")
