from django.contrib import admin

from .models import Image, Album


class ImageInline(admin.TabularInline):
    model = Image
    extra = 3
    exclude = ('info',)


class AlbumAdmin(admin.ModelAdmin):

    def date_f(self, obj):
        return obj.date.strftime("%d.%m.%Y")
    date_f.admin_order_field = 'created_at'
    date_f.short_description = 'Созданно'

    inlines = [ImageInline]
    list_display = ('name', 'description', 'date_f')
    search_fields = ['name']
    exclude = ('description',)
    date_hierarchy = 'created_at'


class ImageAdmin(admin.ModelAdmin):
    def created_at_f(self, obj):
        return obj.created_at.strftime("%d.%m.%Y")

    created_at_f.admin_order_field = 'created_at'
    created_at_f.short_description = 'Созданно'

    list_display = ('info', 'created_at_f')
    date_hierarchy = 'created_at'


admin.site.register(Album, AlbumAdmin)

