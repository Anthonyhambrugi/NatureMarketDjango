from django.contrib import admin
from .models import NmUserSort, UserMod, UserEndereco

@admin.register(NmUserSort)
class NmUserSortAdmin(admin.ModelAdmin):
    list_display = ("user", "tipo_user",)
    search_fields = ("user__username", "tipo_user",)
    list_filter = ("tipo_user",)

@admin.register(UserMod)
class UserModAdmin(admin.ModelAdmin):
    list_display = ("user", "tipo_user", "contatowspp")
    search_fields = ("user__username", "tipo_user", "contatowspp")
    list_filter = ("tipo_user",)

@admin.register(UserEndereco)
class UserEnderecoAdmin(admin.ModelAdmin):
    list_display = ("user", "rua", "numero")
    search_fields = ("user__username", "rua", "numero")
    list_filter = ("cidade", "estado")