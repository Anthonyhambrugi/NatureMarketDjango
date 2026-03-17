from django.urls import path
from . import views

app_name = 'poscompra'

urlpatterns = [
    path('confirmacao/', views.confirmacao, name='confirmacao'),
]
