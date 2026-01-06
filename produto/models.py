from django.db import models
from django.contrib.auth.models import User


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
        
class CadItmModel(models.Model):
    nome = models.CharField(max_length=25)
    descricao = models.TextField(default='Descrição do item')
    autor = models.ForeignKey(User, on_delete=models.CASCADE, null=False, blank=False)
    preco = models.FloatField(default=0.0)
    imagem_item = models.ImageField(upload_to='produto/imagens', null=True, blank=True)
    def __str__(self):
        return self.nome
    
    def get_preco_formatado(self):
        return f"R$ {self.preco:.2f}"