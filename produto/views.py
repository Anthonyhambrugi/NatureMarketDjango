from django.contrib.auth.decorators import login_required, permission_required
from django.shortcuts import render, get_object_or_404, redirect
from django.core.exceptions import PermissionDenied
from django.contrib import messages
from django.views.decorators.http import require_POST
from .forms import CadItmForm
from produto.models import CadItmModel, ImagemProduto


@permission_required('produto.add_caditmmodel', raise_exception=True)
@login_required
def cadastro_produto(request):
    if request.method == 'POST':
        form = CadItmForm(request.POST, request.FILES)
        if form.is_valid():
            produto = form.save(commit=False)
            produto.autor = request.user
            produto.save()

            for img in request.FILES.getlist('imagens'):
                ImagemProduto.objects.create(produto=produto, imagem=img)

            messages.success(request, f'"{produto.nome}" cadastrado com sucesso!')
            return redirect('produto:detalhes_produto', id=produto.id)
    else:
        form = CadItmForm()

    return render(request, 'cadastro_item/cadastro_item.html', {'form': form})


def detalhes_produto(request, id):
    produto = get_object_or_404(CadItmModel, id=id)
    eh_produto_proprio = request.user.is_authenticated and produto.autor == request.user

    return render(request, 'produto/detalhes.html', {
        'produto': produto,
        'eh_produto_proprio': eh_produto_proprio,
    })


@login_required
def editar_produto(request, id):
    produto = get_object_or_404(CadItmModel, id=id)

    if produto.autor != request.user:
        raise PermissionDenied

    if request.method == 'POST':
        form = CadItmForm(request.POST, request.FILES, instance=produto)
        if form.is_valid():
            form.save()
            messages.success(request, 'Produto atualizado!')
            return redirect('produto:detalhes_produto', id=produto.id)
    else:
        form = CadItmForm(instance=produto)

    return render(request, 'produto/editar_produto.html', {'form': form, 'produto': produto})


@login_required
@require_POST
def deletar_produto(request, id):
    produto = get_object_or_404(CadItmModel, id=id)

    if produto.autor != request.user:
        raise PermissionDenied

    nome = produto.nome
    produto.delete()
    messages.success(request, f'"{nome}" foi removido.')
    return redirect('perfil:perfil', username=request.user.username)
