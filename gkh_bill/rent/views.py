from rest_framework import status
from rest_framework.generics import RetrieveAPIView
from rest_framework.response import Response
from rest_framework.views import APIView

from rent.serializers import CalculateRentSerializer
from .models import CalculateRent
from .tasks import calculation_rent


class GetCalculateRentViewSet(RetrieveAPIView):
    """Получить асчет кварплаты."""
    queryset = CalculateRent.objects.all()
    serializer_class = CalculateRentSerializer


class CreateCalculateRentViewSet(APIView):
    """Создать задачу на расчет кварплаты."""
    queryset = CalculateRent.objects.all()
    serializer_class = CalculateRentSerializer

    def post(self, request, *args, **kwargs):
        serializer = self.serializer_class(data=request.data)
        if serializer.is_valid(raise_exception=True):
            calculate_rent = serializer.save()
            calculation_rent.delay(calculate_rent.id)

            return Response(
                serializer.data,
                status=status.HTTP_201_CREATED,
            )
        return Response({'message': serializer.errors})
