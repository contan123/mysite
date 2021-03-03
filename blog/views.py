from django.shortcuts import render,get_object_or_404
from .models import Blog,BlogType,Project
from django.core.paginator import Paginator
from mysite.settings.base import SETTING_PER_PAGE_NUMBER
from blog.utills import create_page_list,read_statistics_once_read,get_month_hot_data
from django.db.models import Count
from django.contrib.contenttypes.models import ContentType
from comment.models import Comment
from comment.forms import CommentForm

def get_blogs(request,blog):
    """
    获取博客基本内容
    """
    page_num = request.GET.get('page', 1)  # 获取url页面参数（GET请求） 默认为1
    paginator = Paginator(blog, SETTING_PER_PAGE_NUMBER)
    page_of_blogs = paginator.get_page(page_num)  # 默认或异常为1
    page_list = create_page_list(current_page=page_of_blogs.number, all_page_len=paginator.num_pages)
    context = {}
    context['page_list'] = page_list #跳转
    context['blogs'] = page_of_blogs.object_list
    context['page_of_blogs'] = page_of_blogs
    context['blog_types'] = BlogType.objects.exclude(type_name__in=['学习记录']).annotate(blog_count=Count('blog'))  # BlogType关联Blog 计数Blog
    dates = Blog.objects.dates('created_time', 'month', order='DESC')
    dates_count = [Blog.objects.filter(created_time__year=i.year,created_time__month =i.month).count() for i in dates]
    context['hot_data'] = get_month_hot_data()
    context['blog_dates'] = [(dates[i],dates_count[i]) for i in range(len(dates_count))]
    return context

def blog_list(request):
    context = get_blogs(request,Blog.objects.all())
    return render(request, 'blog_list.html', context)#context为字典，render 给html传入context参数

def blog_detail(request,blog_pk):
    blog = get_object_or_404(Blog, id=blog_pk)
    read_cookie_key = read_statistics_once_read(request,blog)
    blog_content_type = ContentType.objects.get_for_model(blog)
    comments = Comment.objects.filter(content_type=blog_content_type,object_id=blog.pk)
    context = {}
    context['blog'] = blog
    context['previous_blog'] = Blog.objects.filter(created_time__gt=blog.created_time).last() #get和filiter返回QuerySet
    context['next_blog'] = Blog.objects.filter(created_time__lt=blog.created_time).first()
    context['comments'] = comments
    context['comment_form'] = CommentForm(initial={'content_type':blog_content_type.model,'object_id':blog_pk})
    context['blog_types'] = BlogType.objects.annotate(blog_count=Count('blog'))  # BlogType关联Blog 计数Blog
    dates = Blog.objects.dates('created_time', 'month', order='DESC')
    dates_count = [Blog.objects.filter(created_time__year=i.year, created_time__month=i.month).count() for i in dates]
    context['hot_data'] = get_month_hot_data()
    context['blog_dates'] = [(dates[i], dates_count[i]) for i in range(len(dates_count))]
    response = render(request, 'blog_detail.html', context)
    response.set_cookie(read_cookie_key,'True',max_age=60)
    return response

def blogs_with_type(request,blog_type_pk):
    blog_type = get_object_or_404(BlogType, pk=blog_type_pk)
    context = get_blogs(request,Blog.objects.filter(blog_type=blog_type))
    context['blog_type'] = blog_type
    return render(request, 'blogs_with_type.html', context)

def blog_with_date(request,year,month):
    context = get_blogs(request,Blog.objects.filter(created_time__year=year,created_time__month=month))
    context['blog_date'] = '%s年%s月' % (year, month)
    return render(request, 'blog_with_date.html', context)

def blog_project_list(request):
    context = get_blogs(request,Project.objects.all())
    return render(request, 'blog_project_list.html', context)