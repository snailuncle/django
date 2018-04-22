# -*- coding: utf-8 -*-
from django.shortcuts import render
from .models import Article

# Create your views here.
def index(request):
    article_list = Article.objects.all().order_by('-created_time')
    for each in article_list:
        print(each)
    #文章列表数据的 article_list 变量传给了模板
    return render(request, 'index.html', context={'article_list':article_list})
