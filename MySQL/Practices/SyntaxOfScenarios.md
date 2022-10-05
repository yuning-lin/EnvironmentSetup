## 情境一（update or insert）
[參考 mssqltips：Using MERGE in SQL Server to insert, update and delete at the same time](https://www.mssqltips.com/sqlservertip/1704/using-merge-in-sql-server-to-insert-update-and-delete-at-the-same-time/)  
若新資料 primary key 沒有出現過，則新增該筆資料  
若新資料 primary key 已經出現過，則更新該筆資料  
  
```mysql
MERGE db_name..table_name as t
USING (Values(?,?,?,?)) AS s(pri_key1, pri_key2, col1, col2, col3)
ON t.pri_key1 = s.pri_key1 and t.pri_key2 = s.pri_key2 
WHEN MATCHED 
    THEN UPDATE SET 
        t.col1 = s.col1,
        t.col2 = s.col2,
        t.col3 = s.col3
WHEN NOT MATCHED BY TARGET 
    THEN INSERT (pri_key1, pri_key2, col1, col2, col3)
         VALUES (s.pri_key1, s.pri_key2, s.col1, s.col2, s.col3);
```
