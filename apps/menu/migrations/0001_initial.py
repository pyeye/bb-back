# -*- coding: utf-8 -*-
# Generated by Django 1.11.1 on 2017-06-01 10:56
from __future__ import unicode_literals

import django.contrib.postgres.fields.jsonb
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Category',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=255, unique=True, verbose_name='Название')),
                ('extra', django.contrib.postgres.fields.jsonb.JSONField(blank=True, default={}, null=True, verbose_name='Дополнительно')),
            ],
            options={
                'verbose_name': 'Категория',
                'verbose_name_plural': 'Категории',
            },
        ),
        migrations.CreateModel(
            name='Group',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=255, unique=True, verbose_name='Название')),
                ('code', models.CharField(max_length=128, unique=True, verbose_name='Код')),
                ('extra', django.contrib.postgres.fields.jsonb.JSONField(blank=True, default={}, null=True, verbose_name='Дополнительно')),
            ],
            options={
                'verbose_name': 'Группа',
                'verbose_name_plural': 'Группы',
            },
        ),
        migrations.CreateModel(
            name='Menu',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=255, unique=True, verbose_name='Название')),
                ('description', models.TextField(verbose_name='Описание')),
                ('created_at', models.DateTimeField(auto_now=True, verbose_name='Созданно')),
                ('is_active', models.BooleanField(default=True, verbose_name='Активированно')),
                ('extra', django.contrib.postgres.fields.jsonb.JSONField(blank=True, default={}, null=True, verbose_name='Дополнительно')),
                ('category', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='menu', to='menu.Category', verbose_name='Категория')),
            ],
            options={
                'verbose_name': 'Меню',
                'verbose_name_plural': 'Меню',
            },
        ),
        migrations.CreateModel(
            name='Price',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('count', models.FloatField(blank=True, null=True, verbose_name='Количество')),
                ('measure', models.CharField(blank=True, max_length=64, null=True, verbose_name='Ед. измерения')),
                ('value', models.IntegerField(verbose_name='Значение')),
                ('extra', django.contrib.postgres.fields.jsonb.JSONField(blank=True, default={}, null=True, verbose_name='Дополнительно')),
                ('menu', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, related_name='prices', to='menu.Menu', verbose_name='Меню')),
            ],
            options={
                'verbose_name': 'Стоимость',
                'verbose_name_plural': 'Стоимость',
            },
        ),
        migrations.AddField(
            model_name='category',
            name='group',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='category', to='menu.Group', verbose_name='Группа'),
        ),
    ]
