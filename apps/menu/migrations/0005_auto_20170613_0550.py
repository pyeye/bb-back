# -*- coding: utf-8 -*-
# Generated by Django 1.11.1 on 2017-06-13 05:50
from __future__ import unicode_literals

import apps.menu.models
from django.db import migrations, models
import django.db.models.deletion
import versatileimagefield.fields


class Migration(migrations.Migration):

    dependencies = [
        ('menu', '0004_auto_20170613_0356'),
    ]

    operations = [
        migrations.CreateModel(
            name='Image',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('info', models.CharField(blank=True, max_length=255, null=True, verbose_name='Информация')),
                ('created_at', models.DateTimeField(auto_now=True, verbose_name='Созданно')),
                ('image', versatileimagefield.fields.VersatileImageField(upload_to=apps.menu.models.upload_location, verbose_name='Фото')),
            ],
            options={
                'verbose_name': 'Фотография',
                'verbose_name_plural': 'Фотографии',
            },
        ),
        migrations.AddField(
            model_name='category',
            name='template',
            field=models.CharField(blank=True, choices=[('vertical', 'Вертикальный'), ('horizontal', 'Горизонтальный'), ('horizontal_half', 'Горизонтальный половина'), ('half', 'Половина'), ('full', 'Полный')], default='full', max_length=128, verbose_name='Название'),
        ),
        migrations.AddField(
            model_name='image',
            name='category',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='images', to='menu.Category', verbose_name='Фотография'),
        ),
    ]
