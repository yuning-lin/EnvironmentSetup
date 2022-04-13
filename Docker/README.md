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

## 安裝步驟：
1. 前往官網[Docker Hub](https://hub.docker.com/)註冊帳號密碼
  
  ![](https://github.com/yuning-lin/EnvironmentSetup/blob/main/SetUpPic/docker_sign_up.PNG)
  
2. 根據需求點選費用選項 > 前往註冊信箱進行驗證
  
  ![](https://github.com/yuning-lin/EnvironmentSetup/blob/main/SetUpPic/docker_fee_options.PNG)
  
3. 根據作業系統下載 Docker（示範案例為 Windows 10）
  
  ![](https://github.com/yuning-lin/EnvironmentSetup/blob/main/SetUpPic/docker_download_by_os.PNG)
