'''
Created on 2021年11月15日

@author: Ning_Lin
'''
from datetime import datetime, timedelta
import pendulum
from airflow import DAG
from airflow.operators.bash_operator import BashOperator
from loguru import logger


default_args = {
    "owner": "someone",  # DAG 擁有者的名稱，如上一篇說明的，通常是負責實作這個 DAG 的人員名稱
    "depends_on_past": False,  # 每一次執行的 Task 是否會依賴於上次執行的 Task，如果是 False 的話，代表上次的 Task 如果執行失敗，這次的 Task 就不會繼續執行
    "start_date": datetime(2021, 1, 21).replace(
        tzinfo=pendulum.timezone("Asia/Taipei")
    ),  # Task 從哪個日期後開始可以被 Scheduler 排入排程
    "email": ["airflow@example.com"],  # 如果 Task 執行失敗的話，要寄信給哪些人的 email
    "email_on_failure": False,  # 如果 Task 執行失敗的話，是否寄信
    "email_on_retry": False,  # 如果 Task 重試的話，是否寄信
    "retries": 0,  # 最多重試的次數
    "retry_delay": timedelta(minutes=10),  # 每次重試中間的間隔
    # 'end_date': datetime(2020, 2, 29), # Task 從哪個日期後，開始不被 Scheduler 放入排程
    # 'execution_timeout': timedelta(seconds=300), # Task 執行時間的上限
    # 'on_failure_callback': some_function, # Task 執行失敗時，呼叫的 function
    # 'on_success_callback': some_other_function, # Task 執行成功時，呼叫的 function
    # 'on_retry_callback': another_function, # Task 重試時，呼叫的 function
}

workspace_root = "path/your_workspace"
projects_root = {"project_name": f"{workspace_root}/project_path"}
projects_pythonenv = {"project_name": f"source {workspace_root}/project_path/env3.6/bin/activate"}

'''
1. define tasks with functions
2. run tasks with command lines
3. control data pipeline with DAG with scheduled time
4. use >> to define workflow.
    In this case, function_a and function_b run simultaneously, then go to function_c 
5. put airflow_example.py under AIRFLOW_HOME directory
'''
def function_a(*args, **kwargs):
    logger.info("function_a")

    cmd = f"python3.6  {projects_root['project_name']}/project_path/dag_a_file.py \
        --start_date=2020-10-01 \
        --end_date=2020-12-31"
    command_line = f"{projects_pythonenv['project_name']}; {cmd}"
    return command_line

def function_b(*args, **kwargs):
    logger.info("function_b")

    cmd = f"python3.6  {projects_root['project_name']}/project_path/dag_b_file.py \
        --start_date=2020-10-01 \
        --end_date=2020-12-31"
    command_line = f"{projects_pythonenv['project_name']}; {cmd}"
    return command_line

def function_c(*args, **kwargs):
    logger.info("function_c")

    cmd = f"python3.6  {projects_root['project_name']}/project_path/dag_c_file.py \
        --start_date=2020-10-01 \
        --end_date=2020-12-31"
    command_line = f"{projects_pythonenv['project_name']}; {cmd}"
    return command_line


with DAG(
    dag_id="project_name",
    default_args=default_args,
    schedule_interval="0 0 1 * *",
) as dag:
    function_a = BashOperator(
        task_id="function_a",
        bash_command=function_a(),
        task_concurrency=1,
        provide_context=True,
    )
    function_b = BashOperator(
        task_id="function_b",
        bash_command=function_b(),
        task_concurrency=1,
        provide_context=True,
    )
    function_c = BashOperator(
        task_id="function_c",
        bash_command=function_c(),
        task_concurrency=1,
        provide_context=True,
    )

    # define workflow
    function_a >> function_c
    function_b >> function_c
