from django.contrib import admin
from .models import Course,Lesson,Video,CourseResource
# Register your models here.

class CourseAdmin(admin.ModelAdmin):
    list_display=['name','desc','detail','degree','learn_times','students']
    search_fields=['name','desc','detail','degree','students']
    list_filter=['name','desc','detail','degree','learn_times','students']
class LessonAdmin(admin.ModelAdmin):
    list_display=['course','name','add_time']
    search_fields=['course','name']
    list_filter=['course__name','name','add_time']
class VideoAdmin(admin.ModelAdmin):
    list_display=['lesson','name','add_time']
    search_fields=['course','name']
    list_filter=['lesson','name','add_time']
class CourseResourceAdmin(admin.ModelAdmin):
    list_display=['course','name','download','add_time']
    search_fields=['course','name','download']
    list_filter=['course','name','download','add_time']
    

admin.site.register(Course,CourseAdmin)
admin.site.register(Lesson,LessonAdmin)
admin.site.register(Video,VideoAdmin)
admin.site.register(CourseResource,CourseResourceAdmin)
