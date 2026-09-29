#!/usr/bin/env python3
"""Replace AA-root false exam provenance with verified public-school exam items."""
from __future__ import annotations

import json
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
QDIR = ROOT / "questions/science"
SOURCES = {
    "kouliao": {"url": "https://www.klm.kh.edu.tw/upload/310/101_83606/114-1-3%E8%87%AA8A.pdf", "title": "高雄市立蚵寮國民中學114學年度第一學期第三次定期評量八年級自然科試題", "year": "114學年度"},
    "bali": {"url": "https://www.pljhs.ntpc.edu.tw/var/file/0/1000/attach/86/pta_4170_158052_68738.pdf", "title": "新北市立八里國民中學110學年度第一學期八年級自然科補考題庫", "year": "110學年度"},
    "jinhe": {"url": "https://www.jhsh.ntpc.edu.tw/var/file/0/1000/attach/77/pta_22725_1030925_35628.pdf", "title": "新北市立錦和高級中學113學年度第二學期國中部八年級自然科補考題庫", "year": "113學年度"},
    "meilun": {"url": "https://www.mljh.hlc.edu.tw/modules/tad_uploader/index.php?cat_sn=240&cfsn=1060&name=112-2-8%E5%B9%B4%E7%B4%9A%E8%87%AA%E7%84%B6%E7%A7%91%E7%AC%AC%E4%B8%80%E6%AC%A1%E6%AE%B5%E8%80%83%E8%A9%A6%E5%8D%B7.pdf&op=dlfile", "title": "花蓮縣立美崙國民中學112學年度第二學期八年級自然科第一次段考評量試卷", "year": "112學年度"},
    "jingxing": {"url": "https://www.chhs.tp.edu.tw/uploads/1595570220266AAUtVeTk.pdf", "title": "臺北市立景興國民中學108學年度第二學期八年級自然科第一次段考", "year": "108學年度"},
    "ziqiang": {"url": "https://www.tcjh.tyc.edu.tw/uploads/1556760247155p1mmNx8J.pdf", "title": "桃園市立自強國民中學107學年度第二學期第一次段考八年級自然與生活科技試卷", "year": "107學年度"},
}

# For each question: (school source key, exact paper item, supported ability).
ITEMS = {
    1: [("kouliao", "PDF第3頁第30題", "由鋰原子結構及質子數判讀元素符號"), ("bali", "PDF第3頁第40題", "依元素表示法判讀原子序、質子數及質量數"), ("jinhe", "PDF第4頁第44題", "辨認原子核與原子內基本粒子" )],
    2: [("kouliao", "PDF第4頁第31至32題", "用粒子數據判斷原子電中性和元素化學性質"), ("bali", "PDF第3頁第43題", "以質子、中子、電子模型判讀原子結構"), ("jinhe", "PDF第4頁第44題", "辨認原子核內與核外粒子的結構關係" )],
    3: [("bali", "PDF第3頁第41題", "解讀係數與化學式下標表示的粒子數和原子數"), ("jinhe", "PDF第5頁第49題", "區分元素符號前係數與分子式下標"), ("meilun", "PDF第4頁填充題第1題", "依分子式下標逐元素計算分子量" )],
    4: [("bali", "PDF第3頁第41題", "判斷3H2O中係數和下標各自代表的數量"), ("jinhe", "PDF第5頁第49題", "比較2N與N2的粒子意義"), ("ziqiang", "試題第4題", "從葡萄糖與硫酸分子式判讀分子組成" )],
    5: [("jingxing", "PDF第2頁第11題", "由化學式計算三氧化二鐵式量並換算物質量"), ("meilun", "PDF第4頁填充題第1題", "依化學式計算水、硫酸及葡萄糖分子量"), ("ziqiang", "試題第4題", "由分子式和原子量計算葡萄糖與硫酸分子量" )],
    6: [("kouliao", "PDF第3頁第26至27題", "判讀同族性質與週期表規律"), ("bali", "PDF第3頁第38題", "比較週期表排列、週期與同族性質"), ("jinhe", "PDF第5頁第45及48題", "判讀週期表方向與同族元素性質" )],
    7: [("kouliao", "PDF第3頁第27題", "分辨週期與族並判讀週期表規律"), ("bali", "PDF第3頁第38題", "判讀週期表橫列、縱行與同族規律"), ("jinhe", "PDF第5頁第45題", "辨識週期表的週期、族與排列規則" )],
    8: [("kouliao", "PDF第4頁第34題", "依粒子模型判讀反應前後原子重新排列"), ("bali", "PDF第3頁第41題", "由水分子式判讀單一粒子的原子組成"), ("jinhe", "PDF第4頁第39題", "依元素種類及固定比例區分元素與化合物" )],
    9: [("kouliao", "PDF第4頁第31至32題", "從質子數、電子數資料辨認粒子種類與電性"), ("bali", "PDF第3頁第43題", "以原子結構示意圖判讀基本粒子"), ("jinhe", "PDF第4頁第44題", "判讀原子核與核外電子結構" )],
    10: [("kouliao", "PDF第3頁第26至27題", "以族、週期與性質規律作有限度推論"), ("bali", "PDF第3頁第38題", "依週期表證據檢核分類主張"), ("jinhe", "PDF第5頁第45及48題", "辨認同族規律並排除超出資料的性質斷言" )],
}

DETAILS = {
    1: ("以質子數／原子序判定元素，再排除不具元素識別力的資料。", "元素的原子序等於質子數；中子數可因同位素不同，電子數可因離子化改變，因此不能以兩者單獨決定元素身分。", ["先辨認題目問的是元素身分，而非粒子的電荷或質量。", "原子序定義為原子核中的質子數，因此是識別元素的依據。", "中子數改變會形成同位素，元素種類仍不變。", "電子數改變會形成離子，原子序也不因此改變。", "所以唯一直接決定元素身分的是 A：原子序（質子數）。"]),
    2: ("分別用質子數判斷元素、用質子與電子差判斷電性。", "11個質子表示原子序11；電子比質子少1個，淨電荷為+1，所以是原子序11的陽離子。", ["先列出粒子內有11個質子與10個電子。", "質子數決定元素身分，故原子序為11。", "每個質子帶一個正電、每個電子帶一個負電。", "正電比負電多一個單位，粒子帶+1電荷，是陽離子。", "符合原子序11且帶正電的是 B。"]),
    3: ("辨認化學式內下標所屬的元素，逐項計算單一粒子的原子數。", "Al₂O₃每個化學式單位含2個鋁原子及3個氧原子；下標不表示樣品內有幾個粒子。", ["先將Al₂O₃按元素符號拆成Al與O兩種元素。", "Al右下標2表示每個化學式單位含2個鋁原子。", "O右下標3表示每個化學式單位含3個氧原子。", "故單一化學式單位中的鋁：氧原子數比為2：3。", "下標描述組成比例，答案選 A。"]),
    4: ("先讀下標確定單一分子，再讀係數確定分子個數。", "CO₂的下標2表示每個分子含2個氧原子；前置係數3表示有3個CO₂分子，不會改變各分子的組成。", ["先看CO₂內部的下標2，得知每個分子有2個氧原子。", "沒有寫出的碳下標視為1，所以每個分子有1個碳原子。", "再看整個化學式前方係數3，它計數的是CO₂分子數。", "因此3CO₂有3個分子、共3個碳與6個氧原子。", "只有 B 正確區分係數與下標。"]),
    5: ("依式量計算規則逐項乘算，再合併各元素貢獻。", "X₂Y含2個X與1個Y，式量為2×23＋16＝62；每個下標都要乘上相對原子質量。", ["先由X₂Y辨認組成：2個X原子、1個Y原子。", "計算X的總貢獻：2×23＝46。", "計算Y的總貢獻：1×16＝16。", "將各元素貢獻相加：46＋16＝62。", "因此X₂Y的相對分子質量為62，選 C。"]),
    6: ("從週期表同族規律推測相似處，同時保留個別差異。", "同族元素的最外層電子排列呈相似規律，因此部分化學性質可能接近；這不代表原子序、物理性質或所有反應完全相同。", ["先確認題幹只給出兩元素位於同一族。", "同一族元素的價電子排列有相似規律。", "價電子關係可支持部分化學性質相似的推測。", "但同族元素仍有不同原子序、週期及物理性質。", "因此使用『可能相近』而非『完全相同』的 B 最恰當。"]),
    7: ("利用週期指出電子層數，並分清族位置與其他性質。", "元素位於第3週期，表示其原子有三層電子分布；第17族提供另一個位置資訊，不能推出質量或名稱字數。", ["題目給出第3週期與第17族兩項位置資訊。", "週期號對應原子的電子層數，因此第3週期對應三層。", "族號與最外層電子及化學性質規律相關，不代表質量。", "樣品質量和元素名稱字數都不是週期表位置的證據。", "支持第3週期位置的敘述為 A。"]),
    8: ("在粒子模型中檢查單一粒子是否含兩種以上元素。", "模型約定不同顏色代表不同元素；B的每個粒子都有紅球與白球兩種原子，符合化合物的組成特徵。", ["先依題目圖例確認不同顏色代表不同元素。", "判斷元素或化合物要看單一粒子的組成，不只數整份樣品的顏色。", "B的每個粒子都由紅、白兩種球連結。", "因此B呈現不同元素以固定比例組成的粒子；其餘只含一種球色。", "符合化合物模型的是 B。"]),
    9: ("先比質子數確認是否同元素，再比電子數判定電荷。", "兩粒子都有8個質子，故同為原子序8的氧；8電子者為中性原子，10電子者多2個負電，為2−陰離子。", ["逐一抄出兩粒子的質子數：兩者都是8。", "質子數相同表示元素相同，原子序均為8。", "中性氧原子有8個電子；另一粒子有10個電子。", "後者比質子多2個電子，帶2−電荷，兩者電性不同。", "所以C正確：同一元素的不同電性粒子。"]),
    10: ("把週期表當作可檢驗的預測線索，結論強度不得超過證據。", "同族位置可支持相似化學性質的初步預測；新元素的具體反應與物理性質仍須取得測量資料，未測項目應明確保留為未知。", ["先把主張拆成已知資料與尚未測得的性質。", "週期表位置可提供分類與性質趨勢的初步預測。", "設計能區分假設的實驗或蒐集可靠測量資料。", "比較預測與觀察，並標註目前證據不能回答的部分。", "B同時保留預測、驗證與未知邊界，最符合科學證據原則。"]),
}


def ref(source_key: str, locator: str, skill: str) -> dict[str, str]:
    source = SOURCES[source_key]
    observed = f"原卷{locator}考查：{skill}。本題僅採其能力結構，題幹、數值、選項與解析均另行撰寫。"
    return {"url": source["url"], "title": source["title"], "year": source["year"], "subject": "science", "locator": locator, "locatorLevel": "item", "pattern": observed, "observedPattern": observed, "reuseDecision": "pattern-only", "status": "recorded"}


def main() -> None:
    for n in range(1, 11):
        path = QDIR / f"question-science-content-aa-{n}.json"
        data = json.loads(path.read_text(encoding="utf-8"))
        data["examPatternRefs"] = [ref(*row) for row in ITEMS[n]]
        data["solutionStrategy"], explanation, steps = DETAILS[n]
        data["answer"]["explanation"] = explanation + f" 正確答案：{data['answer']['value']}。"
        data["solutionSteps"] = steps
        data["provenance"]["sourceUrl"] = ITEMS[n] and SOURCES[ITEMS[n][0][0]]["url"]
        data["provenance"]["sourceLocator"] = "；".join(f"{SOURCES[k]['title']}：{loc}（{skill}）" for k, loc, skill in ITEMS[n]) + "；僅供 pattern-only 原創改寫。"
        data["provenance"]["authoringNote"] = "依三所公立學校原卷的題目能力方向獨立改寫；未複製題幹、圖示、選項或答案。答案與五步推理已逐項核對；全庫第二輪內容／版權審查仍未完成。"
        data["updatedAt"] = "2026-09-24"
        path.write_text(json.dumps(data, ensure_ascii=False, indent=2) + "\n", encoding="utf-8")

    catalog_path = ROOT / "implementation/reports/public-exam-source-catalog.json"
    catalog = json.loads(catalog_path.read_text(encoding="utf-8"))
    catalog.setdefault("questionSourceUrls", [])
    catalog.setdefault("sources", [])
    for source in SOURCES.values():
        if source["url"] not in catalog["questionSourceUrls"]:
            catalog["questionSourceUrls"].append(source["url"])
        if not any(row.get("url") == source["url"] for row in catalog["sources"]):
            catalog["sources"].append({"institution": source["title"].split(source["year"])[0].strip(), "url": source["url"], "subjects": ["science"], "availableMaterial": source["title"], "researchUse": "逐題核對原子結構、離子、化學式、相對分子質量與週期表能力；僅作 pattern-only 原創改寫。", "licenseBoundary": "公開查閱不代表可重製；不複製原題、原選項、原圖表或答案。"})
    catalog["updatedAt"] = "2026-09-24"
    catalog_path.write_text(json.dumps(catalog, ensure_ascii=False, indent=2) + "\n", encoding="utf-8")


if __name__ == "__main__":
    main()
