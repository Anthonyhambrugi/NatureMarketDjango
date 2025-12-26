from django.urls import path
from .views import detalhes_produto

urlpatterns = [
    path('detalhes/<int:id>/', detalhes_produto, name='detalhes_produto'),
]
