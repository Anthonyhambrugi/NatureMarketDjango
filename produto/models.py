from django.db import models
from django.contrib.auth.models import User


class CadItmModel(models.Model):
    nome = models.CharField(max_length=100)
    preco = models.DecimalField(max_digits=10, decimal_places=2)
    descricao = models.TextField()

    desconto = models.DecimalField(
        max_digits=5,
        decimal_places=2,
        default=0
    )

    categoria = models.CharField(max_length=50, null=True, blank=True)

    imagem_url = models.URLField(blank=True, null=True)

    autor = models.ForeignKey(User, on_delete=models.CASCADE)
    criado_em = models.DateTimeField(auto_now_add=True)
    eh_do_usuario = lambda self, user: self.autor == user


class ProdutoImagem(models.Model):
    produto = models.ForeignKey(
        CadItmModel,
        related_name="imagens",
        on_delete=models.CASCADE
    )
    imagem_url = models.URLField()
    criada_em = models.DateTimeField(auto_now_add=True)
    def __str__(self):
        return f"Imagem do produto {self.produto.nome} - {self.imagem_url}"