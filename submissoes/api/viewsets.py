from rest_framework.permissions import IsAuthenticated
from rest_framework.viewsets import ModelViewSet
from django.contrib.auth.models import User
from rest_framework.response import Response
from .serializers import SubmissoesSerializer, UserSerializer
from submissoes.models import Submissao
from respostas.models import Resposta
from perguntas.models import Pergunta
from questionarios.models import Questionario
from django.contrib.auth.models import User

class SubmissoesViewSet(ModelViewSet):

    serializer_class = SubmissoesSerializer

    permission_classes = [IsAuthenticated]
    
    def list(self, request):

        usuario = User.objects.get(id=request.user.id)

        submissoes = Submissao.objects.filter(usuario=usuario)
        score = 0
        for submissao in submissoes:
            if submissao.acertou:
                score += 1
        
        return Response({"Usuario": UserSerializer(usuario).data, "score": score})
                
    
    def create(self, request):
    
        id_resposta = request.data['id_resposta']

        resposta = Resposta.objects.get(id=id_resposta)
        pergunta = Pergunta.objects.get(id=resposta.pergunta.id)

        usuario = User.objects.get(id=request.user.id)

        submissao, created = Submissao.objects.get_or_create(usuario=usuario, pergunta=pergunta, resposta=resposta)

        if resposta.correta == True:
            submissao.acertou = True
            submissao.save()

        return Response(SubmissoesSerializer(submissao).data)
