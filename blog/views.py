# -*- coding:utf-8 -*- 
from django.shortcuts import render
from django.http import HttpResponse
from django.views.decorators.csrf import csrf_exempt
from .models import Blog,Tag
from .forms import BlogForm
import time
from project002.settings import MEDIA_ROOT, MEDIA_URL
#from django.core import settings
from django.core.paginator import Paginator

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
		paginator = Paginator(blogs,10)
		page = request.GET.get('page')
		try:
			blog_page = paginator.page(page)
		except :
			blog_page = paginator.page(1)
		return render(request,'blogs.html',{'blogs':blog_page})
	else:
		return HttpResponse("request.method is POST")

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

#写新博客
def new_blog(request):
	if request.method == 'GET':
		form = BlogForm()
		#print(f.as_table())
		return render(request,'new_blog.html',{"form":form})
	else:
		form = BlogForm(request.POST)
		if form.is_valid():
			f = form.cleaned_data
			new_blog = Blog.objects.create(
				title = f['title'],
				author = f['author'],
				content = f['content'],
				)
			blogs = Blog.objects.all()
			#logging.info(blogs[0].id)
			return render(request,'blogs.html',{'blogs':blogs})



#上传文件
@csrf_exempt
def uploadFiles(request):
	
	if request.method == 'POST':
		callback = request.GET.get('CKEditorFuncNum')
		try:
			path = MEDIA_ROOT
			f = request.FILES["upload"]
			f.name = time.strftime("%Y%m%d%H%M%S",time.localtime()) + "_" + f.name  #加个时间前缀
			file_name = path + f.name
			logging.info("filename: %s" % file_name)


			des_origin_f = open(file_name, "wb+")
			#logging.info("Open file:%s" % file_name)  
			for chunk in f.chunks():
			    des_origin_f.write(chunk)
			des_origin_f.close()
			#logging.info("Close file:%s" % file_name)

		except Exception as e:
		    print(e)
		#res = "<script>window.parent.CKEDITOR.tools.callFunction("+callback+",'/"+file_name+"', '');</script>"
		res = "<script>window.parent.CKEDITOR.tools.callFunction("+callback+",'/media/"+f.name+"', '');</script>"
		logging.info("res:%s" % res)
		return HttpResponse(res)
	else:
	    raise Http404()
	