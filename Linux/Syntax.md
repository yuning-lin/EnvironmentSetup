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
`echo "This is a test." > ./test.txt`|創建內容為 This is a test. 至當前目錄下的 test.txt
`cat ./test.txt`|顯示當前目錄下 test.txt 的檔案內容
`curl -O https://s3-ap-northeast-1.amazonaws.com/sqlite-demo-data/gapminder.csv`|下載該網站之 gapminder.csv

## VM 工作執行相關用法
語法|意義
----|----
`htop`|顯示當前執行的工作項目、CPU 及 Memory 等使用情況
`nohup python3 app.py &`|在後台用 python3 執行 app.py
`crontab -e`|看所有正在執行中的 process
`ps aux \| grep A`|列出執行中名字有 A 的 process
`kill process_id`|關掉指定 process_id 的 process

## tmux 相關用法
* [參考教學文件](https://blog.gtwang.org/linux/linux-tmux-terminal-multiplexer-tutorial/)  
  
語法|意義
----|----
`sudo apt install tmux`|Ubuntu Linux 安裝 tmux
`man tmux`|tmux 使用手冊
`tmux ls`|列出所有在執行的 session
`tmux a -t session_name`|追蹤該 session_name 運行狀況


## vim 相關用法
語法|意義
----|----
`i`|編輯文字
esc 鍵|存檔
`:wq`|儲存並離開
`q!`|強制離開
