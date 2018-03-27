from django.db import models

# Create your models here.

#1. 模型类中定义元类，可以在元类中定义这个表的名字，默认<app_name>_<model_name>
#2. 可以为模型类指定管理器，默认objects。
#   如果想要改写默认管理器返回对象，可以自定义一个类继承管理器去改写默认返回的查询，并在模型类中使用
#============================================================================
#3. 插入数据过于麻烦的问题（每次都要在shell中通过模型类对象调用属性赋值后save来插入数据,其实是
#   创建对象过于麻烦的问题 book = BookInfo()）：
#   在管理器类中创建一个方法通过返回BookInfo对象来插入数据
# Manager管理器在整个系统中就是充当ORM的角色，完成从python代码到sql语句的映射操作
class BookInfoManager(models.Manager):

    def get_queryset(self):
        return super(BookInfoManager, self).get_queryset().filter(isDelete=False)

    #创建对象方法二：
    def create_book(self, btitle, bpub_date):
        book = BookInfo()
        book.btitle = btitle
        book.bpub_date = bpub_date
        book.bread = 0
        book.bcomment = 0
        book.isDelete = False
        return book


class BookInfo(models.Model):
    btitle = models.CharField(max_length=20)
    bpub_date = models.DateTimeField(db_column='pub_date')
    bread = models.IntegerField(default=0)
    bcomment = models.IntegerField(default=0)
    isDelete = models.BooleanField(default=False)

    # BookInfo.objects.all()方法调动的是get_queryset的，所以可以通过复写get_queryset
    # 方法修改默认的查询信息， 原始的BookInfo.objects = models.Manager
    books1 = models.Manager()
    books2 = BookInfoManager()

    class Meta():
        #默认表的名称<app_name>_<model_name>   booktestBookInfo
        db_table = 'bookinfo'
        #ordering = ['id'] #排序会增加数据库的开销?

    #创建对象方法一：
    # @classmethod
    # def create(self, btitle, pub_date):
    #     book = BookInfo
    #     book.btitle = btitle
    #     book.bpub_date = pub_date
    #     book.bread = 0
    #     book.bcomment = 0
    #     book.isDelete = False
    #     return book

    def __str__(self):
        return self.btitle


class HeroInfo(models.Model):
    hname = models.CharField(max_length=10)
    hgender = models.BooleanField(default=True)
    hcontent = models.CharField(max_length=1000)
    isDelete = models.BooleanField(default=False)
    book = models.ForeignKey(BookInfo)

    def __str__(self):
        return self.hname
