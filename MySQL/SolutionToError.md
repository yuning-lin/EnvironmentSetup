### 錯誤訊息
* Case：
  ```
  [Microsoft][ODBC SQL Server Driver]COUNT 欄位不正確
  ```
  * 檢查欄位和對應的表間是否有多或少
  * 特別要注意在 python 填入文字訊息的方式，單引號、雙引號的用法是否會導致訊息斷行造成欄位不正確

* Case：
  ```
  (pyodbc.OperationalError) ('HYT00', '[HYT00] [Microsoft][ODBC Driver 18 for SQL Server]Login timeout expired (0) (SQLDriverConnect)')
  (Background on this error at: https://sqlalche.me/e/14/e3q8)
  ```
  * 使用 sqlalchemy 遇到連線資訊有特殊字元會出現此錯誤
  * 使用 `from urllib.parse import quote_plus`，EX：`quote_plus(PWD)` 帶入連線資訊
  * [參考連結](https://stackoverflow.com/questions/1423804/writing-a-connection-string-when-password-contains-special-characters)

* Case：
  ```
  轉換 expression 到資料類型 int 時發生算術溢位錯誤。
  ```
  * 使用 `select sum(convert(numeric(20,0), column_name)) from table_name` 帶入連線資訊
  * [參考連結](https://www.796t.com/content/1528088531.html)

## 非預期結果
* Case：division returns zero
  ```
  CAST(column_name AS float)
  ```
  * 利用上述方法改變欄位型態
