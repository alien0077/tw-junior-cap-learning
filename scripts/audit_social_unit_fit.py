#!/usr/bin/env python3
"""Conservative triage for obvious social-studies unit/question conflicts."""
import json
import re
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]

RULES = {
    # These are deliberately broad curriculum-domain tokens. The audit is a
    # conservative lexical triage, not a substitute for expert item review.
    "historical-timeline": (r"史料|年代分別|建立時間線", ("歷", "史", "文明", "戰爭", "殖民", "文化", "臺灣", "帝國", "早期", "當代", "政治", "外交")),
    "civ-budget": (r"預算|居民意見|決策方式", ("公", "民主", "政府", "權利", "公共", "政策", "治理", "社會", "市場", "經濟", "法律", "選擇")),
    "geography-map": (r"地圖|地形|經緯度|人口密度|雨量|氣候", ("地", "區域", "臺灣", "世界", "人口", "氣候", "資源", "產業", "都市", "環境", "生態", "文化保存", "社會正義")),
    "economic-market": (r"價格|供需|市場|成本|利潤", ("經濟", "市場", "產業", "消費", "生產", "資源", "全球", "選擇", "機會")),
}


def main():
    titles = {}
    for p in (ROOT / "lessons" / "social").glob("*.json"):
        try: x=json.loads(p.read_text())
        except: continue
        titles[x.get("id")] = x.get("title", "")
    mismatches=[]; counts={k:0 for k in RULES}
    for p in sorted((ROOT / "questions" / "social").glob("*.json")):
        x=json.loads(p.read_text()); title=titles.get(x.get("lessonId"),""); prompt=x.get("prompt","")
        for kind,(pattern,allowed) in RULES.items():
            if re.search(pattern,prompt):
                counts[kind]+=1
                if not any(a in title for a in allowed):
                    mismatches.append({"path":str(p.relative_to(ROOT)),"lessonId":x.get("lessonId"),"title":title,"archetype":kind,"prompt":prompt})
                break
    out={"status":"pass" if not mismatches else "mismatch-found","questionCount":len(list((ROOT/'questions'/'social').glob('*.json'))),"archetypeCounts":counts,"mismatchCount":len(mismatches),"mismatches":mismatches,"note":"Conservative lexical triage only; no promotion to content-reviewed."}
    (ROOT/'implementation'/'reports'/'social-question-unit-fit.json').write_text(json.dumps(out,ensure_ascii=False,indent=2)+'\n')
    print(json.dumps({k:out[k] for k in ('status','questionCount','archetypeCounts','mismatchCount')},ensure_ascii=False))


if __name__ == '__main__': main()
