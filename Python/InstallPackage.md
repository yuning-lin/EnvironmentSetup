## 模組安裝方法
* 利用 pip
* 手動安裝
## 利用 pip
進入命令提示字元或 bash shell 後激活虛擬環境再用 pip 進行安裝  
* 命令提示字元：`cd python39/Scripts/` 到資料夾下 `activate`  
* bash shell：`source python39/Scripts/activate`  
  
以 wheel 版本 0.34.1 為例：
意義|指令
----|----
安裝指定版本套件|`pip install wheel==0.34.1`
強制降級套件版本|`pip install --force-reinstall wheel==0.34.1`
升級套件|`pip install --upgrade wheel`
卸載套件|`pip uninstall wheel`
確認套件是否有安裝|`pip show wheel`
列出所有套件及版本|`pip list`
將套件打包成文件|`pip freeze > 文件名（如 requirements.txt）`
打包成文件的套件一次安裝|`pip install -r requirements.txt`
打包成文件的套件一次卸載|`pip uninstall -r requirements.txt`
  
### pip 問題錦集
* 若是升級 pip 後，遇到 `No module named pip` 而無法使用 pip
  * `python -m ensurepip`
* 在安裝套件遇到 `Consider using the --user option or check the permissions.`
  * `pip install --user wheel`
* 在安裝套件遇到 `ERROR: Command errored out with exit status 1: python setup.py egg_info Check the logs for full command output.`
  * `pip install --upgrade setuptools`
  * `pip install --upgrade pip`

## 手動安裝
若使用 pip 失敗，再嘗試用手動安裝  
手動安裝下列以 `pyhdf` 這個套件為例    
1. 至官方網站[下載](https://pypi.org/project/pyhdf/#files)符合自己 python 版本的 .whl  
2. 確認下載檔案須符合 pip 支援的檔名，不符合則需更名  
```python
import wheel.pep425tags as w # wheel 版本為 0.34.1 才有 pep425tags
print(w.get_supported("amd64")) # 視本機為"amd64"或"win32"做選填，印出支援的檔名
```
  
  * 將版號後的字元以下列組合做更動
  * 原檔名為：pyhdf-0.10.3-cp39-cp39-manylinux2014_x86_64.whl 
  * 更檔名為：pyhdf-0.10.3-cp39-cp39-win_amd64.whl
  
```
[('cp39', 'cp39', 'win_amd64'), ('cp39', 'none', 'win_amd64'), ('cp39', 'none', 'any'), 
  ('cp3', 'none', 'any'), ('cp38', 'none', 'any'), ('cp37', 'none', 'any'), ('cp36', 'none', 'any'), 
  ('cp35', 'none', 'any'), ('cp34', 'none', 'any'), ('cp33', 'none', 'any'), ('cp32', 'none', 'any'), 
  ('cp31', 'none', 'any'), ('cp30', 'none', 'any'), ('py3', 'none', 'win_amd64'), ('py39', 'none', 'any'), 
  ('py3', 'none', 'any'), ('py38', 'none', 'any'), ('py37', 'none', 'any'), ('py36', 'none', 'any'), 
  ('py35', 'none', 'any'), ('py34', 'none', 'any'), ('py33', 'none', 'any'), ('py32', 'none', 'any'), 
  ('py31', 'none', 'any'), ('py30', 'none', 'any')]
```
3. 同樣激活虛擬環境後，用 pip 安裝 .whl 檔：
  * `pip install C:/Users/ning_lin/Downloads/pyhdf-0.10.3-cp39-cp39-win_amd64.whl`

