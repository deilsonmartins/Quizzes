from django.contrib.auth.models import User

from django.db import models

from questionarios.models import Questionario

class Submissao(models.Model):
    usuario = models.ForeignKey(User, on_delete=models.CASCADE)
    questionario = models.ForeignKey(Questionario, on_delete=models.CASCADE)
    score = models.IntegerField()

    def __str__(self):
        return self.usuario.get_username()