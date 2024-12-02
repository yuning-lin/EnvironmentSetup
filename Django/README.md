## 簡介
何謂框架（Software Framework）？  
其為軟體提供一套有架構的程式規範  
可以是解決某類問題的類（class）或函數（function）  
不論哪種應用程式，只要有該類問題都能使用該框架  
可以更有效地開發程式  
  
### 常見的程式對應框架：
* Python --> Django / Flask / Tornado
* JavaScript --> Vue / React / Angular

### Django 設計規範
* 可參考多方解釋：
  * [Django 代碼是什麼樣子?](https://developer.mozilla.org/zh-TW/docs/Learn/Server-side/Django/Introduction#django_%E4%BB%A3%E7%A2%BC%E6%98%AF%E4%BB%80%E9%BA%BC%E6%A8%A3%E5%AD%90)
  * [MVC 與 MTV 模型](https://www.runoob.com/django/django-intro.html)
  * [MVC/MTV介紹](https://www.cnblogs.com/wj-1314/p/9406275.html)

* MVC：Model View Controller
  * Model：放和 Database 相關的內容，描述資料類型
  * View：放 HTML、CSS、JS 等前端靜態網頁文件
  * Controller：主要程式撰寫處，定義業務邏輯相關內容、傳遞資料

* MTV：Model Template View
  * Model：放和 Database 相關的內容，描述資料類型
  * Template：放 HTML、CSS、JS 等前端靜態網頁文件
  * View：主要程式撰寫處，定義業務邏輯相關內容、傳遞資料


## 安裝
1. 建議安裝 python3.5+
2. 啟動虛擬環境
3. 終端機：`pip install django==3.0.3`，下載指定版號
4. 終端機：`django-admin --version`，有顯示版號表示安裝成功

## 創建 Django 專案
1. 建立名為 HelloWorld 的資料夾，並 cd 進入夾下
2. 終端機：`django-admin startproject HelloWorld`，在當前資料夾下建立名為的 HelloWorld 專案
3. 建立檔案架構有 HelloWorld 資料夾及夾下檔案、manage.py，說明如下：
    
    名稱|用途
    ----|----
    manage.py|與 HelloWorld 同層，管理專案的連接、啟動等
    HelloWorld/\_\_init\_\_.py|表明 HelloWorld 是一個套件
    HelloWorld/settings.py|設定檔
    HelloWorld/urls.py|定義各個應用程式的網址，並和各 app 裡的 views.py 做對應
    HelloWorld/asgi.py|為 [Asynchronous Server Gateway Interface](https://en.wikipedia.org/wiki/Asynchronous_Server_Gateway_Interface) 的縮寫，用來提供非同步的功能
    HelloWorld/wsgi.py|為 [Web Server Gateway Interface](https://zh.wikipedia.org/zh-tw/Web%E6%9C%8D%E5%8A%A1%E5%99%A8%E7%BD%91%E5%85%B3%E6%8E%A5%E5%8F%A3) 的縮寫，定義 Web server 和 Web App 或框架間的通用介面

4. 終端機：`python manage.py runserver 127.0.0.1:8000`
5. 將 [http://127.0.0.1:8000/](http://127.0.0.1:8000/) 複製於瀏覽器 > 看到成功安裝 Django 的字樣
  
  ![](https://github.com/yuning-lin/EnvironmentSetup/blob/main/SetUpPic/django_successfully_installed.PNG)

## 創建 APP
1. 終端機：`cd HelloWorld/` > `python manage.py startapp greeting`，建立和 manage.py 同層名為 greeting 的 app
2. greeting 資料夾及夾下檔案說明如下：
    
    名稱|用途
    ----|----
    greeting/\_\_init\_\_.py|表明 greeting 是一個套件
    greeting/admin.py|設定 Database 呈現及跟 models.py 溝通的模式等
    greeting/apps.py|識別其為 app 的檔案
    greeting/models.py|放和 Database 相關的內容，描述資料類型
    greeting/tests.py|測試檢查業務邏輯相關內容
    greeting/views.py|主要程式撰寫處，定義業務邏輯相關內容，會和 HelloWorld/urls.py 做呼應傳遞前端頁面
    greeting/migrations/|紀錄 models.py 所創建的資料庫型態
3. **app 間有時須考慮先後順序**，此處將名為 greeting 的 app 新增至 HelloWorld/settings.py 中 INSTALLED_APPS 的最後一個

    ```python
    INSTALLED_APPS = (
        'django.contrib.admin',
        'django.contrib.auth',
        'django.contrib.contenttypes',
        'django.contrib.sessions',
        'django.contrib.messages',
        'django.contrib.staticfiles',
        'greeting.apps.GreetingConfig', # 左邊所列可參考 greeting/apps.py 檔案內容；盡量別用簡寫 'greeting'
    )
    ```
4. 同步資料庫
    1. `python manage.py makemigrations`：根據 greeting/models.py 修改內容建立新的檔案於 migrations 中
    2. `python manage.py migrate`：把 greeting/models.py 存於 migrations 中的修改內容更新至資料庫中
    * 注意：`migrate` 會根據 INSTALLED_APPS 的 app 順序進行更新資料庫
5. 設定管理後臺
    1. `python manage.py createsuperuser`：輸入帳號、Email、密碼等資訊以創建後臺管理者
    2. 在 greeting/admin.py 註冊 greeting/models.py 裡的 YourModel 資訊  
      
        ```python
        from django.contrib import admin
        from .models import YourModel

        admin.site.register(YourModel)
        ```
    3. 前往：http://127.0.0.1:8000/admin，即可看見 YourModel 資訊，有以下兩種方式對資料庫進行新增、刪除、修改等動作
        * 可於網頁直接手動點選操作
        * 另外也可在終端機：`python manage.py shell`，進入 shell 操作  
        
        
          ```python
          from greeting.models import YourModel

          YourModel.objects.all() # 獲取該表所有資料
          YourModel.objects.create(title='***', content='abc') # 新增該筆資料於表 YourModel
          YourModel.objects.get(pk=1) # 讀取 pk=1 的資料
          YourModel.objects.filter(content__contains='a') # 讀取 content 裡有 a 的資料
          YourModel.objects.filter(title="***").update(content='cba') # 修改 title 為 *** 的 content
          YourModel.objects.get(pk=1).delete() # 刪除 pk=1 的資料
          ```

## 創建 templates
* 建立與 manage.py 同層的 templates 資料夾
* Django 在 html 有自己的 Python 語法  
  
  * 呈現變數
  ```python
  <title>{{<variable_name>}}</title>
  ```
  * 迴圈
  ```python
  {% for <element> in <list> %}
  ...
  {% endfor %}
  ```
  * 邏輯判斷
  ```python
  {% if %}
  ... 
  {% else %}
  ...
  {% endif %}
  ```
  * Filters
  ```python
  {{<變數名稱>|<filter功能>:<filter參數>}}
  ```
## 修改設定（EX：HelloWorld/settings.py）
1. 修改語言、時區
    * 預設：
    ```python
    LANGUAGE_CODE = 'en-us'

    TIME_ZONE = 'UTC'
    ```
    * zh-Hant：繁中、zh-Hans：簡中
    ```python
    LANGUAGE_CODE = 'zh-Hant'

    TIME_ZONE = 'Asia/Taipei'
    ```
    * 參考資料：
        * [Blog：時區相關問題](https://www.cnblogs.com/bubu99/p/14774503.html)
        * [Stackoverflow：存取時區](https://stackoverflow.com/questions/29311354/how-to-set-the-timezone-in-django)
      
2. 修改 Database 設定
    * 預設：
    ```python
    DATABASES = {
        'default': {
            'ENGINE': 'django.db.backends.sqlite3',
            'NAME': os.path.join(BASE_DIR, 'db.sqlite3'),
        }
    }
    ```
    * MSSQL：（終端機：`pip install django mssql-django`，安裝 mssql-django）
    ```python
    DATABASES = {
        "default": {
            "ENGINE": "mssql",
            "NAME": "DATABASE_NAME",
            "USER": "USER_NAME",
            "PASSWORD": "PASSWORD",
            "HOST": "HOST_ADDRESS",
            "PORT": "1433",
            "OPTIONS": {"driver": "ODBC Driver 17 for SQL Server", 
            },
        },
    }
    ```
    * MSSQL：（ODBC Driver 版本為 18，[載點](https://learn.microsoft.com/zh-tw/sql/connect/odbc/download-odbc-driver-for-sql-server?view=sql-server-ver16)）
    ```python
    DATABASES = {
        "default": {
            "ENGINE": "mssql",
            "NAME": "DATABASE_NAME",
            "USER": "USER_NAME",
            "PASSWORD": "PASSWORD",
            "HOST": "HOST_ADDRESS",
            "PORT": "1433",
            "OPTIONS": {
                "driver": "ODBC Driver 18 for SQL Server",
                "extra_params": "Encrypt=no",
            },
        },
    }
    ```
3. 修改 templates 路徑
    * 預設：
    ```python
    TEMPLATES = [
        {
            'BACKEND': 'django.template.backends.django.DjangoTemplates',
            'DIRS': [],
            'APP_DIRS': True,
            'OPTIONS': {
                'context_processors': [
                    'django.template.context_processors.debug',
                    'django.template.context_processors.request',
                    'django.contrib.auth.context_processors.auth',
                    'django.contrib.messages.context_processors.messages',
                ],
            },
        },
    ]
    ```
    * MSSQL：（終端機：`pip install django mssql-django`，安裝 mssql-django）
    ```python
    TEMPLATES = [
        {
            'BACKEND': 'django.template.backends.django.DjangoTemplates',
            'DIRS': [os.path.join(BASE_DIR, 'templates').replace('\\', '/')],
            'APP_DIRS': True,
            'OPTIONS': {
                'context_processors': [
                    'django.template.context_processors.debug',
                    'django.template.context_processors.request',
                    'django.contrib.auth.context_processors.auth',
                    'django.contrib.messages.context_processors.messages',
                ],
            },
        },
    ]
    ```
4. 修改 log 內容
    * 預設可參考：
        * [Django logging 官方文件](https://docs.djangoproject.com/en/4.2/topics/logging/)
        * [Package logginf 官方文件](https://docs.python.org/3/library/logging.html#logrecord-attributes)
    * 客製可參考：[Blog：Django 中 的 logging](https://note.qidong.name/2018/11/django-logging/)
    * 遇到重複紀錄 log 文字的情形可參考：[stackoverflow：Duplicate log output when using Django logging module](https://stackoverflow.com/questions/62882552/duplicate-log-output-when-using-django-logging-module)
    * 想定期刪資料 log 的設定可參考：[stackoverflow：Automatically delete logs in Django](https://stackoverflow.com/questions/64412211/automatically-delete-logs-in-django)
    * 範例：
       ```python
        LOGGING = {
            "version": 1,
            "disable_existing_loggers": False,
            "formatters": { # 紀錄 log 的時間、檔名等提示字
                "simple": {
                    "format": "[%(asctime)s][%(levelname)s][%(name)s] %(message)s",
                    "datefmt": "%Y-%m-%d %H:%M:%S",
                },
            },
            "handlers": {
                "console": {
                    "class": "logging.StreamHandler",
                    "formatter": "simple",
                },
                "file": {
                    "level": "INFO",
                    "class": "logging.handlers.TimedRotatingFileHandler",  # 定期刪除 log
                    "filename": f"{BASE_DIR}/log/file.log",
                    "when": "D",  # 以天為單位
                    "interval": 7,  # 七天刪一次
                    "backupCount": 7,  # keep a 7 day history before log deletion
                    "formatter": "simple",
                },
            },
            "loggers": {
                "django": {
                    "handlers": ["console", "file"],
                    "level": "INFO",
                    "propagate": False,  # 避免重複 log 訊息
                },
                "greeting": {
                    "handlers": ["console", "file"],
                    "level": "DEBUG",
                    "level": "INFO",
                    "propagate": False,  # 避免重複 log 訊息
                },
            },
        }

       ```
## 參考資源
* [Docs：Writing your first Django app, part 1](https://docs.djangoproject.com/en/4.1/intro/tutorial01/)
* [Docs：The Django Book](https://django-book.readthedocs.io/en/latest/)
* [Blog：程式語言的框架](https://docs.f5ezcode.in/cs-basic/di-ba-zhang-gong-cheng-de-gong-ju/8.2-cheng-shi-yan-de-kuang-jia)
* [Blog：Django 介紹](https://djangogirlstaipei.gitbooks.io/django-girls-taipei-tutorial/content/django/introduction.html)
* [Org：Django 介紹](https://developer.mozilla.org/zh-TW/docs/Learn/Server-side/Django/Introduction)
* [Org：Django 教程](https://www.runoob.com/django/django-tutorial.html)
* [Org：Django Packages](https://djangopackages.org/)
