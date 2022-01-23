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
