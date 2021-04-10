from rest_framework.serializers import ModelSerializer
from avaliacoes.models import Avaliacao

class AvalicaoSerializer(ModelSerializer):
    class Meta:
        model = Avaliacao
        fields = ('id', 'user', 'comentario', 'nota', 'data')