import json
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
OUT = ROOT / 'questions/science'
URL = 'https://www.yacjh.kh.edu.tw/upload/221/101_30637/114%E4%B8%8B%E5%AD%B8%E6%9C%9F%E7%AC%AC%E4%B8%80%E6%AC%A1%E6%AE%B5%E8%80%83%E4%B8%89%E5%B9%B4%E7%B4%9A%E8%87%AA%E7%84%B6.pdf'
DATA = [
('解離概念', '電解質溶於水後的解離，主要表示？', ['原本的電解質粒子形成可在水中移動的離子', '所有粒子都變成電子', '水分子全部消失', '溶質一定沉澱成固體'], '原本的電解質粒子形成可在水中移動的離子', '解離使離子分散在水中並能移動；離子種類與電荷總量仍須符合物質組成與電荷守恆。'),
('氯化鈉', 'NaCl 溶於水可表示為哪項？', ['NaCl → Na⁺ + Cl⁻', 'NaCl → Na²⁺ + Cl²⁻', 'NaCl → N + Cl', 'NaCl → 電子 + 水'], 'NaCl → Na⁺ + Cl⁻', '氯化鈉解離成一個鈉離子與一個氯離子，正負電荷總量相抵。'),
('氯化鈣', 'CaCl₂ 完全解離時，每一個化學式單位產生的離子為？', ['一個 Ca²⁺ 與兩個 Cl⁻', '兩個 Ca⁺ 與一個 Cl²⁻', '一個 Ca⁺ 與一個 Cl⁻', '只有電子'], '一個 Ca²⁺ 與兩個 Cl⁻', '下標 2 表示氯離子數量；一個二價鈣離子與兩個一價氯離子維持電荷守恆。'),
('離子導電', '解離後溶液能導電的直接原因是？', ['正負離子可在電場中向相反方向移動', '離子固定在晶格中不能動', '中性分子必然沿導線流動', '水把質子變成光'], '正負離子可在電場中向相反方向移動', '溶液導電依靠可移動離子；陽離子與陰離子受電場影響向相反電極移動。'),
('解離程度', '強電解質與弱電解質的主要差異較接近？', ['在相同條件下解離程度與溶液中離子比例不同', '強電解質一定濃度較高', '弱電解質完全沒有粒子', '兩者只差在溶液顏色'], '在相同條件下解離程度與溶液中離子比例不同', '強弱描述解離程度，不等同於溶液濃度或顏色；導電度還受濃度與溫度影響。'),
('稀釋判讀', '把同一電解質溶液加水稀釋，單位體積離子濃度通常？', ['降低，導電性通常也會減弱', '增加到無限大', '離子必然全部沉澱', '與體積完全無關'], '降低，導電性通常也會減弱', '稀釋使相同溶質粒子分布在更大體積，單位體積可移動離子通常減少。'),
('酸解離', '酸在水中能導電，是因為酸分子或晶體解離後？', ['產生可移動的氫離子或水合氫離子與陰離子', '只產生中性氧分子', '所有原子核進入電線', '水分子不再存在'], '產生可移動的氫離子或水合氫離子與陰離子', '酸的水溶液含可移動陽離子與陰離子；課堂模型常以氫離子描述酸性來源。'),
('混合溶液', '將兩種可溶電解質溶液混合，判斷導電性時最需要考量？', ['離子種類、濃度、是否產生沉澱或反應，以及測量條件', '只看混合後顏色', '混合後所有離子必然消失', '只看容器大小不看溶液'], '離子種類、濃度、是否產生沉澱或反應，以及測量條件', '混合可能改變離子濃度或使部分離子生成沉澱／弱電解質，不能只靠外觀判斷。'),
('實驗控制', '比較不同電解質的導電性時，哪項條件應固定？', ['溶液體積、濃度、溫度、電極距離與電路電壓等', '每種溶液使用不同電極距離', '只固定溶液顏色', '每次任意更換電池而不記錄'], '溶液體積、濃度、溫度、電極距離與電路電壓等', '導電測量同時受溶液與裝置影響，需控制非研究變因並重複測量。'),
('證據界線', '導電度較高是否必然代表溶液濃度較高？', ['不一定，還需考慮電解質種類、解離程度、溫度與儀器條件', '一定代表濃度最高', '一定代表溶液沒有離子', '導電度與任何條件都無關'], '不一定，還需考慮電解質種類、解離程度、溫度與儀器條件', '導電度是多因素結果，單一比較不能直接把高導電度等同於高濃度。'),
]
TARGET_ANSWERS = "ABCDBCDACB"

def make(i, row):
    tag, prompt, opts, answer, reason = row
    target = TARGET_ANSWERS[i - 1]
    position = ord(target) - 65
    distractors = [t for t in opts if t != answer]
    arranged = distractors[:position] + [answer] + distractors[position:]
    options = [{'id': chr(65+j), 'text': t} for j, t in enumerate(arranged)]
    aid = target
    steps = [f'讀題定位：圈出「{tag}」與題目中的化學式、離子數量、濃度或測量條件。', f'建立判準：{reason}', f'核對答案：選項 {aid}「{answer}」符合解離與導電模型。', '排除誘答：檢查電荷守恆、下標代表的離子數量、解離程度與導電度的多重因素。', '最後回查：確認方程式、單位與實驗控制條件都和題幹一致，沒有把導電度直接當成單一濃度指標。']
    return {'id': f'question-science-content-jb-iv-2-{i}', 'subject': 'science', 'type': 'single-choice', 'prompt': prompt, 'options': options, 'knowledgeIds': ['kg-science-content-jb-iv-2'], 'difficulty': 'medium', 'answer': {'value': aid, 'explanation': reason}, 'provenance': {'origin': 'original', 'license': 'All rights reserved', 'sourceUrl': URL, 'sourceLocator': '公立國中段考自然科；研究電解質解離、離子數量、導電、濃度與實驗判讀的能力方向。', 'authoringNote': '依官方課綱 KG 與公立國中公開試題能力方向獨立改寫，未複製原文、選項、圖表或答案；待第二輪 AI／Terra 內容複核。'}, 'reviewStatus': 'draft', 'updatedAt': '2026-09-08', 'lessonId': 'lesson-science-content-jb-iv-2', 'examPatternRefs': [{'url': URL, 'title': '公立國中段考自然科；僅研究題型與能力方向，未複製原題。', 'year': '114', 'subject': 'science', 'locator': '電解質解離與導電', 'observedPattern': '能力方向研究後原創改寫', 'reuseDecision': 'pattern-only', 'status': 'recorded', 'locatorLevel': 'paper'}], 'solutionStrategy': '先寫出解離後離子並核對電荷守恆，再判斷離子濃度與導電測量條件。', 'solutionSteps': steps}

for i, row in enumerate(DATA, 1):
    (OUT / f'question-science-content-jb-iv-2-{i}.json').write_text(json.dumps(make(i, row), ensure_ascii=False, indent=2) + '\n')
print('rewrote', len(DATA), 'questions')
