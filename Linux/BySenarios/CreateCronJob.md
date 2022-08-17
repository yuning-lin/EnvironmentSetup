## 情境
可以從 [Crontab – Quick Reference](https://www.adminschoice.com/crontab-quick-reference) 知道 cron、crontab、cron job 的差別  
cron job 設置需遵從固定格式：`* * * * *`  
以下模擬一新例行性工作該如何進行設置

## 步驟
1. 進入 Linux
2. 輸入 `crontab -e` 進入編輯區
3. 按 `i` 開始編輯
4. 輸入 `*/5 * * * * /home/env-test/bin/python /home/test/main.py` 設置每五分鐘跑一次用虛擬環境跑一次 main.py
5. 按 `Ctrl + C` 離開編輯
6. 輸入 `:wq` 進入命令模式後存檔並離開

## 資源
* [Cron Job 時間設定](https://crontab.guru/)
