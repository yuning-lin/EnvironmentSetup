## IDE 介紹
IDE（Integrated Development Environment），可中譯為整合開發環境  
顧名思義就是將多種在程式開發會應用到的工具整合在一起  
python 本身也有 IDE 只是有點陽春...  
坊間現在已經有很多免費且好用的 IDE  
選一個順手的對於新手來說更是事半功倍  
這邊介紹一個歷史算頗久的 IDE  
不僅可以拿來編輯 python 還可以拿來編輯 JAVA  
個人覺得他 DEBUG 的功能蠻強大的  
有興趣的可以跟著下面的步驟安裝看看  

## 開始安裝
1. [python 官方下載連結](https://www.python.org/downloads/)（安裝後 eclipse 才能對接 python）
2. [JAVA 官方下載連結](https://github.com/ojdkbuild/ojdkbuild/blob/master/README.md)（需先安裝 JAVA 才能安裝 Eclipse）  
3. [Eclipse 官方下載連結](https://www.eclipse.org/downloads/)（windows 根據位元選擇下載版本，EX：64 位元下載檔名為 x86_64.msi 結尾）  
4. 點選 eclipse-inst-win64.exe ＞ 選擇「Eclipse IDE for Eclipse Committers」＞ INSTALL ＞ ACCEPT ＞ LAUNCH  
  
![](https://github.com/yuning-lin/EnvironmentSetup/blob/main/SetUpPic/eclipse_committers.PNG)  
  
4. 設定工作空間：選取個人工作空間路徑＞LAUNCH
5. 安裝 PyDev：Help > Install New Software...＞ 點選 Add...＞ 視窗中 Name 輸入「pydev」，Location 輸入「http://www.pydev.org/updates」 ＞ 勾選欲安裝欄位 ＞ Next ＞ Accept  
  
![](https://github.com/yuning-lin/EnvironmentSetup/blob/main/SetUpPic/install_pydev.png)![](https://github.com/yuning-lin/EnvironmentSetup/blob/main/SetUpPic/optional_columns.png)

## 軟體設置
1. 進入 IDE 介面：於介面上方點選 Window ＞ Perspective ＞ Open Perspective ＞ Other… ＞ 點選 PyDev
  
    ![](https://github.com/yuning-lin/EnvironmentSetup/blob/main/SetUpPic/enter_eclipse_interface1.png)![](https://github.com/yuning-lin/EnvironmentSetup/blob/main/SetUpPic/enter_eclipse_interface2.png)  
  
2. 選定 python 環境：於介面上方點選 Window ＞ Preferences ＞ 左方列表點選 PyDev ＞ Interpreters ＞ Python Interpreter
    * 使用預設 python 環境：選右方 Config first in PATH，出現 Python，在點選下方 Apply and Close
      
    ![](https://github.com/yuning-lin/EnvironmentSetup/blob/main/SetUpPic/choose_python_env.PNG)  
      
    * 使用客製虛擬環境：用 [CMD 創建虛擬環境](https://github.com/yuning-lin/EnvironmentSetup/tree/main/Python#%E8%99%9B%E6%93%AC%E7%92%B0%E5%A2%83)後，選右方 Browse for python/pypy exe，出現 python.exe，在點選下方 Apply and Close > 在 Selection needed 點選 Select All
      
    ![](https://github.com/yuning-lin/EnvironmentSetup/blob/main/SetUpPic/choose_python_env2.png)  
      
    * 在創建新專案時點選 eclipse 已存取的虛擬環境可立即使用
      
3. 調整編碼：於介面上方點選 Window ＞ Preferences ＞ 打關鍵字 en ＞ General ＞ Editors ＞ Workspace ＞ UTF-8  
     
    ![](https://github.com/yuning-lin/EnvironmentSetup/blob/main/SetUpPic/change_encoding.PNG)
      
4. 安裝套件：於介面上方點選 Window ＞ Preferences ＞ 左方列表點選 PyDev ＞ Interpreters ＞ Python Interpreter ＞ 點選指定的 python 環境 ＞ manage with pip ＞ 輸入欲安裝的套件  
    
    ![](https://github.com/yuning-lin/EnvironmentSetup/blob/main/SetUpPic/manage_with_pip.PNG)![](https://github.com/yuning-lin/EnvironmentSetup/blob/main/SetUpPic/install_pkg.PNG)  
    
## 新手上路
跟著做到這裡就可以開始新的專案囉～  
建立專案：於介面上方點選 File ＞ New ＞ PyDev Project ＞ 輸入專案名稱、點選 python 環境 ＞ Finish  
  
![](https://github.com/yuning-lin/EnvironmentSetup/blob/main/SetUpPic/create_new_project.PNG)  
  
建立新檔：於專案名點右鍵 ＞ New ＞ PyDev Module ＞ 輸入檔名 ＞ Finish  
  
![](https://github.com/yuning-lin/EnvironmentSetup/blob/main/SetUpPic/create_new_py.png)  
  
除錯模式：於欲除錯的行數旁邊雙擊，出現小綠點 ＞ 點擊小蟲 ＞ 進入除錯模式［圖片螢光筆圖示］  
除錯顯示：於介面上方點選 Window ＞ Show View ＞ Other ＞ Debug ＞ Debug［可以執行多個 DEBUG 程序顯示於左列］
  
![](https://github.com/yuning-lin/EnvironmentSetup/blob/main/SetUpPic/debug_mode.PNG)  
  
## 解除安裝
知道怎麼安裝，也得知道怎麼解除安裝  
有幾次出了問題無解就是靠重新安裝才恢復 IDE 正常使用  
參照以下刪除步驟即可解除安裝  
1. 開始 ＞ 找到 eclipse 後右鍵開啟檔案位置 ＞ 至上層刪掉整個 eclipse 的資料夾
2. 開始 ＞ 找到 eclipse 後右鍵刪除
3. 桌面 ＞ 刪除 eclipse 捷徑
4. C:\Users\User_name\ ＞ 刪除 .p2 資料夾並刪除帶有 eclipse 的所有資料夾

## 參考網址
[基礎教學 PDF](https://www.cs.ccu.edu.tw/~naiwei/cs5812/Eclipse-IDE.pdf)  
[基礎教學 WEB](http://tw.gitbook.net/eclipse.html)  
  
