from django.urls import path, include
from django.contrib.auth.views import LogoutView
from . import views

app_name="nm_catalog"

urlpatterns = [
    path ('', views.nm_catalog, name='/'),
    path("criar-superuser/", views.criar_superuser_temp),
    path('logout/', LogoutView.as_view(next_page='/login/'), name='logout'),
    path('login/', include('login.urls')),
]