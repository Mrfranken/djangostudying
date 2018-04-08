from django.shortcuts import render
from .models import HeroInfo, BookInfo
# Create your views here.

def index(request):
    hero_id1 = HeroInfo.objects.get(pk=1)
    hero_list = HeroInfo.objects.filter(isDelete=False)
    context = {'hero': hero_id1,
               'hero_list': hero_list}
    return render(request, 'booktest/index.html', context=context)