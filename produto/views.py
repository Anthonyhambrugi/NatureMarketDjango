from django.contrib.auth.decorators import login_required
from django.shortcuts import render, get_object_or_404, redirect
from .forms import CadItmForm
from produto.models import CadItmModel, ProdutoImagem

def detalhes_produto(request, id):
    produto = get_object_or_404(CadItmModel, id=id)
    imagens = produto.imagens.all()
    return render(request, 'produto/detalhes.html', {
        'produto': produto,
        'imagens': imagens,
        'eh_produto_proprio': produto.eh_do_usuario(request.user)
    })

@login_required
def cadastro_produto (request):
    if request.method == 'POST':
        form = CadItmForm (request.POST, request.FILES)
        if form.is_valid():
            produto = form.save(commit=False)
            produto.autor = request.user
            produto = form.save()

        for url in request.POST.getlist("imagens_urls[]"):
            ProdutoImagem.objects.create(
                produto=produto,
                imagem_url=url
            )
            return redirect ('detalhes_produto', id=produto.id)

    else:
        form = CadItmForm ()

    return render (request, 'cadastro_item/cadastro_item.html', {'form': form})

def criar_produto(request):
    if request.method == "POST":
        Produto.objects.create(
            nome=request.POST["nome"],
            preco=request.POST["preco"],
            desconto=request.POST.get("desconto", 0),
            descricao=request.POST["descricao"],
            categoria=request.POST["categoria"],
            imagem_url=request.POST.get("imagem_url"),
            autor=request.user
        )
        return redirect("/")
