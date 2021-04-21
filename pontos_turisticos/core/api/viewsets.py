from rest_framework.viewsets import ModelViewSet
from rest_framework.decorators import action
from core.models import PontoTuristico
from .serializers import PontoTuristicoSerializer

class PontoTuristicoViewSet(ModelViewSet):
    serializer_class = PontoTuristicoSerializer
    queryset = PontoTuristico.objects.all()
    
    @action(methods=['get'], detail=True)
    def denunciar(self, request, pk=None):
        pass
        
    
    