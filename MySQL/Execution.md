## ORM 簡介
ORM 物件關聯對映（Object Relational Mapping）
即用程式語言去操作資料庫語言
個人覺得最大的優點就是：
    1. 如果換資料庫了，程式語言不太需要更動也可以操作
    2. 可以減少資料庫語言的撰寫
當然有優點就會有缺點，因為多了一層語言轉換，就會損失一點效能
這次介紹的 sqlalchemy 就是一個具 ORM 功能的套件
據我目前的認知，由於其並非資料庫的 driver，本身並無連接資料庫的功能
除了安裝 sqlalchemy 外，還需另外安裝 mysql-connector-python

## 所需套件
```bash
pip install pandas
pip install mysql-connector-python
pip install sqlalchemy
pip install sqlalchemy-utils # 確認 DB 是否存在等的套包
pip install cymysql # INSERT 中文編碼才不會出問題（預設的 mysqldb 只單純 INSERT 英文資料沒問題）
```

