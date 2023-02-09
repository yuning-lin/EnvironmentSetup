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

參考資源
* [Video：Setting up Django Development in Eclipse with Code Complete and Graphical Debugging](https://vimeo.com/5027645)


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
參考資源
* [Doc：QuerySet API reference](https://docs.djangoproject.com/en/dev/ref/models/querysets/#get)
* [ithelp：Models & Admin](https://ithelp.ithome.com.tw/articles/10201074)
