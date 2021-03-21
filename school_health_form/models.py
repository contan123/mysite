from django.db import models

# Create your models here.

class HealthInfo(models.Model):
    name = models.CharField(max_length=4)
    username = models.CharField(max_length=20)
    password = models.CharField(max_length=2000)
    FDY = models.CharField(max_length=4)
    SSH = models.CharField(max_length=20)
    XY = models.CharField(max_length=20)
    BJ = models.CharField(max_length=20)