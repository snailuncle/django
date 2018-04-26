from django.contrib import admin
from .models import CityDict,CourseOrg,Teacher
# Register your models here.



class CityDictAdmin(admin.ModelAdmin):
    list_display=['name','desc','add_time']
    search_fields=['name','desc']
    list_filter=['name','desc','add_time']






class CourseOrgAdmin(admin.ModelAdmin):
    list_display=['name','short_desc','click_nums','fav_nums']
    search_fields=['name','desc','click_nums','fav_nums']
    list_filter=['name','desc','click_nums','fav_nums']
    def short_desc(self,instance):      
        length=35
        if len(instance.desc)>length:
            return str(instance.desc)[:length]+'...'
        else:
            return str(instance.desc)     
    short_desc.short_description='机构描述'
    short_desc.allow_tags=True



class TeacherAdmin(admin.ModelAdmin):
    list_display=['org','name','work_years','work_company']
    search_fields=['org','name','work_years','work_company']
    list_filter=['org','name','work_years','work_company']


admin.site.register(CityDict,CityDictAdmin)
admin.site.register(CourseOrg,CourseOrgAdmin)
admin.site.register(Teacher,TeacherAdmin)
