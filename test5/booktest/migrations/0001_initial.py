# -*- coding: utf-8 -*-
# Generated by Django 1.9.8 on 2018-04-22 13:44
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='UserInfo',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('uname', models.CharField(max_length=10)),
                ('upwd', models.CharField(max_length=40)),
                ('isDelete', models.BooleanField(default=False)),
            ],
        ),
    ]
