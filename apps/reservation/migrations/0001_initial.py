# -*- coding: utf-8 -*-
# Generated by Django 1.11.1 on 2017-06-01 10:56
from __future__ import unicode_literals

import django.contrib.postgres.fields.jsonb
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Reservation',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('date', models.DateField(verbose_name='Дата')),
                ('time_start', models.TimeField(verbose_name='С')),
                ('time_end', models.TimeField(blank=True, null=True, verbose_name='До')),
                ('phone_number', models.CharField(max_length=17, null=True, verbose_name='Телефон')),
                ('email', models.EmailField(blank=True, max_length=255, null=True, verbose_name='Почта')),
                ('name', models.CharField(max_length=255, verbose_name='Имя')),
                ('count_people', models.PositiveSmallIntegerField(verbose_name='Количество человек')),
                ('status', models.CharField(blank=True, choices=[('w', 'Ожидает'), ('c', 'Подтверждено'), ('d', 'Отменено')], default='w', max_length=2, verbose_name='Статус')),
                ('comment', models.TextField(blank=True, null=True, verbose_name='Коментарий')),
                ('extra', django.contrib.postgres.fields.jsonb.JSONField(blank=True, default={}, verbose_name='Экстра')),
            ],
            options={
                'verbose_name': 'Бронирование',
                'verbose_name_plural': 'Бронирование',
            },
        ),
    ]
