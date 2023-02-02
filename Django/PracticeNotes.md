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
* [Setting up Django Development in Eclipse with Code Complete and Graphical Debugging](https://vimeo.com/5027645)
