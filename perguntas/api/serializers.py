from rest_framework.serializers import ModelSerializer
from perguntas.models import Pergunta
from questionarios.api.serializers import QuestionarioSerializer

class PerguntaSerializer(ModelSerializer):

    questionario = QuestionarioSerializer()
    class Meta:
        model = Pergunta
        fields = "__all__"