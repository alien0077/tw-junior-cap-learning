#!/usr/bin/env python3
"""Create numerically checkable draft questions for identifiable math topics."""
from __future__ import annotations
import glob, json, re
from pathlib import Path
ROOT = Path(__file__).resolve().parents[1]

CASES = [
 ("方程", [("x+5=12，x 為何？", "7"), ("3x=18，x 為何？", "6"), ("2x-4=10，x 為何？", "7"), ("x/4=3，x 為何？", "12"), ("5x+1=16，x 為何？", "3"), ("7-x=2，x 為何？", "5"), ("4(x+1)=20，x 為何？", "4"), ("2x+3= x+9，x 為何？", "6"), ("x-8=-2，x 為何？", "6"), ("9x=0，x 為何？", "0")]),
 ("不等式", [("x+3<7 的解為何？", "x<4"), ("2x≤10 的解為何？", "x≤5"), ("x-4>1 的解為何？", "x>5"), ("-x<3 的解為何？", "x>-3"), ("3x+2≥11 的解為何？", "x≥3"), ("5-x≤2 的解為何？", "x≥3"), ("x/2<4 的解為何？", "x<8"), ("-2x≥6 的解為何？", "x≤-3"), ("x+1≥1 的解為何？", "x≥0"), ("4x-8<0 的解為何？", "x<2")]),
 ("比例", [("2:3=8:x，x 為何？", "12"), ("5:2=x:10，x 為何？", "25"), ("3 公斤 60 元，每公斤多少元？", "20"), ("4:7 中 4 對應 12，7 對應多少？", "21"), ("地圖比例 1:1000，2 公分代表多少公分？", "2000"), ("6 人 4 天完成，12 人同效率需幾天？", "2"), ("a:b=3:5，a=12 時 b 為何？", "20"), ("1:4 的總量 25，較大部分為何？", "20"), ("速度 60 km/h 行駛 2 小時距離？", "120"), ("8:12 化簡為何？", "2:3")]),
 ("平方根", [("√49 為何？", "7"), ("√81 為何？", "9"), ("√(16/25) 為何？", "4/5"), ("√50 化簡為何？", "5√2"), ("√72 化簡為何？", "6√2"), ("若 x²=36 且 x>0，x 為何？", "6"), ("3√2+2√2 為何？", "5√2"), ("√12×√3 為何？", "6"), ("(√5)² 為何？", "5"), ("√2 約為何？", "1.414")]),
 ("畢氏", [("直角邊 3、4，斜邊為何？", "5"), ("斜邊 13、一直角邊 5，另一直角邊？", "12"), ("直角邊 6、8，斜邊為何？", "10"), ("正方形邊長 5，對角線長？", "5√2"), ("直角三角形斜邊 10、一直角邊 6，另邊？", "8"), ("3²+4² 是否等於 5²？", "是"), ("直角邊 5、12，面積？", "30"), ("斜邊 17、一直角邊 8，另邊？", "15"), ("直角邊相等且各為 4，斜邊？", "4√2"), ("距離水平 9、垂直 12，直線距離？", "15")]),
 ("機率", [("公平硬幣擲一次出現正面機率？", "1/2"), ("擲兩次硬幣皆正面機率？", "1/4"), ("骰子擲出 6 的機率？", "1/6"), ("骰子擲出偶數機率？", "1/2"), ("袋中 3 紅 2 藍，抽紅機率？", "3/5"), ("兩事件互斥且機率 0.3、0.2，至少一者？", "0.5"), ("從 1~10 抽到質數機率？", "2/5"), ("擲骰子大於 4 機率？", "1/3"), ("抽一張牌四種花色等數，抽紅色機率？", "1/2"), ("兩次獨立事件機率 1/3、1/2 同時發生？", "1/6")]),
 ("統計", [("資料 2,4,6 的平均數？", "4"), ("資料 1,3,5,7 的中位數？", "4"), ("資料 2,2,3,5 的眾數？", "2"), ("資料 4,9,1 的全距？", "8"), ("資料 10,20,30,40 的平均數？", "25"), ("平均數 6 的 5 筆資料總和？", "30"), ("資料 3,3,3,7 的眾數？", "3"), ("資料 2,8 的中位數？", "5"), ("若最大值 12、最小值 5，全距？", "7"), ("資料 1,2,3,4,5 的平均數？", "3")]),
 ("角", [("三角形內角 50°、60°，第三角？", "70°"), ("四邊形內角和？", "360°"), ("正五邊形內角和？", "540°"), ("正六邊形每內角？", "120°"), ("直線上一角 65°，鄰角？", "115°"), ("對頂角一角 42°，另一角？", "42°"), ("n 邊形內角和公式？", "(n-2)×180°"), ("正方形每內角？", "90°"), ("三角形外角 120°，不相鄰兩內角和？", "120°"), ("圓周角所對圓心角 80°，圓周角？", "40°")]),
]

def main() -> int:
    lessons = {}
    for f in glob.glob(str(ROOT/"lessons/math/*.json")):
        d=json.loads(Path(f).read_text()); lessons[d["id"]]=d
    qfiles={}
    for f in glob.glob(str(ROOT/"questions/math/*.json")):
        d=json.loads(Path(f).read_text()); qfiles.setdefault(d["lessonId"],[]).append((Path(f),d))
    changed=0
    for lid, items in qfiles.items():
        lesson=lessons.get(lid)
        if not lesson or lesson.get("reviewStatus")!="draft": continue
        title=lesson.get("title","")
        case=next((facts for key,facts in CASES if key in title),None)
        if case is None: continue
        concept=title.removeprefix("草稿：")
        for (path,d),(prompt,answer) in zip(sorted(items,key=lambda x:x[0].name),case):
            d["prompt"]=f"「{concept}」：{prompt}"
            wrong=["無法由題目條件判定", "把條件中的數字直接相加", "忽略題目要求的單位或符號"]
            d["options"]= [{"id":"A","text":answer}]+[{"id":chr(66+i),"text":w} for i,w in enumerate(wrong)]
            d["answer"]={"value":"A","explanation":f"依題目給定條件計算，結果為 {answer}；本題仍需數學科逐題 QA。"}
            d["reviewStatus"]="draft"
            path.write_text(json.dumps(d,ensure_ascii=False,indent=2)+"\n")
            changed+=1
    print(f"refreshed {changed} math draft questions")
    return 0
if __name__=="__main__": raise SystemExit(main())
