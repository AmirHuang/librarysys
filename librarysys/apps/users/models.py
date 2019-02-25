from datetime import datetime
from django.contrib.auth.models import AbstractUser
from django.db import models
from books.models import Books


class UserProfile(AbstractUser):
    sn = models.CharField('学号', unique=True, max_length=50, null=True)
    name = models.CharField('姓名', max_length=50, null=True)
    department = models.CharField('系', max_length=50, null=True)
    classx = models.CharField('班级', max_length=50, null=True)
    start_date = models.DateField('入学日期', null=True)
    end_date = models.DateField('毕业日期', null=True, blank=True)
    professional = models.CharField('专业', max_length=50, null=True)
    birth_day = models.DateField('出生日', null=True, blank=True)
    gender = models.CharField('性别', max_length=10, choices=(('male', '男'),
                                                            ('female', '女'),
                                                            ('unknown', '未知')),
                              default='unknown')
    phone = models.CharField('电话', max_length=20, blank=True, null=True)

    class Meta:
        verbose_name = '用户'
        verbose_name_plural = verbose_name

    def __str__(self):
        return self.username

    def save(self, *args, **kwargs):
        if len(self.password) < 20:
            self.set_password(self.password)
        # print(self.password)
        super(UserProfile, self).save(*args, **kwargs)


class Borrow(models.Model):
    user = models.ForeignKey(UserProfile, verbose_name='借阅者', on_delete=models.CASCADE)
    books = models.ForeignKey(Books, verbose_name='书', on_delete=models.SET_NULL, null=True)
    time = models.DateTimeField('借阅时间', default=datetime.now)
    back_time = models.DateTimeField('还书时间', null=True, blank=True)
    num = models.IntegerField('数量', default=1)

    class Meta:
        verbose_name = '借阅记录'
        verbose_name_plural = verbose_name
        unique_together = ('user', 'books')

    def __str__(self):
        return self.user.username
