# Stable Diffusion LLM Wiki

- docs/index.html：14 張教學投影片，支援上一頁、下一頁、鍵盤左右鍵和全部瀏覽。docs/wiki.html：瀏覽 Wiki 與公開來源。
- wiki/index.md：可編輯索引；wiki/papers/：五篇論文筆記。
- raw/：五篇原始 PDF、來源及 SHA-256。請尊重各論文的使用授權。
- AGENTS.md：AI 維護規則。checks/workflow.md 和 checks/report.md：流程及實際檢查紀錄。
- 繳交說明.md：六項繳交內容。

## 重新執行結構檢查
需要 Python 3，在本資料夾執行 `python3 checks/check.py`。該程式不能取代來源忠實度或實際畫面檢查。

## 本機 Git 與 GitHub Pages
本專案保留本機 Git 歷史；解壓縮時請包含隱藏的 .git 資料夾。上傳至 GitHub 並 push 預設分支後，在 Settings → Pages → Build and deployment 選 Deploy from a branch，再選該分支與 `/docs` 並儲存。首頁是簡報，同站 wiki.html 為 Wiki。實際網址以 GitHub 顯示為準；尚未發布。
