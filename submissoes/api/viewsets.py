from rest_framework.viewsets import ModelViewSet
from django.contrib.auth.models import User
from rest_framework.response import Response
from .serializers import SubmissoesSerializer
from submissoes.models import Submissao
from respostas.models import Resposta
from perguntas.models import Pergunta
from django.contrib.auth.models import User

class SubmissoesViewSet(ModelViewSet):

    serializer_class = SubmissoesSerializer

    def get_queryset(self):
        return Submissao.objects.all()
    
    def create(self, request):
    
        id_resposta = request.data['id_resposta']
        ######### provisorio ###########
        id_usuario = request.data['id_usuario']

        resposta = Resposta.objects.get(id=id_resposta)
        pergunta = Pergunta.objects.get(id=resposta.pergunta.id)

        usuario = User.objects.get(id=id_usuario)

        if resposta.correta == True:

            submissao, created = Submissao.objects.get_or_create(usuario=usuario, pergunta=pergunta, resposta=resposta)
            submissao.acertou = True
            submissao.save()

        return Response(SubmissoesSerializer(submissao).data,)