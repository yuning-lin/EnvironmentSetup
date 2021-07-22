## 如何執行 MySQL
* 透過黑窗 MySQL Command Line Client 執行
* 透過圖示介面如 Workbench、HeidiSQL 執行
* 透過 python 或其他程式語言間接執行
>**本文件主軸為 python 連結資料庫的套件介紹**

## Command Line Client
語法|意義
----|----
`mysql -u your_username -h your_host_ip -p`|輸入左列語法再輸入密碼即連接 mySQL
`show databases;`|顯示 database 目錄
`use your_dbname;`|顯示指定 DB

* 顯示指定 DB 內所有表名、資料筆數  

  * 故若資料量大時對 TABLE 進行操作後可能無法立即反應實際資料筆數  
  注意：[Columns in TABLES that represent table statistics hold cached values.](https://dev.mysql.com/doc/refman/8.0/en/information-schema-tables-table.html)  
  ```mysql
  SELECT table_name, table_rows
  FROM INFORMATION_SCHEMA.TABLES
  WHERE TABLE_SCHEMA = 'your_dbname';
  ```
  * 反應大 TABLE 實際資料筆數仍需透過下列語法  
  ```mysql
  SELECT COUNT(*) 
  FROM your_dbname.your_table_name;
  ```

* 刪除 TABLE  
  * 刪除 DB 內所有 TABLE
  ```mysql
  SELECT CONCAT('DROP TABLE IF EXISTS `', table_name, '`;')
  FROM INFORMATION_SCHEMA.TABLES
  WHERE TABLE_SCHEMA = 'your_dbname';
  ```
  * 刪除 DB 指定 TABLE
  ```mysql
  DROP TABLE your_dbname.your_tablename
  ```


* 顯示指定表的欄位屬性
```mysql
SELECT 
TABLE_CATALOG,
TABLE_SCHEMA,
TABLE_NAME, 
COLUMN_NAME, 
DATA_TYPE,
CHARACTER_MAXIMUM_LENGTH
FROM INFORMATION_SCHEMA.COLUMNS
where TABLE_NAME = 'your_tablename'
```

* DB 權限查詢的相關指令（實際差異需另外查詢）
```mysql
SELECT * 
FROM information_schema.user_privileges;
```
```mysql
SELECT * 
FROM information_schema.SCHEMA_PRIVILEGES;
```


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

## 套件：pyodbc
簡化連接 ODBC（open database connectivity）databases 
### 所需套件
```bash
pip install pyodbc
```

## 範例程式
* [sqlalchemy](https://github.com/yuning-lin/EnvironmentSetup/blob/main/MySQL/MySQL_sqlalchemy.ipynb)
* [pymysql](https://github.com/yuning-lin/EnvironmentSetup/blob/main/MySQL/MySQL_pymysql.ipynb)
* [pyodbc](https://github.com/yuning-lin/EnvironmentSetup/blob/main/MySQL/MySQL_pyodbc.ipynb)
