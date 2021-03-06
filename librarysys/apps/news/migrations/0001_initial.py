# Generated by Django 2.0.2 on 2018-10-23 10:47

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='News',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=50, verbose_name='标题')),
                ('content', models.TextField(verbose_name='内容')),
                ('author', models.CharField(max_length=50, verbose_name='作者')),
                ('add_time', models.DateTimeField(default=datetime.datetime.now, verbose_name='创建日期')),
            ],
            options={
                'verbose_name': '新闻公告',
                'verbose_name_plural': '新闻公告',
                'ordering': ['-add_time'],
            },
        ),
    ]
