from django.shortcuts import render, redirect
from django.http import HttpRequest
from .forms import LoginForm
from .models import LoginModel

# Create your views here.
def naturemarket_login (request:HttpRequest):
    nome = None
    sbrnom = None
    if request.method == 'POST':
        form=LoginForm(request.POST)
        if form.is_valid():
            login = form.save()
            request.session['nome'] = login.nome
            request.session['sbrnom'] = login.sbrnom
            return redirect('/')
    else: 
        form = LoginForm()
    formulario = {
            'form': form,
            'nome': nome,
            'sbrnom': sbrnom
        }
    return render (request, 'login/login.html', formulario)