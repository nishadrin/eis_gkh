from rest_framework.permissions import AllowAny

from gkh_bill.views import CreateListRetrieveViewSet
from .models import House, Flat
from .serializers import HouseSerializer, FlatSerializer


class HouseViewSet(CreateListRetrieveViewSet):
    """Вьюз дома."""

    queryset = House.objects.all()
    permission_classes = (AllowAny, )
    serializer_class = HouseSerializer


class FlatViewSet(CreateListRetrieveViewSet):
    """Вьюз квартиры."""

    queryset = Flat.objects.all()
    permission_classes = (AllowAny, )
    serializer_class = FlatSerializer
