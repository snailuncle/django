# -*- coding: utf-8 -*-
from django.shortcuts import render
from django.http import HttpResponse
from .import models
from django.contrib import messages

# Create your views here.




# def index(request):
#     return HttpResponse('hello,world!')
# 三个参数
# 第一个是request
# 第二个是网页模板
# 第三个是传给模板中的字典,在模板中使用{{ 字典的键 }}来引用,字典的值
# def index(request):
#     return render(request,'blog/index.html',{'hello':'hello blog\n从views传过来的字典'})
# def index(request):
#     article=models.Article.objects.get(pk=1)
    
#     return render(request,'blog/index.html',{'article':article})
def index(request):
    # 数据库的表的名字->Article
    #把所有数据存到articles中
    articles=models.Article.objects.all()
    print(request)
    return render(request,'blog/index.html',{'articles':articles})

def article_page(request,article_id):
    article=models.Article.objects.get(pk=article_id)
    return render(request,'blog/article_page.html',{'article':article})
    # return HttpResponse('hello 我是views中的article_page函数')

def edit_page(request,article_id):
    print('到达edit_page函数')
    if str(article_id)==str(0):
        print('get edit_page view')
        return render(request,'blog/edit_page.html')
    article=models.Article.objects.get(pk=article_id)
    print(request)
    print(article)

    return render(request,'blog/edit_page.html',{'article':article})


def edit_action(request):
    title=request.POST.get('title','TITLE')
    print('title='+title)
    content=request.POST.get('content','CONTENT')
    print('content='+content)
    article_id=request.POST.get('article_id','0')
    print('article_id='+article_id)
    if article_id=='0':
        models.Article.objects.create(title=title,content=content)
        articles=models.Article.objects.all()
        return render(request,'blog/index.html',{'articles':articles})
    article=models.Article.objects.get(pk=article_id)
    article.title=title
    article.content=content
    article.save()
    return render(request,'blog/article_page.html',{'article':article})
    
