import json
from pathlib import Path
ROOT=Path(__file__).resolve().parents[1]; OUT=ROOT/'questions/science'
URL='https://www.yacjh.kh.edu.tw/upload/221/101_30637/114%E4%B8%8B%E5%AD%B8%E6%9C%9F%E7%AC%AC%E4%B8%80%E6%AC%A1%E6%AE%B5%E8%80%83%E4%B8%89%E5%B9%B4%E7%B4%9A%E8%87%AA%E7%84%B6.pdf'
DATA=[
('細胞尺度','觀察細胞內的 DNA、蛋白質與脂質，這些物質共同說明什麼？',['細胞由不同分子組成並以微觀結構維持功能','細胞只由水組成','分子比細胞更大','所有分子都具有相同功能'],'細胞由不同分子組成並以微觀結構維持功能','細胞是由水、蛋白質、脂質、核酸等多種分子組成的系統，各分子扮演不同角色。'),
('DNA功能','DNA 在細胞中最主要的功能是什麼？',['儲存與傳遞遺傳資訊','直接提供所有細胞熱量','包覆細胞形成細胞壁','把所有水分排出細胞'],'儲存與傳遞遺傳資訊','DNA 的序列攜帶遺傳資訊，能透過表現與複製參與細胞功能與遺傳。'),
('蛋白質功能','下列哪項最能描述蛋白質在細胞中的作用？',['可作為結構材料、酵素或運輸等多種功能分子','只負責儲存遺傳密碼','一定是細胞膜外的糖','只存在於植物細胞'],'可作為結構材料、酵素或運輸等多種功能分子','蛋白質的形狀與胺基酸排列不同，能執行催化、結構、運輸與訊息等功能。'),
('細胞膜','細胞膜主要由脂質雙層與蛋白質組成，這種結構最重要的意義？',['控制物質進出並維持細胞內外環境差異','讓所有物質自由進出而無選擇','製造染色體','把細胞變成固體金屬'],'控制物質進出並維持細胞內外環境差異','膜的選擇性通透與膜蛋白協助，使細胞能調節物質交換與內部條件。'),
('水分子','細胞含水量高，水在細胞中常見的角色是？',['作為溶劑與反應環境，協助物質運輸','只作為遺傳物質','一定直接變成蛋白質','只存在於細胞核'],'作為溶劑與反應環境，協助物質運輸','水能溶解多種物質並參與細胞內反應與運輸，但不是 DNA 或蛋白質本身。'),
('尺度層級','下列由小到大的排列何者較合理？',['原子→分子→細胞器→細胞','細胞→分子→原子→細胞器','分子→細胞→原子→組織','組織→細胞→原子→分子'],'原子→分子→細胞器→細胞','原子組成分子，分子組成細胞器等結構，細胞器再位於細胞內。'),
('酵素分子','酵素能加快細胞內反應，最合理的微觀解釋？',['酵素提供較適合的反應途徑且本身反應前後大致恢復','酵素把原子變成能量','酵素一定是反應物的主要生成物','酵素會使所有反應同時發生'],'酵素提供較適合的反應途徑且本身反應前後大致恢復','酵素是具有特定形狀的蛋白質催化劑，能降低活化能且具專一性。'),
('顯微證據','用顯微鏡看到細胞內有顆粒，最恰當的做法？',['先描述影像，再用染色、分離或其他證據確認其分子組成','直接斷言每顆都是 DNA','顯微鏡影像能看出所有原子排列','只要顆粒變色就知道功能'],'先描述影像，再用染色、分離或其他證據確認其分子組成','影像提供位置與形態線索，不能單靠外觀確定分子身分與功能。'),
('分子互動','細胞膜的脂質與蛋白質排列會影響物質運輸，這表示？',['微觀結構與分子性質會造成可觀察的細胞功能','細胞功能與分子無關','所有分子排列都完全隨機且沒有影響','只有細胞大小決定運輸'],'微觀結構與分子性質會造成可觀察的細胞功能','結構、分子性質與功能相互關聯；膜的組成和排列會影響通透與運輸。'),
('證據界線','若某細胞缺少一種蛋白質而出現功能異常，最嚴謹的表述？',['結果支持該蛋白質可能參與功能，仍需控制實驗確認因果','可直接證明所有蛋白質都負責同一功能','表示 DNA 一定完全消失','表示細胞不含任何其他分子'],'結果支持該蛋白質可能參與功能，仍需控制實驗確認因果','缺少與功能異常的關聯是線索，需補上對照、恢復或抑制等實驗才能強化因果結論。')]
TARGET_ANSWERS='ABCDBCDACB'
def make(i,row):
 tag,prompt,opts,ans,reason=row; target=TARGET_ANSWERS[i-1]; correct=ans; distractors=[v for v in opts if v != correct]; ordered=distractors[:ord(target)-65]+[correct]+distractors[ord(target)-65:]; opts=ordered; options=[{'id':chr(65+j),'text':v} for j,v in enumerate(opts)]; aid=target
 steps=[f'讀題定位：抓出「{tag}」涉及的細胞結構、分子或尺度證據。',f'建立判準：{reason}',f'核對答案：選項 {aid}「{ans}」符合判準。','排除誘答：分清細胞、細胞器、分子與原子層級，並區分影像線索與功能證據。','最後回查：確認答案同時符合微觀組成、結構功能與實驗證據界線。']
 return {'id':f'question-science-content-fc-iv-2-{i}','subject':'science','type':'single-choice','prompt':prompt,'options':options,'knowledgeIds':['kg-science-content-fc-iv-2'],'difficulty':'medium','answer':{'value':aid,'explanation':reason},'provenance':{'origin':'original','license':'All rights reserved','sourceUrl':URL,'sourceLocator':'公立國中段考自然科；研究細胞分子組成、微觀尺度與結構功能的能力方向。','authoringNote':'依官方課綱 KG 與公立國中公開試題能力方向獨立改寫，未複製原文、選項、圖表或答案；待第二輪 AI／Terra 內容複核。'},'reviewStatus':'draft','updatedAt':'2026-09-08','lessonId':'lesson-science-content-fc-iv-2','examPatternRefs':[{'url':URL,'title':'公立國中段考自然科；僅研究題型與能力方向，未複製原題。','year':'114','subject':'science','locator':'細胞分子組成、微觀尺度與結構功能','observedPattern':'能力方向研究後原創改寫','reuseDecision':'pattern-only','status':'recorded','locatorLevel':'paper'}],'solutionStrategy':'先定位細胞內的分子與結構層級，再以結構功能關係和證據限制判斷。','solutionSteps':steps}
for i,row in enumerate(DATA,1): (OUT/f'question-science-content-fc-iv-2-{i}.json').write_text(json.dumps(make(i,row),ensure_ascii=False,indent=2)+'\n')
print('rewrote',len(DATA),'questions')
