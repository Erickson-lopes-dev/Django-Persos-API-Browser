from django.contrib.auth.models import User
from rest_framework import serializers

from browser.models import Persos, CategoryContent


# Serializer das categorias, eviando na request o link do mesmo com id e nome
class CategorySerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        # modelo de dados que será usado
        model = CategoryContent
        # campos
        fields = ['url', 'id', 'name']


# Serializer dos Persos(Conteúdo do site), serializando com links
class PersosSerializer(serializers.HyperlinkedModelSerializer):

    # Ler o campo capturando o username do objeto
    user = serializers.ReadOnlyField(source='user.username')
    # user = serializers.HyperlinkedIdentityField(many=True, queryset=User.objects.all(), )

    # serializando para o recurso do campo categories seja um link para a categoria
    categories = serializers.HyperlinkedRelatedField(many=True, read_only=True, view_name='categorycontent-detail')

    class Meta:
        # modelo de dados que será usado
        model = Persos
        fields = ['url', 'id', 'title', 'sub_title', 'content', 'categories', 'user']


# Serializer dos Usuarios do sistema, serializando com links
class UserSerializer(serializers.HyperlinkedModelSerializer):
    # buscar todos os persos com chave-primaria com o usuario especifico
    # persos = serializers.PrimaryKeyRelatedField(many=True, queryset=Persos.objects.all())

    # buscar todos os persos com chave-primaria com o usuario especifico em modo de link
    persos = serializers.HyperlinkedRelatedField(many=True, view_name='persos-detail', read_only=True)

    class Meta:
        # modelo de dados que será usado
        model = User
        # isso exibirá convertido os persos que o usuário tem
        fields = ['url', 'id', 'username', 'email', 'persos']
