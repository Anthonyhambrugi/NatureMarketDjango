from django.shortcuts import render
from django.contrib.auth.models import User
from django.http import HttpResponse
from django.conf import settings
from produto.models import CadItmModel, ImagemProduto
from django.db.models import Q


def nm_catalog(request):
    """View principal do catálogo Nature Market"""
    q             = request.GET.get('q', '').strip()
    preco_min     = request.GET.get('preco_min', '').strip()
    preco_max     = request.GET.get('preco_max', '').strip()
    apenas_desconto = request.GET.get('desconto', '')
    ordem         = request.GET.get('ordem', '-criado_em')

    ordens_validas = ['-criado_em', 'criado_em', 'preco', '-preco']
    if ordem not in ordens_validas:
        ordem = '-criado_em'

    tem_filtro = bool(q or preco_min or preco_max or apenas_desconto)

    contexto_base = {
        'q': q,
        'preco_min': preco_min,
        'preco_max': preco_max,
        'apenas_desconto': apenas_desconto,
        'ordem': ordem,
    }

    if tem_filtro:
        qs = CadItmModel.objects.all()

        if q:
            qs = qs.filter(Q(nome__icontains=q) | Q(descricao__icontains=q))

        if preco_min:
            try:
                qs = qs.filter(preco__gte=float(preco_min))
            except ValueError:
                pass

        if preco_max:
            try:
                qs = qs.filter(preco__lte=float(preco_max))
            except ValueError:
                pass

        if apenas_desconto:
            qs = qs.filter(desconto__gt=0)

        qs = qs.order_by(ordem)

        return render(request, 'naturemarket/NMhome.html', {
            **contexto_base,
            'produtos_filtrados': qs,
            'tem_filtro': True,
        })

    # Layout padrão sem filtros
    todos_produtos   = CadItmModel.objects.all().order_by('-criado_em')[:8]
    produtos_desconto = CadItmModel.objects.filter(desconto__gt=0).order_by('-desconto', '-criado_em')[:8]
    novos_produtos   = CadItmModel.objects.all().order_by('-criado_em')[:10]

    return render(request, 'naturemarket/NMhome.html', {
        **contexto_base,
        'produtos': todos_produtos,
        'produtos_desconto': produtos_desconto,
        'novos_produtos': novos_produtos,
        'tem_filtro': False,
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
