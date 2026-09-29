#!/usr/bin/env python3
"""Normalize the Hist Hb-IV-1 Song-Yuan international-interaction bank."""
import json
from pathlib import Path
ROOT=Path(__file__).resolve().parents[1]; OUT=ROOT/"questions/social"; LESSON="lesson-social-content-hist-hb-iv-1"; KG="kg-social-content-hist-hb-iv-1"; TARGETS=["A","B","C","D","B","C","D","A","B","C"]
for i,target in enumerate(TARGETS,1):
 path=OUT/f"question-social-content-hist-hb-iv-1-{i}.json"; item=json.loads(path.read_text(encoding="utf-8")); assert item["lessonId"]==LESSON and item["knowledgeIds"]==[KG]
 old=item["answer"]["value"]; ci=ord(old)-65; ti=ord(target)-65; correct=item["options"][ci]["text"]; rest=[x["text"] for j,x in enumerate(item["options"]) if j!=ci]; ordered=rest[:ti]+[correct]+rest[ti:]
 item["options"]=[{"id":chr(65+j),"text":x} for j,x in enumerate(ordered)]; item["answer"]["value"]=target; item["updatedAt"]="2026-09-13"; item["reviewStatus"]="draft"
 item["solutionSteps"]=["讀題定位：圈出港口、商人、香料、瓷器、造船、海貿機構、朝貢、邊境、商品交換或旅行者等線索。","分層分析互動：先區分外交禮儀、政府管理與實際交易，再比較港口、邊境、商人與地方中介的作用。",f"核對正解：選項 {target}「{correct}」能說明宋元國際互動的多中心網絡，不把單一旅行記錄或中央制度當成全部互動。","排除誘答：檢查是否把朝貢等同沒有貿易、把政府設機構等同全面控制，或忽略外來商人與地方港口資料。","結論回查：確認時期、港口、邊境、參與者與資料來源相稱；補入商品、考古或對方史料後重新檢查。"]
 for ref in item.get("examPatternRefs",[]): ref["reuseDecision"]="pattern-only"; ref["status"]="recorded"
 path.write_text(json.dumps(item,ensure_ascii=False,indent=2)+"\n",encoding="utf-8")
print(f"rewrote {len(TARGETS)} independent questions for {LESSON}")
