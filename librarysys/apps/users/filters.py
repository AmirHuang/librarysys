# _*_ coding: utf-8 _*_
# @Time     : 15:27
# @Author   : Amir
# @Site     : 
# @File     : filters.py
# @Software : PyCharm

import datetime
import django_filters

from .models import Borrow


class BorrowFilter(django_filters.rest_framework.FilterSet):
    back_time = django_filters.BooleanFilter(label='是否退还',
                                             method='back_time_filter')

    def back_time_filter(self, queryset, name, value):
        if value is True:
            return queryset
        else:
            return queryset.filter(back_time=None)

    class Meta:
        model = Borrow
        fields = ['back_time', ]
