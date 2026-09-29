import json
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
OUT = ROOT / 'questions/science'
URL = 'https://www.yacjh.kh.edu.tw/upload/221/101_30637/114%E4%B8%8B%E5%AD%B8%E6%9C%9F%E7%AC%AC%E4%B8%80%E6%AC%A1%E6%AE%B5%E8%80%83%E4%B8%89%E5%B9%B4%E7%B4%9A%E8%87%AA%E7%84%B6.pdf'
DATA = [
('潮汐定義', '月球引力造成海面週期性升降，這種現象稱為什麼？', ['潮汐', '波浪', '海流', '海嘯'], '潮汐', '潮汐是海面較規律的週期升降，主要受月球引力影響，也會受到太陽與海岸地形等因素調整。'),
('波浪成因', '一般風浪的形成，主要是什麼能量傳給海面？', ['風把能量傳給水面形成擾動', '月球引力單獨使每個水分子向前流走', '海水鹽度直接變成波峰', '潮汐一定會形成所有風浪'], '風把能量傳給水面形成擾動', '風浪主要由風與海面摩擦傳遞能量；水面上下起伏不等於整片海水隨波向前搬運。'),
('海流定義', '海流與波浪相比，較適合描述為什麼？', ['海水大尺度且較持續的定向流動', '海面局部上下起伏的波形', '每天固定兩次的海面升降', '海底岩石的震動'], '海水大尺度且較持續的定向流動', '海流是海水的長距離定向移動，波浪主要傳遞擾動與能量，潮汐則是週期性海面升降。'),
('週期資料', '要研究某港口潮汐週期，哪項資料最適合？', ['連續記錄海面高度與時間，找出高潮、低潮及相鄰峰值間隔', '只觀察一次浪花高度', '只記錄當天風速一個數字', '只看海水顏色'], '連續記錄海面高度與時間，找出高潮、低潮及相鄰峰值間隔', '潮汐是時間序列現象，需要連續水位資料；相鄰高潮或低潮時間差可估計週期。'),
('大潮小潮', '日、地、月接近一直線時，潮差通常較大的現象稱為？', ['大潮', '小潮', '海嘯', '風暴潮'], '大潮', '新月或滿月附近日月引潮力方向較一致，高潮與低潮的水位差通常較大，稱為大潮。'),
('小潮成因', '上弦月或下弦月附近，潮差通常較小的原因是？', ['日月引潮作用方向大致互相牽制', '月球完全沒有引力', '風浪被地球自轉消失', '海流停止所有升降'], '日月引潮作用方向大致互相牽制', '上、下弦月時日月與地球約呈直角，兩者引潮作用部分抵銷，潮差通常較小，稱為小潮。'),
('潮流與潮位', '潮汐與潮流的差別，哪項較正確？', ['潮汐著重海面升降，潮流著重伴隨潮汐的海水水平流動', '兩者都只代表風浪高度', '潮流沒有方向，潮汐一定有固定風向', '潮汐只發生在河流'], '潮汐著重海面升降，潮流著重伴隨潮汐的海水水平流動', '潮汐描述水位週期變化，潮流描述因潮汐產生的海水往復流動；觀測量與方向不同但互相關聯。'),
('海嘯判讀', '海嘯與一般風浪相比，較可能由什麼造成？', ['海底地震、山崩等突然大幅移動海水', '每天固定的月球引力升降', '微風吹過海面', '港口潮差正常變化'], '海底地震、山崩等突然大幅移動海水', '海嘯是大尺度海水被突然位移形成的長波，成因與潮汐或一般風浪不同，沿岸可能因地形而放大。'),
('觀測設計', '比較兩個港口的潮汐資料時，哪項做法較公平？', ['使用同一時間基準連續記錄水位，並考慮港灣形狀、風、氣壓與測站高度', '只比較不同日期的一次最高水位', '忽略測站高度與時間差', '把風浪最高點當成潮位'], '使用同一時間基準連續記錄水位，並考慮港灣形狀、風、氣壓與測站高度', '潮位會受地形、風暴、氣壓與測站基準影響，需統一時間與高度基準，才能比較週期與潮差。'),
('證據界線', '下列哪項最符合波浪、海流與潮汐的科學判讀？', ['先依時間尺度、海水運動方向與成因區分，再用連續水位與流速資料驗證', '只要看到海面起伏就能斷定是潮汐', '潮汐、海流、波浪與海嘯完全是同一現象', '一次海邊觀察即可解釋全年海況'], '先依時間尺度、海水運動方向與成因區分，再用連續水位與流速資料驗證', '三者都涉及海水運動但尺度、方向與能量來源不同，還需把海嘯等突發現象分開，不能只靠一次目測。'),
]
TARGET_ANSWERS = 'ABCDBCDACB'

def make(i, row):
    tag, prompt, opts, answer, reason = row
    target = TARGET_ANSWERS[i - 1]
    position = ord(target) - 65
    distractors = [t for t in opts if t != answer]
    arranged = distractors[:position] + [answer] + distractors[position:]
    options = [{'id': chr(65+j), 'text': t} for j, t in enumerate(arranged)]
    aid = target
    steps = [f'讀題定位：圈出「{tag}」以及月球、風、週期、水位、流速或突發海水位移。', f'建立判準：{reason}', f'核對答案：選項 {aid}「{answer}」符合波浪、海流、潮汐與海嘯的區分。', '排除誘答：分清海面升降、海水定向流動、波形擾動與海底突發事件，不把所有起伏都叫潮汐。', '最後回查：確認時間尺度、觀測基準、成因與資料類型都與題幹一致。']
    return {'id': f'question-science-content-ic-iv-1-{i}', 'subject': 'science', 'type': 'single-choice', 'prompt': prompt, 'options': options, 'knowledgeIds': ['kg-science-content-ic-iv-1'], 'difficulty': 'medium', 'answer': {'value': aid, 'explanation': reason}, 'provenance': {'origin': 'original', 'license': 'All rights reserved', 'sourceUrl': URL, 'sourceLocator': '公立國中段考自然科；研究波浪、海流、潮汐、大小潮、潮流、海嘯與海岸觀測資料的能力方向。', 'authoringNote': '依官方課綱 KG 與公立國中公開試題能力方向獨立改寫，未複製原文、選項、圖表或答案；待第二輪 AI／Terra 內容複核。'}, 'reviewStatus': 'draft', 'updatedAt': '2026-09-08', 'lessonId': 'lesson-science-content-ic-iv-1', 'examPatternRefs': [{'url': URL, 'title': '公立國中段考自然科；僅研究題型與能力方向，未複製原題。', 'year': '114', 'subject': 'science', 'locator': '波浪、海流與潮汐', 'observedPattern': '能力方向研究後原創改寫', 'reuseDecision': 'pattern-only', 'status': 'recorded', 'locatorLevel': 'paper'}], 'solutionStrategy': '先按成因、時間尺度與海水運動方向區分現象，再用水位與流速時間序列判讀週期、潮差與突發事件。', 'solutionSteps': steps}

for i, row in enumerate(DATA, 1):
    (OUT / f'question-science-content-ic-iv-1-{i}.json').write_text(json.dumps(make(i, row), ensure_ascii=False, indent=2) + '\n')
print('rewrote', len(DATA), 'questions')
