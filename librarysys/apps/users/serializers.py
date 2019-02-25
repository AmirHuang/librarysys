# _*_ coding: utf-8 _*_
# @Time     : 23:27
# @Author   : Amir
# @Site     : 
# @File     : serializers.py
# @Software : PyCharm

from rest_framework import serializers
from rest_framework.validators import UniqueValidator
from users.models import Borrow
from books.models import Books
from django.contrib.auth import get_user_model

User = get_user_model()


class UserSerializer(serializers.ModelSerializer):
    borrow_num = serializers.IntegerField(default=None)

    class Meta:
        model = User
        fields = ('sn', 'name', 'department', 'classx', 'borrow_num')


class BookSerializer(serializers.ModelSerializer):
    class Meta:
        model = Books
        fields = ('sn', 'title', 'author', 'publisher')


class BorrowCreateSerializer(serializers.Serializer):
    # 获取当前的用户
    user = serializers.HiddenField(default=serializers.CurrentUserDefault())
    num = serializers.IntegerField(required=True, label='数量', min_value=1,
                                   error_messages={
                                       'min_value': '商品数量不能小于1',
                                       'required': '请选择购买数量'
                                   })
    books = serializers.PrimaryKeyRelatedField(required=True,
                                               queryset=Books.objects.all())

    def create(self, validated_data):
        user = self.context['request'].user
        num = validated_data['num']
        books = validated_data['books']

        borrow_list = Borrow.objects.filter(user=user, back_time=None)
        total = 0
        for borrow in borrow_list:
            total += borrow.num
        print('--------------total:', total)
        if total < 4:
            existed = Borrow.objects.filter(user=user, books=books)
            # 如果已经结果书了 并且数量<3 可以继续借
            # 如果数量=3 就不可以借了
            # 如果没有记录 创建记录
            if existed:
                existed = existed[0]
                count = existed.num + num + total
                if count < 4:
                    existed.num = count
                    existed.save()
                else:
                    raise serializers.ValidationError('借书数量不能超过3本啦')
            else:
                if (total + num) < 4:
                    existed = Borrow.objects.create(**validated_data)
                else:
                    raise serializers.ValidationError('借书数量不能超过3本啦')
            return existed
        else:
            raise serializers.ValidationError('借书数量不能超过3本啦')


class BorrowListSerializer(serializers.ModelSerializer):
    id = serializers.IntegerField()
    books = BookSerializer(read_only=True)
    time = serializers.DateTimeField(format='%Y-%m-%d %H:%M:%S')
    back_time = serializers.DateTimeField(format='%Y-%m-%d %H:%M:%S')
    num = serializers.IntegerField()

    class Meta:
        model = Borrow
        fields = ('id', 'books', 'time', 'back_time', 'num')


class UserUpdateSerializer(serializers.ModelSerializer):
    username = serializers.CharField(label='用户名', help_text='用户名',
                                     required=True, allow_blank=False,
                                     validators=[UniqueValidator(
                                         queryset=User.objects.all(),
                                         message='用户已经存在'
                                     )])
    # 输入密码的时候不显示明文
    password = serializers.CharField(style={'input_type': 'password'},
                                     label='密码', write_only=True)

    class Meta:
        model = User
        fields = ('username', 'password')
