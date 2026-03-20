from django.db import models
from django.contrib.auth.models import User
from cloudinary.models import CloudinaryField

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
        return f"{self.user.username} - {self.tipo_user}"


class UserMod(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE, null=True, blank=True)
    fotodeperfil = CloudinaryField('foto de perfil', null=True, blank=True)
    bio = models.TextField(blank=True, null=True)
    tipo_user = models.CharField(max_length=20, default='Cliente')
    contatowspp = models.CharField(max_length=20, blank=True, null=True)

    def __str__(self):
        return self.user.username


class UserEndereco(models.Model):
    user = models.OneToOneField(
        User,
        on_delete=models.CASCADE,
        related_name='endereco',
        null=True,
        blank=True
    )
    cep = models.CharField(max_length=20, blank=True, null=True)
    rua = models.CharField(max_length=100, blank=True, null=True)
    numero = models.CharField(max_length=20, blank=True, null=True)
    complemento = models.CharField(max_length=100, blank=True, null=True)
    bairro = models.CharField(max_length=100, blank=True, null=True)
    cidade = models.CharField(max_length=100, blank=True, null=True)
    estado = models.CharField(max_length=100, blank=True, null=True)

    def __str__(self):
        return f"{self.rua}, {self.numero} - {self.cidade}/{self.estado}"