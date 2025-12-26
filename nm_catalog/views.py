from django.shortcuts import render
<<<<<<< HEAD
from produto.models import Produto

def nm_catalog(request):
    produtos = Produto.objects.all()
    return render(request, 'naturemarket\home.html', {'produtos': produtos})
=======

# Create your views here.
def naturemarket_home (request):
    nome = request.session.get('nome', None)
    sbrnom = request.session.get('sobrenome', None)

    return render(request, 'naturemarket/home.html', {
        'nome': nome,
        'sbrnom': sbrnom
    })
>>>>>>> 8d2058ca414dee02c77770564705a0607d0ec55e
