from django.contrib.auth import authenticate, login as auth_login
from django.shortcuts import render, redirect
from .forms import LoginForm, CadastroForm

def login(request):
    if request.method == 'POST':
        form = LoginForm(request.POST)
        if form.is_valid():
            username = form.cleaned_data['username']
            password = form.cleaned_data['password']

            user = authenticate(request, username=username, password=password)

            if user is not None:
                auth_login(request, user)
                return redirect('/')
            else:
                form.add_error(None, 'Credenciais inválidas. Tente novamente.')
    else:
        form = LoginForm()

    return render(request, 'login/login.html', {
        'form': form
    })

def cadastro(request):
    if request.method == 'POST':
        form = CadastroForm(request.POST)
        if form.is_valid():
            user = form.save()
            auth_login(request, user)
            return redirect('/')
    else:
        form = CadastroForm()
    return render (request, 'cadastro/cadastro.html', {'form':form})
