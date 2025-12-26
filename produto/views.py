<<<<<<< HEAD
from django.shortcuts import render, get_object_or_404
from .models import Produto

def detalhes_produto(request, id):
    produto = get_object_or_404(Produto, id=id)
    return render(request, 'produto/detalhes.html', {'produto': produto})
=======
from django.shortcuts import render

# Create your views here.

def produto (request):
    
    return render(request, 'produto/produto.html')
>>>>>>> 8d2058ca414dee02c77770564705a0607d0ec55e
