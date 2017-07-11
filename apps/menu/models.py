import uuid

from django.db import models
from django.contrib.postgres.fields import JSONField
from django.dispatch import receiver

from versatileimagefield.fields import VersatileImageField
from versatileimagefield.image_warmer import VersatileImageFieldWarmer

from .managers import MenuManager, CategoryManager


def upload_location(instance, filename):
    filename = str(uuid.uuid4())[:13] + '_' + filename
    return "menu/{0}".format(filename)


class Menu(models.Model):
    name = models.CharField(max_length=255, null=False, unique=True, blank=False, verbose_name='Название')
    description = models.TextField(null=True, blank=True, verbose_name='Описание')
    category = models.ForeignKey('Category', related_name='menu', verbose_name='Категория')
    created_at = models.DateTimeField(auto_now=True, null=False, blank=True, verbose_name='Созданно')
    is_active = models.BooleanField(default=True, null=False, blank=True, verbose_name='Активированно')
    extra = JSONField(blank=True, null=True, default={}, verbose_name='Дополнительно')

    objects = models.Manager()
    related_objects = MenuManager()

    def __str__(self):
        return self.name

    class Meta:
        verbose_name = 'Меню'
        verbose_name_plural = 'Меню'


class Category(models.Model):

    TEMPLATE_VERTICAL = 'vertical'
    TEMPLATE_HORIZONTAL = 'horizontal'
    TEMPLATE_HORIZONTAL_HALF = 'horizontal_half'
    TEMPLATE_HALF = 'half'
    TEMPLATE_FULL = 'full'
    TEMPLATE_CHOICES = (
        (TEMPLATE_VERTICAL, 'Вертикальный'),
        (TEMPLATE_HORIZONTAL, 'Горизонтальный'),
        (TEMPLATE_HORIZONTAL_HALF, 'Горизонтальный половина'),
        (TEMPLATE_HALF, 'Половина'),
        (TEMPLATE_FULL, 'Полный'),
    )

    name = models.CharField(max_length=255, null=False, unique=True, blank=False, verbose_name='Название')
    code = models.CharField(max_length=128, null=False, blank=False, verbose_name='Код')
    group = models.ForeignKey('Group', related_name='category', verbose_name='Группа')
    template = models.CharField(max_length=128, default=TEMPLATE_FULL, choices=TEMPLATE_CHOICES, null=False, blank=True, verbose_name='Название')
    extra = JSONField(blank=True, null=True, default={}, verbose_name='Дополнительно')

    def __str__(self):
        return self.name

    objects = models.Manager()
    related_objects = CategoryManager()

    class Meta:
        verbose_name = 'Категория'
        verbose_name_plural = 'Категории'


class Group(models.Model):
    name = models.CharField(max_length=255, null=False, unique=True, blank=False, verbose_name='Название')
    code = models.CharField(max_length=128, null=False, unique=True, blank=False, verbose_name='Код')
    extra = JSONField(blank=True, null=True, default={}, verbose_name='Дополнительно')

    def __str__(self):
        return self.name

    class Meta:
        verbose_name = 'Группа'
        verbose_name_plural = 'Группы'


class Price(models.Model):
    menu = models.ForeignKey(Menu, on_delete=models.CASCADE, blank=True, null=True, related_name='prices', verbose_name='Меню')
    count = models.FloatField(null=True, blank=True, verbose_name='Количество (250/0.75)')
    measure = models.CharField(max_length=64, null=True, blank=True, verbose_name='Ед. измерения (гр./шт./л./мл./на чаше')
    value = models.IntegerField(null=False, blank=False, verbose_name='Цена')
    extra = JSONField(blank=True, null=True, default={}, verbose_name='Дополнительно')

    def __str__(self):
        return str(self.value)

    class Meta:
        verbose_name = 'Стоимость'
        verbose_name_plural = 'Стоимость'


class Image(models.Model):
    info = models.CharField(max_length=255, null=True, blank=True, verbose_name='Информация')
    created_at = models.DateTimeField(auto_now=True, null=False, blank=True, verbose_name='Созданно')
    category = models.ForeignKey(Category, on_delete=models.CASCADE, related_name='images', null=False, blank=False, verbose_name='Фотография')
    image = VersatileImageField(upload_to=upload_location, null=False, blank=False, verbose_name='Фото')

    class Meta:
        verbose_name = 'Фотография'
        verbose_name_plural = 'Фотографии'


@receiver(models.signals.post_save, sender=Image)
def warm_gallery_image_images(sender, instance, **kwargs):
    menu_img_warmer = VersatileImageFieldWarmer(
        instance_or_queryset=instance,
        rendition_key_set='menu_image',
        image_attr='image'
    )
    num_created, failed_to_create = menu_img_warmer.warm()
