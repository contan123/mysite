import re
import string
import random
import time
from django.http import JsonResponse
from django.shortcuts import render,redirect,reverse
from django.contrib import auth
from django.contrib.auth.models import User
from django.contrib import messages
from .models import Profile
from .forms import ChangeNicknameFrom,BindEmailForm
from django.core.mail import send_mail
from .forms import UserDetailForm
from django.contrib.auth.decorators import login_required
def login(request):
    username = request.POST.get('username','')
    password = request.POST.get('password','')
    user = auth.authenticate(request,username=username,password=password)
    referer = request.META.get('HTTP_REFERER',reverse('home'))
    if user is not None:
        auth.login(request,user)
        messages.success(request, '欢迎访问',)
        return redirect(referer)
    else:
        messages.error(request,'用户名或密码错误')
        return redirect(referer)

def logout(request):
    auth.logout(request)
    referer = request.META.get('HTTP_REFERER', reverse('home'))
    messages.success(request,'已退出')
    return redirect(referer)


def register(request):
    user = User
    nickname = request.POST.get('nickname','')
    username = request.POST.get('username', '')
    password1 = request.POST.get('password1', '')
    password2 = request.POST.get('password2', '')
    email = request.POST.get('email','none_email')
    verification_code = request.POST.get('verification_code','none_code')
    referer = request.META.get('HTTP_REFERER', reverse('home'))
    if user.objects.filter(username=username):
        messages.error(request, '用户名已注册')
    elif re.search(r'\W',password1) != None:
        messages.error(request, '密码不能包含特殊字符')
    elif password1!=password2:
        messages.error(request, '两次输入密码不一致')
    elif request.session.get(email) != verification_code:
        messages.error(request, '验证码错误')
    else:
        if username and password1 and email:
            t=user.objects.create_user(username=username,password=password1,email=email)
            Profile.objects.get_or_create(user=t,nickname=nickname)
            messages.success(request, '注册成功')
        else:
            messages.error(request, '用户名密码不可为空')

    return redirect(referer)


    """
    if request.method == 'POST':
        login_form = LoginForm(request.POST)
        if login_form.is_valid():
            username = login_form.cleaned_data['usename']
            password = login_form.cleaned_data['password']
            user = auth.authenticate(request,username=username,password=password)
            if user is None:
                referer = request.META.get('HTTP_REFERER', reverse('home'))
                auth.login(request,user)
                return redirect(referer)
            else:
                login_form.add_error(None,'用户名或密码不正确')
    else:
        login_form = LoginForm()
    context = {}
    context['login_form'] = login_form
"""

def user_info(request):
    context = {}
    return render(request,'user_info.html',context)


def change_nickname(request):
    redirect_to = request.GET.get('from',reverse('home'))

    if request.method == 'POST':
        form =ChangeNicknameFrom(request.POST,user=request.user)
        if form.is_valid():
            nickname_new = form.cleaned_data['nickname_new']
            profile,created=Profile.objects.get_or_create(user=request.user)
            profile.nickname = nickname_new
            profile.save()
            return redirect(redirect_to)
    else:
        form = ChangeNicknameFrom()
    context = {}
    context['form'] = form
    context['page_title'] = '修改昵称'
    context['form_title'] = '修改昵称'
    context['submit_text'] = '修改'
    context['return_back_url'] = redirect_to
    return render(request,'form.html',context)

def bind_email(request):
    redirect_to = request.GET.get('from',reverse('home'))
    if request.method == 'POST':
        form =BindEmailForm(request.POST,request=request)
        if form.is_valid():
            email = form.cleaned_data['email']
            request.user.email = email
            request.user.save()
            del request.session[email]
            return redirect(redirect_to)
    else:
        form = BindEmailForm()
    context = {}
    context['form'] = form
    context['page_title'] = '绑定邮箱'
    context['form_title'] = '绑定邮箱'
    context['submit_text'] = '绑定'
    context['return_back_url'] = redirect_to
    return render(request, 'bind_email.html', context)

def send_verification_code(request):
    email = request.GET.get('email','')
    data ={}
    if User.objects.filter(email=email):
        data['status'] = 'error'
        data['type'] = '该邮箱已注册'
    elif email !='':
        #生产验证码
        code=''.join(random.sample(string.ascii_letters + string.digits,4))
        now = int(time.time())
        send_code_time = request.session.get('send_code_time',0)
        if now - send_code_time <30:
            data['status'] = 'ERROR'

        else:
            #发送邮件
            request.session[email] = code
            request.session['send_code_time'] = now
            send_mail(
                '绑定邮箱', #主题
                '验证码:%s' % code,
                '3143790685@qq.com',
                [email],
                fail_silently=False,
            )
            data['status']='SUCCESS'
    else:
        data['status'] = 'ERROR'
    return JsonResponse(data)

@login_required
def change_avater(request):
    redirect_to = request.GET.get('from', reverse('home'))
    # post请求 表明是在修改用户资料
    if request.method == 'POST':
        form = UserDetailForm(request.POST, request.FILES)
        if form.is_valid():
            if 'avatar' in request.FILES:
                request.user.profile.avatar.delete()
                request.user.profile.avatar = form.cleaned_data["avatar"]
                request.user.profile.save()
                return redirect(redirect_to)
    # 如果是get请求，则使用user生成表单
    else:
        form = UserDetailForm(instance=request.user)
    context = {}
    context['form'] = form
    context['page_title'] = '更改头像'
    context['form_title'] = '更改头像'
    context['submit_text'] = '更改'
    context['return_back_url'] = redirect_to
    return render(request, 'form.html', context)

