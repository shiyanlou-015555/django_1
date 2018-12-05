from django.shortcuts import render

from django.shortcuts import render
from  django.http import  HttpResponse


def index(request):
    return HttpResponse('cms首页')
def login(request):
    return HttpResponse("cms登录页面")
