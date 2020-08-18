from django.db import models


class PersosContent(models.Model):
    title = models.CharField(max_length=100)
    sub_title = models.CharField(max_length=255)
    content = models.TextField()
    created = models.DateField(auto_now=True)

    def __str__(self):
        return self.title

