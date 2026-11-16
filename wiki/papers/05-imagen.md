# Photorealistic Text-to-Image Diffusion Models with Deep Language Understanding

- 作者／版本：Saharia 等（2022）；NeurIPS 2022 會議版
- [公開來源](https://proceedings.neurips.cc/paper_files/paper/2022/hash/ec795aeadae0b7d230fa35cbaf04c041-Abstract-Conference.html) · [原始 PDF](../../raw/05-imagen.pdf)
- 依據與查閱範圍：PDF 第 1、3–5、9–10 頁，第 2 節與第 6 節。 頁碼是 PDF 檢視器頁數；本次重點查閱相關章節，不代表逐字讀完全文。

## 研究目的
探索大型預訓練語言模型搭配擴散模型進行文字生圖的表現。

## 方法
以凍結的 T5 文字編碼器表達提示詞；先產生低解析度圖片，再透過兩階段超解析度擴散放大。

## 主要發現
作者在其實驗設定下發現較強的文字編碼對圖像品質和文字一致性有幫助，並使用 DrawBench 進行比較。

## 限制與適用範圍
Imagen 是另一個獨立模型，不是 Stable Diffusion 的構件。論文提到對人物生成、資料偏差與社會偏見的限制；歷史結果不能直接代表現在模型排名。

## 與本 Wiki 的關聯
參考 [圖像生成流程](../concepts/generation.md)，回到 [Wiki 索引](../index.md)。
