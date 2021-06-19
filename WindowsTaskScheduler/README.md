## 簡介
Windows Task Scheduler 在 Windows 繁中版稱為工作排程器  
為 windows 內建的組件無須另外安裝  
利用簡單的語法檔即可以用點選的方式定時執行程式  
適用於簡易單項程式執行，但若是有上下游關係的程式還是建議用 ariflow  

## 如何使用
1. 開始 ＞ 工作排程器
2. 右列：建立工作
    * 一般：填入工作名稱
    * 觸發程序：選填欲執行程式的時間
    * 動作：瀏覽點選執行程式檔，如 .bat 等
    * 條件：勾選電腦執行程式的狀態條件，如插著電時才執行等
    * 設定：其他執行程式更細項的設定，如工作失敗要重跑等
  
![](https://github.com/yuning-lin/EnvironmentSetup/blob/main/SetUpPic/TaskScheduler_create_task.PNG)
  
![](https://github.com/yuning-lin/EnvironmentSetup/blob/main/SetUpPic/TaskScheduler_set_schedule.PNG)
  
![](https://github.com/yuning-lin/EnvironmentSetup/blob/main/SetUpPic/TaskScheduler_choose_bat.PNG)
  
## 建立 .bat 檔
利用 .bat 讓工作排程器執行程式  
* 有一簡易程式 GetTime.py
* CMD ＞ 測試 bat 語法
  
![](https://github.com/yuning-lin/EnvironmentSetup/blob/main/SetUpPic/TaskScheduler_bat_file.PNG)
  
* 記事本 ＞ 貼上寫好的 bat 語法 ＞ 另存成 .bat
  
![](https://github.com/yuning-lin/EnvironmentSetup/blob/main/SetUpPic/TaskScheduler_bat_file_from_note.PNG)
  
## bat 語法
語法|意義
----|----
`cd C:\Users\USER\Downloads`|指定路徑
`virtualenv --python "C:\Users\USER\AppData\Local\Programs\Python\Python37\python.exe" env3.7` |建立虛擬環境
`fsutil file createnew .\env3.7\Lib\site-packages\a.pth 0`  |建立 a.pth 檔
`echo %CD% >> .\env3.7\Lib\site-packages\a.pth` |加入現有路徑為 python path
`call env3.7\Scripts\activate` |激活虛擬環境
`python GetTime.py` |執行 GetTime.py 檔
