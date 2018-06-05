from django.contrib import admin

# Register your models here.
from .models import UserInfo
from .models import HeroInfo


# 这是第一种注册方式，先定义一个类继承ModelAdmin然后将模板类和这个类一起注册
# class UserInfoAdmin(admin.ModelAdmin):
#     list_display = ['id', 'uname', 'upwd']
#
# admin.site.register(UserInfo, UserInfoAdmin) #这么写是不对的admin.register(UserInfo)

# 第二种注册方式是使用模板类的装饰器装饰UserInfoAdmin这个类
@admin.register(UserInfo)
class UserInfoAdmin(admin.ModelAdmin):
    list_display = ['id', '_uname', '_upwd', 'person_pic']

@admin.register(HeroInfo)
class HeroInfoAdmin(admin.ModelAdmin):
    list_display = ['id', 'hname', 'hgender']

