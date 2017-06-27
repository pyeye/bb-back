# -*- coding: utf-8 -*-
# Generated by Django 1.11.1 on 2017-06-01 10:56
from __future__ import unicode_literals

import apps.gallery.models
from django.db import migrations, models
import django.db.models.deletion
import versatileimagefield.fields


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Album',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=255, verbose_name='Название')),
                ('description', models.TextField(blank=True, null=True, verbose_name='Описание')),
                ('date', models.DateTimeField(verbose_name='Дата')),
                ('created_at', models.DateTimeField(auto_now=True, verbose_name='Созданно')),
                ('main_image', versatileimagefield.fields.VersatileImageField(upload_to=apps.gallery.models.album_upload_location, verbose_name='Фото')),
            ],
            options={
                'ordering': ['-date'],
                'verbose_name': 'Альбом',
                'verbose_name_plural': 'Альбомы',
            },
        ),
        migrations.CreateModel(
            name='Image',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('info', models.CharField(blank=True, max_length=255, null=True, verbose_name='Информация')),
                ('created_at', models.DateTimeField(auto_now=True, verbose_name='Созданно')),
                ('image', versatileimagefield.fields.VersatileImageField(upload_to=apps.gallery.models.upload_location, verbose_name='Фото')),
                ('album', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='images', to='gallery.Album', verbose_name='Альбом')),
            ],
            options={
                'verbose_name': 'Фотография',
                'verbose_name_plural': 'Фотографии',
            },
        ),
    ]
