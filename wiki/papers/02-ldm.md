# High-Resolution Image Synthesis with Latent Diffusion Models

- 作者／版本：Rombach 等（2022）；CVPR 2022 會議版
- [公開來源](https://openaccess.thecvf.com/content/CVPR2022/html/Rombach_High-Resolution_Image_Synthesis_With_Latent_Diffusion_Models_CVPR_2022_paper.html) · [原始 PDF](../../raw/02-ldm.pdf)
- 依據與查閱範圍：PDF 第 1、3–5、8 頁，特別是第 3 節與圖 3。 頁碼是 PDF 檢視器頁數；本次重點查閱相關章節，不代表逐字讀完全文。

## 研究目的
降低直接在像素空間執行擴散模型的計算成本，同時支援高解析度與文字等條件。

## 方法
自編碼器先學習壓縮與重建；擴散模型在潛空間進行去噪；交叉注意力將文字或其他條件注入 U-Net。

## 主要發現
作者比較壓縮程度與表現，並展示文字生圖、修補及超解析度等任務；相對像素擴散，潛空間可降低運算需求。

## 限制與適用範圍
壓縮會影響保留細節；不同設定及資料集結果不應視為所有 Stable Diffusion 版本的固定表現。

## 與本 Wiki 的關聯
參考 [圖像生成流程](../concepts/generation.md)，回到 [Wiki 索引](../index.md)。
