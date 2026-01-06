from django.db import models

# Create your models here.

class LoginModel (models.Model):
    username = models.CharField()
    password = models.CharField(max_length=15)

    def __str__(self):
        return self.nome