# _*_ coding: utf-8 _*_
# @Time     : 16:56
# @Author   : Amir
# @Site     : 
# @File     : adminx.py
# @Software : PyCharm

import xadmin
from .models import News


class NewsAdmin(object):
    list_display = ['title', 'content', 'author', 'add_time']


xadmin.site.register(News, NewsAdmin)


