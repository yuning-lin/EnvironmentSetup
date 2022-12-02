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
2. 終端機：`django-admin startproject HelloWorld .`，在當前資料夾下建立名為的 HelloWorld 專案
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
1. 終端機：`python manage.py startapp greeting`，建立和 manage.py 同層名為 greeting 的 app
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
3. **app 間有時須考慮先後順序**，此處將 greeting 新增至 HelloWorld/settings.py 中 INSTALLED_APPS 的最後一個

    ```python
    INSTALLED_APPS = (
        'django.contrib.admin',
        'django.contrib.auth',
        'django.contrib.contenttypes',
        'django.contrib.sessions',
        'django.contrib.messages',
        'django.contrib.staticfiles',
        'greeting',
    )
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

## 參考資源
* [Blog：程式語言的框架](https://docs.f5ezcode.in/cs-basic/di-ba-zhang-gong-cheng-de-gong-ju/8.2-cheng-shi-yan-de-kuang-jia)
* [Org：Django 介紹](https://developer.mozilla.org/zh-TW/docs/Learn/Server-side/Django/Introduction)
* [Org：Django 教程](https://www.runoob.com/django/django-tutorial.html)
