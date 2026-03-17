import urllib.parse

from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth.decorators import login_required
from django.contrib import messages
from django.http import JsonResponse
from django.views.decorators.http import require_POST

from .models import Carrinho, ItemCarrinho
from cadastro.models import UserEndereco, UserMod
from produto.models import CadItmModel
from .forms import QuantidadeForm


@login_required
def visualizar_carrinho(request):
    try:
        carrinho = Carrinho.objects.get(usuario=request.user)
    except Carrinho.DoesNotExist:
        carrinho = Carrinho.objects.create(usuario=request.user)

    itens = carrinho.itens.all()
    context = {
        'carrinho': carrinho,
        'itens': itens,
        'contatoautor': itens.first().produto.autor.usermod.contatowspp if itens else None,
        'total_itens': carrinho.total_itens,
        'cliente_endereco': UserEndereco.objects.filter(user=request.user).first(),
        'valor_total': carrinho.valor_total,
    }
    return render(request, 'carrinho/carrinho.html', context)


@login_required
@require_POST
def adicionar_ao_carrinho(request, produto_id):
    produto = get_object_or_404(CadItmModel, id=produto_id)
    quantidade = int(request.POST.get('quantidade', 1))

    try:
        carrinho = Carrinho.objects.get(usuario=request.user)
    except Carrinho.DoesNotExist:
        carrinho = Carrinho.objects.create(usuario=request.user)

    item, criado = ItemCarrinho.objects.get_or_create(
        carrinho=carrinho,
        produto=produto,
        defaults={'preco_unitario': produto.preco, 'quantidade': quantidade}
    )

    if not criado:
        item.quantidade += quantidade
        item.save()

    messages.success(request, f'{produto.nome} adicionado ao carrinho!')

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
    try:
        carrinho = Carrinho.objects.get(usuario=request.user)
        carrinho.itens.all().delete()
        messages.success(request, 'Carrinho limpo com sucesso!')
    except Carrinho.DoesNotExist:
        messages.info(request, 'Seu carrinho já está vazio.')

    return redirect('carrinho:visualizar_carrinho')


@login_required
def obter_info_carrinho(request):
    try:
        carrinho = Carrinho.objects.get(usuario=request.user)
    except Carrinho.DoesNotExist:
        carrinho = Carrinho.objects.create(usuario=request.user)

    return JsonResponse({
        'total_itens': carrinho.total_itens,
        'valor_total': str(carrinho.valor_total),
        'itens': list(carrinho.itens.values(
            'id', 'produto__nome', 'quantidade', 'preco_unitario', 'subtotal'
        ))
    })


@login_required
def checkout(request):
    """Tela de revisão do pedido antes de confirmar."""
    endereco_usuario = UserEndereco.objects.filter(user=request.user).first()
    if not endereco_usuario:
        messages.warning(request, 'Cadastre um endereço de entrega antes de finalizar.')
        return redirect('cadastro:endereco')

    try:
        carrinho = Carrinho.objects.get(usuario=request.user)
    except Carrinho.DoesNotExist:
        messages.warning(request, 'Seu carrinho está vazio.')
        return redirect('carrinho:visualizar_carrinho')

    itens = carrinho.itens.select_related('produto__autor__usermod').all()
    if not itens:
        messages.warning(request, 'Seu carrinho está vazio.')
        return redirect('carrinho:visualizar_carrinho')

    # Monta a URL do WhatsApp antecipadamente para o template
    try:
        contato = itens[0].produto.autor.usermod.contatowspp or ''
    except Exception:
        contato = ''

    linhas = '\n'.join(
        f'- {item.produto.nome} (x{item.quantidade}) — R$ {item.subtotal}'
        for item in itens
    )
    msg = (
        f'Olá! Fiz um pedido no Nature Market:\n{linhas}\n\n'
        f'Endereço de entrega:\n'
        f'{endereco_usuario.rua}, {endereco_usuario.numero} - '
        f'{endereco_usuario.bairro}, {endereco_usuario.cidade} - '
        f'{endereco_usuario.estado}, CEP: {endereco_usuario.cep}\n\n'
        f'Total: R$ {carrinho.valor_total}'
    )
    wa_url = f'https://wa.me/{contato}?text={urllib.parse.quote(msg)}' if contato else ''

    return render(request, 'carrinho/comprafinali.html', {
        'endereco': endereco_usuario,
        'carrinho': carrinho,
        'itens': itens,
        'wa_url': wa_url,
    })


@login_required
@require_POST
def confirmar_compra(request):
    """Limpa o carrinho e redireciona para a tela de sucesso."""
    wa_url = request.POST.get('wa_url', '')

    try:
        carrinho = Carrinho.objects.get(usuario=request.user)
        itens = list(carrinho.itens.select_related('produto').all())

        request.session['poscompra_wa_url'] = wa_url
        request.session['poscompra_valor_total'] = str(carrinho.valor_total)
        request.session['poscompra_itens'] = [
            {
                'nome': item.produto.nome,
                'quantidade': item.quantidade,
                'subtotal': str(item.subtotal),
            }
            for item in itens
        ]

        carrinho.itens.all().delete()
    except Carrinho.DoesNotExist:
        pass

    return redirect('poscompra:confirmacao')
