## 安裝 ORACLE SQL Developer 
1. [建立帳號](https://profile.oracle.com/myprofile/account/create-account.jspx)
2. 進入個人信箱驗證註冊訊息
3. [登入帳密後下載符合電腦規格相應的平台](https://www.oracle.com/tools/downloads/sqldev-downloads.html)
4. 點擊解壓縮後的：sqldeveloper.exe
5. 若先前有安裝過 SQL Developer 可以直接匯入偏好設定，按圖中放大鏡選取即可，或直接選否進行安裝
  
![](https://github.com/yuning-lin/EnvironmentSetup/blob/main/SetUpPic/Oracle_SQL_Developer_download_setting.PNG)
   
## 連線已創建的 DB
1. 點選右上角的綠色＋，以創建連線  
  
![](https://github.com/yuning-lin/EnvironmentSetup/blob/main/SetUpPic/Oracle_SQL_Developer_entering.PNG)
  
2. 依序輸入 DB 的資訊儲存後連線（可以勾選儲存密碼）
  
![](https://github.com/yuning-lin/EnvironmentSetup/blob/main/SetUpPic/Oracle_SQL_Developer_building_new_connection.PNG)
   
## 用 python 連線（windows）
1. `pip install cx_Oracle`
2. [下載並解壓縮 Oracle Basic Client](https://www.oracle.com/database/technologies/instant-client/winx64-64-downloads.html)
    * 檔名範例：instantclient-basic-windows.x64-21.3.0.0.0.zip
3. 若出現 **cx_Oracle.DatabaseError: DPI-1047** 則須加入第一行程式碼，印出版號即為連線成功。  
      
    ```python
    import cx_Oracle
    
    cx_Oracle.init_oracle_client(lib_dir=r"your_path/instantclient_19_12")
    dsn_tns = cx_Oracle.makedsn(ORACLE_DB_IP, ORACLE_DB_PORT, ORACLE_DB_SERVICENAME)
    connection = cx_Oracle.connect(
                                    user = ORACLE_DB_USERNAME,
                                    password = ORACLE_DB_PASSWORD,
                                    dsn = dsn_tns
                                    )
    
    # show the version of the Oracle Database
    print(connection.version)
    ```
  
4. 用 pandas 取出資料
    * 當資料不大，可以使用
    ```python
    query = f"""select * from {ORACLE_DB_NAME}.{TABLE_NAME}"""
    df = pd.read_sql(query, con=connection)
    connection.close()
    ```
    * 當資料大時，可以使用
    ```python
    query = f"""select * from {ORACLE_DB_NAME}.{TABLE_NAME}"""
    ref = pd.read_sql_query(query, con=connection, chunksize=1000)
    data_list = [i for i in ref]
    df = pd.concat(data_list).reset_index(drop=True)
    connection.close()
    ```
## resources
* [cx-oracle 官方文件](https://cx-oracle.readthedocs.io/en/latest/user_guide/installation.html)
* [Interacting with Oracle from Pandas](http://www.jtrive.com/interacting-with-oracle-from-pandas.html)
* [cx_Oracle.DatabaseError: DPI-1047: Cannot locate a 64-bit Oracle Client library](https://stackoverflow.com/questions/56119490/cx-oracle-error-dpi-1047-cannot-locate-a-64-bit-oracle-client-library)
