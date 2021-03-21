from .models import HealthInfo
from django.contrib import admin
# Register your models here.


@admin.register(HealthInfo)

class HealthInfo(admin.ModelAdmin):
    list_display = ('name','username')