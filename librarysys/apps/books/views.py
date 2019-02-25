from rest_framework.generics import GenericAPIView
from rest_framework.response import Response
from rest_framework import filters
from rest_framework_jwt.authentication import JSONWebTokenAuthentication
from rest_framework.authentication import SessionAuthentication
from rest_framework import serializers
from rest_framework import viewsets, mixins
from django_filters.rest_framework import DjangoFilterBackend

from utils.publicpagination import PublicPagination
from .models import Books
from .serializers import BooksSerializer


class BooksViewset(mixins.ListModelMixin, viewsets.GenericViewSet):
    queryset = Books.objects.all().order_by('id')
    pagination_class = PublicPagination
    authentication_classes = (JSONWebTokenAuthentication, SessionAuthentication)
    serializer_class = BooksSerializer
    filter_backends = (DjangoFilterBackend, filters.SearchFilter)
    # 搜索
    search_fields = ('sn', 'title', 'author', 'publisher')
