import json
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
OUT = ROOT / 'questions/science'
URL = 'https://www.yacjh.kh.edu.tw/upload/221/101_30637/114%E4%B8%8B%E5%AD%B8%E6%9C%9F%E7%AC%AC%E4%B8%80%E6%AC%A1%E6%AE%B5%E8%80%83%E4%B8%89%E5%B9%B4%E7%B4%9A%E8%87%AA%E7%84%B6.pdf'
DATA = [
('距離與位移', '人從家向東走 100 m，再向西走回原點；總路程與位移為？', ['路程 200 m，位移 0 m', '路程 0 m，位移 200 m 向東', '路程 100 m，位移 100 m 向東', '路程 200 m，位移 200 m 向西'], '路程 200 m，位移 0 m', '路程是實際走過的路徑長度；位移只看起點到終點的有向變化，回到原點即為零。'),
('速率速度', '速率與速度的主要差別是？', ['速率只描述快慢，速度還包含方向', '速率一定包含方向而速度不含', '兩者永遠完全相同', '速度只適用於靜止物體'], '速率只描述快慢，速度還包含方向', '速率是距離除以時間的快慢指標；速度以位移與時間描述，具有方向。'),
('平均速率', '小車先以 2 m/s 行駛 10 s，再以 4 m/s 行駛 10 s，平均速率應用哪種方式求？', ['總路程除以總時間', '兩個速度直接相乘', '只取最後速度', '總時間除以總路程'], '總路程除以總時間', '平均速率定義為全程路程除以全程時間，不能在不同時間段任意只取一段或直接套用最後值。'),
('方向描述', '若以東為正方向，物體速度為 -3 m/s 表示？', ['物體以 3 m/s 向西運動', '物體以 3 m/s 向東運動', '物體靜止不動', '物體加速度必為 3 m/s² 向西'], '物體以 3 m/s 向西運動', '負號表示選定正方向的反向；速度單位 m/s，不能與加速度單位混淆。'),
('位置時間圖', '位置—時間圖的斜率在物理上主要代表？', ['速度', '質量', '加速度一定值', '物體體積'], '速度', '位置對時間的變化率是速度；斜率正負可反映選定座標方向。'),
('折返運動', '位置—時間圖先呈正斜率、後呈負斜率，最可能表示？', ['物體先往正方向移動，之後改往反方向移動', '物體一直靜止', '物體質量先增後減', '時間在圖中倒流'], '物體先往正方向移動，之後改往反方向移動', '斜率代表速度方向；斜率變號表示運動方向改變。'),
('單位換算', '將 72 km/h 換算成 m/s，正確結果為？', ['20 m/s', '7.2 m/s', '259.2 m/s', '0.02 m/s'], '20 m/s', '72 km/h × 1000 m/km ÷ 3600 s/h = 20 m/s，換算時要同時處理距離與時間單位。'),
('相對運動', '坐在行駛中的公車內看旁邊乘客，乘客相對於自己通常是？', ['近似靜止；但相對於路旁觀察者可能在運動', '一定以公車速度反向運動', '相對於所有觀察者都靜止', '沒有位置也沒有時間'], '近似靜止；但相對於路旁觀察者可能在運動', '運動描述依參考系而定；同一物體對不同觀察者的速度可能不同。'),
('實驗設計', '要比較兩台小車的平均速率，較公平的做法是？', ['用相同距離與計時方法重複測量，再以總路程除以總時間比較', '一台測距離、一台只估計時間', '只挑最快的一次作結論', '同時改變距離、計時器與起點'], '用相同距離與計時方法重複測量，再以總路程除以總時間比較', '公平比較要固定測量定義與方法，並以重複資料降低偶然誤差。'),
('證據界線', '測得一段路的平均速率為 5 m/s，最嚴謹的解釋是？', ['該段總路程與總時間的比值為 5 m/s，不代表全程每一瞬間都以 5 m/s 運動', '物體每一瞬間速度都一定是 5 m/s', '物體方向一定沒有改變', '可直接知道物體質量'], '該段總路程與總時間的比值為 5 m/s，不代表全程每一瞬間都以 5 m/s 運動', '平均量描述一段區間的整體比值，不能直接取代每一時刻的瞬時速度資料。'),
]

def make(i, row):
    tag, prompt, opts, answer, reason = row
    options = [{'id': chr(65+j), 'text': t} for j, t in enumerate(opts)]
    aid = next(o['id'] for o in options if o['text'] == answer)
    steps = [f'讀題定位：圈出「{tag}」與題目中的起點、終點、路徑、時間或正方向。', f'建立判準：{reason}', f'核對答案：選項 {aid}「{answer}」符合距離、時間與方向的定義。', '排除誘答：分清路程與位移、速率與速度、平均量與瞬時量，並確認單位。', '最後回查：將方向符號、單位換算與測量區間放回題幹，確認沒有過度推論。']
    return {'id': f'question-science-content-eb-iv-8-{i}', 'subject': 'science', 'type': 'single-choice', 'prompt': prompt, 'options': options, 'knowledgeIds': ['kg-science-content-eb-iv-8'], 'difficulty': 'medium', 'answer': {'value': aid, 'explanation': reason}, 'provenance': {'origin': 'original', 'license': 'All rights reserved', 'sourceUrl': URL, 'sourceLocator': '公立國中段考自然科；研究距離、位移、速率、速度、方向與運動圖表的能力方向。', 'authoringNote': '依官方課綱 KG 與公立國中公開試題能力方向獨立改寫，未複製原文、選項、圖表或答案；待第二輪 AI／Terra 內容複核。'}, 'reviewStatus': 'draft', 'updatedAt': '2026-09-08', 'lessonId': 'lesson-science-content-eb-iv-8', 'examPatternRefs': [{'url': URL, 'title': '公立國中段考自然科；僅研究題型與能力方向，未複製原題。', 'year': '114', 'subject': 'science', 'locator': '以距離、時間與方向描述運動', 'observedPattern': '能力方向研究後原創改寫', 'reuseDecision': 'pattern-only', 'status': 'recorded', 'locatorLevel': 'paper'}], 'solutionStrategy': '先確認參考系與方向，再區分路程／位移、速率／速度，最後檢查單位與圖表斜率。', 'solutionSteps': steps}

for i, row in enumerate(DATA, 1):
    (OUT / f'question-science-content-eb-iv-8-{i}.json').write_text(json.dumps(make(i, row), ensure_ascii=False, indent=2) + '\n')
print('rewrote', len(DATA), 'questions')
