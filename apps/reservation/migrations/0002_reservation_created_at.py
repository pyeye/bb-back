# -*- coding: utf-8 -*-
# Generated by Django 1.11.1 on 2017-07-12 07:54
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('reservation', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='reservation',
            name='created_at',
            field=models.DateTimeField(auto_now=True, verbose_name='Созданно'),
        ),
    ]
