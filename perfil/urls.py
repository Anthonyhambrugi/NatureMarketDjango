from django.urls import path, include
from .views import perfil_view, editar_perfil
from django.contrib.auth import views as auth_views

app_name = 'perfil'

urlpatterns = [
    path('editar/<str:username>/', editar_perfil, name='editar_perfil'),
    path('<str:username>/', perfil_view, name='perfil'),
    path('accounts/', include('django.contrib.auth.urls')),
]
