"""mysite URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/3.1/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path,include
from .views import home,text
from django.conf import settings
from django.conf.urls.static import static
urlpatterns = [
    path('',home,name='home'),
    path('text',text,name='text'),
    path('admin/', admin.site.urls),
    path('ckeditor',include('ckeditor_uploader.urls')),
    path('blog/',include('blog.urls')), #blog 文件夹的 urls路由 以blog传入参数
    path('comment/',include('comment.urls')),
    path('user/',include('user.urls')),
    path('learning_record/',include('learning_record.urls')),
    path('school_health_form/',include('school_health_form.urls')),
]
#管理静态文件
urlpatterns += static(settings.MEDIA_URL,document_root=settings.MEDIA_ROOT)
