#!/usr/bin/env python3
"""Rewrite the 7-IV-3 original questions and replace unverified exam refs."""
import json
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
QUESTION_DIR = ROOT / "questions/english"
TODAY = "2026-09-27"

# Public-school sources are used only to study item form and reasoning demand.
# No original wording, answer, image, or dialogue is reproduced.
SOURCES = [
    {
        "url": "https://www.yacjh.kh.edu.tw/upload/221/101_30637/114%E4%B8%8B%E5%AD%B8%E6%9C%9F%E7%AC%AC%E4%B8%80%E6%AC%A1%E6%AE%B5%E8%80%83%E4%B8%89%E5%B9%B4%E7%B4%9A%E8%8B%B1%E6%96%87.pdf",
        "title": "高雄市立鹽埕國中114學年度下學期第一次段考三年級英文科公開試卷",
        "year": "114-2",
        "locator": "整份試卷；只參考對話語意與情境回應的評量形式，不宣稱對應原卷特定題目",
        "observedPattern": "以全新人物、情境與語句設計情境理解題，要求依對話目的判斷合宜回應；本題不沿用原卷文本或答案。",
    },
    {
        "url": "https://www.kcjh.kh.edu.tw/upload/190/104_34764/%E4%B8%80%E5%B9%B4%E7%B4%9A-%E8%8B%B1%E8%AA%9E.pdf",
        "title": "高雄市立國昌國中110學年度第1學期第1次段考七年級英文科試題",
        "year": "110-1",
        "locator": "PDF第2頁第21至25題對話回應及第3頁第32至33題對話理解；本組只參考題型，不重用原題",
        "observedPattern": "公開卷具備情境對話回應與理解評量；本站另創對話內容並聚焦語言／非語言線索、澄清與輪替。",
        "locatorLevel": "item",
    },
    {
        "url": "https://www.ycm.kh.edu.tw/upload/297/104_62703/111-1%282%29%E4%B8%83%E5%B9%B4%E7%B4%9A%E8%8B%B1%E6%96%87%E8%A9%A6%E9%A1%8C.pdf",
        "title": "高雄市立燕巢國中111學年度第一學期七年級第二次英文科試題卷",
        "year": "111-1",
        "locator": "整份七年級英文試卷；僅參考對話回應與情境語意判讀型態",
        "observedPattern": "公開卷包含依情境選擇合宜言語回應的對話題型；本組改用全新語料測試非語言線索、澄清與溝通修補。",
    },
]

ITEMS = [
    {
        "answer": "C",
        "options": ["A student is asking for a dictionary", "A storm is being announced", "Someone is being invited to sit", "Everyone is being warned to leave"],
        "explanation": "正確答案是 C。空椅說明現場有可坐的位置，指向座位的動作把注意力引向它，微笑又讓邀請的解讀較符合情境。這是依多項線索作出的合理推論，不代表同一手勢在所有文化和場合都只有一種意思。",
        "strategy": "把手勢放回場景解讀：先找動作指向的物件，再用表情與當下需求交叉檢查；若線索仍不足，保留為最可能的意思而非通用定律。",
        "steps": [
            "先確認場景：對方看見一張空椅，題目要推測這個動作傳達什麼。",
            "手指指向座位，動作焦點是椅子；微笑提供友善而非警告的情緒線索。",
            "把候選訊息逐一對照：字典、暴風雨與離開都沒有場景線索支持。",
            "因此選 C：邀請某人坐下；它同時解釋座位、指向動作和微笑。",
            "結論只適用於這個情境；若對方沒有回應，可用簡短問句確認，而不把手勢當成絕對訊號。",
        ],
    },
    {
        "answer": "B",
        "options": ["The speaker is refusing to listen", "The speaker is showing interest in what was said", "The speaker is threatening the listener", "The speaker is giving a bus schedule"],
        "explanation": "正確答案是 B。說話者用語本身表示覺得有意思，溫和語調和點頭也與正向回應一致，非語言訊號因此加強了字面訊息。點頭只能支持此刻有在回應，不能單獨證明對方同意談話中的每個主張。",
        "strategy": "比較語句與聲音、動作是否一致；一致時可提高某種解讀的可信度，若彼此矛盾則先澄清，不把點頭直接等同全面同意。",
        "steps": [
            "先讀字面內容：That is interesting 表示說話者認為內容有意思。",
            "再檢查兩項非語言線索：聲音溫和、同時點頭，兩者都沒有呈現敵意或拒絕。",
            "把字面與語氣合併，正向興趣比威脅、拒聽或報公車時間更有根據。",
            "答案選 B：說話者正表現出對談話內容的興趣。",
            "不要把「感興趣」擴大成「同意所有觀點」；若需要確認立場，接著問對方最認同哪一點。",
        ],
    },
    {
        "answer": "D",
        "options": ["Pretend that the missing place is already clear", "Blame the other person and end the conversation", "Demand a new meeting without explaining the problem", "Ask politely for the place to be repeated"],
        "explanation": "正確答案是 D。問題缺少的是會面地點資訊，因此直接而有禮貌地請對方重說地點，能補回缺口。假裝聽懂可能導致走錯地方；責怪對方或要求改期，都沒有先處理目前缺失的資訊。",
        "strategy": "澄清要對準資訊缺口：指出哪一部分沒聽清楚，禮貌請對方重述；收到後再覆述關鍵資訊確認。",
        "steps": [
            "把已知和未知分開：知道有約會面，但不知道約在哪裡。",
            "選擇能補上「地點」的回應；重問地點比泛稱聽不懂更精準。",
            "排除假裝明白（會傳播錯誤）、責怪（不補資訊）和無故改期（改變任務）。",
            "答案是 D：禮貌請對方再說一次地點。",
            "聽到地點後，可用自己的話覆述，例如確認建築名稱或入口，避免只聽到仍不確定。",
        ],
    },
    {
        "answer": "A",
        "options": ["Let me explain it another way with an example.", "I will repeat the same fast sentence more loudly.", "I will stop and blame the listener.", "I will change to an unrelated topic."],
        "explanation": "正確答案是 A。對方困惑表示目前說法可能沒有傳達成功；換一種說法並補上例子，能提供新的理解入口。提高音量或加快重複原句不會自動解決詞義或邏輯上的困難，責怪聽者則中斷合作。",
        "strategy": "把聽者的困惑當作調整說明的回饋：改變表達方式、縮小一次要說的資訊，並用例子檢查對方是否抓到重點。",
        "steps": [
            "注意到對方看起來困惑，表示原來的說明尚未形成共同理解。",
            "先改變解釋途徑；例子能把抽象說法連到可想像的具體情況。",
            "同一句講得更快、更大聲仍是相同內容；責怪和換題都沒有修補原本的理解落差。",
            "選 A：改用另一種說法並加入例子。",
            "說完停下來，請對方用自己的話說說理解到哪裡，再決定是否需要另一個例子。",
        ],
    },
    {
        "answer": "C",
        "options": ["Why do you have a ruler at all?", "Give me the ruler now or else.", "Could I borrow your ruler for a minute, please?", "Your ruler belongs to me today."],
        "explanation": "正確答案是 C。Could I 以詢問方式徵求同意，please 顯示禮貌，for a minute 也交代借用時間短。其他選項不是威脅或命令，就是把物品說成自己的，沒有尊重對方對物品的決定權。",
        "strategy": "提出請求時交代具體需要、使用詢問句並說明範圍，讓對方能自由答應或拒絕；得到物品後記得歸還並致謝。",
        "steps": [
            "辨認目的：需要短暫借用同學的尺，不是取得所有權。",
            "檢查句型是否留下選擇空間；Could I borrow… 是詢問許可，不是命令。",
            "for a minute 限定借用時間，please 使語氣更有禮貌；其餘選項帶有威脅、質疑或侵占。",
            "所以選 C，向同學有禮貌地詢問能否借尺一會兒。",
            "說完等待對方回覆；若對方同意，使用後及時歸還並道謝，若拒絕則尊重決定。",
        ],
    },
    {
        "answer": "B",
        "options": ["The map is definitely complete and easy to follow", "The listener may be confused and need part of the map explained", "The listener wants to sing a song", "The listener has already left the room"],
        "explanation": "正確答案是 B。聽者看著不清楚的地圖並挑起眉毛，可能是在表達不確定或有疑問；兩個線索一起使「需要解釋」較合理。但表情不能單獨診斷對方想法，應以開放式問題確認是哪一處不清楚。",
        "strategy": "將表情當作需要確認的線索，而非讀心證據；描述可見困難，再問對方卡在哪個位置，避免把推測說成事實。",
        "steps": [
            "場景焦點是地圖：聽者正看著一張不清楚的地圖，並挑起眉毛。",
            "挑眉可能表示疑惑；與地圖難辨認合看，支持「需要說明」的可能性。",
            "完成且易讀與題目描述衝突；唱歌或離開房間都沒有線索支持。",
            "答案選 B：聽者可能困惑，需要有人解釋地圖的一部分。",
            "用中性問題確認，例如「Which part of the map is unclear?」，不要直接斷言對方看不懂。",
        ],
    },
    {
        "answer": "D",
        "options": ["Speak louder until the other person gives up", "Walk away without hearing the topic", "Change every answer into a question", "Pause, let one person finish, and then take a turn"],
        "explanation": "正確答案是 D。兩人同時開口時，問題在於發言順序重疊；先停一下、讓一人說完再接話，能讓訊息被聽見也保留雙方發言機會。提高音量只會競爭聲量，離開或亂改句型則沒有解決輪流問題。",
        "strategy": "先修復談話順序，再處理內容；在重疊處暫停、用眼神或簡短手勢示意，等對方結束後再接續。",
        "steps": [
            "辨認障礙：兩個人同時開始說話，彼此的訊息互相遮蓋。",
            "此處需要的是輪流，不是更大的音量或更多新問題。",
            "等待對方講完會減少重疊，並保留自己稍後表達的機會。",
            "因此選 D：先停下，讓一人說完，再輪到另一人。",
            "實際談話中可先示意「You first」，聽完後回應對方剛才的重點，再說自己的想法。",
        ],
    },
    {
        "answer": "B",
        "options": ["The incorrect number is your problem now.", "Sorry, I meant Room 305, not Room 350.", "I will give three more room numbers without correcting myself.", "Room numbers cannot be spoken aloud."],
        "explanation": "正確答案是 B。305 和 350 容易因數字順序而混淆；這句話先承認剛才說錯，再用 not 對比明確指出正確房號，能讓聽者立即更新資訊。只道歉不給正確號碼，或再丟出更多數字，都會留下歧義。",
        "strategy": "修正口誤時採「指出錯誤資訊—明說正確資訊」的對比結構，必要時請對方覆述，確保更正傳到每位受影響的人。",
        "steps": [
            "先找出錯誤造成的實際風險：對方可能走到 Room 350，而目的地其實是 Room 305。",
            "有效修正至少要提供可採取行動的正確房號，不能只表達歉意或責怪聽者。",
            "B 同時標出 305 是原本誤說的號碼、350 才是更正值，對比清楚。",
            "選 B：Sorry, I meant Room 305, not Room 350. 這句完成了承認與更正。",
            "若訊息已傳給多人，還要同步通知相同對象；可請對方確認收到的是 Room 350。",
        ],
    },
    {
        "answer": "A",
        "options": ["Avoid assuming disinterest and consider the whole context and the visitor's words", "Immediately accuse the visitor of ignoring you", "End every conversation without listening", "Assume every culture uses exactly the same gesture"],
        "explanation": "正確答案是 A。題目已明示訪客所處文化把避免眼神接觸視為禮貌，因此不能直接用自己熟悉的眼神規範推斷對方不專心。應把文化背景、談話內容與其他反應一起考慮；尊重差異不等於認定所有人都相同。",
        "strategy": "解讀非語言行為時先納入當事人的文化與情境；不要把自己的慣例當普遍標準，必要時以尊重、不施壓的方式詢問溝通偏好。",
        "steps": [
            "題幹明確提供文化背景：這位訪客避免眼神接觸是出於禮貌。",
            "因此不能將「沒有眼神接觸」直接等同不感興趣；還要聽對方說了什麼及觀察其他回應。",
            "指責、停止聆聽或假設所有文化都一樣，都忽略了題目提供的脈絡。",
            "答案是 A：不先推定對方不專心，而是綜合其話語與情境判斷。",
            "若仍需要調整互動，可詢問對方較自在的談話方式，不強迫對方採用自己的習慣。",
        ],
    },
    {
        "answer": "C",
        "options": ["Repeat the same unclear words while turning away", "Use only a gesture and never check whether it worked", "Adjust the noise or distance if appropriate, speak clearly, add a simple gesture, then check", "Pretend the partner understood and move to another task"],
        "explanation": "正確答案是 C。吵雜環境可能遮住口語指示，對方的困惑又顯示訊息尚未確認成功；適度改善聆聽條件、清楚重述、配合簡單手勢並確認理解，能同時處理環境和訊息兩端。靠近前應尊重對方空間，手勢也不能取代確認。",
        "strategy": "先降低環境障礙，再用清楚短句和輔助手勢傳遞訊息，最後要求對方確認關鍵步驟；不要把點頭或沉默視為已理解。",
        "steps": [
            "找出兩個問題來源：房間很吵，且夥伴漏聽指示後看起來不確定。",
            "先選可行的環境調整；若要移近，注意距離並先確定對方感到自在。",
            "用清楚短句重述，配合指向相關物件的簡單手勢，讓聲音和視覺線索互補。",
            "所以選 C：調整環境、清楚說明、以手勢輔助，再檢查理解。",
            "請夥伴覆述下一步；若內容仍有落差，就換句話說並再次確認，而非假裝已懂。",
        ],
    },
]


def make_refs(index: int) -> list[dict]:
    focus = [
        "由情境與可見線索推斷說話者可能意圖",
        "比較字面語意與語調、點頭的一致性",
        "辨認缺漏資訊並選擇合宜澄清句",
        "依聽者回饋改述並以例子修補理解",
        "比較請求句型、禮貌標記與允許空間",
        "結合表情與物件脈絡，但避免把推測當定論",
        "依談話輪替情境選擇不競逐發言的回應",
        "以明確對比修正容易混淆的資訊",
        "將文化脈絡納入非語言行為解讀",
        "整合環境、口語、手勢及理解確認",
    ][index - 1]
    refs = []
    for src in SOURCES:
        refs.append({
            "url": src["url"], "title": src["title"], "year": src["year"],
            "subject": "english", "locator": src["locator"],
            "observedPattern": f"{src['observedPattern']}本題的研究焦點：{focus}。",
            "reuseDecision": "pattern-only", "status": "recorded",
            "locatorLevel": src.get("locatorLevel", "paper"),
        })
    return refs


for index, item in enumerate(ITEMS, start=1):
    path = QUESTION_DIR / f"question-english-performance-7-iv-3-{index}.json"
    data = json.loads(path.read_text(encoding="utf-8"))
    data["options"] = [{"id": chr(65 + i), "text": text} for i, text in enumerate(item["options"])]
    data["answer"] = {"value": item["answer"], "explanation": item["explanation"]}
    data["examPatternRefs"] = make_refs(index)
    data["provenance"]["sourceUrl"] = SOURCES[0]["url"]
    data["provenance"]["sourceLocator"] = "三份公立國中英文公開段考僅供對話回應、語意線索與溝通情境評量型態研究；本題使用不同情境及措辭，未複製原題、選項、圖片或答案。"
    data["provenance"]["authoringNote"] = "依官方英語課綱 KG 與鹽埕、新莊、燕巢三所公立國中公開英文評量所呈現的情境判讀／對話回應型態，獨立設計題幹、選項、正解、繁中解析及逐題五步詳解；未複製原卷；仍待完整內容與版權 QA。"
    data["solutionStrategy"] = item["strategy"]
    data["solutionSteps"] = item["steps"]
    data["updatedAt"] = TODAY
    data["reviewStatus"] = "draft"
    path.write_text(json.dumps(data, ensure_ascii=False, indent=2) + "\n", encoding="utf-8")

catalog_path = ROOT / "data/public-exam-sources.json"
catalog = json.loads(catalog_path.read_text(encoding="utf-8"))
catalog_entries = [
    {
        "id": "ycm-111-1-grade7-english",
        "school": "高雄市立燕巢國民中學",
        "grade": "7",
        "subject": "english",
        "exam": "111學年度第1學期第2次段考七年級英文科",
        "questionUrl": SOURCES[2]["url"],
        "answerLocator": "公開七年級英文試題卷；本次採卷級對話回應型態參照，未宣稱對應特定題號",
        "usePolicy": "只研究公立學校公開英文評量的對話語意與情境回應形式；本站題幹、選項、答案及解析均原創，不複製原卷。",
        "verifiedAt": TODAY,
    },
]
catalog["sources"] = [entry for entry in catalog["sources"] if entry.get("id") != "hcjh-113-2-grade7-english"]
known_ids = {entry["id"] for entry in catalog["sources"]}
catalog["sources"].extend(entry for entry in catalog_entries if entry["id"] not in known_ids)
catalog["updatedAt"] = TODAY
catalog_path.write_text(json.dumps(catalog, ensure_ascii=False, indent=2) + "\n", encoding="utf-8")

print(f"rewrote {len(ITEMS)} original 7-IV-3 questions; all remain draft")
