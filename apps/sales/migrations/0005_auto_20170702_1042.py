# -*- coding: utf-8 -*-
# Generated by Django 1.11.1 on 2017-07-02 10:42
from __future__ import unicode_literals

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('sales', '0004_auto_20170628_1330'),
    ]

    operations = [
        migrations.AlterField(
            model_name='daysalerel',
            name='month',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='current_month', to='sales.Month', verbose_name='Месяцы'),
        ),
    ]
