import matplotlib.pyplot as plt
import base64
import datetime
from django.utils import timezone
from io import BytesIO


def get_graph():
    #将二进制转为base64编码
    buffer = BytesIO()
    plt.savefig(buffer,format='png')
    buffer.seek(0)
    image_png = buffer.getvalue()
    graph = base64.b64encode(image_png)
    graph = graph.decode('utf-8')
    buffer.close()
    return graph

def plot_get_sevendays_label():
    label = [timezone.now().date() - datetime.timedelta(days=i) for i in range(1,8)]
    label.reverse()
    return ['%s/%s' % (label[i].month,label[i].day) for i in range(7)]

def get_plot(x,y):
    plt.switch_backend('agg')
    plt.rcParams['font.sans-serif'] = ['SimHei']  # 用来正常显示中文标签
    plt.rcParams['axes.unicode_minus'] = False  # 用来正常显示负号
    plt.figure(figsize=(4,3))

    plt.plot(x,y,'o-')
    plt.yticks([i for i in range(0,max(y)+20,10)])
    plt.xticks(x,plot_get_sevendays_label())
    for a,b in zip(x,y):
        plt.text(a,b+0.7,'%d'%b,ha='center', va= 'bottom')
    plt.tight_layout()
    graph = get_graph()
    return graph

