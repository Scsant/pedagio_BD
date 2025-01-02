from rest_framework.viewsets import ModelViewSet
from .models import ValePedagio
from .serializers import ValePedagioSerializer

class ValePedagioViewSet(ModelViewSet):
    queryset = ValePedagio.objects.all()  # Recupera todos os registros do banco de dados
    serializer_class = ValePedagioSerializer  # Define o serializer que será usado

