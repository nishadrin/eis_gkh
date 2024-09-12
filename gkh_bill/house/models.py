from django.db import models
from django.core.validators import MinValueValidator


class House(models.Model):
    """Модель дома."""

    address = models.CharField(max_length=255, verbose_name='Адрес', )

    maintenance_tariff = models.ForeignKey(
        'Tariff',
        verbose_name='Тариф за содержание общего имущества',
        on_delete=models.CASCADE,
    )

    class Meta:
        ordering = ('address', )
        verbose_name = 'Дом'
        verbose_name_plural = 'Дома'


    def __str__(self):
        return self.address


class Flat(models.Model):
    """Модель квартиры."""

    number = models.PositiveIntegerField(
        verbose_name='Номер квартиры',
        validators=[MinValueValidator(1), ]
    )
    area = models.DecimalField(
        max_digits=6,
        decimal_places=2,
        verbose_name='Площадь квартиры',
    )

    house = models.ForeignKey(
        House,
        on_delete=models.CASCADE,
        related_name='flat',
    )

    class Meta:
        ordering = ('number', )
        verbose_name = 'Квартира'
        verbose_name_plural = 'Квартиры'

        constraints = [
            models.UniqueConstraint(
                fields=['number', 'house', ],
                name='unique_address'
            )
        ]

    def __str__(self):
        return str(self.number)