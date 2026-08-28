# 完整教學正文範圍稽核（2026-08-27）

## 結論

本次「完整教學正文」的可驗收範圍是全部 1,031 筆可用 lesson：官方課綱中 `level=learning-content` 的 583 個原子學習內容節點，另加 4 個補充原創單元，以及 208 個學習表現、179 個 topic、57 個 theme 導覽／能力頁。每一頁均有：

- 依出版社公開目次／影音／教師公開資源研究的 `publisherResearch`；
- 六階段自編正文（引起動機、概念解釋、 worked example、引導練習、遷移、反思）；
- 4 點摘要、3 個離堂檢核；
- 數學的代數表達互動或自然的科學探究互動；
- 至少 10 題連回同一 `lessonId` 的題庫。

教材正文、例題、選項、提示與回饋均為本專案獨立撰寫，出版社資料只用於確認章節順序、概念遞進、活動型態與評量型態；未儲存或重製教科書文字、圖片、習題、答案或影音逐字稿。

`lessonScope` 會保留課綱層級，讓能力／分類頁不被誤稱為出版社章節；它們仍提供可學習的正文與練習，但文字明示其為導覽或能力訓練。

## 節點與教材範圍

`data/m4-coverage-matrix.json` 共 1,032 筆：

| 課綱層級 | 數量 | 在本專案的意義 |
| --- | ---: | --- |
| `learning-content` | 583（另 4 個補充原創單元） | 可直接教學的原子內容；全部完成 `full-lesson-v1` |
| `learning-performance` | 208 | 學習表現／能力動詞，例如聆聽、推理、探究；頁面標示為能力訓練，不冒充出版社章節 |
| `topic` | 179 | `Ab：字詞`、`地 Aa`、`歷 Ha` 等上位分類，頁面標示為導覽並連結子節點 |
| `theme` | 57 | `A：文字篇章`、`自然環境` 等領域主題或學習表現群組 |
| `domain` | 5 | 五個領域根節點；已 deprecated，不列入可用 lesson |

因此 1,031 筆可用頁面現在都能直接閱讀完整正文；其中 444 筆屬分類／能力頁（208+179+57），不被宣稱為出版社章節。若未來要把某個 `topic` 拆成獨立課程，必須先新增來源定位與穩定 ID 對照，再依同一 `full-lesson-v1` 契約撰寫，不能用批次模板冒充。

## 品質驗證

```text
python3 scripts/validate_data.py
validated 13112 JSON files, 12885 IDs, 1032 KG nodes

python3 scripts/validate_site_index.py
site index validated: 1031 lessons, 10310 question paths, revision local

node --check site/app.js
git diff --check
```

另以五科各抽一個單元進行瀏覽器 smoke test：五科皆載入正文區塊與摘要；數學、自然各載入學科互動並可操作，語文與社會則呈現正文與題庫（不強行加入不適切的數理互動）。A-7-1 實測為 7 個正文區塊、3 個互動步驟、10 題題庫。
