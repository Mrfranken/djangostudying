import os
from django.shortcuts import render, redirect
from django.http import HttpResponse
from django.conf import settings
from .models import UserInfo, HeroInfo

# Create your views here.

def index(request):
    u = HeroInfo.objects.all()
    context = {
        'hcontent': u[0].hcontent
    }
    return render(request, 'booktest/index.html', context=context)

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
        return HttpResponse('<img src="/wsj/media/{}">'.format(pic_content.name))
        # return HttpResponse(file_name)

def editor(request):
    return render(request, 'booktest/editor.html')

def show_editor_content(request):
    hcontent = request.POST.get('hcontent', None)
    u = UserInfo(uname='wsj', upwd=hcontent, isDelete=True)
    u.save()
    return HttpResponse(hcontent)

