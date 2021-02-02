from django.urls import path, include
from django.conf.urls import url
from django.contrib import admin
from rest_framework import routers
from questionarios.api.viewset import QuestionarioViewSet
from perguntas.api.viewsets import PerguntaViewSet
from respostas.api.viewsets import RespostasViewSet

router = routers.DefaultRouter()
router.register(r'respostas', RespostasViewSet, basename="Resposta")
router.register(r'questionarios', QuestionarioViewSet, basename="Questionario")
router.register(r'perguntas', PerguntaViewSet, basename="Pergunta")

urlpatterns = [
    path('', include(router.urls)),
    path('admin/', admin.site.urls)
]
