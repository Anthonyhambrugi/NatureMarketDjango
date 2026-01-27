from django.shortcuts import render
from produto.models import CadItmModel, ProdutoImagem
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