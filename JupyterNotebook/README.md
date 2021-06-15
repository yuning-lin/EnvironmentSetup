## 簡介
Jupter Notebook 是一個 Web-based 的程式開發工具  
可以利用網頁即時反饋數學計算、文字編輯等功能  
本身支援的 kernel 非常多樣化，常見的有 Python、R、C# 等  
在 github 上用 .ipynb 也可以將運行的圖直接帶入 repository  
個人經驗在專案初期使用 Jupyter Notebook 的 cell 區隔不同功能的程式也有不錯的管理程式效果  

## 如何安裝
1. 先安裝 python3.3 以上的版本，步驟可見[此文](https://github.com/yuning-lin/EnvironmentSetup/blob/main/Python/README.md)
2. 使用 Anaconda 或 pip 安裝 Jupter Notebook
```
pip3 install --upgrade pip
pip3 install notebook
```
3. 利用 CMD 鍵入 `jupyter notebook` 或是在 windows --> 開始找到 jupyter notebook 後開啟
  
## 如何使用
開啟後介面如下
  
![](https://github.com/yuning-lin/EnvironmentSetup/blob/main/SetUpPic/JupyterNotebook_UI.PNG)
  
功能大致可以切分如流程圖
```mermaid
graph LR;
    id1(User Interface)-->id2(Notebook Dashboard)
    id1(User Interface)-->id3(Note Editor)
    id2(Notebook Dashboard)-->id4(create files)
    id2(Notebook Dashboard)-->id5(modify files)
    id3(Note Editor)-->id6(edit code)
    id3(Note Editor)-->id7(run code)
```
### Notebook Dashboard
在右上角 New 可以新增 .ipynb 檔案、資料夾等
  
![](https://github.com/yuning-lin/EnvironmentSetup/blob/main/SetUpPic/JupyterNotebook_new_files.png)
  
將檔案做更名、移動、刪除，並且可以藉由檔案顏色辨別是否仍在運行  
  
![](https://github.com/yuning-lin/EnvironmentSetup/blob/main/SetUpPic/JupyterNotebook_rename_files.png)
  
### Note Editor
基本運行功能可以用點選 ICON 執行或是另行點選選單  
  
![](https://github.com/yuning-lin/EnvironmentSetup/blob/main/SetUpPic/JupyterNotebook_editor_icon.png)
  
```mermaid
graph LR;
    id1(儲存檔案)---id2(新增 cell)
    id2(新增 cell)---id3(剪下 複製 貼上 cell)
    id3(剪下 複製 貼上 cell)---id4(上下移動 cell)
    id4(上下移動 cell)---id5(執行 中斷 cell)
    id5(執行 中斷 cell)---id6(重啟 kernel)
    id6(重啟 kernel)---id7(重啟 kernel 並執行整個 notebook)
    id7(重啟 kernel 並執行整個 notebook)---id8(更改 cell 類型)
    id8(更改 cell 類型)---id9(開啟命令選單)
```
#### 快捷鍵：
  
快捷鍵|功能
-----|-----
shift + enter|執行並新增 cell 於下方
ctrl + /|註解程式內容
ctrl + enter|執行指定 cell

#### 選單常用功能：
* 另存檔案成 .py
  
![](https://github.com/yuning-lin/EnvironmentSetup/blob/main/SetUpPic/JupyterNotebook_editor_files.png)
  
* 編輯操作 cell，如指定向上、向下插入 cell
  
![](https://github.com/yuning-lin/EnvironmentSetup/blob/main/SetUpPic/JupyterNotebook_editor_edit.png)

* 運行 cell 並可以改變運行 cell 程是內容為 markdown 語言 
  
![](https://github.com/yuning-lin/EnvironmentSetup/blob/main/SetUpPic/JupyterNotebook_editor_cell.png)
  
* 中止或暫停程式運行
  
![](https://github.com/yuning-lin/EnvironmentSetup/blob/main/SetUpPic/JupyterNotebook_editor_kernel.png)
  
