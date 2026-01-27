from django.shortcuts import render
from django.contrib.auth.models import User
from django.http import HttpResponse
from django.conf import settings

def index_view(request):
    return render (request, )

def criar_superuser_temp(request):
    # senha simples de segurança via querystring
    if request.GET.get("key") != settings.SECRET_KEY[:10]:
        return HttpResponse("Acesso negado", status=403)

    if User.objects.filter(is_superuser=True).exists():
        return HttpResponse("Superuser já existe")

    User.objects.create_superuser(
        username="antadmin",
        email="anthonyhambrugi@email.com",
        password="admin12341234"
    )

    return HttpResponse("Superuser criado com sucesso")
