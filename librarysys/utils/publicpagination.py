# _*_ coding: utf-8 _*_
# @Time     : 22:47
# @Author   : Amir
# @Site     : 
# @File     : publicpagination.py
# @Software : PyCharm


from rest_framework.pagination import PageNumberPagination


class PublicPagination(PageNumberPagination):
    '''
    商品列表自定义分页
    '''
    # 默认每页显示的个数
    page_size = 10
    # 可以动态改变每页显示的个数
    page_size_query_param = 'page_size'
    # 页码参数
    page_query_param = 'page'
    # 最多能显示多少页
    max_page_size = 100
