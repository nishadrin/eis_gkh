from rest_framework import serializers

from .models import CalculateRent, Rent

ERRORS = {
    'unique_address': 'Такая квартира есть в базе',
}


class RentSerializer(serializers.ModelSerializer):
    """Сериализатор кварплаты."""
    class Meta:
        model = Rent
        fields = '__all__'


class CalculateRentSerializer(serializers.ModelSerializer):
    """Сериализатор расчета кварплаты."""
    rents = RentSerializer(many=True, read_only=True, )

    class Meta:
        model = CalculateRent
        fields = ('id', 'house', 'month', 'rents', )
        read_only_fields = ('rents',)
