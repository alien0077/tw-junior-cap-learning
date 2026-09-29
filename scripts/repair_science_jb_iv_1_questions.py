import json
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
OUT = ROOT / 'questions/science'
URL = 'https://www.yacjh.kh.edu.tw/upload/221/101_30637/114%E4%B8%8B%E5%AD%B8%E6%9C%9F%E7%AC%AC%E4%B8%80%E6%AC%A1%E6%AE%B5%E8%80%83%E4%B8%89%E5%B9%B4%E7%B4%9A%E8%87%AA%E7%84%B6.pdf'
DATA = [
('電解質定義', '水溶液能導電的物質通常具備哪項特徵？', ['溶液中有可自由移動的離子', '溶液中只有不能移動的分子', '溶質一定是金屬固體', '水本身必然含有大量電子流'], '溶液中有可自由移動的離子', '電解質溶於水後產生可移動離子，離子在電場中定向移動形成導電。'),
('食鹽溶液', '固體食鹽不易導電，但食鹽水可以導電，主要原因是？', ['溶於水後形成可移動的鈉離子與氯離子', '水把食鹽變成金屬', '食鹽固體沒有任何電荷', '食鹽水一定產生電子束'], '溶於水後形成可移動的鈉離子與氯離子', '離子晶體固態時離子位置受限，溶於水後離子可移動，因此溶液具有導電性。'),
('非電解質', '糖水通常導電性很弱，較合理的原因是？', ['糖溶於水主要形成中性分子，沒有大量可移動離子', '糖水沒有水分子', '糖會把所有離子固定成金屬', '糖分子一定帶正電'], '糖溶於水主要形成中性分子，沒有大量可移動離子', '是否含可移動離子是水溶液導電的關鍵；中性分子本身不等同於自由離子。'),
('強弱電解質', '在濃度與測量條件相近時，強電解質溶液通常比弱電解質？', ['產生較多離子，導電性較強', '一定完全不導電', '只因顏色較深而導電', '沒有任何溶質粒子'], '產生較多離子，導電性較強', '強弱電解質的差異與解離程度相關；實際導電度也會受濃度、溫度與儀器影響。'),
('熔融狀態', '某離子化合物熔融後可以導電，固態時卻不易導電，原因是？', ['熔融後離子可移動，固態時離子被晶格限制', '熔融後產生了新的質子', '固態物質沒有任何離子', '溫度升高必然產生金屬電子'], '熔融後離子可移動，固態時離子被晶格限制', '離子化合物的導電與離子是否能移動有關，熔融狀態解除晶格固定。'),
('導電裝置', '用燈泡亮度比較不同溶液導電性時，必須控制哪項條件？', ['電極距離、浸入深度、溶液體積與濃度等條件', '只控制溶液顏色', '每次都更換電池而不記錄', '讓每種溶液使用不同電極距離'], '電極距離、浸入深度、溶液體積與濃度等條件', '燈泡亮度不只受溶液影響，也受電路與電極條件影響，必須控制才能比較。'),
('稀釋影響', '同一電解質溶液逐漸稀釋，導電性常見的變化為？', ['單位體積可移動離子減少，導電性通常降低', '一定無限增加', '離子全部變成電子', '導電性與濃度完全無關'], '單位體積可移動離子減少，導電性通常降低', '稀釋會改變離子濃度；實際導電度需搭配離子種類、溫度與儀器條件判讀。'),
('酸鹼離子', '酸或鹼的水溶液能導電，主要是因為？', ['溶液中有可移動的陽離子與陰離子', '酸鹼只靠顏色傳電', '水溶液中沒有任何粒子', '只有氫原子核在金屬線中流動'], '溶液中有可移動的陽離子與陰離子', '酸鹼溶於水可形成離子；正負離子向相反電極移動而傳遞電流。'),
('證據判讀', '導電測試燈泡不亮，最嚴謹的判讀是？', ['在該電路、濃度與儀器靈敏度下未觀察到足以使燈泡發亮的導電效果', '可直接證明溶液完全沒有任何離子', '可證明儀器一定正常', '代表溶液一定是純水'], '在該電路、濃度與儀器靈敏度下未觀察到足以使燈泡發亮的導電效果', '不亮可能代表導電性太弱或儀器限制，不能把單一結果直接等同於完全無離子。'),
('電極安全', '進行水溶液導電實驗時，哪項做法較適當？', ['使用低電壓電源，保持電極條件一致並避免直接接觸溶液', '使用家用高電壓插座提高亮度', '用手同時接觸兩電極', '為了導電更強而任意混合未知溶液'], '使用低電壓電源，保持電極條件一致並避免直接接觸溶液', '導電實驗需兼顧安全與控制變因，低電壓與一致電極條件可降低風險與誤差。'),
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
    steps = [f'讀題定位：圈出「{tag}」與題目中的溶質狀態、離子、濃度或電極條件。', f'建立判準：{reason}', f'核對答案：選項 {aid}「{answer}」符合電解質與導電模型。', '排除誘答：分清離子與中性分子、固態與溶液、導電性與儀器亮度，不把不亮誤判為完全無離子。', '最後回查：確認比較時控制電極、濃度、溫度與電路，並符合安全要求。']
    return {'id': f'question-science-content-jb-iv-1-{i}', 'subject': 'science', 'type': 'single-choice', 'prompt': prompt, 'options': options, 'knowledgeIds': ['kg-science-content-jb-iv-1'], 'difficulty': 'medium', 'answer': {'value': aid, 'explanation': reason}, 'provenance': {'origin': 'original', 'license': 'All rights reserved', 'sourceUrl': URL, 'sourceLocator': '公立國中段考自然科；研究電解質、離子導電、固液狀態、導電實驗與安全的能力方向。', 'authoringNote': '依官方課綱 KG 與公立國中公開試題能力方向獨立改寫，未複製原文、選項、圖表或答案；待第二輪 AI／Terra 內容複核。'}, 'reviewStatus': 'draft', 'updatedAt': '2026-09-08', 'lessonId': 'lesson-science-content-jb-iv-1', 'examPatternRefs': [{'url': URL, 'title': '公立國中段考自然科；僅研究題型與能力方向，未複製原題。', 'year': '114', 'subject': 'science', 'locator': '導電實驗辨識電解質與非電解質', 'observedPattern': '能力方向研究後原創改寫', 'reuseDecision': 'pattern-only', 'status': 'recorded', 'locatorLevel': 'paper'}], 'solutionStrategy': '先判斷溶液中是否有可移動離子，再檢查濃度、電極、儀器與安全條件。', 'solutionSteps': steps}

for i, row in enumerate(DATA, 1):
    (OUT / f'question-science-content-jb-iv-1-{i}.json').write_text(json.dumps(make(i, row), ensure_ascii=False, indent=2) + '\n')
print('rewrote', len(DATA), 'questions')
