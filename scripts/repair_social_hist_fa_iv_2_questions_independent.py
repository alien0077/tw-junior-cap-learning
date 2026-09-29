#!/usr/bin/env python3
"""Normalize the Hist Fa-IV-2 228 Incident and White Terror bank."""
import json
from pathlib import Path
ROOT=Path(__file__).resolve().parents[1]; OUT=ROOT/"questions/social"; LESSON="lesson-social-content-hist-fa-iv-2"; KG="kg-social-content-hist-fa-iv-2"; TARGETS=["A","B","C","D","B","C","D","A","B","C"]
for i,target in enumerate(TARGETS,1):
 path=OUT/f"question-social-content-hist-fa-iv-2-{i}.json"; item=json.loads(path.read_text(encoding="utf-8")); assert item["lessonId"]==LESSON and item["knowledgeIds"]==[KG]
 old=item["answer"]["value"]; ci=ord(old)-65; ti=ord(target)-65; correct=item["options"][ci]["text"]; rest=[x["text"] for j,x in enumerate(item["options"]) if j!=ci]; ordered=rest[:ti]+[correct]+rest[ti:]
 item["options"]=[{"id":chr(65+j),"text":x} for j,x in enumerate(ordered)]; item["answer"]["value"]=target; item["updatedAt"]="2026-09-13"; item["reviewStatus"]="draft"
 item["solutionSteps"]=["讀題定位：圈出接收、物價、衝突、治理、地方差異、軍隊、官方公告、受難者記憶、戒嚴或司法程序等線索。","交叉比對：分開檢查官方文件、地方時間線、個人記憶與制度資料的形成背景及可見範圍。",f"核對正解：選項 {target}「{correct}」能處理事件的多重原因、地方差異與記憶證據，不把單一公告當成全民立場。","排除誘答：檢查是否以官方鎮壓語言否定受難者、把單一縣市推成全臺同時發生，或忽略程序與權力不對等。","結論回查：確認主張、年代、地區、群體與證據界線一致；保留不確定處並在新增史料後重新檢查。"]
 for ref in item.get("examPatternRefs",[]): ref["reuseDecision"]="pattern-only"; ref["status"]="recorded"
 path.write_text(json.dumps(item,ensure_ascii=False,indent=2)+"\n",encoding="utf-8")
print(f"rewrote {len(TARGETS)} independent questions for {LESSON}")
