from django.urls import path
from . import views

app_name="nm_catalog"

urlpatterns = [
<<<<<<< HEAD
    path ('', views.nm_catalog, name='/'),
=======
    path ('', views.naturemarket_home, name='home'),
>>>>>>> 8d2058ca414dee02c77770564705a0607d0ec55e
]