#!/usr/bin/env python3
"""Independently rewrite classroom-word questions with public-school exam refs."""
import json
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
YICHANG_114_T3 = "https://www.ycjh.hlc.edu.tw/modules/tad_uploader/index.php?cat_sn=449&cfsn=2995&fn=114-1-%E7%AC%AC3%E6%AC%A1%E6%AE%B5%E8%80%837%E5%B9%B4%E7%B4%9A%E8%8B%B1%E8%AA%9E%E7%A7%91%E9%A1%8C%E7%9B%AE%E5%8D%B7-%E6%89%B6%E5%BF%97%E6%81%A9.pdf&op=dlfile"
YICHANG_114_T2 = "https://www.ycjh.hlc.edu.tw/modules/tad_uploader/index.php?cat_sn=449&cfsn=3045&fn=114-1-%E7%AC%AC2%E6%AC%A1%E6%AE%B5%E8%80%837%E5%B9%B4%E7%B4%9A%E8%8B%B1%E8%AA%9E%E7%A7%91%E9%A1%8C%E7%9B%AE%E8%88%87%E7%AD%94%E6%A1%88-%E6%9B%BE%E8%A9%A0%E5%9C%92.pdf&op=dlfile"
YICHANG_112_T3 = "https://www.ycjh.hlc.edu.tw/modules/tad_uploader/index.php?cat_sn=417&cfsn=2829&name=112-2-%E7%AC%AC3%E6%AC%A1%E6%AE%B5%E8%80%837%E5%B9%B4%E7%B4%9A%E8%8B%B1%E8%AA%9E%E7%A7%91%E9%96%B1%E8%AE%80%E9%A1%8C%E7%9B%AE-%E7%8E%8B%E7%90%87%E8%90%B1.pdf&op=dlfile"
SOURCES = {
    YICHANG_114_T3: ("花蓮縣立宜昌國中", "114學年度第一學期第三次段考七年級英語科試題卷", "公開查閱不等於可重製；只參考逐題標示的詞彙、方位、時間及短文判讀能力，不複製原題文字、選項或答案。"),
    YICHANG_114_T2: ("花蓮縣立宜昌國中", "114學年度第一學期第二次段考七年級英語科試題卷", "公開查閱不等於可重製；只參考逐題標示的命令句、校園情境、行程資料與指令判讀形式，不複製原題文字、選項、圖片或答案。"),
    YICHANG_112_T3: ("花蓮縣立宜昌國中", "112學年度第二學期第三次段考七年級英語科試題卷", "公開查閱不等於可重製；只參考逐題標示的順序、頻率、校園工作與情境詞義判讀方式，不複製原題文字、選項或答案。"),
}

ITEMS = [
    {"answer":"D","source":(YICHANG_114_T3,4,"PDF page 1, item 4: infer a location preposition from the scene"),"prompt":"The microscope is on the bench. Please put the slide box beside it. Where should the box go?","options":[("A","Inside the microscope."),("B","Under the bench."),("C","Far across the room."),("D","Next to the microscope.")],"explanation":"Beside 表示在某物旁邊，因此 slide box 要放在 microscope 的側邊。D 的 next to 表達同一空間關係；其他選項分別表示在裡面、下方或遠處。","strategy":"先找出方位字，再確認它連結的兩個物件；把文字關係轉成簡單位置圖，比逐字翻譯更容易排除相反方向。","steps":["句子給了兩個定位物件：slide box 是要移動的物品，microscope 是參照物。","圈出 beside，判斷這是位置關係而不是移動方向、容器或上下位置。","把工作臺想成平面圖，將盒子放在顯微鏡一側，並確認兩件器材彼此相鄰而非重疊。","D 的 next to 符合相鄰；inside、under、far across 分別違反旁邊這個關係。","因此選 D；實際操作時先指認參照物，再把盒子放在它旁邊，不要放到器材內部。"]},
    {"answer":"B","source":(YICHANG_114_T3,1,"PDF page 1, item 1: use a time preposition to place one activity before another"),"prompt":"The art room closes at 4:00. A student must return the brushes before 3:50. By what time should the brushes be back?","options":[("A","After 4:00."),("B","Earlier than 3:50."),("C","Exactly at 4:00."),("D","Any time tomorrow.")],"explanation":"Before 3:50 表示在3:50之前完成，不是等到關門後或隔天。B 唯一符合期限；題目沒有要求恰好在某一分鐘完成。","strategy":"讀到 before 或 after 先畫出時間先後箭頭，再將期限與活動時間排序；不要把「之前」誤當成「當下」或「之後」。","steps":["先分清兩個時間資訊：房間4:00關閉，歸還刷具的期限則更早，是3:50之前。","找出 before 修飾的時間點，表示完成動作必須落在3:50的左側。","把時間軸排成「較早完成 → 3:50期限 → 4:00關門」，即可看出安全完成區間。","B 表示早於3:50；A晚於關門、C晚於指定期限、D把期限推到隔天。","選 B；安排實際行動時也要留出走到器材櫃的時間，不應把 before 解讀成準時抵達即可。"]},
    {"answer":"C","source":(YICHANG_114_T2,1,"PDF page 1, item 1: understand a classroom prohibition and its action words"),"prompt":"A sign at the media room says, “Please don’t move the camera while the red light is on.” What should a student do when the light is red?","options":[("A","Carry the camera outside."),("B","Turn the camera toward the door."),("C","Leave the camera where it is."),("D","Ask a partner to move it.")],"explanation":"Don’t move 是禁止移動。紅燈亮時，學生應讓攝影機留在原位，所以 C 正確；請別人代移仍違反同一條規定。","strategy":"先把 don’t 當作禁止標記，接著找出被禁止的動作與條件；不要只看懂動詞，卻漏掉否定或適用時機。","steps":["先確認規則有明確條件：只有紅燈亮起時，這項器材指示才限制學生的動作。","辨認 don’t move 的結構，意思是不要搬動攝影機，而不是不要開燈。","將規則套回情境：現在紅燈亮，所以攝影機應保持原位不動，直到訊號改變。","C 符合禁止移動；A、B 都搬動或轉動器材，D 只是換人執行仍然移動。","答案選 C；遇到安全規則，應保留否定詞與條件一起判斷，不能只挑一個看似可行的動作。"]},
    {"answer":"A","source":(YICHANG_114_T2,18,"PDF page 2, item 18: interpret a teacher's classroom direction"),"prompt":"The teacher points to the map and says, “Follow the yellow route to the greenhouse.” What should the group do?","options":[("A","Go along the yellow route to the greenhouse."),("B","Erase the yellow route from the map."),("C","Wait inside the classroom."),("D","Choose a different destination.")],"explanation":"Follow the yellow route 是沿著黃色路線前進到指定目的地，不是擦掉路線或改去別處。A 同時保留了路線和 greenhouse 兩項指令資訊。","strategy":"聽讀指令時分開抓動作、路徑與目的地三個槽位；若只記住 route 卻漏掉終點，仍可能走錯方向。","steps":["句子先指定動作 follow，再給出路徑 yellow route，最後給出目的地 greenhouse。","將三個資訊依序標記，避免把 follow 誤讀成追蹤、擦除或等待。","在地圖上從目前位置沿黃色線移動，直到抵達溫室，不自行更換終點。","A 完整保留路線和目的地；B、C、D 分別改變動作、停留位置或任務目標。","所以選 A；執行校園指令時，出發前重述路徑與終點可快速檢查是否聽懂。"]},
    {"answer":"D","source":(YICHANG_112_T3,31,"PDF page 4, item 31: infer the meaning of a school-duty verb from the surrounding dialogue"),"prompt":"The class monitor checks the equipment list after cleanup to make sure every item is back. What does checks mean here?","options":[("A","Buys new equipment."),("B","Carries everything home."),("C","Hides the list."),("D","Looks over the list to confirm the items.")],"explanation":"後面的目的語 make sure every item is back 說明 monitor 要查看清單、確認物品是否歸位。D 符合 checks 在此處的意思，其他選項都不是核對。","strategy":"碰到多義動詞時，不急著套第一個中文意思；先讀它後面的物件，再找句中說明目的的線索來縮小解釋。","steps":["定位主詞 class monitor 和動作 checks，接著確認 checks 的受詞是 equipment list。","再讀目的片語 make sure，知道這個動作是為了確認物品是否全部放回。","把工作流程想成整理後逐項對照清單，而不是購買、搬回家或藏起清單。","D 表示查看清單並確認物品；A、B、C 都和核對工作的目的相矛盾。","所以選 D；遇到 check、watch 等多義字，應用受詞和目的判定當下語意。"]},
    {"answer":"B","source":(YICHANG_112_T3,30,"PDF page 4, item 30: infer a frequency question from repeated weekly tasks"),"prompt":"The library team shelves returned books on Monday, Wednesday, and Friday. How often do they do this job?","options":[("A","Once a month."),("B","Three times a week."),("C","Every day."),("D","Only on Friday.")],"explanation":"工作表列出一週中的星期一、三、五，共三個執行日，所以頻率是每週三次。B 正確；不能只挑最後出現的 Friday，也不是每天都做。","strategy":"遇到 how often，將列出的日期逐一標記並計數，再注意問題問的是一週、一天或整月的頻率單位。","steps":["先圈出題目問 how often，這是在問重複頻率，不是在問某一次發生的日期。","從安排中逐項標記 Monday、Wednesday、Friday，確認三個不同的工作日。","把三個日期歸入同一週，得到每週執行三次，並與「每天」或「每月」的週期分開。","B 同時符合次數與單位；A、C、D 都錯置時間範圍或漏算兩天。","選 B；若行程跨越多週，先判定列表的週期，再按該週期計數，避免把日期數當成月份頻率。"]},
    {"answer":"A","source":(YICHANG_112_T3,27,"PDF page 4, item 27: use ordinal vocabulary to identify the earliest person"),"prompt":"Mika arrives at the classroom before everyone else and unlocks the door. Which word describes Mika in the arrival order?","options":[("A","The first."),("B","The last."),("C","The next-to-last."),("D","The one in the middle.")],"explanation":"Before everyone else 表示 Mika 最早到，因此在到達順序中是 the first。A 對應最前的位置；last 與 middle 都和「比所有人早」不符。","strategy":"先把事件按時間排隊，再將序數字詞對應到隊列位置；first 和 last 描述位置，不是人數或頻率。","steps":["題目給出關鍵線索 before everyone else，意思是 Mika 的抵達時間早於所有同學。","把全班依抵達時間排成一列，並依實際先後比較，Mika 位在隊伍最前端。","最前端的位置用序數 the first 表達，與人數多少無關。","A 指第一位；B 是最後一位，C 是倒數第二，D 是中間位置，皆和線索矛盾。","所以選 A；判斷序數時先建立順序，再找位置名稱，不要把 first 誤當成「唯一」。"]},
    {"answer":"C","source":(YICHANG_114_T3,31,"PDF page 3, item 31: combine a short passage's details to identify its central message"),"prompt":"A short notice says that students should return tools, wipe the worktables, and sort reusable materials after the design activity. What is the notice mainly about?","options":[("A","How to register for the design activity."),("B","Which student made the best project."),("C","What students must do when cleaning up after the activity."),("D","Why reusable materials are expensive.")],"explanation":"三個細節都在說活動結束後要做的整理工作：歸還工具、擦桌面、分類材料。C 能涵蓋共同主題；其餘選項把焦點轉到報名、作品評比或費用。","strategy":"找主旨時把每句細節分類，尋找能包住多個細節的共同上位概念；不要將其中一個名詞誤當成整段主旨。","steps":["先列出通知中的三項行動：歸還工具、擦工作桌、分類可重用材料。","比較這些動作的共同時間與目的，發現都發生在設計活動結束後，且屬於收拾工作。","用能概括三項行動的較大概念表述，而不是只重複材料分類這個單一細節。","C 同時涵蓋三項整理行動；A、B、D 沒有足夠文本線索支撐。","所以選 C；主旨答案應能解釋段落中多數細節，若只能對應一小句，就太狹窄。"]},
    {"answer":"D","source":(YICHANG_114_T2,25,"PDF page 3, item 25: compare repeated entries in a weekly school schedule"),"prompt":"A club schedule lists robotics at 9:00 on Tuesday and Friday, while art is listed only on Thursday. Which activity meets more often?","options":[("A","Art, because Thursday comes first."),("B","Both meet the same number of times."),("C","Art, because it has a shorter name."),("D","Robotics, because it appears on two days.")],"explanation":"比較課表時數出現位置：robotics 有星期二、星期五兩次，art 只有星期四一次，因此 robotics 開課較頻繁。D 是唯一使用表格次數而非無關線索的答案。","strategy":"比較行程表時先確定比較對象與共同單位，再數各自出現次數；不要讓星期先後或字詞長短干擾資料判讀。","steps":["先找出題目要求比較的兩項活動：robotics 和 art，而不是比較星期或課名。","在一週課表中標記 robotics 的 Tuesday、Friday 兩格，再標記 art 的 Thursday 一格。","把兩者都換成每週出現次數，分別是兩次與一次，單位一致才可比較。","D 說明 robotics 出現兩天；A、B、C 沒有依據課表的實際次數。","因此選 D；遇到表格比較題，先圈欄列與單位，再計數，不能憑星期順序猜頻率。"]},
    {"answer":"A","source":(YICHANG_114_T2,17,"PDF page 2, item 17: resolve a classroom direction using its context and referent"),"prompt":"During a science demonstration, the teacher says, “Please keep your hands away from the glass tank.” What should students do?","options":[("A","Watch without touching the tank."),("B","Move the tank closer."),("C","Put their hands inside the tank."),("D","Carry the tank to another room.")],"explanation":"Keep your hands away 表示手不要靠近或碰觸玻璃缸；在示範中應觀看但不觸摸。A 符合指令，其他選項都讓手靠近或移動器材。","strategy":"將指令拆成動作與受詞，再用場景判斷它要避免的行為；away from 是保持距離，不是把物品搬走。","steps":["辨認 teacher 的指令受詞是 your hands，參照物是 glass tank。","抓住 keep ... away from 的距離關係，意思是讓雙手不要接近玻璃缸。","結合 science demonstration 情境，推知學生可以觀察，但不應接觸或移動器材。","A 保持安全距離；B、C、D 都會使手碰近器材或造成不必要搬動。","選 A；聽到器材安全指令時，先確認被限制的是身體部位還是物品，再選安全行動。"]},
]


def make_ref(url: str, number: int, locator: str) -> dict:
    school, exam, boundary = SOURCES[url]
    year = {YICHANG_114_T3: "114-1-3", YICHANG_114_T2: "114-1-2", YICHANG_112_T3: "112-2-3"}[url]
    return {
        "url": url,
        "title": f"{school}{exam}",
        "year": year,
        "subject": "english",
        "locator": locator,
        "observedPattern": f"只參照第{number}題的校園詞彙／指令／行程或語境推論形式；{boundary}",
        "reuseDecision": "pattern-only",
        "status": "recorded",
        "locatorLevel": "item",
    }


def main() -> None:
    paths = [ROOT / f"questions/english/question-english-performance-3-iv-2-{number}.json" for number in range(1, 11)]
    if len(ITEMS) != 10 or any(not path.is_file() for path in paths):
        raise FileNotFoundError("Expected ten stable question IDs; no writes performed")
    for path, item in zip(paths, ITEMS, strict=True):
        data = json.loads(path.read_text(encoding="utf-8"))
        url, number, locator = item["source"]
        data["prompt"] = item["prompt"]
        data["options"] = [{"id": key, "text": text} for key, text in item["options"]]
        data["answer"] = {"value": item["answer"], "explanation": item["explanation"]}
        data["examPatternRefs"] = [make_ref(url, number, locator)]
        data["solutionStrategy"] = item["strategy"]
        data["solutionSteps"] = item["steps"]
        data["provenance"] = {
            "origin": "original",
            "license": "All rights reserved",
            "sourceUrl": url,
            "sourceLocator": f"{SOURCES[url][0]}公開試題，{locator}；只參照題型，不重製原卷。",
            "authoringNote": "依官方英語課綱與 Knowledge Graph，參照公立學校公開試題的課堂指令、校園詞彙、時間／方位與情境推論能力獨立改寫；未複製原題題幹、選項、資料或答案。題目維持draft，尚待版本研究及完整發布審查。",
        }
        data["reviewStatus"] = "draft"
        data["updatedAt"] = "2026-09-24"
        path.write_text(json.dumps(data, ensure_ascii=False, indent=2) + "\n", encoding="utf-8")

    catalog_path = ROOT / "implementation/reports/public-exam-source-catalog.json"
    catalog = json.loads(catalog_path.read_text(encoding="utf-8"))
    for url, (school, exam, boundary) in SOURCES.items():
        row = {
            "institution": school,
            "url": url,
            "subjects": ["english"],
            "availableMaterial": exam,
            "researchUse": "英語3-Ⅳ-2課堂指令、校園詞彙、時間／方位關係與行程判讀；逐題pattern-only，不複製原卷。",
            "licenseBoundary": boundary,
        }
        old = next((entry for entry in catalog["sources"] if entry.get("url") == url), None)
        if old:
            old.update(row)
        else:
            catalog["sources"].append(row)
    catalog["questionSourceUrls"] = sorted({entry["url"] for entry in catalog["sources"] if entry.get("url")})
    catalog_path.write_text(json.dumps(catalog, ensure_ascii=False, indent=2) + "\n", encoding="utf-8")
    print(json.dumps({"rewritten": len(ITEMS), "remainDraft": True, "sourcePapers": len(SOURCES)}, ensure_ascii=False))


if __name__ == "__main__":
    main()
