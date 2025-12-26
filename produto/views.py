from django.shortcuts import render, get_object_or_404
from .models import Produto

def detalhes_produto(request, id):
    produto = get_object_or_404(Produto, id=id)
    return render(request, 'produto/detalhes.html', {'produto': produto})