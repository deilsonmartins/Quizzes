from rest_framework.permissions import IsAuthenticated
from rest_framework.viewsets import ModelViewSet
from .serializers import RespostaSerializer
from respostas.models import Resposta

class RespostasViewSet(ModelViewSet):

    serializer_class = RespostaSerializer

    permission_classes = [IsAuthenticated]

    def get_queryset(self):
        return Resposta.objects.all()