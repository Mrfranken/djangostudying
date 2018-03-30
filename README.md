
chapter | status
---|---
Django入门（代码test1） | Done
Django模型（代码test2） | Doing 还有几个小问题（查询方式需要巩固）
row 3 col 1 | row 3 col 2

- ### 在线教程
```
https://code.ziqiangxuetang.com/django/django-tutorial.html
```

- ### 一些第三方的whl库
```
https://www.lfd.uci.edu/~gohlke/pythonlibs/#lxml
```

- ### 开发流程
```
step1: 创建虚拟环境
step2: 安装django
step3: 创建项目
step4: 创建应用
step5: 在models.py中定义模型类
step6: 定义视图
step7: 配置url
step8: 创建模板
```

- ### Django如何重设Admin密码
```python
#忘记密码时
python manage.py shell

from django.contrib.auth.models import User 
user = User.objects.get(username='admin') 
user.set_password('new_password') 
user.save()
```

```python
#用户名密码都忘记时
from django.contrib.auth.models import User
user = User.objects.get(pk=1)
user.set_password('your_new_password')
user.save()
quit()
```