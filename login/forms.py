from django import forms
from .models import LoginModel

class LoginForm (forms.ModelForm):
    class Meta:
        model = LoginModel
        fields = ['nome', 'sbrnom', 'username', 'senha']
        widgets = {
            'nome': forms.TextInput(attrs={'class': 'nome'}),
            'sbrnom': forms.TextInput(attrs={'class': 'sbrnom'}),
            'username': forms.TextInput(attrs={'class': 'username'}),
            'senha': forms.PasswordInput(attrs={'class': 'senha'}),
        }