# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models

class Resposta(models.Model):
    label = models.CharField(max_length=100)
    correta = models.BooleanField(default=False)

    def __str__(self):
        return self.label