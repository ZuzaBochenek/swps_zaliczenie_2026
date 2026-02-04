from rest_framework.viewsets import ModelViewSet
from .models import ExchangeRequest
from .serializers import ExchangeRequestSerializer


class ExchangeRequestViewSet(ModelViewSet):
    queryset = ExchangeRequest.objects.all()
    serializer_class = ExchangeRequestSerializer
