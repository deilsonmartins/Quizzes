from rest_framework.serializers import ModelSerializer
from categorias.models import Categoria

class CategoriaSerializer(ModelSerializer):
    class Meta:
        model = Categoria
        exclude = ["id"]
        