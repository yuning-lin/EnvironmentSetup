## 紀錄問題解方
* ```
  fatal: Unable to create 'D:/XXXXXX/.git/index.lock': File exists.
  
  Another git process seems to be running in this repository, e.g.
  an editor opened by 'git commit'. Please make sure all processes
  are terminated then try again. If it still fails, a git process
  may have crashed in this repository earlier:
  remove the file manually to continue.
  ```
  1. 將所有相關程式關閉，重啟後再試一次
  2. 若 i. 失敗，將 /.git/index.lock 檔案刪除後再試一次

* pull 後跟遠端分支仍不相同
  注意：最後一行會把跟遠端不一樣的檔案刪除，若 local 有 untracked 的檔案也會被刪除
  ```linux
  git fetch origin
  git reset --hard origin/master
  git clean -f -d
  ```
