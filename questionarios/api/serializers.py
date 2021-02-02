from rest_framework.serializers import ModelSerializer
from questionarios.models import Questionario
from categorias.api.serializers import CategoriaSerializer

class QuestionarioSerializer(ModelSerializer):

    categoria = CategoriaSerializer()
    
    class Meta:
        model = Questionario
        fields = "__all__"