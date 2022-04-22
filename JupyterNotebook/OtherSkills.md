## Shell Commands
在 Jupyter Notebook 可以在兩處用 Shell Commands 執行 py 檔：
1. .ipynb 的 cell 內
    * `!python your_code.py`
    *  但此時只會在 Jupyter Notebook 預設環境下執行
3. 在 Notebook Dashboard 開啟的 terminal 內
    * `source bin/activate` 激活指定虛擬環境
    * `python your_code.py`
 
 其他 cell 內指令：
 指令|意義
 ---|---
 `%matplotlib notebook`|拖曳縮放 cell output 內圖形
 `%matplotlib inline`|讓圖形直接畫在 cell output
 `%pip install package_name`|安裝套件
 `!pwd`|秀出當前程式檔路徑
 `!ls`|秀出當前程式檔案夾下所有檔案

## 建立虛擬環境於 Jupyter Notebook
1. 開啟 CMD／Git Bash，建立虛擬環境（以下以 Git Bash 為例）
   * EX：建立名為 py39_torch 的虛擬環境
   * 指令：`virtualenv --python C:/Users/user_name/AppData/Local/Programs/Python/Python39/python.exe py39_torch`
2. 激活虛擬環境
   * EX：激活名為 py39_torch 的虛擬環境
   * 指令：`source py39_torch/Scripts/activate`
3. 創建該虛擬環境於 Jupyter Notebook
   * 該虛擬環境需先安裝 `pip install ipykernel`
   * 指令：`python -m ipykernel install --user --name py39_torch --display-name "py39_torch"`
   * 註：
      * --name 是 Jupyter 在內部使用的名稱
      * --display-name 是 notebook menus 會看到的名稱
      * 此指令會覆蓋任何具有相同名稱的現有 kernel
   * 在 UI 介面的 New 即可在新虛擬環境創建 .ipynb，如圖
     
   ![](https://github.com/yuning-lin/EnvironmentSetup/blob/main/SetUpPic/JupyterNotebook_create_env_menu.PNG)
4. 查看與刪除虛擬環境選項
   * EX：查看有哪些虛擬環境
   * 指令：`jupyter kernelspec list`
   * EX：刪除指定虛擬環境 py39_torch
   * 指令：`jupyter kernelspec uninstall py39_torch`
## 如何 debug
1. 利用套件 `pdb`、`IPython` 的 `set_trace()` 下中斷點
2. run cell 即可進入 debug 模式，cell 也會顯示正在運行 `[*]`
3. 搭配互動式的介面，如綠框處，建入相應的指令完成需求
  
  ![](https://github.com/yuning-lin/EnvironmentSetup/blob/main/SetUpPic/JupyterNotebook_debug_mode1.PNG)
   
4. 指令範例，如圖紅框處：
  
   指令|意義
   ---|---
   `n`|運行到下一行
   `c`|運行後續所有程式
   `h`|叫出指令表
   
  ![](https://github.com/yuning-lin/EnvironmentSetup/blob/main/SetUpPic/JupyterNotebook_debug_mode2.PNG)
    
