## Debug/Run Configurations
Python 一些套件（EX：Typer、Flask、Django 等）可以將執行指令參數等打包，在命令列執行時可以帶入參數等  
以下設置可以將基本參數做指定代入以執行 Debug 的動作，Run 也有自己的 Configurations，做一樣的設置即可  
1. 打開執行主檔 .py 文件
2. 在想要的行號前點擊兩次設置中斷點
3. 在上方的導航欄中，選擇 "Run" -> "Debug Configurations"
4. 在彈出的視窗中，在 "Main" 標籤下：
    *  "Project" 欄位選擇該專案
    *  "Main Module" 欄位選擇執行主檔 .py 文件位置。
5. 在彈出的視窗中，在 "Arguments" 標籤下：
    * "Program arguments" 中，輸入執行所需參數
6. 點擊 "Apply" 保存你的配置
7. 點擊 "Debug" 來開始 debug
