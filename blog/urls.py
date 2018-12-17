from django.conf.urls import url

from blog import views

urlpatterns = [
    # 首页
    url(r'^index/$', views.index, name='index'),

    # 登录
    url(r'^login/$', views.login, name='login'),
    # 图片验证码
    url(r'^tuyzm/$', views.tuyzm, name='tuyzm'),
    # 注册
    url(r'^reg/$', views.reg, name='reg'),
    # 注册信息
    url(r'^logon/$', views.logon, name='logon'),
    # 短信验证码
    url(r'^send/$', views.send, name='send'),

    # 我的主页
    url(r'^homepage/$', views.homepage, name='homepage'),

    #博客管理
    url(r'^guanli/$',views.guanli,name='guanli'),

    url(r'^add/$',views.add,name='add'),
    url(r'^change/$',views.change,name='change'),
    url(r'^dele/$',views.dele,name='dele'),
    url(r'^dodele/(\d+)/$',views.dodele,name='dodele')

]