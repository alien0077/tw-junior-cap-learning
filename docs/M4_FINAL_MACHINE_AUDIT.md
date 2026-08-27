# M4 機器稽核快照（2026-08-27）

本次在 `/Users/alien/Desktop/tw-junior-cap-learning` 執行：

```text
python3 scripts/validate_data.py
validated 12905 JSON files, 12885 IDs, 1032 KG nodes
```

## 已由本地證據確認

- lessons：1,036；questions：10,360。
- 每個 lesson 至少 10 題；最低題數為 10，未達門檻 0 筆。
- lesson 狀態：121 `content-reviewed`、915 `draft`。
- question 狀態：1,210 `content-reviewed`、9,150 `draft`。
- lesson/question 缺少 provenance：0 / 0。
- 數學與自然互動步驟及 Schema 驗證通過。
- 題目必要欄位（options、answer.value、answer.explanation、lessonId、provenance）缺漏：0 筆；`git diff --check` 無錯誤。
- 有 3 題答案解析少於 10 字（`question-science-heat-7`、`question-math-equation-9`、`question-chinese-common-words-recognition-3`）；語意仍可讀，但列為人工內容 QA，不擅自擴寫。

## 尚不能由機器稽核證明

- `content-reviewed` 不是教師或學科專家認證。
- 題目是否逐題符合各官方課綱語意、答案是否經外部來源核對，仍需人工／外部內容審查。
- 南一 30 冊及翰林非國文 24 冊的完整出版社正式目次與逐碼 KG 對照仍未完成。
- GitHub Actions API 本次因網路連線錯誤無法取得最新 run；本地 validator 結果不替代遠端 CI 證據。

本文件是機器稽核紀錄，不是 M4 完成宣告。
