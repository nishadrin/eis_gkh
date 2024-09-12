from rest_framework import serializers

from counter.serializers import WaterCounterSerializer
from .models import House, Flat

ERRORS = {
    'unique_address': 'Такая квартира есть в базе.',
}


class FlatSerializer(serializers.ModelSerializer):
    """Сериализатор квартиры."""
    water_counters = WaterCounterSerializer(many=True, read_only=True, )

    class Meta:
        model = Flat
        fields = ('id', 'number', 'area', 'house', 'water_counters', )
        read_only_fields = ('water_counters', )
        validators = [
            serializers.UniqueTogetherValidator(
                queryset=Flat.objects.all(),
                fields=['number', 'house'],
                message=ERRORS.get('unique_address'),
            )
        ]


class HouseSerializer(serializers.ModelSerializer):
    """Сериализатор дома."""
    flats = FlatSerializer(many=True, )

    class Meta:
        model = House
        fields = ('id', 'address', 'maintenance_tariff', 'flats', )
