#!/usr/bin/env python3
"""Rewrite clearly mismatched science questions with unit-specific original items."""
from __future__ import annotations

import json
import re
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]

def rotate_options(correct: str, distractors: list[str], index: int):
    texts = [correct] + distractors
    shift = index % 4
    texts = texts[shift:] + texts[:shift]
    ids = ["A", "B", "C", "D"]
    correct_id = ids[texts.index(correct)]
    return [{"id": i, "text": t} for i, t in zip(ids, texts)], correct_id

def build(title: str, index: int):
    # Every branch returns a fresh prompt and a single defensible answer.
    if "介質性質與聲音傳播速率" in title:
        medium = ["空氣", "水", "鋼鐵"][index % 3]
        prompt = f"比較聲音在空氣、水與鋼鐵中的傳播速度；若其他條件相近，研究「{title}」時，哪項判斷最合理？"
        correct = "通常在鋼鐵中最快，在空氣中最慢"
        distract = ["三種介質速度完全相同", "通常在空氣中最快，在鋼鐵中最慢", "聲音只能在真空中傳播"]
        explanation = "聲音需要介質傳遞，介質的彈性與粒子排列會影響速度；一般固體最快、氣體最慢。"
        strategy = "先辨認比較的介質，再把聲音傳播需要介質與速度差異的條件套入選項。"
    elif "光速與影響因素" in title:
        prompt = f"光從真空進入空氣與玻璃時，研究「{title}」的光速變化，哪項敘述正確？"
        correct = "光在真空中最快，進入玻璃後速度降低"
        distract = ["光在所有介質中速度都相同", "光進入玻璃後一定比真空快", "光只在水中才能傳播"]
        explanation = "光在真空中的速度最大，進入透明介質後通常變慢；介質性質會影響光速。"
        strategy = "先比較真空與介質，再依光速受介質影響的物理關係排除相反敘述。"
    elif "橫波與縱波" in title:
        prompt = f"繩上的波使繩段上下振動、波形向右傳播；研究「{title}」時，這屬於哪一類波？"
        correct = "橫波，介質振動方向垂直於傳播方向"
        distract = ["縱波，介質振動方向平行於傳播方向", "靜止現象，沒有能量傳遞", "只有聲音才可能是橫波"]
        explanation = "繩段上下振動而波向右傳播，兩個方向互相垂直，因此是橫波。"
        strategy = "把介質振動方向與波的傳播方向分開標示，再以平行或垂直判斷波型。"
    elif title == "Ka：波動、光及聲音":
        prompt = f"研究「{title}」時，一列波在 4 秒內完成 12 次振動；若波長為 0.5 公尺，波速為何？"
        correct = "1.5 公尺／秒"
        distract = ["3 公尺／秒", "6 公尺／秒", "24 公尺／秒"]
        explanation = "頻率為 12÷4＝3 Hz，波速 v＝fλ＝3×0.5＝1.5 公尺／秒。"
        strategy = "先由振動次數除以時間求頻率，再使用波速等於頻率乘波長。"
    elif "波峰、波谷、波長、頻率、波速與振幅" in title:
        prompt = f"一列波的頻率為 5 Hz、波長為 2 公尺；研究「{title}」時，波速是多少？"
        correct = "10 公尺／秒"
        distract = ["2.5 公尺／秒", "7 公尺／秒", "25 公尺／秒"]
        explanation = "使用 v＝fλ，代入 5×2，得到波速 10 公尺／秒；振幅不影響這個基本計算。"
        strategy = "先找出頻率與波長，再寫出 v＝fλ 並檢查答案單位。"
    elif "三稜鏡分光" in title:
        prompt = f"白光通過三稜鏡後分成多種色光；研究「{title}」時，這個現象最能說明什麼？"
        correct = "不同色光在介質中的折射程度不同"
        distract = ["白光只由一種顏色組成", "三稜鏡把光能完全消失", "所有色光折射角永遠相同"]
        explanation = "三稜鏡使不同波長的色光產生不同程度的折射，因而分散成色帶。"
        strategy = "先辨認觀察到的分光結果，再把色光差異連到折射程度，而非把分光當成吸收。"
    elif "音調、響度、音色與超聲波" in title:
        prompt = f"兩個音源的響度相近，但甲的振動頻率高於乙；研究「{title}」時，哪項比較正確？"
        correct = "甲的音調較高"
        distract = ["甲的音調較低", "甲一定比較大聲且音色相同", "頻率只影響音量，不影響音調"]
        explanation = "音調主要由頻率決定；頻率越高，音調越高，響度則主要與振幅相關。"
        strategy = "先把頻率、振幅與音色分開，再只用題幹給的頻率條件判斷音調。"
    elif "光合作用製造養分並釋氧" in title:
        prompt = f"在有光、適量水分與二氧化碳的條件下，研究「{title}」時，綠色植物最主要產生哪一組結果？"
        correct = "製造有機養分，並釋放氧氣"
        distract = ["消耗氧氣並製造二氧化碳", "只吸收礦物質而不形成養分", "把光能直接轉成聲音"]
        explanation = "光合作用利用光能將二氧化碳和水合成有機養分，並釋放氧氣。"
        strategy = "先列出光合作用的反應物與產物，再檢查選項的氣體方向和能量形式。"
    elif "影響光合作用的因素與探究" in title:
        factor = ["光照強度", "二氧化碳濃度", "供水量"][index % 3]
        prompt = f"若要研究「{title}」中的{factor}是否影響光合作用速率，哪種設計最公平？"
        correct = f"只改變{factor}，其餘條件保持相同並量測相同時間的產氧量"
        distract = ["同時改變光照、溫度與水量", "只觀察一片葉子一次就下結論", "改變{factor}但每組使用不同植物種類"]
        explanation = "探究單一因素時要控制其他變因，並用可量測、可比較且可重複的指標判斷影響。"
        strategy = "先指定自變因與應變因，再列出必須控制的條件與重複測量方式。"
    elif "光合作用與呼吸作用的能量轉換" in title:
        prompt = f"研究「{title}」時，哪項敘述正確描述兩種作用的能量方向？"
        correct = "光合作用儲存能量，呼吸作用分解養分並釋放可用能量"
        distract = ["兩者都只把能量轉成光", "呼吸作用製造葡萄糖並儲存全部能量", "光合作用只消耗氧氣而不需光能"]
        explanation = "光合作用把光能轉成有機物中的化學能；呼吸作用分解有機物，釋放細胞可利用的能量。"
        strategy = "先分辨反應物、產物與能量方向，再比較儲存和釋放兩個功能。"
    elif "波浪、海流與潮汐" in title:
        prompt = f"月球引力造成海水週期性升降；研究「{title}」時，這種海面週期變化稱為什麼？"
        correct = "潮汐"
        distract = ["海流", "波浪的折射", "地震波"]
        explanation = "潮汐是海水面受到月球等天體引力及地球運動影響而呈現的週期性升降。"
        strategy = "先抓住週期性升降與月球引力兩個證據，再和風浪或長距離海水流動區分。"
    elif "聲波反射的測量與傳播用途" in title:
        prompt = f"蝙蝠利用發出的聲音遇到障礙物後返回來辨認距離；研究「{title}」時，這是聲音的哪種現象？"
        correct = "回聲，屬於聲波反射"
        distract = ["光合作用", "聲音被完全吸收", "電磁波折射"]
        explanation = "聲音遇到障礙物反射回來形成回聲，可利用回聲的時間差估算距離。"
        strategy = "先辨認聲音往返的證據，再以反射和時間差判斷用途。"
    elif "光的反射與折射規律" in title:
        prompt = f"光由空氣斜射進入玻璃；研究「{title}」時，哪項現象最合理？"
        correct = "光的傳播方向改變，且在玻璃中的速度通常較慢"
        distract = ["光一定沿原方向且速度變快", "光進入玻璃後完全消失", "光只能在真空中折射"]
        explanation = "斜向進入不同介質會發生折射，光速改變並使傳播方向偏折。"
        strategy = "先確認介質是否改變及入射是否斜向，再同時檢查方向與速度的變化。"
    elif "聲音特性研究與噪音防治" in title:
        prompt = f"研究「{title}」時，若要降低教室長時間噪音對聽力的影響，哪項作法較適當？"
        correct = "降低音源音量、縮短暴露時間並使用隔音或吸音措施"
        distract = ["把音量調到最大以蓋過噪音", "只測一次就宣稱沒有風險", "讓所有人靠近音箱聆聽"]
        explanation = "噪音風險與音量、暴露時間和距離有關，降低音量、縮短時間與隔音可降低危害。"
        strategy = "先找出噪音的暴露條件，再用降低強度、時間與傳播的方式評估防治方案。"
    elif "大氣壓力由空氣重量造成" in title:
        prompt = f"研究「{title}」時，登山高度增加後通常觀察到哪項變化？"
        correct = "上方空氣柱變短，所測大氣壓力通常降低"
        distract = ["空氣柱變長且壓力一定升高", "大氣壓力與上方空氣重量無關", "高度改變只會改變水的密度"]
        explanation = "大氣壓力來自上方空氣的重量；高度越高，上方空氣柱通常越短，因此壓力降低。"
        strategy = "先連結壓力來源與上方空氣重量，再比較高度改變後空氣柱的差異。"
    elif "壓力與帕斯卡原理" in title:
        prompt = f"液壓裝置的小活塞面積為 2 cm²，大活塞面積為 20 cm²；研究「{title}」時，小活塞施加 30 N，理想狀態下大活塞可產生多大力？"
        correct = "300 N"
        distract = ["3 N", "30 N", "600 N"]
        explanation = "帕斯卡原理使壓力傳遞相同，F大／20＝30／2，因此 F大＝300 N。"
        strategy = "先把兩活塞的壓力相等列式，再用面積比換算力並檢查單位。"
    elif "定溫定量氣體的壓力與體積關係" in title:
        prompt = f"固定溫度與氣體量時，若容器體積由 6 L 壓縮成 3 L；研究「{title}」時，壓力如何變化？"
        correct = "壓力約變為原來的 2 倍"
        distract = ["壓力約變為原來的一半", "壓力保持不變", "壓力變為原來的 4 倍"]
        explanation = "定溫定量下壓力與體積成反比，體積減半時壓力約加倍。"
        strategy = "先確認溫度與氣體量固定，再用壓力乘體積近似不變判斷倍數。"
    elif "功率" in title:
        prompt = f"某馬達在 6 秒內做功 120 J；研究「{title}」時，平均功率為何？"
        correct = "20 W"
        distract = ["0.05 W", "114 W", "720 W"]
        explanation = "功率 P＝功／時間＝120÷6＝20 W，表示每秒平均完成 20 焦耳的功。"
        strategy = "先辨認功與時間，再用 P＝W/t 計算並確認功率單位是瓦特。"
    elif "能量的形式與轉換" in title or title in ("能量與能源", "INa-Ⅳ-1：能量具有多種形式"):
        prompt = f"電池使手電筒發光；研究「{title}」時，主要的能量轉換順序為何？"
        correct = "化學能轉成電能，再轉成光能與熱能"
        distract = ["光能直接變成化學能且沒有其他形式", "聲能轉成質量", "熱能消失而不發生轉換"]
        explanation = "電池先以化學能提供電能，燈具再把部分電能轉成光能，同時常伴隨熱能。"
        strategy = "依裝置的輸入、傳遞與輸出順序排列能量形式，再檢查是否誤寫成能量消失。"
    elif "生態系中能量的流動" in title or "生態系角色促成能量流轉" in title:
        prompt = f"研究「{title}」時，草→蝗蟲→青蛙的食物鏈中，能量流動的方向為何？"
        correct = "由草經蝗蟲流向青蛙，逐層傳遞且部分以熱散失"
        distract = ["由青蛙流回草且能量全部循環", "能量只在蝗蟲體內停留", "能量由分解者產生並無需來源"]
        explanation = "能量從生產者進入消費者，沿食物鏈單向傳遞；各層代謝也會散失部分熱能。"
        strategy = "先找出食物鏈中的生產者與消費者，再沿取食方向追蹤能量並加入散失限制。"
    elif "能量可相互轉換並維持定值" in title or "能量形式、轉換與守恆" in title:
        prompt = f"摩擦使運動中的物體逐漸停止；研究「{title}」時，最合理的能量解釋是什麼？"
        correct = "機械能主要轉換成內能，總能量仍守恆"
        distract = ["能量完全消失", "摩擦把能量創造成質量而無熱", "只有速度改變，能量形式不變"]
        explanation = "摩擦把部分機械能轉成物體與環境的內能；能量形式改變，但總量不憑空消失。"
        strategy = "先辨認初始與最後的能量形式，再檢查轉換方向和守恆條件。"
    elif "生物體內的能量與代謝" in title or "呼吸作用釋放能量" in title:
        prompt = f"細胞分解葡萄糖以維持活動；研究「{title}」時，這個過程主要作用為何？"
        correct = "將有機物中的化學能釋放，供細胞進行生命活動"
        distract = ["把能量全部變成光", "只製造氧氣而不釋放能量", "讓物質不經反應就增加能量"]
        explanation = "細胞呼吸分解有機物，釋放可供細胞使用的能量，並常伴隨二氧化碳與水生成。"
        strategy = "先辨認反應物與細胞需求，再把有機物分解和可用能量釋放連起來。"
    elif "力作功與能量改變" in title:
        prompt = f"水平力推箱子使箱子沿力的方向移動；研究「{title}」時，哪項判斷正確？"
        correct = "力對物體作功，物體的能量狀態可能改變"
        distract = ["只要有力就一定沒有位移", "力與位移垂直時作功最大", "作功代表能量完全消失"]
        explanation = "力在位移方向有分量時會對物體作功，造成能量轉移或改變；作功不是能量消失。"
        strategy = "先比較力與位移的方向，再判斷是否有能量轉移及其意義。"
    elif "太陽" in title:
        prompt = f"研究「{title}」時，地球上多數天氣與生態系能量的根本來源為何？"
        correct = "太陽輻射能"
        distract = ["月球自行產生的熱能", "地震釋放的所有能量", "海水不需來源即可產生能量"]
        explanation = "太陽輻射為大氣運動、水循環與多數生態系的主要外部能量來源。"
        strategy = "先找出地球系統的外部輸入，再區分根本能源與系統內部的轉換形式。"
    elif "地球的歷史" in title or "岩性與化石記錄地球歷史" in title:
        prompt = f"研究「{title}」時，若在不同地層找到化石，哪項方法較能建立相對年代？"
        correct = "比較地層上下關係與化石特徵，並保留產地與層位記錄"
        distract = ["只以化石大小判定年代", "把所有地層視為同一時間形成", "只依顏色深淺直接排序"]
        explanation = "地層關係與化石特徵可提供相對年代線索，必須結合層位與來源記錄，不能只看外觀。"
        strategy = "先定位資料的層位與化石證據，再區分可支持的相對年代和不能直接推出的絕對年代。"
    elif "地球自轉與高低氣壓旋轉" in title:
        prompt = f"北半球一個低氣壓系統的近地面風向呈逆時針向中心旋入；研究「{title}」時，哪項解釋較合理？"
        correct = "氣壓梯度力把空氣拉向低壓，地球自轉造成偏向"
        distract = ["低壓中心把空氣向外推出且沒有偏向", "只有月球引力造成風向", "風向與氣壓差及地球自轉無關"]
        explanation = "氣壓差促使空氣由高壓往低壓移動，地球自轉造成科氏偏向，使北半球低壓呈逆時針旋入。"
        strategy = "先辨認氣壓梯度的基本方向，再加入半球與自轉偏向判斷旋轉方向。"
    elif "地球與太空" in title:
        prompt = f"研究「{title}」時，北半球夏季較炎熱的主要原因為何？"
        correct = "地軸傾斜使北半球日照角度較大且白晝較長"
        distract = ["地球夏季一定離太陽最近", "月球在夏季停止公轉", "地球自轉速度變成零"]
        explanation = "季節主要由地軸傾斜與公轉造成；夏季日照較直接、白晝較長，單靠日地距離不能解釋。"
        strategy = "先辨認季節的時間與半球，再用地軸傾斜、日照角度和白晝長度建立因果。"
    elif "能源開發的風險評估與決策" in title:
        prompt = f"研究「{title}」時，若比較兩個能源方案，哪種資料組合最適合支持決策？"
        correct = "同時比較供能量、成本、環境影響、事故風險與受影響族群"
        distract = ["只比較短期發電量", "只採用支持其中一方案的單一數據", "忽略安全與環境代價只看價格"]
        explanation = "能源決策涉及多重指標與不同群體，必須把效益、成本、風險與分配影響一起比較。"
        strategy = "先列出決策指標與利害關係人，再比較證據範圍和方案取捨，避免單一數字決定結論。"
    else:
        return None
    distractors = [d.format(**locals()) for d in distract]
    return prompt, correct, distractors, explanation, strategy

def main():
    titles = {}
    for p in (ROOT / "lessons" / "science").glob("*.json"):
        data = json.loads(p.read_text(encoding="utf-8"))
        titles[data.get("id")] = data.get("title", "")
    changed = []
    rules = {
        "reflection": re.compile(r"反射角為何"),
        "density": re.compile(r"其密度為何"),
        "speed": re.compile(r"平均速率為何"),
        "rain": re.compile(r"迎風坡年雨量"),
    }
    allowed = {
        "reflection": re.compile(r"反射|光學原理|光的|物體顏色"),
        "density": re.compile(r"浮力|密度|物質"),
        "speed": re.compile(r"運動|速度|速率"),
        "rain": re.compile(r"氣候|季風|鋒面|天氣|海流|大氣|水圈|地球環境|變動的地球"),
    }
    for path in sorted((ROOT / "questions" / "science").glob("*.json")):
        data = json.loads(path.read_text(encoding="utf-8"))
        title = titles.get(data.get("lessonId"), "")
        kind = next((k for k, pattern in rules.items() if pattern.search(data.get("prompt", ""))), None)
        if not kind or allowed[kind].search(title):
            continue
        match = re.search(r"-(\d+)\.json$", path.name)
        index = int(match.group(1)) - 1 if match else len(changed)
        built = build(title, index)
        if built is None:
            continue
        prompt, correct, distractors, explanation, strategy = built
        options, answer_id = rotate_options(correct, distractors, index)
        data["prompt"] = prompt
        data["options"] = options
        data["answer"] = {"value": answer_id, "explanation": explanation}
        data["solutionStrategy"] = strategy
        data["solutionSteps"] = [
            f"定位單元：先確認本題要判斷的是「{title}」的核心概念，而不是沿用原本不相干的表面情境。",
            f"整理證據：從題幹找出現象、條件與要求，並將它們連到「{prompt}」。",
            f"套用原理：依「{explanation}」逐步推導正確判準，得到選項 {answer_id}「{correct}」。",
            f"排除干擾：逐項檢查其他選項是否違反單元定義、因果方向、公式、單位或必要條件；不能只看熟悉字詞。",
            f"最後回查：把選項 {answer_id} 放回題幹，確認答案同時符合資料與「{title}」的範圍；條件改變時要重新推理。",
        ]
        data["reviewStatus"] = "draft"
        data["updatedAt"] = "2026-09-07"
        path.write_text(json.dumps(data, ensure_ascii=False, indent=2) + "\n", encoding="utf-8")
        changed.append({"path": str(path.relative_to(ROOT)), "lessonId": data.get("lessonId"), "title": title, "kind": kind})
    report = {"updatedAt": "2026-09-07", "changedQuestions": len(changed), "byKind": {k: sum(1 for x in changed if x["kind"] == k) for k in rules}, "status": "draft-unit-fit-repair-pending-subject-review", "changed": changed, "boundary": "Only clear lexical mismatches were rewritten with original unit-specific prompts, options, answers, explanations and steps; public-exam provenance remains pattern-only and all changed questions stay draft."}
    out = ROOT / "implementation/reports/science-clear-unit-mismatch-repair.json"
    out.write_text(json.dumps(report, ensure_ascii=False, indent=2) + "\n", encoding="utf-8")
    print(json.dumps({"changedQuestions": len(changed), "byKind": report["byKind"], "status": report["status"]}, ensure_ascii=False))

if __name__ == "__main__":
    main()
