# M4 公開來源核對紀錄

更新日期：2026-08-26

## 核對範圍

- 1,032 筆 coverage rows、1,036 份 lesson、10,360 題 question。
- lesson 以國家教育研究院課程綱要入口與國中教育會考官方網站作為公開查核入口。
- question 保留原創性；來源欄位只表示學習目標／能力方向的查核入口，不表示題目摘錄或改寫自外部題庫。

## 來源與界線

1. 國教院課程綱要：確認五科學習內容與學習表現的官方範圍。
2. 國中教育會考官方網站：確認能力導向與公開樣卷／說明的查核入口。
3. 翰林、南一、康軒公開頁面：只核對版本、冊別、章節 metadata；不擷取課文、習作或題庫。
4. Wiki 或一般教育網站：僅作次要交叉資料，不能單獨推翻官方課綱。

## 機器核對結果

- 所有 lesson 已具 `studyReferences` 公開來源連結。
- 所有 question 已具 `provenance.sourceUrl` 與 `sourceLocator`（KG ID）。
- `python3 scripts/validate_data.py`：12,537 JSON files、12,524 IDs、1,032 KG nodes。
- `content-reviewed` 仍代表 repo 內部 QA；未標記 `teacher-reviewed`。
