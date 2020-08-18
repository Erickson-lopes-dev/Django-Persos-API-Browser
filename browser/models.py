from django.contrib.auth.models import User
from django.db import models


class CategoryContent(models.Model):
    name = models.CharField(max_length=100)
    created = models.DateField(auto_now=True)

    def __str__(self):
        return self.name


class Persos(models.Model):
    title = models.CharField(max_length=100)
    sub_title = models.CharField(max_length=255)
    content = models.TextField()
    created = models.DateField(auto_now=True)
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    categories = models.ManyToManyField(CategoryContent)

    def __str__(self):
        return self.title

