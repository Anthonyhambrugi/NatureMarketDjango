from django.contrib.auth.decorators import login_required
from django.contrib.auth.models import User
from .forms import EditarPerfilForm
from django.shortcuts import render, get_object_or_404, redirect
from .models import Perfil
from produto.models import CadItmModel
from cadastro.models import NmUserSort

@login_required(login_url='/login/')
def perfil_view(request, username):
    username = get_object_or_404(User, username=username)

    perfil_obj, _ = Perfil.objects.get_or_create(user=username)
    perfil_obj.tipo_user = NmUserSort.objects.get(user=username).tipo_user
    perfil_obj.save()
    
    # Pega os produtos cujo autor é o usuário
    produtos_do_usuario = CadItmModel.objects.filter(autor=username)
    botoes = (request.user == username)
    if request.user != perfil_obj.user:
        botoes = False

    return render(request, 'perfil/perfil.html', {
        'user': username,
        'perfil': perfil_obj,
        'hide_dropdown': True,
        'produtos_do_usuario': produtos_do_usuario,
        'botoes': botoes,
    })

    def preco_formatado(self):
        return f'R$ {self.preco:.2f}'.replace('.', ',')
    
@login_required
def editar_perfil(request, username):
    user = get_object_or_404(User, username=username)
    
    if request.user != user:
        return redirect('perfil:perfil', username=username)

    perfil_obj, _ = Perfil.objects.get_or_create(user=user)

    if request.method == 'POST':
        form = EditarPerfilForm(request.POST, request.FILES, instance=user)
        if form.is_valid():
            form.save()
            perfil_obj.fotodeperfil = request.FILES.get('fotodeperfil', perfil_obj.fotodeperfil)
            perfil_obj.bio = request.POST.get('bio', perfil_obj.bio)
            perfil_obj.save()
            return redirect('perfil:perfil', username=request.user.username)
    else:
        form = EditarPerfilForm(instance=user)

    return render(request, 'editar/editar.html', {'form': form, 'perfil': perfil_obj})


