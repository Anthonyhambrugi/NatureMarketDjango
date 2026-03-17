from django.contrib.auth import login as auth_login
from django.shortcuts import render, redirect
from .forms import CadastroForm, UserEnderecoForm, NmUserSortForm
from cadastro.models import NmUserSort, UserMod, UserEndereco


def cadastro(request):
    if request.method == 'POST':
        form = CadastroForm(request.POST)
        form2 = NmUserSortForm(request.POST)

        if form.is_valid() and form2.is_valid():
            user = form.save()

            nm_user_sort = form2.save(commit=False)
            nm_user_sort.user = user
            nm_user_sort.save()

            # 🔒 Segurança: nunca duplica
            user_mod, created = UserMod.objects.get_or_create(
                user=user,
                defaults={
                    "tipo_user": nm_user_sort.tipo_user
                }
            )

            auth_login(request, user)
            return redirect('cadastro:endereco')

    else:
        form = CadastroForm()
        form2 = NmUserSortForm()

    return render(request, 'cadastro/cadastro.html', {
        'form': form,
        'form2': form2,
        'passo_cadastro': 1
    })

def endereco(request):
    endereco_obj = UserEndereco.objects.filter(user=request.user).first()

    if request.method == 'POST':
        form = UserEnderecoForm(request.POST, instance=endereco_obj)

        if form.is_valid():
            endereco = form.save(commit=False)
            endereco.user = request.user
            endereco.save()

            if request.META.get('HTTP_REFERER') and "/carrinho" in request.META.get('HTTP_REFERER'):
                return redirect('carrinho:visualizar_carrinho')
            else:
                return redirect('perfil:editar_perfil', username=request.user.username)

    else:
        form = UserEnderecoForm(instance=endereco_obj)

    return render(request, 'cadastro/endereco.html', {
        'form': form,
        'endereco': endereco_obj,
        'passo_cadastro': 2,
    })