# _*_ coding: utf-8 _*_
# @Time     : 23:17
# @Author   : Amir
# @Site     : 
# @File     : serializers.py
# @Software : PyCharm

from rest_framework import serializers
from .models import News


class NesSerializer(serializers.ModelSerializer):
    add_time = serializers.DateTimeField(format='%Y-%m-%d')

    class Meta:
        model = News
        fields = '__all__'
