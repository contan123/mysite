import datetime
from django.contrib.contenttypes.models import ContentType
from read_statistics.models import BlogReadNum,ReadDetail
from django.utils import timezone
from django.db.models import Sum
from blog.models import Blog
def create_page_list(current_page,all_page_len):
    page_list = [current_page + i for i in range(-2, 3) if (0 < current_page + i <= all_page_len)]
    current_len = len(page_list)
    if current_len < 7:
        if page_list[0] == 1:
            page_list += [i for i in range(page_list[-1] + 1, page_list[-1] + (8 - current_len)) if
                          i <= all_page_len]
            if page_list[-1] >= 7:
                page_list[-2] = '...'
                page_list[-1] = all_page_len

        elif page_list[-1] == all_page_len:
            page_list = list(range(max(page_list[0] - (7 - current_len), 1), page_list[0])) + page_list
            if page_list[-1] >= 7:
                page_list[0] = 1
                page_list[1] = '...'
        else:
            page_list[0] = '...'
            page_list[-1] = '...'
            page_list.insert(0, 1)
            page_list.append(all_page_len)
    return page_list

def read_statistics_once_read(request,obj):
    ct = ContentType.objects.get_for_model(obj)
    key = "%s_%s_read" % (ct.model,obj.pk)
    if request.user != obj.author:
        if not request.COOKIES.get(key):
            #总阅读数+1
            """
            if BlogReadNum.objects.filte r(content_type=ct,object_id=obj.pk).count() != 0:
                readnum = BlogReadNum.objects.get(content_type=ct,object_id=obj.pk)
            else:
                readnum = BlogReadNum(content_type=ct,object_id=obj.pk)
                可用get_or_create替代 返回(对象,是否为创建TRUE/FALSE)元组
            """
            readnum,created = BlogReadNum.objects.get_or_create(content_type=ct,object_id=obj.pk)
            readnum.read_num += 1
            readnum.save()

            #当天阅读+1
            date=timezone.now().date()

            """
            if ReadDetail.objects.filter(content_type=ct,object_id=obj.pk,date=date).count():
                readdetail=ReadDetail.objects.get(content_type=ct,object_id=obj.pk,date=date)
            else:
                readdetail = ReadDetail(content_type=ct,object_id=obj.pk,date=date)
            """
            readdetail,created = ReadDetail.objects.get_or_create(content_type=ct,object_id=obj.pk,date=date)
            readdetail.read_num += 1
            readdetail.save()
    return key

def get_week_read_data(content_type):
    today = timezone.now().date()
    read_nums = []
    for i in range(7,0,-1):
        date =today - datetime.timedelta(days=i) #日期差量
        read_deatils = ReadDetail.objects.filter(content_type=content_type,date=date)
        result = read_deatils.aggregate(read_num_sum=Sum('read_num'))#聚合函数
        read_nums.append(result["read_num_sum"] or 0)
    return read_nums

def get_days_hot_data(end_data=0,begin_date=0):
    today = timezone.now().date()-datetime.timedelta(days=end_data)
    begin_date = timezone.now().date()-datetime.timedelta(days=begin_date)
    read_details = Blog.objects\
        .filter(read_details__date__lte=today,read_details__date__gte=begin_date)\
        .values('id','title')\
        .annotate(read_num_sum = Sum('read_details__read_num'))\
        .order_by('-read_num_sum')
    return read_details[:8]

def get_today_hot_data():
    return get_days_hot_data(0,0)

def get_yesterday_hot_data():
    return get_days_hot_data(1,1)

def get_week_hot_data():
    return get_days_hot_data(1,7)

def get_month_hot_data():
    return get_days_hot_data(0,30)