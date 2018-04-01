from django.contrib import admin

# Register your models here.
from .models import BookInfo, HeroInfo


class HeroInfoInline(admin.TabularInline):
    model = HeroInfo
    extra = 2

class BookInfoAdmin(admin.ModelAdmin):
    # btitle = models.CharField(max_length=20)
    # bpub_date = models.DateTimeField(db_column='pub_date')
    # bread = models.IntegerField(default=0)
    # bcomment = models.IntegerField(default=0)
    # isDelete = models.BooleanField(default=False)
    list_display = ['btitle', 'bpub_date', 'bread', 'bcomment', 'isDelete']
    search_fields = ['btitle', 'bread']
    inlines = [HeroInfoInline]

admin.site.register(BookInfo, BookInfoAdmin)
admin.site.register(HeroInfo)