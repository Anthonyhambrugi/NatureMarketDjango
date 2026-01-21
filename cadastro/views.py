from django.contrib.auth import login as auth_login
from django.shortcuts import render, redirect
from .forms import CadastroForm


def cadastro(request):
    """
    View pra fazer o cadastro maneiro
    Se vier POST, valida e salva o usuário
    Se não, só mostra o formulário
    """
    if request.method == 'POST':
        form = CadastroForm(request.POST)
        if form.is_valid():
            user = form.save()
            auth_login(request, user)
            return redirect('/')
    else:
        form = CadastroForm()
    return render (request, 'cadastro/cadastro.html', {'form': form})
