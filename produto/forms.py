from django import forms
from .models import CadItmModel, ImagemProduto

class CadItmForm(forms.ModelForm):
    class Meta:
        model = CadItmModel
        fields = ['nome', 'descricao', 'preco', 'desconto', 'imagem_item']
        labels = {
            'nome': 'Nome do Produto',
            'descricao': 'Descrição',
            'preco': 'Preço (R$)',
            'desconto': 'Desconto (%)',
            'imagem_item': 'Imagem Principal (Opcional)'
        }


class ImagemProdutoForm(forms.ModelForm):
    class Meta:
        model = ImagemProduto
        fields = ['imagem']
        labels = {'imagem': 'Imagem'}
