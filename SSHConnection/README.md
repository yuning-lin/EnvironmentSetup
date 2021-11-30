## 安裝
1. 至[ PuTTY 官網](https://www.chiark.greenend.org.uk/~sgtatham/putty/latest.html)下載符合本地端相應的規格  
2. 用 PuTTYgen 創建 .ppk
3. 利用 .ppk 及管理者提供帳密等連線到遠端伺服器
  
## 管理者須提供
* 機器名稱或 IP
* 登入帳號及密碼
* 私鑰（private key）id_rsa 檔
  
## Windows 環境實作
### 創建 .ppk
1. 搜尋＞PuTTYgen＞Load
2. 選取右下 All Files(*.*)＞點選指定 id_rsa 檔＞開啟＞確定
3. 點選 Save private key＞在 PuTTYgen Warning 點是
4. 填寫檔案名稱，EX：開發環境_port號_名字＞存成 .ppk 檔
  
  ![](https://github.com/yuning-lin/EnvironmentSetup/blob/main/SetUpPic/ssh_create_ppk.PNG)
   
### 遠端伺服器連線
1. 搜尋＞PuTTY
2. 先至左列 Connection＞Data＞Auto-login username 填上管理者提供的帳號名稱
3. 再至左列 Session＞輸入管理者提供的 Host Name / IP Address、Port＞Saved Sessions 填上管理者提供的名稱＞Save
4. 再至左列 Connection＞SSH＞Auth＞Browse 選擇剛創建的 .ppk 檔
5. 再至左列 Session＞Save
6. 正中 Default Settings 下會出現剛剛儲存的 Saved Sessions＞在該名稱上左鍵點擊兩下即可連線
  
  ![](https://github.com/yuning-lin/EnvironmentSetup/blob/main/SetUpPic/ssh_connect_server.PNG)
   
