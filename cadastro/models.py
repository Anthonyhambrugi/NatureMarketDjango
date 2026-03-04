from django.db import models
from django.contrib.auth.models import User
from django.contrib.auth.models import Group
from django.core.exceptions import ObjectDoesNotExist
from cloudinary.models import CloudinaryField

# App de cadastro, bem tranquilão

class NmUserSort(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE, null=True, blank=True)

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

class UserMod(models.Model):
    user = models.ForeignKey(
    User,
    on_delete=models.CASCADE,
    null=True,
    blank=True
)
    fotodeperfil = CloudinaryField('foto de perfil', null=True, blank=True)
    bio = models.TextField(blank=True, null=True)
    tipo_user = models.CharField(max_length=20, default='Cliente')

    def __str__(self):
        return self.user.username
