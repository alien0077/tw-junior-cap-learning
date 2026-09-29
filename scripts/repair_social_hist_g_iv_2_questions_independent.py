#!/usr/bin/env python3
"""Normalize the Hist G-IV-2 E/F inquiry and exhibition bank."""
import json
from pathlib import Path
ROOT=Path(__file__).resolve().parents[1]; OUT=ROOT/"questions/social"; LESSON="lesson-social-content-hist-g-iv-2"; KG="kg-social-content-hist-g-iv-2"; TARGETS=["A","B","C","D","B","C","D","A","B","C"]
for i,target in enumerate(TARGETS,1):
 path=OUT/f"question-social-content-hist-g-iv-2-{i}.json"; item=json.loads(path.read_text(encoding="utf-8")); assert item["lessonId"]==LESSON and item["knowledgeIds"]==[KG]
 old=item["answer"]["value"]; ci=ord(old)-65; ti=ord(target)-65; correct=item["options"][ci]["text"]; rest=[x["text"] for j,x in enumerate(item["options"]) if j!=ci]; ordered=rest[:ti]+[correct]+rest[ti:]
 item["options"]=[{"id":chr(65+j),"text":x} for j,x in enumerate(ordered)]; item["answer"]["value"]=target; item["updatedAt"]="2026-09-13"; item["reviewStatus"]="draft"
 item["solutionSteps"]=["讀題定位：圈出殖民、戰後、民主化、全球化、教育、城市、農村、語言、對象、政治目的、展演或全臺主張等線索。","縮小研究範圍：先選定時期、地區、政策或群體，再安排可比較的資料與展演證據。",f"核對正解：選項 {target}「{correct}」能把 E、F 主題轉成有界的探究問題，並保留時期、地區與群體差異。","排除誘答：檢查是否範圍跨越過大、把城市經驗推成全臺、把相同校數當成相同教育目的，或只選符合結論的資料。","成果回查：確認展演每項說法都有時間、地點、資料來源與群體標示；觀眾提出新證據時能修正結論。"]
 for ref in item.get("examPatternRefs",[]): ref["reuseDecision"]="pattern-only"; ref["status"]="recorded"
 path.write_text(json.dumps(item,ensure_ascii=False,indent=2)+"\n",encoding="utf-8")
print(f"rewrote {len(TARGETS)} independent questions for {LESSON}")
