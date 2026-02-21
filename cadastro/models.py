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
        ('Administrador', 'Administrador'),
    ]
    tipo_user = models.CharField(
        max_length=20,
        choices=TIPO_USER_CHOICES,
        default='Comprador',
    )

    def __str__(self):
        return self.tipo_user
    
    def cadastro_usuario(self):
        try:
            if self.tipo_user == 'Cliente':
                grupo = Group.objects.get(name='Cliente')
            elif self.tipo_user == 'Vendedor':
                grupo = Group.objects.get(name='Vendedor')
            elif self.tipo_user == 'Administrador':
                grupo = Group.objects.get(name='Administrador')
            else:
                return  # não adiciona se não for nenhum
            grupo.user_set.add(self.user)
        except Group.DoesNotExist:
            print(f'O grupo {self.tipo_user} não existe.')
        