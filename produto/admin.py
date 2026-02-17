# app/admin.py
from django.contrib import admin
from .models import CadItmModel, ImagemProduto

class ImagemProdutoInline(admin.TabularInline):
    model = ImagemProduto
    extra = 1

@admin.register(CadItmModel)
class CadItmModelAdmin(admin.ModelAdmin):
    list_display = ("nome", "preco")
    search_fields = ("nome", "descricao",)
    list_filter = ("preco",)
    ordering = ("-criado_em",)
    inlines = [ImagemProdutoInline]
