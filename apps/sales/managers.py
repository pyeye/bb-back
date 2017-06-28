from django.db import models


class MonthManager(models.Manager):

    def get_queryset(self):
        return super(MonthManager, self).get_queryset().prefetch_related('current_month')


class DaySaleManager(models.Manager):

    def get_queryset(self):
        return super(DaySaleManager, self).get_queryset().select_related('month').select_related('days').prefetch_related('sales')
