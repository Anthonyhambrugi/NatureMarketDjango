from django.urls import path
from . import views

app_name="nm_catalog"

urlpatterns = [
    path ('', views.naturemarket_home, name='home'),
]