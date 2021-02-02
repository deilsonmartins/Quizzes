from django.db import models
from questionarios.models import Questionario

class Pergunta(models.Model):
    label = models.CharField(max_length=100)
    questionario = models.ForeignKey(Questionario, on_delete=models.CASCADE)

    def __str__(self):
        return self.label

