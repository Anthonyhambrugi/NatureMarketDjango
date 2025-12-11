from django.db import models

# Create your models here.

class LoginModel (models.Model):
    nome = models.CharField()
    sbrnom = models.CharField()
    username = models.CharField(max_length=20)
    senha = models.CharField(max_length=8)

    def __str__(self):
        return self.nome