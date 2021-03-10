from django.contrib import admin
from .models import LearningCourse,Lesson
# Register your models here.

@admin.register(LearningCourse)

class LearningCourse(admin.ModelAdmin):
    list_display = ('id','type_name')

@admin.register(Lesson)

class Lesson(admin.ModelAdmin):
    list_display = ('id', 'title', 'course', 'author', 'search_readnum', 'created_time', 'last_updated_time')