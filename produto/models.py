# produto/models.py
from django.db import models

class Produto(models.Model):
    imagem = models.ImageField(
    upload_to='produtos/',
    blank=True,
    null=True)
    nome = models.CharField(max_length=100)
    preco = models.DecimalField(max_digits=10, decimal_places=2)
    descricao = models.TextField()

    def __str__(self):
        return self.nome

    def get_preco_formatado(self):
        return f"R$ {self.preco:.2f}"
