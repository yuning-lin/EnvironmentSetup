## 簡介
何謂框架（Software Framework）？  
其為軟體提供一套有架構的程式規範  
可以是解決某類問題的類（class）或函數（function）  
不論哪種應用程式，只要有該類問題都能使用該框架  
可以更有效地開發程式  
  
常見的程式對應框架：
* Python --> Django
* JavaScript --> Vue / React / Angular

## 安裝
1. 建議安裝 python3.5+
2. 終端機下載指定版號：`pip install django==3.0.3`
3. 在當前資料夾下建立名為的 HelloWorld 專案：`django-admin startproject HelloWorld .`
4. 建立檔案架構有 HelloWorld 資料夾及夾下檔案、manage.py，說明如下：
    
    名稱|用途
    ----|----
    manage.py|與 HelloWorld 同層，管理專案的連接、啟動等
    HelloWorld/\_\_init\_\_.py|表明 HelloWorld 是一個套件
    HelloWorld/settings.py|設定檔
    HelloWorld/urls.py|定義各個應用程式的網址
    HelloWorld/asgi.py|為 [Asynchronous Server Gateway Interface](https://en.wikipedia.org/wiki/Asynchronous_Server_Gateway_Interface) 的縮寫，用來提供非同步的功能
    HelloWorld/wsgi.py|為 [Web Server Gateway Interface](https://zh.wikipedia.org/zh-tw/Web%E6%9C%8D%E5%8A%A1%E5%99%A8%E7%BD%91%E5%85%B3%E6%8E%A5%E5%8F%A3) 的縮寫，定義 Web server 和 Web App 或框架間的通用介面

5. 終端機：`python manage.py runserver`
6. 將出現於終端機的網址複製於瀏覽器 > 看到成功安裝 Django 的字樣

## 參考資源
* [Blog：程式語言的框架](https://docs.f5ezcode.in/cs-basic/di-ba-zhang-gong-cheng-de-gong-ju/8.2-cheng-shi-yan-de-kuang-jia)
* [Org：Django 介紹](https://developer.mozilla.org/zh-TW/docs/Learn/Server-side/Django/Introduction)
* [Org：Django 教程](https://www.runoob.com/django/django-tutorial.html)
