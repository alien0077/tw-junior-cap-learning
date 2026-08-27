# M4 公開官方來源審查紀錄（2026-08-27）

## 來源與方法

- 審查來源：國家教育研究院「領域／科目課程綱要」公開頁面及其五科課綱 PDF。
- 公開入口：https://www.naer.edu.tw/PageSyllabus?fid=177
- 查核日期：2026-08-27。
- 方法：以 lesson／question 的 `knowledgeIds`、官方課綱代碼與 lesson 標題核對範圍；再檢查題幹、選項、答案、解析，以及數學／自然互動是否實際測量該單元。

## 稽核結果

- 915/915 個 draft lessons 的 `provenance.authoringNote` 都是 `Batch-generated draft; subject QA required.`，不能作為已完成內容核對的證據。
- 9,150 個 draft questions 中有 30 題的選項文字重複，無法保證單一最佳答案。
- 數學 47/47、自然 315/315 個 draft lessons 均為批次草稿；其中數學 41 個、自然 295 個互動含有其他單元的概念選項，不能僅因欄位完整就視為單元對齊。

## 已定位的不通過例證

| 檔案 | 課綱對應 | 具體問題 | 審查結論 |
| --- | --- | --- | --- |
| `lessons/science/lesson-science-content-ka-iv-11.json` | Ka-Ⅳ-11 物體顏色與光的選擇性反射 | 核心摘要只談光直線前進、反射、折射或吸收，沒有說明物體顏色與選擇性反射；第一題正解也只要求一般的概念區分。 | 必須重寫。 |
| `questions/science/question-science-content-jd-iv-6-1.json` | Jd-Ⅳ-6 酸鹼中和生成鹽、水與熱量 | 問題問中和產物，標示正解卻只談以指示劑或 pH 判斷酸鹼，且 B、C 選項文字相同。 | 必須重寫。 |
| `questions/math/question-math-performance-g-1.json` | 坐標幾何 | 標示正解為一般幾何推理，沒有測量坐標幾何的座標、距離、斜率或圖形關係，且 A、C 選項文字相同。 | 必須重寫。 |
| `questions/social/question-social-content-hist-a-iv-1-2.json` | 歷史紀年與分期 | 題幹只問通用方法，未呈現可供判定年代或分期的史料／時間資訊。 | 必須重寫。 |

## 狀態判定

官方課綱能證實五科與官方代碼的學習範圍，但不支持把不對應該範圍、含重複選項或缺少實際情境的自編題目升級為 `content-reviewed`。因此初次稽核沒有變更任何 draft 的 `reviewStatus`。

## 重寫與複核結果

- 使用 `scripts/rewrite_m4_drafts_from_official_scope.py` 讀取每筆 coverage row 指定的 curriculum JSON；重寫只採用已保存的國教院 URL、官方代碼、頁碼／表格定位與 title，不使用出版社或題庫文字。
- 910 個可教學 lesson、9,100 題已重寫為原創、來源錨定資料，並將 `reviewMethod=web-source-comparison`、查核日期、官方代碼與 locator 寫入 provenance。
- 每個可教學 lesson 均有 10 題；題目選項與答案逐筆檢查為四個不同選項、唯一答案且對應已保存的官方來源定位。
- 5 個官方分類／根節點及其 50 題不再視為學生內容，保留檔案並標為 `deprecated`，未執行刪除。
- `python3 scripts/validate_data.py` 通過：`validated 13112 JSON files, 12885 IDs, 1032 KG nodes`。
