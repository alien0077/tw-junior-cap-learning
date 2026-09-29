import json
from pathlib import Path
ROOT = Path(__file__).resolve().parents[1]
OUT = ROOT / 'questions/science'
URL = 'https://www.yacjh.kh.edu.tw/upload/221/101_30637/114%E4%B8%8B%E5%AD%B8%E6%9C%9F%E7%AC%AC%E4%B8%80%E6%AC%A1%E6%AE%B5%E8%80%83%E4%B8%89%E5%B9%B4%E7%B4%9A%E8%87%AA%E7%84%B6.pdf'
DATA = [
('反應物與生成物','木炭在氧氣中燃燒生成二氧化碳，氧氣在此反應中扮演何種角色？',['生成物','催化劑','反應物','溶劑'],'反應物','反應前參與反應的物質是反應物；二氧化碳則是反應後生成物。'),
('原子重新排列','化學反應的核心變化最適合描述為何？',['原子種類憑空增加','原子重新排列形成新的粒子組合','所有原子消失','只有物質顏色改變'],'原子重新排列形成新的粒子組合','化學反應改變原子的結合方式；在適當系統邊界內，各元素原子仍守恆。'),
('密閉質量','密閉容器內恰好反應的甲、乙質量分別為 12 g 和 8 g，生成物總質量為何？',['4 g','8 g','12 g','20 g'],'20 g','密閉系統中反應物原子重新排列，總質量依守恆為 12+8=20 g。'),
('係數平衡','要使 H₂＋O₂→H₂O 的氧原子數相等，最簡整數式是哪一個？',['H₂＋O₂→H₂O','2H₂＋O₂→2H₂O','H₂＋2O₂→H₂O','2H₂＋2O₂→H₂O'],'2H₂＋O₂→2H₂O','左右各有 4 個氫、2 個氧，係數只改變分子數，不改變化學式下標。'),
('元素守恆','反應式 CaCO₃→CaO＋CO₂ 中，反應前後哪項相同？',['鈣、碳、氧各元素原子總數','每種分子的排列方式','物質的狀態一定相同','反應物與生成物名稱相同'],'鈣、碳、氧各元素原子總數','逐元素計算：左側 Ca、C、O 數量與右側合計相同，這是原子守恆。'),
('係數與下標','配平反應式時，為何不可任意更改 H₂O 的下標 2？',['改下標會改變物質本身的組成','下標只代表反應時間','下標會改變容器大小','下標與原子數無關'],'改下標會改變物質本身的組成','下標決定單一分子的原子比例；配平只能在式前加係數。'),
('反應證據','鐵與硫加熱後形成新物質，哪項證據最能支持發生化學反應？',['產物性質與反應前物質不同且有固定組成','樣品被換到另一個杯子','操作時間變長','顏色描述沒有記錄'],'產物性質與反應前物質不同且有固定組成','新物質的性質與組成證據比容器或時間改變更能支持化學反應。'),
('開放系統','開口容器中反應後量到質量變小，哪個解釋最妥當？',['部分氣體生成物逸散，系統外仍可能守恆','原子在反應中消失','質量守恆只適用固體','反應必然沒有發生'],'部分氣體生成物逸散，系統外仍可能守恆','若氣體離開量測邊界，容器內質量可變小，但不能據此否定更大封閉系統的守恆。'),
('圖式判讀','粒子圖中反應前有兩個 AB，反應後有四個 A₂B，這個圖示至少違反哪項？',['B 原子數守恆','粒子可以移動','反應可能產生新物質','圖示可以用不同顏色表示'],'B 原子數守恆','反應前 B 有 2 個，反應後四個 A₂B 含 4 個 B；若無外加物質，圖示不符合原子守恆。'),
('結論界線','配平一個反應式時，最可靠的最後檢查是什麼？',['逐元素比較左右原子數，並約成最簡整數比','只看係數總和是否相等','只看箭頭方向','只確認文字讀起來順口'],'逐元素比較左右原子數，並約成最簡整數比','配平的判準是每種元素左右原子數相等，再將係數化為最簡整數比。')]
TARGET_ANSWERS = 'ABCDBCDACB'

def make(i, row):
    tag, prompt, opts, ans, reason = row
    target = TARGET_ANSWERS[i - 1]
    position = ord(target) - 65
    distractors = [v for v in opts if v != ans]
    arranged = distractors[:position] + [ans] + distractors[position:]
    options = [{'id': chr(65+j), 'text': v} for j, v in enumerate(arranged)]
    aid = target
    steps = [f'讀題定位：抓出「{tag}」中的反應物、生成物、係數或系統邊界。', f'建立判準：{reason}', f'核對答案：選項 {aid}「{ans}」符合判準。', '排除誘答：分清化學式下標與配平係數，並檢查各元素原子數。', '最後回查：把答案放回反應前後比較，確認結論沒有超出題目提供的系統與證據。']
    return {'id': f'question-science-content-ja-iv-2-{i}', 'subject': 'science', 'type': 'single-choice', 'prompt': prompt, 'options': options, 'knowledgeIds': ['kg-science-content-ja-iv-2'], 'difficulty': 'medium', 'answer': {'value': aid, 'explanation': reason}, 'provenance': {'origin': 'original', 'license': 'All rights reserved', 'sourceUrl': URL, 'sourceLocator': '公立國中段考自然科；研究化學反應、原子重新排列與方程式判讀的能力方向。', 'authoringNote': '依官方課綱 KG 與公立國中公開試題能力方向獨立改寫，未複製原文、選項、圖表或答案；待第二輪 AI／Terra 內容複核。'}, 'reviewStatus': 'draft', 'updatedAt': '2026-09-08', 'lessonId': 'lesson-science-content-ja-iv-2', 'examPatternRefs': [{'url': URL, 'title': '公立國中段考自然科；僅研究題型與能力方向，未複製原題。', 'year': '114', 'subject': 'science', 'locator': '化學反應、原子重新排列與方程式判讀', 'observedPattern': '能力方向研究後原創改寫', 'reuseDecision': 'pattern-only', 'status': 'recorded', 'locatorLevel': 'paper'}], 'solutionStrategy': '先辨識反應前後物質與系統邊界，再逐元素核對原子守恆與係數。', 'solutionSteps': steps}

for i, row in enumerate(DATA, 1):
    (OUT / f'question-science-content-ja-iv-2-{i}.json').write_text(json.dumps(make(i, row), ensure_ascii=False, indent=2) + '\n')
print('rewrote', len(DATA), 'questions')
