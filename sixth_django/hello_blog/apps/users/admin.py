from django.contrib import admin

from .models import UserProfile,EmailVerifyRecord,Banner


# Register your models here.

admin.site.site_header = '小信风博客后台管理中心'
admin.site.site_title = '小信风博客后台'



#用户
class UserProfileAdmin(admin.ModelAdmin):
    pass

#关联
admin.site.register(UserProfile,UserProfileAdmin)


# 邮箱验证码
class EmailVerifyRecordAdmin(admin.ModelAdmin):
    list_display=['code','email','send_type','send_time']
    search_fields=['code','email','send_type']
    list_filter=['code','email','send_type','send_time']

class BannerAdmin(admin.ModelAdmin):
    list_display=['title','image','url','index','add_time']
    search_fields=['title','image','url','index','add_time']
    list_filter=['title','image','url','index','add_time']
    

admin.site.register(EmailVerifyRecord,EmailVerifyRecordAdmin)
admin.site.register(Banner,BannerAdmin)
