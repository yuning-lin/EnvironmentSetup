## 簡介
python3 有 sqlite3，即可用 py 檔創建資料庫  
但本身並沒有 GUI 圖形操作介面，可以透過安裝 [DB browser for SQLite](https://github.com/sqlitebrowser/sqlitebrowser/releases) 做可視化管理  

## DB browser for SQLite
下載完後雙擊 DB browser for SQLite.exe 即可看到圖形化介面  
建立資料庫：點選新建資料庫 ＞ 輸入資料庫名：sqlite_test ＞ 存檔  
  
![](https://github.com/yuning-lin/EnvironmentSetup/blob/main/SetUpPic/sqlite_gui_create_db.png)
  
建立資料表：資料表輸入：customer_info ＞ 欄位 Add ID、NAME 等並勾選每個欄位的類型與性質 ＞ OK
  
![](https://github.com/yuning-lin/EnvironmentSetup/blob/main/SetUpPic/sqlite_gui_create_table.png)  
  
縮寫|意義
----|----
NN|not null（非空）
PK|primary key（主鍵）
AL|autoincrement（自動遞增）
U|unique（唯一）
  
新增資料：Browse Data ＞ 選取欲編輯的 table ＞ 插入新紀錄［螢光筆處］＞ Write Changes［將資料寫進資料庫］ 
  
![](https://github.com/yuning-lin/EnvironmentSetup/blob/main/SetUpPic/sqlite_gui_create_data.png)  
  
## python 創建資料庫
* 用 sqlite3 建立資料庫，並創建資料表類型與性質  
```python
import sqlite3
conn = sqlite3.connect('sqlite_test2.db')
c = conn.cursor()
c.execute('''
          CREATE TABLE customer_info
              (
              ID INT PRIMARY KEY     NOT NULL,
              NAME           TEXT    NOT NULL,
              AGE            INT     NOT NULL
              )
          ;
          ''')
conn.commit()
conn.close()
```
* INSERT：建立資料
```python
import sqlite3
conn = sqlite3.connect('sqlite_test2.db')
c = conn.cursor()
c.execute("INSERT INTO customer_info (ID,NAME,AGE) \
           VALUES (1, 'Anna', 16)")
c.execute("INSERT INTO customer_info (ID,NAME,AGE) \
           VALUES (2, 'Joe', 15)")
c.execute("INSERT INTO customer_info (ID,NAME,AGE) \
           VALUES (5, 'Ben', 22)")
conn.commit()
conn.close()
```
* UPDATE：更新資料
```python
import sqlite3
conn = sqlite3.connect('sqlite_test2.db')
c = conn.cursor()
c.execute("UPDATE customer_info set AGE = 18 where ID=5")
conn.commit()
conn.close()
```
* DELETE：刪除資料
```python
import sqlite3
conn = sqlite3.connect('sqlite_test2.db')
c = conn.cursor()
c.execute("DELETE from customer_info where ID=5")
conn.commit()
conn.close()
```
* SELECT：獲取資料表
```python
import sqlite3
conn = sqlite3.connect('sqlite_test2.db')
table = conn.execute("SELECT ID, NAME, AGE from customer_info")
for row in table:
    print(row)
```
獲取結果如下：  
```
(1, 'Anna', 16)
(2, 'Joe', 15)
```
