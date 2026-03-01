from django.contrib import admin
from django.urls import include, path
from django.shortcuts import render
from django.conf import settings
from django.conf.urls.static import static
from . import views


def erro_403(request, exception=None):
    return render(request, "403.html", status=403)


# ✅ SEM STRING
handler403 = erro_403


urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include('nm_catalog.urls')),
    path('login/', include("login.urls")),
    path('cadastro/', include("cadastro.urls")),
    path('produto/', include('produto.urls')),
    path('perfil/', include('perfil.urls')),
    path('carrinho/', include('carrinho_chatgpt.urls')),
    path("teste/", views.teste_template, name="teste_template"),
]

if settings.DEBUG:
    urlpatterns += static(
        settings.MEDIA_URL,
        document_root=settings.MEDIA_ROOT
    )