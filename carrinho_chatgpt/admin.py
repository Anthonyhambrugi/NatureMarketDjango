from django.contrib import admin
from .models import Carrinho, ItemCarrinho


@admin.register(Carrinho)
class CarrinhoAdmin(admin.ModelAdmin):
    list_display = ['id', 'usuario', 'criado_em', 'atualizado_em', 'ativo']
    list_filter = ['ativo', 'criado_em']
    search_fields = ['usuario__username']
    readonly_fields = ['criado_em', 'atualizado_em']


@admin.register(ItemCarrinho)
class ItemCarrinhoAdmin(admin.ModelAdmin):
    list_display = ['id', 'carrinho', 'produto', 'quantidade', 'preco_unitario']
    list_filter = ['carrinho__ativo']
    search_fields = ['produto__nome', 'carrinho__usuario__username']
    readonly_fields = ['criado_em']
