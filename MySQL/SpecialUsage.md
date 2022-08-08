## 部分轉置
某表（db..table）某欄位（same_col）相同  
某些欄位（diff_row、diff_row2）值不同  
想把橫列轉直欄併在旁邊一起看

```sql
SELECT T1.same_col, col1, col2
FROM
  (SELECT same_col, diff_row as [col1] FROM db..table where diff_row2 = 'aa') T1
INNER JOIN
  (SELECT same_col, diff_row as [col2] FROM db..table where diff_row2 = 'aa_1') T2
ON T1.same_col=T2.same_col;
```
