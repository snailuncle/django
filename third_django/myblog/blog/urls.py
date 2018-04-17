"""myblog URL Configuration

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
from django.urls import path,re_path
from . import views
app_name='blog'
print('blog_urls')
urlpatterns = [    
    re_path(r'^index/', views.index,name='index'),
    # path(  route,       view,        kwargs=None,         name=None)
    # article_id
    re_path(r'^edit/(?:(?P<article_id>\d+)/)?$',views.edit_page,name='edit_page'),
    re_path(r'^article/(?P<article_id>\d+)/detail/$',views.article_detail,name='article_detail'),
    re_path(r'^edit/result/$',views.edit_submit_result,name='edit_submit_result'),
    
]

