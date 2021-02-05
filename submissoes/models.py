from django.contrib.auth.models import User
from django.db import models
from respostas.models import Resposta
from perguntas.models import Pergunta

class Submissao(models.Model):
    usuario = models.ForeignKey(User, on_delete=models.CASCADE)
    pergunta = models.ForeignKey(Pergunta, on_delete=models.CASCADE)
    resposta = models.ForeignKey(Resposta, on_delete=models.CASCADE)
    acertou = models.BooleanField(default=False)

    def __str__(self):
        return self.usuario.get_username()