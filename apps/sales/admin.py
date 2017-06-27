from django.contrib import admin
from django.db import models
from pagedown.widgets import AdminPagedownWidget

from .models import Month, Sale, Day


class SaleInline(admin.TabularInline):
    model = Sale
    extra = 3

    fields = ['name', 'info', 'day', 'image']

    formfield_overrides = {
        models.TextField: {'widget': AdminPagedownWidget},
    }


class MonthAdmin(admin.ModelAdmin):

    inlines = [SaleInline]
    list_display = ('name', 'code')
    search_fields = ['name']


class DayAdmin(admin.ModelAdmin):

    list_display = ('name', 'code')


admin.site.register(Month, MonthAdmin)
admin.site.register(Day, DayAdmin)
