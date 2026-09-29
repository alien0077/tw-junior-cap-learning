#!/usr/bin/env python3
"""Normalize the Hist Ha-IV-2 ethnicity and cultural-interaction bank."""
import json
from pathlib import Path
ROOT=Path(__file__).resolve().parents[1]; OUT=ROOT/"questions/social"; LESSON="lesson-social-content-hist-ha-iv-2"; KG="kg-social-content-hist-ha-iv-2"; TARGETS=["A","B","C","D","B","C","D","A","B","C"]
for i,target in enumerate(TARGETS,1):
 path=OUT/f"question-social-content-hist-ha-iv-2-{i}.json"; item=json.loads(path.read_text(encoding="utf-8")); assert item["lessonId"]==LESSON and item["knowledgeIds"]==[KG]
 old=item["answer"]["value"]; ci=ord(old)-65; ti=ord(target)-65; correct=item["options"][ci]["text"]; rest=[x["text"] for j,x in enumerate(item["options"]) if j!=ci]; ordered=rest[:ti]+[correct]+rest[ti:]
 item["options"]=[{"id":chr(65+j),"text":x} for j,x in enumerate(ordered)]; item["answer"]["value"]=target; item["updatedAt"]="2026-09-13"; item["reviewStatus"]="draft"
 item["solutionSteps"]=["讀題定位：圈出族名、內外分類、貿易、軍事、邊境、農業、遊牧、土地、安全、婚姻、語言、宗教或文化交流等線索。","多方比較：先分辨政權命名與群體自我認同，再比較交易、衝突、合作與文化流動的具體資料。",f"核對正解：選項 {target}「{correct}」能處理族群互動的多重關係，不把官方族名或單一史書當成固定本質。","排除誘答：檢查是否把周邊群體永遠敵對、把分類詞當自然身分，或只看戰爭而忽略交易、婚姻與文化混合。","結論回查：確認名稱、時期、邊境、資料來源與群體觀點相稱；補入對方史料或物質文化後重新檢查。"]
 for ref in item.get("examPatternRefs",[]): ref["reuseDecision"]="pattern-only"; ref["status"]="recorded"
 path.write_text(json.dumps(item,ensure_ascii=False,indent=2)+"\n",encoding="utf-8")
print(f"rewrote {len(TARGETS)} independent questions for {LESSON}")
