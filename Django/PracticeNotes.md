## Debug Mode
錯誤訊息
* `django.core.exceptions.AppRegistryNotReady: Apps aren't loaded yet.`
```python
import os
import django

os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'ft_scheduling.settings')
django.setup() # 先於 import test_app.models

from test_app.models import ClassA
```
* `ModuleNotFoundError: No module named 'your_project_name.settings'`
```python
# Example (Unix Bash shell):
export DJANGO_SETTINGS_MODULE=mysite.settings

# Example (Windows shell):
set DJANGO_SETTINGS_MODULE=mysite.settings
```

參考資源
* [Video：Setting up Django Development in Eclipse with Code Complete and Graphical Debugging](https://vimeo.com/5027645)
* [Doc：Django settings¶](https://django.readthedocs.io/en/stable/topics/settings.html)


## URL 捕獲器
一般設置如下方範例，捕獲 URL 的方式有二：
* path：較新版本 Django 才出現的 function，可以使用尖括號來捕獲 URL 中的值
   * 其他常見的型別有：
      * `<int:variable>`：捕獲正整數。
      * `<str:variable>`：捕獲除了路徑分隔符（'/'）以外的任何字符串。
      * `<slug:variable>`：捕獲由 ASCII 字母或數字以及連字符或下劃線組成的字符串。
      * `<uuid:variable>`：捕獲格式化為UUID的字符串。
      * `<path:variable>`：捕獲任何非空字符串，包括路徑分隔符。
* re_path：較舊版本 Django 就有的 function，利用正則表達式捕獲 URL 中的值
* 注意：不論使用 path 或 re_path，最後一定要有 "/" 結尾，才不會有 404 的錯誤
  
django_prj/django_prj/urls.py 範例：  
```python
from django.contrib import admin
from django.urls import path, re_path

from appA.views import funcA
from appB.views import funcB

urlpatterns = [
    path("admin/", admin.site.urls),
    re_path("^api/appA/(?P<year>[0-9]{4})/$", funcA),
    path("api/appB/<int:year>/", funcB),
]
```
  
以上捕獲器對應的 django_prj/appB/views.py 撰寫範例：  
```python
import os

import django
from django.http import JsonResponse

os.environ.setdefault("DJANGO_SETTINGS_MODULE", "django_prj.settings")
django.setup()

from appB import Article
def funcA(request, year):

    article = Article(year)
    article.main()

    return JsonResponse(article.return_msg)
```

## 常見問題
* 跑沒有返回任何錯誤：可藉由 `python manage.py makemigrations` 的錯誤訊息查找
* log 在 settings.py 設定完了卻沒有實際寫入：在執行主檔加入以下程式  
   ```python
   import os
   import django
   
   os.environ.setdefault("DJANGO_SETTINGS_MODULE", "project_name.settings")
   django.setup()
   ```

## 聚合
概念  
* aggregate：返回聚合值
* annotate：返回 querySet，並將聚合值存於 querySet
  
參考資源
* [Docs：聚合](https://docs.djangoproject.com/zh-hans/4.1/topics/db/aggregation/)
* [Blog：aggregate和annotate方法使用详解与示例](https://zhuanlan.zhihu.com/p/50974992)

## QuerySet by Model
* 提取 model 內容
```python
from app.models import UserData

UserData._meta.fields
UserData._meta.get_fields() # 同上
UserData._meta.get_field('Name') # 取出 field 是 Name 的資料
```
* 變更 model 內容
```python
update_values = {"is_manager": False}
new_values = {"name": "Bob", "age": 25, "is_manager":True}

# In this case, if the UserData already exists, its existing name is preserved
obj, created = UserData.objects.get_or_create(
        identifier=identifier, defaults={"name": name}
)

# In this case, if the UserData already exists, its name is updated
obj, created = UserData.objects.update_or_create(
        identifier=identifier, defaults={"name": name}
)
if created:
    obj.update(**new_values)
```

## Customized Commands Management（argparse）
* mycommand.py
```python
import argparse
from django.core.management.base import BaseCommand

class Command(BaseCommand):
    help = 'My custom command'

    def add_arguments(self, parser):
        parser.add_argument('-m', '--message', type=str, help='A custom message')

    def handle(self, *args, **options):
        message = options.get('message')
        if message:
            print(message)
        else:
            print('No message specified')

```
* CMD：`python manage.py mycommand --message "Hello, world!"`

## Multiple Database
* test_app/models.py
```python
class ModelA(models.Model):
    class params:
        db = 'default'

class ModelB(models.Model):
    class params:
        db = 'otherdb'
    ...
```

* test_app/dbrouters.py
```python
import test_app.models
allmodels = dict([(name.lower(), cls) for name, cls in test_app.models.__dict__.items() if isinstance(cls, type)])
...
class MyDBRouter(object):

    def db_for_read(self, model, **hints):
        """ reading model based on params """
        return getattr(model.params, 'db')

    def db_for_write(self, model, **hints):
        """ writing model based on params """
        return getattr(model.params, 'db')

    def allow_migrate(self, db, app_label, model_name = None, **hints):
        """ migrate to appropriate database per model """
        model = allmodels.get(model_name)
        return(model.params.db == db)
```
* test_app/settings.py
```python
DATABASE_ROUTERS = ('test_app.dbrouters.MyDBRouter',)
...
DATABASES = {
    'default': {
        ....
    }
    'otherdb': {
        ....
    }
}
```
* CMD
```linux
python3 manage.py migrate test_app --database default
python3 manage.py migrate test_app --database otherdb
```

## Sorting Data From Model
* 法一：（負號表：descending）
```python
class ModelA(models.Model):
    ...
    class Meta:
        ...
        ordering = ["column1", "-column2"]
```
* 法二：
```python
MyModel.objects.all().order_by("column1", "-column2")
```

參考資源
* [Doc：QuerySet API reference](https://docs.djangoproject.com/en/dev/ref/models/querysets/#get)
* [Doc：Multiple databases](https://docs.djangoproject.com/en/3.0/topics/db/multi-db/#database-routers)
* [ithelp：Models & Admin](https://ithelp.ithome.com.tw/articles/10201074)
* [ithelp：Repository 設計模式(Python)](https://ithelp.ithome.com.tw/articles/10282153?sc=iThomeR)
* [Blog：How to Create Custom Django Management Commands](https://simpleisbetterthancomplex.com/tutorial/2018/08/27/how-to-create-custom-django-management-commands.html)

