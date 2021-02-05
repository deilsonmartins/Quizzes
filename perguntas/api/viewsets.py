from rest_framework.permissions import IsAuthenticated
from rest_framework.viewsets import ModelViewSet
from perguntas.models import Pergunta
from .serializers import PerguntaSerializer

class PerguntaViewSet(ModelViewSet):

    serializer_class = PerguntaSerializer
    
    permission_classes = [IsAuthenticated]

    def get_queryset(self):
        return Pergunta.objects.all()