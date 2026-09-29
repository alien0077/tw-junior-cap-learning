import json
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
OUT = ROOT / 'questions/science'
URL = 'https://www.yacjh.kh.edu.tw/upload/221/101_30637/114%E4%B8%8B%E5%AD%B8%E6%9C%9F%E7%AC%AC%E4%B8%80%E6%AC%A1%E6%AE%B5%E8%80%83%E4%B8%89%E5%B9%B4%E7%B4%9A%E8%87%AA%E7%84%B6.pdf'
DATA = [
('氧氣粒子','氧氣分子 O₂ 表示什麼？',['一個氧分子由兩個氧原子組成','一個氧原子含兩個電子層','兩種元素各一個原子','兩個氧分子合成一個氧原子'],'一個氧分子由兩個氧原子組成','O₂ 的下標 2 表示同一分子中有兩個氧原子。'),
('水分子','一個 H₂O 分子共有幾個原子？',['3 個','2 個','1 個','4 個'],'3 個','氫有 2 個，未標下標的氧有 1 個，合計 3 個。'),
('二氧化碳','CO₂ 中碳與氧原子的個數比為何？',['1：2','2：1','1：1','2：2'],'1：2','C 未標下標是 1 個，O 的下標是 2 個。'),
('原子分子','下列哪一項屬於分子而不是單一原子？',['N₂','Ne','Fe','He'],'N₂','N₂ 由兩個氮原子組成一個粒子。'),
('化學式係數','3H₂O 代表共有多少個氫原子？',['6 個','3 個','2 個','9 個'],'6 個','係數 3 乘每個分子的氫原子數 2，得到 6。'),
('擴散模型','氣體擴散後仍可被偵測，哪個粒子推論合理？',['粒子持續運動且粒子間有空隙','粒子完全靜止且沒有空間','粒子因擴散變成另一元素','粒子只能在容器底部排列'],'粒子持續運動且粒子間有空隙','擴散支持粒子運動與粒子間有空隙的模型。'),
('原子守恆','化學反應若只是重新排列原子，哪項保持不變？',['各元素原子的種類與總數','分子的排列方式','物質的顏色','所有物質的狀態'],'各元素原子的種類與總數','反應改變結合方式，但封閉系統中原子不會憑空增減。'),
('混合物','O₂ 與 N₂ 混合時最適合的描述？',['不同種類分子共存，未必形成新分子','氧原子變成氮原子','必定變成 CO₂','每個粒子只剩一個原子'],'不同種類分子共存，未必形成新分子','混合表示多種粒子共存，沒有反應證據不能宣稱產生新物質。'),
('分子數量','哪一項表示兩個二氧化碳分子？',['2CO₂','C₂O','CO₄','2C₂O₂'],'2CO₂','係數 2 表示兩個 CO₂ 分子，下標不能代替分子數。'),
('模型限制','模型球表示物質粒子時，哪個說法恰當？',['表達種類、數量和排列，球色不是真實外觀','球越大原子一定越重','球距離就是真實距離','畫球就能證明化學反應'],'表達種類、數量和排列，球色不是真實外觀','模型是表徵工具，能表達關係但有假設與限制。')]

def make(i, row):
    tag, prompt, opts, ans, reason = row
    options = [{'id': chr(65+j), 'text': v} for j, v in enumerate(opts)]
    aid = next(o['id'] for o in options if o['text'] == ans)
    steps = [f'讀題定位：抓出「{tag}」的化學式、係數、下標或模型證據。', f'建立判準：{reason}', f'核對答案：選項 {aid}「{ans}」符合判準。', '排除誘答：分清原子、分子、係數與下標，不能混用。', '最後回查：答案須能完整解釋題幹，條件改變時重新判讀。']
    return {'id': f'question-science-content-cb-iv-1-{i}', 'subject': 'science', 'type': 'single-choice', 'prompt': prompt, 'options': options, 'knowledgeIds': ['kg-science-content-cb-iv-1'], 'difficulty': 'medium', 'answer': {'value': aid, 'explanation': reason}, 'provenance': {'origin': 'original', 'license': 'All rights reserved', 'sourceUrl': URL, 'sourceLocator': '公立國中段考自然科；研究粒子模型、化學式與證據判讀的能力方向。', 'authoringNote': '依官方課綱 KG 與公立國中公開試題能力方向獨立改寫，未複製原文、選項、圖表或答案；待第二輪 AI／Terra 內容複核。'}, 'reviewStatus': 'draft', 'updatedAt': '2026-09-08', 'lessonId': 'lesson-science-content-cb-iv-1', 'examPatternRefs': [{'url': URL, 'title': '公立國中段考自然科；僅研究題型與能力方向，未複製原題。', 'year': '114', 'subject': 'science', 'locator': '粒子模型、化學式與證據判讀', 'observedPattern': '能力方向研究後原創改寫', 'reuseDecision': 'pattern-only', 'status': 'recorded', 'locatorLevel': 'paper'}], 'solutionStrategy': '先辨識原子、分子、係數、下標與粒子模型層次，再檢查選項。', 'solutionSteps': steps}

for i, row in enumerate(DATA, 1):
    (OUT / f'question-science-content-cb-iv-1-{i}.json').write_text(json.dumps(make(i, row), ensure_ascii=False, indent=2) + '\n')
print('rewrote', len(DATA), 'questions')
