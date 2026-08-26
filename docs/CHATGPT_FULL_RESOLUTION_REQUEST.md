# 給 ChatGPT 的 M4 完整解決委託

請你直接協助完成 `alien0077/tw-junior-cap-learning` 的 M4 未完成工作。這不是請你評論計畫，而是請你產出 Codex 可以逐筆套用的完整結果。

## 目前真實缺口

- 915 個 draft lessons：需逐單元內容核對與原創重寫建議。
- 9,150 題 draft questions：需逐題核對題幹、選項、答案、解析與概念對齊。
- 3,960 題 migration unresolved：需要唯一 `targetUnitId`，或有充分理由標記 `blocked`。
- 161 個 canonical units：需判定 `keep`、`split`、`merge`、`classification-only` 或 `blocked`。
- 南一 30 冊、翰林非國文 24 冊：需查找正式出版社目次；找不到時要逐冊明確標記 `blocked`。

完整逐條輸入清單：

- `docs/M4_ALL_UNFINISHED_ITEMS.md`
- `docs/M4_UNRESOLVED_MIGRATION_HANDOFF.md`
- `docs/M4_DRAFT_DUPLICATE_QUESTION_HANDOFF.md`

## 你的任務

### 1. 逐題完成 3,960 題 migration

請讀取每題對應的 question JSON、source lesson JSON、`knowledgeIds`、官方 curriculum JSON 與 canonical-unit mapping。不得只依檔名、parentId 或題號猜測。

每題必須回傳：

```json
{
  "subject": "chinese|english|math|science|social",
  "questionId": "question-...",
  "sourceLessonId": "lesson-...",
  "questionKnowledgeIds": [],
  "lessonKnowledgeIds": [],
  "candidateUnitIds": [],
  "decision": "map|blocked",
  "targetUnitId": "canonical-unit-... 或 null",
  "reason": "具體說明題目實際考查概念與官方課綱對應",
  "sourceUrl": "可公開開啟的官方 URL",
  "sourceLocator": "PDF 頁碼、章節、表格或官方代碼",
  "confidence": "high|medium|low"
}
```

規則：

- 唯一 teachable canonical unit 才可 `decision=map`。
- 多候選、root-only 或資料不足必須 `decision=blocked`，不得硬填。
- target 不得是 `teachable=false` 的 domain／navigation unit。
- 只因題目品質差不能取消正確 mapping；mapping 與 QA 分開回報。
- 3,960 題必須全部逐條回覆，不可只回總數或抽樣。

### 2. 逐條完成 draft lesson QA

對 915 個 lesson 逐條回傳：

```json
{
  "lessonId": "lesson-...",
  "decision": "rewrite|keep-pending|blocked",
  "curriculumCode": "官方代碼",
  "sourceUrl": "公開官方 URL",
  "sourceLocator": "PDF 頁碼／表格／章節",
  "contentFindings": ["具體問題"],
  "rewriteBrief": "原創重寫內容大綱，不得複製教科書",
  "requiredInteractiveChanges": ["數學／自然適用時填寫"],
  "confidence": "high|medium|low"
}
```

`草稿：`、固定通用摘要、與單元無關的「不要猜／檢查證據」不能算通過。數學與自然每課至少 3 個真正涉及該概念的互動步驟。

### 3. 逐條完成 draft question QA

對 9,150 題逐條回傳：

```json
{
  "questionId": "question-...",
  "decision": "keep|rewrite|blocked",
  "correctOptionId": "A|B|C|D",
  "answerReason": "為何正確",
  "distractorFindings": {"A": "...", "B": "...", "C": "...", "D": "..."},
  "rewritePrompt": "必要時提供原創題幹",
  "rewriteOptions": ["A...", "B...", "C...", "D..."],
  "rewriteExplanation": "逐步解釋正解與主要干擾項",
  "sourceUrl": "公開官方 URL",
  "sourceLocator": "PDF 頁碼／官方代碼",
  "confidence": "high|medium|low"
}
```

必須拒絕或重寫：重複題幹、固定正解 A、`只記頁碼`、`只背答案`、`跳過學習目標`、只說「符合本單元」的解析，以及沒有測量實際課綱概念的題目。

### 4. 逐條核定 canonical units

對 161 個 unit 回傳：

```json
{
  "unitId": "canonical-unit-...",
  "decision": "keep|split|merge|classification-only|blocked",
  "teachable": true,
  "recommendedRelation": "covers|supports|classifies",
  "curriculumIds": ["cur-..."],
  "sourceUrl": "公開官方 URL",
  "sourceLocator": "精確 PDF 頁碼／官方代碼",
  "reason": "官方 grouping 與 instructional cohesion 判斷",
  "confidence": "high|medium|low"
}
```

已知規則：中文／英文 domain 為 `classification-only`；中文 Ab、英文 Ae 使用 child split；自然全球氣候變遷與社會公民 Aa 維持官方 grouping。這些仍須附公開來源定位，不能只引用本提示。

### 5. 出版社逐冊來源

對南一 30 冊與翰林非國文 24 冊逐冊回傳：

```json
{
  "publisher": "南一|翰林",
  "subject": "chinese|english|math|science|social",
  "grade": "7|8|9",
  "semester": "上|下",
  "bookExistenceVerified": true,
  "tocVerified": true,
  "kgMapped": true,
  "academicYearVerified": true,
  "sourceUrl": "官方公開 URL 或 null",
  "sourceLocator": "頁碼／章節或 blocked 理由",
  "evidenceTier": "official-publisher|school-plan|education-platform|blocked"
}
```

商品頁、搜尋摘要、登入後資源不能直接證明章節內容。找不到可公開固定定位時，請誠實回傳 `blocked`，不要捏造章名或頁碼。

## 交付方式

請分批回傳，但不可省略任何項目：

1. 先交付完整 161 個 canonical-unit JSONL。
2. 再交付 3,960 個 migration JSONL。
3. 再交付 915 個 lesson QA JSONL。
4. 再交付 9,150 個 question QA JSONL。
5. 最後交付 54 冊出版社來源 JSONL。

每批都必須包含批次範圍、總筆數、缺漏筆數與 JSON 可解析結果。請不要宣稱「全部完成」而只提供摘要、抽樣或方法；若沒有足夠證據，逐條標記 `blocked` 並說明缺少的資料。

## 重要限制

- 只能使用可公開開啟且可定位的官方來源；另一個 ChatGPT 工作階段的內部引用不算來源。
- 不得複製教科書、教師手冊或受著作權保護題庫；重寫必須是原創。
- 不得把 `validator passed`、`mapped` 或固定題數當成 semantic／teacher review。
- 請直接提供上述逐筆 JSONL 結果，讓 Codex 可以驗證、套用、更新狀態並提交；不要只給建議。
