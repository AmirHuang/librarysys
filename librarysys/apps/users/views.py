from datetime import datetime
from rest_framework import viewsets, mixins
from django_filters.rest_framework import DjangoFilterBackend
from rest_framework_jwt.authentication import JSONWebTokenAuthentication
from rest_framework.authentication import SessionAuthentication
from rest_framework.permissions import IsAuthenticated
from users.serializers import UserUpdateSerializer, BorrowCreateSerializer, BorrowListSerializer
from utils.publicpagination import PublicPagination
from .filters import BorrowFilter
from django.contrib.auth import get_user_model
User = get_user_model()


class UserViewset(mixins.UpdateModelMixin,
                  mixins.RetrieveModelMixin,
                  viewsets.GenericViewSet):
    queryset = User.objects.all()
    serializer_class = UserUpdateSerializer
    authentication_classes = (JSONWebTokenAuthentication, SessionAuthentication)
    permission_classes = (IsAuthenticated,)


class BorrowViewset(mixins.ListModelMixin,
                    mixins.CreateModelMixin,
                    mixins.RetrieveModelMixin,
                    mixins.DestroyModelMixin,
                    viewsets.GenericViewSet):
    # pagination_class = PublicPagination
    def get_serializer_class(self):
        if self.action == 'create':
            return BorrowCreateSerializer
        else:
            return BorrowListSerializer
    authentication_classes = (JSONWebTokenAuthentication, SessionAuthentication)
    permission_classes = (IsAuthenticated,)
    # filter_backends = (DjangoFilterBackend,)
    # filter_class = BorrowFilter

    def get_queryset(self):
        tag = self.request.GET.get('tag')
        if tag == 'None':
            return self.request.user.borrow_set.filter(back_time=None)
        else:
            return self.request.user.borrow_set.all()

    # 库存 -num
    def perform_create(self, serializer):
        borrow_obj = serializer.save()
        book_obj = borrow_obj.books
        book_obj.stock -= borrow_obj.num
        book_obj.save()

    # 库存 + num
    def perform_destroy(self, instance):
        book_obj = instance.books
        book_obj.stock += instance.num
        book_obj.save()
        instance.back_time = datetime.now()
        instance.save()













