## 簡介
為不同專案建立客製的虛擬環境  
避免全部專案都使用同一環境的套件衝突  
紀錄 python 常用的虛擬環境設置方法  

## virtualenv
必須先下載 python 後才可以使用  
以下以 Git Bash 為例：
1. 安裝套件：`pip3 install virtualenv`
2. 指定虛擬環境 python 版本並命名為 env_test：`virtualenv --python "C:\Users\username\AppData\Local\Programs\Python\Python36\python.exe" env_test`
4. 激活虛擬環境後可以安裝某專案指定套件：`source env_test/Script/activate`
5. 解除虛擬環境：`deactivate`

## venv
* 安裝最新且是乾淨的 python 版本：`python -m venv env_test`
* 若同時有 python2、python3，可以指定：`python3 -m venv env_test`
* 激活虛擬環境後可以安裝某專案指定套件：`source env_test/Script/activate`
* 解除虛擬環境：`deactivate`

## pyenv
#### Windows
1. 取得 pyenv-win
  
|情境|PowerShell or Git Bash|CMD|
|---|---|---|
|若已經下載過 python|`pip install pyenv-win --target $HOME/.pyenv`|`pip install pyenv-win --target %USERPROFILE%\.pyenv`|
|使用 Git 取得|`git clone https://github.com/pyenv-win/pyenv-win.git "$HOME/.pyenv"`|`git clone https://github.com/pyenv-win/pyenv-win.git "%USERPROFILE%\.pyenv"`|
|自行[下載](https://github.com/pyenv-win/pyenv-win/archive/master.zip)安裝|`mkdir $HOME/.pyenv`<br>將下載檔案（pyenv-win-master.zip）解壓縮後<br>複製 pyenv-win 整個資料夾至 `$HOME/.pyenv`|`mkdir %USERPROFILE%\.pyenv`<br>將下載檔案（pyenv-win-master.zip）解壓縮後<br>複製 pyenv-win 整個資料夾至 `%USERPROFILE%\.pyenv`|
  
注：
* PowerShell or Git Bash 下 > 輸入 `$HOME` > 即會跳到該路徑
* 按住 windows 再按 E > 在路徑輸入 `%USERPROFILE%` > 即會跳到該路徑

2. 打開 PowerShell 複製以下程式以添加 PYENV、PYENV_HOME、PYENV_ROOT 至環境變數
```
[System.Environment]::SetEnvironmentVariable('PYENV',$env:USERPROFILE + "\.pyenv\pyenv-win\","User")
[System.Environment]::SetEnvironmentVariable('PYENV_ROOT',$env:USERPROFILE + "\.pyenv\pyenv-win\","User")
[System.Environment]::SetEnvironmentVariable('PYENV_HOME',$env:USERPROFILE + "\.pyenv\pyenv-win\","User")
```
3. 同樣在 PowerShell 複製以下程式以添加下面路徑至 USER PATH 中，才可以使用 pyenv 的指令
```
[System.Environment]::SetEnvironmentVariable('path', $env:USERPROFILE + "\.pyenv\pyenv-win\bin;" + $env:USERPROFILE + "\.pyenv\pyenv-win\shims;" + [System.Environment]::GetEnvironmentVariable('path', "User"),"User")
```
4. 重啟得以開始使用 pyenv
5. pyenv 常用語法
  
|意義|語法|
|---|---|
|列出所有 pyenv 支援的 python 版本|`pyenv install -l`|
|過濾 pyenv 支援指定的 python 版本|`pyenv install -l \| findstr 3.8`|
|安裝 pyenv 單個或多個指定的 python 版本|`pyenv install 3.5.2 3.6.8`|
|設置指定的 python 版本為全域版本，前提是尚未設置區域版本|`pyenv global 3.5.2`|
|設置指定的 python 版本為當前資料夾的區域版本，不同於虛擬環境，不需激活|`pyenv global 3.5.2`|
|解除安裝指定的 python 版本|`pyenv uninstall 3.5.2`|
|列出當前使用的 python 版本|`pyenv version`|
|列出系統所有安裝過的 python 版本|`pyenv versions`|
|解除或安裝 python 套件時重新連結|`pyenv rehash`|
|列出所有存在的虛擬環境|`pyenv virtualenvs`|
|指定虛擬環境 python 版本並命名為 env_test|`pyenv virtualenv 3.6.8 env_test`|
|激活虛擬環境|`pyenv activate env_test`|
|解除虛擬環境|`pyenv deactivate`|
|刪除虛擬環境|`pyenv uninstall env_test`|
|絕對路徑安裝套件|`/home/user/.pyenv/versions/env-test/bin/python -m pip install XXXX`|

## 參考來源
* [官方：Pyenv for Windows](https://github.com/pyenv-win/pyenv-win#manually-check-the-settings)
