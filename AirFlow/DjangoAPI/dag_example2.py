"""
目標：於 airflow 啟動 Django 專案的 API
"""

"""
法二：
因為需要 DAG 維持持續運行的狀態，所以創建一個無限循環的 DAG，
schedule_interval 設置為 @hourly，
通過搭配 retry_delay 和 max_active_runs 等參數來控制持續運行的狀態
多設置 concurrency=1, max_active_runs=1（確保同一時間僅一個實例在運行，避免多次重複啟動 Django API）
"""
from airflow import DAG
from airflow.operators.bash_operator import BashOperator
from datetime import datetime, timedelta

default_args = {
    'owner': 'airflow',
    'depends_on_past': False,
    'start_date': datetime(2023, 9, 1),
    'retry_delay': timedelta(minutes=5),  # 每 5 分鐘重試一次
}

with DAG(
    dag_id="API_EXAMPLE",
    default_args=default_args,
    schedule_interval='@hourly',
) as dag:
    # 使用 BashOperator 啟動 Django API
    API_EXAMPLE_ACTIVATE = BashOperator(
        task_id='API_EXAMPLE_ACTIVATE',
        bash_command="""
        source /path_to_your_virtualenv/bin/activate && \
        cd /path_to_your_django_project && \
        gunicorn your_project_name.wsgi:application --bind 0.0.0.0:8000
        """
    )

    # 其他可以添加的任務，比如啟動後檢查 API 是否運行正常
    API_EXAMPLE_CHECK_STATUS = BashOperator(
        task_id='API_EXAMPLE_CHECK_STATUS',
        bash_command='curl -I http://localhost:8000 || echo "API not running"'
    )

    API_EXAMPLE_ACTIVATE >> API_EXAMPLE_CHECK_STATUS
