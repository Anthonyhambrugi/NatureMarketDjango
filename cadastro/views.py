from django.contrib.auth import login as auth_login
from django.shortcuts import render, redirect
from .forms import CadastroForm
from .forms import NmUserSortForm
from django.contrib.auth.models import Group
from cadastro.models import NmUserSort, UserMod

def cadastro(request):
    if request.method == 'POST':
        form = CadastroForm(request.POST)
        form2 = NmUserSortForm(request.POST)

        if form.is_valid() and form2.is_valid():
            user = form.save()
            nm_user_sort = form2.save(commit=False)
            nm_user_sort.user = user
            nm_user_sort.save()
            user_mod = UserMod.objects.create(user=user, tipo_user=nm_user_sort.tipo_user)
            auth_login(request, user)
            return redirect('perfil:editar_perfil', username=user.username)
    else:
        form = CadastroForm()
        form2 = NmUserSortForm()
    return render (request, 'cadastro/cadastro.html', {'form': form, 'form2': form2})
