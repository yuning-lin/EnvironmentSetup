## 常用語法
語法|意義
----|----
`ls`|列出當前資料夾下的所有檔案
`ls -l`|列出當前資料夾下的所有檔案及其詳細資訊
`ls \| grep main`|列出當前資料夾下有 **main** 字的檔案
`pip list \| grep pandas`|列出 python 已安裝套件中有 **pandas** 字樣的套件
`call env_python\Scripts\activate`|啟動名為 env_python 的虛擬環境
`mkdir /Users/user_name/folder_name`|創建 /Users/user_name/folder_name
`cd /Users/user_name/folder_name`|移動至 /Users/user_name/folder_name
`touch file_name.txt`|創建 file_name.txt
`find . -name file_name.txt`|尋找當前目錄底下名為 file_name.txt 的檔案
`rm file_name.txt`|刪除 file_name.txt
`mv file_name.txt src`|移動 file_name.txt 於 src 下
`cp file_name.txt src`|複製 file_name.txt 於 src 下
`cp file_name.txt file_name2.txt`|於當前資料夾下複製 file_name.txt 並命名為 file_name2.txt
`echo "This is a test." > ./test.txt`|創建內容為 This is a test. 至當前目錄下的 test.txt
`cat ./test.txt`|顯示當前目錄下 test.txt 的檔案內容
`curl -O https://s3-ap-northeast-1.amazonaws.com/sqlite-demo-data/gapminder.csv`|下載該網站之 gapminder.csv
`sudo apt-get install vim`| 讓一般用戶得以用系統管理員的身分執行 vim 套件的安裝（sudo：仿管理員身分、apt-get：套件管理工具）

## VM 工作執行相關用法
* [Linux 技術支援 - Process（進程）](https://www.hy-star.com.tw/tech/linux/process/process.html#jobs)
  
語法|意義
----|----
`htop`|顯示當前執行的工作項目、CPU 及 Memory 等使用情況
`nohup python3 app.py &`|在背景用 python3 執行 app.py（nohup：不斷地執行、&：在背景執行）
`ps aux \| grep A`|列出執行中名字有 A 的 process（a：顯示所有 process、u：以用戶為主的格式来顯示、x：不以終端機區分）
`ps aux \| grep app.py`|列出執行命令中名字有 app.py 的 process
`kill process_id`|關掉指定 process_id 的 process
`netstat -ap\|grep port_num`|檢視佔用此 port_num 的 process

## crontab 工作排程相關指令
* [情境模擬範例](https://github.com/yuning-lin/EnvironmentSetup/blob/main/Linux/BySenarios/CreateCronJob.md) 
* 部分編輯的概念跟 vim 指令通用 
  
語法|意義
----|----
`crontab -l`|查看 crontab 內容
`crontab -e`|編輯 crontab 內容
`crontab -r`|刪除 crontab 內容
`sudo crontab -u user_name -l`|查看指定使用者 crontab 內容
`crontab -u user_name -e`|編輯指定使用者 crontab 內容
`* * * * * path_of_file --parameter`|新增 crontab 設定
`* * * * * user_name path_of_file --parameter`|新增指定使用者 crontab 設定

## tmux 相關用法
終端機管理工具。  
可以同時開啟多個獨立的 session 執行背景程式、啟著 api 等  
* [Blog：Linux tmux 終端機管理工具使用教學](https://blog.gtwang.org/linux/linux-tmux-terminal-multiplexer-tutorial/) 
* [Blog：終端機 session 管理神器 — tmux](https://larrylu.blog/tmux-33a24e595fbc) 
  
語法|意義
----|----
`sudo apt install tmux`|Ubuntu Linux 安裝 tmux
`tmux`|進入 tmux（會在視窗底部出現綠色狀態列）
`man tmux`|tmux 使用手冊
`tmux ls`|列出所有在執行的 session
`tmux new -s session_name`|創建一個新的 session_name 
`tmux a -t session_name`|追蹤該 session_name 運行狀況
`tmux set mouse on`|設定可以滑鼠滾動

鍵盤輸入|意義
----|----
crtl + B 放開再按 D | 跳出 tmux


## vim 相關用法
`vim file_name.txt`：開啟視窗編輯 file_name.txt
  
語法|意義
----|----
`i`|進入編輯模式
esc 鍵|回到一般模式
`:`|進入命令模式
`:wq`|進入命令模式後，儲存並離開
`:q!`|進入命令模式後，強制離開

## nano 相關用法
`nano file_name.txt`：開啟視窗編輯 file_name.txt
  
語法|意義
----|----
`Ctrl + V`|移動到上一頁
`Ctrl + Y`|移動到下一頁
`Ctrl + W`|搜尋文字內容
`Ctrl + X`|離開

## 參考資源
* [Blog：Linux指令集](https://www.pcnet.idv.tw/pcnet/linux/linux_command.htm)
