# app/admin.py
from django.contrib import admin
from .models import CadItmModel

@admin.register(CadItmModel)
class CadItmModelAdmin(admin.ModelAdmin):
    list_display = ("nome", "preco")
    search_fields = ("nome", "descricao",)
    list_filter = ("preco",)
