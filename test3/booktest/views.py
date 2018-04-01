from django.shortcuts import render
from django.http import HttpResponse


# Create your views here.

def index(request):
    # return render(request, HttpResponse('helloworld'))
    # return HttpResponse('一个人的朝圣')
    return HttpResponse(
        request.path + '-' + request.method)


def detail(request, num):
    return HttpResponse("you've got {}".format(num))


def ganjianzhiparams(request, id2, id1):
    # 参数匹配规则：优先使用命名参数，如果没有命名参数则使用位置参数
    return HttpResponse("you've got {}年{}月".format(id1, id2))

#展示链接的页面
def getTest1(request):
    return render(request, 'booktest/gettest1.html')

#接受一键一值的情况
def getTest2(request):
    a1 = request.GET['a']
    b1 = request.GET['b']
    c1 = request.GET['c']
    context = {'a': a1,
               'b': b1,
               'c': c1}
    return render(request, 'booktest/gettest2.html', context=context)

#接受一键多值的情况
def getTest3(request):
    a1 = request.GET.getlist('a')
    b1 = request.GET['b']
    context = {
        'a': a1,
        'b': b1
    }
    return render(request, 'booktest/gettest3.html', context=context)

def posttest1(request):
    return render(request, 'booktest/posttest1.html')

def posttest2(request):
    username = request.POST['username']
    password = request.POST['password']
    gender = request.POST['gender']
    hobby = request.POST.getlist('hobby')
    context = {
        'username': username,
        'password': password,
        'gender': gender,
        'hobby': hobby
    }
    return render(request, 'booktest/posttest2.html', context=context)

