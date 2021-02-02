from django.db import models
from perguntas.models import Pergunta

class Resposta(models.Model):
    pergunta = models.ForeignKey(Pergunta, on_delete=models.CASCADE)
    label = models.CharField(max_length=100)
    correta = models.BooleanField(default=False)

    def __str__(self):
        return self.label