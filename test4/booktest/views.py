from django.shortcuts import render
from .models import HeroInfo, BookInfo
# Create your views here.

def index(request):
    hero_id1 = HeroInfo.objects.get(pk=1)
    hero_list = HeroInfo.objects.filter(isDelete=False)
    context = {'hero': hero_id1,
               'hero_list': hero_list}
    return render(request, 'booktest/index.html', context=context)

def show(request, id): #正常解析
    context = {'id': id}
    return render(request, 'booktest/show1.html', context=context)

def show_reverse(request, id1, id2): #反向解析
    context = {'id': (id1, id2)}
    return render(request, 'booktest/show.html', context=context)
