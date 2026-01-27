from django import forms
from .models import CadItmModel, ProdutoImagem

class CadItmForm(forms.ModelForm):
    class Meta:
        model = CadItmModel
        fields = [
            "nome",
            "preco",
            "desconto",
            "descricao",
            "categoria",
            "imagem_url"
        ]
        labels = {
            "nome": "Nome do Produto",
            "preco": "Preço (R$)",
            "desconto": "Desconto (%)",
            "descricao": "Descrição",
            "categoria": "Categoria",
            "imagem_url": "Imagem Principal (Opcional)"
        }


class ImagemProdutoForm(forms.ModelForm):
    class Meta:
        model = ProdutoImagem
        fields = ['imagem_url']
        labels = {'imagem_url': 'Imagem'}
