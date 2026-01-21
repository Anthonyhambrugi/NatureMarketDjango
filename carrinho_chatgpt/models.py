from django.db import models
from django.contrib.auth.models import User
from produto.models import CadItmModel


class Carrinho(models.Model):
    usuario = models.OneToOneField(User, on_delete=models.CASCADE, related_name='carrinho')
    criado_em = models.DateTimeField(auto_now_add=True)
    atualizado_em = models.DateTimeField(auto_now=True)
    ativo = models.BooleanField(default=True)

    class Meta:
        verbose_name = 'Carrinho'
        verbose_name_plural = 'Carrinhos'

    def __str__(self):
        return f"Carrinho de {self.usuario.username}"

    @property
    def total_itens(self):
        """Retorna a quantidade total de itens no carrinho"""
        return sum(item.quantidade for item in self.itens.all())

    @property
    def valor_total(self):
        """Retorna o valor total do carrinho"""
        return sum(item.subtotal for item in self.itens.all())


class ItemCarrinho(models.Model):
    carrinho = models.ForeignKey(Carrinho, on_delete=models.CASCADE, related_name='itens')
    produto = models.ForeignKey(CadItmModel, on_delete=models.CASCADE)
    quantidade = models.PositiveIntegerField(default=1)
    preco_unitario = models.DecimalField(max_digits=10, decimal_places=2)
    criado_em = models.DateTimeField(auto_now_add=True)
    atualizado_em = models.DateTimeField(auto_now=True)

    class Meta:
        verbose_name = 'Item do Carrinho'
        verbose_name_plural = 'Itens do Carrinho'
        unique_together = ['carrinho', 'produto']

    def __str__(self):
        return f"{self.quantidade}x {self.produto.nome} - {self.carrinho.usuario.username}"

    @property
    def subtotal(self):
        """Calcula o subtotal do item"""
        return self.preco_unitario * self.quantidade
