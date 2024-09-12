from django.contrib import admin

from .models import House, Flat


@admin.register(Flat)
class FlatAdmin(admin.ModelAdmin):
    list_display = (
        'number',
        'area',
        'house',
    )
    search_fields = ('number', 'house', )
    list_filter = ('number', 'house', )


@admin.register(House)
class HouseAdmin(admin.ModelAdmin):
    list_display = (
        'address',
        'maintenance_tariff',
    )
    search_fields = ('address', )
