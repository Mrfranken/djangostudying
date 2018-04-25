from django.shortcuts import render

# Create your views here.
from .models import HeroInfo
from django.core.paginator import Paginator


#test5中分页练习 方法1是直接请求带有数字的url链接
# def herolist(request, page_num=1):
#     hero_list = HeroInfo.objects.all()
#     paginator = Paginator(hero_list, per_page=5)
#     page = paginator.page(page_num)
#     context = {'page': page}
#     return render(request, 'booktest/herolist.html', context=context)


#test5中分页练习 方法2是通过get请求传入数字来进行请求（只需要在urls中定义一个url匹配）
def herolist(request):
    a = request.GET.get('a', 1)
    hero_list = HeroInfo.objects.all()
    paginator = Paginator(hero_list, per_page=5) #将信息分成每5个一页
    page = paginator.page(a) #拿到第a页的数据，是个集合
    context = {'page': page}
    return render(request, 'booktest/herolist.html', context=context)