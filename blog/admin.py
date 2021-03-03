from django.contrib import admin
from .models import BlogType,Blog,Project
# Register your models here.


@admin.register(BlogType)

class BlogType(admin.ModelAdmin):
    list_display = ('id','type_name')

@admin.register(Blog)

class Blog(admin.ModelAdmin):
    list_display = ('id','title','blog_type','author','search_readnum','created_time','last_updated_time')

@admin.register(Project)

class Project(admin.ModelAdmin):
    list_display = ('id','title','blog','image')