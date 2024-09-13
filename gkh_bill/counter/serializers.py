from django.utils.datetime_safe import date
from rest_framework import serializers

from .models import WaterCounter


class WaterCounterSerializer(serializers.ModelSerializer):
    """Сериализатор счетчика воды."""

    class Meta:
        model = WaterCounter
        fields = ('value', 'tariff', 'flat', 'date', )
        read_only_fields = ('date', )

    def create(self, validated_data) -> WaterCounter:
        """
        При повторном создании данных в этом месяце, они обновляются.
        :param validated_data:
        :return WaterCounter:
        """
        water_counter = WaterCounter.objects.filter(
            date__month=date.today().month,
            date__year=date.today().year,
            **validated_data,
        )
        if water_counter:
            water_counter = water_counter.first()
            water_counter.value = validated_data.pop('value')
            water_counter.save()
        else:
            water_counter = WaterCounter.objects.create(**validated_data)

        return water_counter
