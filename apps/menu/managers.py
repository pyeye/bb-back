from django.db import models


class MenuManager(models.Manager):

    def get_queryset(self):
        return super(MenuManager, self).get_queryset().prefetch_related('prices').select_related('category')


class CategoryManager(models.Manager):

    def get_queryset(self):
        return super(CategoryManager, self).get_queryset().prefetch_related('images')