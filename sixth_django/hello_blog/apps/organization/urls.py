
from django.urls import path,re_path,include


from .views import OrgView,AddUserAskView

app_name='org'
urlpatterns=[
    #课程机构首页
    re_path(r'^list/$',OrgView.as_view(),name='org_list'),
    re_path(r'^add_ask/$',AddUserAskView.as_view(),name='add_ask')


]
