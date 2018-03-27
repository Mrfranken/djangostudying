from django.contrib import admin

# Register your models here.
from .models import BookInfo, HeroInfo


admin.register(BookInfo)
admin.register(HeroInfo)