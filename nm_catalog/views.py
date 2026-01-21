from django.shortcuts import render
from produto.models import CadItmModel
from django.db.models import Q

def nm_catalog(request):
    """
    View do catálogo, organiza os produtos em seções
    """
    # Todos os produtos (Para você!)
    todos_produtos = CadItmModel.objects.all()
    
    # Produtos em promoção (desconto > 0)
    produtos_desconto = CadItmModel.objects.filter(desconto__gt=0).order_by('-desconto')
    
    # Novos produtos (últimos adicionados)
    novos_produtos = CadItmModel.objects.all().order_by('-criado_em')[:10]

    return render(request, 'naturemarket/NMhome.html', {
        'produtos': todos_produtos,
        'produtos_desconto': produtos_desconto,
        'novos_produtos': novos_produtos,
    })