from datetime import datetime
from random import randint

from django.core.paginator import Paginator
from django.shortcuts import render, HttpResponse, redirect

# Create your views here.
from django.urls import reverse

from blog.md5 import md_5
from blog.models import User, Category, Tag, Article

from blog.sms import SMS
from blog.verifycode import Verifycode


# 首页
def index(request,num='1'):
    art = Article.objects.order_by('id').reverse()
    data = {
        'art':art
    }
    # print(art)

    return render(request, 'blog/base.html',context=data)


# 登录
def login(request):
    if request.method == 'GET':
        # print(1)
        return render(request, 'blog/login.html')
    else:
        username = request.POST.get('username')
        password = request.POST.get('password')
        tuyzm = request.POST.get('tuyzm')
        # 获取session中的验证码
        code = request.session.get('code')
        if tuyzm == code:

            password = md_5(password)
            # print(password)
            user = User.objects.filter(user_name=username, password=password)

            # print(username)
            # 判断用户是否存在
            if user.exists():
                res = redirect(reverse('blog:index'))
                # print(2)
                # 设置session
                request.session['username'] = username
                request.session['password'] = password
                return res
            else:
                return redirect(reverse('blog:login'))
                # return render(request, 'blog/base.html', context={'data': '用户名或密码错误'})
        else:
            return redirect(reverse('blog:login'))

            # return render(request, 'blog/login.html', context={'data': '验证码错误'})


# 图片验证码
def tuyzm(request):
    vc = Verifycode(4)
    res = vc.output()
    # 将验证码字符串添加到session
    request.session['code'] = vc.code
    # print('vc.code',vc.code)
    return HttpResponse(res, 'image/png')


# 注册
def reg(request):
    # print(11)
    return render(request, 'blog/reg.html')


# 注册信息
def logon(request):
    username = request.POST.get('username')
    password = request.POST.get('password')
    phone = request.POST.get('phone')
    yzm = request.POST.get('yzm')

    # session 取出验证码
    yzm1 = request.session.get('yzm')
    yzm1 = str(yzm1)
    #print(yzm, yzm1)
    if yzm == yzm1:
        user = User()
        user.user_name = username
        user.password = md_5(password)
        user.user_phone = phone
        user.save()
        return HttpResponse('注册成功')

    return HttpResponse('验证码错误')


# 短信验证码
def send(request):
    phone = request.GET.get('phone')
    sms = SMS('fdy','SMS_151577891')
    num = randint(1000, 9999)
    #print(num)
    # 验证码写入session
    request.session['yzm'] = num
    res = sms.send_sms(phone, num)
    return HttpResponse(res)




# 我的主页
def homepage(request):
    # 判断用户是否登录
    username = request.session.get('username')
    #print(username)
    if username:
        user_id = User.objects.get(user_name=username).id

        art = Article.objects.filter(user_id=user_id).order_by('id').reverse()

        return render(request, 'blog/homepage.html', context={'username': username, 'art': art})

    else:
        return render(request, 'blog/login.html')


def guanli(request):
    return render(request,'blog/guanli.html')


def add(request):
    art = Article()
    if request.method == "POST":
        username = request.session.get('username')
        user_id = User.objects.get(user_name=username).id
        art.user_id = user_id
        art.page_view = randint(1,20)
        art.category_id = randint(1,5)
        art.title = request.POST.get('title')
        #print(art.title)
        art.content = request.POST.get('content')
        art.date_publish = datetime.today().strftime("%Y/%m/%d/%H/%M/%S")
        art.save()
    return render(request, 'blog/add.html')


def change(request):
    return render(request,'blog/list.html')


def dele(request):
    username = request.session.get('username')
    user_id = User.objects.get(user_name=username).id

    art = Article.objects.filter(user_id=user_id)

    return render(request,'blog/cate.html',context={'art':art})


def dodele(request,id):
    article = Article.objects.get(pk=int(id))
    article.delete()
    return redirect(reverse('blog:dele'))