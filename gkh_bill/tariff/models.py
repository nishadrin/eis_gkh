from django.db import models


class Tariff(models.Model):
    """Модель тарифа."""

    TARIFF_NAME = [
        ('hot', 'Горячая вода'),
        ('cold', 'Холодная вода'),
        ('maintenance', 'Содержание общего имущества')
    ]
    name = models.CharField(
        choices=TARIFF_NAME,
        max_length=50,
        verbose_name='Наименование',
    )
    price = models.DecimalField(
        max_digits=7,
        decimal_places=2,
        verbose_name='Цена',
    )

    class Meta:
        ordering = ('name',)
        verbose_name = 'Тариф'
        verbose_name_plural = 'Тарифы'

    def __str__(self):
        return self.name
