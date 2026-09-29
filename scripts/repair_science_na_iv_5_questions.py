import json
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
DATA = [
    ("評估一個社區的廢棄物是否超過環境承載力，最需要比較哪類資料？", ["廢棄物產生量、處理容量、污染負荷與環境恢復速度", "只比較垃圾袋顏色", "只計算社區人口而不看廢棄物", "只看清運車輛外觀"], "A", "承載力與環境能否吸收、分解或處理人類活動負荷有關，需同時看產生量、處理能力與污染恢復。", "先定義承載力，再把負荷、處理能力與恢復時間量化。"),
    ("若學校想減少一次性餐具，哪項屬於最前端的源頭減量？", ["改用可重複餐具並建立清洗、歸還與補充制度", "先購買更大的垃圾桶", "把所有餐具混合焚燒", "只在學期末統計垃圾"], "A", "改變使用制度以減少一次性用品需求，介入廢棄物產生前，效果通常比末端擴充垃圾桶更直接。", "找出措施介入的時間點，優先判斷是否在垃圾產生前減量。"),
    ("掩埋場若防水層破損，最需要監測哪項環境風險？", ["滲出水進入土壤與地下水造成污染", "垃圾會立刻變成氧氣", "所有廢棄物會自動回收", "只會讓天空顏色改變"], "A", "雨水與廢棄物接觸可能形成含污染物的滲出水，若防護失效可能影響土壤與地下水。", "從處理方式找出可能的污染路徑，再配對監測項目。"),
    ("焚化可以減少垃圾體積，但評估是否適合時仍須注意什麼？", ["空氣污染控制、灰渣處理、能源回收與排放監測", "只看垃圾體積變小就代表沒有污染", "焚化後所有物質都消失", "只測焚化爐外觀"], "A", "焚化可減量或回收熱能，但可能產生煙氣與灰渣，需搭配污染防制和後續處理。", "同時檢查減量效益、排放與副產物，不把末端處理視為零風險。"),
    ("回收物中混入油污或不可回收複合材料，最可能造成什麼問題？", ["降低回收物純度並增加分類與處理負荷", "使所有材料自動變成可回收", "提高原料品質而不需處理", "讓垃圾量必然變成零"], "A", "污染或複合材質會降低再生料品質，增加人工與設備處理負擔，甚至使整批材料無法利用。", "先判斷分類純度，再評估回收流程是否能接受該污染。"),
    ("廚餘堆肥計畫若出現臭味與蚊蠅增加，最適當的改善方向是？", ["調整碳氮比、水分、通氣與覆蓋管理，並監測成熟度", "直接把更多未分類垃圾混入", "停止所有紀錄", "只用香水掩蓋氣味"], "A", "堆肥需控制水分、通氣與材料比例，並妥善管理病原、臭味與成熟度，不能只遮蔽氣味。", "把現象對應到微生物分解條件與管理指標。"),
    ("處理廢手機時，哪項做法最能兼顧資源循環與環境安全？", ["交給合格回收管道，分離電池與可回收金屬並妥善處理有害物質", "直接丟入一般垃圾焚化", "拆下電池後任意丟棄", "把手機埋入土中等待分解"], "A", "電子廢棄物含有可回收金屬與可能有害成分，需要合格管道拆解與處理。", "先辨認資源與危害成分，再選擇能封閉污染路徑的處理方式。"),
    ("比較可重複水壺與一次性瓶裝水的環境負荷，哪項分析較完整？", ["納入製造、運輸、清洗用水與能源、使用次數及報廢回收", "只看購買時的重量", "只看產品包裝顏色", "假設可重複產品完全沒有製造負荷"], "A", "可重複產品仍有製造與清洗負荷，需以合理使用次數與完整生命週期比較。", "先設定系統邊界，再逐階段比較資源投入與廢棄物。"),
    ("社區推行垃圾費隨袋徵收後，垃圾量下降但資源回收污染上升，最合理的評估是？", ["減量可能有效，但仍需改善分類教育與回收品質，不能只看垃圾總量", "垃圾量下降就代表所有環境問題解決", "回收污染與政策無關", "應刪除回收資料"], "A", "政策可能改善某項指標卻造成新的管理問題，需同時追蹤垃圾量、回收純度、非法棄置與成本。", "建立多指標評估，分開看成效、外部成本與副作用。"),
    ("要判斷校園廢棄物處理方案是否接近承載力要求，哪組指標最適合長期追蹤？", ["每人廢棄量、分類純度、最終處置量、處理設施容量與污染監測", "只記錄宣導海報張數", "只統計垃圾桶數量", "只訪問一位學生"], "A", "承載力與處理系統需由產生量、分類品質、最終負荷、容量與污染資料共同判斷。", "把來源、分類、處理、最終處置與環境結果串成完整指標鏈。"),
]

PUBLIC_REFERENCES = [
    {"url": "https://www.cp.ptc.edu.tw/storage/134523/134523_114_B-23_7A.pdf?1774770497=", "title": "屏東縣新園國中 114 學年度七年級自然領域教學計畫表", "year": "114"},
    {"url": "https://www.tsjh.ntpc.edu.tw/app/index.php?Action=downloadfile&cg=119&file=WVhSMFlXTm9MelkzTDNCMFlWOHhNamcwTmw4Mk9UazRNell4WHpjNE1qQXhMbkJrWmc9PQ%3D%3D&fname=WSGGRPQK20QO41KKLOLK54TXXSMO25JGKLB0NO24CCA1XW40YSYWEGB40054ROEGDGKKDH00DG04ICHCIGNKTS34OPB035MKQP35NOTSUWZWCDUWFH10YWFCRKPOSSYX24XWJG34XSKOSSICDGB040WSHDNPMLOOPOUSUSKLDGA4A4FCVW0021JH20B0RKZWOO30LKKKQOJCTWICZTA1LKQPSWYWKORK00SSPKROKK04POPO", "title": "新北市立泰山國中 114 學年度第二學期部定課程計畫", "year": "114"},
    {"url": "https://nethd.whjhs.tp.edu.tw/org/edu01/%E8%B3%87%E6%BA%90%E5%9B%9E%E6%94%B6.htm", "title": "臺北市立萬華國中環境教育及防災教育網：資源回收", "year": "公開資料"},
]
for ref in PUBLIC_REFERENCES:
    ref.update({"subject": "science", "locator": ref["title"], "observedPattern": "僅研究公立學校公開課程與環境教育資料的廢棄物減量、承載力、分類回收與處理方法能力方向；未複製教材文字、題目、選項、圖表或答案。", "reuseDecision": "pattern-only", "status": "recorded", "locatorLevel": "paper"})

for i, (prompt, options, answer, explanation, strategy) in enumerate(DATA, 1):
    path = ROOT / "questions/science" / f"question-science-content-na-iv-5-{i}.json"
    item = json.loads(path.read_text())
    correct = options[ord(answer) - 65]
    item.update({
        "prompt": prompt,
        "options": [{"id": chr(65 + j), "text": text} for j, text in enumerate(options)],
        "answer": {"value": answer, "explanation": f"{explanation} 正確答案為選項 {answer}：「{correct}」。"},
        "solutionStrategy": strategy,
        "solutionSteps": [
            "圈出題幹中的廢棄物來源、處理方式、承載力與環境指標。",
            "先建立從源頭、分類、處理到最終環境負荷的流程。",
            f"套用原理：{explanation}",
            f"排除只看垃圾量或單一宣導指標的選項，答案為「{correct}」。",
            "回查是否同時考慮污染路徑、資源循環、副產物與長期容量。",
        ],
        "examPatternRefs": PUBLIC_REFERENCES,
        "reviewStatus": "draft",
    })
    path.write_text(json.dumps(item, ensure_ascii=False, indent=2) + "\n")
print(f"rewrote {len(DATA)} questions")
