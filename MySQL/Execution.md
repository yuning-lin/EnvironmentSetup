## 如何執行 MySQL
* 透過黑窗 MySQL Command Line Client 執行
* 透過圖示介面如 Workbench、HeidiSQL 執行
* 透過 python 或其他程式語言間接執行

>**本文件主軸為如何用 python 連結資料庫並存取資料**
## 套件：sqlalchemy
### ORM 簡介
ORM 物件關聯對映（Object Relational Mapping）  
即用程式語言去操作資料庫語言  
個人覺得最大的優點就是：  
1. 如果換資料庫了，程式語言不太需要更動也可以操作
2. 可以減少資料庫語言的撰寫

當然有優點就會有缺點，因為多了一層語言轉換，就會損失一點效能  
這次介紹的 sqlalchemy 就是一個具 ORM 功能的套件  
據我目前的認知，由於其並非資料庫的 driver，本身並無連接資料庫的功能  
除了安裝 sqlalchemy 外，還需另外安裝 mysql-connector-python  

### 所需套件
```bash
pip install pandas
pip install mysql-connector-python
pip install sqlalchemy
pip install sqlalchemy-utils # 確認 DB 是否存在等的套包
pip install cymysql # INSERT 中文編碼才不會出問題（預設的 mysqldb 只單純 INSERT 英文資料沒問題）
```

## 套件：pymysql
用 SQL 語言在 Python 執行  
相對於 sqlalchemy 少一層語言的轉換，效能上可能會好點  
但是這語法就會受限於需用在 mysql 的系統  
### 所需套件
```bash
pip install pymysql
pip install cryptography
```

## 範例程式
* [sqlalchemy](https://github.com/yuning-lin/EnvironmentSetup/blob/main/MySQL/MySQL_sqlalchemy.ipynb)
* [pymysql](https://github.com/yuning-lin/EnvironmentSetup/blob/main/MySQL/MySQL_pymysql.ipynb)
* [pyodbc](https://github.com/yuning-lin/EnvironmentSetup/blob/main/MySQL/MySQL_pyodbc.ipynb)
