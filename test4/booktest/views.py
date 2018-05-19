from django.shortcuts import render, redirect
from .models import HeroInfo, BookInfo
from django.http import HttpResponse


# Create your views here.

def index(request):
    hero_id1 = HeroInfo.objects.get(pk=1)
    hero_list = HeroInfo.objects.filter(isDelete=False)
    context = {'hero': hero_id1,
               'hero_list': hero_list}
    return render(request, 'booktest/index.html', context=context)


def show(request, id):  # 正常解析
    context = {'id': id}
    return render(request, 'booktest/show1.html', context=context)


def show_reverse(request, id1, id2):  # 反向解析
    context = {'id': (id1, id2)}
    return render(request, 'booktest/show.html', context=context)


# 用于练习模板的继承
def index2(request):
    return render(request, 'booktest/index2.html')


# 三层模板继承 #templates中 user1.html和user2.html继承自base_user.html继承自base.html
def user1(request):
    context = {'user1_title': 'user1_title',
               'uname': 'my name is user1'}
    return render(request, 'booktest/user1.html', context=context)


def user2(request):
    context = {'title': 'user12',
               'uname': 'my name is user2'}
    return render(request, 'booktest/user2.html', context=context)


# html转义练习
def htmlzhuanyitest(request):
    '''
    从视图传到模板当中的变量默认是转义的，传什么给模板，模板就输出什么；
    而直接在模板中定义的变量是不经过转义的
    '''
    context = {'t1': '<h1>123</h1>'}
    return render(request, 'booktest/htmltest.html', context=context)


# csrf练习
def csrf1(request):
    return render(request, 'booktest/csrf1.html')


def csrf2(request):
    username = request.POST['username']
    return HttpResponse('username is {}'.format(username))


# 验证码练习
def verify_code_test(request):
    from PIL import Image, ImageDraw, ImageFont
    import random
    # 创建背景色
    bgColor = (random.randrange(50, 100), random.randrange(50, 100), 0)
    # 规定宽高
    width = 100
    height = 25
    # 创建画布
    image = Image.new('RGB', (width, height), bgColor)
    # 构造字体对象
    font = ImageFont.truetype('C:\Windows\Fonts\simfang.ttf', 24)
    # 创建画笔
    draw = ImageDraw.Draw(image)
    # 创建文本内容
    text = '0123ABCD'
    # 逐个绘制字符
    textTemp = ''
    for i in range(4):
        textTemp1 = text[random.randrange(0, len(text))]
        textTemp += textTemp1
        draw.text((i * 25, 0), textTemp1, (255, 255, 255), font)
    request.session['code'] = textTemp
    image.save('D:\png1.png', 'JPEG')
    # 保存到内存流中
    from io import StringIO, BytesIO
    buf = BytesIO()
    image.save(buf, 'png')
    # 将内存流中的内容输出到客户端
    return HttpResponse(buf.getvalue(), 'image/png')

def verifytest1(request):
    return render(request, 'booktest/verifytest1.html')

def verifytest2(request):
    # return render(request, 'booktest/verifytest2.html')
    code = request.POST.get('code')
    session_code = request.session.get('code')
    if code.lower() == session_code.lower():
        # return redirect('/booktest/')
        return HttpResponse('您已登录成功')

