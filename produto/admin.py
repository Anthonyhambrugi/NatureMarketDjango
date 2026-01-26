# app/admin.py
from django.contrib import admin
from .models import CadItmModel, ImagemProduto

class ImagemProdutoInline(admin.TabularInline):
    model = ImagemProduto
    extra = 1
    fields = ['imagem']

@admin.register(CadItmModel)
class CadItmModelAdmin(admin.ModelAdmin):
    list_display = ("nome", "preco")
    search_fields = ("nome", "descricao",)
    list_filter = ("preco",)
    inlines = [ImagemProdutoInline]

@admin.register(ImagemProduto)
class ImagemProdutoAdmin(admin.ModelAdmin):
    list_display = ("produto", "criada_em")
    search_fields = ("produto__nome",)
    list_filter = ("criada_em",)
