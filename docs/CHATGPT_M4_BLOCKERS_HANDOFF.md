# M4 尚需外部 ChatGPT 協助的事項

本文件只列出目前無法僅依 repo 內部資料安全完成、需要外部來源或學科判斷的工作。請勿把 `mapped`、`content-reviewed` 或固定題數當成正式完成證明。

## 1. 出版社正式章節目次與逐碼 KG 對照

### 南一 30 冊

- 現有證據：校方課程計畫、教育平台或公開 metadata。
- 缺口：南一出版社可公開開啟的正式逐冊章節目次，以及每章／單元對官方 KG code 的逐筆核對。
- 請回傳：冊次、章／單元名稱、官方 URL、PDF 頁碼或穩定定位、對應 curriculumIds、confidence。
- 不可接受：只提供商品存在性、搜尋摘要或無法開啟的動態頁面。

### 翰林非國文 24 冊

- 現有證據：官方 metadata、教材簡介、部分校方課程計畫。
- 缺口：英文、數學、自然、社會完整正式逐冊目次與逐碼 KG 對照。
- 請明確區分翰林 `i英語` 商品體系與國教院審定出版者清冊，不可混為同一出版者事實。

## 2. Canonical unit 語意核對

- 國文 Ab 四個 child unit：確認「字形音義與造字／常用語詞／文言詞彙／書法」的分組是否符合教學粒度。
- 英文 Ae 三個 child unit：確認「敘事與文學／圖表與公共廣播／實用與多體裁」分組，尤其 Ae-Ⅳ-5 的歸屬。
- 自然 49 個 unit：確認跨科主題與各次主題是否應為 teachable 或 supports。
- 社會 77 個 unit：確認地理／歷史／公民 parent grouping 是否過細或應合併。
- 每項請提供 officialGroupingValid、instructionalCohesionValid、gradeScopeValid、decision、sourceUrl、sourceLocator。

## 3. Lesson／question 內容 QA

- 915 個 draft lesson、9,150 題 draft question 尚未完成逐單元內容審核。
- 需要確認 lesson 是否真的教對應 curriculum/KG 概念，而非只有欄位、題數與 provenance。
- 需要逐題核對選項、answer.value、answer.explanation 與題幹語意。
- 特別檢查國文 Ab、英文 Ae 拆分後的題目 targetUnitId，以及國文 Bd-Ⅳ-2 論證題是否真的測量比較／比喻論證。
- 請回傳可套用清單：questionId、decision、targetUnitId、reason、sourceUrl、sourceLocator、重寫建議。

## 4. 可直接升級與不可升級界線

- 可考慮升級：有官方課綱直接階層與代碼支持、且 unit 邊界具凝聚性者。
- 不可直接升級：出版社章節未取得正式來源者、canonical child design 未經核對者、題目只因 KG endpoint 正確者。
- `mapped` = 機械分群通過；`verified` = 來源與語意均核對完成。

## 5. 請回傳格式

```json
{
  "subject": "chinese",
  "unitId": "canonical-unit-chinese-content-ab-calligraphy",
  "decision": "keep | split | merge | classification-only | blocked",
  "teachable": true,
  "recommendedRelation": "covers | supports | classifies",
  "confidence": "low | medium | high",
  "curriculumIds": [],
  "sourceUrl": "https://...",
  "sourceLocator": "PDF p.X／章節／官方代碼",
  "reason": "",
  "affectedQuestionIds": []
}
```

找不到可公開驗證來源時，請明確標記 `blocked`，不要猜測或補寫不存在的頁碼。
