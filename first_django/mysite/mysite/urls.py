"""mysite URL Configuration

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
from django.contrib import admin
from django.urls import path,include

#在mysite项目目录下
#http收到请求先访问,项目目录中的urls
#从上到下依次匹配
#首先访问mysite文件夹下的polls目录,他导入了polls目录下的urls模块,现在转到polls.urls模块,发送给polls.urls的部分是polls/之后的字符
urlpatterns = [
    path('polls/',include('polls.urls')),
    path('admin/', admin.site.urls),
]
