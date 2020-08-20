from django.contrib.auth.models import User
from django.db import models


# Modelo das categorias
class CategoryContent(models.Model):
    # Campo com nome com maximo de 100 caractere
    name = models.CharField(max_length=100)
    # Data de criação
    created = models.DateField(auto_now=True)

    # Retorna o campo name para exibir o nome do objeto
    def __str__(self):
        return self.name


# Classe dos modelos de Persos
class Persos(models.Model):
    # titulo com 100 caracteres
    title = models.CharField(max_length=100)
    # subtitulo com maximo de 255 caractere e pode ser null ou vazio
    sub_title = models.CharField(max_length=255, null=True, blank=True)
    # campo de texto
    content = models.TextField()
    # data de criação
    created = models.DateField(auto_now=True)
    # usuário que registrou o objeto
    user = models.ForeignKey(User, related_name='persos', on_delete=models.CASCADE)
    # campo da categoria relacionada
    categories = models.ManyToManyField(CategoryContent)

    class Meta:
        # ordem que devera aparecer
        ordering = ['created']

    # Retorna o campo name para exibir o nome do objeto
    def __str__(self):
        return self.title
