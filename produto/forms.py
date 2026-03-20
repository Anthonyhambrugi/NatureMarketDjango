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
            "imagem_item",
            "categoria",
        ]
        widgets = {
            'nome': forms.TextInput(attrs={'class': 'form-control'}),
            'preco': forms.NumberInput(attrs={'class': 'form-control'}),
            'desconto': forms.NumberInput(attrs={'class': 'form-control'}),
            'descricao': forms.Textarea(attrs={'class': 'form-control', 'rows': 3}),
            'categoria': forms.TextInput(attrs={
                'class': 'form-control',
                'list': 'datalistOptions',  # Conecta ao DataList no HTML
                'placeholder': 'Selecione ou digite uma categoria...'
            }),
        }
        labels = {
            "nome": "Nome do Produto",
            "preco": "Preço (R$)",
            "desconto": "Desconto (%)",
            "descricao": "Descrição",
            "imagem_item": "Imagem Principal",
            "categoria": "Categoria",
        }

    def clean_categoria(self):
        categoria = self.cleaned_data.get('categoria')
        if categoria:
            # Remove espaços extras e coloca em formato Título (Ex: "fruta " vira "Fruta")
            return categoria.strip().title()
        return categoria


class ImagemProdutoForm(forms.ModelForm):
    class Meta:
        model = ImagemProduto
        fields = ['imagem']
        labels = {'imagem': 'Imagem secundária'}