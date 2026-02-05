from rest_framework.viewsets import ModelViewSet
from rest_framework.permissions import IsAuthenticated
from rest_framework.decorators import action
from rest_framework.response import Response

from .models import Listing
from .serializers import ListingSerializer
from .permissions import IsOwnerOrReadOnly


class ListingViewSet(ModelViewSet):
    queryset = Listing.objects.all()
    serializer_class = ListingSerializer
    permission_classes = [IsAuthenticated, IsOwnerOrReadOnly]

    def perform_create(self, serializer):
        serializer.save(owner=self.request.user)

    @action(detail=False, methods=['get'])
    def my(self, request):
        queryset = self.queryset.filter(
            owner=request.user,
            status='active'
        )
        serializer = self.get_serializer(queryset, many=True)
        return Response(serializer.data)

