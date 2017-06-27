from django.contrib import admin

from .models import Menu, Price, Category, Group, Image


class ImageInline(admin.TabularInline):
    model = Image
    extra = 3


class PriceInline(admin.TabularInline):
    model = Price
    extra = 1


class MenuAdmin(admin.ModelAdmin):
    inlines = [PriceInline]

    def created_at_f(self, obj):
        return obj.created_at.strftime("%d.%m.%Y")

    created_at_f.admin_order_field = 'created_at'
    created_at_f.short_description = 'Созданно'

    def prices(self, obj):
        return obj.prices.all()

    list_display = ('name', 'created_at_f', 'is_active')
    list_filter = ['is_active']
    #list_editable = ['is_special']
    search_fields = ['name']
    date_hierarchy = 'created_at'


class CategoryAdmin(admin.ModelAdmin):
    inlines = [ImageInline]
    list_display = ('name', 'group')
    search_fields = ['name']


class GroupAdmin(admin.ModelAdmin):
    list_display = ('name', 'code')
    search_fields = ['name']


admin.site.register(Menu, MenuAdmin)
admin.site.register(Category, CategoryAdmin)
admin.site.register(Group, GroupAdmin)

