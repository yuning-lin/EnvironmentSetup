## 簡介
HeidiSQL 為支援多種資料庫的圖型化界面  
在官網上看到包含：MariaDB, MySQL, Microsoft SQL, PostgreSQL and SQLite  
[官網主頁](https://www.heidisql.com/)
## 開始安裝
[官方下載連結](https://www.heidisql.com/download.php?download=installer)  
按照預設安裝執行即可
## 如何使用
1. 連結資料庫：開啟 HeidiSQL ＞ 點選左下角 add 的下三角 ＞ 在根目錄新增工作階段（W）
  
![](https://github.com/yuning-lin/EnvironmentSetup/blob/main/SetUpPic/heidi_step1_add_new_session.PNG)
  
2. 開啟資料庫：設置欲連線的資料庫 ＞ 儲存 ＞ 開啟
  
![](https://github.com/yuning-lin/EnvironmentSetup/blob/main/SetUpPic/heidi_step2_before_setting.PNG)
![](https://github.com/yuning-lin/EnvironmentSetup/blob/main/SetUpPic/heidi_step2_after_setting.PNG)
  
3. 建立資料庫：在 HeidiSQL 介面中 localhost ＞ 右鍵建立新的（O） ＞ 資料庫（U） ＞ test
  
![](https://github.com/yuning-lin/EnvironmentSetup/blob/main/SetUpPic/heidi_step3_open_interface.png)
  
4. 手動點選建立資料表：點選 test ＞ 右鍵建立新的（O） ＞ 資料表（V） ＞ test1
  
![](https://github.com/yuning-lin/EnvironmentSetup/blob/main/SetUpPic/heidi_step4_create_table_by_click.png)
  
5. 執行程式建立資料表：點選 test ＞ 查詢 ＞ 貼上 SQL 指令 ＞ RUN（F9）
    * 最下方會出現執行正確或錯誤
    * 執行完在資料庫 test ＞ 右鍵更新，即可見新表 test2
    * 查詢 ＞ ctrl + s ＞ SQL 指令存成 .sql 檔
  
![](https://github.com/yuning-lin/EnvironmentSetup/blob/main/SetUpPic/heidi_step5_create_table_by_run.png)
