## 情境
寫好一新的 DAG 該如何放上 UI 操作？

## 步驟
1. 寫好一包好 DAG 的 test.py
2. 於 Ubuntu
    * 先找出在 Ubuntu dag folder 的位置：`airflow dags list`
    * 複製已寫好的 test.py 於 Ubuntu dag folder 的位置：`cp /mnt/c/Users/user_name/AirflowHome/test.py /home/user_name/.local/lib/python3.8/site-packages/airflow/example_dags/`
    * 確認檔案有被放進：`airflow dags list`
    * 若有錯誤可輸入：`airflow dags list-import-errors`
    * 更新新增的 DAG：`airflow scheduler`
3. 同樣在瀏覽器輸入：http://localhost:8080 ，即可看到新增的 DAG

## 參考資源
* [Official：Tutorial](https://airflow.apache.org/docs/apache-airflow/stable/tutorial.html)
