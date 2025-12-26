from django.urls import include, path
from django.contrib import admin
from . import views

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include('nm_catalog.urls')),
    path('login/', include("login.urls")),
    path('cadastrar_produto/', include('cadastro_item.urls')),
    path('produto/', include('produto.urls')),
]
