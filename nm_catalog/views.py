from django.shortcuts import render

# Create your views here.
def naturemarket_home (request):
    nome = request.session.get('nome', None)
    sbrnom = request.session.get('sobrenome', None)

    return render(request, 'naturemarket/home.html', {
        'nome': nome,
        'sbrnom': sbrnom
    })