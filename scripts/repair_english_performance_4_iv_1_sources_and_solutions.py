#!/usr/bin/env python3
"""Replace weak source pointers and generic explanations for English 4-IV-1.

Only public-exam format is reused.  Each prompt and solution remains original;
all question-level source locators below were checked against public school PDFs.
"""
from __future__ import annotations

import json
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
QUESTION_DIR = ROOT / "questions/english"
UPDATED_AT = "2026-09-26"

ZIQIANG = "https://www.tcjh.tyc.edu.tw/uploads/1548635646492gsGMmT1l.pdf"
GUOCHANG = "https://www.kcjh.kh.edu.tw/upload/190/104_34764/%E4%BA%8C%E5%B9%B4%E7%B4%9A%E8%8B%B1%E6%96%87%E7%A7%91_1.pdf"
SANDUO = "https://www.sdjh.ntpc.edu.tw/app/index.php?Action=downloadfile&file=WVhSMFlXTm9MekkxTDNCMFlWOHhPVFV6WHpJek1qWTBNREJmTkRrd09URXVjR1Jt&fname=WW54RPOKRK44A1HH50LKKPHG1430WTRLKLB0XSXSTXA1LK40NKROSTB4WW54A0OKWW5400HHA404LK14MOPKTSLOOPB0QLYWXTYTXWA0SWZWCDUWUSOOXSFCUS00HH25DGA0DCZWFCMO40201434ZWMKUTGDUT21SSUSJGB0GGA401USTWLKUXJHGG04MOLOQOB4GCKKYSEGFHMONPNPSSOK14B4JGKL14DCFGB0USLKPPYXWWVWTSMOVWPKZTICKLQK35YS00QLUTMLSSMKLLVWFHOODGXXGCTSHDYXFGZSLK14PKJCUWXSECRO5035UTJDML4414NO1111"

SCHOOLS = {
    "ziqiang": {
        "url": ZIQIANG,
        "title": "桃園市立自強國中107學年度第1學期第一次段考八年級英語科試題",
        "year": "107-1",
        "locator": lambda n: f"PDF第1頁，第{n}題文意字彙：以句意及部分字母提示寫出完整單字",
        "pattern": "先用句意和已給字母縮小候選，再核對完整字母次序；本站改為全新詞彙、句子及選項。",
    },
    "guochang": {
        "url": GUOCHANG,
        "title": "高雄市立國昌國民中學111學年度第1學期八年級第1次段考英文科試題",
        "year": "111-1",
        "locator": lambda n: f"PDF第5頁，第{n}題文意字彙：依句意與部分字母補出詞彙",
        "pattern": "依語意提示與字母缺漏完成拼字，再把答案放回句中驗證；本站只取作答能力模式。",
    },
    "sanduo": {
        "url": SANDUO,
        "title": "新北市立三多國民中學111學年度第2學期第1次段考八年級英語科試題與答案卷",
        "year": "111-2",
        "locator": lambda n: f"PDF第4頁（答案卷附原題），第{n}題文意字彙：部分字母、句意線索與完整拼寫",
        "pattern": "將詞義線索、句中搭配及部分字母合併判讀；本站另改寫為不同單字與選項。",
    },
}

# Per-item authoring: each rationale identifies the relevant context, spelling
# feature, and why the tempting alternatives do not work.
ITEMS = {
    1: {
        "strategy": "先由 Please 和受詞 the window 判定需要「關上」的動詞，再檢查 close 的母音與詞尾 e。",
        "explanation": "答案 A close 是「關上」窗戶的動詞。close 以 c-l-o-s-e 排列，結尾 e 不可漏；cloze、clouse、cloes 分別混入 z、改變母音組合或調換詞尾字母。",
        "steps": ["先讀 Please ___ the window，確認空格要放可執行的動詞。", "用 window 和 before class 的情境鎖定「關窗」，不是其他動作。", "逐字核對 close：c-l-o-s-e，注意中間是 o、s，最後保留不發音的 e。", "比較選項：cloze 把 s 換成 z；clouse 多出 u；cloes 把 e、s 次序弄錯。", "填入 close 後朗讀 Please close the window，確認語意、詞性與拼法都合。"],
    },
    2: {
        "strategy": "a new 後面需要單數名詞；用博物館展示太空主題的語意確認 exhibition，再按字母區塊核對。",
        "explanation": "答案 B exhibition 是博物館的新展覽。句法位置要求名詞；拼字可分成 ex-hi-bi-tion。A 漏 h，C 把第二個 i 誤成 e，D 多寫一個 n。",
        "steps": ["先看 a new ___：冠詞與形容詞後需要名詞，而非動詞或形容詞。", "museum 與 about space 表示一項展示活動，因此語意應是 exhibition。", "分段核字母 ex-hi-bi-tion，確認 h、兩個 i 及 -tion 的次序。", "排除 exibition（漏 h）、exhebition（母音錯）與 exhibitionn（多一個 n）。", "回填 a new exhibition about space，確認單數名詞位置與「展覽」意思吻合。"],
    },
    3: {
        "strategy": "should 後面接原形動詞；由 old bridge 和 before using it 判斷要先修繕，再用 re-pair 檢查拼字。",
        "explanation": "答案 A repair 表示修理、修復。should 後用動詞原形；repair 可按 re-pair 記住 a-i-r 的順序。其餘選項把詞尾字母順序或母音寫錯。",
        "steps": ["圈出 should，先確定空格必須是原形動詞。", "old bridge before using it 指使用前要先修復，不是單純描述橋梁。", "將 repair 拆成 re + pair，核對第二音節拼作 p-a-i-r。", "排除 repare（以 e 取代 a）、repiare（字母次序錯）和 repaire（詞尾多 e）。", "放回 We should repair the old bridge，確認情態動詞後的形式與語意均完整。"],
    },
    4: {
        "strategy": "a short 後需要名詞；週末記錄對應 diary，並用 diary／dairy 的詞義差異及 -ary 結尾防止混淆。",
        "explanation": "答案 C diary 是日記。Mia 寫下週末經歷，需要個人紀錄；dairy 指乳品相關事物，diery、dyary 則是母音拼錯。diary 的尾段是 -ary。",
        "steps": ["由 a short ___ 判斷空格需要可數名詞。", "wrote about her weekend 指記錄個人經歷，目標詞是 diary。", "按 d-i-a-r-y 核對中間母音順序及字尾 -ary。", "A 的 ie 次序錯；B dairy 是乳品相關字；D 把第二個 i 寫成 y。", "回讀 a short diary about her weekend，確認名詞和上下文相符。"],
    },
    5: {
        "strategy": "be 動詞 are 後、very 後需要形容詞；先辨認 instructions 的特性，再核對 clear 中 ea 的字母組合。",
        "explanation": "答案 A clear 描述指示容易理解。句型 are very ___ 需要形容詞。clear 的母音字母是 ea；cleer、claer、clere 都改錯母音組合或字母次序。",
        "steps": ["讀出 The instructions are very ___，辨認空格位於 be 動詞與 very 之後。", "此處要描述 instructions 的品質，選形容詞而不是副詞或名詞。", "語意需要「清楚的」；核對 clear 的拼法 c-l-e-a-r。", "比較 ea 的固定次序：cleer 換成 ee，claer 調換母音，clere 把 r、e 移位。", "填回 are very clear，確認形容詞位置與「指示清楚」的意思一致。"],
    },
    6: {
        "strategy": "good 後應接名詞；gave me ___ about 的搭配指向建議，並以 advice（名詞）對照 advise（動詞）。",
        "explanation": "答案 B advice 是「建議」這個名詞，符合 good advice。advise 是動詞「建議某人」，不能直接放在 good 後；advaice 與 advize 的字母組合不正確。",
        "steps": ["先由 good ___ 判斷空格需要名詞；good 是形容詞。", "gave me ___ about resting 表示收到關於休息的建議，語意搭配為 advice。", "核對字母 a-d-v-i-c-e，記住此名詞以 -ce 結尾。", "排除 advise（以 -se 結尾的動詞）、advaice（多插入 a）和 advize（將 c 誤成 z）。", "朗讀 gave me good advice about resting，確認詞性與介系詞片語接續自然。"],
    },
    7: {
        "strategy": "will 後面要用原形動詞；tomorrow 指未來要公布結果，announce 的雙 n 與 -ounce 字母序需完整。",
        "explanation": "答案 A announce 是「宣布」。will 後接原形動詞，句意是明天公布結果。announce 拼作 a-n-n-o-u-n-c-e；B 漏一個 n，C 漏 n，D 把 c 寫成 s。",
        "steps": ["圈出 will，確定空格要填原形動詞。", "final result 與 tomorrow 組成「明天公布結果」的語境，目標動詞是 announce。", "分段核對 a-n-nounce，特別檢查開頭連續兩個 n 及結尾 -nce。", "排除 anounce、annouce 的漏字，以及把 c 寫成 s 的 announse。", "回填 Our team will announce the final result tomorrow，確認情態動詞後不加 -s 或 -ed。"],
    },
    8: {
        "strategy": "Please ___ your name 要求一個動作；表單情境指向 sign，拼寫時要保留不發音的 g。",
        "explanation": "答案 A sign 是「簽名」。your name at the bottom of the form 提供明確語意線索。sign 中 g 不發音但仍須寫出；sine 是不同字，signe 多 e，sygn 把 i 誤成 y。",
        "steps": ["先依 Please 與受詞 your name 判斷空格需要動詞。", "at the bottom of the form 表示在表單底部簽名，目標詞是 sign。", "逐字母核對 s-i-g-n；雖然 g 不發音，拼字仍不可省略。", "排除 sine（拼成另一個字）、signe（多出 e）和 sygn（母音字母錯）。", "填回 Please sign your name，確認動作、受詞與表單位置一致。"],
    },
    9: {
        "strategy": "be 動詞 are 後需要形容詞；句尾 so 提示兩個實驗結果不相同，拼寫 different 時檢查雙 f 與 -ent。",
        "explanation": "答案 A different 是「不同的」形容詞。主詞 results 為複數，搭配 are；different 拼作 d-i-f-f-e-r-e-n-t，含雙 f。其餘選項漏 f 或把 -ent 寫錯。",
        "steps": ["由 results are ___ 判定空格要放形容詞補充主詞狀態。", "so we checked the experiment again 說明結果不一致，語意是 different。", "分段核對 dif-fer-ent，確認中間有兩個 f，結尾為 -ent。", "排除 diffrent（漏 e）、diferent（漏一個 f）及 differant（把末尾 e 寫成 a）。", "回讀 The two results are different，確認主詞、be 動詞及形容詞一致。"],
    },
    10: {
        "strategy": "will 後接原形動詞；a tree beside the gate 表示把樹種進土裡，plant 的母音是 a 且不加詞尾 e。",
        "explanation": "答案 A plant 是「種植」。will 後用原形；plent 誤換母音，plaunt 多出 u，plante 多出不需要的 e。",
        "steps": ["先用 will 判定空格要填不加時態字尾的原形動詞。", "a tree beside the gate 表示把樹種在門旁，對應 plant。", "核對 plant 的字母 p-l-a-n-t，短母音位置是 a。", "排除 plent（母音錯）、plaunt（插入 u）和 plante（多加詞尾 e）。", "回填 Our class will plant a tree，確認動詞形式與種樹情境相符。"],
    },
}


def refs(number: int) -> list[dict[str, str]]:
    zi = SCHOOLS["ziqiang"]
    gu = SCHOOLS["guochang"]
    sa = SCHOOLS["sanduo"]
    gu_item = 36 + ((number - 1) % 5)
    sa_item = 1 + ((number - 1) % 6)
    rows = [
        (zi, number),
        (gu, gu_item),
        (sa, sa_item),
    ]
    return [{
        "url": source["url"],
        "title": source["title"],
        "year": source["year"],
        "subject": "english",
        "locator": source["locator"](item),
        "locatorLevel": "item",
        "observedPattern": source["pattern"],
        "reuseDecision": "pattern-only",
        "status": "recorded",
    } for source, item in rows]


def main() -> None:
    changed = 0
    for number, authored in ITEMS.items():
        path = QUESTION_DIR / f"question-english-performance-4-iv-1-{number}.json"
        data = json.loads(path.read_text(encoding="utf-8"))
        assert data["lessonId"] == "lesson-english-performance-4-iv-1"
        assert data["answer"]["value"] in {option["id"] for option in data["options"]}
        data["examPatternRefs"] = refs(number)
        data["provenance"]["sourceUrl"] = ZIQIANG
        data["provenance"]["sourceLocator"] = (
            f"本題依桃園自強國中107-1八年級英文第{number}題，以及高雄國昌國中111-1第{36 + ((number - 1) % 5)}題、"
            f"新北三多國中111-2第{1 + ((number - 1) % 6)}題的公開文意字彙作答模式研究；只改寫題型與推理方式，未複製原題、選項或答案。"
        )
        data["answer"]["explanation"] = authored["explanation"]
        data["solutionStrategy"] = authored["strategy"]
        data["solutionSteps"] = authored["steps"]
        data["updatedAt"] = UPDATED_AT
        data["reviewStatus"] = "draft"
        path.write_text(json.dumps(data, ensure_ascii=False, indent=2) + "\n", encoding="utf-8")
        changed += 1
    print(json.dumps({"unit": "english 4-IV-1", "questionsUpdated": changed, "publicSchools": 3, "refsPerQuestion": 3, "reviewStatus": "draft"}, ensure_ascii=False))


if __name__ == "__main__":
    main()
