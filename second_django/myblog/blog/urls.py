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
app_name = 'blog'
urlpatterns = [
    path('index/', views.index),
    re_path('article/(?P<article_id>[0-9]+)/', views.article_page,name='article_page'),
    re_path('edit/(?P<article_id>[0-9]+)/',views.edit_page,name='edit_page'),
    path('edit/action/',views.edit_action,name='edit_action'),
]
