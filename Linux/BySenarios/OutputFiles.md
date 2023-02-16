## Linux tee 檔案輸出
### 範例
```
# 搜尋當前目錄下 *.sh 的檔案並寫入 out.txt
find ./ -name "*.sh" > out.txt

# 搜尋當前目錄下 *.sh 的檔案視窗顯示並寫入 out.txt
find ./ -name "*.sh" | tee out.txt

# 搜尋當前目錄下 *.sh 的檔案視窗顯示並以添加的方式寫入 out.txt
find ./ -name "*.sh" | tee -a out.txt

# 顯示 error_file 檔案內容，但無此檔的錯誤訊息於視窗顯示並以添加的方式寫入 out.txt
cat error_file 2>&1 | tee -a out.txt
```

## 參考資源
* [Blog：Linux tee 同時螢幕標準輸出和輸出到檔案用法與範例](https://shengyu7697.github.io/linux-tee/)
* [Blog：Linux Command 「2>&1」 輕鬆談](https://mks.tw/2928/%E5%AD%B8%E7%BF%92%E7%AD%86%E8%A8%98-linux-command-%E3%80%8C21%E3%80%8D-%E8%BC%95%E9%AC%86%E8%AB%87)
