## 前言
在大資料用 SQL 語法做簡單的前處理  
可以省去很多在 python 得用平行處理的麻煩  
SQL 語法的功能有順序規定  
前後不能顛倒否則無法運行  
順序由上至下如下表
  
### 語法順序
語法|功能|備註
----|----|----
SELECT|欲挑選的欄位|可包含簡單運算，AS 令為欄位代號
FROM|選取的表格|
WHERE|查詢條件|無法搭配聚合函數使用
GROUP BY|分組欄位|
HAVING|組別條件|可以搭配聚合函數使用，如 AVG()、COUNT()、MAX()、MIN()、SUM() 等
ORDER BY|顯示順序|
LIMIT|顯示限制筆數|

* 語法順序－範例  
利用 mysql workbench 內建表格 sakila.address 將上述功能簡易示範  
並且在程式最後須加上分號才能運行  
```mysql
SELECT count(address_id) AS cnt, district
FROM sakila.address
WHERE address LIKE '%Drive%'
   OR address LIKE '%Lane%'
GROUP BY district
HAVING cnt=1
ORDER BY district
LIMIT 10;
```

### 表格合併
![](https://github.com/yuning-lin/EnvironmentSetup/blob/main/SetUpPic/sql_join_table.PNG)

### With as 用法
為將欲選取資料以一般資料表運算式（Common Table Expression, CTE）做暫存的語法  
常見於搭配 UNION ALL 使用，可以讓合併多張表的語法更整潔  
  
* 範例一：將表格欄位重新命名並暫存後再選取
```mysql
WITH City_table (城市ID, 城市名, 國家ID) AS
	(
	 Select city_id, city, country_id
	 from sakila.city
	)

SELECT * 
FROM City_table;
```

* 範例二：引用兩個 CTE 並做 JOIN
```mysql
WITH 
country_table as
(
SELECT country, country_id
FROM sakila.country
),
city_table as
(
SELECT city_id, city, country_id
FROM sakila.city
WHERE city LIKE 'A%' OR city LIKE 'B%'
)

Select *
From country_table A inner join city_table B
on A.country_id = B.country_id;
```

