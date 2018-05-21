from django.db import models
from tinymce.models import HTMLField

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


class AreaInfo(models.Model):
    title = models.CharField(max_length=20)
    parea = models.ForeignKey('self', null=True, blank=True)
    # 如果设置null为True，则对于空记录，django会用NULL去填充，默认情况下，django会用空字符串填充
    # blank=True 表示该字段是否可以为空

class HeroInfo(models.Model):
    hname = models.CharField(max_length=10)
    hgender = models.BooleanField(default=True)
    hcontent = HTMLField()
    isDelete = models.BooleanField(default=False)