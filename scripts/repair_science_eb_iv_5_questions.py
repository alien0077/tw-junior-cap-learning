import json
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
OUT = ROOT / 'questions/science'
URL = 'https://www.yacjh.kh.edu.tw/upload/221/101_30637/114%E4%B8%8B%E5%AD%B8%E6%9C%9F%E7%AC%AC%E4%B8%80%E6%AC%A1%E6%AE%B5%E8%80%83%E4%B8%89%E5%B9%B4%E7%B4%9A%E8%87%AA%E7%84%B6.pdf'
DATA = [
('壓力定義', '壓力的物理定義為何？', ['單位面積所受的垂直作用力', '物體重量乘以體積', '單位時間通過的距離', '物體質量除以溫度'], '單位面積所受的垂直作用力', '壓力 p=F/A，描述垂直作用力分布在單位面積上的程度。'),
('面積效應', '同樣大小的力作用在兩個面積不同的接觸面上，哪個面積較小時壓力較大？', ['接觸面積較小者', '接觸面積較大者', '兩者壓力必定相同', '壓力只由顏色決定'], '接觸面積較小者', '力固定時，面積越小，單位面積分得的力越大，因此壓力越大。'),
('帕斯卡原理', '密閉液體中某處受到的壓力增加，帕斯卡原理表示？', ['壓力會傳到液體各處，理想情況下可用於傳遞力量', '壓力只停留在施力點', '液體會把壓力轉成質量', '只有氣體能傳遞壓力'], '壓力會傳到液體各處，理想情況下可用於傳遞力量', '帕斯卡原理適用於密閉液體，外加壓力可傳遞到各方向與液體其他位置。'),
('液壓計算', '小活塞面積 2 cm² 受力 20 N，大活塞面積 10 cm²；忽略損耗時大活塞力為？', ['100 N', '4 N', '20 N', '200 N'], '100 N', '壓力相等：20/2=F/10，因此 F=100 N；力放大伴隨大活塞移動距離較短。'),
('液壓方向', '液壓煞車能讓駕駛以較小踏力控制車輪，主要利用？', ['密閉液體傳遞壓力，並由活塞面積配置產生所需力', '液體完全不受壓力', '煞車把質量變成零', '輪胎不需要接觸地面'], '密閉液體傳遞壓力，並由活塞面積配置產生所需力', '液壓系統藉帕斯卡原理傳遞壓力，活塞面積比影響輸出力。'),
('液體深度', '同一液體中，越深處的液體壓力通常越大，主要因為？', ['上方液柱重量造成的壓力增加', '深處液體密度一定變成零', '容器底部沒有重力', '壓力只由液面面積決定'], '上方液柱重量造成的壓力增加', '液體壓力會受液體密度、重力與深度影響；深度增加時上方液柱較高。'),
('大氣壓應用', '吸盤能貼在平滑牆面上，較適當的解釋是？', ['吸盤內外壓力差與接觸密封共同產生作用力', '吸盤會主動產生永久黏著力', '牆面沒有受到任何力', '大氣壓只存在水中'], '吸盤內外壓力差與接觸密封共同產生作用力', '排出部分空氣後，外側大氣壓可透過壓力差把吸盤壓向牆面；密封狀態很重要。'),
('控制變因', '比較不同鞋底在地面造成的壓力，應固定哪項條件以公平比較？', ['作用力大小與測量方法，只改變接觸面積或材料中的一項', '同時改變重量、面積與材料', '只記錄鞋底顏色', '每次使用不同單位且不換算'], '作用力大小與測量方法，只改變接觸面積或材料中的一項', '由 p=F/A 可知，若比較面積效應就要固定力；若比較材料也需固定幾何與測量方法。'),
('證據界線', '液壓裝置實測輸出力小於理想計算值，最合理的判讀是？', ['摩擦、漏液或活塞重量等損耗使效率低於理想模型', '帕斯卡原理在任何液體都不存在', '實測值一定代表計算公式完全錯誤', '輸出力小於理想值表示壓力不能傳遞'], '摩擦、漏液或活塞重量等損耗使效率低於理想模型', '理想模型忽略損耗；實際系統可仍遵守壓力傳遞但輸出功與力受效率影響。'),
('單位判讀', '計算壓力時，若力用 N、面積用 m²，壓力的 SI 單位是？', ['Pa（N/m²）', 'J（N·m）', 'W（J/s）', 'kg/m³'], 'Pa（N/m²）', '壓力單位帕斯卡等於每平方公尺的牛頓，必須先確認面積單位一致。'),
]

def make(i, row):
    tag, prompt, opts, answer, reason = row
    options = [{'id': chr(65+j), 'text': t} for j, t in enumerate(opts)]
    aid = next(o['id'] for o in options if o['text'] == answer)
    steps = [f'讀題定位：圈出「{tag}」與題目中的力、面積、液體、深度或活塞條件。', f'建立判準：{reason}', f'核對答案：選項 {aid}「{answer}」符合壓力與帕斯卡原理。', '排除誘答：分清壓力與力、面積比與單位，並區分理想模型與實際損耗。', '最後回查：確認公式、單位與控制變因都和題幹條件一致，沒有把壓力傳遞誤解成能量無損。']
    return {'id': f'question-science-content-eb-iv-5-{i}', 'subject': 'science', 'type': 'single-choice', 'prompt': prompt, 'options': options, 'knowledgeIds': ['kg-science-content-eb-iv-5'], 'difficulty': 'medium', 'answer': {'value': aid, 'explanation': reason}, 'provenance': {'origin': 'original', 'license': 'All rights reserved', 'sourceUrl': URL, 'sourceLocator': '公立國中段考自然科；研究壓力、帕斯卡原理、液壓、液體深度與單位的能力方向。', 'authoringNote': '依官方課綱 KG 與公立國中公開試題能力方向獨立改寫，未複製原文、選項、圖表或答案；待第二輪 AI／Terra 內容複核。'}, 'reviewStatus': 'draft', 'updatedAt': '2026-09-08', 'lessonId': 'lesson-science-content-eb-iv-5', 'examPatternRefs': [{'url': URL, 'title': '公立國中段考自然科；僅研究題型與能力方向，未複製原題。', 'year': '114', 'subject': 'science', 'locator': '壓力與帕斯卡原理', 'observedPattern': '能力方向研究後原創改寫', 'reuseDecision': 'pattern-only', 'status': 'recorded', 'locatorLevel': 'paper'}], 'solutionStrategy': '先確認壓力 p=F/A，再判斷液體深度、活塞面積比、單位與實際損耗。', 'solutionSteps': steps}

for i, row in enumerate(DATA, 1):
    (OUT / f'question-science-content-eb-iv-5-{i}.json').write_text(json.dumps(make(i, row), ensure_ascii=False, indent=2) + '\n')
print('rewrote', len(DATA), 'questions')
