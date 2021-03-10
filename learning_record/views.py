from django.shortcuts import render,get_object_or_404
from django.core.paginator import Paginator
from mysite.settings.base import SETTING_PER_PAGE_NUMBER
from .models import LearningCourse,Lesson
from blog.utills import create_page_list,get_month_hot_data,read_statistics_once_read
from blog.models import Blog,BlogType
from django.db.models import Count
from comment.models import Comment
from comment.forms import CommentForm
from django.contrib.contenttypes.models import ContentType
# Create your views here.

def course_list(request):
    courses = LearningCourse.objects.all()
    page_num = request.GET.get('page', 1)  # 获取url页面参数（GET请求） 默认为1
    paginator = Paginator(courses, SETTING_PER_PAGE_NUMBER)
    page_of_blogs = paginator.get_page(page_num)  # 默认或异常为1
    page_list = create_page_list(current_page=page_of_blogs.number, all_page_len=paginator.num_pages)
    context = {}
    context['page_list'] = page_list
    context['courses'] = page_of_blogs.object_list
    context['page_of_blogs'] = page_of_blogs
    context['blog_types'] = BlogType.objects.exclude(type_name__in=['学习记录']).annotate(blog_count=Count('blog'))  # BlogType关联Blog 计数Blog
    dates = Blog.objects.dates('created_time', 'month', order='DESC')
    dates_count = [Blog.objects.filter(created_time__year=i.year, created_time__month=i.month).count() for i in dates]
    context['hot_data'] = get_month_hot_data()
    context['blog_dates'] = [(dates[i], dates_count[i]) for i in range(len(dates_count))]
    return render(request, 'learning_record_list.html', context)

def lesson_list(request,course_pk):
    course = get_object_or_404(LearningCourse, pk=course_pk)
    lesson = Lesson.objects.filter(course=course).first()
    read_cookie_key = read_statistics_once_read(request, lesson)
    lesson_content_type = ContentType.objects.get_for_model(lesson)
    comments = Comment.objects.filter(content_type=lesson_content_type, object_id=lesson.pk)
    lessons = Lesson.objects.filter(course=lesson.course)
    context = {}
    context['lesson'] = lesson
    context['comments'] = comments
    context['comment_form'] = CommentForm(initial={'content_type': lesson_content_type.model, 'object_id': lesson.pk})
    context['lessons'] = lessons
    context['course'] = lesson.course
    context['next_lesson'] = Lesson.objects.filter(created_time__gt=lesson.created_time,course=lesson.course).first()
    context['previous_lesson'] = Lesson.objects.filter(created_time__lt=lesson.created_time,course=lesson.course).last()
    response = render(request,'lesson.html',context)
    response.set_cookie(read_cookie_key, 'True', max_age=72000)
    return response

def lesson(request,lesson_pk):
    lesson = get_object_or_404(Lesson, id=lesson_pk)
    read_cookie_key = read_statistics_once_read(request, lesson)
    lesson_content_type = ContentType.objects.get_for_model(lesson)
    comments = Comment.objects.filter(content_type=lesson_content_type, object_id=lesson.pk)
    lessons = Lesson.objects.filter(course=lesson.course)
    context = {}
    context['lesson'] = lesson
    context['comments'] = comments
    context['comment_form'] = CommentForm(initial={'content_type': lesson_content_type.model, 'object_id': lesson_pk})
    context['lessons'] =lessons
    context['course'] = lesson.course
    context['next_lesson'] = Lesson.objects.filter(created_time__gt=lesson.created_time,course=lesson.course).first()
    context['previous_lesson'] = Lesson.objects.filter(created_time__lt=lesson.created_time,course=lesson.course).last()
    response = render(request,'lesson.html',context)
    response.set_cookie(read_cookie_key,'True',max_age=72000)
    return response