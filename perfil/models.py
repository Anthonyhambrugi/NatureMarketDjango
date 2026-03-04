from django.contrib.auth.models import User
from django.db import models

def vitrine(request):
    produtos_do_usuario = CadItmModel.objects.filter(autor=request.user)
    return produtos_do_usuario
