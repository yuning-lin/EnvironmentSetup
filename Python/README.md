## 開始安裝
 [官方連結](https://www.python.org/downloads/)   
python 主要有兩代，python2、python3  
個人主要都使用 python3 居多，故下列示範為安裝 python3   
於「Looking for a specific release?」可以下載指定版本的 python，EX：[3.7.9](https://www.python.org/downloads/release/python-379/)  
根據個人電腦作業系統選擇 windows 或 macOS；其中  
windows 若為 64 位元的選擇「Windows x86-64 executable installer」  
windows 若為 32 位元的選擇「Windows x86 executable installer」 
  
![](https://github.com/yuning-lin/EnvironmentSetup/blob/main/SetUpPic/python_download_option.PNG)
  
小建議：
* 不要下載最新版容易會有版本相容的問題  
* 於一開始的安裝畫面，勾選「Add Python 3.7 to PATH」（將 python 加到環境變數中）  
  
![](https://github.com/yuning-lin/EnvironmentSetup/blob/main/SetUpPic/add_python_to_path.PNG)
* 安裝時維持路徑等預設，遇到問題比較方便查找  

## 安裝確認
要如何知道自己是否安裝成功呢？  
只要在：開始＞命令提示字元＞輸入：python  
並看到以下畫面即表示安裝成功囉～  
  
![](https://github.com/yuning-lin/EnvironmentSetup/blob/main/SetUpPic/CMD.PNG)

## 虛擬環境
因為套件間會有相容性的問題  
一般來說會希望不同專案的環境是分開來的  
除了方便管理外，協作的人也可以快速套用  
下面就來示範如何在「命令提示字元」建立虛擬環境
指令|意義
----|----
which python | 預設的 python 是哪個
where python | python 的路徑在哪裡
virtualenv --python "python path" env3.9 | 建立叫 env3.9 的虛擬環境（建議取有意義的名字）
source ./env3.9/Scripts/activate | 啟動虛擬環境
deactivate | 關閉虛擬環境
## 快速上手
初學者建議根據要使用的套件自行個別安裝  
可以更了解每個套件的使用方式  
不過如果需要快速建立普遍都會使用到的套件模組們可以下載 [Anaconda](https://docs.anaconda.com/anaconda/install/windows/)  
連結裡就有官方安裝教學
但是就切分專案不同版本套件上可能會比較麻煩，還是不建議初學者使用
