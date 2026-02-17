from django.db import models
from django.contrib.auth.models import User

# App de cadastro, bem tranquilão

class NmUserSort(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)

    TIPO_USER_CHOICES = [
        ('Comprador', 'Comprador'),
        ('Vendedor', 'Vendedor'),
        ('Administrador', 'Administrador'),
    ]
    tipo_user = models.CharField(
        max_length=20,
        choices=TIPO_USER_CHOICES,
        default='Comprador',
    )

    def __str__(self):
        return self.tipo_user