## 情境
想指定 git 忽略追蹤的檔案或檔案類型（EX：機敏資料、日誌等）  
因此建立 gitignore 檔儲存忽略追蹤的規則    
切記，gitignore 檔僅對創造規則後才開始用 git 追蹤的檔案才有管理效果  

## 步驟
1. 專案下開啟 git bash
2. `touch .gitignore`：新增 gitignore 檔
3. .gitignore 點兩下 > 開始編輯如下框內容 > 儲存
  ```
  # 忽略 log.txt 檔案
  log.txt

  # 忽略所有附檔名是 .txt 的檔案
  *.txt

  # 忽略 db 目錄下的 password.txt 檔案
  db/password.txt 

  # 忽略所有 db 目錄下附檔名是 .sql 的檔案
  db/*.sql
  ```
  
  ## 參考資源
  * [github 整理各種語言常見的 .gitignore 內容](https://github.com/github/gitignore)
