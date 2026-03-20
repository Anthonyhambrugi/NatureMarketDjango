from django.contrib.auth import login as auth_login
from django.shortcuts import render, redirect
from .forms import CadastroForm, UserEnderecoForm, NmUserSortForm, UserModForm
from cadastro.models import NmUserSort, UserMod, UserEndereco


def cadastro(request):
    if request.method == 'POST':
        formuser = CadastroForm(request.POST)
        formcargo = NmUserSortForm(request.POST)
        formwspp = UserModForm(request.POST)

        if formuser.is_valid() and formcargo.is_valid() and formwspp.is_valid():
            user = formuser.save()

            nm_user_sort = formcargo.save(commit=False)
            nm_user_sort.user = user
            nm_user_sort.save()

            # 🔒 Segurança: nunca duplica
            user_mod, created = UserMod.objects.get_or_create(
                user=user,
                defaults={
                    "tipo_user": nm_user_sort.tipo_user
                }
            )

            # Salva o número formatado no perfil
            if formwspp.cleaned_data.get('contatowspp'):
                user_mod.contatowspp = formwspp.cleaned_data['contatowspp']
                user_mod.save()

            auth_login(request, user)
            return redirect('cadastro:endereco')

    else:
        formuser = CadastroForm()
        formcargo = NmUserSortForm()
        formwspp = UserModForm()

    return render(request, 'cadastro/cadastro.html', {
        'form': formuser,
        'form2': formcargo,
        'formwspp': formwspp,
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