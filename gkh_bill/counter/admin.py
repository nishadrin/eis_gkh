from django.contrib import admin

from .models import WaterCounter


@admin.register(WaterCounter)
class WaterCounterAdmin(admin.ModelAdmin):
    list_display = (
        'id',
        'value',
        'date',
        'flat',
        'tariff',
    )
    search_fields = ('flat', )
    list_filter = ('flat', )
