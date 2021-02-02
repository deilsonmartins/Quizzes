from rest_framework.viewsets import ModelViewSet
from questionarios.models import Questionario
from .serializers import QuestionarioSerializer

class QuestionarioViewSet(ModelViewSet):

    serializer_class = QuestionarioSerializer

    def get_queryset(self):
        return Questionario.objects.all()