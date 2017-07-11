from django.contrib import admin
from django.db import models
from pagedown.widgets import AdminPagedownWidget

from .models import Month, Sale, Day, DaySaleRel


class DayAdmin(admin.ModelAdmin):

    list_display = ('name', 'code')


class SaleAdmin(admin.ModelAdmin):

    list_display = ('name', 'is_active')
    exclude = ('info', 'extra')

    formfield_overrides = {
        models.TextField: {'widget': AdminPagedownWidget},
    }


class DaySaleInline(admin.TabularInline):
    model = DaySaleRel
    extra = 3
    filter_horizontal = ('sales',)


class MonthAdmin(admin.ModelAdmin):

    inlines = [DaySaleInline]
    list_display = ('date',)


admin.site.register(Day, DayAdmin)
admin.site.register(Sale, SaleAdmin)
admin.site.register(Month, MonthAdmin)

