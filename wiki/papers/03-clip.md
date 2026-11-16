# Learning Transferable Visual Models From Natural Language Supervision

- 作者／版本：Radford 等（2021）；arXiv v1
- [公開來源](https://arxiv.org/abs/2103.00020) · [原始 PDF](../../raw/03-clip.pdf)
- 依據與查閱範圍：PDF 第 1、3–5 頁，第 2.3 節及圖 2、3。 頁碼是 PDF 檢視器頁數；本次重點查閱相關章節，不代表逐字讀完全文。

## 研究目的
探索能否利用自然語言監督，訓練可遷移到多種視覺任務的圖像表示。

## 方法
以大量圖文配對進行對比學習，分別編碼圖像與文字，拉近配對表示、區分不相配的表示。

## 主要發現
作者報告其表示可用自然語言進行零樣本遷移，並在多個資料集上評估。

## 限制與適用範圍
CLIP 原研究不是擴散生成模型；只用它來理解部分早期 Stable Diffusion 的文字編碼器，不代表所有版本皆相同。

## 與本 Wiki 的關聯
參考 [圖像生成流程](../concepts/generation.md)，回到 [Wiki 索引](../index.md)。
