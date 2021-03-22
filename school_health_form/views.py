
from .models import HealthInfo
from django.http import JsonResponse
from django.shortcuts import render
from .utils import ver


# Create your views here.

def health_form(request):
    context = {}
    return render(request,'healthinfo.html',context)

def find(request):
    data = {}
    if request.user.is_authenticated:
        username = request.GET.get('username')
        user = HealthInfo.objects.filter(username=username).first()
        if user:
            data['status'] = 'SUCCESS'
            data['name'] = user.name[:1]+''.join(['*' for i in range(1,len(user.name))])
            data['password'] = ''.join(['*' for i in range(0,len(user.password))])
            data['XY'] = ''.join(['*' for i in range(0,len(user.XY))])
            data['BJ'] = ''.join(['*' for i in range(0,len(user.BJ))])
            data['SSH'] = ''.join(['*' for i in range(0,len(user.SSH))])
            data['FDY'] = user.FDY
        else:
            data['status'] = 'ERROR'
            data['info'] = '未查询到结果，请创建'
    else:
            data['status'] = 'ERROR'
            data['info'] = '用户未登录'
    return JsonResponse(data)

def save(request):
    data = {}
    if request.user.is_authenticated:
        #保存或更改健康信息表
        username = request.GET.get('username','')
        obj,t = HealthInfo.objects.get_or_create(username=username)
        if request.GET.get('name',''):
            obj.name = request.GET.get('name','')
        if request.GET.get('password', ''):
            obj.password = request.GET.get('password', '')
        if request.GET.get('SSH',''):
            obj.SSH = request.GET.get('SSH','')
        if request.GET.get('XY', ''):
            obj.XY = request.GET.get('XY','')
        if request.GET.get('BJ', ''):
            obj.BJ = request.GET.get('BJ','')
        if request.GET.get('FDY', ''):
            obj.FDY = request.GET.get('FDY', '')
        obj.save()
        data['status'] ='SUCCESS'
        data['info'] = '保存成功'
    else:
        data['status'] ='ERROR'
        data['info'] = '用户未登录'
    return JsonResponse(data)

def verify(request):
    data = {}
    if request.user.is_authenticated:
        username = request.GET.get('username', '')
        obj, t = HealthInfo.objects.get_or_create(username=username)
        if request.GET.get('name', ''):
            obj.name = request.GET.get('name', '')
        if request.GET.get('password', ''):
            obj.password = request.GET.get('password', '')
        if request.GET.get('SSH', ''):
            obj.SSH = request.GET.get('SSH', '')
        if request.GET.get('XY', ''):
            obj.XY = request.GET.get('XY', '')
        if request.GET.get('BJ', ''):
            obj.BJ = request.GET.get('BJ', '')
        if request.GET.get('FDY', ''):
            obj.FDY = request.GET.get('FDY', '')
        user_1 = {
            'username': obj.username,
            'password': obj.password,
            'name': obj.name,
            'FDY': obj.FDY,
            'SSH': obj.SSH,
            "XY": obj.XY,
            "BJ": obj.BJ,
        }
        data = ver(user_1,data)
    else:
        data['status']='ERROR'
        data['info']='用户未登录'
    return JsonResponse(data)
