from django.db import models
from django.contrib.auth.models import User #用户模型
from ckeditor_uploader.fields import RichTextUploadingField
from read_statistics.models import ReadNumExpandMethod,BlogReadNum,ReadDetail
from comment.models import Comment
from django.contrib.contenttypes.fields import GenericRelation
# Create your models here.

class BlogType(models.Model):
    type_name = models.CharField(max_length= 15)
    def __str__(self):
        return self.type_name



class Blog(models.Model,ReadNumExpandMethod):
    title = models.CharField(max_length= 50)
    blog_type = models.ForeignKey(BlogType,on_delete=models.CASCADE)
    content = RichTextUploadingField()
    author = models.ForeignKey(User,on_delete=models.CASCADE)
    read_details = GenericRelation(ReadDetail)
    created_time = models.DateTimeField(auto_now_add=True)
    last_updated_time = models.DateTimeField(auto_now=True)
    blog_read_nums = GenericRelation(BlogReadNum)
    comments = GenericRelation(Comment)


    def __str__(self):
        return '<Blog:%s>'%self.title

    class Meta:     #分页排序
        ordering = ['-created_time']

