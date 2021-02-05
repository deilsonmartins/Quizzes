from rest_framework.serializers import ModelSerializer, SerializerMethodField
from submissoes.models import Submissao
from perguntas.api.serializers import PerguntaSerializer
from respostas.api.serializers import RespostaSerializer
from django.contrib.auth.models import User

class UserSerializer(ModelSerializer):
    class Meta:
        model = User
        fields = ["id", "username"]

class SubmissoesSerializer(ModelSerializer):

    pergunta = PerguntaSerializer()
    resposta = RespostaSerializer()
    usuario = UserSerializer()

    class Meta:
        model = Submissao
        fields = "__all__" 
    