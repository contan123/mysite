from django.contrib import admin
from .models import BlogReadNum,ReadDetail
# Register your models here.
@admin.register(BlogReadNum)

class BlogReadNum(admin.ModelAdmin):
    list_display = ('read_num','content_object')

@admin.register(ReadDetail)

class ReadDetail(admin.ModelAdmin):
    list_display = ('read_num','content_object','date')