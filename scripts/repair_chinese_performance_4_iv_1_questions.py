import json
from pathlib import Path
ROOT=Path(__file__).resolve().parents[1]; OUT=ROOT/"questions/chinese"
SOURCES=[
("https://www.sdjh.ntpc.edu.tw/var/file/0/1000/attach/16/pta_2229_1166226_19803.pdf","新北市立石碇國中公開國文試題","字詞語境與閱讀判讀"),
("https://www.yacjh.kh.edu.tw/upload/221/101_30637/114%E4%B8%8B%E5%AD%B8%E6%9C%9F%E7%AC%AC%E4%B8%80%E6%AC%A1%E6%AE%B5%E8%80%83%E4%B8%89%E5%B9%B4%E7%B4%9A%E5%9C%8B%E6%96%87.pdf","高雄市立鹽埕國中公開國文段考","字音字形、詞義與語用"),
("https://www.jlsh.mlc.edu.tw/var/file/12/1012/img/113-2-7-4.pdf","國立卓蘭高中附設國中部公開課程與試題資料","語境推論與字詞辨析")]
DATA=[
("形近字", "下列句子中，哪一個字形最符合語意：『研究團隊持續___集雨量資料』？", ["蒐", "搜", "艘", "嗖"], "蒐", "『蒐集』指廣泛收集資料，需依詞義辨識形近字，不能只看讀音相近。"),
("詞義語境", "『這項措施旨在降低通勤風險』中的『旨在』，意思最接近哪一項？", ["目的在於", "已經造成", "不願意面對", "暫時停止"], "目的在於", "『旨在』用來指出目的，必須把詞義放回句中的政策與結果關係判斷。"),
("搭配限制", "哪個詞語最適合填入『___證據後再提出結論』？", ["檢視", "品嚐", "聆賞", "栽培"], "檢視", "證據需要查閱、檢查與評估，『檢視』的語意搭配最自然。"),
("多義辨析", "『他把事情說得很透』中的『透』，最接近哪個意思？", ["清楚深入", "穿過物體", "液體滲出", "光線明亮"], "清楚深入", "同一字在不同語境有不同義項；『說得很透』指解釋清楚、深入。"),
("語體選擇", "給校方的正式建議書中，哪個詞語最合適？", ["建請研議", "超讚啦", "有點扯", "隨便弄弄"], "建請研議", "正式公文需要穩定、清楚且合乎對象的語體，不能把口語網路語塞入正式文本。"),
("讀音判斷", "下列哪一組詞語的加點字讀音相同？", ["行走／行業", "長短／成長", "和平／唱和", "便宜／方便"], "便宜／方便", "讀音辨識要逐詞放回語境；『便宜』與『方便』的『便』都讀ㄅㄧㄢˋ。"),
("字詞修訂", "句子『他用很精準的眼光觀察問題』若要使詞語更自然，哪項修訂較佳？", ["他用敏銳的眼光觀察問題", "他用甜美的眼光觀察問題", "他用沉重的眼光觀察問題", "他用遙遠的眼光觀察問題"], "他用敏銳的眼光觀察問題", "『敏銳』能修飾觀察力；修訂要同時考慮詞義、搭配與句子語境。"),
("詞語推論", "文章寫『雨勢稍歇，街角又恢復___』，哪個詞最能表現人車活動重新出現？", ["喧闐", "寂寥", "凝滯", "荒蕪"], "喧闐", "『喧闐』描述聲音與人群熱鬧，和雨停後活動恢復的脈絡相合。"),
("查證策略", "遇到不確定的成語用字，哪種查證順序最可靠？", ["先看完整語境，再查權威辭典例句，最後回讀句子確認", "只依手機自動選字，不看句意", "選筆畫最少的字", "問朋友一次就當作確定"], "先看完整語境，再查權威辭典例句，最後回讀句子確認", "字詞判斷要結合語境與可靠工具；查到義項後仍需回到原句驗證搭配。"),
("整合閱讀", "閱讀科普短文時遇到陌生詞，哪套方法最能保留理解又避免誤解？", ["先用上下文推測，再拆解詞素或查辭典，最後以後文證據修正詞義", "看到陌生詞就跳過整段", "只記住最像的同音字", "把詞義固定成第一次猜的意思"], "先用上下文推測，再拆解詞素或查辭典，最後以後文證據修正詞義", "成熟的字詞學習是可修正的推理流程，讓語境、構詞、工具和後文共同驗證。")]
def make(i,row):
 tag,prompt,opts,ans,exp=row; options=[{"id":chr(65+j),"text":t} for j,t in enumerate(opts)]; aid=next(x["id"] for x in options if x["text"]==ans)
 refs=[{"url":u,"title":f"{t}；僅研究公開題型與能力方向，未複製原題。","year":"113-114","subject":"chinese","locator":loc,"observedPattern":"公開國文評量以字音字形、詞義、語境、搭配和閱讀推論檢查字詞運用；本題以新語境獨立改寫。","reuseDecision":"pattern-only","status":"recorded","locatorLevel":"paper"} for u,t,loc in SOURCES]
 steps=[f"讀題定位：圈出「{tag}」，判斷題目考字形、讀音、詞義、搭配、語體或查證方法。",f"回到語境：觀察前後詞、句子目的與語體限制；本題核心是「{exp}」",f"核對正解：選項 {aid}「{ans}」在字形／音義／搭配上與語境一致。","排除誘答：不要只依外形、同音、直覺或自動選字；把每個選項放回完整句子比較。","完成查核：用語境推測→拆詞／查辭典→例句比對→回讀句子，確認選字能支撐原意。"]
 return {"id":f"question-chinese-performance-4-iv-1-{i}","subject":"chinese","type":"single-choice","prompt":prompt,"options":options,"knowledgeIds":["kg-chinese-performance-4-iv-1"],"difficulty":"medium","answer":{"value":aid,"explanation":exp},"provenance":{"origin":"original","license":"All rights reserved","sourceUrl":SOURCES[0][0],"sourceLocator":"公立學校公開國文段考與課程資料；本題只研究公開試題與課程評量的能力結構。","authoringNote":"依官方語文領域課綱、單元 KG 與三個公立學校公開來源的題型方向，獨立改寫形近字、詞義、搭配、多義、語體、讀音、修訂、成語、查證及陌生詞推論；未複製原文、選項、篇章、圖表或答案；待第二輪 AI／Terra 內容複核。"},"reviewStatus":"draft","updatedAt":"2026-09-09","lessonId":"lesson-chinese-performance-4-iv-1","examPatternRefs":refs,"solutionStrategy":"先把字詞放回完整語境，再分辨字形、讀音、義項與搭配；遇到不確定處使用權威辭典與例句查證，最後回讀確認。","solutionSteps":steps}
for i,row in enumerate(DATA,1):(OUT/f"question-chinese-performance-4-iv-1-{i}.json").write_text(json.dumps(make(i,row),ensure_ascii=False,indent=2)+"\n",encoding="utf-8")
print(f"rewrote {len(DATA)} questions")
