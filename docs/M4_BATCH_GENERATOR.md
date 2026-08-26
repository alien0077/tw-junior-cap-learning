# M4 批次產生器

`scripts/generate_m4_batch.py` 從 coverage matrix 取出指定科目尚未建立 lesson 的節點，建立每單元 10 題 draft lesson/question。

```bash
python scripts/generate_m4_batch.py --subject chinese --limit 5
```

產生物件一律標為 `draft`，必須完成學科 QA 才能改為 `content-reviewed`；不複製出版社或外部題庫內容。
