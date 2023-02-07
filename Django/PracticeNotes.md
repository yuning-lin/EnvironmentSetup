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
