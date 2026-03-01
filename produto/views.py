from django.contrib.auth.decorators import login_required
from django.shortcuts import render, get_object_or_404, redirect
from django.core.exceptions import PermissionDenied
from .forms import CadItmForm
from produto.models import CadItmModel, ImagemProduto
from django.contrib.auth.decorators import permission_required

#Permission vem antes, senão da bosta
@permission_required(
    'produto.add_caditmmodel',
    raise_exception=True
)
@login_required
def cadastro_produto(request):
    print(request.user.get_all_permissions())

    if request.user.has_perm('produto.add_caditmmodel'):
        pass
    else:
        raise PermissionDenied("Você não tem permissão para cadastrar produtos.")

    if request.method == 'POST':
        form = CadItmForm(request.POST, request.FILES)

        if form.is_valid():
            produto = form.save(commit=False)
            produto.autor = request.user
            produto.save()

            imagens = request.FILES.getlist("imagens")

            for img in imagens:
                ImagemProduto.objects.create(
                    produto=produto,
                    imagem=img
                )

            return redirect('detalhes_produto', id=produto.id)

    else:
        form = CadItmForm()

    return render(
        request,
        "cadastro_item/cadastro_item.html",
        {"form": form}
    )

def detalhes_produto(request, id):
    produto = get_object_or_404(CadItmModel, id=id)
    imagens = ImagemProduto.objects.filter(produto=produto)

    return render(
        request,
        "cadastro_item/detalhes.html",
        {"produto": produto, "imagens": imagens}
    )