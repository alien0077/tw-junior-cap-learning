import json
from pathlib import Path

ROOT=Path(__file__).resolve().parents[1]; OUT=ROOT/"questions/chinese"
SOURCES=[
 ("https://www.sdjh.ntpc.edu.tw/var/file/0/1000/attach/16/pta_2229_1166226_19803.pdf","新北市立石碇國中公開國文試題","常用字使用、字音與詞語搭配"),
 ("https://www.yacjh.kh.edu.tw/upload/221/101_30637/114%E4%B8%8B%E5%AD%B8%E6%9C%9F%E7%AC%AC%E4%B8%80%E6%AC%A1%E6%AE%B5%E8%80%83%E4%B8%89%E5%B9%B4%E7%B4%9A%E5%9C%8B%E6%96%87.pdf","高雄市立鹽埕國中公開國文段考","形音義與語詞運用"),
 ("https://www.jlsh.mlc.edu.tw/var/file/12/1012/img/113-2-7-4.pdf","國立卓蘭高中附設國中部公開課程與試題資料","常用字與語境判讀"),
]
DATA=[
 ("詞語用字","下列哪一組詞語的用字都正確？",["即然／即使","即然／既使","既然／即使","既然／既使"],"既然／即使","『既然』表示已知條件，『即使』表示假設讓步；兩者字形與詞義都需依句法確認。"),
 ("音近字","『一場＿＿的演講』若要表達內容深刻、能引發思考，最適合填入？",["精彩","精采","菁彩","精在"],"精彩","『精彩』表示出色、精采，適合修飾演講；音近字不能只憑發音選擇。"),
 ("形近字","下列哪句的括號內字形使用正確？",["請你仔細端詳這幅畫。","請你仔細端祥這幅畫。","請你仔細端詳這幅划。","請你仔細端祥這幅划。"],"請你仔細端詳這幅畫。","『端詳』指仔細觀看，『畫』指圖畫；形近字要配合詞語與對象檢查。"),
 ("詞義搭配","下列哪個詞語最適合填入『研究結果＿＿了原先的假設』？",["推翻","推番","推翻了","推返"],"推翻","『推翻』可表示否定原先主張；詞語搭配要同時注意字形、語義與句法。"),
 ("讀音判斷","下列哪一組詞語中的『著』讀音與意思相同？",["著急／著火","著作／著名","沉著／著急","著手／著作"],"著急／著火","『著急』與『著火』中的『著』均讀ㄓㄠˊ，分別表示心急與接觸燃燒等語境；其餘讀音或詞義不同。"),
 ("字詞辨正","下列哪句最適合使用『辨識』？",["透過指紋辨識確認身分。","透過指紋辯識確認身分。","透過指紋辨析確認身分。","透過指紋辯論確認身分。"],"透過指紋辨識確認身分。","『辨識』是分辨認出，符合透過指紋確認身分的語境；『辯』涉及言語爭論。"),
 ("同音字語境","『他＿＿完成作業，才去休息』適合填入哪個詞？",["終於","忠於","中於","鐘於"],"終於","『終於』表示經過一段過程後達成，與完成作業的時間關係相符；同音或近音字不可混用。"),
 ("詞性與搭配","下列哪個詞語可以自然填入『老師＿＿我們遵守實驗室規則』？",["勸告","勸告著","勸告地","勸告過於"],"勸告","『勸告』可作動詞帶出受勸對象與內容，搭配句意自然；詞性形式也要一併檢查。"),
 ("語境選字","『他在會議中提出＿＿的建議，讓大家容易執行』，最適合的詞語是？",["具體","具體地","俱體","具體於"],"具體","『具體』可形容建議內容清楚可執行；形近字與詞性變化不能只看讀音。"),
 ("資料界線","題目只提供一個同音字，沒有完整詞語或句子。最妥當的判斷是？",["先列出可能字形與詞義，要求補充語境後再選定","直接選最常見字形並宣稱唯一正確","只看偏旁就能確定詞義","同音字可以在任何詞語互換"],"先列出可能字形與詞義，要求補充語境後再選定","同音字選擇依賴詞語搭配與句意，單獨一個音節不足以確定唯一字形。"),
]
def make_question(i,row):
 tag,prompt,options,answer,explanation=row; opts=[{"id":chr(65+j),"text":t} for j,t in enumerate(options)]; aid=next(x["id"] for x in opts if x["text"]==answer)
 refs=[{"url":u,"title":f"{t}；僅研究公開題型與能力方向，未複製原題。","year":"113-114","subject":"chinese","locator":l,"observedPattern":"公立學校國文公開試題以常用字形、字音、詞義、同音形近與詞語搭配考查語文運用；本題重新設計。","reuseDecision":"pattern-only","status":"recorded","locatorLevel":"paper"} for u,t,l in SOURCES]
 steps=[f"讀題定位：圈出「{tag}」與詞語搭配、句法位置、讀音、形近部件及上下文。",f"建立選字表：先辨認詞義與詞性，再查標準字形和讀音，最後放回句子核對；本題核心是「{explanation}」",f"核對正解：選項 {aid}「{answer}」的字形、音義與句意都一致。","排除誘答：檢查是否只憑同音、偏旁或熟悉感選字，忽略詞語固定搭配和句中動作、對象。","結論回查：完整朗讀詞語與句子，確認沒有形音義衝突；語境不足時要求補充資料。"]
 return {"id":f"question-chinese-content-ab-iv-2-{i}","subject":"chinese","type":"single-choice","prompt":prompt,"options":opts,"knowledgeIds":["kg-chinese-content-ab-iv-2"],"difficulty":"medium","answer":{"value":aid,"explanation":explanation},"provenance":{"origin":"original","license":"All rights reserved","sourceUrl":SOURCES[0][0],"sourceLocator":"公立學校公開國文段考與課程資料；本題只研究公開試題與課程評量的能力結構。","authoringNote":"依官方語文領域課綱、單元 KG 與三個公立學校公開來源的題型方向，獨立改寫常用字形、字音、詞義、同音形近與詞語搭配；未複製原文、選項、篇章、圖表或答案；待第二輪 AI／Terra 內容複核。"},"reviewStatus":"draft","updatedAt":"2026-09-09","lessonId":"lesson-chinese-content-ab-iv-2","examPatternRefs":refs,"solutionStrategy":"先辨認詞語在句中的意思與詞性，再核對字形、讀音和固定搭配，最後用完整句意排除形近或同音誘答。","solutionSteps":steps}
for i,row in enumerate(DATA,1):(OUT/f"question-chinese-content-ab-iv-2-{i}.json").write_text(json.dumps(make_question(i,row),ensure_ascii=False,indent=2)+"\n",encoding="utf-8")
print(f"rewrote {len(DATA)} questions")
