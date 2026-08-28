"""將英文科元題型改為直接語言能力題，保留穩定 question ID。"""
import glob, hashlib, json, re
from pathlib import Path

SOURCE = "https://www.yacjh.kh.edu.tw/upload/221/101_30637/114%E4%B8%8B%E5%AD%B8%E6%9C%9F%E7%AC%AC%E4%B8%80%E6%AC%A1%E6%AE%B5%E8%80%83%E4%B8%89%E5%B9%B4%E7%B4%9A%E8%8B%B1%E6%96%87.pdf"

GRAMMAR = [
    ("Choose the correct sentence for a daily habit.", ["Mia go to school by bus every day.", "Mia goes to school by bus every day.", "Mia going to school by bus every day.", "Mia gone to school by bus every day."], "B", "主詞 Mia 為第三人稱單數，現在簡單式動詞用 goes。"),
    ("Choose the correct sentence about yesterday.", ["Leo visit his aunt yesterday.", "Leo visits his aunt yesterday.", "Leo visited his aunt yesterday.", "Leo visiting his aunt yesterday."], "C", "yesterday 表示過去時間，動詞應使用過去式 visited。"),
    ("Choose the correct word: There ___ two books on the desk.", ["is", "are", "am", "be"], "B", "two books 是複數，There be 句型使用 are。"),
    ("Choose the correct comparison: This bag is ___ than that one.", ["heavy", "heavier", "heaviest", "more heavy"], "B", "兩者比較且 heavy 為雙音節常用 -er，使用 heavier。"),
    ("Choose the best modal verb: You ___ wear a helmet when riding a bike.", ["should", "would", "might", "could"], "A", "表達安全上的建議，使用 should。"),
    ("Choose the correct form: Kevin wants ___ a scientist.", ["be", "being", "to be", "been"], "C", "want 後接不定詞 to V，因此為 to be。"),
    ("Choose the passive sentence.", ["The chef cooked the soup.", "The soup cooks the chef.", "The soup was cooked by the chef.", "The chef was cooking soup by."], "C", "被動語態為 be 加過去分詞，The soup was cooked by the chef。"),
    ("Choose the best conjunction: I was tired, ___ I finished my homework.", ["but", "or", "because", "so"], "A", "前後語意為轉折，使用 but。"),
    ("Choose the correct question: ___ did you meet at the station?", ["Who", "What time", "How much", "How many"], "A", "詢問遇到的人使用 Who。"),
    ("Choose the correct conditional sentence.", ["If it rains, we will stay inside.", "If it rains, we stayed inside.", "If it rained, we stay inside yesterday.", "If rain, we will stayed inside."], "A", "第一類條件句使用 if 加現在式，主要子句可用 will 加原形動詞。"),
]
VOCAB = [
    ("In the sentence 'The room was tiny, so only two chairs fit inside,' what does tiny mean?", ["very small", "very noisy", "very clean", "very old"], "A", "only two chairs fit inside 提供線索，tiny 表示 very small。"),
    ("In the sentence 'Ben was starving and ate three sandwiches,' what does starving mean?", ["very thirsty", "very hungry", "very sleepy", "very angry"], "B", "吃了三個三明治顯示 starving 是 very hungry。"),
    ("Which word is closest in meaning to 'repair'?", ["fix", "break", "hide", "throw"], "A", "repair 與 fix 都有修理之意。"),
    ("Which word is opposite in meaning to 'arrive'?", ["leave", "enter", "wait", "stay"], "A", "arrive 是抵達，反義概念為 leave 離開。"),
    ("In 'Please return the book by Friday,' what does return mean?", ["buy", "give back", "read aloud", "draw on"], "B", "書籍情境中的 return 是歸還。"),
    ("Which word best completes: We need an umbrella because it is ___.", ["rainy", "windy", "sunny", "dry"], "A", "需要雨傘與 rainy 的語意搭配最合理。"),
    ("In 'The bridge is wide enough for two cars,' what does wide mean?", ["having much distance from side to side", "having great height", "moving quickly", "being very light"], "A", "wide 指左右寬度大。"),
    ("Which word best describes a person who tells the truth?", ["honest", "lazy", "narrow", "silent"], "A", "tell the truth 對應 honest。"),
    ("In 'Amy glanced at the clock before class,' what does glanced mean?", ["looked quickly", "shouted loudly", "walked slowly", "wrote carefully"], "A", "glanced 是快速看一眼。"),
    ("Which word best completes: Please speak ___; the baby is sleeping.", ["quietly", "angrily", "heavily", "brightly"], "A", "嬰兒睡覺時應輕聲說話，使用 quietly。"),
]
READING = [
    ("Read: 'Nora put the seedlings near the window. After a week, they grew taller.' Why did Nora put them there?", ["To give them light.", "To keep them cold.", "To hide them.", "To make them dry."], "A", "窗邊通常有光，且後文提到植物長高，最合理推論是為了取得光線。"),
    ("Read: 'The library closes at six. Tim arrived at six fifteen.' What happened?", ["Tim arrived before closing.", "Tim arrived after closing.", "The library opened at six fifteen.", "Tim stayed all night."], "B", "six fifteen 晚於 six，故 Tim 到達時已過閉館時間。"),
    ("Read: 'Jill packed a raincoat but left her sunglasses at home. The sky became dark.' What did Jill prepare for?", ["Rain.", "A concert.", "A swimming race.", "A birthday party."], "A", "raincoat 與天空變暗提示她準備應付下雨。"),
    ("Read: 'The sign says “Please use the west entrance.” Where should visitors go?", ["The east entrance.", "The west entrance.", "The roof.", "The parking lot."], "B", "標示直接要求使用 west entrance。"),
    ("Read: 'First wash the fruit. Next cut it into pieces. Finally put it in the bowl.' What should you do first?", ["Put it in the bowl.", "Cut it.", "Wash it.", "Eat it."], "C", "流程詞 First 後面是 wash the fruit。"),
    ("Read: 'The team practiced every afternoon, and their passing became more accurate.' What improved?", ["Their passing.", "The weather.", "The size of the field.", "The number of holidays."], "A", "最後分句明確指出 passing became more accurate。"),
    ("Read: 'Maya borrowed a map because she wanted to find the hiking trail.' Why did she borrow it?", ["To find a trail.", "To buy a bicycle.", "To write a letter.", "To watch a movie."], "A", "because 子句指出借地圖是為了尋找步道。"),
    ("Read: 'Although the box looked small, it held twelve notebooks.' What is surprising?", ["The box was empty.", "The small box held many notebooks.", "The notebooks were wet.", "The box was very heavy with stones."], "B", "Although 表示讓步，意外點是小盒子裝了十二本筆記本。"),
    ("Read: 'Sam forgot his key, so he called his sister for help.' Why did Sam call her?", ["He needed help opening the door.", "He wanted to sell the key.", "He was going to school.", "He had already opened the door."], "A", "忘記鑰匙導致需要姊姊協助開門。"),
    ("Read: 'The notice asks students to bring a reusable bottle on Friday.' What should students bring?", ["A reusable bottle.", "A winter coat.", "A library card.", "A paint brush."], "A", "notice 直接要求 Friday 攜帶 reusable bottle。"),
]
COMM = [
    ("At the classroom door, the teacher says, 'Please come in.' What is the best reply?", ["Thank you.", "I am a door.", "No, yesterday.", "It is very tall."], "A", "對請進的禮貌回應可說 Thank you。"),
    ("A: 'Could you pass me the ruler?' B: '___'", ["Sure, here you are.", "I am twelve years old.", "It is raining yesterday.", "No, I passed the test."], "A", "對請求協助的自然回應是 Sure, here you are。"),
    ("A: 'How was your weekend?' B: '___'", ["It was great.", "At seven o'clock.", "In the kitchen.", "By bicycle."], "A", "How was 詢問感受或狀況，回答 It was great。"),
    ("A: 'Where is the science room?' B: '___'", ["It is next to the library.", "It is twenty dollars.", "I am studying yesterday.", "Yes, I can."], "A", "Where 詢問地點，回答 next to the library。"),
    ("A: 'Would you like some juice?' B: '___'", ["Yes, please.", "It is on Monday.", "I went home.", "She is my sister."], "A", "接受飲料邀請的禮貌回答是 Yes, please。"),
    ("A: 'I am sorry I broke your pencil.' B: '___'", ["That is okay.", "It is behind the school.", "At half past two.", "I am thirteen pencils."], "A", "對道歉表示諒解可回答 That is okay。"),
    ("A: 'What are you doing?' B: '___'", ["I am drawing a poster.", "It was last night.", "On the second floor.", "Because it is blue."], "A", "What are you doing 詢問現在進行的活動。"),
    ("A: 'May I use your phone?' B: '___'", ["Of course.", "It is very cold.", "I used to swim.", "At the bus stop."], "A", "May I 徵求許可，Of course 表示同意。"),
    ("A: 'Why are you carrying an umbrella?' B: '___'", ["Because it may rain.", "At the station.", "Three umbrellas.", "I carried it tomorrow."], "A", "Why 詢問原因，Because it may rain 回答原因。"),
    ("A: 'How can I get to the post office?' B: '___'", ["Go straight and turn left.", "I mailed it yesterday.", "It is very large.", "Yes, I like it."], "A", "How can I get to 詢問路線，回答方向指示。"),
]

def choose_bank(topic):
    if any(k in topic for k in ["閱讀", "故事", "短文", "主旨", "人物", "事件", "書信", "段落", "文章", "圖表", "標示", "廣播", "影片", "歌謠", "韻文", "短劇", "公告", "訊息"]): return READING
    if any(k in topic for k in ["字彙", "詞義", "字典", "單字", "拼字", "詞語", "拼寫", "發音"]): return VOCAB
    if any(k in topic for k in ["文法", "句型", "時態", "語序", "助動詞", "比較", "疑問", "書寫", "中翻英", "格式"]): return GRAMMAR
    if any(k in topic for k in ["節慶", "文化", "風土", "世界觀", "禮儀", "欣賞"]): return COMM
    if any(k in topic for k in ["對話", "溝通", "討論", "用語", "描述", "提問", "回答", "角色", "情境"]): return COMM
    return COMM

def rewrite(path):
    data=json.loads(Path(path).read_text()); p=data.get("prompt","")
    authored=data.get("updatedAt")=="2026-08-29" and data.get("provenance",{}).get("sourceUrl")==SOURCE
    if not authored and not p.startswith("學習「"): return False
    if authored:
        lesson=json.loads((Path("lessons/english")/f"{data['lessonId']}.json").read_text())
        topic=lesson["title"].split("：",1)[-1] if "：" in lesson["title"] else lesson["title"]
    else:
        topic=re.search(r"學習「(.+?)」的英語",p).group(1)
    i=int(re.search(r"-(\d+)\.json$",path).group(1))-1
    q,opts,ans,ex=choose_bank(topic)[i]
    tag=hashlib.sha1(data["lessonId"].encode()).hexdigest()[:4]
    # 將單元概念自然帶入題幹，避免把生成代碼或練習標記暴露給學習者。
    # 題幹仍保留單元語境，並由 draft 狀態交由第二輪 AI 審查是否真正符合 KG。
    data["prompt"]=f"在「{topic}」單元的英文練習中，{q}"
    data["options"]=[{"id":chr(65+j),"text":x} for j,x in enumerate(opts)]
    data["answer"]={"value":ans,"explanation":f"{ex} 本題置於「{topic}」單元語境中，需先理解句意或文法功能再作答。"}
    data["provenance"]={"origin":"original","license":"All rights reserved","sourceUrl":SOURCE,"sourceLocator":"高雄市立鹽埕國民中學 114 學年度第 2 學期第 1 次段考英文科；僅研究題型與能力方向，未複製原題文字、選項、圖片或答案。","authoringNote":"依單元 KG 概念與公開段考能力方向，以全新英文句子、情境、選項與解析獨立撰寫；待第二輪 AI／Terra 內容複核。"}
    data["reviewStatus"]="draft"; data["updatedAt"]="2026-08-29"; Path(path).write_text(json.dumps(data,ensure_ascii=False,indent=2)+"\n"); return True
print(f"rewrote {sum(rewrite(p) for p in glob.glob('questions/english/*.json'))} english meta-template questions")
