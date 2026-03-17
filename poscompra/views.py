from django.shortcuts import render
from django.contrib.auth.decorators import login_required


@login_required
def confirmacao(request):
    """Tela de sucesso exibida após o pedido ser confirmado e o carrinho limpo."""
    wa_url     = request.session.pop('poscompra_wa_url', '')
    itens      = request.session.pop('poscompra_itens', [])
    valor_total = request.session.pop('poscompra_valor_total', '0')

    return render(request, 'poscompra/confirmacao.html', {
        'wa_url': wa_url,
        'itens': itens,
        'valor_total': valor_total,
    })
