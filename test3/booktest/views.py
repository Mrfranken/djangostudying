from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.

def index(request):
    # return render(request, HttpResponse('helloworld'))
    # return HttpResponse('一个人的朝圣')
    return HttpResponse(request.path+'-'+request.method)

def detail(request, num):
    return HttpResponse("you've got {}".format(num))

def ganjianzhiparams(request, id2, id1):
    #参数匹配规则：优先使用命名参数，如果没有命名参数则使用位置参数
    return HttpResponse("you've got {}年{}月".format(id1, id2))