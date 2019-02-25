# _*_ coding: utf-8 _*_
# @Time     : 17:05
# @Author   : Amir
# @Site     : 
# @File     : adminx.py
# @Software : PyCharm

from .models import Category, Books
import xadmin


class CategoryAdmin(object):
    list_display = ["name", "room", "site"]


class BooksAdmin(object):
    list_display = ["sn", "title", "author", "publisher", "publication_date", "status", 'desc', 'category']


xadmin.site.register(Category, CategoryAdmin)
xadmin.site.register(Books, BooksAdmin)
