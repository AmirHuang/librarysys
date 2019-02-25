"""librarysys URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/2.0/topics/http/urls/
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
from django.urls import path, include
import xadmin
from rest_framework.routers import DefaultRouter
from rest_framework.authtoken import views
from rest_framework_jwt.views import obtain_jwt_token
from django.views.static import serve
from librarysys.settings import MEDIA_ROOT
from rest_framework.documentation import include_docs_urls
from books.views import BooksViewset
from news.views import NewsViewset
from users.views import UserViewset, BorrowViewset

router = DefaultRouter()
router.register(r'books', BooksViewset, base_name="books")

router.register(r'news', NewsViewset, base_name="news")

router.register(r'users', UserViewset, base_name="users")

router.register(r'borrows', BorrowViewset, base_name="borrows")

urlpatterns = [
    path('xadmin/', xadmin.site.urls),
    path('ueditor/', include('DjangoUeditor.urls')),

    # 文件
    path('media/<path:path>', serve, {'document_root': MEDIA_ROOT}),

    # drf文档，title自定义
    path('docs', include_docs_urls(title='Amir')),
    # rest登陆
    path('api-auth/', include('rest_framework.urls')),
    path('', include(router.urls)),

    # token
    path('api-token-auth/', views.obtain_auth_token),

    # jwt的token认证接口
    path('login', obtain_jwt_token),

]
