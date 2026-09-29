import json
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
DATA = [
    ("同一公園中，三隻同種麻雀共同生活並在同一季節繁殖，最適合稱為哪個層次？", ["族群", "個體", "群集", "生物圈"], "A", "同一地點、同一物種的個體集合稱為族群；多個不同物種族群共同組成群集。", "先判斷物種數量與空間範圍，再對照個體、族群與群集定義。"),
    ("池塘中的魚、藻類、細菌、陽光、水溫與溶氧共同構成什麼？", ["一個生態系的生物與非生物組成", "只有一個族群", "只是一條食物鏈", "整個生物圈"], "A", "生態系包含生物因子與非生物環境，以及兩者之間的交互作用；池塘是生態系的一個例子。", "把觀察項目分成生物因子與非生物因子，再判斷系統層次。"),
    ("由『水草→蝸牛→魚→水鳥』可直接判斷哪項？", ["箭頭表示能量與食物關係的傳遞方向", "水鳥把能量傳給水草", "蝸牛一定是生產者", "這條鏈包含所有池塘物種"], "A", "食物鏈箭頭通常由被取食者指向取食者，表示能量流動方向；一條食物鏈不等於完整食物網。", "先讀箭頭方向，再區分生產者、消費者與鏈網範圍。"),
    ("在能量塔中，通常哪一層可用能量最多？", ["生產者", "初級消費者", "次級消費者", "頂級消費者"], "A", "能量沿食物鏈傳遞時有部分用於生命活動並散失為熱，通常越接近生產者可用能量越多。", "依能量流動方向排列營養階層，不把個體數量直接當成能量。"),
    ("一個小島上的所有生物族群與陽光、土壤、降雨及溫度共同形成的範圍，最接近哪個概念？", ["島嶼生態系", "單一個體", "單一族群", "只有生物圈"], "A", "特定區域內的生物群集與非生物環境互相作用，構成該區域的生態系。", "確認題目是否同時包含生物與環境，並看空間邊界。"),
    ("分解者在生態系中的主要功能是什麼？", ["分解遺體與排遺，將物質返回環境供其他生物利用", "把所有能量循環回太陽", "只吃活的生產者", "使物質不再進入環境"], "A", "分解者促進有機物分解與元素循環，但能量仍會在代謝過程中以熱散失，不能說能量完全循環。", "把物質循環與能量單向流動分開判斷。"),
    ("若溪流上游砍伐造成遮蔭減少、水溫升高與溶氧下降，魚類數量減少，最完整的解釋是？", ["非生物因子改變影響生物生存，進而改變生態系組成", "魚類一定被其他魚吃掉", "水溫與魚類完全無關", "只要增加魚飼料就能恢復生態系"], "A", "遮蔭、水溫與溶氧是非生物因子，改變後會影響魚類生存並牽動食物網。", "先找環境因子變化，再連結生物分布與交互作用。"),
    ("比較珊瑚礁與沙漠生態系時，哪項做法較合理？", ["比較各自的溫度、水分、光照、主要生物與能量流動，不預設兩者相同", "只比較生物種類總數", "只看地表顏色", "因為都是生態系所以環境條件一定相同"], "A", "不同生態系具有不同非生物條件與生物適應，應以多項資料比較其結構與功能。", "分別建立兩個系統的生物與非生物資料，再比較差異。"),
    ("生物圈與單一生態系的關係，哪項敘述正確？", ["生物圈是地球上所有生態系與生命可存在環境的整體", "生物圈只包含海洋", "生態系一定比個體小", "生物圈只由動物組成"], "A", "生物圈是最大的生命世界尺度，包含地球上各種生態系以及其生命活動範圍。", "按空間尺度由局部生態系推到全球生物圈。"),
    ("要判斷一座校園池塘是否為完整生態系，哪組觀察最有用？", ["記錄生產者、消費者、分解者、水溫、光照、溶氧及彼此作用", "只拍攝最大的魚", "只量池塘面積", "只列出植物名稱而不看環境"], "A", "生態系判斷需涵蓋生物角色、非生物環境與交互作用，不能只靠單一物種或面積。", "按照生物角色、環境條件與交互作用三類整理證據。"),
]

PUBLIC_REFERENCES = [
    {"url": "https://www.kcjh.kh.edu.tw/upload/190/104_34764/1-%E7%94%9F%E7%89%A9_2.pdf", "title": "高雄市立國昌國民中學 113 學年度第二學期第三次段考一年級生物科試題", "year": "113"},
    {"url": "https://www.nhjh.tp.edu.tw/uploads/16907876075520ZxFKMA0.pdf", "title": "臺北市立內湖國中 111 學年度第二學期七年級第三次段考生物科題目卷", "year": "111"},
    {"url": "https://www.jhsh.ntpc.edu.tw/var/file/0/1000/attach/57/pta_15673_6875098_06860.pdf", "title": "新北市立錦和高級中學 112 學年度第一學期國中部八年級自然科補考題庫", "year": "112"},
]
for ref in PUBLIC_REFERENCES:
    ref.update({"subject": "science", "locator": ref["title"], "observedPattern": "僅研究公立學校公開試題的生態系組成、食物鏈、能量塔與生物圈層次判讀能力方向；未複製原題文字、選項、圖表或答案。", "reuseDecision": "pattern-only", "status": "recorded", "locatorLevel": "paper"})

target_answers = "ABCDBCDACB"
for i, (prompt, options, answer, explanation, strategy) in enumerate(DATA, 1):
    target = target_answers[i - 1]
    correct_option = options[0]
    distractors = options[1:]
    options = distractors[:ord(target) - 65] + [correct_option] + distractors[ord(target) - 65:]
    answer = target
    path = ROOT / "questions/science" / f"question-science-content-fc-iv-1-{i}.json"
    item = json.loads(path.read_text())
    correct = options[ord(answer) - 65]
    item.update({
        "prompt": prompt,
        "options": [{"id": chr(65 + j), "text": text} for j, text in enumerate(options)],
        "answer": {"value": answer, "explanation": f"{explanation} 正確答案為選項 {answer}：「{correct}」。"},
        "solutionStrategy": strategy,
        "solutionSteps": [
            "圈出題幹中的個體、族群、群集、生態系、生物圈或食物關係。",
            "先判斷空間尺度與生物／非生物組成，再排列層次。",
            f"套用原理：{explanation}",
            f"排除把能量流動、物質循環與層次定義混淆的選項，答案為「{correct}」。",
            "回查是否把單一食物鏈誤當完整食物網，或把局部系統誇大成生物圈。",
        ],
        "examPatternRefs": PUBLIC_REFERENCES,
        "reviewStatus": "draft",
    })
    path.write_text(json.dumps(item, ensure_ascii=False, indent=2) + "\n")
print(f"rewrote {len(DATA)} questions")
