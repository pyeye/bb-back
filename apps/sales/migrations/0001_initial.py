# -*- coding: utf-8 -*-
# Generated by Django 1.11.1 on 2017-06-28 13:04
from __future__ import unicode_literals

import apps.sales.models
import django.contrib.postgres.fields.jsonb
from django.db import migrations, models
import django.db.models.deletion
import versatileimagefield.fields


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Day',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=255, verbose_name='День')),
                ('code', models.PositiveSmallIntegerField(unique=True, verbose_name='Код')),
                ('extra', django.contrib.postgres.fields.jsonb.JSONField(blank=True, default={}, null=True, verbose_name='Дополнительно')),
            ],
            options={
                'verbose_name': 'День',
                'verbose_name_plural': 'Дни',
            },
        ),
        migrations.CreateModel(
            name='DaySale',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('day', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='days', to='sales.Day', verbose_name='Дни')),
            ],
            options={
                'ordering': ['day__code'],
            },
        ),
        migrations.CreateModel(
            name='Month',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('date', models.DateField(verbose_name='Дата')),
                ('extra', django.contrib.postgres.fields.jsonb.JSONField(blank=True, default={}, null=True, verbose_name='Дополнительно')),
            ],
            options={
                'verbose_name': 'Месяц',
                'verbose_name_plural': 'Месяцы',
            },
        ),
        migrations.CreateModel(
            name='Sale',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=255, verbose_name='Название')),
                ('info', models.TextField(verbose_name='Информация')),
                ('image', versatileimagefield.fields.VersatileImageField(upload_to=apps.sales.models.upload_location, verbose_name='Фото')),
                ('is_active', models.BooleanField(default=True, verbose_name='Активированно')),
                ('created_at', models.DateTimeField(auto_now=True, verbose_name='Созданно')),
                ('extra', django.contrib.postgres.fields.jsonb.JSONField(blank=True, default={}, null=True, verbose_name='Дополнительно')),
            ],
            options={
                'verbose_name': 'Акция',
                'verbose_name_plural': 'Акции',
            },
        ),
        migrations.AddField(
            model_name='daysale',
            name='month',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='day_sales', to='sales.Month', verbose_name='Месяцы'),
        ),
        migrations.AddField(
            model_name='daysale',
            name='sales',
            field=models.ManyToManyField(related_name='sales', to='sales.Sale', verbose_name='Акции'),
        ),
    ]
