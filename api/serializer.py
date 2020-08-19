from django.contrib.auth.models import User
from rest_framework import serializers
from browser.models import Persos, CategoryContent


class CategorySerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = CategoryContent
        fields = ['url', 'id', 'name']


class PersosSerializer(serializers.HyperlinkedModelSerializer):
    # Ler o campo capturando o username do objeto
    user = serializers.ReadOnlyField(source='user.username')
    categories = serializers.HyperlinkedRelatedField(many=True, read_only=True, view_name='categorycontent-detail')

    class Meta:
        model = Persos
        fields = ['url', 'id', 'title', 'sub_title', 'content', 'categories', 'user']


class UserSerializer(serializers.HyperlinkedModelSerializer):
    # buscar todos os persos com chave-primaria com o usuario especifico
    # persos = serializers.PrimaryKeyRelatedField(many=True, queryset=Persos.objects.all())

    # buscar todos os persos com chave-primaria com o usuario especifico em modo de link
    persos = serializers.HyperlinkedRelatedField(many=True, view_name='persos-detail', read_only=True)

    class Meta:
        model = User
        # isso exibirá convertido os persos que o usuário tem
        fields = ['url', 'id', 'username', 'persos']
