from django.shortcuts import render
from produto.models import CadItmModel
from django.db.models import Q

def nm_catalog(request):
    """View principal do catálogo Nature Market"""
    todos_produtos = CadItmModel.objects.all()
    
    produtos_desconto = CadItmModel.objects.all().order_by('preco', '-criado_em')
    
    novos_produtos = CadItmModel.objects.all().order_by('-criado_em')[:10]

    return render(request, 'naturemarket/NMhome.html', {
        'produtos': todos_produtos,
        'produtos_desconto': produtos_desconto,
        'novos_produtos': novos_produtos,
    })