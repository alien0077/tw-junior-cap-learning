#!/usr/bin/env python3
"""Normalize the Hist Fb-IV-1 economic-development bank."""
import json
from pathlib import Path
ROOT=Path(__file__).resolve().parents[1]; OUT=ROOT/"questions/social"; LESSON="lesson-social-content-hist-fb-iv-1"; KG="kg-social-content-hist-fb-iv-1"; TARGETS=["A","B","C","D","B","C","D","A","B","C"]
for i,target in enumerate(TARGETS,1):
 path=OUT/f"question-social-content-hist-fb-iv-1-{i}.json"; item=json.loads(path.read_text(encoding="utf-8")); assert item["lessonId"]==LESSON and item["knowledgeIds"]==[KG]
 old=item["answer"]["value"]; ci=ord(old)-65; ti=ord(target)-65; correct=item["options"][ci]["text"]; rest=[x["text"] for j,x in enumerate(item["options"]) if j!=ci]; ordered=rest[:ti]+[correct]+rest[ti:]
 item["options"]=[{"id":chr(65+j),"text":x} for j,x in enumerate(ordered)]; item["answer"]["value"]=target; item["updatedAt"]="2026-09-13"; item["reviewStatus"]="draft"
 item["solutionSteps"]=["讀題定位：圈出土地制度、小農、農村階層、GDP、出口、工業產值、房價、工時、所得差距、製造業或人口移動等線索。","拆分發展指標：分開檢查總量成長、分配效果、勞動條件、區域差距與城鄉移動，再比較不同資料。",f"核對正解：選項 {target}「{correct}」能同時評估經濟成長與社會轉型的收益、成本及群體差異。","排除誘答：檢查是否只看 GDP 或出口、把工廠增加等同全民改善，或忽略房價、工時、所得與農村人口的變化。","結論回查：確認指標、時期、地區與群體相稱；補入分配與生活資料後重新檢查經濟奇蹟或改革的結論。"]
 for ref in item.get("examPatternRefs",[]): ref["reuseDecision"]="pattern-only"; ref["status"]="recorded"
 path.write_text(json.dumps(item,ensure_ascii=False,indent=2)+"\n",encoding="utf-8")
print(f"rewrote {len(TARGETS)} independent questions for {LESSON}")
