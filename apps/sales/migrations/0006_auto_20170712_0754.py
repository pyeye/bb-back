# -*- coding: utf-8 -*-
# Generated by Django 1.11.1 on 2017-07-12 07:54
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('sales', '0005_auto_20170702_1042'),
    ]

    operations = [
        migrations.AlterField(
            model_name='sale',
            name='info',
            field=models.TextField(blank=True, null=True, verbose_name='Информация'),
        ),
    ]
