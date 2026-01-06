from django.urls import path
from . import views

urlpatterns = [
    path('detalhes/<int:id>/', views.detalhes_produto, name='detalhes_produto'),
    path('cadastrar-produto', views.cadastro_produto, name='cadastrar'),
]
