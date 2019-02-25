from datetime import datetime
from django.db import models


class News(models.Model):
    title = models.CharField('标题', max_length=50)
    content = models.TextField('内容')
    author = models.CharField('作者', max_length=50)
    add_time = models.DateTimeField('创建日期', default=datetime.now)

    class Meta:
        verbose_name = '新闻公告'
        verbose_name_plural = verbose_name
        ordering = ['-add_time']

    def __str__(self):
        return self.title