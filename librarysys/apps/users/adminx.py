# _*_ coding: utf-8 _*_
# @Time     : 16:36
# @Author   : Amir
# @Site     : 
# @File     : adminx.py
# @Software : PyCharm

import xadmin
from xadmin import views
from .models import Borrow


class BaseSetting(object):
    # 添加主题功能
    enable_themes = True
    use_bootswatch = True


class GlobalSettings(object):
    # 全局配置，后台管理标题和页脚
    site_title = "Amir"
    site_footer = "xxxxxx"
    # 菜单收缩
    menu_style = "accordion"


# class UserProfileAdmin(object):
#     list_display = ['sn', 'name', 'department', 'classx', 'start_date',
#                     'end_date', 'end_date', 'professional', 'birth_day', 'gender', 'phone']


class BorrowAdmin(object):
    list_display = ['user', 'books', 'time', 'back_time']


# xadmin.site.unregister(User)
# xadmin.site.register(User, UserProfileAdmin)

xadmin.site.register(Borrow, BorrowAdmin)

xadmin.site.register(views.BaseAdminView, BaseSetting)
xadmin.site.register(views.CommAdminView, GlobalSettings)