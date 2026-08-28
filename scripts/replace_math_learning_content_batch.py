"""以公開試題的能力型態為研究來源，替換數學總分類節點的模板題。

題目為獨立編寫，保留既有 question ID；不複製公開試卷的題幹、選項、圖表或答案。
"""
from __future__ import annotations

import json
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
SOURCE = "https://www.yacjh.kh.edu.tw/upload/221/101_30637/114%E4%B8%8B%E5%AD%B8%E6%9C%9F%E7%AC%AC%E4%B8%80%E6%AC%A1%E6%AE%B5%E8%80%83%E4%B8%89%E5%B9%B4%E7%B4%9A%E6%95%B8%E5%AD%B8.pdf"
CURRICULUM = "https://www.naer.edu.tw/upload/1/16/doc/815/%E5%8D%81%E4%BA%8C%E5%B9%B4%E5%9C%8B%E6%B0%91%E5%9F%BA%E6%9C%AC%E6%95%99%E8%82%B2%E8%AA%B2%E7%A8%8B%E7%B6%B1%E8%A6%81%E5%9C%8B%E6%B0%91%E4%B8%AD%E5%B0%8F%E5%AD%B8%E6%9A%A8%E6%99%AE%E9%80%9A%E5%9E%8B%E9%AB%98%E7%B4%9A%E4%B8%AD%E7%AD%89%E5%AD%B8%E6%A0%A1-%E6%95%B8%E5%AD%B8%E9%A0%98%E5%9F%9F.pdf"

ITEMS = [
    ("某商品原價 800 元，先打 75 折，再加收 5% 的服務費，最後應付多少元？", ["600 元", "630 元", "640 元", "660 元"], "B", "先算 800×0.75=600，再算 600×1.05=630；折扣與加成要依序作用。", "easy"),
    ("若直線 y=−2x+6 與 x 軸交於 P 點，P 的座標為何？", ["(−3,0)", "(0,3)", "(3,0)", "(6,0)"], "C", "與 x 軸交點的 y=0，代入 0=−2x+6 得 x=3，因此 P=(3,0)。", "easy"),
    ("方程式 x²−5x+6=0 的兩根相差多少？", ["1", "2", "3", "5"], "A", "x²−5x+6=(x−2)(x−3)，兩根為 2、3，相差 1。", "medium"),
    ("一個三角形的三邊長為 6、8、10，則此三角形的面積為多少？", ["24", "30", "40", "48"], "A", "6²+8²=10²，為直角三角形；面積為 6×8÷2=24。", "medium"),
    ("半徑 3 公分、高 5 公分的圓柱，若 π 取 3.14，體積約為多少立方公分？", ["47.1", "94.2", "141.3", "282.6"], "C", "圓柱體積=πr²h=3.14×3²×5=141.3。", "medium"),
    ("資料 4、6、6、8、11 的平均數與中位數分別為何？", ["7 與 6", "7 與 7", "7.2 與 6", "7.2 與 7"], "A", "總和 35，平均數 35÷5=7；排序後中央值是 6，因此選 A。", "easy"),
    ("袋中有 3 顆紅球、2 顆藍球，不放回連取 2 顆，兩顆同色的機率為何？", ["1/5", "2/5", "1/2", "3/5"], "B", "同色情形為紅紅或藍藍：(3/5)(2/4)+(2/5)(1/4)=8/20=2/5。", "hard"),
    ("若 a:b=3:5 且 a+b=32，則 b−a 為何？", ["8", "10", "12", "20"], "A", "總份數 8 份，每份 4；a=12、b=20，所以 b−a=8。", "easy"),
    ("等差數列 5、9、13、17、… 的第 20 項為何？", ["77", "81", "85", "89"], "B", "第 n 項=5+(n−1)×4，代 n=20 得 5+76=81。", "medium"),
    ("在座標平面上，點 A(−2,3) 向右平移 5、向下平移 4 後得到 B，B 的座標為何？", ["(3,−1)", "(−7,7)", "(3,7)", "(−7,−1)"], "A", "向右 5 使 x 變 −2+5=3，向下 4 使 y 變 3−4=−1，因此 B=(3,−1)。", "easy"),
]

def main() -> None:
    for i, (prompt, texts, answer, explanation, difficulty) in enumerate(ITEMS, 1):
        path = ROOT / "questions" / "math" / f"question-math-learning-content-{i}.json"
        data = json.loads(path.read_text())
        data["prompt"] = prompt
        data["options"] = [{"id": chr(65+j), "text": text} for j, text in enumerate(texts)]
        data["difficulty"] = difficulty
        data["answer"] = {"value": answer, "explanation": explanation}
        data["provenance"] = {
            "origin": "original",
            "license": "All rights reserved",
            "sourceUrl": SOURCE,
            "sourceLocator": f"高雄市立鹽埕國中 114 學年度下學期第一次段考三年級數學科試題卷；僅研究公開題型與能力方向，本題為獨立改編，非原題重製。另以官方數學課綱核對範圍（{CURRICULUM}）。",
            "authoringNote": "Safe adaptation from public-exam skill patterns; no source wording, options, figures, or answer reproduced. Requires second-pass AI content review.",
        }
        data["reviewStatus"] = "draft"
        data["updatedAt"] = "2026-08-28"
        path.write_text(json.dumps(data, ensure_ascii=False, indent=2) + "\n")

if __name__ == "__main__":
    main()
