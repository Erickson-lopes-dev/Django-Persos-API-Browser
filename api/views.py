from django.contrib.auth.models import User
from rest_framework import generics, permissions

from api.permissions import IsUserOrReadOnly
from api.serializer import PersosSerializer, UserSerializer, CategorySerializer
from browser.models import Persos, CategoryContent


class PersosGenericList(generics.ListCreateAPIView):
    queryset = Persos.objects.all()

    def perform_create(self, serializer):
        serializer.save(user=self.request.user)

    serializer_class = PersosSerializer

    # authenticado ou apenas leitura
    permission_classes = [permissions.IsAuthenticatedOrReadOnly]


class PersosGenericDetail(generics.RetrieveUpdateDestroyAPIView):
    queryset = Persos.objects.all()
    serializer_class = PersosSerializer
    permission_classes = [permissions.IsAuthenticatedOrReadOnly, IsUserOrReadOnly]


class UserList(generics.ListAPIView):
    queryset = User.objects.all()
    serializer_class = UserSerializer


class UserDetails(generics.RetrieveAPIView):
    queryset = User.objects.all()
    serializer_class = UserSerializer


class CategoryContentList(generics.ListAPIView):
    queryset = CategoryContent.objects.all()
    serializer_class = CategorySerializer


class CategoryContentDetail(generics.RetrieveAPIView):
    queryset = CategoryContent.objects.all()
    serializer_class = CategorySerializer
