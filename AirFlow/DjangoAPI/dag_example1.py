"""
目標：於 airflow 啟動 Django 專案的 API
"""

"""
法一：
因為 schedule_interval 設置為 None
所以需要第一次啟用時在 airflow UI 點 Trigger Dag
"""
from airflow import DAG
from airflow.operators.bash_operator import BashOperator
from datetime import datetime

# 定義 DAG 的基本信息
default_args = {
    'owner': 'your_name',
    "email": ["your_name@email.com"],
    'start_date': datetime(2024, 9, 13),
    'retries': 1,
}

with DAG(
    dag_id="API_EXAMPLE",
    default_args=default_args,
    schedule_interval=None,
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
