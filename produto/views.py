from django.contrib.auth.decorators import login_required
from django.shortcuts import render, get_object_or_404, redirect
from .forms import CadItmForm
from produto.models import CadItmModel

def detalhes_produto(request, id):
    produto = get_object_or_404(CadItmModel, id=id)
    return render(request, 'produto/detalhes.html', {
        'produto': produto
    })

@login_required
def cadastro_produto (request):
    if request.method == 'POST':
        form = CadItmForm (request.POST, request.FILES)
        if form.is_valid():
            produto = form.save(commit=False)
            produto.autor = request.user
            produto.save()
            return redirect ('/')
    else:
        form = CadItmForm ()

    return render (request, 'cadastro_item/cadastro_item.html', {'form': form})