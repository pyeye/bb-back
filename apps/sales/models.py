import uuid

from django.db import models
from django.dispatch import receiver
from django.contrib.postgres.fields import JSONField

from versatileimagefield.fields import VersatileImageField
from versatileimagefield.image_warmer import VersatileImageFieldWarmer

from .managers import MonthManager, DaySaleManager


def upload_location(instance, filename):
    filename = str(uuid.uuid4())[:13] + '_' + filename
    return "sales/{0}".format(filename)


class Month(models.Model):
    date = models.DateField(null=False, blank=False, verbose_name='Дата')
    extra = JSONField(blank=True, null=True, default={}, verbose_name='Дополнительно')

    objects = models.Manager()
    related_objects = MonthManager()


    class Meta:
        verbose_name = 'Месяц'
        verbose_name_plural = 'Месяцы'


class Day(models.Model):
    name = models.CharField(max_length=255, null=False, blank=False, verbose_name='День')
    code = models.PositiveSmallIntegerField(null=False, blank=False, unique=True, verbose_name='Код')
    extra = JSONField(blank=True, null=True, default={}, verbose_name='Дополнительно')

    def __str__(self):
        return self.name

    class Meta:
        verbose_name = 'День'
        verbose_name_plural = 'Дни'


class Sale(models.Model):
    name = models.CharField(max_length=255, null=False, blank=False, verbose_name='Название')
    info = models.TextField(null=True, blank=True, verbose_name='Информация')
    image = VersatileImageField(upload_to=upload_location, null=False, blank=False, verbose_name='Фото')
    is_active = models.BooleanField(default=True, null=False, blank=True, verbose_name='Активированно')
    created_at = models.DateTimeField(auto_now=True, null=False, blank=True, verbose_name='Созданно')
    extra = JSONField(blank=True, null=True, default={}, verbose_name='Дополнительно')

    def __str__(self):
        return self.name

    class Meta:
        verbose_name = 'Акция'
        verbose_name_plural = 'Акции'


class DaySaleRel(models.Model):
    day = models.ForeignKey(Day, blank=False, null=False, related_name='current_days', verbose_name='Дни')
    sales = models.ManyToManyField('Sale', related_name='current_sales', verbose_name='Акции')
    month = models.ForeignKey(Month, blank=False, null=False, related_name='current_month', verbose_name='Месяцы')

    objects = models.Manager()
    related_objects = DaySaleManager()

    class Meta:
        ordering = ['day__code']


@receiver(models.signals.post_save, sender=Sale)
def warm_gallery_image_images(sender, instance, **kwargs):
    sale_img_warmer = VersatileImageFieldWarmer(
        instance_or_queryset=instance,
        rendition_key_set='sales_image',
        image_attr='image'
    )
    num_created, failed_to_create = sale_img_warmer.warm()

