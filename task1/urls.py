"""task1 URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.1/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import include,path
from django.urls import re_path as url
from Chemai_data.views import Back_end_See_File
from django.conf import settings
from django.conf.urls.static import static
from django.views.static import serve
from task1.settings import MEDIA_ROOT
urlpatterns = [
    path("", include("Chemai_data.urls")), #前端界面
    path("Chemai_data/", include("Chemai_data.urls")),#项目路径跳转
    url('admin/', admin.site.urls),#后端界面
    url(r'^media/(?P<path>.*)$', serve, {"document_root": MEDIA_ROOT}),#后端实现文件存储
    url(r'admin/Chemai_data/Files/Chemai_data', Back_end_See_File.get_file),#后端界面文件预览
    # 移除重复的include，避免命名空间冲突
    # url(r'^video/', include("Chemai_data.urls")),#本地文件访问链接

]