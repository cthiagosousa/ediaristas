from rest_framework.serializers import ModelSerializer
from web.models import Diarist

class DiaristCitySerializer(ModelSerializer):
    class Meta:
        model = Diarist
        fields = ('nome_completo', 'imagem_usuario', 'cidade',)
