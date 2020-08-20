from django.contrib.auth.models import User
from rest_framework import generics, permissions, viewsets

from api.permissions import IsUserOrReadOnly
from api.serializer import PersosSerializer, UserSerializer, CategorySerializer
from browser.models import Persos, CategoryContent


# ViewSet dos Persos contendo todos os métodos
class PersosViewSet(viewsets.ModelViewSet):
    # Especificando modelo de dados
    queryset = Persos.objects.all()

    # Quando executar a tarefa de criar
    def perform_create(self, serializer):
        # na função .save pegue o campo com nome user
        serializer.save(user=self.request.user)

    # Especificando Serializador
    serializer_class = PersosSerializer

    # Permissões authenticado ou apenas leitura
    permission_classes = [permissions.IsAuthenticatedOrReadOnly, IsUserOrReadOnly]


# View de usuários, apenas leitura do modelo
class UserViewSet(viewsets.ReadOnlyModelViewSet):
    # Especificando modelo de dados
    queryset = User.objects.all()
    # Especificando Serializador
    serializer_class = UserSerializer


# ViewSet das Categorias, apenas leitura
class CategoryContentViewSet(viewsets.ReadOnlyModelViewSet):
    # Especificando modelo de dados
    queryset = CategoryContent.objects.all()
    # Especificando Serializador
    serializer_class = CategorySerializer
