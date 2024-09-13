from celery import shared_task

from house.models import Flat
from django.utils.datetime_safe import date
from django.db.models import OuterRef
from counter.models import WaterCounter
from django.db.models import Subquery
from django.db.models import F
from django.db.models import Sum

from rent.models import CalculateRent, Rent


@shared_task
def calculation_rent(calculation_rent_id: int) -> None:
    calculation_rent = CalculateRent.objects.get(id=calculation_rent_id)

    previous_month = WaterCounter.objects.filter(
        date__month=(calculation_rent.month - 1),
        date__year=date.today().year,
        flat=OuterRef('pk'),
        tariff=OuterRef('water_counters__tariff')
    )

    qs_bill = Flat.objects.filter(
        house=calculation_rent.house.id
    ).prefetch_related('water_counters').filter(
        water_counters__date__month=calculation_rent.month,
        water_counters__date__year=date.today().year
    ).alias(
        previous_value=Subquery(previous_month.values('value')),
        cost=((F('water_counters__value') - F('previous_value'))
              * F('water_counters__tariff__price'))
    ).values('flat_id').annotate(
        water_cost=Sum('cost'),
        maintenance_cost=F('area') * F('house__maintenance_tariff__price')
    )

    rents = []
    for data in qs_bill:
        flat_id = data.get('flat_id')
        water_cost = data.get('water_cost')
        maintenance_cost = data.get('maintenance_cost')
        rents.append(
            Rent(
                flat=Flat.objects.get(id=flat_id),
                water = water_cost,
                maintenance = maintenance_cost,
            )
        )

    Rent.objects.bulk_create(rents, batch_size=5000)
