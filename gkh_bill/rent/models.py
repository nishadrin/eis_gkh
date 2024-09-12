from django.db import models


class CalculateRent(models.Model):
    """Модель расчета квартплаты."""

    house = models.ForeignKey(
        'house.House',
        verbose_name='Адресс',
        on_delete=models.CASCADE,
    )
    month = models.PositiveSmallIntegerField(verbose_name='Месяц')


class Rent(models.Model):
    """Модель квартплаты."""

    water = models.DecimalField(
        max_digits=9,
        decimal_places=2,
        verbose_name='Водоснабжение'
    )
    maintenance = models.DecimalField(
        max_digits=9,
        decimal_places=2,
        verbose_name='Содержание общего имущества'
    )
    date = models.DateField(
        auto_now_add=True,
        verbose_name='Дата показаний',
    )

    flat = models.ForeignKey(
        'house.Flat',
        on_delete=models.CASCADE,
        verbose_name='Квартира',
    )
    calculate_rent = models.ForeignKey(
        CalculateRent,
        on_delete=models.CASCADE,
        verbose_name='Расчет кварплаты',
    )

    class Meta:
        ordering = ('flat',)
        verbose_name = 'Квартплата'
        verbose_name_plural = 'Квартплаты'

    def __str__(self):
        return str(self.flat)
