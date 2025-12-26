from django.urls import path
<<<<<<< HEAD
from .views import detalhes_produto

urlpatterns = [
    path('detalhes/<int:id>/', detalhes_produto, name='detalhes_produto'),
]
=======
from . import views

app_name="produto"

urlpatterns = [
    path ('', views.produto, name= "produto" ),
]
>>>>>>> 8d2058ca414dee02c77770564705a0607d0ec55e
