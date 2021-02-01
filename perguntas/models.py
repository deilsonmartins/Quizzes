from django.db import models
from respostas.models import Resposta

class Pergunta(models.Model):
    label = models.CharField(max_length=100)
    respostas = models.ForeignKey(Resposta, on_delete=models.CASCADE)

    def __str__(self):
        return self.label

