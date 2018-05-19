from django.db import models
from django.utils.html import format_html

# Create your models here.
class BookInfo(models.Model):
    btitle = models.CharField(max_length=20, verbose_name="名字")
    bpub_date = models.DateTimeField(verbose_name='日期')

    # 1. 这里不写，在后台管理系统中数据库每个item的显示时会为一个对象: "HeroInfo Object"
    def __str__(self):
        return self.btitle

class HeroInfo(models.Model):
    hname = models.CharField(max_length=10, verbose_name="名字")
    hgender = models.BooleanField()
    hcontent = models.CharField(max_length=1000, default="", verbose_name='内容')
    hbook = models.ForeignKey(BookInfo, verbose_name='来自于书籍')

    def content(self):
        return self.hcontent

    def hgender(self):
        if self.hgender:
            return '男'
        else:
            return '女'

    def book(self):
        return self.hbook.btitle

    hgender.short_description = '性别'

    #1. 这里不写，在后台管理系统中数据库每个item的显示时会为一个对象: "HeroInfo Object"
    def __str__(self):
        return self.hname

    class Meta:
        ordering = ['id']

