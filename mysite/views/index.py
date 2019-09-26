from django.http.response import HttpResponse
import datetime
from django.shortcuts import render_to_response
from django.db import connection
from mysite.models import Slideshow
import json

def index(request):

    '''
    cursor = connection.cursor()
    result = cursor.execute("select * from bas_account")
    # 获取所有记录列表
    results = cursor.fetchall()
    for row in results:
        fname = row[0]
        lname = row[1]
        age = row[2]
        sex = row[3]
        income = row[4]
        # 打印结果
        print("name=%s,lname=%s,age=%s,sex=%s,income=%s", fname, lname, age, sex, income)
    '''

    # insert()
    query()
    return render_to_response('index.html', {'title': 'Hello World', 'message': datetime.datetime.now()})


def insert():
    # 随机整数 作为学号
    for i in range(0, 5):
        # 从models文件中获取student对象
        slideshow = Slideshow()
        # 给对象赋值
        slideshow.Slideshow_img_url = 'http://www.baidu.com'
        slideshow.Slideshow_url = 'http://www.baidu.com'
        slideshow.Slideshow_title = '图片名称'
        # 插入数据
        slideshow.save()


def query():
    slideshowlist = Slideshow.objects.filter(Slideshow_img_url='http://www.baidu.com')
    for item in slideshowlist:
        print(json.dumps(item, default=obj_2_json))


def obj_2_json(obj):
    return {
        "id": obj.id,
        "Slideshow_img_url": obj.Slideshow_img_url,
        "Slideshow_url": obj.Slideshow_url,
        "Slideshow_title": obj.Slideshow_title
    }


def sayhello(request):
    s = 'Hello World!'
    current_time = datetime.datetime.now()
    html = '<html><head></head><body><h1> %s </h1><p> %s </p></body></html>' % (s, current_time)
    return HttpResponse(html)
