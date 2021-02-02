from rest_framework.serializers import ModelSerializer
from respostas.models import Resposta
from perguntas.api.serializers import PerguntaSerializer

class RespostaSerializer(ModelSerializer):
    pergunta = PerguntaSerializer()

    class Meta:
        model = Resposta
        exclude = ["correta"]