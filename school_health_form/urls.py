from django.urls import path
from . import views

urlpatterns = [
    path('',views.health_form,name='health_form'),
    path('save',views.save,name='save'),
    path('find',views.find,name='find'),
    path('verify',views.verify,name='verify')
]