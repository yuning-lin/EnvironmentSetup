## 簡介
2021 最新 Mac Ｍ1 pro 晶片在 python3.8- 有許多 Python 套件沒有支援   
目前已知深度學習至少都要 python3.6+   
所以以下嘗試以相對穩定 python3.9 做安裝


## 安裝步驟
1. 前往 python 官網下載目前 stable release 最新的 python3.9.9
2. 點 `macOS 64-bit universal2 installer` 下載好並開始安裝
3. 出現需要安裝 Rosetta，點選安裝後就自動安裝 python
  ![](https://github.com/yuning-lin/EnvironmentSetup/blob/main/SetUpPic/python_install_rosetta.png)
4. 預設路徑：/Applications/Python 3.9/
  

## 常用終端機語法
|語法|意義|
|----|----|
|`python3 -V`|印出 python3 版本|
|`python3.9 -m pip install --user --upgrade pip`|更新 pip 至最新版本|
|`python3.9 -m pip install --user virtualenv`|安裝套件 virtualenv|
|`virtualenv env3.9 --python=python3.9`|用 python3.9 建立一個名叫 env3.9 的虛擬環境|
|`source env3.9/bin/activate `|激活虛擬環境 env3.9|
  

## 添加 python 至路徑
`WARNING：'/Users/user_name/Library/Python/3.9/bin' which is not on PATH.`
1. `vi ~/.bash_profile`：開啟添加路徑的文件
2. 按 `i` 表插入
3. 鍵入 `export "PATH=/Users/ninglin/Library/Python/3.9/bin:$PATH"`
4. 輸入路徑後，按 `Esc` 键退出编輯
5. 按 `:`，並输入 `wq` 保存後即可退出
6. 透過重啟終端機；或透過 `source ~/.bash_profile` 重新加載
