from django.contrib.auth.models import User
from rest_framework import generics, permissions, viewsets

from api.permissions import IsUserOrReadOnly
from api.serializer import PersosSerializer, UserSerializer, CategorySerializer
from browser.models import Persos, CategoryContent


class PersosViewSet(viewsets.ModelViewSet):
    queryset = Persos.objects.all()

    def perform_create(self, serializer):
        serializer.save(user=self.request.user)

    serializer_class = PersosSerializer

    # authenticado ou apenas leitura
    permission_classes = [permissions.IsAuthenticatedOrReadOnly, IsUserOrReadOnly]


class UserViewSet(viewsets.ReadOnlyModelViewSet):
    queryset = User.objects.all()
    serializer_class = UserSerializer


class CategoryContentViewSet(viewsets.ReadOnlyModelViewSet):
    queryset = CategoryContent.objects.all()
    serializer_class = CategorySerializer
