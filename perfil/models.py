from django.contrib.auth.models import User
from django.db import models

class Perfil(models.Model):
    user = models.ForeignKey(
    User,
    on_delete=models.CASCADE,
    null=True,
    blank=True
)
    fotodeperfil = models.ImageField(
        upload_to='perfil/imagens/',
        blank=True,
        null=True
    )
    bio = models.TextField(blank=True, null=True)

    def __str__(self):
        return self.user.username
