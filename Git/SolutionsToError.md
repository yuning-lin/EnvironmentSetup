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
  * 第二行要放想要同步的遠端分支名 origin/remote_branch_name
  * 最後一行會把跟遠端不一樣的檔案刪除，若 local 有 untracked 的檔案也會被刪除
  ```linux
  git fetch origin
  git reset --hard origin/master
  git clean -f -d
  ```

* `error: path 'config.py' is unmerged`，未 merge 且無法 checkout
  ```linux
  git reset config.py
  git checkout config.py
  ```

* 若有遇到專案套件新舊版本有兩套想整合時，相同套件不同版本以舊版為準的方法：
  ```python
  # 將舊有的虛擬環境先存成 current_requirements.txt
  pip freeze > current_requirements.txt
  # 將舊有版本當作限制項 current_requirements.txt
  pip install -r requirements.txt --constraint current_requirements.txt
  ```
