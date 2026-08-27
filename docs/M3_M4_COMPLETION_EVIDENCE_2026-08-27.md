# M3／M4 公開證據結案紀錄

更新日期：2026-08-27

## 結論

M3 的公開證據門檻已完成：五科、三家版本、六冊共 90 個
`publisher × subject × volume` 格都有至少一個可追溯的公開來源，機器檢查
共找到 97 個來源綁定。這代表專案可提供可查證的版本／章節對照；不代表
每一筆都是出版社的正式背書。

## 證據分層

1. 國家教育研究院的 115 學年度教科用書資料確認版本／冊別事實：
   <https://textbooks.naer.edu.tw/>。
2. 出版社公開頁面的章節或產品索引，例如翰林數學六冊公開索引：
   <https://mathvideo.hle.com.tw/1A/>。
3. 公立國中公開的 115 學年度選書與課程計畫，作為實際採用及逐單元的
   交叉證據，例如新北市崇林國中：
   <https://www.chjs.ntpc.edu.tw/p/406-1000-12156%2Cr73.php?Lang=zh-tw>。

各 mapping set 的原始 URL、章節定位、驗證日期、證據型別及信心值仍保留在
`textbook-mapping/`。校方資料保持 `medium`，絕不改標為
`official-publisher-page` 或 `high`；只有公開出版社索引才可使用後者。

## 可重複驗證

```sh
python3 scripts/validate_m3_public_evidence.py
```

輸出應為 `M3 public evidence verified: 90 publisher/subject/volume cells`。

## M4 canonical migration 的結案範圍

M4 教材／題目的課程事實已由原有 stable KG ID 表達；canonical unit 是網站
導航資料，不是另一個教材事實來源。故本次將 6,420 筆有唯一 target 的遷移
標為 `candidate`，並把 3,940 筆無唯一 target 的項目明確標為
`not-applicable`：保留其直接 KG 關係，不硬塞入推測的 canonical unit。
五份 migration manifest 均已標為 `completed`。

此決策不刪除任何 lesson、question、KG ID 或 migration 記錄；也不把
canonical navigation metadata 說成出版社章節對照。
