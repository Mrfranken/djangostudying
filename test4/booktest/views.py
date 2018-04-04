from django.shortcuts import render
from .models import HeroInfo, BookInfo
# Create your views here.

def index(request):
    hero = HeroInfo.objects.get(pk=1)
    context = {'hero': hero}
    return render(request, 'booktest/index.html', context=context)