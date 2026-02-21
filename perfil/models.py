from django.contrib.auth.models import User
from django.db import models
from cloudinary.models import CloudinaryField

class Perfil(models.Model):
    user = models.ForeignKey(
    User,
    on_delete=models.CASCADE,
    null=True,
    blank=True
)
    fotodeperfil = CloudinaryField('foto de perfil', null=True, blank=True)
    bio = models.TextField(blank=True, null=True)

    def __str__(self):
        return self.user.username

def vitrine(request):
    produtos_do_usuario = CadItmModel.objects.filter(autor=request.user)
    return produtos_do_usuario
