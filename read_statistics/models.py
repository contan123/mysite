from django.contrib.contenttypes.fields import GenericForeignKey,GenericRelation
from django.contrib.contenttypes.models import ContentType
from django.db import models
from django.db.models.fields import exceptions
from django.utils import timezone
# Create your models here.


class BlogReadNum(models.Model):
    read_num = models.IntegerField(default=0)
    content_type = models.ForeignKey(ContentType, on_delete=models.DO_NOTHING)
    object_id = models.PositiveIntegerField()
    content_object = GenericForeignKey('content_type', 'object_id') #联合主键
    read_detail = GenericRelation('ReadDetail') #反向关联使得能够级联删除


class ReadNumExpandMethod():
    #model Blog 多重继承
    def search_readnum(self):
        try:
            ct = ContentType.objects.get_for_model(self)
            read_num = BlogReadNum.objects.get(content_type=ct,object_id=self.pk).read_num
            return read_num
        except exceptions.ObjectDoesNotExist:
            return 0

class ReadDetail(models.Model):
    #每日博客阅读数量
    date = models.DateField(default=timezone.now)
    read_num = models.IntegerField(default=0)
    content_type = models.ForeignKey(ContentType, on_delete=models.DO_NOTHING)
    object_id = models.PositiveIntegerField()
    content_object = GenericForeignKey('content_type', 'object_id')