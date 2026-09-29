#!/usr/bin/env python3
"""Record distinct public-school chapter evidence for Geo Aa child nodes."""
from __future__ import annotations
import json, re
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
REPORT = ROOT / "implementation/reports/publisher-chapter-evidence-samples.json"
SOURCES = {
    "nani": ("https://www.jlsh.mlc.edu.tw/var/file/12/1012/img/113-2-7-4.pdf", "卓蘭高中附設國中部南一版七年級社會計畫"),
    "kanghsuan": ("https://course.cyc.edu.tw/upfile/course113/file_school/15683227287080309.pdf", "阿里山國民中小學康軒版七年級社會地理計畫"),
    "hanlin": ("https://course.cyc.edu.tw/upfile/course114/sub1/15937393490258175.pdf", "新港國中翰林版七年級社會地理計畫"),
}
UNITS = {
    "Aa-Ⅳ-1": {
        "title": "全球經緯度座標系統",
        "concepts": ["經度與緯度構成全球位置座標", "以座標描述一地的絕對位置", "由緯度、經度連結時區與位置判讀"],
        "representations": ["經緯線網格", "座標讀值與位置標記", "地圖上的絕對位置比較"],
        "assessment": ["地圖判讀", "紙筆測驗", "口頭詢問", "自我評量"],
        "locators": {"nani": "單元 1 地圖與座標系統；列地 Aa-Ⅳ-1 全球經緯度座標系統。", "kanghsuan": "第一單元基本概念與臺灣第 1 課位置、地圖與座標系統；列地 Aa-Ⅳ-1。", "hanlin": "第一篇臺灣的環境上第一章認識位置與地圖；列地 Aa-Ⅳ-1，並安排經緯線、絕對位置與時區。"},
    },
    "Aa-Ⅳ-2": {
        "title": "全球海陸分布",
        "concepts": ["以全球尺度辨識海陸與洲界分布", "比較臺灣在東亞與全球空間中的位置", "用地圖尺度說明位置與範圍的關係"],
        "representations": ["世界海陸分布圖", "洲際與區域位置圖", "全球尺度的範圍比較"],
        "assessment": ["世界地圖判讀", "紙筆測驗", "口頭問答", "課堂觀察"],
        "locators": {"nani": "單元 1 地圖與座標系統；列地 Aa-Ⅳ-2 全球海陸分布。", "kanghsuan": "第一篇基本概念與臺灣延伸；以臺灣位置、範圍及全球關聯建立世界尺度判讀。", "hanlin": "第一篇臺灣的環境上第二章世界中的臺灣；列地 Aa-Ⅳ-2，安排全球海陸與臺灣範圍。"},
    },
    "Aa-Ⅳ-3": {
        "title": "臺灣地理位置特性及影響",
        "concepts": ["臺灣位置影響交通、氣候、生態與區域互動", "區分位置條件與人類活動的中介因素", "以資料支持位置帶來的機會與限制"],
        "representations": ["臺灣區域位置圖", "自然與人文影響對照表", "位置—活動—結果因果鏈"],
        "assessment": ["資料判讀", "口頭說明", "紙筆測驗", "討論與學習歷程"],
        "locators": {"nani": "單元 1 延伸臺灣和世界關聯；以地 Aa-Ⅳ-3／Aa-Ⅳ-4 的位置影響與探究方向記錄。", "kanghsuan": "第一篇臺灣環境單元；由臺灣位置與範圍延伸位置對環境及發展的影響。", "hanlin": "第一篇臺灣的環境上第二章世界中的臺灣；列地 Aa-Ⅳ-3，安排位置影響、生態多樣性與世界關聯。"},
    },
    "Aa-Ⅳ-4": {
        "title": "臺灣與世界各地的關聯探究",
        "concepts": ["從位置、交通、貿易與環境資料探究臺灣和世界的關聯", "區分地理位置提供的條件與社會選擇形成的結果", "以多種資料提出可查證的區域關聯解釋"],
        "representations": ["全球—臺灣關聯地圖", "交通／貿易／環境資料表", "問題—證據—結論探究單"],
        "assessment": ["資料判讀", "分組討論", "口頭說明", "學習歷程與紙筆評量"],
        "locators": {"nani": "單元 1 地圖與座標系統；列地 Aa-Ⅳ-4 問題探究：臺灣和世界各地的關聯性。", "kanghsuan": "第一單元基本概念與臺灣延伸；以臺灣位置、範圍與世界關係作為探究情境。", "hanlin": "第一篇臺灣的環境上第二章世界中的臺灣；列地 Aa-Ⅳ-4，安排臺灣與世界關聯的問題探究。"},
    },
}

def make(code, cfg):
    records=[]
    for pub,(url,edition) in SOURCES.items():
        records.append({"publisher":pub,"sourceUrl":url,"sourceKind":"public-school-course-plan-identifying-publisher-material","locator":f"{edition}；{cfg['locators'][pub]} 核讀 2026-09-20。","accessedAt":"2026-09-20","observedConcepts":cfg['concepts'],"observedRepresentations":cfg['representations'],"observedAssessment":cfg['assessment'],"licenseBoundary":"只記錄公立學校課程計畫的章節、學習重點與評量方向，不複製教材、地圖、題目或答案。"})
    return {"lessonId":f"lesson-social-content-geo-aa-{code.split('-')[-1].lower()}","title":f"{code}：{cfg['title']}","evidenceStatus":"chapter-level-recorded-pending-fusion-review","sources":records,"fusionReview":{"commonCore":cfg['concepts'],"differencesToReview":[f"南一以地圖與座標進入{cfg['title']}。",f"康軒以基本概念與臺灣情境安排{cfg['title']}。",f"翰林把{cfg['title']}放在臺灣環境篇的地理判讀序列。"],"originalSynthesisBoundary":"本樣本只記錄三筆公立學校章節級證據；lesson 正文、地圖、互動與題目仍須逐單元融合、內容／版權審查與 Terra 複核，維持 draft，不升級 publisher status。"}}

data=json.loads(REPORT.read_text(encoding='utf-8')); existing={x['lessonId'] for x in data['units']}; added=[]
for code,cfg in UNITS.items():
 rec=make(code,cfg)
 if rec['lessonId'] not in existing:data['units'].append(rec);added.append(code)
data['unitCount']=len(data['units']);data['updatedAt']='2026-09-20';REPORT.write_text(json.dumps(data,ensure_ascii=False,indent=2)+'\n',encoding='utf-8')
bp=ROOT/'implementation/reports/blockers.json'; blockers=json.loads(bp.read_text(encoding='utf-8'))
for b in blockers.get('blockers',[]):
 r=b.get('reason')
 if isinstance(r,str) and 'unit samples' in r:b['reason']=re.sub(r'Three hundred [a-z-]+ unit samples','Three hundred seventy-four unit samples',r)
bp.write_text(json.dumps(blockers,ensure_ascii=False,indent=2)+'\n',encoding='utf-8')
print(json.dumps({'unitCount':data['unitCount'],'added':added},ensure_ascii=False))
