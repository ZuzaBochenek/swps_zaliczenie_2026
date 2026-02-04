from rest_framework.viewsets import ModelViewSet
from .models import Listing
from .serializers import ListingSerializer


class ListingViewSet(ModelViewSet):
    queryset = Listing.objects.all()
    serializer_class = ListingSerializer
