from django.contrib.auth.decorators import login_required
from django.contrib.auth.models import User
from .forms import EditarPerfilForm
from django.shortcuts import render, get_object_or_404, redirect
from .models import Perfil

@login_required(login_url='/login/')
def perfil_view(request, username):
    username = get_object_or_404(User, username=username)

    perfil_obj, _ = Perfil.objects.get_or_create(user=username)

    return render(request, 'perfil/perfil.html', {
        'user': username,
        'perfil': perfil_obj
    })
    
@login_required
def editar_perfil(request):
    user = request.username

    if request.method == 'POST':
        form = EditarPerfilForm(request.POST, instance=user)
        if form.is_valid():
            form.save()
            return redirect('perfil:perfil', username=request.user.username)
    else:
        form = EditarPerfilForm(instance=user)

    return render(request, 'editar/editar.html', {'form': form})
