from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.

def index(request):
    return render(request, 'booktest/index.html')

def execptiontest_func(request):
    a1 = int('abc')
    return HttpResponse('hello')
