#!/usr/bin/env python3
"""Repair Db-IV-8 question quality and attach directly verified public-exam patterns.

The only source used here is Neihu Junior High's publicly available Grade 7
biology exam. Original prompts/options/answers are not reproduced. All target
records must still be drafts; this script does not promote review status.
"""
from __future__ import annotations

import json
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
SOURCE_URL = "https://www.nhjh.tp.edu.tw/uploads/1660183128914WHF2n4Sp.pdf"
SOURCE_TITLE = "臺北市立內湖國中110學年度第二學期七年級第三次生物段考"

ITEMS = {
    1: {
        "item": 40,
        "pattern": "以植物構造的作用解釋水土保持；改寫為樹冠攔雨後水量路徑判讀。",
        "strategy": "把雨水當作有總量的流量帳：先追蹤葉面暫存，再分辨枝幹流、穿透雨、入滲、逕流與蒸散。",
        "explanation": "樹冠截留只改變雨水到達地面的時間與路徑。水可能暫留葉面後蒸發、沿枝幹流下或穿過樹冠；其餘再入滲或形成逕流，因此不能說雨水全變地下水或被根吸光。",
        "steps": [
            "先把題目邊界定為『降到樹冠上的水』，不要把它和整場降雨量混為一談。",
            "在草稿畫出葉面暫存、枝幹流、穿透雨三條離開樹冠的路徑。",
            "再將到達地面的水分成入滲、地表逕流與暫留，另標蒸散離開測量系統。",
            "逐一檢查選項是否把某一條路徑說成唯一去向，或誤稱水量憑空消失。",
            "C 同時承認暫存、重新分配與蒸發；結論只說明可能路徑，不推定各路徑比例。",
        ],
    },
    2: {
        "item": 42,
        "pattern": "以樹蔭和植物環境作用為題型脈絡；改寫為地表溫度比較的測量公平性。",
        "strategy": "先鎖定可比較的表面與測點，再固定量測高度、時段和儀器；日照與風要同步記錄，不能只挑最明顯的差值。",
        "explanation": "A 讓兩處使用相同量測方法，在同一時段與相近天氣比較，並把日照和風納入紀錄。其餘選項混用時點或工具，或只保留極端讀值，無法公平歸因於樹蔭。",
        "steps": [
            "因變項是地表溫度，先確認兩個測點的表面材質相同或足夠相近。",
            "把探頭固定在相同高度與接觸方式，避免一邊測空氣、一邊測地面。",
            "安排樹蔭與對照點同時量測，並記錄日照、風速、雲量及最近降雨。",
            "重複多個成對時段，以中位數或變化範圍比較，不採單一最大溫差。",
            "只有 A 同時維持可比條件並留下天氣資訊，因此它能支持較公平的比較。",
        ],
    },
    3: {
        "item": 39,
        "pattern": "以不同植物覆蓋條件、固定土盆與相同供水比較逕流混濁；改寫為雨後積水的替代原因檢驗。",
        "strategy": "把『積水退得快』拆成入滲、坡度排水和地表逕流三種可能，先列出未控制條件再決定能否下因果結論。",
        "explanation": "積水消退快可能是水進入土壤，也可能由較大坡度、排水孔或不同降雨造成。沒有在相同土壤、地形、降雨和排水條件下比較，不能只把差異歸因於植被。",
        "steps": [
            "把觀察量定義清楚：記錄積水深度隨時間的變化，而非只用『看起來乾了』。",
            "畫出候選機制：土壤入滲、地勢導流、排水設施及地表蒸發都可能讓水面下降。",
            "提出植被與裸地的配對測點，讓土壤類型、面積和微地形盡量一致。",
            "用相同降雨量或等量加水重複測試，同時收集入滲時間與流出水量。",
            "D 把坡度、土壤、降雨與排水納入待驗條件；單次共現不足以證明植物是唯一原因。",
        ],
    },
    4: {
        "item": 42,
        "pattern": "以植物可能調節空氣與溫度的說法為題型脈絡；改寫為多因素造成測值偏高的解釋。",
        "strategy": "不要在『樹有沒有作用』二選一；先辨識植被作用方向，再查排放量、風場和測站位置是否改變淨測值。",
        "explanation": "樹木可能攔截部分粒狀物，但道路排放、風向、街道通風、葉面狀態和測點距離都會影響量測。高讀值既不能證明植物完全無效，也不能只怪樹太少。",
        "steps": [
            "確認儀器量的是哪一類粒狀物，以及『樹多』描述的是冠幅、葉面或植栽數量。",
            "把污染源、樹列、主風向與測站位置畫在同一張平面圖上。",
            "檢查高讀值時段是否恰逢車流增加、逆風、低風速或葉面覆塵。",
            "在道路上風／下風、不同距離及有樹／無樹位置同步重測，排除單點偶然值。",
            "B 保留植物攔截與其他因素相互抵銷的可能，沒有把複雜結果簡化成單一原因。",
        ],
    },
    5: {
        "item": 39,
        "pattern": "用等面積植物盆、相同土壤與給水量測試覆蓋度對出流水混濁的影響；改寫為辨別相關與因果。",
        "strategy": "因果判斷看比較設計，不看兩項指標是否一起變化；找出操弄的覆蓋度、固定條件、結果量測和重複次數。",
        "explanation": "A 描述以配對測點控制材質、日照和風速並重複量測，讓樹蔭成為主要比較差異。B 把共變誤當因果，C 缺少量測，D 則把未控制因素當成不存在。",
        "steps": [
            "先把『有樹較涼』標成觀察到的相關，而非已證實的因果。",
            "列出共同影響樹蔭和溫度的因素，例如地面材質、建築遮蔽、測量時段與風。",
            "選擇條件相近的成對地點，明確把遮蔭狀態當作比較因素。",
            "用同一校正過的儀器反覆量測，記錄每次差值和天氣而不是只留平均值。",
            "A 提供控制和重複比較；即使如此，結論也只支持這些場址與觀測條件。",
        ],
    },
    6: {
        "item": 41,
        "pattern": "以山林開發及保育的取捨為題型脈絡；改寫為樹冠降溫與狹巷通風的多目標方案評估。",
        "strategy": "把降溫和通風列成並行的結果，而非互相抵銷後只報一個分數；比較不同巷寬、樹種和配置的受益與風險。",
        "explanation": "C 同時量測溫度、風速與空氣品質，並考慮街道尺度，能呈現降溫收益和通風副作用。只報降溫或一遇到副作用就全面否定，都忽略了場址差異與可調整配置。",
        "steps": [
            "先確認決策不是『種或不種』的單一選項，而是要選位置、樹種、間距與修剪方式。",
            "為熱環境和通風各訂一項指標，例如行人高度溫度與巷道風速。",
            "挑選不同街寬或冠幅的區段作比較，固定量測高度、時間與天氣背景。",
            "把住戶、行人和沿街店家的受益／受影響位置標上地圖，檢查是否有人承受集中副作用。",
            "C 用多指標及街道尺度評估方案；資料不足時先試行可逆配置，再依監測結果調整。",
        ],
    },
    7: {
        "item": 40,
        "pattern": "要求從植物根系固定土壤與葉片削弱雨滴沖刷等作用解釋水土保持；改寫為選取入滲／逕流資料。",
        "strategy": "選擇能直接描述水走向的量，不用植物長得高或照片顏色代替水文測量；比較時要匹配降雨與地形。",
        "explanation": "入滲時間和逕流量直接呈現水是否進入土壤或流出坡面。相同降雨、坡度和面積下再比較不同根系與覆蓋條件，才較能判斷植物是否改變水流。",
        "steps": [
            "把研究問題改寫成可量測結果：水進入土壤需要多久，以及表面流走多少水。",
            "分別記錄根系密度、地表覆蓋和土壤性質，避免把三種特徵混成一個『植物多寡』。",
            "在同一坡度、面積與土壤來源的樣區施以相同雨量或標準化灑水。",
            "量取入滲所需時間與收集到的逕流水量，並為每種覆蓋條件設重複樣區。",
            "D 直接量到水流結果，且要求條件一致；只看植株高度、照片或不量雨量都答非所問。",
        ],
    },
    8: {
        "item": 42,
        "pattern": "檢視植物降低粒狀物與改善熱環境等說法是否有直接支持；改寫為測站結果的下一步驗證。",
        "strategy": "單次低值只能形成待驗假說；下一步要擴大時空取樣、校正儀器並找出排放源及風向這些混淆因素。",
        "explanation": "樹下測站一次偏低，可能來自風向、交通時段、儀器誤差或局部遮蔽。B 用重複、多位置、多時段並校正儀器的方式，能檢查差異是否穩定，而不是挑最低值外推。",
        "steps": [
            "先把目前資料限定為『某一測點、某一時刻』，不把它直接推成整區空氣改善。",
            "檢查測站零點與校正紀錄，並確認進氣口高度、位置及遮蔽條件一致。",
            "設置樹下、無樹對照與不同距離的測點，避開只選最低讀值的取樣偏差。",
            "跨時段同步記錄風向、車流和天候，觀察樹下差異是否在不同條件仍重現。",
            "B 同時補足空間、時間與儀器證據，之後才可評估能否將結果推廣到其他區域。",
        ],
    },
    9: {
        "item": 41,
        "pattern": "將山林開發和保育放在環境評估框架中思考；改寫為校園植樹配置決策。",
        "strategy": "決策先盤點場址限制，再比較多項環境服務與維護代價；用校園地圖及基準測量決定種在哪裡，而非先選最快長大的樹。",
        "explanation": "A 把水流、熱、空氣品質、根系空間、維護和土地使用一起納入場址評估，避免只追求樹冠或生長速度。植物效益取決於配置與環境條件，需以現地資料驗證。",
        "steps": [
            "在校園平面圖標出地下管線、建築、日照、風廊、人流與現有排水位置。",
            "把預期效益拆成遮蔭降溫、雨水入滲和粒狀物攔截，另列根系、落葉及維護成本。",
            "依每個候選地點的可用土壤體積、巷道寬度和安全視線篩除不適配置。",
            "先建立植樹前的溫度、積水或粒狀物基準值，並規劃植後同點追蹤。",
            "A 讓位置與樹種服從場址和多目標證據；只看生長速度、樹冠大小或口號均不足以決策。",
        ],
    },
    10: {
        "item": 39,
        "pattern": "以植物覆蓋度比較出流水狀態的控制實驗作證據鏈；綜合到植被對水、熱與空氣環境的條件式結論。",
        "strategy": "總結時分開說機制、量測結果和推論範圍；只把原始觀察能支持的部分寫進結論，未測項目明列為待查。",
        "explanation": "C 沒有把植被寫成必然改善所有環境的萬靈丹，而是把作用限定在植物、測點、季節與風雨條件，並要求以同步資料檢驗。單一地點或一次測量不能代表整座城市。",
        "steps": [
            "將結論切成三欄：觀察到的水文變化、可能的熱／空氣機制、尚未量到的項目。",
            "逐項核對每個主張是否有同一場址、同一時段及可追溯的量測資料。",
            "列出會改變結果的條件，包括樹種與冠層、季節、風雨、排放源和地表材料。",
            "標明樣本數、測點覆蓋與重複次數的限制，不以局部結果代替全市估計。",
            "C 以條件式語句保留不確定性，並指出要靠同步、多點資料來檢驗外推。",
        ],
        "additional_items": [
            (40, "以根系固定土壤與葉片削弱雨滴沖刷等植物作用作為水文結論的補充對照。"),
            (42, "以植物對空氣品質與氣溫作用的陳述作為熱／空氣結論的補充對照。"),
        ],
    },
}


def make_ref(item: int, pattern: str) -> dict[str, str]:
    return {
        "url": SOURCE_URL,
        "title": SOURCE_TITLE,
        "year": "110-2",
        "subject": "science",
        "locator": f"紙本第4頁／PDF第4頁，第{item}題",
        "locatorLevel": "item",
        "observedPattern": pattern,
        "reuseDecision": "pattern-only",
        "status": "recorded",
    }


def main() -> int:
    changed = []
    for number, item in ITEMS.items():
        path = ROOT / f"questions/science/question-science-content-db-iv-8-{number}.json"
        data = json.loads(path.read_text(encoding="utf-8"))
        if data.get("reviewStatus") != "draft":
            raise SystemExit(f"Refusing to change non-draft question: {data['id']}")
        if data.get("answer", {}).get("value") not in {o["id"] for o in data.get("options", [])}:
            raise SystemExit(f"Answer key does not match options: {data['id']}")

        data["answer"]["explanation"] = item["explanation"]
        data["solutionStrategy"] = item["strategy"]
        data["solutionSteps"] = item["steps"]
        refs = [ref for ref in data.get("examPatternRefs", []) if ref.get("status") != "pending-item-locator"]
        refs.insert(0, make_ref(item["item"], item["pattern"]))
        for additional, additional_pattern in item.get("additional_items", []):
            refs.append(make_ref(additional, additional_pattern))
        data["examPatternRefs"] = refs
        data["provenance"]["sourceUrl"] = SOURCE_URL
        data["provenance"]["sourceLocator"] = f"臺北市立內湖國中110-2七年級生物，第4頁第{item['item']}題；只借用題型與能力結構。"
        data["provenance"]["authoringNote"] = (
            "題幹、選項、答案、解析與教學步驟均依 Db-Ⅳ-8 獨立原創；"
            "只參考公立學校公開試題的實驗比較、機制解釋或環境評估能力，不重製原卷內容。"
            "本紀錄是首輪 AI 檢查，完整教材、三版本融合、版權及發布審查仍待完成。"
        )
        path.write_text(json.dumps(data, ensure_ascii=False, indent=2) + "\n", encoding="utf-8")
        changed.append(data["id"])

    print(json.dumps({"unitId": "science-content-db-iv-8", "changed": changed, "count": len(changed)}, ensure_ascii=False))
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
