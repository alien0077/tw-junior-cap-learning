#!/usr/bin/env python3
"""Normalize the Hist D-IV-1 local-history inquiry bank."""
import json
from pathlib import Path
ROOT=Path(__file__).resolve().parents[1]; OUT=ROOT/"questions/social"; LESSON="lesson-social-content-hist-d-iv-1"; KG="kg-social-content-hist-d-iv-1"; TARGETS=["A","B","C","D","B","C","D","A","B","C"]
for i,target in enumerate(TARGETS,1):
 path=OUT/f"question-social-content-hist-d-iv-1-{i}.json"; item=json.loads(path.read_text(encoding="utf-8")); assert item["lessonId"]==LESSON and item["knowledgeIds"]==[KG]
 old=item["answer"]["value"]; ci=ord(old)-65; ti=ord(target)-65; correct=item["options"][ci]["text"]; rest=[x["text"] for j,x in enumerate(item["options"]) if j!=ci]; ordered=rest[:ti]+[correct]+rest[ti:]
 item["options"]=[{"id":chr(65+j),"text":x} for j,x in enumerate(ordered)]; item["answer"]["value"]=target; item["updatedAt"]="2026-09-13"; item["reviewStatus"]="draft"
 item["solutionSteps"]=["讀題定位：圈出研究問題、地圖、帳冊、報紙、照片、口述、踏查、人口、交通或產業等資料線索。","安排研究流程：先界定時間、地點與研究對象，再分辨資料形成背景、可回答的問題與限制。",f"核對正解：選項 {target}「{correct}」能把地方資料連成可檢驗的主張，並保留因果、記憶與倫理界線。","排除誘答：檢查是否只數一種資料、把單一回憶當普遍事實、把同時發生當因果，或未取得受訪者同意就公開身分。","結論回查：確認每項主張都有相稱證據、不同資料已交叉比較，且成果不超出受訪者與地方資料的授權範圍。"]
 for ref in item.get("examPatternRefs",[]): ref["reuseDecision"]="pattern-only"; ref["status"]="recorded"
 path.write_text(json.dumps(item,ensure_ascii=False,indent=2)+"\n",encoding="utf-8")
print(f"rewrote {len(TARGETS)} independent questions for {LESSON}")
