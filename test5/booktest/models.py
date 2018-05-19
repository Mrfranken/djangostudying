from django.db import models

# Create your models here.
class UserInfo(models.Model):
    uname = models.CharField(max_length=10)
    upwd = models.CharField(max_length=40)
    isDelete = models.BooleanField(default=False)
    person_pic = models.ImageField(upload_to='person/', verbose_name='个人照片', default='无')

    def _uname(self):
        return self.uname

    def _upwd(self):
        return self.upwd

    # 改变后台页面显示时默认的字段 uname --> '名字'  upwd --> '密码'
    _uname.short_description = '名字'
    _upwd.short_description = '密码'

# class PersonInfo(models.Model):
