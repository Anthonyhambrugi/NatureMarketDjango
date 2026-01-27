from django.shortcuts import render
from django.contrib.auth.models import User
from django.http import HttpResponse
from django.conf import settings
from produto.models import CadItmModel, ImagemProduto
from django.db.models import Q

def nm_catalog(request):
    """View principal do catálogo Nature Market"""
    # Para você - produtos mais recentes e populares
    todos_produtos = CadItmModel.objects.all().order_by('-criado_em')[:8]
    
    # Descontos imperdíveis - produtos com desconto, ordenados por desconto
    produtos_desconto = CadItmModel.objects.filter(desconto__gt=0).order_by('-desconto', '-criado_em')[:8]
    
    # Novidades - produtos mais recentes
    novos_produtos = CadItmModel.objects.all().order_by('-criado_em')[:10]

    return render(request, 'naturemarket/NMhome.html', {
        'produtos': todos_produtos,
        'produtos_desconto': produtos_desconto,
        'novos_produtos': novos_produtos,
    })

def criar_superuser_temp(request):
    if User.objects.filter(is_superuser=True).exists():
        return HttpResponse("Superuser já existe")

    User.objects.create_superuser(
        username="admin",
        email="admin@email.com",
        password="senha_forte_aqui"
    )

    return HttpResponse("Superuser criado com sucesso")