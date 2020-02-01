# -*-coding:utf-8-*-
"""blogsys URL Configuration

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
from django.conf import settings
from blog import views
from django.views.static import serve
from blog.upload import upload_image

urlpatterns = [
    url(r'^admin/', admin.site.urls),
    url(r'^all/(?P<type_id>\d+)', views.index),
    url(r'^all', views.index),
    url(r'^$', views.index),
    url(r'^produce_code', views.produce_code),

    url(r'^login', views.login),
    url(r'^logout', views.logout),
    url(r'^reg', views.reg),
    url(r"^uploads/(?P<path>.*)$", serve, {"document_root": settings.MEDIA_ROOT, }),
    #富文本编辑器图片上传
    url(r'^admin/upload/(?P<dir_name>[^/]+)$', upload_image, name='upload_image'),
]
