from django.shortcuts import render
from django.http import HttpResponse
from .import models
# Create your views here.
def index(request):
    articles=models.Article.objects.all()
    return render(request,'blog/index.html',{'articles':articles})

def edit_page(request,article_id):
    # article_id当前修改的文章ID号
    #根据article_id显示当前显示的标题和内容
    if str(article_id)==str(0):
        #给edit_page.html页面传送article_id为0的article
        article=''
    else:
        article=models.Article.objects.get(pk=article_id)
    return render(request,'blog/edit_page.html',{'article':article})

def article_detail(request,article_id):
    print('进入文章详情页_views_article_detail')  
    article=models.Article.objects.get(pk=article_id)
    return render(request,'blog/article_detail.html',{'article':article})
def edit_submit_result(request):
    result='准备写入数据库'
    try:
        print('进入文章修改结果页_edit_submit_result') 
        article_id=request.POST.get('article_id','article_id')
        title=request.POST.get('title','TITLE')
        content=request.POST.get('content','CONTENT')
        print('从编辑页面传回来的参数title和content以及article_id')
        print(title)
        print(content)
        print(article_id)
        if str(article_id)==str(0):
            models.Article.objects.create(title=title,content=content)
            result='新文章写入数据库成功'
        else:
            article=models.Article.objects.get(pk=article_id)
            article.title=title
            article.content=content
            article.save()
            result='原有文章修改成功'
    except Exception:
        result='写入数据库失败'
    return render(request,'blog/edit_submit_result.html',{'result':result})
