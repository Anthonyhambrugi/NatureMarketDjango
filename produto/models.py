from django.db import models
from django.contrib.auth.models import User
from cloudinary.models import CloudinaryField
from cadastro.models import UserMod, UserEndereco


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
    autor = models.ForeignKey(User, on_delete=models.CASCADE)
    contato = models.CharField(max_length=20, blank=True, null=True)
    preco = models.FloatField(default=0.0)
    desconto = models.FloatField(default=0.0)
    categoria = models.CharField(max_length=50, blank=True, null=True)

    imagem_item = CloudinaryField('imagem_principal', null=True, blank=True)

    criado_em = models.DateTimeField(auto_now_add=True)

    id = models.AutoField(primary_key=True)

    CADASTRO_CHOICES = [
        ('Fruta', 'Fruta'),
        ('Verdura', 'Verdura'),
        ('Legume', 'Legume'),
        ('Grãos', 'Grãos'),
        ('Cereais', 'Cereais'),
        ('Reciclados', 'Reciclados'),
        ('Outros', 'Outros'),
    ]



    def __str__(self):
        return self.nome
    
    def get_preco_formatado(self):
        return f"R$ {self.preco:.2f}"
    
    def preco_com_desconto(self):
        """Calcula o preço com desconto aplicado"""
        if self.desconto > 0:
            return self.preco * (1 - self.desconto / 100)
        return self.preco
    
    def eh_do_usuario(self, usuario):
        """Verifica se o produto pertence ao usuário"""
        if usuario.is_authenticated:
            return self.autor == usuario
        return False

class ImagemProduto(models.Model):
    produto = models.ForeignKey(
        CadItmModel,
        on_delete=models.CASCADE,
        related_name='imagens'
    )
    imagem = CloudinaryField('imagem')
    criada_em = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"Imagem de {self.produto.nome}"

    class Meta:
        ordering = ['-criada_em']