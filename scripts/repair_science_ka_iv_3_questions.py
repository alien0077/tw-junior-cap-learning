import json
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
OUT = ROOT / 'questions/science'
URL = 'https://www.yacjh.kh.edu.tw/upload/221/101_30637/114%E4%B8%8B%E5%AD%B8%E6%9C%9F%E7%AC%AC%E4%B8%80%E6%AC%A1%E6%AE%B5%E8%80%83%E4%B8%89%E5%B9%B4%E7%B4%9A%E8%87%AA%E7%84%B6.pdf'
DATA = [
('介質比較', '在常溫附近，聲音在空氣、水與鋼鐵中的傳播速率通常如何比較？', ['鋼鐵通常最快，水次之，空氣較慢', '空氣最快，鋼鐵最慢', '三者速率完全相同', '聲音只在空氣中能傳播'], '鋼鐵通常最快，水次之，空氣較慢', '聲速受介質彈性與密度等性質影響，常見材料中固體鋼鐵較快、液體水次之、氣體空氣較慢；實際值也受溫度與材料狀態影響。'),
('機械波', '聲音不能在真空中傳播，主要原因是？', ['聲音需要介質粒子振動並傳遞能量', '真空會把聲音頻率變成零', '聲音只能靠光線傳播', '真空中的聲音一定太大'], '聲音需要介質粒子振動並傳遞能量', '聲音是機械波，需要介質粒子間的作用傳遞擾動；真空沒有足夠粒子，因此不能傳聲。'),
('溫度效應', '在空氣中，溫度升高時聲速通常如何變化？', ['聲速通常增加，但仍需確認濕度與測量條件', '聲速必定降低到零', '聲速與溫度完全無關', '空氣會變成固體'], '聲速通常增加，但仍需確認濕度與測量條件', '氣體分子熱運動與介質狀態會影響聲速；在一般空氣條件下溫度升高通常使聲速增加，但實驗要記錄其他條件。'),
('公式應用', '聲波在某介質中以 340 m/s 傳播，經過 2 秒走過的距離約為多少？', ['680 m', '170 m', '342 m', '0.0059 m'], '680 m', '使用距離 d=vt=340×2=680 m；題目沒有回波情況，因此不需再除以二。'),
('頻率與速率', '同一介質中，聲源頻率改變但溫度與介質不變，聲速通常如何？', ['大致不變，但波長會隨頻率改變以維持 v=fλ', '頻率越高聲速必定越快', '頻率改變會使聲音不再需要介質', '頻率與波長都固定不變'], '大致不變，但波長會隨頻率改變以維持 v=fλ', '在同一介質條件下聲速主要由介質決定；頻率改變時，波長會依 v=fλ 調整。'),
('測量設計', '比較聲音在兩種介質中的速率，哪項實驗設計較公平？', ['使用同一頻率與已知距離，固定溫度與幾何位置，測量到達時間並重複試驗', '每種介質使用不同距離與不同頻率', '只憑先聽到的感覺排序', '不記錄介質溫度與距離'], '使用同一頻率與已知距離，固定溫度與幾何位置，測量到達時間並重複試驗', '速率由距離與時間求得，介質與溫度會影響結果；控制變因和重複測量可降低比較偏差。'),
('回聲與距離', '利用聲音回聲測量峭壁距離時，計時得到的是哪段路徑？', ['聲音到峭壁再返回的往返路徑，因此距離要用 vt/2 計算', '只有聲音去程，因此直接用 vt', '聲音只在峭壁內傳播', '時間越長代表聲速越快'], '聲音到峭壁再返回的往返路徑，因此距離要用 vt/2 計算', '回聲計時包含去程與回程，總路徑為 vt；單程距離是總路徑的一半。'),
('介面傳播', '聲音從水中傳入空氣時，部分能量可能反射，主要與什麼有關？', ['兩種介質的聲學性質與阻抗不同，介面不一定完全透射', '聲音遇介面一定全部消失', '只有顏色會決定反射', '聲速相同才能產生所有反射'], '兩種介質的聲學性質與阻抗不同，介面不一定完全透射', '介質的密度與彈性等造成聲學阻抗差異，界面會影響反射與透射比例；能量可分配到不同方向。'),
('圖表判讀', '比較不同溫度下空氣聲速的實驗資料時，哪項圖表做法較適當？', ['以溫度為橫軸、聲速為縱軸，標示重複測量平均與誤差', '只畫最符合預測的一點', '把溫度單位和聲速單位混在同一軸', '不標示資料數量與測量條件'], '以溫度為橫軸、聲速為縱軸，標示重複測量平均與誤差', '圖表要清楚呈現自變因、應變因、單位與變異，才能判斷趨勢與資料可信度。'),
('證據界線', '下列哪項最符合介質與聲速研究的判讀？', ['聲速比較要說明介質、溫度、頻率、距離與儀器條件，不能把一次結果推廣到所有情況', '只要在空氣測一次就能知道所有材料聲速', '固體越重聲速必定越慢', '聲音的音調可以直接取代聲速測量'], '聲速比較要說明介質、溫度、頻率、距離與儀器條件，不能把一次結果推廣到所有情況', '聲速是介質與條件共同決定的物理量，結論需標示測量範圍與誤差，避免過度推論。'),
]

TARGET_ANSWERS = 'ABCDBCDACB'

def make(i, row):
    tag, prompt, opts, answer, reason = row
    target = TARGET_ANSWERS[i - 1]
    correct_index = opts.index(answer)
    distractors = [text for index, text in enumerate(opts) if index != correct_index]
    position = ord(target) - 65
    arranged = distractors[:position] + [answer] + distractors[position:]
    options = [{'id': chr(65+j), 'text': text} for j, text in enumerate(arranged)]
    aid = target
    steps = [f'讀題定位：圈出「{tag}」以及介質、溫度、頻率、距離、時間或回聲條件。', f'建立判準：{reason}', f'核對答案：選項 {aid}「{answer}」符合聲速與介質傳播原理。', '排除誘答：分清聲速與頻率、單程與往返距離、介質性質與主觀聽感，並檢查單位。', '最後回查：確認控制變因、公式使用與結論適用範圍都和題幹一致。']
    return {'id': f'question-science-content-ka-iv-3-{i}', 'subject': 'science', 'type': 'single-choice', 'prompt': prompt, 'options': options, 'knowledgeIds': ['kg-science-content-ka-iv-3'], 'difficulty': 'medium', 'answer': {'value': aid, 'explanation': reason}, 'provenance': {'origin': 'original', 'license': 'All rights reserved', 'sourceUrl': URL, 'sourceLocator': '公立國中段考自然科；研究聲音在固液氣介質中的速率、溫度、頻率、回聲、介面反射與實驗資料的能力方向。', 'authoringNote': '依官方課綱 KG 與公立國中公開試題能力方向獨立改寫，未複製原文、選項、圖表或答案；待第二輪 AI／Terra 內容複核。'}, 'reviewStatus': 'draft', 'updatedAt': '2026-09-08', 'lessonId': 'lesson-science-content-ka-iv-3', 'examPatternRefs': [{'url': URL, 'title': '公立國中段考自然科；僅研究題型與能力方向，未複製原題。', 'year': '114', 'subject': 'science', 'locator': '介質性質與聲音傳播速率', 'observedPattern': '能力方向研究後原創改寫', 'reuseDecision': 'pattern-only', 'status': 'recorded', 'locatorLevel': 'paper'}], 'solutionStrategy': '先確認介質與條件，再用 v=d/t 或 v=fλ 判斷聲速，遇到回聲要辨識往返路徑，最後檢查控制變因與誤差。', 'solutionSteps': steps}

for i, row in enumerate(DATA, 1):
    (OUT / f'question-science-content-ka-iv-3-{i}.json').write_text(json.dumps(make(i, row), ensure_ascii=False, indent=2) + '\n')
print('rewrote', len(DATA), 'questions')
