from django.urls import path
from . import views

app_name = 'produto'

urlpatterns = [
    path('detalhes/<int:id>/', views.detalhes_produto, name='detalhes_produto'),
    path('cadastrar-produto', views.cadastro_produto, name='cadastrar_produto'),
    path('editar/<int:id>/', views.editar_produto, name='editar_produto'),
    path('deletar/<int:id>/', views.deletar_produto, name='deletar_produto'),
]
