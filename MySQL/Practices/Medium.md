### Q1 薪水是五萬到十萬的工人，印出全名和薪水
```sql
SELECT CONCAT(FIRST_NAME, ' ', LAST_NAME) As COMPLETE_NAME, Salary
FROM Worker 
WHERE WORKER_ID IN 
  (SELECT WORKER_ID FROM Worker 
   WHERE Salary BETWEEN 50000 AND 100000);
```
### Q2 印出不同部門名稱和人數，並以部門人數降序排列
```sql
SELECT DEPARTMENT, count(WORKER_ID) NumOfWorkers 
FROM Worker 
GROUP BY DEPARTMENT 
ORDER BY NumOfWorkers DESC;
```
### Q3 結合表 Title，找出職稱為經理的人
```sql
SELECT W.FIRST_NAME, T.WORKER_TITLE
FROM Worker as W
INNER JOIN Title as T
ON W.WORKER_ID=T.WORKER_REF_ID
AND T.WORKER_TITLE IN ('Manager')
```
### Q4 根據 WORKER_TITLE, AFFECTED_FROM 計算人數，並列出人數大於一的資料
```sql
SELECT WORKER_TITLE, AFFECTED_FROM, COUNT(*)
FROM Title
GROUP BY WORKER_TITLE, AFFECTED_FROM
HAVING COUNT(*) > 1;
```
### Q5 找出薪水一樣但 WORKER_ID 不一樣的資料
```sql
SELECT DISTINCT W.WORKER_ID, W.FIRST_NAME, W.Salary 
FROM Worker W, Worker W1 
WHERE W.Salary = W1.Salary 
AND W.WORKER_ID != W1.WORKER_ID;
```
### Q6 找出第二高薪水
```sql
SELECT MAX(Salary)
FROM Worker
WHERE Salary NOT IN 
	(SELECT MAX(Salary)
	 FROM Worker);
```
### Q7 找出人數少於五人的 DEPARTMENT
```sql
SELECT COUNT(WORKER_ID) AS CNT
FROM Worker
GROUP BY DEPARTMENT
HAVING CNT<5
```
### Q8 找出每個部門薪水最高的所有資訊
```sql
SELECT * 
FROM
	(SELECT MAX(Salary) AS MaxSalary, DEPARTMENT
	 FROM Worker
	 GROUP BY DEPARTMENT) AS W
INNER JOIN Worker
ON W.DEPARTMENT=Worker.DEPARTMENT
AND W.MaxSalary=Worker.SALARY;
```
### 兩張表上下合併
* 保留重複值
```sql
SELECT * FROM table_a
UNION ALL
SELECT * FROM table_b
```
* 不保留重複值
```sql
SELECT * FROM table_a
UNION
SELECT * FROM table_b
```
### 計算比例
```sql
select k1, k2, SUM(qty) as [qty_by_key], SUM(SUM(qty)) OVER () as [total_qty], SUM(qty) / SUM(SUM(qty)) OVER () AS [ratio]
from tb
group by k1, k2
```
### 計算以 k1 為群組、k2 的比例
```sql
select k1, k2, SUM(qty) as [qty_by_key], SUM(SUM(qty)) OVER (PARTITION BY k1) as [total_qty], SUM(qty) / SUM(SUM(qty)) OVER (PARTITION BY k1) AS [ratio]
from tb
group by k1, k2
```
### k1 每一組都插入一筆「k2='AAA', qty_by_key=0」的資料
```sql
SELECT k1, k2, SUM(qty) as [qty_by_key]
FROM tb
WHERE add_date between '2023-01-01' and '2023-03-31'
GROUP BY k1, k2,
UNION ALL
SELECT k1, 'AAA', SUM(0) as [qty_by_key]
FROM tb
WHERE add_date between '2023-01-01' and '2023-03-31'
GROUP BY k1
```

### 篩選各群組前幾名
* ROW_NUMBER() 一定要搭配 over 使用
* ROW_NUMBER() 僅能在 select, order by 出現
```sql
select *
from (
	select top 10 a.*
	from (
		select k1, k2, SUM(qty) as [qty_by_key], SUM(SUM(qty)) OVER (k1) as [total_qty], SUM(qty) / SUM(SUM(qty)) OVER (k1) AS [ratio]
		from tb 
		group by k1, k2
		) as a
		order by ROW_NUMBER() over (partition by k1
					    order by a.ratio desc)
	) as b
order by b.k1, b.ratio desc
```
### 數值格式轉換
```sql
select format(A,'N0'), /* 將數值轉成帶千分位逗號的字串 */
       format(C,'P2')  /* 將數值轉成帶 % 以及取到小數點後兩位的字串 */
from tb
```
### 條件式
```sql
select D = iif(A = '1', B*C, B) /* if A = '1' do B*C, else do B */
from tb
```
### 轉置單一欄位
```sql
SELECT 'AverageCol2' AS AVG_COL2,   
  [0], [1], [2], [3], [4]  
FROM  
(
  SELECT Col1, Col2   
  FROM table1
  WHERE Col3 <> 0
) AS SourceTable  
PIVOT  
(  
  AVG(Col2)  
  FOR Col1 IN ([0], [1], [2], [3], [4])  
) AS PivotTable; 
```
### 條件判斷
```sql
select   
    case   
        when age>=12 and age<24 then 'g1'  
        when age>=24 and age<36 then 'g2'  
        when age>=36 then 'g3'  
    end as age_group  
from table1
```
### 分組排名
* 每個班級按照成績排名
```sql
SELECT RANK() OVER(PARTITION BY class ORDER BY score DESC) AS Rank, name, score, class  
FROM students;
```
### 單行差分
```sql
SELECT time_col, Value, Value - LAG(Value) OVER (ORDER BY time_col) AS Value_Diff
FROM your_table_name;
```
