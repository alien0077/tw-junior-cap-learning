# M4 自編教材與題庫方法

## 目前內容的真實來源

目前 repo 的 10 份 lesson 與 100 題 question 都是本專案自行撰寫：

- 沒有從網路題庫、補習班題庫、出版社課本、習作或教師用書複製。
- 沒有把現有題目改幾個字後當成原創題。
- 學習目標來自 repo 已核驗的官方課綱資料與穩定 Knowledge Graph ID；這些是「學什麼」的依據，不是可改寫的題目來源。
- 網路學霸筆記只作為重點研究與學習策略查核；不得複製其文字、題目、選項或答案。整合紀錄見 docs/M4_STUDY_NOTE_HIGHLIGHTS.md。若未來使用外部資料，只能作為事實查核或題型研究，不能抽取原文、選項、答案或解析。

## 參考資料層級

1. 教育部／國家教育研究院正式課綱 PDF：確認學習表現、學習內容與範圍。
2. knowledge 目錄中的 foundational graph：使用已驗證的穩定 KG ID，讓 lesson/question 可追溯回課綱來源。
3. 國中教育會考官方公開說明：只用來理解能力導向與題型方向，不複製歷屆題目。
4. 出版商公開資料：M3 版本 mapping 使用，不拿出版社教材內容產生 M4 題目。

官方課綱 URL、發布日與定位集中記錄在 docs/SOURCES.md 及各 curriculum／knowledge JSON 的 sources 欄位。

## Lesson 編寫流程

1. 選定一個或多個 KG ID，寫出可觀察的學習目標。
2. 用自己的語言寫摘要、核心概念、判斷步驟與常見錯誤。
3. 加入可以自我檢查或遷移到新情境的練習策略。
4. 檢查沒有依賴出版社課文、例句、圖片或教師手冊。
5. 標記 provenance.origin=original、reviewStatus=content-reviewed，並確認所有 KG endpoint 存在。

## Question 編寫流程

1. 指定唯一測量的 KG ID 與題目目標。
2. 先寫正確答案與理由，再設計三個具有迷惑性但可排除的 distractors。
3. 確認題幹資訊足夠、只有一個最佳答案，且不能靠字數、語氣或選項位置猜答案。
4. 在 answer.value 寫答案，在 answer.explanation 寫可檢查的推理；不能只寫「答案是 B」。
5. 標記 provenance.origin=original 與 reviewStatus=content-reviewed。
6. 通過 Schema、JSON 語法、KG endpoint 與答案欄位檢查。

## 答案與審核標準

每題至少要能回答：正確選項是什麼、為什麼符合 KG 目標、其他選項為何不如正解，以及不同解法哪些仍可接受。

本專案沒有真人 reviewer。`content-reviewed` 表示已通過本專案的 AI 判讀審查，不等於教師、真人或學科專家審查。內容審查由 AI 執行；需要較高判讀能力時，建議升級 Terra model 做第二輪 AI 複核。Terra 複核仍不代表真人認證。

AI 審查至少檢查：單元／KG 符合度、唯一最佳答案、干擾選項品質、解析是否支持答案、來源與授權界線、同課重複、跨課模板重用，以及是否仍殘留批次模板文字。任何一項未完成即維持 `draft`。

## 歷屆題與公立國中考題

- 歷屆會考題先確認依法令舉行考試的來源與可利用範圍，並記錄年度、科目、題號、`sourceUrl`、`sourceLocator`、答案與解析。
- 公立國中考題的公開網址不等於重製授權；有明示授權才可收錄原題或改編題，使用 `provenance.origin=licensed` 並保存授權證據。
- 沒有明示授權時，只能研究其能力目標與題型，重新獨立設計題幹、數據、選項與解析；只改數字、人名或情境仍不得視為原創。
- 每個 lesson 內不得有重複題幹或完整重複題目；題目 QA 會以正規化後的題幹、選項與答案檢查。

## 未來若要使用外部參考

可引用公開、可追溯且授權允許的資料來查核事實，但該筆資料必須記錄 sourceUrl 與 sourceLocator，並保留足夠表達差異。不得使用「先找題庫、再改寫」作為原創題目流程；若要收錄合法公開題，應改標 official-open 或 licensed，保留原始授權與來源，不可標成 original。

## M4 題庫最低數量

- 每個 lesson 必須有至少 10 題已連結的 question；question 以 lessonId 明確歸屬單元。
- 每題必須保留 answer.value 與 answer.explanation；CI 會計算每個 lesson 的題數，少於 10 題即失敗。
\n## 學霸筆記重點與互動教學\n\n每份 lesson 以 studyHighlights 標出至少三個可操作重點，並保存 studyReferences。數學與自然 lesson 必須提供至少三步 guided-choice 互動，每步包含選項、答案與回饋，讓學童先作答再回看重點。\n
