from django.shortcuts import render
from blog.utills import get_week_read_data,get_today_hot_data,get_yesterday_hot_data,get_week_hot_data
from django.contrib.contenttypes.models import ContentType
from blog.models import Blog
from mysite.utills import get_plot
from django.core.cache import cache
from django.contrib import messages

def home(request):
    context = {}
    blog_content_type = ContentType.objects.get_for_model(Blog)
    read_nums = get_week_read_data(blog_content_type)
    today_hot_data = get_today_hot_data()
    yesterday_hot_data = get_yesterday_hot_data()

    week_hot_data = cache.get('week_hot_data')
    chart = cache.get('chart1')
    if chart is None:
        chart = get_plot([1,2,3,4,5,6,7],read_nums)
        cache.set('chart1', chart, 3600)

    if week_hot_data is None:
        week_hot_data = get_week_hot_data()
        cache.set('week_hot_data',week_hot_data,3600)#键值秒

    context['read_nums'] = read_nums
    context['today_hot_data'] = today_hot_data
    context['yesterday_hot_data'] = yesterday_hot_data
    context['week_hot_data'] = week_hot_data
    context['chart'] = chart
    return render(request,'home.html',context)

def text(request):
    # 需要弹出的消息框
    messages.success(request, '欢迎访问')
    #  注意你需要在index.html添加我们上面的js代码
    return render(request, 'text.html', {})

