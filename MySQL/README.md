## Windows 開始安裝
[Windows 官方下載連結](https://dev.mysql.com/downloads/windows/installer/)   
下面選項按 download  
  
![](https://github.com/yuning-lin/EnvironmentSetup/blob/main/SetUpPic/mysql_download_option.PNG)  
  
可以選擇不要註冊，點選下面小小的「No thanks, just start my download.」 
  
![](https://github.com/yuning-lin/EnvironmentSetup/blob/main/SetUpPic/mysql_download_signup.PNG)  
  
選擇 developer default 即可  
  
![](https://github.com/yuning-lin/EnvironmentSetup/blob/main/SetUpPic/mysql_setup_type.PNG)  
  
靜候安裝完按 next    

![](https://github.com/yuning-lin/EnvironmentSetup/blob/main/SetUpPic/mysql_installation.PNG)  
  
初次使用維持預設設定即可  
  
![](https://github.com/yuning-lin/EnvironmentSetup/blob/main/SetUpPic/mysql_typeNnetworking.PNG)

開始設置根密碼，盡量不要設太弱  

![](https://github.com/yuning-lin/EnvironmentSetup/blob/main/SetUpPic/mysql_account_setting.PNG)
  
並加入使用者名稱、密碼  

![](https://github.com/yuning-lin/EnvironmentSetup/blob/main/SetUpPic/mysql_adduser.PNG)
  
可以勾選開機時自動開啟，省去再去開他的麻煩  
  
![](https://github.com/yuning-lin/EnvironmentSetup/blob/main/SetUpPic/mysql_windows_service.PNG)  
  
最後按 execute，router configuration 可以不必打勾，初始有根帳密即可  
  
![](https://github.com/yuning-lin/EnvironmentSetup/blob/main/SetUpPic/mysql_apply_configuration.PNG)  
  
![](https://github.com/yuning-lin/EnvironmentSetup/blob/main/SetUpPic/mysql_router_configuration.PNG)
  
輸入根密碼按 check 後執行，看到 installation complete，基本上就完成了安裝囉～  
根據使用習慣勾選要開啟的介面，這邊我選 Workbench（可以不用另外再下載圖型化界面）  

![](https://github.com/yuning-lin/EnvironmentSetup/blob/main/SetUpPic/mysql_connect_to_server.PNG)

點選 localhost 方框輸入根密碼即可進入使用畫面如圖示  
  
![](https://github.com/yuning-lin/EnvironmentSetup/blob/main/SetUpPic/mysql_start_workbench.PNG)

![](https://github.com/yuning-lin/EnvironmentSetup/blob/main/SetUpPic/workbench_user_interface.PNG)  

## Mac 開始安裝
1. [官方下載頁面](https://dev.mysql.com/downloads/mysql/)
2. 選取相應版本後，示範選 dmg 下載 > 點選 `No thanks, just start my download.`
  
  ![](https://github.com/yuning-lin/EnvironmentSetup/blob/main/SetUpPic/mysql_mac_download.png)
  
3. 打開下載檔案進行安裝 > 為 root 設置密碼 > 安裝完成
4. 打開終端機 > 切換至根目錄 > 編輯 bash_profile
  ```
  cd ~
  vim ./.bash_profile
  ```
5. 按 i 進行 insert 環境變數 > esc > wq 寫入後離開
  ```
  export PATH=$PATH:/usr/locol/mysql/bin
  export PATH=$PATH:/usr/local/mysql/support-files
  ```
6. 系統偏好設定 > 點選 mysql > 可以更改路徑並套用
  ![](https://github.com/yuning-lin/EnvironmentSetup/blob/main/SetUpPic/mysql_mac_system_preference.png)
  ![](https://github.com/yuning-lin/EnvironmentSetup/blob/main/SetUpPic/mysql_mac_configuration.png)
7. 開啟終端機 > `mysql -u root -p` 如看到 `sh:command not found: mysql`
    * 每次輸入： `alias mysql=/usr/local/mysql/bin/mysql` > `mysql -u root -p`
    * 永久更改：
       1. 更改檔案：`cd ~` > `vim ~/.bashrc` > 添加 `alias mysql=/usr/local/mysql/bin/mysql` > esc > wq
       2. 重啟終端機：source ~/.bashrc > mysql
  ![](https://github.com/yuning-lin/EnvironmentSetup/blob/main/SetUpPic/mysql_mac_terminal_activate.png)
## 其他圖型化界面
* [HeidiSQL 安裝教學](https://github.com/yuning-lin/EnvironmentSetup/tree/main/HeidiSQL)
