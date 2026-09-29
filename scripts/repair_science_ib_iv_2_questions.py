import json
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
OUT = ROOT / 'questions/science'
URL = 'https://www.yacjh.kh.edu.tw/upload/221/101_30637/114%E4%B8%8B%E5%AD%B8%E6%9C%9F%E7%AC%AC%E4%B8%80%E6%AC%A1%E6%AE%B5%E8%80%83%E4%B8%89%E5%B9%B4%E7%B4%9A%E8%87%AA%E7%84%B6.pdf'
DATA = [
('風的成因', '地表附近的風通常由哪項差異造成空氣流動？', ['不同位置間的氣壓差', '所有地方溫度完全相同', '月亮顏色改變', '空氣完全沒有質量'], '不同位置間的氣壓差', '空氣會受到氣壓梯度力影響，由高氣壓區朝低氣壓區流動，實際風向還可能受地轉與摩擦影響。'),
('受熱差異', '白天海風通常由海洋吹向陸地，常見原因是？', ['陸地升溫較快，近地面氣壓較低，海上較冷空氣流向陸地', '海洋一定比陸地更熱', '風永遠由低壓吹向高壓', '海水會主動吸走所有空氣'], '陸地升溫較快，近地面氣壓較低，海上較冷空氣流向陸地', '不同地表受熱與散熱速度造成溫度、密度與氣壓差異，形成局部環流。'),
('風向判讀', '若地面 A 點氣壓高、B 點氣壓低，忽略其他因素時近地面空氣較可能？', ['由 A 流向 B', '由 B 流向 A', '垂直向下不移動', '氣壓差越大反而越不會流動'], '由 A 流向 B', '氣壓梯度力促使空氣由高壓往低壓流動；實際風向需標示觀察高度與其他力。'),
('等壓線', '天氣圖上等壓線越密集的區域，通常表示？', ['水平氣壓梯度較大，風速可能較強', '氣壓完全相同且沒有風', '溫度一定最高', '降雨必然為零'], '水平氣壓梯度較大，風速可能較強', '等壓線間距反映氣壓變化快慢；風速還會受摩擦、地形與高度影響。'),
('低壓天氣', '低壓中心附近空氣較容易上升，可能帶來哪種天氣？', ['上升冷卻、凝結後較容易形成雲雨', '下沉增溫且天空必然無雲', '空氣完全停止運動', '只會形成沙塵而不含水氣'], '上升冷卻、凝結後較容易形成雲雨', '低壓系統常有輻合上升，若水氣與穩定條件適合，可能形成雲雨；不是每次都必然降雨。'),
('高壓天氣', '高壓中心附近常見下沉氣流，較可能造成？', ['空氣下沉增溫、雲量較少的穩定天氣', '空氣不斷上升形成必然暴雨', '氣壓差消失且無風', '溫度永遠低於周圍'], '空氣下沉增溫、雲量較少的穩定天氣', '下沉氣流常抑制雲發展，但實際天氣仍受水氣、地形與季節等條件影響。'),
('壓差與風速', '在其他條件相近時，兩地氣壓差增加，風速通常可能？', ['增加，因為驅動空氣流動的壓力梯度較大', '必然減少到零', '與風速一定無關', '只由空氣顏色決定'], '增加，因為驅動空氣流動的壓力梯度較大', '壓力梯度是風的驅動因素之一；地形、摩擦與氣流方向仍需一併考量。'),
('資料判讀', '連續測得某地氣壓下降且風速增加，最合理的初步推論是？', ['可能有氣壓系統移近或壓力梯度改變，但需結合鄰近站資料判斷', '一定代表當地立刻發生颱風', '可證明風完全由溫度造成', '氣壓下降代表空氣停止流動'], '可能有氣壓系統移近或壓力梯度改變，但需結合鄰近站資料判斷', '單站資料提供線索，不足以確定完整天氣系統或唯一成因。'),
('實驗設計', '模擬地表受熱造成風向，較公平的設計是？', ['固定容器、空氣量與觀察位置，只改變一側加熱或冷卻條件並重複觀察', '同時改變容器大小、風扇與加熱強度', '只看紙帶一次偏轉', '先選風向再挑影片片段'], '固定容器、空氣量與觀察位置，只改變一側加熱或冷卻條件並重複觀察', '要研究受熱差異，需控制幾何與觀察方法，以重複的風向或溫度資料支持解釋。'),
('證據界線', '氣象站測得風由北方吹來，最嚴謹的表述是？', ['該時段該站觀測到風向來自北方，不代表整個區域風向都相同', '北方一定存在低氣壓中心', '風向測量可直接知道所有地表溫度', '當天任何高度風向都必定相同'], '該時段該站觀測到風向來自北方，不代表整個區域風向都相同', '風向資料有時間、地點與高度範圍；區域天氣判斷需結合多站與多時段資料。'),
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
    steps = [f'讀題定位：圈出「{tag}」與題目中的氣壓、溫度、等壓線、風向或觀測範圍。', f'建立判準：{reason}', f'核對答案：選項 {aid}「{answer}」符合氣壓差造成風的概念。', '排除誘答：分清高壓與低壓、風向來向與去向、壓差驅動與其他天氣因素，並保留資料界線。', '最後回查：確認時間、地點、觀測高度與控制變因都和題幹一致。']
    return {'id': f'question-science-content-ib-iv-2-{i}', 'subject': 'science', 'type': 'single-choice', 'prompt': prompt, 'options': options, 'knowledgeIds': ['kg-science-content-ib-iv-2'], 'difficulty': 'medium', 'answer': {'value': aid, 'explanation': reason}, 'provenance': {'origin': 'original', 'license': 'All rights reserved', 'sourceUrl': URL, 'sourceLocator': '公立國中段考自然科；研究氣壓差、風向、等壓線、海陸風與資料判讀的能力方向。', 'authoringNote': '依官方課綱 KG 與公立國中公開試題能力方向獨立改寫，未複製原文、選項、圖表或答案；待第二輪 AI／Terra 內容複核。'}, 'reviewStatus': 'draft', 'updatedAt': '2026-09-08', 'lessonId': 'lesson-science-content-ib-iv-2', 'examPatternRefs': [{'url': URL, 'title': '公立國中段考自然科；僅研究題型與能力方向，未複製原題。', 'year': '114', 'subject': 'science', 'locator': '氣壓差造成風', 'observedPattern': '能力方向研究後原創改寫', 'reuseDecision': 'pattern-only', 'status': 'recorded', 'locatorLevel': 'paper'}], 'solutionStrategy': '先判斷高低壓與溫度差，再依氣壓梯度追蹤風向，最後檢查地點、時間與其他天氣因素。', 'solutionSteps': steps}

for i, row in enumerate(DATA, 1):
    (OUT / f'question-science-content-ib-iv-2-{i}.json').write_text(json.dumps(make(i, row), ensure_ascii=False, indent=2) + '\n')
print('rewrote', len(DATA), 'questions')
