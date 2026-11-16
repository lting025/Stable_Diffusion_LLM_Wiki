# 索引

- [圖像生成流程](concepts/generation.md)
- [執行紀錄](log.md)

## 論文
- [Denoising Diffusion Probabilistic Models](papers/01-ddpm.md)：訓練時將影像逐步加入雜訊，學習反向去噪；生成時從隨機雜訊出發反覆去噪。
- [High-Resolution Image Synthesis with Latent Diffusion Models](papers/02-ldm.md)：先使用自編碼器壓縮影像，在潛空間進行擴散，並以交叉注意力接收文字等條件，最後解碼為圖片。
- [Learning Transferable Visual Models From Natural Language Supervision](papers/03-clip.md)：CLIP 利用圖文配對訓練影像與文字編碼器，使對應圖文的表示較接近。
- [Classifier-Free Diffusion Guidance](papers/04-cfg.md)：無分類器引導結合有條件與無條件預測，調整生成對條件的遵循及品質與多樣性之間的取捨。
- [Photorealistic Text-to-Image Diffusion Models with Deep Language Understanding](papers/05-imagen.md)：Imagen 以 T5 文字編碼器、低解析度擴散與後續超解析度擴散生成圖片，展示文字表徵的重要性。
