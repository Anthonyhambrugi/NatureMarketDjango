from django.contrib.auth.models import Group
from django.db.models.signals import post_migrate
from django.dispatch import receiver
from django.db.models.signals import post_save
from .models import NmUserSort

@receiver(post_save, sender=NmUserSort)
def adicionar_usuario_ao_grupo(sender, instance, created, **kwargs):
    if created:
        grupo_nome = {
            'Cliente': 'Cliente',
            'Vendedor': 'Vendedor',
            'Administrador': 'Administrador'
        }.get(instance.tipo_user, None)
        if grupo_nome:
            grupo = Group.objects.get(name=grupo_nome)
            grupo.user_set.add(instance.user)