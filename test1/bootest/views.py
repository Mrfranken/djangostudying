from django.shortcuts import render

# Create your views here.

from django.http import HttpResponse
# from django.template import RequestContext, loader

from .models import HeroInfo, BookInfo


def index(request):
    # 写法一
    # 加载模板
    # temp = loader.get_template('bootest/nihao.html')
    # render方法渲染模板
    # return HttpResponse(temp.render())

    # 写法二(写法1和2的实现机制是一样的)
    # 使用model 使用模板
    booklist = BookInfo.objects.all()
    context = {'bookinfo': booklist}
    return render(request, 'bootest/nihao.html', context=context)

def detail(request, book_id):
    return render(request, 'bootest/book_info.html', context={'book_id': book_id})