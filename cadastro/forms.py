from django import forms
from django.contrib.auth.models import User
from django.contrib.auth.forms import UserCreationForm
from cadastro.models import NmUserSort, UserEndereco, UserMod

class CadastroForm (UserCreationForm):
    email = forms.EmailField(required=True)

    class Meta:
        model = User
        fields = ['username', 'password1', 'password2']
        
    def clean_username(self):
        username = self.cleaned_data.get('username')
        if not username.startswith('@'):
            raise forms.ValidationError (
                'O nome de usuário deve ter um @ no começo'
            )
        return username
    
    def clean_password(self):
        password = self.cleaned_data.get('password')
        if len(password) < 8:
            raise forms.ValidationError (
                'A senha deve ter no mínimo 8 dígitos'
            )
        return password

class NmUserSortForm(forms.ModelForm):
    class Meta:
        model = NmUserSort
        fields = ['tipo_user']
        widgets = {
            'tipo_user': forms.Select(attrs={'class': 'form-select'})
        }
        labels = {
            'tipo_user': 'Tipo de usuário',
        }

class UserModForm(forms.ModelForm):
    class Meta:
        model = UserMod
        fields = ['contatowspp']
        widgets = {
            'contatowspp': forms.TextInput(attrs={'class': 'form-control'})
        }
        labels = {
            'contatowspp': 'Contato WhatsApp (opcional)',
        }

    def clean_contatowspp(self):
        numero = self.cleaned_data.get('contatowspp')
        if not numero:
            return numero
        numeros = ''.join(filter(str.isdigit, numero))
        
        # Se o JavaScript enviou com 55 (13 dígitos), removemos o 55 para padronizar a validação
        if len(numeros) == 13 and numeros.startswith('55'):
            numeros = numeros[2:]
            
        if len(numeros) == 11:
            return f"+55 ({numeros[:2]}) {numeros[2:7]}-{numeros[7:]}"
        return numero

class UserEnderecoForm(forms.ModelForm):
    class Meta:
        model = UserEndereco
        fields = ['cep', 'rua', 'numero', 'complemento', 'bairro', 'cidade', 'estado']
        widgets = {
            'cep': forms.TextInput(attrs={'class': 'form-control', 'required': True}),
            'rua': forms.TextInput(attrs={'class': 'form-control', 'required': True}),
            'numero': forms.TextInput(attrs={'class': 'form-control', 'required': True}),
            'complemento': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Ex.: Fica perto de um mercado'}),
            'bairro': forms.TextInput(attrs={'class': 'form-control', 'required': True}),
            'cidade': forms.TextInput(attrs={'class': 'form-control', 'required': True}),
            'estado': forms.TextInput(attrs={'class': 'form-control', 'required': True}),
        }
    labels = {
        'cep': 'CEP',
        'rua': 'Rua',
        'numero': 'Número',
        'complemento': 'Complemento',
        'bairro': 'Bairro',
        'cidade': 'Cidade',
        'estado': 'Estado',
    }