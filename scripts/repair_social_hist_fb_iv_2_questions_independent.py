#!/usr/bin/env python3
"""Normalize the Hist Fb-IV-2 mass-culture bank."""
import json
from pathlib import Path
ROOT=Path(__file__).resolve().parents[1]; OUT=ROOT/"questions/social"; LESSON="lesson-social-content-hist-fb-iv-2"; KG="kg-social-content-hist-fb-iv-2"; TARGETS=["A","B","C","D","B","C","D","A","B","C"]
for i,target in enumerate(TARGETS,1):
 path=OUT/f"question-social-content-hist-fb-iv-2-{i}.json"; item=json.loads(path.read_text(encoding="utf-8")); assert item["lessonId"]==LESSON and item["knowledgeIds"]==[KG]
 old=item["answer"]["value"]; ci=ord(old)-65; ti=ord(target)-65; correct=item["options"][ci]["text"]; rest=[x["text"] for j,x in enumerate(item["options"]) if j!=ci]; ordered=rest[:ti]+[correct]+rest[ti:]
 item["options"]=[{"id":chr(65+j),"text":x} for j,x in enumerate(ordered)]; item["answer"]["value"]=target; item["updatedAt"]="2026-09-13"; item["reviewStatus"]="draft"
 item["solutionSteps"]=["讀題定位：圈出廣播、報紙、電影、電視、新聞、教育、娛樂、頻道、政府規範、家庭、階層或地區等線索。","分層分析媒介：先比較技術普及、內容製作、傳播範圍與接收條件，再檢查誰能觀看、誰被排除以及誰掌握內容。",f"核對正解：選項 {target}「{correct}」能說明大眾文化的媒介效果、制度權力與群體差異。","排除誘答：檢查是否把熱門作品等同全民文化、把媒介普及當成所有人平等接觸，或忽略政府規範與地方接收差異。","結論回查：確認作品、媒介、年代、觀眾與資料樣本相稱；補入收視、發行或不同群體資料後重新檢查。"]
 for ref in item.get("examPatternRefs",[]): ref["reuseDecision"]="pattern-only"; ref["status"]="recorded"
 path.write_text(json.dumps(item,ensure_ascii=False,indent=2)+"\n",encoding="utf-8")
print(f"rewrote {len(TARGETS)} independent questions for {LESSON}")
