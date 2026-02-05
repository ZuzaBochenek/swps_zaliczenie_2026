from rest_framework.viewsets import ModelViewSet
from .models import Material
from .serializers import MaterialSerializer
from rest_framework.decorators import action
from rest_framework.response import Response


class MaterialViewSet(ModelViewSet):
    queryset = Material.objects.all()
    serializer_class = MaterialSerializer
    
    @action(detail=False, methods=['get'])
    def search(self, request):
        prefix = request.query_params.get('q', '')
        queryset = self.queryset.filter(title__istartswith=prefix)
        serializer = self.get_serializer(queryset, many=True)
        return Response(serializer.data)
