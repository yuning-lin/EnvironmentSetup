## 如何使用 py 檔操作
1. 編寫 DAG 的 .py 文件
2. 用 CMD 檢驗指令正確性
      
    指令|意義
    ----|----
    `airflow list_dags`|印出活躍的 DAGs
    `airflow list_tasks Test_DAG`|印出 dag_id 為 Test_DAG 的 tasks 列表
    `airflow list_tasks Test_DAG --tree`|印出 dag_id 為 Test_DAG 階層式的 tasks 列表
    `airflow trigger_dag Test_DAG`|觸發 Test_DAG
    `airflow pause Test_DAG`|暫停 Test_DAG
    `airflow unpause Test_DAG`|取消暫停 Test_DAG
    `airflow clear Test_DAG`|清空 Test_DAG 狀態
    `airflow test Test_DAG task1 2021-05-10`|執行時間為 2021-05-10 **測試** 單個 task 
    `airflow run Test_DAG task1 2021-05-10`|執行時間為 2021-05-10 **運行** 單個 task
    `airflow backfill Test_DAG -s 2021-01-01 -e 2021-05-10`|回補執行任務時間從 2021-01-01 至 2021-05-10
  
3. 在 ~/airflow 路徑下創建 dags 文件夾，置 .py 檔於內即可
4. 監控工作流程在 airflow UI 畫面上運行狀況     

## Operator
利用多種 Operator 組成 DAG 來執行工作流程管理
  
Operator|簡述
----|----
BashOperator|用於在 bash shell 運行 sh script
PythonOperator|用於運行 python 程式碼
EmailOperator|用於發送 email
HTTPOperator|用於發送 http request
SqlOperator|用於執行 SQL 語法
DummyOperator|空操作

## Cron Presets
於 DAG 設置 schedule_interval 參數時可以使用
#### 參數意義：
```
* * * * *
| | | | |
| | | | day of week (0 - 6)
| | | month (1 - 12)
| | day of month (1 - 31)
| hour (0 - 23)
minute (0 - 59)
```
#### 參數範例：
參數|意義
----|----
`0 * * * *` | 一小時執行 DAG 一次
`6 0 * * *` | 每天早上六點執行 DAG 一次
`1 0 * * 0` | 每周日凌晨一點執行 DAG 一次
`0 0 1 * *` | 每個月第一天午夜執行 DAG 一次
`0 0 1 1 *` | 每年第一天午夜執行 DAG 一次


## 參考來源
* [airflow Command](https://airflow.apache.org/docs/apache-airflow/stable/cli-and-env-variables-ref.html)
* [airflow Cron Presets](https://airflow.readthedocs.io/en/1.10.14/dag-run.html)
* [airflow 知乎文章](https://zhuanlan.zhihu.com/p/352989254)
* [airflow的安裝和使用 – 完全版](https://codingnote.cc/zh-tw/p/119158/)
