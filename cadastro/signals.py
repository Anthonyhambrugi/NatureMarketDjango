from django.db.models.signals import post_migrate, post_save
from django.dispatch import receiver
from django.contrib.auth.models import Group, Permission, User
from django.contrib.contenttypes.models import ContentType

from produto.models import CadItmModel, ImagemProduto


# -----------------------------
# CRIA GRUPOS E PERMISSÕES
# -----------------------------
@receiver(post_migrate)
def criar_grupos(sender, **kwargs):
    ct_produto = ContentType.objects.get_for_model(CadItmModel)
    ct_imagem = ContentType.objects.get_for_model(ImagemProduto)

    # criar grupos fixos
    vendedor, _ = Group.objects.get_or_create(name="Vendedor")
    cliente, _ = Group.objects.get_or_create(name="Cliente")
    anonimo, _ = Group.objects.get_or_create(name="Anônimo")

    # permissões para vendedor
    permissoes_vendedor = Permission.objects.filter(
        content_type__in=[ct_produto, ct_imagem],
        codename__in=['add_caditmmodel', 'change_caditmmodel', 'delete_caditmmodel',
                      'add_imagemproduto', 'change_imagemproduto', 'delete_imagemproduto']
    )
    vendedor.permissions.set(permissoes_vendedor)
    vendedor.save()

    permissoes_cliente = Permission.objects.filter(
        content_type__in=[ct_produto, ct_imagem],
        codename__in=['view_caditmmodel', 'view_imagemproduto']
        
    )
    cliente.permissions.set(permissoes_cliente)
    cliente.save()

    permissoes_anonimo = Permission.objects.filter(
        content_type__in=[ct_produto, ct_imagem],
        codename__in=['view_caditmmodel', 'view_imagemproduto']
    )
    anonimo.permissions.set(permissoes_anonimo)
    anonimo.save()


# -----------------------------
# USUÁRIO NOVO → GRUPO CLIENTE OU OUTRO
# -----------------------------
@receiver(post_save, sender=User)
def adicionar_usuario_ao_grupo(sender, instance, created, **kwargs):
    group = instance.nmusersort.tipo_user if hasattr(instance, 'nmusersort') else 'Anônimo'
    grupo, _ = Group.objects.get_or_create(name=group)

# Supondo que seu modelo de perfil se chame NmUserSort
from .models import NmUserSort 

@receiver(post_save, sender=NmUserSort)
def vincular_grupo_pelo_perfil(sender, instance, created, **kwargs):
    if created:
        # 1. Pegamos o tipo_user direto da instância do perfil que acabou de ser salva
        nome_grupo = instance.tipo_user or 'Cliente'
        
        # 2. Buscamos o grupo no banco
        grupo, _ = Group.objects.get_or_create(name=nome_grupo)
        
        # 3. Adicionamos o grupo ao USUÁRIO vinculado a esse perfil
        # (instance.user é a FK ou OneToOne para o User)
        instance.user.groups.add(grupo)

@receiver(post_save, sender=NmUserSort)
def atualizar_grupo_usuario(sender, instance, **kwargs):
    
    # Adiciona o novo grupo baseado no cargo atual
    grupo, _ = Group.objects.get_or_create(name=instance.tipo_user)
    instance.user.groups.add(grupo)