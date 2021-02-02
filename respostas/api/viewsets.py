from rest_framework.viewsets import ModelViewSet
from .serializers import RespostaSerializer
from respostas.models import Resposta

class RespostasViewSet(ModelViewSet):

    serializer_class = RespostaSerializer

    def get_queryset(self):
        return Resposta.objects.all()