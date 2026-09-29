#!/usr/bin/env python3
"""Normalize the Hist Ea-IV-3 colonial frontier-policy bank."""
import json
from pathlib import Path
ROOT=Path(__file__).resolve().parents[1]; OUT=ROOT/"questions/social"; LESSON="lesson-social-content-hist-ea-iv-3"; KG="kg-social-content-hist-ea-iv-3"; TARGETS=["A","B","C","D","B","C","D","A","B","C"]
for i,target in enumerate(TARGETS,1):
 path=OUT/f"question-social-content-hist-ea-iv-3-{i}.json"; item=json.loads(path.read_text(encoding="utf-8")); assert item["lessonId"]==LESSON and item["knowledgeIds"]==[KG]
 old=item["answer"]["value"]; ci=ord(old)-65; ti=ord(target)-65; correct=item["options"][ci]["text"]; rest=[x["text"] for j,x in enumerate(item["options"]) if j!=ci]; ordered=rest[:ti]+[correct]+rest[ti:]
 item["options"]=[{"id":chr(65+j),"text":x} for j,x in enumerate(ordered)]; item["answer"]["value"]=target; item["updatedAt"]="2026-09-13"; item["reviewStatus"]="draft"
 item["solutionSteps"]=["讀題定位：圈出分類詞、隘勇線、駐在所、道路、出入限制、官方報告、部落回應或社會變化等線索。","拆分權力與經驗：先辨認政策的分類、設施與治理目的，再比較官方資料、族人行動、地方空間與不同群體的經驗。",f"核對正解：選項 {target}「{correct}」能說明殖民前線政策的權力效果與資料限制，不把官方分類當成中性事實。","排除誘答：檢查是否直接沿用歧視性分類、只用官員報告推論接受，或把道路與駐在所只看成交通設施而忽略控制功能。","結論回查：確認詞語的歷史語境、政策範圍、族群觀點與證據來源相稱；補入部落資料後重新檢查判斷。"]
 for ref in item.get("examPatternRefs",[]): ref["reuseDecision"]="pattern-only"; ref["status"]="recorded"
 path.write_text(json.dumps(item,ensure_ascii=False,indent=2)+"\n",encoding="utf-8")
print(f"rewrote {len(TARGETS)} independent questions for {LESSON}")
