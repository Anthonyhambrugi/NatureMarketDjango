from django.db import models

# Create your models here.
class CadItmModel (models.Model):
    titulo = models.CharField()
    desc = models.TextField()
    username = models.CharField(max_length=20)
    senha = models.CharField(max_length=8)