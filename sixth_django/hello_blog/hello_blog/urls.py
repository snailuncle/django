"""hello_blog URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/2.0/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.conf.urls.static import static
from django.conf import settings
from django.contrib import admin
from django.urls import path,re_path,include
from django.views.generic import TemplateView
from blog.views import getform
# from users.views import user_login
from users.views import LoginView,RegisterView,ActiveUserView,ForgetPwdView,ResetView,ModifyPwdView
from organization.views import OrgView
                            

urlpatterns = [
    path('admin/', admin.site.urls),
    re_path(r'^form/$', getform,name='go_form'),
    re_path(r'^$',TemplateView.as_view(template_name='index.html'),name='index'),
    # re_path(r'^login/$',TemplateView.as_view(template_name='login.html'),name='login'),
    # re_path(r'^login/',user_login,name='login'),
    re_path(r'^login/',LoginView.as_view(),name='login'),
    re_path(r'^register/',RegisterView.as_view(),name='register'),
    re_path(r'^captcha/', include('captcha.urls')),
    re_path(r'^active/(?P<active_code>.*)/$',ActiveUserView.as_view(),name='user_active'),
    re_path(r'^forget/$',ForgetPwdView.as_view(),name='forget_pwd'),
    re_path(r'^reset/(?P<active_code>.*)/$',ResetView.as_view(),name='reset_pwd'),
    re_path(r'^forget/$',ForgetPwdView.as_view(),name='forget_pwd'),
    re_path(r'^modify_pwd/$',ModifyPwdView.as_view(),name='modify_pwd'),

    #课程机构首页
    re_path(r'^org_list/$',OrgView.as_view(),name='org_list'),


    
]
