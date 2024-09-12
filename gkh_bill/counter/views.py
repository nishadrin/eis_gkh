from rest_framework.permissions import AllowAny

from .models import WaterCounter
from .serializers import WaterCounterSerializer
from gkh_bill.views import CreateListRetrieveViewSet


class WaterCounterViewSet(CreateListRetrieveViewSet):
    """Вьюз дома."""

    queryset = WaterCounter.objects.all()
    permission_classes = (AllowAny, )
    serializer_class = WaterCounterSerializer
