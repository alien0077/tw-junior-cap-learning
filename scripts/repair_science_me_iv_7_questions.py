import json
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
OUT = ROOT / 'questions/science'
URL = 'https://www.yacjh.kh.edu.tw/upload/221/101_30637/114%E4%B8%8B%E5%AD%B8%E6%9C%9F%E7%AC%AC%E4%B8%80%E6%AC%A1%E6%AE%B5%E8%80%83%E4%B8%89%E5%B9%B4%E7%B4%9A%E8%87%AA%E7%84%B6.pdf'
DATA = [
('音調', '兩個聲音的響度相近，但甲的振動頻率高於乙，哪項比較正確？', ['甲的音調較高，音調主要由頻率決定', '甲的音調較低，因為頻率越高聲音越小', '兩者音調必定相同', '只能由聲音傳播距離決定'], '甲的音調較高，音調主要由頻率決定', '音調與頻率相關；頻率越高通常音調越高，響度則主要與振幅及接收位置的聲強有關。'),
('響度', '在同一測量位置，若音源振幅變大而頻率近似不變，通常會發生什麼？', ['聲音響度變大，音調大致不變', '音調必定變高而響度不變', '聲音速度變成無限大', '聲音不再需要介質'], '聲音響度變大，音調大致不變', '振幅較大代表傳遞的能量與聲強通常較大，聽感較響；頻率未變時音調不必跟著改變。'),
('音色', '同一音高由長笛與小提琴演奏，聽起來不同的主要原因是？', ['波形與泛音組成不同，形成不同音色', '兩者的音速必定不同', '音色只由音量決定', '只要頻率相同，所有樂器聲音必完全相同'], '波形與泛音組成不同，形成不同音色', '基頻可相同但泛音比例與波形不同，耳朵因此辨認不同音色；音調、響度與音色是不同聲音特徵。'),
('分貝判讀', '測得教室噪音由 70 dB 降至 60 dB，最適當的解讀是？', ['分貝數下降表示測量到的聲音強度等級降低，但不能只靠數字判斷所有聽力風險', '聲音能量一定只剩原來一半', '聲音頻率一定降低十倍', '分貝與聲音無關'], '分貝數下降表示測量到的聲音強度等級降低，但不能只靠數字判斷所有聽力風險', '分貝是對數尺度，數值變化不能直接當成線性倍數；風險還和暴露時間、頻率與個體差異有關。'),
('傳播介質', '聲音在真空中不能傳播，最直接的原因是？', ['聲音需要介質粒子振動並傳遞擾動', '真空中的聲音頻率太高', '真空會把所有光吸收', '聲音只在水中能傳播'], '聲音需要介質粒子振動並傳遞擾動', '機械波的聲音必須透過介質粒子間的作用傳遞，真空缺乏粒子，因此沒有聲音傳播的介質。'),
('防音材料', '比較兩種教室隔音設計時，哪項實驗安排較公平？', ['固定音源、距離、測量位置與播放時間，只改變隔音材料並重複量測', '同時更換音源、距離、材料與測量儀器', '只由一位同學主觀判斷大小聲', '先挑選符合預期的數據'], '固定音源、距離、測量位置與播放時間，只改變隔音材料並重複量測', '要比較材料效果，音源、幾何位置、時間與儀器需固定，並以重複測量降低偶然誤差。'),
('噪音防治', '降低校園長時間噪音對聽力的影響，哪項策略較完整？', ['降低聲源、阻隔或吸收傳播、增加距離並縮短暴露時間', '只把耳朵摀住但讓聲源持續增強', '把所有聲音頻率都提高', '只在事後猜測音量而不測量'], '降低聲源、阻隔或吸收傳播、增加距離並縮短暴露時間', '噪音防治可從源頭、路徑與受音者三方面著手，並控制暴露時間；單一措施不一定足夠。'),
('波形資料', '觀察示波器上兩個聲音波形，若週期較短且振幅相近，通常代表？', ['頻率較高、音調較高，而響度可能相近', '頻率較低且響度一定較大', '音速一定較快', '波形週期與音調無關'], '頻率較高、音調較高，而響度可能相近', '週期 T 越短，頻率 f=1/T 越高；振幅相近只能支持響度近似，不代表音速改變。'),
('資料可信度', '測量街道噪音以評估防治成效時，哪組資料最有比較價值？', ['相同時段、位置、儀器與天氣條件下，記錄防治前後多次 dB 值', '防治前在街道測量，防治後在室內測量一次', '只記錄最大值而不記錄時間', '不同儀器的數字直接平均而不校正'], '相同時段、位置、儀器與天氣條件下，記錄防治前後多次 dB 值', '噪音隨時段、位置與環境改變，必須控制量測條件並重複紀錄，才能把差異合理歸因於防治措施。'),
('健康證據', '下列哪項最符合長時間噪音與聽力保護的判讀？', ['風險要同時考量聲音強度、暴露時間與頻率，應依測量結果採取減噪與休息措施', '只要聲音不刺耳就完全沒有風險', '短暫安靜一次即可抵消所有長時間暴露', '只要音調低就不必控制音量'], '風險要同時考量聲音強度、暴露時間與頻率，應依測量結果採取減噪與休息措施', '聽力風險不是只由主觀音調決定，需看強度與暴露時間等條件；防治應建立在量測與安全原則上。'),
]

TARGET_ANSWERS = 'BCADBBCADC'

def make(i, row):
    tag, prompt, opts, answer, reason = row
    correct_index = next(j for j, text in enumerate(opts) if text == answer)
    target = TARGET_ANSWERS[i - 1]
    distractors = [text for j, text in enumerate(opts) if j != correct_index]
    position = ord(target) - 65
    arranged = distractors[:position] + [answer] + distractors[position:]
    options = [{'id': chr(65+j), 'text': t} for j, t in enumerate(arranged)]
    steps = [f'讀題定位：圈出「{tag}」以及頻率、振幅、音色、分貝、介質或暴露時間。', f'建立判準：{reason}', f'核對答案：選項 {target}「{answer}」符合聲音特性或噪音防治原理。', '排除誘答：分清音調、響度、音色、聲速與分貝，不把單一聲音特徵混作另一種物理量。', '最後回查：確認測量位置、控制變因與健康風險的時間尺度都和題幹一致。']
    return {'id': f'question-science-content-me-iv-7-{i}', 'subject': 'science', 'type': 'single-choice', 'prompt': prompt, 'options': options, 'knowledgeIds': ['kg-science-content-me-iv-7'], 'difficulty': 'medium', 'answer': {'value': target, 'explanation': f'{reason} 正確答案為選項 {target}：「{answer}」。'}, 'provenance': {'origin': 'original', 'license': 'All rights reserved', 'sourceUrl': URL, 'sourceLocator': '公立國中段考自然科；研究音調、響度、音色、分貝、波形、噪音防治與聽力保護的能力方向。', 'authoringNote': '依官方課綱 KG 與公立國中公開試題能力方向獨立改寫，未複製原文、選項、圖表或答案；待第二輪 AI／Terra 內容複核。'}, 'reviewStatus': 'draft', 'updatedAt': '2026-09-19', 'lessonId': 'lesson-science-content-me-iv-7', 'examPatternRefs': [{'url': URL, 'title': '公立國中段考自然科；僅研究題型與能力方向，未複製原題。', 'year': '114', 'subject': 'science', 'locator': '聲音特性研究與噪音防治', 'observedPattern': '能力方向研究後原創改寫', 'reuseDecision': 'pattern-only', 'status': 'recorded', 'locatorLevel': 'paper'}], 'solutionStrategy': '先辨識聲音特徵對應的物理量，再控制量測條件比較資料，最後把強度與暴露時間連結到噪音防治。', 'solutionSteps': steps}

for i, row in enumerate(DATA, 1):
    (OUT / f'question-science-content-me-iv-7-{i}.json').write_text(json.dumps(make(i, row), ensure_ascii=False, indent=2) + '\n')
print('rewrote', len(DATA), 'questions')
