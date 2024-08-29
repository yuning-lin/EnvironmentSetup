## 情境
當 airflow 架設在 A 機台，但是想要管控的專案在 B 機台  

### 設置 SSH 連接
#### Web UI 設定 
1. 登錄 Airflow 的 Web UI 界面
2. 點選頂部選單的 Admin > 點選 Connections
3. 點選加號（Add a new record）
    * Conn Id: 自行命名，是後續在 SSHOperator 會使用到的 ssh_conn_id，EX：server_b。
    * Conn Type: 選擇 SSH。
    * Host: 填寫 B 機台的 IP 地址或主機名。
    * Schema: 可以留空。
    * Login: 填寫登錄 B 機台所需的用户名。
    * Password: 填寫登錄 B 機台所需的密碼。
    * Port: 填寫 SSH 端口（通常是 22）。
    * Extra: 如果使用 SSH 密鑰認證，可以在此填寫密鑰文件路徑等額外參數。

#### python 實作
```python
from datetime import datetime, timedelta

from airflow import DAG
from airflow.operators.empty import EmptyOperator
from airflow.providers.ssh.operators.ssh import SSHOperator

default_args = {
    "owner": "your_name",
    "depends_on_past": False,
    "email": ["your_name@gmail.com"],
    "email_on_failure": True,
    "start_date": datetime(2024, 8, 28),
    "retries": 1,
    "retry_delay": timedelta(minutes=5),
}


with DAG(
    dag_id="ProjectName",
    default_args=default_args,
    schedule_interval=f"0 8 * * *",
    catchup=False,
) as dag:
    Project_Start = EmptyOperator(task_id="Project_Start")

    Process = SSHOperator(
        ssh_conn_id="server_b",
        task_id="Process",
        command="/home/.pyenv/versions/env-project/bin/python /home/project_name/src/main.py",
        dag=dag,
        cmd_timeout=240,
    )

    Project_End = EmptyOperator(task_id="Project_End")

    Project_Start >> Process >> Project_End

```
