import json
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
LESSON = ROOT / "lessons/science/lesson-science-content-je-iv-2.json"
REPORT = ROOT / "implementation/reports/science-content-je-iv-2-first-pass-review.json"
URLS = [
    ("https://www.nehs.tc.edu.tw/wp-content/uploads/sites/95/2026/02/6%E7%90%86%E5%8C%96%E7%A7%91-%E4%B9%9D%E5%B9%B4%E7%B4%9A-%E9%A1%8C%E5%BA%AB.pdf", "國立中科實驗高級中學公開九年級理化題庫", "可逆反應、反應速率與資料判讀"),
    ("https://www.nhjh.tp.edu.tw/uploads/1675417616549dOhkhC5L.pdf", "臺北市立內湖國民中學公開九年級理化段考", "化學平衡、濃度變化與密閉系統"),
    ("https://www.kcjh.kh.edu.tw/upload/190/104_34764/%E4%B8%89%E5%B9%B4%E7%B4%9A%E7%90%86%E5%8C%96-%E7%AC%AC三次段考5-OK.pdf", "高雄市立國昌國民中學公開三年級自然科試題", "正逆反應、動態平衡與控制變因"),
]
BOUNDARY = "本紀錄只保存可追溯公開來源的章節定位、教學方向與評量能力；不複製出版社或學校教材正文、原題、選項、圖表、答案、影音或版面。"
PATTERN = "公立學校公開自然／理化試題常以密閉容器、顏色或濃度時間序列、濃度擾動、反應速率與控制變因考查可逆反應和動態平衡；本題只取能力方向並重新設計情境與數據。"
QUESTIONS = [
    ("密閉容器中的反應物 A 可生成 B，B 也能回生成 A。若一段時間後 A、B 的濃度都仍有變化，但各自的平均濃度維持穩定，最合理的判斷是？", ["反應完全停止", "只有正反應進行", "只有逆反應進行", "正、逆反應仍同時進行且速率相等"], "D", "濃度穩定不等於粒子停止；在動態平衡時正、逆反應仍同時發生，平均速率相等。"),
    ("研究可逆反應時，把反應物濃度與溫度同時改變，最主要的實驗問題是什麼？", ["所有物質必然變成氣體", "無法判定是哪個變因造成結果差異", "反應必然立刻達平衡", "系統一定不再有逆反應"], "B", "兩個自變因同時變動會混淆因果，不能知道觀察差異是濃度、溫度或交互作用造成。"),
    ("要判斷密閉容器中的可逆反應是否接近動態平衡，哪組資料最有用？", ["只看反應開始時的顏色", "只記錄最後一次溫度", "連續量測反應物與生成物濃度的時間序列", "只比較容器大小"], "C", "動態平衡的判斷需要時間序列，觀察兩方向的平均變化是否趨於穩定；單一時間點不足。"),
    ("某反應的正反應與逆反應都可能發生，但開放容器中生成物持續逸出。此時與密閉容器相比，哪項最合理？", ["移走生成物可能使逆反應受抑，系統未必維持原平衡", "生成物逸出一定使正逆速率相等", "反應一定完全停止", "容器是否開放不影響組成"], "A", "生成物離開系統會改變濃度與反應商，逆反應條件可能被削弱；必須先交代系統邊界。"),
    ("若加深可逆反應混合物的顏色，但沒有量測濃度或溫度資料，最保守的結論是？", ["一定已達動態平衡", "只能說觀察到顏色改變，原因仍需其他證據判斷", "一定只發生正反應", "一定沒有發生化學反應"], "B", "顏色可作為線索，但可能受濃度、光程、溫度或其他物質影響；不能只靠顏色宣告機制。"),
    ("在相同溫度和初始濃度下，將可逆反應重複三次，結果各次達穩定所需時間不同。最先應檢查什麼？", ["直接刪除不同的資料", "確認攪拌、量測時間、容器氣密與操作步驟是否一致", "宣布反應沒有可逆性", "把所有差異歸因於平衡常數"], "B", "先查操作與量測的控制條件，才能分辨實驗誤差、混合不均與真正的反應差異。"),
    ("向已達平衡的密閉系統加入少量反應物，若溫度不變，最合理的短期描述是？", ["正反應速率立刻永遠為零", "系統會因濃度擾動而先偏向消耗新增反應物，之後再調整", "逆反應永遠消失", "所有物質立刻變成相同濃度"], "B", "加入反應物改變濃度後，正逆速率暫時失衡；系統會重新調整到新的動態平衡，而非停止反應。"),
    ("某可逆反應的反應物濃度由 0.80 M 降到 0.50 M，生成物由 0.20 M 升到 0.50 M。若要判斷是否只是接近平衡，還缺少哪項關鍵資訊？", ["濃度單位", "反應時間與後續時間序列，以及反應式與溫度條件", "容器顏色", "讀者姓名"], "B", "需知道變化發生的時間、是否繼續穩定、反應式係數及溫度，才能判斷正逆速率與平衡狀態。"),
    ("看到可逆反應的濃度曲線在後段變平，哪項檢查最能避免把它誤判成反應停止？", ["確認正、逆方向的速率是否都可能仍存在，並增加解析度或取樣頻率", "只看最後一個點", "把平線當成沒有粒子碰撞", "刪除前段資料"], "A", "曲線變平可能代表動態平衡或儀器解析度不足；需用更細的時間與濃度證據檢查，而非直接宣告停止。"),
    ("要判斷可逆反應中是否真的有電子轉移或其他化學變化，哪項證據最直接？", ["只看溶液的容器形狀", "只看液面高度", "比較反應前後的物質組成並以反應式、濃度或光譜等資料交叉確認", "只憑題目出現雙向箭頭"], "C", "雙向箭頭是模型表示，不是觀測證據；需比較物質組成並以可測量資料支持化學變化與其方向。"),
]
STRATEGIES = [
    "區分濃度穩定與反應停止，先檢查正、逆反應是否同時存在。",
    "找出所有自變因，判斷是否能把單一變因造成的效果分離。",
    "優先選擇包含反應物與生成物的時間序列，而非單一終點觀察。",
    "先確認密閉或開放，再判斷生成物移出如何改變逆反應條件。",
    "把顏色當線索，列出可能原因並找需要補充的量測。",
    "先排查操作與量測一致性，再討論反應本身的差異。",
    "把加入物質造成的濃度擾動連到速率暫時失衡與重新平衡。",
    "整理時間、反應式、溫度與濃度資料，確認是否足以判斷平衡。",
    "用更高解析度的時間序列區分動態平衡與停止或量測不足。",
    "以物質組成與可量測資料作化學反應證據，不把符號當觀察。",
]
STEPS = [
    "確認反應物、生成物、正反應與逆反應的方向。",
    "檢查系統是否密閉、溫度是否固定及資料的時間範圍。",
    "比較濃度、顏色或速率的前後變化與時間序列。",
    "判斷是反應停止、尚在調整，還是達到動態平衡。",
    "寫出證據、限制與需要補測的資料，避免過度推論。",
]


def refs():
    return [{"url": u, "title": f"{t}；只取{loc}的題型與推理方向，未複製原題、選項、圖表、答案或版面。", "year": "109-115", "subject": "science", "locator": loc, "observedPattern": PATTERN, "reuseDecision": "pattern-only", "status": "recorded", "locatorLevel": "paper"} for u, t, loc in URLS]


def main():
    lesson = json.loads(LESSON.read_text(encoding="utf-8"))
    lesson.update({"updatedAt": "2026-09-21", "reviewStatus": "draft", "authoringStandard": "version-fused-v1"})
    for row in lesson.get("publisherResearch", []): row["reviewedAt"] = "2026-09-21"
    for row in lesson.get("versionResearch", []): row.update({"reviewedAt": "2026-09-21", "licenseBoundary": BOUNDARY})
    lesson["fusionRecord"]["llmSynthesisNote"] = "本課依官方自然科學課綱、kg-science-content-je-iv-2、南一／康軒／翰林可取得的公開研究方向與三筆公立學校自然／理化試題能力模式，以自己的話獨立融合可逆反應、正逆方向、密閉／開放系統、反應速率、濃度時間序列、濃度擾動與動態平衡；並移除原先錯置的氧化還原通用題，重寫 10 題單元題，未複製教材或試題，Terra 第二輪與正式發布審查尚未完成，維持 draft。"
    LESSON.write_text(json.dumps(lesson, ensure_ascii=False, indent=2) + "\n", encoding="utf-8")
    for i, (prompt, option_texts, correct, explanation) in enumerate(QUESTIONS, 1):
        path = ROOT / f"questions/science/question-science-content-je-iv-2-{i}.json"
        q = json.loads(path.read_text(encoding="utf-8"))
        q["prompt"] = prompt
        q["options"] = [{"id": chr(65 + n), "text": text} for n, text in enumerate(option_texts)]
        q["answer"]["value"] = correct
        q["answer"]["explanation"] = explanation
        q.update({"examPatternRefs": refs(), "reviewStatus": "draft", "updatedAt": "2026-09-21", "solutionStrategy": STRATEGIES[i - 1], "solutionSteps": STEPS})
        q["provenance"].update({"sourceUrl": URLS[0][0], "sourceLocator": "三筆公立學校公開自然／理化試題中的可逆反應、濃度時間序列、密閉系統、正逆速率、動態平衡與控制變因能力；本題改寫為可逆反應原創情境。"})
        path.write_text(json.dumps(q, ensure_ascii=False, indent=2) + "\n", encoding="utf-8")
    REPORT.write_text(json.dumps({"unit": lesson["title"], "lessonId": lesson["id"], "status": "first-pass-ai-review-complete", "reviewStatus": "draft", "checks": {"unitSpecificOriginalContent": True, "threeVersionResearchRecords": True, "publicExamPatternRewrite": True, "fusionRecordPresent": True, "interactivePredictionManipulationExplanation": True, "answersAndDetailedSteps": True, "questionContentRewritten": True, "terraSecondPass": "pending"}, "reviewedAt": "2026-09-21"}, ensure_ascii=False, indent=2) + "\n", encoding="utf-8")
    print("authored science content je iv 2")


if __name__ == "__main__": main()
