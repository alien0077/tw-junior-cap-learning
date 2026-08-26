# M4 需要 ChatGPT 協助事項

更新日期：2026-08-26

本文件是目前 repo 唯一的外部協作入口。Codex 已完成資料結構、來源欄位、schema 與 validator；以下工作需要另一個 ChatGPT 具備課綱研究與學科內容判斷後提供可追溯回覆。

## 一、逐題 migration 語意核對

目前共有 4,050 題沒有唯一 `targetUnitId`，不能依 `parentId` 或檔名猜測：

| 科目 | 待核對題數 |
|---|---:|
| 國文 | 540 |
| 英文 | 1,010 |
| 數學 | 50 |
| 自然 | 970 |
| 社會 | 1,480 |
| 合計 | 4,050 |

逐題清單：`docs/M4_UNRESOLVED_MIGRATION_HANDOFF.md`。

請依題目實際考查概念，決定唯一 teachable canonical unit；若無法判斷，標記 `blocked`，不可填入猜測的 unit。

## 二、915 個 draft lesson 的學科內容審核

每個 lesson 需要核對：

1. 是否真正回答對應官方課綱 title。
2. 內容是否適合國中程度、無超出課綱。
3. 學霸筆記與 references 是否支持內容。
4. 數學／自然是否有至少 3 步可操作互動教學。
5. 是否含重複或批次通用模板；必要時提供原創重寫方向。

各科 draft lesson：國文 63、英文 131、數學 47、自然 315、社會 359。

## 三、9,150 題 draft question 的逐題 QA

逐題核對：

- options 是否合理且只有正確答案。
- `answer.value` 是否對應正確選項。
- `answer.explanation` 是否真的支持答案。
- 題目是否測到該 lesson／KG 概念，而非泛用題。
- 干擾選項是否具有迷惑性但不造成歧義。
- 是否有重複題幹、超綱概念或受著作權保護的複製內容。

重複題幹明細：`docs/M4_DRAFT_DUPLICATE_QUESTION_HANDOFF.md`；聚合 QA：`docs/M4_DRAFT_QA_REPORT.md`。

## 四、canonical unit 語意與版本核驗

161 個 canonical units 目前是 `mapped` 候選，不是出版社或教師認證。請核對：

- 國文 Ab 四個 child 分組是否具教學凝聚性。
- 英文 Ae 三個 child 分組是否合理。
- 自然跨科主題是否維持 teachable／`covers`。
- 社會地理、歷史、公民 grouping 是否符合官方課綱層級。
- 哪些 unit 可升級 `verified`，哪些只能維持 `mapped` 或 `blocked`。

## 五、出版社章節來源

- 南一 30 冊：需要出版社正式逐冊章節目次、公開 URL、頁碼／章節定位，以及對應 KG code。
- 翰林非國文 24 冊：需要出版社正式逐冊章節目次、公開 URL、頁碼／章節定位，以及對應 KG code。

校方課程計畫、教育平台或商品存在頁只能作交叉證據，不能宣稱出版社背書。找不到公開定位時請標記 `blocked`。

## 回覆格式（請逐筆或逐組提供）

```json
{
  "subject": "chinese|english|math|science|social",
  "unitId": "canonical-unit-...",
  "questionId": "question-...",
  "decision": "keep|split|merge|classification-only|blocked",
  "targetUnitId": "canonical-unit-... 或 null",
  "reason": "具體語意與課綱判斷理由",
  "sourceUrl": "可公開開啟的官方 URL",
  "sourceLocator": "PDF 頁碼、章節、表格或官方代碼",
  "rewrite": "必要時提供原創重寫方向",
  "confidence": "high|medium|low"
}
```

注意：另一個 ChatGPT 工作階段的內部引用、未公開連結、搜尋摘要或猜測頁碼，不能作為 repo provenance。收到可追溯回覆後，Codex 才會套用資料、更新狀態、執行 validator 並推送。

相關完整清單：`docs/M4_REMAINING_TASKS_MASTER.md`。
