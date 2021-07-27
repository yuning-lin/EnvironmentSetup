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

