from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth.decorators import login_required
from django.contrib import messages
from django.http import JsonResponse
from django.views.decorators.http import require_POST
from decimal import Decimal

from .models import Carrinho, ItemCarrinho
from produto.models import CadItmModel
from .forms import QuantidadeForm


@login_required
def visualizar_carrinho(request):
    """Exibe o carrinho do usuário"""
    try:
        carrinho = Carrinho.objects.get(usuario=request.user)
    except Carrinho.DoesNotExist:
        carrinho = Carrinho.objects.create(usuario=request.user)
    
    itens = carrinho.itens.all()
    context = {
        'carrinho': carrinho,
        'itens': itens,
        'total_itens': carrinho.total_itens,
        'valor_total': carrinho.valor_total,
    }
    return render(request, 'carrinho/carrinho.html', context)


@login_required
@require_POST
def adicionar_ao_carrinho(request, produto_id):
    """Adiciona um produto ao carrinho"""
    produto = get_object_or_404(CadItmModel, id=produto_id)
    quantidade = int(request.POST.get('quantidade', 1))

    try:
        carrinho = Carrinho.objects.get(usuario=request.user)
    except Carrinho.DoesNotExist:
        carrinho = Carrinho.objects.create(usuario=request.user)

    # Verifica se o item já está no carrinho
    item, criado = ItemCarrinho.objects.get_or_create(
        carrinho=carrinho,
        produto=produto,
        defaults={'preco_unitario': produto.preco, 'quantidade': quantidade}
    )

    if not criado:
        # Se o item já existe, aumenta a quantidade
        item.quantidade += quantidade
        item.save()

    messages.success(request, f'{produto.nome} adicionado ao carrinho!')
    
    # Se for uma requisição AJAX, retorna JSON
    if request.headers.get('X-Requested-With') == 'XMLHttpRequest':
        return JsonResponse({
            'sucesso': True,
            'mensagem': f'{produto.nome} adicionado ao carrinho!',
            'total_itens': carrinho.total_itens,
            'valor_total': str(carrinho.valor_total)
        })

    return redirect('carrinho:visualizar_carrinho')


@login_required
@require_POST
def remover_do_carrinho(request, item_id):
    """Remove um item do carrinho"""
    item = get_object_or_404(ItemCarrinho, id=item_id, carrinho__usuario=request.user)
    produto_nome = item.produto.nome
    carrinho = item.carrinho

    item.delete()
    messages.success(request, f'{produto_nome} removido do carrinho!')

    if request.headers.get('X-Requested-With') == 'XMLHttpRequest':
        return JsonResponse({
            'sucesso': True,
            'mensagem': f'{produto_nome} removido do carrinho!',
            'total_itens': carrinho.total_itens,
            'valor_total': str(carrinho.valor_total)
        })

    return redirect('carrinho:visualizar_carrinho')


@login_required
@require_POST
def atualizar_quantidade(request, item_id):
    """Atualiza a quantidade de um item no carrinho"""
    item = get_object_or_404(ItemCarrinho, id=item_id, carrinho__usuario=request.user)
    quantidade = int(request.POST.get('quantidade', 1))

    if quantidade <= 0:
        item.delete()
        return redirect('carrinho:visualizar_carrinho')

    item.quantidade = quantidade
    item.save()

    messages.success(request, 'Quantidade atualizada!')

    if request.headers.get('X-Requested-With') == 'XMLHttpRequest':
        return JsonResponse({
            'sucesso': True,
            'mensagem': 'Quantidade atualizada!',
            'subtotal': str(item.subtotal),
            'valor_total': str(item.carrinho.valor_total)
        })

    return redirect('carrinho:visualizar_carrinho')


@login_required
@require_POST
def limpar_carrinho(request):
    """Limpa todos os itens do carrinho"""
    try:
        carrinho = Carrinho.objects.get(usuario=request.user)
        carrinho.itens.all().delete()
        messages.success(request, 'Carrinho limpo com sucesso!')
    except Carrinho.DoesNotExist:
        messages.info(request, 'Seu carrinho já está vazio.')

    return redirect('carrinho:visualizar_carrinho')


@login_required
def obter_info_carrinho(request):
    """Retorna informações do carrinho em JSON (para requisições AJAX)"""
    try:
        carrinho = Carrinho.objects.get(usuario=request.user)
    except Carrinho.DoesNotExist:
        carrinho = Carrinho.objects.create(usuario=request.user)

    return JsonResponse({
        'total_itens': carrinho.total_itens,
        'valor_total': str(carrinho.valor_total),
        'itens': list(carrinho.itens.values('id', 'produto__nome', 'quantidade', 'preco_unitario', 'subtotal'))
    })
