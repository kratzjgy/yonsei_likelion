# -*- coding: utf-8 -*-
# Generated by Django 1.9 on 2018-12-26 09:53
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('homepage', '0005_auto_20181226_1851'),
    ]

    operations = [
        migrations.AlterField(
            model_name='post',
            name='author',
            field=models.CharField(max_length=10, null=True),
        ),
    ]
