from django import forms
from .models import CadItmModel, ImagemProduto

class CadItmForm(forms.ModelForm):
    class Meta:
        model = CadItmModel
        fields = [
            "nome",
            "preco",
            "desconto",
            "descricao",
            "imagem_item"
        ]
        labels = {
            "nome": "Nome do Produto",
            "preco": "Preço (R$)",
            "desconto": "Desconto (%)",
            "descricao": "Descrição",
            "imagem_item": "Imagem Principal (Opcional)"
        }


class ImagemProdutoForm(forms.ModelForm):
    class Meta:
        model = ImagemProduto
        fields = ['imagem']
        labels = {'imagem': 'Imagem'}