# -*- coding: utf-8 -*-
# Generated by Django 1.11.1 on 2017-06-05 16:17
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('gallery', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='album',
            name='date',
            field=models.DateField(verbose_name='Дата'),
        ),
    ]
