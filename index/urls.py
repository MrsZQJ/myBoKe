from django.urls import path, include, re_path
#上面这行多加了一个re_path
from django.views.static import serve
#导入静态文件模块
from django.conf import settings
#导入配置文件里的文件上传配置
from index import views

urlpatterns = [
    path('index', views.index),
    path('banner', views.s_banner),
    path('category',views.s_category),
    path('article',views.s_new_article),
    path('a_detail',views.s_detail_artical),
    path('web',views.s_web),
    path('python',views.s_python),
    path('myself',views.s_myself),
    path('search',views.search),
    re_path(r'^static/(?P<path>.*)$', serve, {'document_root': settings.VUE_URL+'static'}),
]
