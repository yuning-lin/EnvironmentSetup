## 情境一（update or insert）
若新資料 primary key 沒有出現過，則新增該筆資料  
若新資料 primary key 已經出現過，則更新該筆資料  
  
```mysql
MERGE db_name..table_name as t
USING (Values(?,?,?,?)) AS s(pri_key, col1, col2, col3)
ON t.pri_key = s.pri_key 
WHEN MATCHED 
    THEN UPDATE SET 
        t.col1 = s.col1,
        t.col2 = s.col2,
        t.col3 = s.col3
WHEN NOT MATCHED BY TARGET 
    THEN INSERT (pri_key, col1, col2, col3)
         VALUES (s.pri_key, s.col1, s.col2, s.col3;
```
