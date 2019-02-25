# _*_ coding: utf-8 _*_
# @Time     : 22:42
# @Author   : Amir
# @Site     : 
# @File     : serializers.py
# @Software : PyCharm

from rest_framework import serializers
from books.models import Books, Category


class CategorySerializer(serializers.ModelSerializer):

    class Meta:
        model = Category
        fields = '__all__'


class BooksSerializer(serializers.ModelSerializer):
    category = CategorySerializer(many=False)

    class Meta:
        model = Books
        fields = '__all__'
