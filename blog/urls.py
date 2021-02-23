from django.urls import path
from .views import blog_detail,blogs_with_type,blog_list,blog_with_date
urlpatterns = [
    path('',blog_list,name='blog_list'),
    path('<int:blog_pk>',blog_detail,name='blog_deatil'),
    path('type/<int:blog_type_pk>',blogs_with_type,name="blogs_with_type"),
    path('data/<int:year>/<int:month>',blog_with_date,name="blog_with_date")
]
