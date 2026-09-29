import json
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
OUT = ROOT / 'questions/science'
URL = 'https://www.yacjh.kh.edu.tw/upload/221/101_30637/114%E4%B8%8B%E5%AD%B8%E6%9C%9F%E7%AC%AC%E4%B8%80%E6%AC%A1%E6%AE%B5%E8%80%83%E4%B8%89%E5%B9%B4%E7%B4%9A%E8%87%AA%E7%84%B6.pdf'
DATA = [
('音調與頻率', '兩個音源響度相近，但甲的振動頻率高於乙，哪項正確？', ['甲的音調較高，因為音調主要由頻率決定', '甲的音調較低，因為頻率高代表聲音小', '兩者音調一定相同', '只能由音源距離決定'], '甲的音調較高，因為音調主要由頻率決定', '頻率越高通常音調越高；響度相近只表示振幅或聲強條件近似，不能改變頻率與音調的對應。'),
('響度與振幅', '同一音源頻率不變，振幅增加時，通常會如何？', ['響度增加而音調大致不變', '音調一定升高而響度不變', '聲速必定變快', '聲音不需介質即可傳播'], '響度增加而音調大致不變', '振幅與聲音能量、聲強及響度相關；頻率不變時，音調不必隨振幅改變。'),
('音色與波形', '兩種樂器演奏相同音高，仍能辨識音色不同，主要因為？', ['波形與泛音組成不同', '兩者一定在不同介質中傳播', '音色只由音量決定', '相同頻率代表波形必完全相同'], '波形與泛音組成不同', '音色由波形與泛音結構等特徵造成；基頻相同不代表所有諧波比例都相同。'),
('超聲波定義', '人耳通常聽不到頻率高於約 20 kHz 的聲波，這類聲波稱為？', ['超聲波', '次聲波', '可見光', '電磁波'], '超聲波', '超聲波頻率高於人耳一般可聽範圍；次聲波則是頻率低於可聽範圍的聲波。'),
('超聲波應用', '醫療超音波檢查能形成影像，主要利用聲波的哪種現象？', ['遇到不同組織界面產生反射，接收回波判斷位置', '聲波在真空中自行發光', '聲波把所有組織變成相同密度', '只依靠可見光穿透人體'], '遇到不同組織界面產生反射，接收回波判斷位置', '不同組織的聲學性質不同，界面反射回波的時間與強度可提供位置和結構資訊。'),
('回波測距', '聲波在介質中的速率已知，利用回波測量障礙物距離時，為何要把往返時間除以二？', ['測得時間包含去程與回程兩段路徑', '因為聲波頻率要除以二才是距離', '因為障礙物會移動兩倍', '因為分貝值代表兩倍距離'], '測得時間包含去程與回程兩段路徑', '回波計時是聲音從發射端到障礙物再返回的總時間，距離 d=v t/2；需確認介質與速度。'),
('超聲波安全', '使用超聲波清洗或檢查設備時，哪項做法較適當？', ['依設備規範控制強度與時間，避免直接接觸高能量發射區並檢查設備狀態', '把身體直接放在高能量探頭前測試', '為求清楚影像任意提高輸出', '只要人耳聽不到就代表完全無風險'], '依設備規範控制強度與時間，避免直接接觸高能量發射區並檢查設備狀態', '聽不到不等於沒有能量；安全要依設備用途、輸出、時間與操作規範，不能只以人耳感覺判斷。'),
('資料判讀', '比較兩個超聲波探頭的測距結果，哪項設計較公平？', ['使用相同介質、目標距離與溫度，校正探頭後重複測量回波時間', '同時更換介質、目標、距離與探頭', '只看一次最短時間', '不記錄溫度與設備設定'], '使用相同介質、目標距離與溫度，校正探頭後重複測量回波時間', '聲速會受介質與溫度影響，探頭設定也會造成差異；控制條件與重複測量才能比較性能。'),
('可聽範圍', '下列哪項說法最恰當？', ['人耳可聽頻率範圍因人與年齡而異，超聲波不代表沒有物理作用', '所有人都能聽到所有頻率', '聽不到的聲波一定不存在', '頻率越高一定代表響度越大'], '人耳可聽頻率範圍因人與年齡而異，超聲波不代表沒有物理作用', '可聽範圍是感覺與生理界線，超聲波仍能傳遞能量並可用於測距、成像等技術。'),
('證據界線', '研究音調、響度、音色與超聲波時，哪項判讀最完整？', ['分別量測頻率、振幅或聲強、波形與回波資料，並標示儀器限制與介質條件', '只靠主觀覺得大小聲就判定所有物理量', '只記錄頻率即可解釋音色與回波', '只要一次數據符合預期就不必重測'], '分別量測頻率、振幅或聲強、波形與回波資料，並標示儀器限制與介質條件', '不同聲音特徵對應不同物理量，超聲波應用還需考慮介質、速度、回波與儀器限制，不能混用單一證據。'),
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
    steps = [f'讀題定位：圈出「{tag}」以及頻率、振幅、波形、回波、介質或安全條件。', f'建立判準：{reason}', f'核對答案：選項 {aid}「{answer}」符合聲音特性與超聲波應用原理。', '排除誘答：分清音調、響度、音色與聲速，並把超聲波的不可聽範圍與物理作用分開判斷。', '最後回查：確認測量條件、單位、往返路徑與儀器限制都與題幹一致。']
    return {'id': f'question-science-content-ka-iv-5-{i}', 'subject': 'science', 'type': 'single-choice', 'prompt': prompt, 'options': options, 'knowledgeIds': ['kg-science-content-ka-iv-5'], 'difficulty': 'medium', 'answer': {'value': aid, 'explanation': reason}, 'provenance': {'origin': 'original', 'license': 'All rights reserved', 'sourceUrl': URL, 'sourceLocator': '公立國中段考自然科；研究音調、響度、音色、超聲波、回波測距、超音波成像與資料安全的能力方向。', 'authoringNote': '依官方課綱 KG 與公立國中公開試題能力方向獨立改寫，未複製原文、選項、圖表或答案；待第二輪 AI／Terra 內容複核。'}, 'reviewStatus': 'draft', 'updatedAt': '2026-09-08', 'lessonId': 'lesson-science-content-ka-iv-5', 'examPatternRefs': [{'url': URL, 'title': '公立國中段考自然科；僅研究題型與能力方向，未複製原題。', 'year': '114', 'subject': 'science', 'locator': '音調、響度、音色與超聲波', 'observedPattern': '能力方向研究後原創改寫', 'reuseDecision': 'pattern-only', 'status': 'recorded', 'locatorLevel': 'paper'}], 'solutionStrategy': '先把聲音特徵對應到頻率、振幅、波形與回波，再分析超聲波應用的介質與路徑，最後檢查測量與安全限制。', 'solutionSteps': steps}

for i, row in enumerate(DATA, 1):
    (OUT / f'question-science-content-ka-iv-5-{i}.json').write_text(json.dumps(make(i, row), ensure_ascii=False, indent=2) + '\n')
print('rewrote', len(DATA), 'questions')
