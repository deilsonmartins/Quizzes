# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models

from categorias.models import Categoria

from perguntas.models import Pergunta

from categorias.models import Categoria

class Questionario(models.Model):
    categoria = models.ForeignKey(Categoria, on_delete=models.CASCADE)
    nome = models.CharField(max_length=100)
    descricao = models.TextField()
    perguntas = models.ForeignKey(Pergunta, on_delete=models.CASCADE)
    data = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.nome