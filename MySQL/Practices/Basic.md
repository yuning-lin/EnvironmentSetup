### Q1 選取表 Worker FIRST_NAME 並用別名 WORKER_NAME 顯示
```sql
SELECT FIRST_NAME AS WORKER_NAME FROM Worker;
```
### Q2 選取表 Worker FIRST_NAME 並將該欄位內容轉成大寫
```sql
SELECT UPPER(FIRST_NAME) FROM Worker;
```
### Q3 選取表 Worker FIRST_NAME 並去除字串右邊空白
```sql
SELECT RTRIM(FIRST_NAME) FROM Worker;
```
### Q4 選取表 Worker FIRST_NAME 的 a 替換成 A
```sql
SELECT REPLACE(FIRST_NAME,'a','A') FROM Worker;
```
### Q5 選取表 Worker FIRST_NAME 和 LAST_NAME 用空格連接成為 COMPLETE_NAME
```sql
SELECT CONCAT(FIRST_NAME, ' ', LAST_NAME) AS 'COMPLETE_NAME' FROM Worker;
```
### Q6 選取表 Worker 僅列出不同部門
```sql
SELECT DISTINCT(DEPARTMENT) FROM Worker;
```
### Q7 選取表 Worker 並列出不同部門名稱長度
```sql
SELECT DISTINCT length(DEPARTMENT) FROM Worker;
```
### Q8 選取表 Worker FIRST_NAME 為 Amitabh 並僅顯示字母 a 第一個出現的位置
```sql
SELECT INSTR(FIRST_NAME, 'a') FROM Worker WHERE FIRST_NAME='Amitabh';
```
### Q9 選取表 Worker 所有欄位並根據 FIRST_NAME 的字母升序
```sql
SELECT * FROM Worker ORDER BY FIRST_NAME ASC;
```
### Q10 選取表 Worker 所有欄位並根據 FIRST_NAME 的字母升序，DEPARTMENT 的字母降序
```sql
SELECT * FROM Worker ORDER BY FIRST_NAME ASC, DEPARTMENT DESC;
```
### Q11 選取表 Worker FIRST_NAME 為 / 不為 Vipul 或 Satish 的所有欄位
```sql
SELECT * FROM Worker WHERE FIRST_NAME IN ('Vipul','Satish');
SELECT * FROM Worker WHERE FIRST_NAME NOT IN ('Vipul','Satish');
```
### Q12 選取表 Worker DEPARTMENT 為 Ad 開頭的所有欄位
```sql
SELECT * FROM Worker WHERE DEPARTMENT LIKE 'Ad%';
```
### Q13 選取表 Worker DEPARTMENT 為六個字母且結尾為 h 的所有欄位
```sql
SELECT * FROM Worker WHERE DEPARTMENT LIKE '_____h';
```
### Q14 選取表 Worker DEPARTMENT 是 Admin 的資料筆數
```sql
SELECT COUNT(*) FROM Worker WHERE DEPARTMENT = 'Admin';
```
### Q15 選取表 Worker SALARY 介於一萬到五萬的所有欄位
```sql
SELECT * FROM Worker WHERE SALARY BETWEEN 100000 AND 500000;
```
### Q16找出表 Worker 中薪水前三名的所有欄位
```sql
SELECT * FROM Worker ORDER BY Salary DESC LIMIT 3;
```
### Q17 選取表 Worker JOINING_DATE 是 2014 年 2 月的所有欄位
```sql
SELECT * FROM Worker WHERE YEAR(JOINING_DATE) = 2014 AND MONTH(JOINING_DATE) = 2;
```
### Q18 秀出 WORKER_ID 為奇數／偶數的資料
```sql
SELECT * FROM Worker WHERE MOD (WORKER_ID, 2) <> 0;
SELECT * FROM Worker WHERE MOD (WORKER_ID, 2) = 0;
```
### Q19 複製表 Worker 到表 WorkerClone
```sql
CREATE TABLE WorkerClone LIKE Worker;
```
### Q20 顯示現在日期、時間
```sql
SELECT CURDATE();
SELECT NOW();
```










