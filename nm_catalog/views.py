from django.shortcuts import render
from produto.models import CadItmModel

def nm_catalog(request):
    produtos = CadItmModel.objects.all()

    return render(request, 'naturemarket/NMhome.html', {'produtos': produtos})