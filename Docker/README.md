## 簡介
### Docker 重點名詞關係
|名稱|概念|譬喻|
|----|----|----|
|repository（倉庫）|存放各種模板的倉庫|眾多商品的購物網|
|image（映像檔）|打包各種服務的模板|將箱子裡的電視機拆封並插好電源|
|container（容器）|真正提供服務的虛擬機|可看節目的電視機|

## Virtual Machine VS Container
|名稱|概念|譬如想吃舒肥雞|
|----|----|----|
|Virtual Machine|把 CPU、內存、網卡、顯卡等虛擬化 > 建立作業系統 > 運行應用程式|有機器設備、廚房、廚師再做出來|
|Container|不會虛擬硬體，和宿主共用 > 用 Docker Engine 做資源隔離 > 運行應用程式|在便利商店買的即食包|

## Docker 優缺點
### 優點：
* 輕量化即主打快速佈署應用，所以運行效率高
* 能建立標準化的環境，讓程式運行更順利
### 缺點：
* 宿主和容器之間在硬體上並非完全切割，故可能會有病毒傳染、搶資源的情形

## 從 docker docs 安裝
1. 前往官網選擇對應系統[下載](https://docs.docker.com/desktop/windows/install/)
2. 點 `Docker Desktop Installer.exe` 兩下進行安裝，預設勾勾保留並重新開機
3. 錯誤訊息：
    1. `Hardware assisted virtualization and data execution protection must be enabled in the BIOS`
        * 以下步驟啟動模擬：
        * 按 `windows+I` > 更新與安全性 > 復原 > 立即重新啟動
        * 重新開機之後會進入「WinRE」的環境 > 疑難排解 > 進階選項 > UEFI 韌體設定
        * 每家主機板商不太一樣，但可以尋找類似選項：Security > Virtualization > Intel Virtualization Technology: On > Intel VT-d Feature: On
        * 可以看見右下角模擬：已停用 --> 已啟用
          
        ![](https://github.com/yuning-lin/EnvironmentSetup/blob/main/SetUpPic/docker_virtualization0.PNG)
          
        ![](https://github.com/yuning-lin/EnvironmentSetup/blob/main/SetUpPic/docker_virtualization1.PNG)
          
    2. `WSL 2 installation is incomplete`
        * 根據 docker 錯誤提示的[連結](https://docs.microsoft.com/zh-tw/windows/wsl/install-manual#step-4---download-the-linux-kernel-update-package)
        * 打開 power shell，將 WSL2 設為預設版本：`wsl --set-default-version 2`

## 從 docker hub 安裝
1. 前往官網[Docker Hub](https://hub.docker.com/)註冊帳號密碼
  
  ![](https://github.com/yuning-lin/EnvironmentSetup/blob/main/SetUpPic/docker_sign_up.PNG)
  
2. 根據需求點選費用選項 > 前往註冊信箱進行驗證
  
  ![](https://github.com/yuning-lin/EnvironmentSetup/blob/main/SetUpPic/docker_fee_options.PNG)
  
3. 根據作業系統下載 Docker（示範案例為 Windows 10）
  
  ![](https://github.com/yuning-lin/EnvironmentSetup/blob/main/SetUpPic/docker_download_by_os.PNG)
