from django.db import models


class InstagramManager(models.Manager):

    def get_queryset(self):
        return super(InstagramManager, self).get_queryset().select_related('category')
