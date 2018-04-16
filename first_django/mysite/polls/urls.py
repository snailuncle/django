from django.urls import path
import datetime
from . import views
from django.utils import timezone

now = timezone.now()
print('*'*33)
print('polls_urls.py')
print(now)

app_name = 'polls'
# views.py 或 models.py根据name来获取path中对应的网址
# name是给views和models用的
# help(views.IndexView.as_view())
# print(dir(views.IndexView.as_view))
# print(views.IndexView.as_view.__subclasshook__)
urlpatterns = [
    # @classonlymethod
    # def as_view(cls, **initkwargs):
    path('', views.IndexView.as_view(), name='index'),
    path('<int:pk>/', views.DetailView.as_view(), name='detail'),
    path('<int:pk>/results/', views.ResultsView.as_view(), name='results'),
    path('<int:question_id>/vote/', views.vote, name='vote'),
]
