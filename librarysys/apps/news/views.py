from rest_framework import viewsets, mixins
from rest_framework_jwt.authentication import JSONWebTokenAuthentication
from rest_framework.authentication import SessionAuthentication
from rest_framework.permissions import IsAuthenticated
from utils.publicpagination import PublicPagination
from .models import News
from .serializers import NesSerializer


class NewsViewset(mixins.ListModelMixin, viewsets.GenericViewSet):
    queryset = News.objects.all().order_by('id')
    pagination_class = PublicPagination
    serializer_class = NesSerializer
    authentication_classes = (JSONWebTokenAuthentication,
                              SessionAuthentication)
    permission_classes = (IsAuthenticated,)