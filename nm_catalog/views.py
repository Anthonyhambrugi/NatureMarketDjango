from django.shortcuts import render
from produto.models import Produto

def nm_catalog(request):
    produtos = Produto.objects.all()
    return render(request, 'naturemarket/home.html', {'produtos': produtos})
