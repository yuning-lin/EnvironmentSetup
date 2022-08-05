## 情境
想要讓電腦持續監控某資料夾  
當資料夾出現新的檔案時  
執行指定的 .py 檔  

## 步驟
1. 安裝 `inotify-tools` 監控檔案的各種變動，以觸發對應動作
  ```
  # Ubuntu
  sudo apt install inotify-tools
  ```
2. 撰寫監控及觸發動作於 .sh 檔
   
  |語法|意義|
  |----|----|
  |`inotifywait`|監看指定檔案變動情形|
  |`-d`|以背景執行 inotifywait|
  |`-m`|讓 inotifywait 持續監看|
  |`-r`|讓 inotifywait 遞迴監看|
  |`-o`|讓 inotifywait 監看的事件訊息輸出於指定檔案|
  |`--format`|自訂輸出訊息格式|

## 語法範例
```bash
# 持續監看 /tmp 夾下的檔案
inotifywait -m /tmp

# 持續監看 /tmp 夾下及其子目錄所有的檔案
inotifywait -m -r /tmp

# 持續監看 /tmp 夾下的檔案並於檔案變動時輸出以逗號分隔（%e）的變動檔名（%w）
inotifywait -m --format "%:e %w" /tmp

# 持續監看 /tmp 夾下被建立或移入的檔案
inotifywait -m -e create -e moved_to /tmp

# 持續監看 /tmp 夾下被建立或移入的檔案，變動時將事件訊息輸出於 events.log
inotifywait -m -e create -e moved_to -o events.log /tmp

# 背景執行持續監看 /tmp 夾下的檔案，變動時將事件訊息輸出於 events.log
inotifywait -m -d -o events.log /tmp
```

## 完整應用範例：.sh
```bash
'''
監控 monitored_folder 是否有新建或移入的檔案
有則將新建或移入的檔案名稱、路徑、新建或移入的時間記錄於 monitor.log
以及指定 python 環境觸發對應動作的螢幕輸出、錯誤輸出記錄於 monitor.log
'''

inotifywait -m $1 -e create -e moved_to /monitored_folder |
    while read path action file; do
        echo "The file '$file' appeared in directory '$path' via '$action' at '$(date '+%Y/%m/%d %H:%M:%S')'" | tee -a monitor.log
        /home/test/.pyenv/versions/3.6.10/envs/env-test/bin/python /home/test/src/main.py $1 $2 | tee -a monitor.log
    done
```

## 參考資源
* [B：Bash 程式設計教學與範例：inotify-tools 監控檔案變動、觸發處理動作](https://officeguide.cc/bash-tutorial-inotify-tools-file-system-monitoring/)
