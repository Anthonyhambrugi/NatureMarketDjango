from django.db import models
from django.contrib.auth.models import User
from django.contrib.auth.models import Group
from django.core.exceptions import ObjectDoesNotExist

# App de cadastro, bem tranquilão

class NmUserSort(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)

    TIPO_USER_CHOICES = [
        ('Cliente', 'Cliente'),
        ('Vendedor', 'Vendedor'),
    ]
    tipo_user = models.CharField(
        max_length=20,
        choices=TIPO_USER_CHOICES,
        default='Cliente',
    )

    def __str__(self):
        return self.tipo_user
        