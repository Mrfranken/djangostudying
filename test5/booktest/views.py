import os
from django.shortcuts import render
from django.http import HttpResponse
from django.conf import settings

# Create your views here.

def index(request):
    return render(request, 'booktest/index.html')

def execptiontest_func(request):
    a1 = int('abc')
    return HttpResponse('hello')

def upload_pic(request):
    return render(request, 'booktest/uploadpic.html')

def uploadhandle(request):
    if request.method == 'POST':
        pic_content = request.FILES.get('pic1')
        file_name = os.path.join(settings.MEDIA_ROOT, pic_content.name)
        with open(file_name, 'wb') as f:
            for content in pic_content.chunks():
                f.write(content)
                # 转义字符
        return HttpResponse('<img src="/abc/media/{}/">'.format(file_name))
