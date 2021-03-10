from django.db import models
from django.contrib.auth.models import User #用户模型
from ckeditor_uploader.fields import RichTextUploadingField
from read_statistics.models import ReadNumExpandMethod,BlogReadNum,ReadDetail
from comment.models import Comment
from django.contrib.contenttypes.fields import GenericRelation

# Create your models here.

class LearningCourse(models.Model):
    type_name = models.CharField(max_length= 15)
    content = models.TextField(max_length=100)
    def __str__(self):
        return self.type_name



class Lesson(models.Model,ReadNumExpandMethod):
    title = models.CharField(max_length= 50)
    course = models.ForeignKey(LearningCourse,on_delete=models.CASCADE)
    content = RichTextUploadingField()
    author = models.ForeignKey(User,on_delete=models.CASCADE)
    read_details = GenericRelation(ReadDetail)
    created_time = models.DateTimeField(auto_now_add=True)
    last_updated_time = models.DateTimeField(auto_now=True)
    read_nums = GenericRelation(BlogReadNum)
    comments = GenericRelation(Comment)
