from django.contrib.auth import login as auth_login
from django.shortcuts import render, redirect
from .forms import CadastroForm
from .forms import NmUserSortForm


def cadastro(request):
    """
    View pra fazer o cadastro maneiro
    Se vier POST, valida e salva o usuário
    Se não, só mostra o formulário
    """
    if request.method == 'POST':
        form = CadastroForm(request.POST)
        form2 = NmUserSortForm(request.POST)
        if form.is_valid() and form2.is_valid():
            user = form.save()
            nm_user_sort = form2.save(commit=False)
            nm_user_sort.user = user
            nm_user_sort.save()
            auth_login(request, user)
            return redirect('/')
    else:
        form = CadastroForm()
        form2 = NmUserSortForm()
    return render (request, 'cadastro/cadastro.html', {'form': form, 'form2': form2})
