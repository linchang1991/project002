# -*- coding:utf-8 -*- 
"""project002 URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/1.11/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  url(r'^$', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  url(r'^$', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.conf.urls import url, include
    2. Add a URL to urlpatterns:  url(r'^blog/', include('blog.urls'))
"""
from django.conf.urls import url
from django.contrib import admin
from blog.views import blogs, blog, new_blog, uploadFiles
from django.conf import settings
from django.conf.urls.static import static


urlpatterns = [
    url(r'^admin/', admin.site.urls),

    #博客
    url(r'^blogs/$',blogs),
    url(r'^blog/(?P<blog_id>[^/]+)/$',blog),
    
    url(r'^uploadFiles',uploadFiles),
    url(r'^new_blog/$', new_blog),    
    #url(r'^modify_staff/(?P<modify_staff_name>[^/]+)/$','examine.views.modify_staff'),
] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)


