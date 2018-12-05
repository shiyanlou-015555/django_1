from django.shortcuts import render
from  django.http import  HttpResponse
from django.shortcuts import redirect


def index(request):
    usename = request.GET.get('username')
    if usename:
        return HttpResponse('前台首页')
    else :
        return redirect('/login/')
def login(request):
    return HttpResponse("f登录页面")
