## 如何啟用 Airflow API
1. 改設定：airflow.cfg 中 > enable_experimental_api = True
2. 驗證 API 是否已經啟用：直接訪問 http://<your-airflow-server>:8000/api/your_api/

## 注意
* 在開發環境可以使用：`python /path/to/your/django/manage.py runserver 0.0.0.0:8000`
* 在正式環境盡量使用：`gunicorn your_project_name.wsgi:application --bind 0.0.0.0:8000`
