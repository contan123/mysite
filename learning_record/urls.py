from django.urls import path
from . import views
urlpatterns = [
    path('',views.course_list,name='course_list'),
    path('lesson/<int:lesson_pk>',views.lesson,name='lesson'),
    path('lesson_list/<int:course_pk>',views.lesson_list,name='lesson_list'),
]