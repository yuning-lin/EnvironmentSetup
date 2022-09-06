## 情境一
寫好一新的 DAG 該如何放上 UI 操作？

### 步驟
1. 寫好一包好 DAG 的 test.py
2. 於 Ubuntu
    * 先找出在 Ubuntu dag folder 的位置：`airflow dags list`
    * 複製已寫好的 test.py 於 Ubuntu dag folder 的位置：`cp /mnt/c/Users/user_name/AirflowHome/test.py /home/user_name/.local/lib/python3.8/site-packages/airflow/example_dags/`
    * 確認檔案有被放進：`airflow dags list`
    * 若有錯誤可輸入：`airflow dags list-import-errors`
    * 更新新增的 DAG：`airflow scheduler`
3. 同樣在瀏覽器輸入：http://localhost:8080 ，即可看到新增的 DAG

## 情境二
不想刪除 DAG 示範檔，但也不希望其秀在 UI 上，該怎麼做？  
注意：以下方法是所有放至 `/home/user_name/.local/lib/python3.8/site-packages/airflow/example_dags/` 的檔案都不會秀出，即包含自行新增至此的檔案  

### 步驟
```linux
export AIRFLOW__CORE__LOAD_EXAMPLES = False
airflow scheduler
```

## 情境三
如何建立自己的 dag folder？  

### 步驟
* 於 Windows：將 test.py 直接放置 C:\Users\ning_lin\AirflowHome\dags  
* 於 Ubuntu
   1. `nano airflow/airflow.cfg` 修改 dags_folder 的路徑 > ctrl +X > y > enter
      
      ```linux
      [core]
      # The folder where your airflow pipelines live, most likely a
      # subfolder in a code repository. This path must be absolute.
      dags_folder = /mnt/c/Users/user_name/AirflowHome/dags
      ```
   2. 更新參數
      
      ```linux
      airflow db init
      airflow scheduler
      ```

## 參考資源
* [Official：Tutorial](https://airflow.apache.org/docs/apache-airflow/stable/tutorial.html)
