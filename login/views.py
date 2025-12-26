from django.shortcuts import render, redirect
from django.http import HttpRequest
from .forms import LoginForm

def naturemarket_login(request: HttpRequest):
    if request.method == 'POST':
        form = LoginForm(request.POST)
        if form.is_valid():
            username = form.cleaned_data['username']
            password = form.cleaned_data['password']

            # aqui depois tu pode usar authenticate/login
            # por enquanto só redireciona
            return redirect('/')
    else:
        form = LoginForm()

    return render(request, 'login/login.html', {
        'form': form
    })