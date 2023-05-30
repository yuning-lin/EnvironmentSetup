## 錯誤訊息一
```
[Microsoft][ODBC SQL Server Driver]COUNT 欄位不正確
```
* 檢查欄位和對應的表間是否有多或少
* 特別要注意在 python 填入文字訊息的方式，單引號、雙引號的用法是否會導致訊息斷行造成欄位不正確

## 錯誤訊息二
```
(pyodbc.OperationalError) ('HYT00', '[HYT00] [Microsoft][ODBC Driver 18 for SQL Server]Login timeout expired (0) (SQLDriverConnect)')
(Background on this error at: https://sqlalche.me/e/14/e3q8)
```
* 使用 sqlalchemy 遇到連線資訊有特殊字元會出現此錯誤
* 使用 `from urllib.parse import quote_plus`，EX：`quote_plus(PWD)` 帶入連線資訊
* [參考連結](https://stackoverflow.com/questions/1423804/writing-a-connection-string-when-password-contains-special-characters)
