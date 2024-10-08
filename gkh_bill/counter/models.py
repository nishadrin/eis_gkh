from django.db import models
from django.core.validators import MinValueValidator


class WaterCounter(models.Model):
    """Модель счетчика воды."""

    value = models.PositiveIntegerField(
        verbose_name='Показания счетчика',
        validators=[MinValueValidator(1), ],
        help_text='Введите показания',
    )
    date = models.DateField(
        auto_now=True,
        verbose_name='Дата показаний',
    )

    tariff = models.ForeignKey(
        'tariff.Tariff',
        verbose_name='Тариф',
        on_delete=models.CASCADE,
    )
    flat = models.ForeignKey(
        'house.Flat',
        verbose_name='Квартира',
        on_delete=models.CASCADE,
    )

    class Meta:
        ordering = ('tariff',)
        default_related_name = 'water_counters'
        verbose_name = 'Счетчик воды'
        verbose_name_plural = 'Счетчики воды'

    def __str__(self):
        return str(self.value)
