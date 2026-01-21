from django import forms
from .models import ItemCarrinho


class QuantidadeForm(forms.ModelForm):
    quantidade = forms.IntegerField(
        min_value=1,
        widget=forms.NumberInput(attrs={
            'class': 'form-control',
            'style': 'width: 80px;',
            'placeholder': 'Quantidade'
        })
    )

    class Meta:
        model = ItemCarrinho
        fields = ['quantidade']
