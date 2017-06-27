from django.db import models


class MonthManager(models.Manager):

    def get_queryset(self):
        return super(MonthManager, self).get_queryset().prefetch_related('sales')


class SaleManager(models.Manager):

    def get_queryset(self):
        return super(SaleManager, self).get_queryset().prefetch_related('day')
