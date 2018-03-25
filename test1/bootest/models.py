from django.db import models

# Create your models here.
class BookInfo(models.Model):
    btitle = models.CharField(max_length=20)
    bpub_date = models.DateTimeField()

    # 1. 这里不写，在后台管理系统中数据库每个item的显示时会为一个对象: "HeroInfo Object"
    def __str__(self):
        return self.btitle

class HeroInfo(models.Model):
    hname = models.CharField(max_length=10)
    hgender = models.BooleanField()
    hcontent = models.CharField(max_length=1000)
    hbook = models.ForeignKey(BookInfo)

    def gender(self):
        if self.hgender:
            return '男'
        else:
            return '女'

    def book(self):
        return self.hbook.btitle

    # gender.short_description = '性别'

    #1. 这里不写，在后台管理系统中数据库每个item的显示时会为一个对象: "HeroInfo Object"
    def __str__(self):
        return self.hname

