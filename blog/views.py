# -*- coding:utf-8 -*- 
from django.shortcuts import render
from .models import Blog,Tag
# 日志相关
import logging
logging.basicConfig(level=logging.INFO,
    format='%(asctime)s %(filename)s[line:%(lineno)d] %(levelname)s %(message)s',
    datefmt='%Y-%m-%d %H:%M:%S',
    filename='blog_log.txt',
    filemode='w')
#################################################################################################
#定义一个StreamHandler，将INFO级别或更高的日志信息打印到标准错误，并将其添加到当前的日志处理对象#
console = logging.StreamHandler()
console.setLevel(logging.INFO)
formatter = logging.Formatter('%(name)-12s: %(levelname)-8s %(message)s')
console.setFormatter(formatter)
logging.getLogger('').addHandler(console)
#################################################################################################


# Create your views here.
# 展示博客列表
def blogs(request):
	if request.method == 'GET':
		blogs = Blog.objects.all()
		#logging.info(blogs[0].id)
		return render(request,'blogs.html',{'blogs':blogs})
	else:
		return render(request,'blogs.html',{'blogs':blogs})

#展示博客详情
def blog(request,blog_id):
	if request.method == 'GET':
		logging.info(blog_id)
		try:
			blog = Blog.objects.get(id = blog_id)
		except:
			logging.info("Cannot find a blog of which id is %s !" % str(blog_id))
		return render(request,'blog.html',{'blog':blog})
	else:
		return render(request,'blog.html',{'blog':blog})