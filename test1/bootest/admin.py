from django.contrib import admin

# Register your models here.

from .models import BookInfo, HeroInfo


class HeroInfoInline(admin.StackedInline):
    model = HeroInfo
    extra = 2
    # 这个数字表示在添加BookInfo的时候会列出1个表单让填写HeroInfo
    # 继承StackedInline表示显示的添加表单形式是stack形式的，还有TabularInline


class BookInfoAdmin(admin.ModelAdmin):
    # 自定义model的管理页面
    list_display = ['id', 'btitle', 'bpub_date']
    list_filter = ['id', 'btitle', 'bpub_date']
    search_fields = ['btitle']
    fields = ['bpub_date', 'btitle']
    list_per_page = 10

    actions_on_top = True
    # actions_on_bottom = True

    inlines = [HeroInfoInline]


class HeroInfoAdmin(admin.ModelAdmin):
    list_display = ['id', 'hname', 'hgender', 'book', 'content']
    search_fields = ['hname']


admin.site.register(BookInfo, BookInfoAdmin)
admin.site.register(HeroInfo, HeroInfoAdmin)

# admin使用总结：
# 1. 添加管理员账户
# 2. 使用admin注册Model类（如需自定义展示页面则可以自定义类继承admin.ModelAdmin）
