## 開始安裝
[官方網站主頁](https://git-scm.com/)  
[官方 windows 下載連結](https://gitforwindows.org/)  
基本上按著預設一直點下去到安裝完為止即可  
接下來只要在開始就可以叫出 Git Bash 下指令  
或是在各個專案點右鍵也會出現 Git Bash 的選項，開啟即是專案路徑

## 圖示簡介  
剛開始直接讀 git 語法沒有這種圖，對架構總是有點霧煞煞  
有這種圖表示每個動作大致的關係，新手應該較能理解  
[圖片來源](https://unwiredlearning.com/blog/git-basic-for-beginners/)也有英文版教學
![](https://unwiredlearning.com/wp-content/uploads/2018/07/git-flow-1024x684.png)
## 語法簡介
對於使用黑窗不習慣的人，有很多圖型化界面工具用點選操作進行版本控制如：[tortoise](https://tortoisegit.org/download/) 、 [sourcetree](https://www.sourcetreeapp.com/) 等  
官方也有列出幾款比較常用的於：https://git-scm.com/downloads/guis  
但用下指令的方式會比較直接，無須找功能在選單的位置，也可以藉此熟悉黑窗操作  
下表列出比較常使用的語法，更進階的語法可以遇到問題後再另外查詢  
指令|意義
--|--
git log --oneline|秀出這個專案所有 commit 過的資訊
git branch --remote|秀出這個專案遠端所有分支
git init|初始化當前目錄，讓 GIT 開始對此目錄進行版本控制
git status|查詢當前目錄的狀態
git clone ssh_value|把專案複製一份並存在同名的目錄裡
git clone ssh -b branch_name|在本機端，將遠端檔案庫的全部檔案複製一份下來，並指定 branch 的名字（可不必同 remote 端）
git branch|知道現在在哪個分支，以及這個專案有哪些其他分支
git branch branch_name|建立分支
git checkout branch_name|切換分支
git checkout -b branch_name|直接建立及切換分支
git checkout -t -b branch_name origin / branch_name|將遠端分支拉下來並建立分支（create branch (-b) 和 upstream track (-t)）
git checkout file_name|將修改到一半的檔案還原到上次commit的狀態
git merge master/branch|合併 master / branch 至當前分支
git pull|將分支更新至遠端狀態
git pull --rebase|它在 Fetch 完成之後，便會使用 Rebase 方式進行合併，不需要因為合併而再 commit
git add abc.py|讓 GIT 開始追蹤 abc.py 此檔
git add *.py|把所有附檔名為 py 的檔案全家到暫存區
git add --all|把所有檔案全加到暫存區
git commit -m "notes"|把暫存區的檔案加到永久區，並說明做了甚麼
git commit -a -m "notes"|把暫存區 changed / deleted 的檔案（不包含 untracked）加到永久區，並說明做了甚麼
git push -u origin remote_branch|遠端節點預設使用 origin，將當前分支推向指定遠端分支（若沒有該遠端分支則建立指定名稱）
git push remote_branch local_branch|將當前分支推向指定遠端分支（若沒有該遠端分支則建立指定名稱）
git mv oldfolder/ newfolder/|將資料夾做搬遷
git mv oldfolder newfolder|變更資料夾名、檔名
git rm -r –cached folder_name|移除資料夾 git管理
git diff|秀出修改不同之處
git checkout HEAD^ filename|回到前一個版本
git stash|備份當前工作區
git stash pop|讀取最新一次保存內容並恢復
git stash list|列出所有備份
git stash clear|清空備份
git remote update --prune|等同 git fetch –all，更新所有遠端分支（--prune 把原本刪除的 remote branch 刪除）
git submodule update --init --recursive|更新 submodule

## BASH 快捷鍵
快捷鍵|意義
----|----
shift + Q | 換行
ctrl + C | 暫停執行

## 參考來源
* [連猴子都能懂得 Git 入門指南](https://backlog.com/git-tutorial/tw/intro/intro2_1.html)
* [為你自己學 Git](https://gitbook.tw/)

